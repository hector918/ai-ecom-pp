from fastapi import FastAPI
from browser.playwright_ctrl import Browser
from agent.agent import Agent

app = FastAPI()
browser = Browser()
agent = Agent(browser)

@app.post("/task/step")
def step(goal: str):
    action = agent.step(goal)
    return {"action": action}
