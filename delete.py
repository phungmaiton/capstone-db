from app import app
from models import db, Blog, User

if __name__ == "__main__":
    with app.app_context():
        # # Get all the blog records from the database
        # blogs = Blog.query.all()

        # # Update the blog_country field to "South Africa" for each blog record
        # for blog in blogs:
        #     blog.blog_country = "South Africa"

        # # Commit the changes to the database
        # db.session.commit()

        user = User.query.filter(User.id == 1).first()

        user.profile_img = "https://media.istockphoto.com/id/1311084168/photo/overjoyed-pretty-asian-woman-look-at-camera-with-sincere-laughter.webp?b=1&s=170667a&w=0&k=20&c=XPuGhP9YyCWquTGT-tUFk6TwI-HZfOr1jNkehKQ17g0="

        db.session.commit()
