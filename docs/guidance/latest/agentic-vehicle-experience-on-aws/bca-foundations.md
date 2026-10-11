

# The two foundations
<a name="bca-foundations"></a>

AVX treats CMS and ADP as external service providers, not internal modules. Each foundation is independently deployable and independently governed. AVX holds no vehicle database, no knowledge corpus, and no analytical data lake of its own — all of that lives in the foundations.

![AVX data grounding architecture in five zones: the ADP foundation lake on Amazon S3 holds reference documents tagged by source_category and curated Iceberg data products, encrypted with AWS KMS; Amazon Bedrock Knowledge Bases embeds the documents with Titan Text Embeddings V2 into Amazon S3 Vectors, which is reached only through the knowledge base, and the AWS Glue Data Catalog and AWS Lake Formation govern the tables; AVX reads across accounts with a Bedrock Retrieve call filtered by source_category, Amazon Athena through Lake Formation GetDataAccess, and CMS live state from Redis and the vehicle and service records; the Tier 1 runtime on Amazon Bedrock AgentCore writes a session snapshot to AgentCore Memory, while Tier 2 agents on AWS Lambda, started by schedules and events, read source data directly; Tier 2 writes Findings with evidence and freshness to Amazon DynamoDB, which Amazon API Gateway serves to the app cards and portal queues and Tier 1 narrates with its computed_at time.](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-data-foundation-architecture.png)


## CMS: live operational state
<a name="bca-cms"></a>

The Connected Mobility (CMS) platform provides the real-time operational view of every vehicle in the fleet. From AVX’s perspective, CMS exposes five data surfaces:


| CMS surface | What AVX reads from it | 
| --- | --- | 
| DynamoDB — `vehicles`  | VIN registration, enrollment date, tenant association, device UUID. Read at session init to confirm VIN ownership and tenant binding before any tool is dispatched. | 
| DynamoDB — `trips`, `service-history`  | Trip records (start/end, distance, events) and service history (date, type, provider, cost, linked DMS ticket ID). Read per-VIN by the `service_history` and `interaction_history` tools. | 
| Redis Last-Known-State (LKS) | Sub-millisecond telemetry snapshot: speed, RPM, coolant temperature, brake wear estimate, tire pressure per wheel, active diagnostic trouble codes (DTC codes with severity), and GPS position. Read once at session initialization; the snapshot is held in session context for the duration of the conversation so that every subsequent tool call — including `triage()` — works from a consistent point-in-time picture of the vehicle. | 
| IoT Core / MSK\+Flink pipeline outputs | AVX does not subscribe to the telemetry pipeline directly. It reads the pipeline’s outputs (DynamoDB \+ Redis) via the same Lambda-backed CMS APIs that the CMS Fleet Intelligence portal uses. | 
| Recalls integration | NHTSA recall open/closed status per VIN, reachable via the CMS `recall-integration` Lambda. The `triage()` tool factors open recalls into its P0–P3 classification, and the supervisor surfaces recall context in its response. | 

CMS is a hard prerequisite. The `book()` tool writes service appointments back to the CMS `service-history` table, and the `escalate()` tool packages the CMS session-state snapshot as the handoff payload to a tier-2 agent. If CMS is not deployed, neither of those tools can complete successfully.

## ADP: reference and curated data
<a name="bca-adp"></a>

The Automotive Data Platform (ADP) provides the governed data products that give AVX its automotive depth. ADP exposes two surfaces to AVX:

### Tabular data products (cross-account Lake Formation)
<a name="bca-adp-tabular"></a>

ADP publishes curated Iceberg tables through AWS Lake Formation v4 wildcard cross-account grants. AVX’s AgentCore execution role receives `lakeformation:GetDataAccess` on the in-scope ADP databases and issues Athena queries against them at session initialization. The results are loaded into AgentCore Memory LTM (see [Session initialization and data-fusion pattern](bca-data-fusion.md) below).

The in-scope ADP data products, and the personas that consume each, are:


| ADP data product | Fleet Driver | Consumer | Retail Advisor | Vehicle Owner | Service Advisor | Technician | 
| --- | --- | --- | --- | --- | --- | --- | 
| Vehicle Identity (VIN decode, make/model/year/powertrain) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Service Records (repair history, providers, costs) | ✓ | — | — | ✓ | ✓ | ✓ | 
| Charging Sessions (EV session history, energy) | ✓ | ✓ | — | ✓ | — | — | 
| Customer 360 (profile snapshot, preferences) | — | ✓ | ✓ | ✓ | ✓ | — | 
| Customer Interactions (prior contact history) | — | ✓ | ✓ | — | ✓ | — | 
| OTA Campaigns (software update history and pending campaigns) | ✓ | ✓ | — | ✓ | — | — | 
| Vehicle Telemetry Aggregated | ✓ | — | — | ✓ | — | — | 
| Energy Usage | ✓ | ✓ | — | — | — | — | 

The `vehicle_telemetry_aggregated` and `energy_usage` products depend on the `PySpark via Glue` data pipeline in ADP. The tools for these products (`telemetry_summary`, `energy_summary`) are deployed and query AgentCore Memory using the appropriate `data_source` filter; until the upstream ADP Glue tables are registered, the `persona_loader` skips the Athena fetch for these products and the tools return a structured `{"available": false}` response.

### Bedrock Knowledge Base (cross-account Retrieve)
<a name="bca-adp-kb"></a>

ADP hosts a Bedrock Knowledge Base backed by an Amazon S3 Vectors index. The corpus contains automotive reference content indexed by `source_category`:


|  `source_category`  | Content | 
| --- | --- | 
|  `dtc_guide`  | Diagnostic Trouble Code guides: symptom, likely causes, repair procedure, severity rating. Used by Fleet Driver and Technician personas. | 
|  `tsb_recall`  | Technical Service Bulletins and NHTSA recall notices. Used by Service Advisor and Technician. | 
|  `owner_manual`  | Owner manual excerpts relevant to maintenance and warning lights. Used by Vehicle Owner and Consumer personas. | 
|  `service_policy`  | Tenant service-level policies, warranty terms, and coverage rules. Used by Service Advisor and Retail Advisor. | 
|  `parts_catalog`  | Parts catalog narratives with OEM part numbers and pricing references. Used by Technician and Retail Advisor for repair-cost estimates. | 
|  `charging_narrative`  | EV charging guidance, range anxiety FAQ, charging-network information. Used by Consumer and Fleet Driver personas for EV-specific queries. | 

AVX invokes Bedrock `Retrieve` cross-account, passing the Knowledge Base ARN and a metadata filter on `source_category`. This narrows retrieval to the subset of the corpus relevant to the current persona and query, reducing both latency and noise in the retrieved chunks. The grounding strategy for choosing between KB Retrieve and Memory LTM is detailed in [Knowledge and Grounding](knowledge-and-grounding.md).