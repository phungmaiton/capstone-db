from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import Bcrypt
from sqlalchemy import JSON
import os, json

db = SQLAlchemy()

bcrypt = Bcrypt()


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    email = db.Column(db.String)
    profile_img = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zipcode = db.Column(db.Integer)
    country = db.Column(db.String)
    currency_code = db.Column(db.String)

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes may not be viewed.")

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))

    def __repr__(self):
        return f"<User {self.username}>"

    serialize_rules = ("-_password_hash", "-usercities", "-blogs.user")

    @validates("email")
    def validate_email(self, key, email):
        if "@" not in email:
            raise ValueError("Please enter a valid email address")
        return email


class City(db.Model, SerializerMixin):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String)
    state_code = db.Column(db.String)
    country_name = db.Column(db.String)
    exchange_rate = db.Column(JSON)
    currency_code = db.Column(db.String)
    img = db.Column(db.String)

    prices = db.relationship("Price", backref="city", cascade="all, delete-orphan")

    serialize_rules = ("-usercities",)

    @property
    def exchange_rate_object(self):
        if self.exchange_rate:
            return json.loads(self.exchange_rate)
        return None

    @exchange_rate_object.setter
    def exchange_rate_object(self, value):
        self.exchange_rate = json.dumps(value)


class UserCity(db.Model, SerializerMixin):
    __tablename__ = "usercities"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        "user_id",
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )

    city_id = db.Column(
        "city_id",
        db.Integer,
        db.ForeignKey("cities.id", ondelete="CASCADE"),
        primary_key=True,
    )

    rating = db.Column(db.Integer)


class Price(db.Model, SerializerMixin):
    __tablename__ = "prices"

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey("cities.id"))

    item_name = db.Column(db.String)
    category_name = db.Column(db.String)

    avg_usd = db.Column(db.Float)

    serialize_rules = ("-city.prices",)

    @validates("avg_usd")
    def validate_avg(self, key, avg_usd):
        if not isinstance(avg_usd, float):
            raise ValueError("Must enter a valid price")
        return avg_usd


class Blog(db.Model, SerializerMixin):
    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        "user_id",
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
    )
    title = db.Column(db.String)
    blog_body = db.Column(db.String)
    blog_img = db.Column(db.String)
    blog_city = db.Column(db.String)
    blog_country = db.Column(db.String)

    serialize_rules = ("-user.blogs",)
