# Watchtower

**An orchestration-first AI incident investigation system** built with raw Python + Gemini SDK.

A deliberate exercise in real-world GenAI systems engineering — inspired by [Anthropic's guide to building effective agents](https://www.anthropic.com/engineering/building-effective-agents).

---

## Engineering Philosophy

Watchtower follows a **workflow-first architecture**.

> **LLMs generate reasoning. Software systems control execution.**

The LLM is treated as one subsystem inside a larger orchestration runtime.

---

## Architecture

### Watchtower Incident Investigation Pipeline

```mermaid
flowchart TD
    Title[Watchtower - AI Incident Investigation System] 
    
    Title --> A[Incident Input]

    A --> B[1. Analysis Stage\nLLM]
    B --> C[Structured Analysis State\nPydantic Validation]
    C --> D[2. Planning Stage\nLLM]
    D --> E[Execution Plan]
    E --> F[3. Tool Orchestration Layer]
    F --> G[Tool Results]
    G --> H[4. Summarization Stage\nLLM]
    H --> I[Final Investigation Summary]

    classDef title fill:#1E2937,stroke:#0EA5E9,stroke-width:4px,color:#E0F2FE,rx:25,ry:25
    classDef input fill:#334155,stroke:#64748B,color:#F1F5F9
    classDef llm fill:#0EA5E9,stroke:#0369A1,color:#0F172A,rx:15,ry:15
    classDef state fill:#14B8A6,stroke:#0F766E,color:#0F172A,rx:12,ry:12
    classDef tools fill:#8B5CF6,stroke:#6D28D9,color:#F1F5F9,rx:15,ry:15
    classDef final fill:#22C55E,stroke:#15803D,color:#0F172A,rx:15,ry:15

    class Title title
    class A input
    class B,D,H llm
    class C,E,G state
    class F tools
    class I final

    B -. "Gemini SDK" .-> C
    D -. "Gemini SDK" .-> E
    H -. "Gemini SDK" .-> I

## Features

### LLM Layer
- Gemini SDK integration via raw provider SDK
- Provider abstraction layer (`GeminiClient`)
- Structured generation pipeline

### Schema & Validation Layer
- Typed orchestration state using Pydantic
- Runtime schema validation
- Structured intermediate workflow state

### Workflow Layer
- Multi-stage orchestration pipeline
- Prompt chaining
- Planning-based execution
- Tool orchestration
- Feedback-driven summarization

### Tool Layer
- Dynamic tool registry
- Tool execution runtime
- Controlled execution environment

---

## Workflow Stages

### 1. Incident Analysis

Transforms unstructured incident text into validated structured state.

**Input:**
```
"API latency increased after deployment and error rates are rising rapidly."
```

**Output:**
```json
{
  "issue_type": "Performance Degradation",
  "severity": "Critical",
  "needs_logs": true,
  "needs_metrics": true,
  "summary": "API latency increased and error rates are rising rapidly after deployment."
}
```

### 2. Investigation Planning

The LLM generates a structured execution plan.

```json
{
  "steps": ["collect_logs", "collect_metrics"],
  "reasoning": "Latency and error spikes require logs and metrics investigation."
}
```

### 3. Tool Execution

Python orchestrates deterministic tool execution using a controlled tool registry.

Current tools: `collect_logs`, `collect_metrics`

### 4. Final Summarization

The LLM receives tool results and generates a structured final summary.

```json
{
  "root_cause": "Likely deployment-related performance regression",
  "recommended_action": "Inspect deployment changes and compare metrics before and after deployment",
  "confidence": "medium"
}
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13+ |
| API Framework | FastAPI |
| LLM Provider | Google Gemini SDK |
| Validation | Pydantic + Pydantic Settings |
| Package Manager | uv |

---

## Project Structure

```
watchtower/
│
├── app/
│   ├── agents/
│   │   └── runtime.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── llm/
│   │   └── client.py
│   │
│   ├── workflows/
│   │   ├── planner.py
│   │   ├── summarizer.py
│   │   └── incident_workflow.py
│   │
│   ├── schemas/
│   │   ├── incident.py
│   │   ├── plan.py
│   │   └── summary.py
│   │
│   ├── tools.py
│   └── main.py
│
├── .env
├── pyproject.toml
└── README.md
```

---

## Setup

**Clone the repository:**
```bash
git clone <repo-url>
cd watchtower
```

**Create and activate a virtual environment:**
```bash
uv venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\Activate.ps1       # Windows PowerShell
```

**Install dependencies:**
```bash
uv sync
```

**Configure environment variables** — create a `.env` file at the project root:
```
GEMINI_API_KEY=your_api_key
```

**Run:**
```bash
uv run python -m app.main
```

---

## Example Output

```
ANALYSIS:
issue_type='Performance Degradation'
severity='Critical'

PLAN:
steps=['collect_logs', 'collect_metrics']

RESULT:
Collected logs and metrics

SUMMARY:
Likely deployment-related regression
```

---

## Orchestration Patterns

Watchtower implements several patterns from Anthropic's engineering philosophy:

- Augmented LLM systems
- Routing workflows
- Prompt chaining workflows
- Tool orchestration
- Feedback-driven reasoning
- Structured intermediate state
- Typed orchestration pipelines

---

## Roadmap

**Workflow Evolution**
- Parallel workflow execution
- Evaluator-optimizer workflows
- Controlled retry loops
- Stateful orchestration runtime
- Workflow tracing

**Tooling**
- Real observability integrations (log ingestion, metrics ingestion, incident timeline analysis)

**Infrastructure**
- FastAPI API layer
- Async orchestration runtime
- Persistent workflow state
- Structured execution logs

**Agentic Systems**
- Controlled agent loops
- Human-in-the-loop checkpoints
- Multi-provider orchestration
- Evaluation pipelines

---

## Status

Early-stage orchestration runtime prototype. The goal is a deep, first-principles understanding of production-oriented AI systems engineering — through explicit workflow design and minimal abstraction.