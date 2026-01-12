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
    async def click(self, selector: str):
        if not self.page:
            return {"error": "Browser not started"}

        await self.page.click(selector)
        return {"status": "clicked", "selector": selector}

    async def type_text(self, selector: str, text: str):
        if not self.page:
            return {"error": "Browser not started"}

        await self.page.fill(selector, text)
        return {
            "status": "typed",
            "selector": selector,
            "text": text
        }

    async def wait(self, milliseconds: int):
        if not self.page:
            return {"error": "Browser not started"}

        await self.page.wait_for_timeout(milliseconds)
        return {"status": "waited", "ms": milliseconds}

    async def scroll(self, pixels: int = 500):
        if not self.page:
            return {"error": "Browser not started"}

        await self.page.mouse.wheel(0, pixels)
        return {"status": "scrolled", "pixels": pixels}
