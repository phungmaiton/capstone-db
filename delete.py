from app import app
from models import db, Blog, User, BlogComment, Price, UserCity

if __name__ == "__main__":
    with app.app_context():
        # # Get all the blog records from the database
        # blogs = Blog.query.all()

        # # Update the blog_country field to "South Africa" for each blog record
        # for blog in blogs:
        #     blog.blog_country = "South Africa"

        # # Commit the changes to the database
        # db.session.commit()

        # BlogComment.query.delete()
        # db.session.commit()

        comment = BlogComment.query.filter(BlogComment.id == 12).first()
        db.session.delete(comment)
        db.session.commit()
