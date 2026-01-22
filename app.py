from fastapi import FastAPI
from browser.playwright_ctrl import Browser
from agent.agent import Agent

app = FastAPI()

browser = Browser()
agent = None

@app.on_event("startup")
async def startup():
    global agent
    await browser.start(headless=True)
    agent = Agent(browser)

@app.on_event("shutdown")
async def shutdown():
    await browser.close()

@app.post("/task/step")
async def step(goal: str):
    output = await agent.step(goal)
    return {
        "status": "running",
        "data": output
    }
