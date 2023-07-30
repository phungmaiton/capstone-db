from app import app
from models import db, User, City, Price, UserCity, BlogComment


if __name__ == "__main__":
    with app.app_context():
        comment = BlogComment(
            id=1, user_id=2, blog_id=1, comment="This is an awesome post! Thank you!"
        )

        db.session.add(comment)
        db.session.commit()
