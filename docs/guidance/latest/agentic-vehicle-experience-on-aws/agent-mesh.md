

# Supervisor and specialist agent mesh
<a name="agent-mesh"></a>

The AVX agentic layer is organized as a **supervisor \+ specialist mesh**. The supervisor agent receives every customer interaction, classifies intent, and delegates to the appropriate specialist tools as Strands `@tool`-decorated callables. Specialist logic is encapsulated in focused, independently testable tool implementations with well-defined contracts.

## Mesh topology
<a name="mesh-topology"></a>

The supervisor agent runs on AgentCore, receives every customer interaction, and dispatches to `@tool`-decorated callables. Specialist logic is encapsulated in tools registered per-persona in `PERSONA_TOOL_FACTORIES` (`agents/supervisor/tools/init.py`). Multi-tenant configuration is loaded from the `vsa-tenant-config` DynamoDB record at session start; per-tenant KB, branding, policy, and tool enablement are all configurable without code changes.

The supervisor agent sits at the top of the mesh. It calls Triage first on every session, then routes to the appropriate specialist(s) based on classification and customer intent.

```
VSA SUPERVISOR  (per session)
  Claude Sonnet 4.6 via Bedrock inference profile
  Tenant-aware system prompt + per-persona tool registry
  Calls triage first, then routes
        │
   ┌────┼──────────────────────┬──────────────────────────┐
   │    │                      │                          │
triage  book/escalate   fleet_intelligence     DMS persona tools
tool    tools           (fleet_manager)        (warranty_agent,
   │                                            dm_copilot,
   └── P0–P3 classification                     comms_triage,
       + reason trace                           parts_intel)
```

## Supervisor agent
<a name="supervisor-agent"></a>

The supervisor is a Strands `BidiAgent` (voice) or `Agent` (text) running Claude Sonnet 4.6 via the `us.anthropic.claude-sonnet-4-6` cross-region inference profile. Its responsibilities:
+ Authenticate the caller and resolve the vehicle (VIN) and tenant at session start.
+ Call the Triage tool on every session to classify criticality before any other action.
+ Select and invoke specialist tools based on classification and customer intent.
+ Synthesize a coherent, voice-friendly response from specialist outputs.
+ Emit a STAR-JSON service ticket and offer escalation when appropriate.

The supervisor’s system prompt is the source of persona, tone, and routing logic. It is constructed at session start from the tenant config record, incorporating per-tenant branding and tool-enablement policies.

## Triage tool
<a name="triage-tool"></a>

The `triage` tool calls the deterministic-first P0–P3 criticality classifier (`lambdas/triage-classifier/`). See [Deterministic-first P0–P3 triage](triage-classifier.md) for the full specification.

## Booking tool (STAR-JSON)
<a name="booking-tool-star-json"></a>

Booking is a tool, not a separate agent. The `book` tool (`agents/supervisor/tools/book.py`) builds a STAR-JSON `ServiceRequestAdd` envelope and writes a `scheduled` row to the CMS service-history table; the companion app books appointment times through `POST /book`. See [Booking (STAR-JSON)](booking-agent.md).

## Session context
<a name="session-context"></a>

At session start, the session-init step in `agents/supervisor/agentcore_app.py` resolves the caller’s phone number or account ID to a tenant, VIN, and driver identity. Loads live vehicle state from the CMS Redis Last-Known-State (LKS) cache and seeds the session’s `SessionContext` object. Enforces consent prompts per tenant config.

## Fleet manager tools
<a name="fleet-manager-tools"></a>

The `fleet_manager` persona accesses fleet-aggregate data through two tools that read the CMS Fleet Intelligence API (`services/fleet_intelligence/` in the CMS repository, which also backs the CMS Fleet Intelligence portal), and explains Action Queue items through a third that reads AVX’s own tables:


| Tool | Responsibility | Reads | 
| --- | --- | --- | 
|  `fleet_lifecycle`  | Fleet vehicle lifecycle summary — vehicles approaching end-of-life, compliance status, and service-due counts | CMS Fleet Intelligence API `GET /api/v1/fleet-intelligence/lifecycle`  | 
|  `fleet_cost_outliers`  | Cost-per-mile outliers — the fleet’s mean cost per mile, the outlier threshold (a multiple of the mean), and each outlier’s cost per mile, total cost and miles, highest first | CMS Fleet Intelligence API `GET /api/v1/fleet-intelligence/cpm/outliers`  | 
|  `fleet_recommendation`  | Answers "why did you recommend this?" for one Action Queue item: the Finding’s headline, detail and evidence, the recommended action, the decision Action and the queue status. For a recall or a stop-driving fault it returns `safety_text`, which the assistant reads word for word. No model call and no ADP query; it checks the caller’s fleet standing as the queue does | AVX `vsa-{stage}-avx-findings` and `vsa-{stage}-avx-actions`  | 

The `fleet_manager` persona is text-only (non-bidi). The lifecycle read takes approximately 2.6 seconds on staging, which exceeds Nova Sonic’s \~1 second tool budget, so the persona is explicitly excluded from the bidirectional voice runtime.

All three tools return `{available: false, reason: "…​"}` on any failure, so the supervisor agent always receives an explicit signal rather than an empty result that reads as "nothing flagged."

## Extending the specialist tool set
<a name="extending-the-specialist-tool-set"></a>

Additional per-tenant specialist tools can be loaded conditionally from the tenant config record. To add a tenant-specific tool — for example, a rental-policy handler for mileage-cap flows, or a fleet-SLA checker — implement it as a `@tool`-decorated callable, register it in `PERSONA_TOOL_FACTORIES` for the target persona, and enable it via the tenant config record’s `tool_overrides` field. No changes to the supervisor agent are required to add or remove tools for a tenant.