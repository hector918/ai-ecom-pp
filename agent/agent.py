from agent.planner import Planner
from agent.executor import Executor
from agent.memory import Memory

class Agent:
    def __init__(self, browser):
        self.browser = browser
        self.planner = Planner()
        self.executor = Executor(browser)
        self.memory = Memory()

    async def step(self, goal):
        dom = await self.browser.snapshot()
        action = self.planner.plan(goal, dom)  # LLM 是同步 HTTP，不影响
        result = await self.executor.run(action)
        self.memory.add(dom, action, result)

        return {
            "action": action,
            "result": result,
            "history": self.memory.steps
        }
