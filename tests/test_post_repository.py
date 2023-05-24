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
        Post(1, 'Hello, world!', '2023-05-19 09:00:00', 1),
        Post(2, 'This is my first peep!', '2023-05-19 10:30:00', 2)
    ]
    
#     """
# When we call AlbumRepository#create
# We get a new record in the database.
# """
    # expected_posts = [
    #     Post(1, 'Hello, world!', '2023-05-19 09:00:00', 1),
    #     Post(2, 'This is my first peep!', '2023-05-19 10:30:00', 2)
    # ]

    # # Assert on the results
    # assert len(posts) == len(expected_posts)  # Check if the number of posts is the same

    # for post, expected_post in zip(posts, expected_posts):
    #     assert post.id == expected_post.id
    #     assert post.content == expected_post.content
    #     assert post.post_time == expected_post.post_time
    #     assert post.user_id == expected_post.user_id
# def test_create_record(db_connection):
#     db_connection.seed("seeds/music_web_app.sql")
#     repository = AlbumRepository(db_connection)

#     repository.create(Album(None, 'Mahmoud', 1987 , 2))

#     result = repository.all()
#     assert result == [
#         Album(1, 'Doolitle', 1989 , 1),
#         Album(2, 'Surfer Rosa', 1988 , 2),
#         Album(3, 'Mahmoud', 1987 , 2)
#     ]
    
# """
# When we call BookRepository#find
# We get a single Book object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/music_web_app.sql")
#     repository = AlbumRepository(db_connection)

#     album = repository.find(1)
#     assert album == Album(1, "Doolitle", 1989, 1)