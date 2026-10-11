

# The Finding Contract
<a name="ap-finding-contract"></a>

A Tier 2 agent writes a Finding to `vsa-{stage}-avx-findings`. The Finding carries the evidence, provenance, and timestamps that Tier 1 needs to narrate accurately and that operators need to audit the reasoning after the fact.


| Field | Type | Semantics | 
| --- | --- | --- | 
|  `finding_id`  | String (`FIND-{uuid}`) | Stable UUID, set on creation. Preserved across in-place updates. The persistent identity for cross-system audit. | 
|  `finding_key`  | SHA-256 hex | The stable identity of a persistent condition on a scope. Computed from `(agent_id, scope_field, scope_value, finding_kind)`. Before writing, the agent queries this key. If an open row exists (not yet expired), the agent updates it in place — extending `expires_at`, refreshing evidence, appending to `audit_trail`. If no open row exists, the agent writes a new `PutItem` with a new `finding_id`. Cross-run idempotency is `finding_key`-based, not `inputs_hash`-based. | 
|  `agent_id`  | String | Which agent module produced this Finding. For example, `agent-2-vehicle-health`. Stable per module; enables per-agent queries. | 
|  `agent_version`  | String (semantic version) | The exact version that produced this Finding. Immutable after write. | 
|  `scope`  | Object | Exactly one of `vin`, `owner_id`, `fleet_id`, `dealership_id`, `district_id`, or `population_id` is populated. Consumer and vehicle-owner personas scope to `vin`. Fleet-owner personas scope to `fleet_id` with per-VIN attribution in `evidence[]`. Dealership and district scopes are for pre-brief agents. Population scope (`population_id`, the vehicle maker’s id) is for fleet-quality investigations, which no fleet queue shows. | 
|  `severity`  |  `p0 \| attention \| soon \| routine \| informational`  | Customer-visible urgency. Derived from the triage classifier for safety Findings; set by the agent for all others. The broker reads severity as the primary channel-selection signal. By default, only `p0` triggers an APNs push; every severity creates an in-app card. | 
|  `computed_at`  | ISO-8601 UTC | When the agent’s reasoning completed. Tier 1 narrates "as of …​" using this value. | 
|  `expires_at`  | ISO-8601 UTC | When this Finding leaves the active query window. Each agent sets its own freshness TTL. Expired Findings are invisible to queries but retained for audit. | 
|  `confidence`  |  `low \| medium \| high`  | The agent’s confidence in its reasoning. Tier 1 adjusts narration tone accordingly. | 
|  `finding_kind`  | String (enum) | The logical category: `health.tires`, `health.brakes`, `health.battery` (Agent 2); `energy. ` (Agent 1); `coverage.`, `loyalty. ` (Agent 3); `concierge.` (Agent 4); `fleet.cost. `, `fleet.recall.vehicle`, `fleet.warranty.claim_candidate`, `fleet.health.service`, `fleet.rebalance.` (Fleet Intelligence agents); `quality.investigation`, `quality.issue` (fleet-quality agent). Determines the card template and which executor targets are relevant. | 
|  `headline`  | String (≤120 chars) | Human-readable title. Rendered as the card headline and as the push notification body. The flywheel agents and the cost agent write it with the LLM; the other Fleet Intelligence agents fill a fixed template, and their model writes only `detail`. For `p0` Findings, the headline carries the triage classifier’s verbatim stop-driving phrase without paraphrase. | 
|  `detail`  | String (Markdown) | LLM-generated explanation with evidence citations. Rendered in the card drawer and narrated by Tier 1 on drill-down. | 
|  `evidence[]`  | Array of objects | Every input signal and intermediate result that produced this Finding. Each entry carries `kind`, `source`, `source_ref`, `value`, `computed_at`, `provenance` (`live \| mocked \| absent`), and optionally `vin` for fleet-scoped Findings. Required for audit and for the Tier 1 reasoning drawer. | 
|  `inputs_hash`  | SHA-256 hex | Hash of the canonical input rows for this execution attempt. Scoped to retry-safety within a single run. Two attempts with the same hash are treated as duplicates. | 
|  `tokens_used`  | Integer | Zero when the deterministic fallback ran; positive when the LLM path ran. Tier 1 uses this to distinguish agent reasoning from system-computed signals. | 
|  `cost_usd`  | Float | Per-Finding inference cost. Zero when the deterministic path ran. Aggregated for cost monitoring. | 
|  `disclosure_txt`  | String (verbatim) | Populated only when the Finding surfaces a monetary figure. Contains the exact disclosure text that Tier 1 narrates and the app displays. No paraphrase. See [Deterministic Seams and Guards](ap-deterministic-seams.md). | 
|  `audit_trail[]`  | Array of objects | Appended on every in-place update. Each entry records `at`, `agent_version`, `inputs_hash`, `from_expires_at`, `to_expires_at`, and an optional `note`. The full update history is reconstructable from the Finding alone. | 

## Why the contracts are structured this way
<a name="why-the-contracts-are-structured-this-way"></a>

Evidence is what separates a Finding from an assertion. Without `evidence[]`, an operator cannot determine why the agent reached a conclusion. Without `computed_at` and `expires_at`, Tier 1 cannot tell the owner how fresh the reasoning is. Without `finding_key`, a persistent tire-wear condition accumulates redundant rows instead of updating in place.

The `inputs_hash` field only prevents two concurrent execution attempts from writing duplicate rows within the same run. It does not determine whether a condition is new or persistent; `finding_key` does that.

## Finding lifecycle
<a name="finding-lifecycle"></a>

1.  **Emission** — The agent validates the schema, computes `finding_key`, and either updates the existing open row or writes a new one.

1.  **Delivery** — The broker stream-processes the write from a DynamoDB stream on the table. It evaluates consent, rate limits, cardinality cap, and feedback demotion. It decides whether the Finding produces an in-app card only, or a card and an APNs push.

1.  **Narration** — When the owner opens the card or starts a Tier 1 session, the agent narrates `headline`, `detail`, and `disclosure_txt` (where present) without editorializing.

1.  **Action** — The owner approves or dismisses. Approval creates an Action row and routes it to the executor. Dismissal sets `Action.status = dismissed`, records feedback in the broker’s demotion table, and closes the card.

1.  **Expiry** — At `expires_at`, the Finding leaves the active query window. The artifact row is retained.