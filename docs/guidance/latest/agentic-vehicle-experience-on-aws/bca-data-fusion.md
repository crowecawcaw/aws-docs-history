

# Session initialization and data-fusion pattern
<a name="bca-data-fusion"></a>

Each AVX session fuses data from both foundations into a coherent in-session context before the first tool is dispatched. The pattern has two phases: session initialization (sync, at session start) and tool dispatch (lazy, per-request).

## Session initialization
<a name="bca-init"></a>

When a new session begins — whether triggered by an incoming Connect call, a web chat message, or a mobile app request — the AVX handler executes the following initialization sequence before yielding to the supervisor agent:

1.  **Caller resolution.** The session-init step maps the incoming caller identifier (phone number, Cognito IdToken, or API key) to a tenant ID and a list of associated vehicles. If the caller has exactly one associated vehicle the VIN is auto-selected; if multiple, the supervisor asks the caller to confirm before proceeding.

1.  **CMS live-state read.** The handler reads the Redis LKS entry for the resolved VIN. This is a sub-millisecond read that returns the current telemetry snapshot: speed, RPM, coolant temperature, brake wear, tire pressures, active DTC codes (with severity flags), GPS position, and a timestamp. The snapshot is attached to the session context object and held for the session lifetime. All subsequent triage, booking, and escalation tool calls read from this snapshot rather than re-querying Redis on each turn.

1.  **ADP persona snapshot load.** The `persona_loader` issues a set of partition-scoped Athena queries against the ADP Glue tables in scope for the resolved persona. The result rows are serialized to JSON and written to AgentCore Memory as metadata-tagged records, using deterministic metadata keys (`persona_id`, `vehicle_id`, `customer_id`, `data_source`, `tenant_id`). Metadata is set by `persona_loader` — not derived by the LLM — so that subsequent tool calls can use exact-match filters to retrieve the right records without any semantic ambiguity.

The session-init persona load is bounded in both time and data volume. The in-scope ADP tables for a typical persona yield fewer than 100 KiB of JSON after serialization, and the Athena queries are partition-pruned by `vehicle_id` or `customer_id`. The resulting Memory write is colocated with the AgentCore runtime (same region), keeping the round-trip latency to a few hundred milliseconds.

## Tool dispatch
<a name="bca-tool-dispatch"></a>

After initialization, the supervisor dispatches tool calls in response to the caller’s questions. The data-fusion split at tool dispatch time is:


| Tool | Data source | Reason | 
| --- | --- | --- | 
|  `vehicle_identity()`  | AgentCore Memory LTM — filter: `data_source=vehicle_identity`, `vehicle_id=<vin>`  | Loaded at session init; sub-millisecond read; VIN decode does not change within a session. | 
|  `service_history()`  | AgentCore Memory LTM — filter: `data_source=service_records`, `vehicle_id=<vin>`  | Loaded at session init; historical records do not change within a session. | 
|  `charging_history()`  | AgentCore Memory LTM — filter: `data_source=charging_sessions`, `vehicle_id=<vin>`  | Loaded at session init; 30-day window snapshot. | 
|  `customer_profile()`  | AgentCore Memory LTM — filter: `data_source=customer_360`, `customer_id=<id>`  | Loaded at session init; profile snapshot for the session. | 
|  `interaction_history()`  | AgentCore Memory LTM — filter: `data_source=customer_interactions`, `customer_id=<id>`  | Loaded at session init; 50 most-recent interactions. | 
|  `ota_history()`  | AgentCore Memory LTM — filter: `data_source=ota_campaigns`, `vehicle_id=<vin>`  | Loaded at session init; 6-month window. | 
|  `triage()`  | CMS Redis LKS snapshot (held in session context) \+ tenant policy DynamoDB record | Live vehicle state; must reflect the vehicle’s condition at the moment of the call. | 
|  `book()`  | CMS DynamoDB `service-history` (write path); tenant booking config from DynamoDB | Writes back to CMS; requires live credentials scoped to the CMS account. | 
|  `escalate()`  | CMS session-state snapshot (assembled from LKS \+ DDB) \+ Amazon Connect queue config | Handoff payload carries live context; queue ARN is per-tenant config. | 
|  `knowledge()`, `parts_lookup()`, `retrieve()`  | ADP Bedrock KB cross-account Retrieve — filter: `source_category=<category>`  | Reference content; KB is the source of truth for DTC guides, TSBs, parts pricing. | 
|  `diy_repair_advisor()`  | Local triage rules \+ ADP Bedrock KB Retrieve (filter: `source_category=dtc_guide`) | Hybrid: local rules provide the decision tree; KB augments with procedure detail. | 

The split ensures that expensive cross-region or cross-account calls happen once at session start, not once per turn. Within a session, the vast majority of tool dispatches are in-region Memory reads or Bedrock Retrieve calls — both complete in tens to low hundreds of milliseconds.