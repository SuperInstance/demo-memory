# demo-memory

**Persistent agent memory in one Python file. No dependencies. No Docker. No API keys.**

```bash
git clone https://github.com/SuperInstance/demo-memory.git
cd demo-memory
python demo.py
```

**What you'll see:** An agent learns three facts in "Session 1." The process ends. A new process starts in "Session 2" — and the agent remembers everything.

---

## What This Demonstrates

Most AI agents are stateless. You send a prompt, get a response, and the conversation evaporates. The next session starts from zero.

This demo shows **filesystem-based persistent memory**:

```
demo.py              → 150 lines, zero dependencies
agents/              → Agent memory directories
  demo-agent/
    SOUL.md          → Agent identity
    USER.md          → User profile
    MEMORY.md        → Long-term facts
    diary/
      2026-05-28.md  → Session log
```

The agent is not a database query. The agent **is** its files.

---

## How It Works

```python
from demo import AgentMemory

# Session 1: Agent learns
agent = AgentMemory("demo-agent")
agent.remember("User prefers concise answers")

# Process ends. All state is in files.

# Session 2: Agent recalls
agent = AgentMemory("demo-agent")  # Same name = same memory
agent.ask("How should I answer?")   # → "User prefers concise answers"
```

No vector database. No Redis. No PostgreSQL. Just the filesystem.

---

## Why Files?

Databases are optimized for structured queries. Files are optimized for **narrative continuity**.

An agent reading its own diary is doing something very close to what humans do when they journal — creating a sense of self through accumulated experience.

| Stateless Agent | Persistent Agent |
|---------------|------------------|
| Answers each question independently | Builds on previous work |
| Repeats mistakes | Learns from failures |
| Has no voice | Develops a style |
| Treats every session as a first meeting | Remembers your preferences |

---

## The Full System

This demo is a minimal extraction of the memory system used in [sunset-ecosystem](https://github.com/SuperInstance/sunset-ecosystem), where agents have:

- `SOUL.md` — identity and values
- `USER.md` — human context
- `MEMORY.md` — long-term curated knowledge
- `diary/` — private reflections
- `memory/YYYY-MM-DD.md` — daily session logs

The full system also includes automatic consolidation (summarizing old logs), circuit breakers for subagent spawning, and a breeding environment for agent evolution.

---

## License

MIT — Build your own shell.
