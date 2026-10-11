

# Add a Specialist Agent or Tool
<a name="extend-specialist-tool"></a>

## The @tool and sub-agent-as-tool pattern
<a name="extend-tool-pattern"></a>

Every capability the supervisor agent can invoke is registered as a Strands `@tool`-decorated function. The `agents/supervisor/tools/` directory contains all tool implementations; the registry in `agents/supervisor/tools/init.py` exports them as factories and maps them to personas via `PERSONA_TOOL_FACTORIES`.

A tool factory takes a `SessionContext` and a `Config` and returns the decorated function. This closure pattern keeps the session’s `tenant_id`, JWT, and `session_id` out of the LLM-visible signature while still making them available at call time:

```
# agents/supervisor/tools/my_new_tool.py
from strands import tool
from agents.supervisor.session import SessionContext
from agents.supervisor.config import Config

def make_my_new_tool(ctx: SessionContext, config: Config):
    @tool
    def my_new_tool(query: str) -> dict:
        """One-sentence description Nova uses for routing decisions."""
        # ... implementation ...
        return {"result": "..."}
    return my_new_tool
```

After implementing the factory, register it in `agents/supervisor/tools/init.py`:

```
from agents.supervisor.tools.my_new_tool import make_my_new_tool

__all__ = [
    # ... existing entries ...
    "make_my_new_tool",
]

PERSONA_TOOL_FACTORIES: dict[str, list] = {
    "fleet_driver": [
        # ... existing factories ...
        make_my_new_tool,   # <-- add here for the personas that need it
    ],
    # ... other personas ...
}
```

## Nova 2 Sonic latency constraint
<a name="extend-tool-latency"></a>

Nova 2 Sonic’s bidi loop assumes tool calls return within approximately one second. Tools that exceed this window cause Nova’s post-tool TTS to go silent for the remainder of the session — a hard operational constraint discovered during early development (see [Agentic Architecture](agentic-architecture.md)).

The production-safe pattern is the **retrieval-only sub-agent**: the tool returns raw KB content and Nova synthesizes the spoken response herself. `diy_repair_advisor` and `knowledge` follow this pattern. `agents/supervisor/tools/sub_agent.py` provides `make_sub_agent_tool` and `SubAgentConfig` as the reusable factory for this pattern:

```
# Example: a new recall-lookup sub-agent pointing at the tsb-recalls corpus
from agents.supervisor.tools.sub_agent import make_sub_agent_tool, SubAgentConfig

recall_config = SubAgentConfig(
    name="recall_lookup",
    description=(
        "Look up open recalls and TSBs for the current vehicle. "
        "Call this when the driver asks about recalls, campaigns, or safety notices."
    ),
    corpus_subdir="tsb-recalls",   # directory under corpora/
)

def make_recall_lookup_tool(ctx, config):
    return make_sub_agent_tool(recall_config, ctx=ctx)
```

**Note**  
 `make_sub_agent_tool` loads `.md` files from `corpora/<subdir>/` at module import and returns raw text. Adding new content requires a code change and a full agent redeploy. To update content without a redeploy, replace `_load_corpus(subdir)` with a Bedrock Knowledge Base query call. See [Content-as-Config](extend-content-as-config.md) for the KB update workflow.