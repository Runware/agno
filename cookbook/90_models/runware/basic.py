"""
Runware Basic
=============

Cookbook example for Runware, OpenAILike model provider.
"""

import asyncio

from agno.agent import Agent
from agno.models.runware import Runware

# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------

agent = Agent(model=Runware(id="openai-gpt-5-mini"), markdown=True)

# You can also select the provider by string, which resolves to the same class:
# agent = Agent(model="runware:openai-gpt-5-mini", markdown=True)

# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # --- Sync ---
    agent.print_response("Explain quantum computing in simple terms")

    # --- Sync + Streaming ---
    agent.print_response("Explain quantum computing in simple terms", stream=True)

    # --- Async ---
    asyncio.run(agent.aprint_response("Share a 2 sentence horror story"))

    # --- Async + Streaming ---
    asyncio.run(
        agent.aprint_response(
            "Write a short poem about artificial intelligence", stream=True
        )
    )
