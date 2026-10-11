

# Tier 2 platform — autonomous agent-reasoning layer
<a name="tier-2-platform"></a>

Tier 2 agents run as Lambda functions triggered by EventBridge Scheduler (daily, per-VIN or per-fleet), EventBridge event rules (DMS repair-order status, warranty verdict change, recall publication, ADP prediction arrival), or an Amazon SQS queue (a product engineer’s investigation request). Each agent reads the data platform at source, reasons with Claude Sonnet 4.6, and writes a Finding to DynamoDB. Tier 1 tools read those Findings in a single DynamoDB call.

![Tier 2 autonomous agents architecture in five zones: EventBridge Scheduler, EventBridge event rules and Amazon SQS start agent runs, and Amazon Athena reads ADP and DMS tables at source; AWS Lambda runs four flywheel agents and five fleet agents that call Claude Sonnet 4.6 on Amazon Bedrock with Bedrock Guardrails, with run records and missed-run and cost alarms; Findings are written to the avx-findings DynamoDB table, where the outreach broker applies consent, quiet hours and caps and sends an Amazon SNS push hook to the app cards and portal queues; an owner, fleet operator or product engineer approves through Amazon API Gateway, or an auto-approval rule approves a vehicle move, and each Action passes guardrails G1 to G5 in registry.dispatch(); eight executors call the DMS, CMS and ADP APIs, and DMS repair-order status events from Amazon EventBridge advance each Action.](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-tier2-architecture.png)


## Why Tier 2 is necessary
<a name="why-tier-2-is-necessary"></a>

A voice-session tool call has a \~1 second budget (Nova Sonic’s post-tool TTS window). Querying vehicle health history, running statistical analysis, and composing narration exceeds that budget by orders of magnitude. Tier 2 moves that work outside the conversation: scheduled, with full history, producing a result that Tier 1 reads fast.

 **Example: "How is my battery?"** 
+ Tier 2 agent (overnight): reads 6 months of battery state-of-health data from the ADP `battery_soh` product, fits a degradation curve, and compares the result to the vehicle’s tenure and to similar vehicles. Writes a Finding: `computed_at: 2026-07-14T02:15:00Z`, `confidence: high`, `headline: "Battery health is within normal range for this vehicle’s age and usage"`, `evidence: [{kind: "soh_trend", value: "99%_after_6mo"}]`, `tokens_used: 8750`.
+ Tier 1 agent (during a voice turn, <1 sec): reads that Finding from DynamoDB in \~15 ms. Narrates: "Your battery is in good shape — 99% health after six months." Surfaces `computed_at`: "We ran this check last night at 2 AM." No re-computation.

## Platform substrate
<a name="platform-substrate"></a>

The agent registry is pluggable. Each agent module provides:
+ A system prompt scoped to the agent’s goal
+ The Finding kinds it is permitted to write (enforced at write time)
+ A read stack — cross-account Athena queries against ADP curated products, DMS tables, or both
+ A Strands agent factory (`make_strands_agent_fn`)

The runner, Finding table, artifact contract, executor dispatch, broker, and observability stack are shared across all agents. To add an agent, register a module; no changes to the substrate are required.

Tier 2 reads the data platform at source — cross-account Athena on ADP curated products and DMS tables. It does not read AgentCore Memory; Tier 2 runs have no session context.

## Triggers
<a name="triggers"></a>


| Trigger | When used | 
| --- | --- | 
| EventBridge Scheduler (daily, per-VIN) | Battery SoH trend, tire health sweep, charging plan, household equity check | 
| EventBridge event rule: `dms.repair-order.status_changed`  | Warranty verdict narration, coverage check after service completion | 
| EventBridge event rule: ADP prediction arrival | Tire or brake alert — immediate response to a new prediction | 
| EventBridge event rule: recall publication | Coverage check for a new open recall | 
| EventBridge event rule: finance milestone or tenure threshold | Household concierge position update | 
| EventBridge Scheduler (daily, Fleet Intelligence) | Cost at 04:00 UTC, recall at 05:00, warranty at 05:20, fleet health at 05:40, rebalancing at 06:00. Each runs after the ADP jobs it reads and after the nightly vehicle health runs (02:00–02:40). See [Fleet Intelligence agents](fi-agents.md). | 
| Amazon SQS queue: engineer investigation request | Fleet-quality investigation of a fault pattern, started from the Connected Services portal | 

## Operational controls
<a name="operational-controls"></a>


| Parameter | Configuration | 
| --- | --- | 
| LLM | Claude Sonnet 4.6 (`us.anthropic.claude-sonnet-4-6`) via cross-region inference profile | 
| Per-run cost cap | SSM `/vsa/{stage}/tier2/{agent_id}/cost-cap-usd`; enforced by the runner; CloudWatch alarm on exceeded | 
| Dry-run mode |  `VSA_TIER2_DRY_RUN=1` — runs reasoning, writes no Findings | 
| Decision replay | Every run stores inputs and reasoning trace in `audit_trail[]`; supports "why this, why now?" queries | 
| Alarms | CloudWatch alarms on Lambda `Errors`, cost-cap exceeded, and scan failures, plus a staleness alarm per scheduled component that fires when a run is missed. All alarm actions publish to the operator SNS topic `vsa-{stage}-tier2-operator-alerts`  | 
| Run records | Every run writes a record to `vsa-{stage}-avx-agent-runs`, keyed `<agent_id>#<component>`: start and finish, `completed` or `aborted`, counts, and `agent_version`. A screen reads the latest record to say when an agent last ran and to show a missed run as stale | 

Run an agent in pull-only mode first — Finding \+ Tier 1 read tool — and validate reasoning on real data before enabling proactive delivery.

## Finding data model
<a name="finding-data-model"></a>

Findings are stored in `vsa-{stage}-avx-findings`. See [Cross-surface Actions framework](cross-surface-actions.md) for the canonical schema. Each Finding carries:


| Field group | Fields | 
| --- | --- | 
| Identity |  `finding_id`, `finding_key` (SHA-256 of agent\_id \+ scope field/value \+ finding\_kind; persistent conditions update in place rather than creating a duplicate) | 
| Provenance |  `agent_id`, `agent_version`, `computed_at`, `expires_at`, `inputs_hash` (idempotency key), `tokens_used`, `cost_usd`  | 
| Classification |  `severity` (`p0\|attention\|soon\|routine\|informational`), `finding_kind`, `confidence` (`low\|medium\|high`) | 
| Scope | Exactly one of: `vin`, `owner_id`, `fleet_id`, `dealership_id`, `district_id`, `population_id`  | 
| Content |  `headline` (≤120 chars), `detail` (markdown), `evidence[]` — each entry: `kind`, `source`, `source_ref`, `value`, `computed_at`, `provenance: live\|mocked\|absent`, `vin` (optional) | 
| Disclosure |  `disclosure_txt` — verbatim disclosure copy for monetary Findings; `null` otherwise | 
| Audit |  `audit_trail[]`  | 

 **Idempotency**: `inputs_hash` is a SHA-256 of the canonicalized inputs (VIN, component\_id, data `snapshot_date`, agent\_version). On re-run, the agent issues conditional `PutItem`. If a Finding with the same hash exists within the TTL window, the run writes nothing. This prevents duplicate notifications and duplicate audit-trail entries.