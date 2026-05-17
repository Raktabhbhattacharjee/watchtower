from app.tools import TOOLS


class IncidentWorkflow:

    def run(self, plan):

        actions = []

        for step in plan.steps:

            tool = TOOLS.get(step)

            if tool:

                result = tool()

                actions.append(result)

        return {
            "executed_steps": plan.steps,
            "actions": actions,
        }