from lib.user import User 

class UserRepository():
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute('SELECT * FROM users;')
        users = []
        for row in rows:
            item = User(row['id'], row['name'], row['username'], row['email'], row['password'])
            users.append(item)
        return users    
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (name, username, email, password) VALUES (%s, %s, %s, %s)', [user.name, user.username, user.email, user.password])
        return None
    
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row['id'], row['name'], row['username'], row['email'], row['password'])
    
    def find_with_post(self, post_id):
        rows = self._connection.execute(
                'SELECT * from users JOIN posts ON users.id = posts.user_id WHERE posts.id = %s', [post_id])
        row = rows[0]
        return User(row['id'], row['name'], row['username'], row['email'], row['password'])
