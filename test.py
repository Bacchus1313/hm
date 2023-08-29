from playwright.sync_api import Playwright, sync_playwright, expect


def test_homework(playwright: Playwright) -> None:
    driver = playwright.chromium.launch(headless=False)
    context = driver.new_context()
    page = driver.new_page()
    page.goto("https://cloud.ru/ru")
    page.locator("ul[class='Header_menu__C1bZ_'] li:nth-child(3)").click()
    page.locator("div[class^='Products_block__QWrJ9']:nth-child(2) a:nth-child(6)").click()
    h1_title = page.wait_for_selector("h1[class='Hero_title__0eNxo']", timeout=5000).inner_text()
    title_page = page.title()
    page.close()
    context.close()
    driver.close()
    assert title_page == "API Gateway", "Страница API Gateway не открылась"
    assert h1_title == "API Gateway", f"""Заголовок не соответствует. Ожидали "API Gateway", получили {h1_title}"""

