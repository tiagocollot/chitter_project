from playwright.sync_api import Page, expect

def test_get_posts(page, test_web_address, db_connection):
    db_connection.seed("seeds/chitter_database.sql")
    page.goto(f"http://{test_web_address}/posts")
    page.screenshot(path="screenshot.png", full_page=True)
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        'Hello, world!',
        'This is my first peep!',
    ])
    expect(paragraph_tags).to_have_text([
        'Post time: 2023-05-19 09:00:00',
        'Post time: 2023-05-19 10:30:00'
    ])   
    
def test_get_single_post(page, test_web_address, db_connection):
    db_connection.seed("seeds/chitter_database.sql")
    page.goto(f"http://{test_web_address}/posts/1")
    page.screenshot(path="screenshot.png", full_page=True)
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        'Hello, world!'
    ])
    expect(paragraph_tags).to_have_text([
        'Post time: 2023-05-19 09:00:00',
        'Artist: JohnDoe'
    ]) 