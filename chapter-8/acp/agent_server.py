"""
agent_server.py
Run with:  python agent_server.py
Then visit: http://127.0.0.1:8000/agents to see the agent manifest.
"""
import asyncio
import ast
from collections.abc import AsyncGenerator

from acp_sdk.server import Server, Context, RunYield, RunYieldResume
from acp_sdk.models import Message, MessagePart

server = Server()                      # Creates the FastAPI app + /agents registry


@server.agent(name="calculator", description="Evaluates basic arithmetic like '2+2*3'")
async def calculator(                 # Signature required by ACP  :contentReference[oaicite:2]{index=2}
    inputs: list[Message],            # Chat‑style inputs
    context: Context
) -> AsyncGenerator[RunYield, RunYieldResume]:

    for msg in inputs:
        expr = msg.parts[0].content

        # 1️⃣ stream a “thought” back to caller
        yield {"thought": f"Computing {expr!r} …"}

        # 2️⃣ do the work (very naive, safe only for demo)
        await asyncio.sleep(0.2)      # pretend it’s expensive
        try:
            tree = ast.parse(expr, mode="eval")
            if not all(isinstance(n, (ast.Expression, ast.BinOp, ast.UnaryOp,
                                       ast.Num, ast.operator, ast.unaryop))
                       for n in ast.walk(tree)):
                raise ValueError("unsupported input")
            result = eval(compile(tree, filename="<expr>", mode="eval"))
        except Exception as exc:
            result = f"⚠️  error: {exc}"

        # 3️⃣ send the final answer
        yield Message(
            parts=[MessagePart(content=str(result), content_type="text/plain")]
        )


if __name__ == "__main__":
    # runs uvicorn with sensible defaults (incl. OpenTelemetry hooks)
    server.run(port=8000)
