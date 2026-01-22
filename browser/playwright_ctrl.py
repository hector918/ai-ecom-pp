
from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self, headless=False):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=headless)
        self.page = self.browser.new_page()

    def goto(self, url):
        self.page.goto(url)

    def snapshot(self):
        return self.page.evaluate("""
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

    def execute(self, action):
        t = action.get("action")
        if t == "goto":
            self.goto(action["url"])
        elif t == "click":
            self.page.click(action["selector"])
        elif t == "fill":
            self.page.fill(action["selector"], action["text"])
        elif t == "press":
            self.page.press(action["selector"], action["key"])

    def close(self):
        self.browser.close()
        self.p.stop()
