# Watchtower

Watchtower is an orchestration-first AI incident analysis system built with raw Python and the Gemini SDK.

The goal of this project is to learn and implement real-world GenAI systems engineering principles inspired by Anthropic’s engineering philosophy around effective agents and orchestration systems.

This project intentionally avoids heavy framework abstraction in the early stages to better understand:
- LLM runtime architecture
- structured outputs
- orchestration workflows
- typed state management
- provider abstraction
- backend-driven AI systems

---

# Engineering Philosophy

Watchtower follows several core principles:

- Start simple
- Prefer composable workflows over unnecessary autonomy
- Treat agents as orchestration systems, not magic AI
- Focus on state, validation, observability, retries, and tool design
- Avoid unnecessary abstraction layers until they are truly needed

Core idea:

```text
LLMs generate reasoning.
Software systems control execution.
```

The LLM is treated as one subsystem inside a larger orchestration runtime.

---

# Current Features

- Gemini SDK integration
- Centralized configuration using Pydantic Settings
- Structured outputs with schema validation
- Typed orchestration state using Pydantic
- Provider abstraction layer (`GeminiClient`)
- Async-ready architecture
- Incident analysis workflow foundation

---

# Tech Stack

- Python 3.13+
- FastAPI
- Google Gemini SDK
- Pydantic
- uv

---

# Current Architecture

```text
Request
    ↓
GeminiClient
    ↓
Gemini API
    ↓
Structured Output
    ↓
Pydantic Validation
    ↓
Typed Runtime State
```

---

# Example Structured Output

Input:

```text
"API latency increased after deployment and error rates are rising rapidly."
```

Output:

```json
{
  "issue_type": "Performance Degradation",
  "severity": "Critical",
  "needs_logs": true,
  "needs_metrics": true,
  "summary": "API latency increased and error rates are rising rapidly after deployment."
}
```

---

# Project Structure

```text
watchtower/
│
├── app/
│   ├── core/
│   │   └── config.py
│   │
│   ├── llm/
│   │   └── client.py
│   │
│   ├── schemas/
│   │   └── incident.py
│   │
│   ├── test_config.py
│   └── test_structured.py
│
├── .env
├── pyproject.toml
└── README.md
```

---

# Setup

## Clone Repository

```bash
git clone <repo-url>
cd watchtower
```

---

## Create Virtual Environment

```bash
uv venv
```

---

## Activate Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
uv sync
```

---

## Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

---

# Run Structured Output Test

From the project root:

```bash
uv run python -m app.test_structured
```

---

# References

This project is heavily inspired by Anthropic’s engineering article:

- [Building Effective Agents — Anthropic Engineering](https://www.anthropic.com/engineering/building-effective-agents)


The architecture and implementation philosophy of Watchtower focuses on:
- composable workflows
- structured orchestration
- typed runtime state
- tool-driven execution
- observability-first design
- minimizing unnecessary abstraction

---

# Roadmap

- Workflow routing
- Tool execution layer
- Retry and failure handling
- Observability and tracing
- Streaming support
- Async orchestration pipelines
- Stateful workflows
- Controlled agent loops
- Evaluation and feedback systems

---

# Status

Early-stage orchestration runtime prototype focused on learning production-oriented AI systems engineering principles.