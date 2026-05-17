import asyncio

from app.llm.client import GeminiClient
from app.schemas.incident import IncidentAnalysis
from app.workflows.incident_workflow import IncidentWorkflow
from app.workflows.planner import InvestigationPlanner
from app.workflows.summarizer import IncidentSummarizer


async def main():

    incident_text = """
    API latency increased after deployment.
    Error rates are rising rapidly.
    """

    client = GeminiClient()

    analysis = await client.generate_structured(
        prompt=f"""
        Analyze this incident:

        {incident_text}
        """,
        schema=IncidentAnalysis,
    )

    planner = InvestigationPlanner(llm=client)

    plan = await planner.create_plan(
        incident_text=incident_text,
        analysis=analysis,
    )

    workflow = IncidentWorkflow()

    result = workflow.run(plan)

    summarizer = IncidentSummarizer(llm=client)

    summary = await summarizer.summarize(
        incident_text=incident_text,
        tool_results=result,
    )

    print("ANALYSIS:")
    print(analysis)

    print("\nPLAN:")
    print(plan)

    print("\nRESULT:")
    print(result)

    print("\nSUMMARY:")
    print(summary)


if __name__ == "__main__":
    asyncio.run(main())
