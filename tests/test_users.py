from lib.users import User

"""
User constructs with an id, username and password
"""
def test_user_constructs():
    user = User(1, "john_doe", "password123")
    assert User.id == 1
    assert User.username == "john_doe"
    assert User.password == "password123"