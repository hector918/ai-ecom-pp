class Executor:
    def __init__(self, browser):
        self.browser = browser

    async def run(self, action):
        return await self.browser.execute(action)
