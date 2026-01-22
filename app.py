from fastapi import FastAPI
from browser.playwright_ctrl import Browser
from agent.agent import Agent

app = FastAPI()

browser = Browser(headless=True)   # 服务器环境必须 headless
agent = Agent(browser)

@app.post("/task/step")
def step(goal: str):
    output = agent.step(goal)
    return {
        "status": "running",
        "data": output
    }
