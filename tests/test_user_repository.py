from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_get_all_users(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/chitter_database.sql")
    repository = UserRepository(db_connection) 
    users = repository.all() # Get all users

    # Assert on the results
    assert users == [
        User(1, 'John Doe', 'JohnDoe', 'johndoe@example.com', 'password123'),
        User(2, 'Jane Smith', 'JaneSmith', 'janesmith@example.com', 'abc123')
    ]

"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/chitter_database.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, "Test Name", "Test Username", "Test email", "Test password"))

    result = repository.all()
    assert result == [
        User(1, 'John Doe', 'JohnDoe', 'johndoe@example.com', 'password123'),
        User(2, 'Jane Smith', 'JaneSmith', 'janesmith@example.com', 'abc123'),
        User(3, 'Test Name', 'Test Username', 'Test email', 'Test password'),
    ]
    
    
"""
When we call UserRepository#find
We get a single User object reflecting the seed data.
"""
def test_get_single_artist(db_connection):
    db_connection.seed("seeds/chitter_database.sql")
    repository = UserRepository(db_connection)

    user = repository.find(1)
    assert user ==  User(1, 'John Doe', 'JohnDoe', 'johndoe@example.com', 'password123')
    
def test_find_with_post(db_connection):
    db_connection.seed("seeds/chitter_database.sql")
    repository = UserRepository(db_connection)
        # Assuming the album_id 1 exists in the database
    post_id = 1
    # Call the method under test
    result = repository.find_with_post(post_id)
    assert result == User(1, 'John Doe', 'JohnDoe', 'johndoe@example.com', 'password123')