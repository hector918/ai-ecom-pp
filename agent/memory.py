class Memory:
    def __init__(self):
        self.steps = []

    def add(self, dom, action, result=None):
        self.steps.append({
            "action": action,
            "result": result
        })
