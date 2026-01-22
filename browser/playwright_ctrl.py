from playwright.async_api import async_playwright

class Browser:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    async def start(self, headless=True):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page()

    async def goto(self, url):
        await self.page.goto(url)

    async def snapshot(self):
        return await self.page.evaluate("""
        () => {
            const els = [];
            document.querySelectorAll("input, button, a, select").forEach(el => {
                els.push({
                    tag: el.tagName,
                    text: el.innerText,
                    id: el.id,
                    name: el.name,
                    class: el.className
                });
            });
            return els;
        }
        """)

    async def extract(self, selector, limit=5):
        return await self.page.evaluate(f"""
        () => {{
            const results = [];
            const nodes = document.querySelectorAll("{selector}");
            for (let i = 0; i < Math.min(nodes.length, {limit}); i++) {{
                results.push(nodes[i].innerText);
            }}
            return results;
        }}
        """)

    async def execute(self, action):
        t = action.get("action")

        if t == "goto":
            await self.goto(action["url"])
        elif t == "click":
            await self.page.click(action["selector"])
        elif t == "fill":
            await self.page.fill(action["selector"], action["text"])
        elif t == "press":
            await self.page.press(action["selector"], action["key"])
        elif t == "extract":
            return await self.extract(action["selector"], action.get("limit", 5))

    async def close(self):
        await self.browser.close()
        await self.playwright.stop()
