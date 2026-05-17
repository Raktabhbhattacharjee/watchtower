import asyncio


async def collect_logs():
    await asyncio.sleep(1)
    return "Collected recent application logs"


async def collect_metrics():
    await asyncio.sleep(1)
    return "Collected latency and error-rate metrics"


TOOLS = {
    "collect_logs": collect_logs,
    "collect_metrics": collect_metrics,
}