

# Sub-agent-as-tool pattern
<a name="sub-agent-as-tool"></a>

In Strands, specialist agents are exposed to the supervisor as `@tool`-decorated Python callables. The supervisor’s LLM sees each specialist as a named tool with a schema; it decides which tool(s) to call based on the customer’s intent and the triage classification.

## Pattern implementation
<a name="pattern-implementation"></a>

```
from strands import tool

@tool
def triage(
    dtc_codes: list[str],
    telemetry_flags: list[str],
    recall_ids: list[str],
    tenant_policy_overrides: dict,
) -> dict:
    """Classify vehicle criticality on the P0–P3 taxonomy.

    Args:
        dtc_codes: Active DTC codes from the vehicle's OBD-II port.
        telemetry_flags: Active threshold breaches (e.g. coolant_temp_high).
        recall_ids: Open NHTSA recall IDs for this VIN.
        tenant_policy_overrides: Tenant-specific escalation overrides.
    """
    # Deterministic rule engine — no LLM call inside this tool
    return _run_triage_classifier(
        dtc_codes, telemetry_flags, recall_ids, tenant_policy_overrides
    )
```

The `@tool` decorator generates the LLM-visible JSON schema from the function’s type annotations and Google-style docstring. The supervisor LLM never sees the tool’s implementation — only the schema and the return value.

## Why sub-agents must return fast: Nova 2 Sonic tool-completion window
<a name="why-sub-agents-must-return-fast-nova-2-sonic-tool-completion-window"></a>

**Note**  
This constraint is platform-level and **cannot be worked around in application code**. Every sub-agent or tool the supervisor calls during a voice session must complete within approximately one second.

Amazon Nova 2 Sonic v2 has a tool-completion budget of approximately **1 second**. When a tool call exceeds this window, Nova’s post-tool text-to-speech synthesis goes silent — the agent stops speaking for the rest of the session, until the 55-second AgentCore session timeout fires. This was verified empirically: a Strands tool making an LLM call (≈ 3 seconds for Claude Sonnet, ≈ 2 seconds for Haiku) consistently broke Nova’s TTS output.

The correct pattern for retrieval-heavy tools is:

1.  **Return retrieved content, do not synthesize inside the tool.** The tool fetches from the Knowledge Base or DynamoDB and returns raw content. Nova synthesizes the spoken response herself using her own bidi inference — she is already running and optimized for this.

1.  **Cache hot queries.** Triage classifier output and vehicle-state lookups are stable within a session; cache at session-init rather than repeating on every tool call.

1.  **Use the narration-injection pattern for tool results.** After a tool returns, inject the narration text as a separate `asyncio.create_task(agent.send(…​))` — never inline from inside `output_callable`. The Strands re-entrancy constraint means inline `await agent.send(…​)` from within the output callback is silently dropped.

```
async def output_callable(event: dict) -> None:
    if event.get("type") == "tool_result":
        narration = extract_narration(event)
        if narration:
            # CORRECT: schedule outside the callback's call stack
            asyncio.create_task(
                agent.send(f"Tell the driver: {narration}"),
                name="narration-injection"
            )
            # WRONG: await agent.send(narration)  -- silently dropped
```