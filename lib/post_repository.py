from lib.post import Post
from datetime import datetime

class PostRepository():
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            post_time = datetime.strftime(row["post_time"], "%Y-%m-%d %H:%M:%S")
            item = Post(row["id"], row["content"], post_time, row["user_id"])
            posts.append(item)
        return posts
    
    def create(self, post):
        self._connection.execute('INSERT INTO posts (content, post_time, user_id) VALUES (%s, %s, %s)', [post.content, post.post_time, post.user_id])      
        return None
    
    def find(self, post_id):
        rows = self._connection.execute(
                'SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        post_time = datetime.strftime(row["post_time"], "%Y-%m-%d %H:%M:%S")
        return Post(row["id"], row["content"], post_time,  row["user_id"])