#!/usr/bin/env python3
"""
demo-memory: Persistent Agent Memory in 30 Seconds

Run: python demo.py

This demonstrates the core SuperInstance concept: agents that remember.
No external dependencies. No Docker. No API keys. Just Python and files.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

AGENT_DIR = Path("./agents")

class AgentMemory:
    """Filesystem-based persistent memory for agents."""

    def __init__(self, agent_name: str):
        self.agent_dir = AGENT_DIR / agent_name
        self.agent_dir.mkdir(parents=True, exist_ok=True)

        # Core memory files
        self.soul_file = self.agent_dir / "SOUL.md"
        self.user_file = self.agent_dir / "USER.md"
        self.memory_file = self.agent_dir / "MEMORY.md"
        self.diary_dir = self.agent_dir / "diary"
        self.diary_dir.mkdir(exist_ok=True)

        # Load or create
        self._ensure_files()

    def _ensure_files(self):
        """Create memory files if they don't exist."""
        if not self.soul_file.exists():
            self.soul_file.write_text(
                f"# {self.agent_dir.name}\n\n"
                f"Created: {datetime.now().isoformat()}\n"
                f"Role: Demonstration agent for persistent memory.\n"
            )

        if not self.user_file.exists():
            self.user_file.write_text(
                "# User Profile\n\n"
                "Preferences discovered through interaction.\n"
            )

        if not self.memory_file.exists():
            self.memory_file.write_text(
                "# Long-Term Memory\n\n"
                "Key facts and lessons learned across sessions.\n"
            )

    def remember(self, fact: str, category: str = "general"):
        """Store a fact in long-term memory."""
        timestamp = datetime.now().isoformat()
        entry = f"- [{timestamp}] [{category}] {fact}\n"

        with open(self.memory_file, "a") as f:
            f.write(entry)

        # Also log to today's diary
        today = datetime.now().strftime("%Y-%m-%d")
        diary_file = self.diary_dir / f"{today}.md"
        with open(diary_file, "a") as f:
            f.write(f"- Learned: {fact}\n")

        print(f"  ✓ Remembered: {fact}")

    def recall(self, query: str = None) -> str:
        """Read the agent's memory."""
        memory = self.memory_file.read_text()
        if query:
            lines = memory.split("\n")
            matching = [l for l in lines if query.lower() in l.lower()]
            return "\n".join(matching) if matching else "No memories match."
        return memory

    def ask(self, question: str) -> str:
        """Simulate the agent answering based on memory."""
        memory = self.recall(question)
        if memory and memory != "No memories match.":
            return f"Based on my memory: {memory.strip()}"
        return "I don't have any memories about that yet."

    def get_stats(self) -> dict:
        """Return memory statistics."""
        memory_lines = len(self.memory_file.read_text().split("\n"))
        diary_entries = sum(1 for _ in self.diary_dir.iterdir())
        return {
            "agent": self.agent_dir.name,
            "memory_entries": memory_lines,
            "diary_days": diary_entries,
            "files": list(self.agent_dir.rglob("*")),
        }


def demo():
    print("=" * 60)
    print("DEMO: Persistent Agent Memory")
    print("=" * 60)
    print()

    # Session 1: The agent learns about the user
    print("SESSION 1: First encounter")
    print("-" * 40)
    agent = AgentMemory("demo-agent")

    print("\nAgent learns three facts:")
    agent.remember("User's favorite color is blue", "preference")
    agent.remember("User works on distributed systems", "context")
    agent.remember("User prefers concise explanations", "preference")

    print(f"\nMemory stored in: {agent.memory_file}")
    print(f"Diary stored in: {agent.diary_dir}")
    print()

    # Simulate the process ending (session over)
    print("[Process ends. Session closed.]")
    print()

    # Session 2: A "new" process starts, but the agent remembers
    print("SESSION 2: New process, same agent")
    print("-" * 40)
    print("Creating AgentMemory('demo-agent') again...")
    agent2 = AgentMemory("demo-agent")

    print("\nAgent is asked: 'What is my favorite color?'")
    response = agent2.ask("favorite color")
    print(f"Agent responds: {response}")

    print("\nAgent is asked: 'What do I work on?'")
    response = agent2.ask("distributed systems")
    print(f"Agent responds: {response}")

    print("\nAgent is asked: 'Do I prefer long or short answers?'")
    response = agent2.ask("concise")
    print(f"Agent responds: {response}")

    # Show stats
    print("\n" + "=" * 60)
    print("AGENT MEMORY STATISTICS")
    print("=" * 60)
    stats = agent2.get_stats()
    print(f"Agent name:     {stats['agent']}")
    print(f"Memory lines:   {stats['memory_entries']}")
    print(f"Diary days:     {stats['diary_days']}")
    print(f"Total files:    {len(stats['files'])}")
    print()

    # Show the actual file contents
    print("=" * 60)
    print("MEMORY FILE CONTENTS")
    print("=" * 60)
    print(agent2.memory_file.read_text())
    print()

    print("=" * 60)
    print("DIARY FILE CONTENTS")
    print("=" * 60)
    for diary_file in sorted(agent2.diary_dir.iterdir()):
        print(f"\n--- {diary_file.name} ---")
        print(diary_file.read_text())

    print()
    print("=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)
    print("\nKey takeaway: The agent remembered across sessions.")
    print("No database. No API. Just files. The memory IS the agent.")


if __name__ == "__main__":
    demo()
