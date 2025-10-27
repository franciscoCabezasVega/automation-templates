def test_open_inventory(page):
    page.goto("https://www.saucedemo.com/v1/inventory.html")
    assert "inventory" in page.url
    assert page.locator(".inventory_item").count() > 0