from playwright.async_api import async_playwright

class BrowserController:
    def __init__(self):
        self.browser = None
        self.page = None

    async def open(self, url: str):
        p = await async_playwright().start()
        self.browser = await p.chromium.launch(headless=False)
        self.page = await self.browser.new_page()

        await self.page.goto(url)
        title = await self.page.title()

        return {
            "url": url,
            "title": title
        }
