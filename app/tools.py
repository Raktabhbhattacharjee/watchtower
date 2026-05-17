def collect_logs():
    return "Collected recent application logs"


def collect_metrics():
    return "Collected latency and error-rate metrics"


TOOLS = {
    "collect_logs": collect_logs,
    "collect_metrics": collect_metrics,
}