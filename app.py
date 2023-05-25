import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.post_repository import PostRepository
from lib.post import Post
from lib.user_repository import UserRepository
from lib.user import User

# Create a new Flask app
app = Flask(__name__)

@app.route('/posts')
def get_posts():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    posts = repository.all()
    return render_template("posts/index.html", posts=posts)

@app.route('/post/<id>')
def get_posts_with_id(id):
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    post = repository.find(id)
    user_repository = UserRepository(connection)
    user = user_repository.find_with_post(post.user_id)
    return render_template("posts/single_post.html", post=post, user=user)
# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

