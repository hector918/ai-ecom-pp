
class Memory:
    def __init__(self):
        self.steps = []

    def add(self, dom, action):
        self.steps.append({
            "dom": dom,
            "action": action
        })
