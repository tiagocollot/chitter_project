from lib.users import User

"""
User constructs with an id, username, email and password
"""
def test_user_constructs():
    user = User(1, 'JohnDoe', 'johndoe@example.com', 'password123')
    assert user.id == 1
    assert user.username == 'JohnDoe'
    assert user.email == 'johndoe@example.com'
    assert user.password == 'password123'

"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, 'JohnDoe', 'johndoe@example.com', 'password123')
    user2 = User(1, 'JohnDoe', 'johndoe@example.com', 'password123')
    assert user1 == user2
    
"""
We can format users to strings nicely
"""
def test_user_format_nicely():
    user = User(1, 'JohnDoe', 'johndoe@example.com', 'password123')
    assert str(user) == "User(1, JohnDoe, johndoe@example.com, password123)"