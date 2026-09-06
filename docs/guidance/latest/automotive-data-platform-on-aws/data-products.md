

# Data products
<a name="data-products"></a>

The Automotive Data Platform is organized as a data mesh: one Amazon DataZone V2 domain with 9 producer projects (one per data product) and 1 smoke-test consumer project. Producers publish their Glue databases as DataZone asset catalog entries; consumers discover, subscribe to, and query products through the DataZone self-service portal or API — governed at every step by AWS Lake Formation tag-based access control.

For the broader data-mesh strategy — including the three-layer automotive data portfolio (operational / analytical / channel), the platform-foundation topology, and the cross-cutting governance layer — see [Automotive Data Mesh](automotive-data-mesh.md).

## Product catalog
<a name="product-catalog"></a>

All 9 data products publish to the same DataZone domain (`adp-{stage}-foundation-domain`). Eight are Iceberg-backed tables stored in the shared S3 lake bucket; one (`vehicle_knowledge_base`) uses direct S3 storage backed by a Bedrock Knowledge Base. Glue databases follow the naming pattern `adp_{stage}_<technical_name>`.


| \# | Domain | Display name | Technical name | Partition | 
| --- | --- | --- | --- | --- | 
| 1 | Automotive | Vehicle Telemetry (Aggregated) |  `vehicle_telemetry_aggregated`  |  `event_date`, bucketed by `vin` (16) | 
| 2 | Automotive | Vehicle Identity Graph |  `vehicle_identity`  |  `model_year`  | 
| 3 | EV Operations | Charging Sessions |  `charging_sessions`  |  `session_date`, bucketed by `vin` (16) | 
| 4 | EV Operations | Energy Usage |  `energy_usage`  |  `usage_date`  | 
| 5 | EV Operations | OTA Campaigns |  `ota_campaigns`  |  `campaign_id` (header) \+ `dispatch_date` (events) | 
| 6 | Customer | Customer 360 |  `customer_360`  |  `snapshot_date`  | 
| 7 | Customer | Customer Interactions |  `customer_interactions`  |  `interaction_date`, bucketed by `customer_id` (16) | 
| 8 | Service | Service Records |  `service_records`  |  `service_month`  | 
| 9 | Knowledge | Vehicle Knowledge Base |  `vehicle_knowledge_base`  | (text artifacts; not Iceberg — direct S3 \+ Bedrock KB) | 

Per-product schemas, sample queries, and lineage notes live under `platform-foundation/source/data-products/<technical_name>/`. Cross-product join examples live under `platform-foundation/source/athena-queries/`.

## Per-domain summaries
<a name="per-domain-summaries"></a>

### Automotive domain
<a name="automotive-domain"></a>

The Automotive domain contains two products that form the foundation of vehicle-level analytics. `vehicle_telemetry_aggregated` publishes VSS-aligned time-series signals (speed, battery SoC, motor torque, ambient temperature, and more) aggregated at the trip level, partitioned by `event_date` with bucket partitioning on `vin` for efficient per-vehicle queries. `vehicle_identity` is the authoritative vehicle registry — model, trim, powertrain type, battery capacity, manufacture date — partitioned by `model_year`. Together these two products are the join backbone for every other domain.

### EV Operations domain
<a name="ev-operations-domain"></a>

The EV Operations domain captures the three operational loops unique to electric vehicle fleets. `charging_sessions` records every charge event (session start/end, energy dispensed, peak power, station type, charge limit) with bucket partitioning on `vin` to co-locate all sessions for a vehicle in the same file group. `energy_usage` aggregates daily energy consumption per vehicle, including range estimates, regeneration, and ambient-temperature effects. `ota_campaigns` is a two-table product — a header table of campaign metadata (firmware version, rollout schedule, target population) and an events table of per-VIN dispatch outcomes — enabling operators to track campaign adoption, rollback rates, and post-OTA efficiency drift.

### Customer domain
<a name="customer-domain"></a>

The Customer domain provides two complementary views of the customer relationship. `customer_360` is a daily snapshot of the full customer profile — demographics, preferences, vehicle assignments, lifetime charging spend, and risk tier — partitioned by `snapshot_date` to support point-in-time lookups. `customer_interactions` records every customer-touchpoint event (contact-center call, service booking, app session, live-chat exchange) with bucket partitioning on `customer_id`, enabling conversation-level grounding for CVX agents and analytics-level segmentation for BI consumers.

### Service domain
<a name="service-domain"></a>

The Service domain contains `service_records`, which publishes the complete service history for every vehicle: DTC codes, repair lines, parts consumed, dealer identifiers, labor hours, warranty status, and recall completion flags. Partitioned by `service_month`, it enables time-windowed analysis of fleet-wide service trends, dealer performance, and parts demand forecasting. `service_records` is the primary grounding source for predictive-maintenance consumers.

### Knowledge domain
<a name="knowledge-domain"></a>

The Knowledge domain contains the single non-Iceberg product: `vehicle_knowledge_base`. This product publishes structured text artifacts (DTC diagnostic guides, Technical Service Bulletins, recall advisories, owner manuals, parts catalog excerpts, service network descriptions, charging narratives, OTA rollout summaries) as document chunks ingested into an Amazon Bedrock Knowledge Base with an OpenSearch Serverless vector index. See [Vehicle Knowledge Base — storage and cost distinction](#vkb-distinctness) for the technical distinction from the Iceberg products.

## Subscription pattern
<a name="subscription-pattern"></a>

Consumers subscribe to ADP data products via the Amazon DataZone V2 self-service portal or the DataZone API. Within the domain, subscriptions are auto-granted — no manual approval step is required. After subscription approval, the consumer project receives Athena-ready credentials scoped by Lake Formation to the subscribed product’s Glue database and tables.

The canonical subscription workflow — including IAM role assumptions, Athena workgroup configuration, per-product sample queries, and cross-product join patterns — is documented in `docs/cvx-integration-contract.md`. That document contains 17 sample SQL blocks: one per product (9) plus 4 cross-product joins (customer × charging × energy, VIN × OTA × energy, customer × service × charging, and a full-VIN-360 join), plus the Bedrock KB seeding and lineage-trace patterns. The SQL blocks are not reproduced here; treat `docs/cvx-integration-contract.md` as the authoritative executable reference.

## Data contracts
<a name="data-contracts"></a>

ADP publishes a formal data contract in `docs/data-contracts.md` that covers:
+  **VSS vocabulary** — the 40-signal subset of VSS v6.0 published across `vehicle_telemetry_aggregated` and `energy_usage`, with ADP column names, units, and valid ranges.
+  **Identifier formats and regexes** — canonical format and regex for `vin`, `customer_id`, `dealer_id`, `supplier_id`, `part_number`, and `station_id`.
+  **Partition conventions** — the Iceberg partition expressions (including bucket counts) for all 8 Iceberg products, and the rationale for each partition key.
+  **Time and date conventions** — ISO-8601 timestamps in UTC, `YYYY-MM-DD` date strings, and the `service_month` / `snapshot_date` periodicity conventions.
+  **Explicit non-dependencies** — what CMS and CVX do NOT need to know about ADP internals.

Do not reproduce identifier regex tables or VSS signal tables from `docs/data-contracts.md` in consumer-facing code or documentation — cross-link to the source document so that contract updates propagate to all consumers automatically.

## Vehicle Knowledge Base — storage and cost distinction
<a name="vkb-distinctness"></a>

 `vehicle_knowledge_base` (product \#9) differs architecturally from the 8 Iceberg products in two important ways.

 **Storage model.** Instead of Iceberg-on-Glue, `vehicle_knowledge_base` uses direct S3 object storage for the raw document chunks, backed by an Amazon Bedrock Knowledge Base with an Amazon OpenSearch Serverless (AOSS) collection as the vector index. Queries are issued via the Bedrock `RetrieveAndGenerate` or `Retrieve` API rather than Athena SQL. There is no Glue database for this product and no DataZone Iceberg asset; the DataZone project for `vehicle_knowledge_base` catalogs the S3 prefix and the Bedrock KB ARN.

 **Cost caveat.** OpenSearch Serverless incurs a minimum hourly commitment regardless of query volume. At current rates, the AOSS collection backing `vehicle_knowledge_base` costs approximately $200–400/month per stage (the single largest cost component of the foundation). Operators who do not require knowledge-base-grounded queries (DTC guides, recall lookups, owner-manual search) may defer this product and skip the KB-seeding step. See `docs/DEPLOYMENT.md` § "Vehicle Knowledge Base" and the cost table in `docs/DEPLOYMENT.md` § "Cost estimates" for current per-stage estimates and an opt-out procedure.

For CVX agents consuming `vehicle_knowledge_base`, the subscription pattern uses the Bedrock KB `Retrieve` API directly rather than Athena; the call pattern and KB ARN resolution are documented in `docs/cvx-integration-contract.md`.