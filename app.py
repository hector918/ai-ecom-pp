from fastapi import FastAPI
from browser.playwright_ctrl import Browser
from agent.agent import Agent

from pydantic import BaseModel

class TaskRequest(BaseModel):
    goal: str
    
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
async def step(request: TaskRequest):
    output = await agent.step(request.goal)
    return {
        "status": "running",
        "data": output
    }
