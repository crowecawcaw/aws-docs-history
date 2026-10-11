

# AVX as a composition layer
<a name="arch-composition-layer"></a>

AVX does not own a vehicle database or a knowledge corpus. It composes three external platforms, each of which is independently deployable and independently governed, and exposes their capabilities through a single agentic interface.

The three foundations are described below.

## Connected Mobility (CMS)
<a name="arch-foundation-cms"></a>

CMS is the real-time vehicle state and fleet management platform. It provides:
+  **DynamoDB tables** — vehicles, drivers, trips, service history, maintenance alerts, warranty claims, and triage decisions. These tables are the authoritative record of what has happened to a vehicle and what its current operational state is.
+  **Redis Last-Known-State (LKS)** — a sub-millisecond cache of the most recent telemetry snapshot per vehicle (speed, RPM, coolant temperature, brake wear, tire pressure, active diagnostic trouble codes). AVX reads this store at session initialization to ground every turn with live vehicle state without querying the message bus on each request.
+  **IoT Core \+ MSK/Flink pipeline** — the continuous telemetry ingestion path. IoT Core receives raw vehicle signals; Flink processors normalize, enrich, and project them into DynamoDB and Redis. AVX does not participate in this pipeline; it reads its outputs.
+  **Recalls integration** — NHTSA recall open/closed status per VIN, reachable via a CMS Lambda-backed API.

In an AVX deployment, CMS is a prerequisite. The `book()` tool, which creates service appointments and links them to DMS ticket systems, writes back to CMS service-history tables. The `escalate()` tool, which hands a call to a tier-2 agent, carries the CMS session-state snapshot as the handoff context payload.

## Automotive Data Platform (ADP)
<a name="arch-foundation-adp"></a>

ADP is the governed analytical data platform that publishes the curated data products AVX needs for persona grounding and reference knowledge retrieval. It provides two surfaces to AVX:
+  **Tabular data products via cross-account Lake Formation grants** — Vehicle Identity (VIN decode, make/model/year/powertrain), Parts Catalog (OEM part numbers, pricing, availability), Service Network (dealer and service-center locations, specialties, hours), Vehicle Lifecycle (warranty terms, warranty coverage windows, campaign history), and customer and interaction data products. At session initialization, AVX’s `persona_loader` issues partition-scoped Athena queries against ADP Glue tables and seeds the result into AgentCore Memory metadata-tagged long-term memory (LTM). Subsequent tool calls within the session retrieve records from Memory rather than re-querying Athena, bounding both latency and cross-region data-transfer cost.
+  **Bedrock Knowledge Base (cross-account Retrieve)** — ADP hosts a Bedrock Knowledge Base backed by an Amazon S3 Vectors index, loaded with automotive reference content: DTC diagnostic guides, Technical Service Bulletins (TSBs), recall notices, owner manuals, service policies, and parts catalog narratives. AVX tools invoke Bedrock Retrieve cross-account with source-category filters, retrieving the subset of the corpus relevant to the current persona and query rather than the full document set.

ADP’s cross-account Lake Formation share and the Bedrock KB resource policy are the two authorization boundaries between ADP and AVX. These boundaries are parameterized in CDK context (`adpAccountId`, `cvxKbPrincipals`) and support both same-account cross-region (current staging topology) and full cross-account customer deployments.

**Note**  
The `vehicle_telemetry_aggregated` and `energy_usage` products depend on the `PySpark via Glue` data pipeline in ADP. The `telemetry_summary` and `energy_summary` tools are deployed and query AgentCore Memory for those data sources; until the upstream ADP Glue tables are registered, the `persona_loader` skips the Athena fetch and each tool returns `{"available": false}`. No code change is required when the pipeline ships — the tools automatically serve data as soon as Memory contains the records.

## Amazon Connect
<a name="arch-foundation-connect"></a>

Amazon Connect is the contact center platform AVX hands a conversation to when it needs a person. AVX does not replace Amazon Connect; it extends it:
+  **Voice and text channels** — the driver talks to AVX in the app: by voice over a WebSocket to the AgentCore bidirectional runtime, with Amazon Nova 2 Sonic speech-to-speech, or by text through `POST /assistant/chat`. Both channels escalate into Connect the same way.
+  **Human handoff** — when the triage classifier returns P0 (Stop Driving) or P1, the app shows a card with **Talk to an agent** (and **Request roadside** on P0); a customer can also ask for a person at any time. The driver’s tap reaches `/escalate`, which starts a Connect chat on the tenant’s chat queue. The contact attributes and the chat’s first message carry the triage classification, the reason, the VIN and vehicle, the driver and a conversation summary. On a verified P0, a tenant can also have Connect call the assigned driver back.