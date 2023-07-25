import os, urllib.request, json
import urllib.request, json
from flask import Flask, make_response, request, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, User, City, Price, UserCity
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
                return user.to_dict(), 200

        return {"error": "Invalid username or password"}, 401


api.add_resource(Login, "/login", endpoint="login")


class Logout(Resource):
    def delete(self):
        if session.get("user_id"):
            session["user_id"] = None

            return {}, 204

        return {"error": "401 Unauthorized"}, 401


api.add_resource(Logout, "/logout", endpoint="logout")


# Users
class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]

        return make_response(users, 200)


api.add_resource(Users, "/users")


class UserByID(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()

        if user:
            return make_response(user.to_dict(), 200)
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

                return make_response({"message": "successful"}, 202)
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
            return make_response({"message": "success"}, 202)
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

        new_uc = UserCity(user_id=data["user_id"], city_id=data["city_id"], rating=0)

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

if __name__ == "__main__":
    app.run(port=5555, debug=True)
