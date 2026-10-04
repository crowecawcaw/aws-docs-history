

# Data products
<a name="data-products"></a>

The Automotive Data Platform is organized as a data mesh: one Amazon DataZone V2 domain carrying 12 projects — 9 core producer projects (one per core data product except `tire_health`), 1 smoke-test consumer project, and 2 domain projects (`dealer_domain`, `parts_domain`). Producers publish their Glue databases as DataZone asset catalog entries; consumers discover, subscribe to, and query products through the DataZone self-service portal or API — governed at every step by AWS Lake Formation tag-based access control.

For the broader data-mesh strategy — including the three-layer automotive data portfolio (operational / analytical / channel), the platform-foundation topology, and the cross-cutting governance layer — see [Automotive Data Mesh](automotive-data-mesh.md).

## Product catalog
<a name="product-catalog"></a>

All 10 data products publish to the same DataZone domain (`adp-{stage}-foundation-domain`). Nine are Iceberg-backed tables stored in the shared S3 lake bucket; one (`vehicle_knowledge_base`) uses direct S3 storage backed by a Bedrock Knowledge Base. Glue databases follow the naming pattern `adp_{stage}_<technical_name>`.


| \# | Domain | Display name | Technical name | Partition | 
| --- | --- | --- | --- | --- | 
| 1 | Automotive | Vehicle Telemetry (Aggregated) |  `vehicle_telemetry_aggregated`  |  `event_date`, bucketed by `vin` (16) | 
| 2 | Automotive | Vehicle Identity Graph |  `vehicle_identity`  |  `model_year`  | 
| 3 | Automotive | Tire Health (Daily Aggregate) |  `tire_health`  |  `event_date`, bucketed by `vin` (16) | 
| 4 | EV Operations | Charging Sessions |  `charging_sessions`  |  `session_date`, bucketed by `vin` (16) | 
| 5 | EV Operations | Energy Usage |  `energy_usage`  |  `usage_date`, bucketed by `vin` (16) | 
| 6 | EV Operations | OTA Campaigns |  `ota_campaigns`  |  `campaign_id` (header) \+ `dispatch_date` (events) | 
| 7 | Customer | Customer 360 |  `customer_360`  |  `snapshot_date`  | 
| 8 | Customer | Customer Interactions |  `customer_interactions`  |  `interaction_date`, bucketed by `customer_id` (16) | 
| 9 | Service | Service Records |  `service_records`  |  `service_month`, bucketed by `vin` (16) | 
| 10 | Knowledge | Vehicle Knowledge Base |  `vehicle_knowledge_base`  | (text artifacts; not Iceberg — direct S3 \+ Bedrock KB) | 

Per-product schemas, sample queries, and lineage notes live under `platform-foundation/source/data-products/<technical_name>/`. Cross-product join examples live under `platform-foundation/source/athena-queries/`.

## Additional catalog domains — dealer and parts
<a name="additional-catalog-domains"></a>

Two additional DataZone projects and Glue databases ship alongside the 10 core products to serve the Dealer Management System (DMS) accelerator. They live in the same `adp-{stage}-foundation-domain` and share the same governance layer as the core products, but they are grouped as separate *catalog domains* because they cover dealer-operations and parts data rather than vehicle-lifecycle data. Both databases are provisioned by dedicated `dealer_domain` and `parts_domain` stacks (see [Platform foundation](platform-foundation.md)). Tables are populated by one-shot Glue/PySpark generators — the stacks emit zero `AWS::Glue::Table` resources.

### Dealer domain (`adp_{stage}_dealer_domain`)
<a name="dealer-domain-adp_stage_dealer_domain"></a>

Five Iceberg tables shaped for franchise-dealer service and sales operations:


| Product | Purpose | 
| --- | --- | 
|  `service_records`  | Service records joining VIN, customer, dealer, and parts, scoped to the dealer domain. Distinct from the core `service_records` product; the two share schema conventions but not row semantics. | 
|  `dealer_performance`  | Dealer performance rollups across KPIs and time windows. | 
|  `certification_scores`  | STAR interface certification scores per dealer × interface. | 
|  `dealer_inventory`  | Dealer vehicle inventory snapshots. | 
|  `deal_pipeline`  | Active deal pipeline with F&I stage tracking. | 

Product-owner metadata is `"DMS accelerator"`. Cross-account Lake Formation grants are provisioned in-IaC by the `governance` stack for the DMS consumer principal.

### Parts domain (`adp_{stage}_parts_domain`)
<a name="parts-domain-adp_stage_parts_domain"></a>

Three Iceberg tables shaped after the Auto Care ACES 5.0 and PIES 8.0 industry standards, populated with synthetic IDs only:


| Product | Standard | Notes | 
| --- | --- | --- | 
|  `parts_catalog`  | PIES 8.0 shape | Primary key `(brand_aaia_id, part_number)`. `brand_aaia_id` is always a synthetic `DMS-BR-*` value — never a real Auto Care Brand Table `BrandAAIAID`, which is licensed. | 
|  `parts_fitment`  | ACES 5.0 shape | Primary key `(part_number, vehicle_config_id, position_id, qualifier_hash)`. `vehicle_config_id` is always a synthetic `DMS-VCFG-*` value — never a real Auto Care VCdb `VehicleID`, which is licensed. | 
|  `parts_interchange`  | — | Primary key `(primary_part_number, replacement_part_number)`. `relationship_type` is one of `supersession`, `oe_cross`, `aftermarket_equivalent`. Kept as a separate product because supersession is 1:N and OE cross-references are bidirectional. | 

All three products carry an `access_channel` dimension with values in `{franchise, independent}` for REPAIR Act forward-readiness; v1 seeds and enables `franchise` only.

**Important**  
Auto Care VCdb, PCdb, Qdb, PAdb, and the Brand Table are subscription-based licensed property. This repository ships ACES/PIES-conformant *schema shape* and message structure only, populated with synthetic `DMS- ` prefixed values. Every synthetic ID lives in a distinct namespace (`DMS-VCFG-`, `DMS-BR- `, `DMS-PT-`, `DMS-QT- `, `DMS-PA-`) so no synthetic value can be mistaken for a licensed one. Enforced at CI time by `platform-foundation/scripts/lint_no_licensed_autocare_ids.py`.

The `parts_catalog` table is the *authoritative* source for parts data. A parallel Bedrock Knowledge Base source category (`source_category: "parts_catalog"`) under the `vehicle_knowledge_base` product is a *derived read surface* regenerated from `parts_catalog` — one markdown document per SKU. The regeneration boundary and the compatibility contract with downstream consumers are documented in `docs/parts-surface-boundary.md`.

## Per-domain summaries
<a name="per-domain-summaries"></a>

### Automotive domain
<a name="automotive-domain"></a>

The Automotive domain contains three products that form the foundation of vehicle-level analytics. `vehicle_telemetry_aggregated` publishes VSS-aligned time-series signals (speed, battery SoC, motor torque, ambient temperature, and more) aggregated at the trip level, partitioned by `event_date` with bucket partitioning on `vin` for efficient per-vehicle queries. `vehicle_identity` is the authoritative vehicle registry — model, trim, powertrain type, battery capacity, manufacture date — partitioned by `model_year`. `tire_health` is a daily aggregate of per-tire conditions (tread depth, pressure, temperature) with supervised labels for maintenance: `needs_replacement` (bool) and `wear_category` (ok/monitor/replace). Joinable to `vehicle_telemetry_aggregated` on `vin`\+`event_date` and to `service_records` on `vin` \+ service type, tire\_health enables predictive tire maintenance and fleet-wide tread wear analytics. Together these three products are the join backbone for every other domain.

### EV Operations domain
<a name="ev-operations-domain"></a>

The EV Operations domain captures the three operational loops unique to electric vehicle fleets. `charging_sessions` records every charge event (session start/end, energy dispensed, peak power, station type, charge limit) with bucket partitioning on `vin` to co-locate all sessions for a vehicle in the same file group. `energy_usage` aggregates daily energy consumption per vehicle, including range estimates, regeneration, and ambient-temperature effects. `ota_campaigns` is a two-table product — a header table of campaign metadata (firmware version, rollout schedule, target population) and an events table of per-VIN dispatch outcomes — enabling operators to track campaign adoption, rollback rates, and post-OTA efficiency drift.

### Customer domain
<a name="customer-domain"></a>

The Customer domain provides two complementary views of the customer relationship. `customer_360` is a daily snapshot of the full customer profile — demographics, preferences, vehicle assignments, lifetime charging spend, and risk tier — partitioned by `snapshot_date` to support point-in-time lookups. `customer_interactions` records every customer-touchpoint event (contact-center call, service booking, app session, live-chat exchange) with bucket partitioning on `customer_id`, enabling conversation-level grounding for Agentic Vehicle Experience (AVX) agents and analytics-level segmentation for BI consumers.

### Service domain
<a name="service-domain"></a>

The Service domain contains `service_records`, which publishes the complete service history for every vehicle: DTC codes, repair lines, parts consumed, dealer identifiers, labor hours, warranty status, and recall completion flags. Partitioned by `service_month`, it enables time-windowed analysis of fleet-wide service trends, dealer performance, and parts demand forecasting. `service_records` is the primary grounding source for predictive-maintenance consumers.

### Knowledge domain
<a name="knowledge-domain"></a>

The Knowledge domain contains the single non-Iceberg product: `vehicle_knowledge_base`. This product publishes structured text artifacts (DTC diagnostic guides, Technical Service Bulletins, recall advisories, owner manuals, parts catalog excerpts, service network descriptions, charging narratives, OTA rollout summaries) as document chunks ingested into an Amazon Bedrock Knowledge Base with an S3 Vectors vector index. See [Vehicle Knowledge Base — storage and cost distinction](#vkb-distinctness) for the technical distinction from the Iceberg products.

## Subscription pattern
<a name="subscription-pattern"></a>

Consumers subscribe to ADP data products via the Amazon DataZone V2 self-service portal or the DataZone API. Within the domain, subscriptions are auto-granted — no manual approval step is required. After subscription approval, the consumer project receives Athena-ready credentials scoped by Lake Formation to the subscribed product’s Glue database and tables.

The canonical subscription workflow — including IAM role assumptions, Athena workgroup configuration, per-product sample queries, and cross-product join patterns — is documented in `docs/cvx-integration-contract.md`. That document contains 16 sample SQL blocks, covering per-product queries, cross-product joins (customer × charging × energy, VIN × OTA × energy, customer × service × charging, and a full-VIN-360 join), and the Bedrock KB seeding and lineage-trace patterns. The SQL blocks are not reproduced here; treat `docs/cvx-integration-contract.md` as the authoritative executable reference.

## Data contracts
<a name="data-contracts"></a>

ADP publishes a formal data contract in `docs/data-contracts.md` that covers:
+  **VSS vocabulary** — the 40-signal subset of VSS v6.0 published across `vehicle_telemetry_aggregated` and `energy_usage`, with ADP column names, units, and valid ranges.
+  **Identifier formats and regexes** — canonical format and regex for `vin`, `customer_id`, `dealer_id`, `supplier_id`, `part_number`, and `station_id`.
+  **Partition conventions** — the Iceberg partition expressions (including bucket counts) for all 9 Iceberg products in the core catalog, and the rationale for each partition key.
+  **Time and date conventions** — ISO-8601 timestamps in UTC, `YYYY-MM-DD` date strings, and the `service_month` / `snapshot_date` periodicity conventions.
+  **Explicit non-dependencies** — what CMS and AVX do NOT need to know about ADP internals.

Do not reproduce identifier regex tables or VSS signal tables from `docs/data-contracts.md` in consumer-facing code or documentation — cross-link to the source document so that contract updates propagate to all consumers automatically.

## Vehicle Knowledge Base — storage and cost distinction
<a name="vkb-distinctness"></a>

 `vehicle_knowledge_base` (product \#10 in the core catalog) differs architecturally from the 9 Iceberg products in two important ways.

 **Storage model.** Instead of Iceberg-on-Glue, `vehicle_knowledge_base` uses direct S3 object storage for the raw document chunks, backed by an Amazon Bedrock Knowledge Base with an Amazon S3 Vectors collection as the vector index. Queries are issued via the Bedrock `RetrieveAndGenerate` or `Retrieve` API rather than Athena SQL. There is no Glue database for this product and no DataZone Iceberg asset; the DataZone project for `vehicle_knowledge_base` catalogs the S3 prefix and the Bedrock KB ARN.

 **Cost advantage.** Amazon S3 Vectors is usage-priced, eliminating the per-stage hourly commitment that was required with OpenSearch Serverless (AOSS). The S3 Vectors collection backing `vehicle_knowledge_base` now costs single-digit dollars per month per stage (reduced from \~$200–400/month AOSS minimum). See `docs/DEPLOYMENT.md` § "Vehicle Knowledge Base (Bedrock KB \+ S3 Vectors) deploy" and the cost table in `docs/DEPLOYMENT.md` § "Cost estimates" for current per-stage estimates.

For AVX agents consuming `vehicle_knowledge_base`, the subscription pattern uses the Bedrock KB `Retrieve` API directly rather than Athena; the call pattern and KB ARN resolution are documented in `docs/cvx-integration-contract.md`.