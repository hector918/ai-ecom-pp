class Executor:
    def __init__(self, browser):
        self.browser = browser

    def run(self, action):
        result = self.browser.execute(action)
        return result
