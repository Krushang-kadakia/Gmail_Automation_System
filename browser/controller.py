from playwright.async_api import async_playwright

class BrowserController:
    def __init__(self):
        self.browser = None
        self.page = None
        self.playwright = None

    async def open(self, url: str):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.page = await self.browser.new_page()

        await self.page.goto(url)

        return {
            "url": self.page.url,
            "title": await self.page.title()
        }

    async def observe(self):
        if not self.page:
            return {"error": "Browser not started"}

        dom = await self.page.content()

        return {
            "url": self.page.url,
            "title": await self.page.title(),
            "dom_snippet": dom[:1000]  # truncate on purpose
        }
