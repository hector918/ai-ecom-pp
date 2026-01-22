
import json
from llm.ollama_client import OllamaClient

PROMPT = """
你是一个浏览器自动化 Agent。

当前目标：
{goal}

当前网页可交互元素：
{dom}

请给出下一步 Playwright 动作(JSON)：
格式例如：
{{"action":"click","selector":"#submit"}}

只返回 JSON，不要解释。
"""

class Planner:
    def __init__(self):
        self.llm = OllamaClient()

    def plan(self, goal, dom):
        prompt = PROMPT.format(goal=goal, dom=dom)
        resp = self.llm.chat(prompt)
        return json.loads(resp)
