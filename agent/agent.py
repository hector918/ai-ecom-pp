
from agent.planner import Planner
from agent.executor import Executor
from agent.memory import Memory

class Agent:
    def __init__(self, browser):
        self.browser = browser
        self.planner = Planner()
        self.executor = Executor(browser)
        self.memory = Memory()

    def step(self, goal):
        dom = self.browser.snapshot()
        action = self.planner.plan(goal, dom)
        self.executor.run(action)
        self.memory.add(dom, action)
        return action
