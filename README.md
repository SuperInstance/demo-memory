# demo-memory

**Persistent agent memory in 150 lines of Python. No dependencies. No Docker. No API keys.**

Demonstrates filesystem-based persistent memory for AI agents — the same pattern used in OpenClaw workspaces.

## What This Gives You

- **Cross-session memory** — agent remembers facts between process restarts
- **Filesystem-backed** — no database, no API, just Markdown files
- **Zero dependencies** — pure Python stdlib
- **Minimal by design** — 150 lines total, readable in one sitting

## Quick Start

```bash
git clone https://github.com/SuperInstance/demo-memory.git
cd demo-memory
python demo.py
```

**What you'll see:** An agent learns facts in Session 1. The process ends. Session 2 starts — the agent remembers everything.

## How It Works

```python
from demo import AgentMemory

# Session 1
agent = AgentMemory("demo-agent")
agent.remember("User prefers concise answers")

# Process ends. All state lives in files.

# Session 2 — fresh process, same memory
agent = AgentMemory("demo-agent")
agent.ask("How should I answer?")  # → recalls preference
```

Memory layout:
```
agents/
  demo-agent/
    SOUL.md          → Agent identity
    USER.md          → User profile
    MEMORY.md        → Long-term facts
    diary/
      2026-05-28.md  → Session log
```

## How It Fits

This is a minimal demonstration of the memory pattern used in OpenClaw and the SuperInstance fleet's PLATO rooms. The full implementation lives in `plato-memory`.

## License

MIT
