
class Executor:
    def __init__(self, browser):
        self.browser = browser

    def run(self, action):
        self.browser.execute(action)
