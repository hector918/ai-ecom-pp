from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self, headless=True):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=headless)
        self.page = self.browser.new_page()

    def goto(self, url):
        self.page.goto(url)

    def snapshot(self):
        # 返回可交互元素
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

    def extract(self, selector, limit=5):
        # 用于真正“抓数据”
        return self.page.evaluate(f"""
        () => {{
            const results = [];
            const nodes = document.querySelectorAll("{selector}");
            for (let i = 0; i < Math.min(nodes.length, {limit}); i++) {{
                results.push(nodes[i].innerText);
            }}
            return results;
        }}
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

        elif t == "extract":
            return self.extract(
                action["selector"],
                action.get("limit", 5)
            )
