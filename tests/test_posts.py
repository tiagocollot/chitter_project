from lib.post import Post

"""
Posts constructs with an id, content, post_time amnd user_id
"""
def test_posts_constructs():
    post = Post(1, 'Hello, world!', '2023-05-19 09:00:00', 1)
    assert post.id == 1
    assert post.content == 'Hello, world!'
    assert post.post_time == '2023-05-19 09:00:00'
    assert post.user_id == 1
    
"""
We can compare two identical posts
And have them be equal
"""    
    
def test_posts_are_equal():
    post1 = Post(1, 'Hello, world!', '2023-05-19 09:00:00', 1)
    post2 = Post(1, 'Hello, world!', '2023-05-19 09:00:00', 1)
    assert post1 == post2
    
"""
We can format posts to strings nicely
"""
def test_post_format_nicely():
    post = Post(1, 'Hello, world!', '2023-05-19 09:00:00', 1, 'JohnDoe')
    assert str(post) == "Post(1, Hello, world!, 2023-05-19 09:00:00, 1, JohnDoe)"