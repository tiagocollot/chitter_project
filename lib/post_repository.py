from lib.post import Post

class PostRepository():
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["content"], row["post_time"], row["user_id"])
            posts.append(item)
        return posts