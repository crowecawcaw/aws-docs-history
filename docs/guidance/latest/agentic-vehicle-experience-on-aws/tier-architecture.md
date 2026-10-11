

# Architecture Overview
<a name="tier-architecture"></a>

AVX deploys a **two-tier agentic architecture**: Tier 1 conversational agents (Strands supervisor, <1 sec latency) paired with Tier 2 autonomous agents (scheduled daily, evidence-carrying artifacts). Both tiers share the same Finding \+ Action data model and executor dispatch abstraction, enabling cross-surface workflows (iOS cards → Tier 1 drill-down → DMS pre-brief → dealer approval → customer iOS action feed).

 **Tier 1 (conversational, <1 sec)** — AgentCore runtime runs a Strands supervisor agent (Claude Sonnet 4.6) that reads finished Tier 2 Findings from DynamoDB. Tools are thin: DDB reads, booking API calls, escalation. No reasoning inside tools. The supervisor narrates Findings, routes approvals to executors, and handles drill-down chat pre-seeded with evidence.

 **Tier 2 (autonomous, scheduled and event-driven)** — four loyalty-flywheel agents for owners and five Fleet Intelligence agents for fleets run on EventBridge Scheduler, event rules and, for engineering investigations, an Amazon SQS queue. Each agent owns a specific goal, reasons with Claude Sonnet 4.6, reads from the data platform at source, and writes an evidence-carrying Finding to DynamoDB. Tier 1 reads that Finding in a single DynamoDB call:
+  **Agent 1 — Energy & Charging Advocate** (`agent-1-energy`): runs daily per VIN and on charging-session end or tariff change. Reads ADP charging history and energy usage. Tier 1 read: `get_energy_advice()`.
+  **Agent 2 — Vehicle Health & Service Agent** (`agent-2-vehicle-health`): runs on ADP prediction / alert arrival, DTC event, telemetry threshold, or service-interval approach. Covers the service arc from detection through booking; the `dms` executor creates the repair order on customer approval. Tier 1 read: `get_health_findings()`.
+  **Agent 3 — Ownership Cost & Coverage Advocate** (`agent-3-ownership-cost`): runs on service event, warranty verdict change, recall publication, and tenure milestone, plus a daily prepaid sweep. The only agent with discount authority. Tier 1 reads: `get_coverage()`, `get_loyalty_standing()`.
+  **Agent 4 — Household Mobility Concierge** (`agent-4-concierge`): runs on finance milestone, household change, or equity threshold. Trade-in valuation output carries mandatory verbatim disclosure. Tier 1 read: `get_ownership_position()`.

The five Fleet Intelligence agents (cost, recall and warranty, fleet health, rebalancing, and fleet quality) write recommendations to the Fleet Intelligence Action Queue, where a fleet operator or product engineer approves each one; see [Fleet Intelligence agents](fi-agents.md).

A pluggable registry governs all nine agents. Each module provides a system prompt, its allowed Finding kinds, a read stack, and a Strands agent factory. The runner, artifact contract, executor dispatch, and delivery broker are shared.

Each Tier 2 agent runs on a schedule, an event or a request, produces a Finding with `computed_at`, `confidence`, `evidence[]`, `agent_version`, `inputs_hash`, and `finding_key` (stable-identity idempotency), and stores it in a DDB table with GSIs for owner / vehicle / fleet / dealership / district scopes.

 **Load-bearing constraints** (enforced by tests): - **Tier 1 tools must return <1 sec** (Nova Sonic tool-completion window is \~1 sec; exceeding it breaks audio TTS mid-session). - **Deterministic seams narrate verbatim** (triage P0 stop-driving rule, DMS warranty verdicts, payment authorization, disclosure copy). - **Agent-vs-tool vocabulary stays honest** (a `@tool` is a scoped retrieval callable, not an agent in the reasoning sense). - **Tier 2 artifacts carry their own evidence** (so Tier 1 can narrate staleness, confidence, and the reasoning trace without re-computing).

See [Tier 2 platform — autonomous agent-reasoning layer](tier-2-platform.md) for the Tier 2 design, [Cross-surface Actions framework](cross-surface-actions.md) for the Finding \+ Action model, and [Executor pattern — pluggable dispatch](cross-surface-actions.md#executor-pattern) for the pluggable dispatch.