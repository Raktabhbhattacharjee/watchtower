import asyncio

from app.llm.client import GeminiClient


async def main():

    client = GeminiClient()

    response = await client.generate_text(
        "Explain what an orchestration runtime is in one sentence."
    )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())