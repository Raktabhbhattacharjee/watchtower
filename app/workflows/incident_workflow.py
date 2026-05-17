import asyncio

from app.tools import TOOLS


class IncidentWorkflow:

    async def run(self, plan):
        tasks = []

        for step in plan.steps:
            tool = TOOLS.get(step)

            if tool:
                tasks.append(tool())

        actions = await asyncio.gather(*tasks)

        return {
            "executed_steps": plan.steps,
            "actions": actions,
        }