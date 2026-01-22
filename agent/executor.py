class Executor:
    def __init__(self, browser):
        self.browser = browser

    async def run(self, action):
        if not isinstance(action, dict):
            raise ValueError(f"Action must be a dict, got: {action}")

        t = action.get("action")
        if not t:
            raise ValueError(f"Action missing 'action' field: {action}")

        if t == "goto":
            url = action.get("url")
            if not url:
                raise ValueError(f"'goto' action missing 'url': {action}")
            return await self.browser.goto(url)

        elif t == "click":
            selector = action.get("selector")
            if not selector:
                raise ValueError(f"'click' action missing 'selector': {action}")
            return await self.browser.page.click(selector)

        elif t == "fill":
            selector = action.get("selector")
            text = action.get("text")
            if not selector or text is None:
                raise ValueError(f"'fill' action missing 'selector' or 'text': {action}")
            return await self.browser.page.fill(selector, text)

        elif t == "press":
            selector = action.get("selector")
            key = action.get("key")
            if not selector or not key:
                raise ValueError(f"'press' action missing 'selector' or 'key': {action}")
            return await self.browser.page.press(selector, key)

        elif t == "extract":
            selector = action.get("selector")
            limit = action.get("limit", 5)
            if not selector:
                raise ValueError(f"'extract' action missing 'selector': {action}")
            return await self.browser.extract(selector, limit)

        else:
            raise ValueError(f"Unknown action type: {t}")
