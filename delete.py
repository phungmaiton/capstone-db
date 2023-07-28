from app import app
from models import db, User, City, Price, UserCity, Blog


if __name__ == "__main__":
    with app.app_context():
        Blog.query.delete()
        db.session.commit()
