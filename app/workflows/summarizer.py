from app.llm.client import GeminiClient
from app.schemas.summary import IncidentSummary


class IncidentSummarizer:
    def __init__(self, llm: GeminiClient):
        self.llm = llm

    async def summarize(
        self,
        incident_text: str,
        tool_results: dict,
    ) -> IncidentSummary:

        prompt = f"""
        Create a final incident investigation summary.

        Original incident:
        {incident_text}

        Tool results:
        {tool_results}

        Return:
        - likely root cause
        - recommended action
        - confidence level
        """

        return await self.llm.generate_structured(
            prompt=prompt,
            schema=IncidentSummary,
        )
