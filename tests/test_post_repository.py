from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_posts(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/chitter_database.sql")
    repository = PostRepository(db_connection) 

    posts = repository.all() # Get all posts

    # Assert on the results  
    assert posts == [
        Post(1, 'Hello, world!', '2023-05-19 09:00:00', 1, 'JohnDoe'),
        Post(2, 'This is my first peep!', '2023-05-19 10:30:00', 2, 'JaneSmith')
    ]
    
"""
When we call PostRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/chitter_database.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, 'This is my second peep!', '2023-05-19 10:35:00', 2, 'JaneSmith'))

    result = repository.all()
    assert result == [
        Post(1, 'Hello, world!', '2023-05-19 09:00:00', 1, 'JohnDoe'),
        Post(2, 'This is my first peep!', '2023-05-19 10:30:00', 2, 'JaneSmith'),
        Post(3, 'This is my second peep!', '2023-05-19 10:35:00', 2, 'JaneSmith')
    ]

"""
When we call PostRepository#find
We get a single Post object reflecting the seed data.
"""
def test_get_single_post_record(db_connection):
    db_connection.seed("seeds/chitter_database.sql")
    repository = PostRepository(db_connection)

    post = repository.find(2)
    assert post == Post(2, 'This is my first peep!', '2023-05-19 10:30:00', 2)