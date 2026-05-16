import asyncio

from app.llm.client import GeminiClient
from app.schemas.incident import IncidentAnalysis


async def main():

    client = GeminiClient()

    analysis = await client.generate_structured(
        prompt="""
        Analyze this incident:

        API latency increased after deployment.
        Error rates are rising rapidly.
        """,
        schema=IncidentAnalysis,
    )

    print(analysis)
    print(type(analysis))


if __name__ == "__main__":
    asyncio.run(main())