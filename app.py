import os, urllib.request, json
import urllib.request, json
from flask import Flask, make_response, request, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, User, City, Price, UserCity, Blog, BlogComment
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nomadic.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.json.compact = False  # configures JSON responses to print on indented lines
app.secret_key = b"\xba\xac\xeb\x94\xcfM\xd1\xba?\xb8s\x91i\x1c\x81u\x89\x900'"

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

# User Authentication


class ClearSession(Resource):
    def delete(self):
        session["page_views"] = None
        session["user_id"] = None

        return {}, 204


api.add_resource(ClearSession, "/clear", endpoint="clear")


class Signup(Resource):
    def post(self):
        request_json = request.get_json()
        username = request_json["username"]
        password = request_json["password"]
        profile_img = request_json["profile_img"]
        email = request_json["email"]
        city = request_json["city"]
        state = request_json["state"]
        zipcode = request_json["zipcode"]
        country = request_json["country"]
        currency_code = request_json["currency_code"]

        new_user = User(
            username=username,
            profile_img=profile_img,
            email=email,
            city=city,
            state=state,
            zipcode=zipcode,
            country=country,
            currency_code=currency_code,
        )
        new_user.password_hash = password
        try:
            db.session.add(new_user)
            db.session.commit()
            session["user_id"] = new_user.id

            return new_user.to_dict(), 201
        except IntegrityError:
            db.session.rollback()
            return {"error": "Username already exists"}, 422

        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)


api.add_resource(Signup, "/signup", endpoint="signup")


class Login(Resource):
    def post(self):
        request_json = request.get_json()
        username = request_json["username"]
        user = User.query.filter(User.username == username).first()
        password = request_json["password"]
        print(user)
        if user:
            if user.authenticate(password):
                session["user_id"] = user.id
                return user.to_dict(rules=("-blogs.comments", "-comments")), 200

        return {"error": "Invalid username or password"}, 401


api.add_resource(Login, "/login", endpoint="login")


class Logout(Resource):
    def delete(self):
        if session.get("user_id"):
            session["user_id"] = None

            return {}, 204

        return {"error": "401 Unauthorized"}, 401


api.add_resource(Logout, "/logout", endpoint="logout")


class CheckSession(Resource):
    def get(self):
        if session.get("user_id"):
            user = User.query.filter(User.id == session["user_id"]).first()
            return user.to_dict(rules=("-blogs.comments", "-comments")), 200

        return {"error": "401 Unauthorized"}, 401


api.add_resource(CheckSession, "/check_session", endpoint="check_session")


# Users
class Users(Resource):
    def get(self):
        users = [
            user.to_dict(rules=("-blogs.comments", "-comments.blog"))
            for user in User.query.all()
        ]

        return make_response(users, 200)


api.add_resource(Users, "/users")


class UserByID(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()

        if user:
            return make_response(
                user.to_dict(rules=("-blogs.comments", "-comments")), 200
            )
        else:
            return make_response({"error": "User not found"}, 404)

    def delete(self, id):
        user = User.query.filter(User.id == id).first()

        if user:
            db.session.delete(user)
            db.session.commit()

            return make_response({}, 204)
        else:
            return make_response({"error": "User not found"}, 404)

    def patch(self, id):
        user = User.query.filter(User.id == id).first()

        if user:
            data = request.get_json()
            try:
                for key in data:
                    if key == "password":
                        user.password_hash = data[key]
                    setattr(user, key, data[key])

                db.session.add(user)
                db.session.commit()

                return make_response(user.to_dict(), 202)
            except IntegrityError:
                db.session.rollback()
                return {"error": "Username already exists"}, 422

        else:
            return make_response({"error": "User not found"}, 404)


api.add_resource(UserByID, "/users/<int:id>")


# Cities
class Cities(Resource):
    def get(self):
        cities = [city.to_dict() for city in City.query.all()]

        return make_response(cities, 200)

    def post(self):
        data = request.get_json()

        new_city = City(
            city_name=data["city_name"],
            state_code=data["state_code"],
            country_name=data["country_name"],
            exchange_rate=data["exchange_rate"],
            currency_code=data["currency_code"],
            img=data["img"],
        )

        db.session.add(new_city)
        db.session.commit()
        return make_response({"message": "success"}, 201)


api.add_resource(Cities, "/cities")


class CityByID(Resource):
    def get(self, id):
        city = City.query.filter(City.id == id).first()

        if city:
            return make_response(city.to_dict(), 200)
        else:
            return make_response({"error": "City not found"}, 404)

    def patch(self, id):
        city = City.query.filter(City.id == id).first()

        if city:
            data = request.get_json()
            for key in data:
                setattr(city, key, data[key])
            db.session.add(city)
            db.session.commit()
            return make_response(city.to_dict(), 202)
        else:
            return make_response({"error": "City not found"}, 404)


api.add_resource(CityByID, "/cities/<int:id>")


# Prices
class Prices(Resource):
    def get(self):
        prices = [price.to_dict() for price in Price.query.all()]

        return make_response(prices, 200)

    def post(self):
        data = request.get_json()

        try:
            new_price = Price(
                city_id=data["city_id"],
                item_name=data["item_name"],
                category_name=data["category_name"],
                avg_usd=data["avg_usd"],
            )

            db.session.add(new_price)
            db.sesison.commit()
            return make_response({"message": "success"}, 201)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)


api.add_resource(Prices, "/prices")


# UserCities
class UserCities(Resource):
    def get(self):
        usercities = [usercity.to_dict() for usercity in UserCity.query.all()]

        return make_response(usercities, 200)

    def post(self):
        data = request.get_json()

        new_uc = UserCity(
            id=data["id"], user_id=data["user_id"], city_id=data["city_id"], rating=0
        )

        db.session.add(new_uc)
        db.session.commit()
        return make_response({"message": "success"}, 201)


api.add_resource(UserCities, "/usercities")


class UserCityByID(Resource):
    def patch(self, id):
        uc = UserCity.query.filter(UserCity.id == id).first()

        if uc:
            data = request.get_json()
            for key in data:
                setattr(uc, key, data[key])
            db.session.add(uc)
            db.session.commit()
            return make_response(uc.to_dict, 204)
        else:
            return make_response({"error": "Not found"}, 404)

    def delete(self, id):
        uc = UserCity.query.filter(UserCity.id == id).first()

        if uc:
            db.session.delete(uc)
            db.session.commit()

            return make_response({}, 204)
        else:
            return make_response({"error": "Not found"}, 404)


api.add_resource(UserCityByID, "/usercities/<int:id>")

# Blog


class Blogs(Resource):
    def get(self):
        blogs = [
            blog.to_dict(rules=("-comments.user.blogs", "-user.comments"))
            for blog in Blog.query.all()
        ]
        return make_response(blogs, 200)

    def post(self):
        data = request.get_json()

        try:
            new_blog = Blog(
                user_id=data["user_id"],
                title=data["title"],
                blog_body=data["blog_body"],
                blog_city=data["blog_city"],
                blog_country=data["blog_country"],
                blog_img=data["blog_img"],
            )
            db.session.add(new_blog)
            db.session.commit()
            return make_response({"message": "success"}, 201)

        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)


api.add_resource(Blogs, "/blogs")


class BlogByID(Resource):
    def get(self, id):
        blog = Blog.query.filter(Blog.id == id).first()

        if blog:
            return make_response(
                blog.to_dict(rules=("-comments.user", "-user.comments", "-comments")),
                200,
            )
        else:
            return make_response({"error": "Blog not found"}, 404)

    def patch(self, id):
        blog = Blog.query.filter(Blog.id == id).first()

        if blog:
            data = request.get_json()
            for key in data:
                setattr(blog, key, data[key])
            db.session.add(blog)
            db.session.commit()
            return make_response(blog.to_dict(), 202)
        else:
            return make_response({"error": "Blog not found"}, 404)

    def delete(self, id):
        blog = Blog.query.filter(Blog.id == id).first()

        if blog:
            db.session.delete(blog)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "Blog not found"}, 404)


api.add_resource(BlogByID, "/blogs/<int:id>")


class BlogComments(Resource):
    def get(self):
        comments = [
            comment.to_dict(rules=("-blog.user", "-user.blogs"))
            for comment in BlogComment.query.all()
        ]
        return make_response(comments, 200)

    def post(self):
        data = request.get_json()

        try:
            new_comment = BlogComment(
                id=data["id"],
                user_id=data["user_id"],
                blog_id=data["blog_id"],
                comment=data["comment"],
            )
            db.session.add(new_comment)
            db.session.commit()
            return make_response({"message": "success"}, 201)
        except Exception as e:
            db.session.rollback()
            return {"errors": ["Validation errors", str(e)]}, 400


api.add_resource(BlogComments, "/comments")


class BlogCommentByID(Resource):
    def get(self, id):
        comment = BlogComment.query.filter(BlogComment.id == id).first()

        if comment:
            return make_response(comment.to_dict(), 200)
        return make_response({"error": "Comment not found"}, 404)

    def patch(self, id):
        comment = BlogComment.query.filter(BlogComment.id == id).first()

        if comment:
            data = request.get_json()
            for key in data:
                setattr(comment, key, data[key])
            db.session.add(comment)
            db.session.commit()
            return make_response(comment.to_dict(), 202)
        else:
            return make_response({"error": "Comment not found"}, 404)

    def delete(self, id):
        comment = BlogComment.query.filter(BlogComment.id == id).first()

        if comment:
            db.session.delete(comment)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "Comment not found"}, 404)


api.add_resource(BlogCommentByID, "/blogs/<int:id>")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
