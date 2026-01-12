from playwright.async_api import async_playwright

async def open_browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://example.com")
        title = await page.title()
        print("Page title:", title)

        await page.wait_for_timeout(3000)
        await browser.close()
