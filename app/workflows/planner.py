from app.llm.client import GeminiClient
from app.schemas.incident import IncidentAnalysis
from app.schemas.plan import InvestigationPlan


class InvestigationPlanner:
    def __init__(self, llm: GeminiClient):
        self.llm = llm

    async def create_plan(
        self,
        incident_text: str,
        analysis: IncidentAnalysis,
    ) -> InvestigationPlan:

        prompt = f"""
        Create an investigation plan for this incident.

        Original incident:
        {incident_text}

        Structured analysis:
        issue_type: {analysis.issue_type}
        severity: {analysis.severity}
        needs_logs: {analysis.needs_logs}
        needs_metrics: {analysis.needs_metrics}
        summary: {analysis.summary}

        Valid steps:
        - collect_logs
        - collect_metrics

        Only choose steps from the valid steps list.
        """

        return await self.llm.generate_structured(
            prompt=prompt,
            schema=InvestigationPlan,
        )