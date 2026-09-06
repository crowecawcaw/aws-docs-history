

# Analytical data platform for automotive OEMs on AWS
<a name="guidance-overview"></a>

Publication date: *January 2026 ([last update](revisions.md): July 2026)* 

Automotive organizations — from EV startups to established OEMs — build connected-vehicle data platforms on AWS. They need a data foundation that matches how they actually operate: vehicle telemetry, charging behavior, OTA campaigns, customer interactions, and service records—all governed and joinable for analytics, ML, and agent grounding.

The Guidance for an Automotive Data Platform on AWS (ADP) is that foundation. ADP is the analytical layer in a three-layer automotive data platform. It deploys as **one foundation deploy publishing 9 governed data products (a dataset with an owner, an access policy, and a documented schema, published so other teams can discover and subscribe to it)** through an Amazon DataZone V2 domain.

## The Three-Layer Automotive Data Portfolio
<a name="the-three-layer-automotive-data-portfolio"></a>

ADP is the analytical layer in a three-layer reference portfolio for automotive organizations on AWS:


| Layer | Repo | What it does | 
| --- | --- | --- | 
| Operational |  [CMS (Connected Mobility on AWS)](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws)  | How the automotive organization runs the vehicle — real-time ingest, fleet operations UI, FleetWise telemetry, DynamoDB, MSK, Apache Flink | 
|  **Analytical**  |  **ADP (this guidance)**  |  **How the automotive organization analyzes its data — governed lake, 9 data products, DataZone catalog, agent grounding**  | 
| Channel | CVX (Connected Vehicle Experience on AWS) | How the automotive organization talks to customers — voice, agentic, multi-channel | 

Each layer is independently deployable. Each delivers full value alone. Together is additive. Neither CMS nor CVX takes a code or runtime dependency on ADP.

## Why ADP
<a name="why-adp"></a>

Automotive organizations face a familiar data-fragmentation challenge: vehicle telemetry, charging behavior, OTA campaign history, customer interactions, and service records live in disconnected systems — owned by different teams, stored in different databases, governed by different policies, with no shared key that lets you join them.

**Important**  
 **The core enabling thesis**: Governed cross-silo data is what makes every downstream consumption pattern possible. Agents need context that spans vehicle state, customer history, and service records in a single grounded answer. ML models need clean, joined training datasets that no single system owns alone. Business queries need a coherent picture that lives across operational silos. ADP’s governed data-product model is the enabling layer beneath all of these — rather than each team solving data access independently, every consumption pattern (agents, ML, BI, executive natural-language query) draws from the same 9 governed data products, with consistent identifiers, documented schemas, and access control that IT actually enforces.

ADP gives any automotive organization the governed lake, synthetic data, and DataZone catalog they need to:
+ Answer operational questions: "Which vehicles have degraded battery SoH after winter?" "Which customers have open service records and unresolved OTA failures?"
+ Train predictive models: the reference Isolation-Forest predictive-maintenance notebook subscribes to four data products via DataZone and joins them in Amazon Athena.
+ Ground agentic workloads: CVX agents subscribe to ADP data products via DataZone to deliver multi-channel customer conversations backed by a single coherent view of the vehicle, the customer, and the service history.

## What You Get
<a name="what-you-get"></a>

A single deploy under `platform-foundation/` provisions:
+  **Amazon DataZone V2 domain** (`adp-{stage}-foundation-domain`) with 9 producer projects \+ 1 smoke-test consumer project, all auto-grant within the domain.
+  **S3 \+ Glue \+ Iceberg lake** with one Glue database per data product (`adp_{stage}_<product>`) and a shared `adp_{stage}_dimensions` database.
+  **Realistic synthetic data** with referential integrity preserved by construction across products, intentional 1–3% edge-case injection per the six-code taxonomy, VSS-aligned vehicle signals, and automotive-fleet-shaped distributions (battery age × SoH correlation, winter range loss, post-OTA efficiency drift, \~70/25/5 charging mix).
+  **Cross-cutting governance layer**: Lake Formation tag-based access control, AWS Macie classification on PII-bearing prefixes, CloudTrail data-event logging on the lake bucket, IAM Identity Center groups (`adp-{stage}-data-owners`, `-data-consumers`, `-platform-admins`).
+  **Bedrock Knowledge Base seeding** for the `vehicle_knowledge_base` product (DTCs, TSBs, recalls, owner manuals, parts catalog, service network, charging narratives, OTA rollout summaries).
+  **Predictive-maintenance reference-consumer notebook**: a SageMaker Studio notebook that subscribes to four products via DataZone, joins them in Athena, and trains an Isolation-Forest at-risk-VIN model.
+  **End-to-end verification**: `scripts/smoke-test-subscription.sh`, `scripts/verify-standalone.sh`, `scripts/verify-contract-queries.sh`, `scripts/profile-data.py`, and a CloudWatch data-quality dashboard.

The foundation deploys to a single AWS account in `us-east-1`. Two stages are supported: `staging` and `prod`.

## The 9 Governed Data Products
<a name="the-9-governed-data-products"></a>

All 9 products publish to the same DataZone V2 domain. Eight are Iceberg-backed; one (`vehicle_knowledge_base`) is a Bedrock Knowledge Base built from text artifacts on S3.


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

Per-product schemas, sample queries, and lineage live under `platform-foundation/source/data-products/<product>/`. Cross-product join examples live under `platform-foundation/source/athena-queries/`.

## Relationship to CMS and CVX
<a name="relationship-to-cms-and-cvx"></a>

ADP, CMS, and CVX are independent accelerators that converge on shared schema conventions. There is no code or runtime dependency between them in either direction, with one explicitly opt-in exception (CMS → ADP ingest, off by default).

### CMS: The Operational Layer
<a name="cms-the-operational-layer"></a>

 [CMS (Connected Mobility on AWS)](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws) owns the operational layer—DynamoDB, Redis, MSK, Flink, fleet UI, FleetWise telemetry. CMS continues to deploy standalone to a clean account with zero ADP references.

The convergence is **schema-only**: ADP publishes `docs/data-contracts.md` declaring the VSS signal subset, identifier formats (VIN, `customer_id`, `dealer_id`, `supplier_id`, `part_number`, `station_id`), time/date conventions, and Iceberg partition conventions. CMS optionally references this document from its own `docs/`.

When CMS and ADP are deployed in the same account, an opt-in CDK context flag enables a DynamoDB Streams → Kinesis Firehose → S3 raw → Glue Iceberg MERGE pipeline that lands CMS DynamoDB updates in an `adp_{stage}_cms_ingest` Glue database. Off by default. See `docs/cms-ingest-optional-module.md` for the rationale, prereqs, enable command, cost estimate, and disable command.

### CVX: The Channel Layer
<a name="cvx-the-channel-layer"></a>

CVX is the channel layer (voice, agentic, multi-channel customer conversations). CVX agents subscribe to ADP data products via DataZone to ground multi-channel conversations on a single coherent customer view. The contract is documented in `docs/cvx-integration-contract.md`: 17 sample SQL blocks across 9 per-product queries plus 4 cross-product joins (customer × charging × energy, VIN × OTA × energy, customer × service × charging, full-VIN-360), plus the Bedrock KB seeding and lineage-trace patterns. CVX takes no code or runtime dependency on ADP—only a documented subscription flow.

## Foundation Deploy Architecture
<a name="foundation-deploy-architecture"></a>

The `platform-foundation/` CDK app deploys five per-stage stacks plus one account-singular bootstrap stack:


| Deploy order | Stack logical name | Purpose | 
| --- | --- | --- | 
| Bootstrap (once) |  `adp-shared-bootstrap`  | Account-level Macie session; deploy once per account | 
| 1 |  `adp-{stage}-foundation-network`  | VPC \+ VPC endpoints | 
| 2 |  `adp-{stage}-foundation-lake`  | S3 lake bucket \+ KMS \+ 10 Glue databases | 
| 3 |  `adp-{stage}-foundation-datazone`  | DataZone V2 domain \+ roles | 
| 4 |  `adp-{stage}-foundation-datazone-projects`  | 10 projects (9 product \+ 1 smoke-test consumer) | 
| 5 |  `adp-{stage}-foundation-governance`  | Lake Formation tags \+ CloudTrail trail \+ 3 IAM Identity Center groups | 
| Optional |  `adp-{stage}-foundation-cms-ingest`  | DynamoDB Streams → Firehose → Iceberg; off by default | 

The 9 data products are populated by independent generators that consume a shared dimension catalog (5M VINs, 5M customers, 200 dealers, 500 suppliers, 50K parts, 50K charging stations, 10 years of calendar). Generators are deterministic under a fixed seed — re-runs produce byte-identical parquet.

## What ADP Does Not Include (v0.2)
<a name="what-adp-does-not-include-v0-2"></a>

ADP v0.2 is a focused analytical foundation. Compared to v0.1.0, the following have been removed or moved:
+  **Pre-built BI dashboards** — v0.2 ships zero pre-built visual-analytics dashboard assets. Analytics visualization is a consumer responsibility.
+  **Aurora pgvector** — replaced by Bedrock Knowledge Base \+ OpenSearch Serverless on the `vehicle_knowledge_base` product.
+  **Custom Bedrock-Agent CDK** — agents live in CVX, not ADP.
+  **Tire-anomaly Random Cut Forest API** — replaced by the SageMaker Studio Isolation-Forest reference-consumer notebook.
+  **Multi-region EU Data Act / GDPR cross-region split** — ADP v0.2 is single-region (`us-east-1`). EU Data Act cross-region architecture is out of foundation v1 scope.
+  **Manufacturing data products** (`production_quality`, `supplier_traceability`) — deferred to a possible v2.

See `docs/MIGRATION-FROM-V0.1.0.md` for the full per-subdir disposition table.

## Cost Estimates
<a name="cost-estimates"></a>

The following table provides estimated monthly costs for deploying the foundation layer. Costs are based on `us-east-1` region pricing and assume a development/staging workload. Production workloads with higher data volumes and query rates will scale accordingly.


| Component | Approx monthly cost (us-east-1) | 
| --- | --- | 
| S3 lake bucket (synthetic data, \~2–3 TiB at full Spark scale) | $50–80 | 
| Glue catalog (10 databases) | <$5 | 
| Athena queries (development workload) | $5–25 | 
| DataZone V2 domain | $0 (consumption-based; minimal at v1) | 
| Macie classification | $30–80 (PII-bearing prefixes only) | 
| CloudTrail data events | $5–15 | 
| Bedrock Knowledge Base \+ OpenSearch Serverless | $200–400 | 
| CloudWatch quality dashboard | $3 | 
| Optional CMS-ingest module (one CMS table) | \+$256 (Firehose \+ Glue MERGE) | 
|  **Foundation only**  |  **\~$300–600**  | 
|  **\+ Optional CMS-ingest**  |  **\~$550–860**  | 

**Note**  
These estimates are approximate and based on publicly available AWS pricing as of January 2026. Actual costs depend on usage patterns, data volumes, query frequency, and region. Use the [AWS Pricing Calculator](https://calculator.aws/) for detailed estimates tailored to your workload.

## Target Audience
<a name="target-audience"></a>

This guidance is designed for:
+  **Automotive engineering teams** building the analytical layer for a modern connected-vehicle platform on AWS — whether at an EV startup, an established OEM, or a Tier-1 supplier
+  **Data engineers** implementing governed data mesh patterns with domain-oriented ownership and DataZone V2
+  **ML engineers** building predictive maintenance and customer analytics models that consume ADP data products
+  **Solutions architects** designing the analytical tier of a three-layer automotive data portfolio (operational CMS \+ analytical ADP \+ channel CVX)
+  **Data and analytics teams** in automotive organizations building a governed lake on Iceberg with Lake Formation \+ IAM Identity Center access control
+  **Business and executive stakeholders** in automotive organizations exploring natural-language querying and AI-assisted reporting over governed vehicle and customer data — the Agentic Enterprise chapter addresses this audience directly

## About This Guide
<a name="about-this-guide"></a>

This guide documents architectural use cases and design patterns for building on the Automotive Data Platform — the kinds of recurring customer questions AWS’s automotive solutions team answers repeatedly, generalized into reusable guidance. The `platform-foundation/` codebase demonstrates a foundational subset of these patterns directly (see [Platform foundation](platform-foundation.md) and [Data products](data-products.md)); other chapters describe patterns you can build on top of that foundation, informed by real implementations where one exists, but not necessarily present in the codebase today. A pattern remaining in this guide does not imply it ships as deployable code in the current release — check [Platform foundation](platform-foundation.md) and [Data products](data-products.md) for what the foundation deploy actually provisions.

## How This Guide Is Organized
<a name="how-this-guide-is-organized"></a>

This implementation guide is organized as follows:
+  **Guidance Overview** (this chapter) — Why ADP, the three-layer automotive data portfolio, the 9 governed data products, relationship to CMS and CVX, cost estimates
+  **Architecture Overview** — High-level architecture diagrams and the 5-stack-per-stage \+ bootstrap topology
+  **Platform Foundation** — Single-foundation-deploy chapter: `make deploy` flow, staging/prod stages, cross-cutting governance (Lake Formation, Macie, CloudTrail, IAM Identity Center), KB deploy, teardown
+  **Data Products** — The 9-product catalog chapter (Automotive \+ EV Operations \+ Customer \+ Service \+ Knowledge domains) with per-product technical name, partition, publisher project, and subscription pattern
+  **Agentic Enterprise** — Living pattern catalog for building agentic and AI-assisted workloads on top of ADP’s governed data products, including a customer-facing agent grounding example and a natural-language business-query example.
+  **Automotive Data Mesh** — DataZone V2 domain strategy, data-as-a-product principles, federated governance, and cross-domain analytics patterns for automotive organizations
+  **Customer 360** — Architecture pattern for unified customer analytics combining [Amazon Quick Suite](https://docs.aws.amazon.com/quicksuite/latest/userguide/) dashboards, Bedrock AI agents, and Aurora pgvector knowledge base — grounded in the `customer_360`, `customer_interactions`, and `service_records` data products.
+  **Predictive Maintenance** — Reference architecture for predicting physical-asset failures from time-series sensor telemetry, demonstrated here with a tire predictive-maintenance implementation (dual ML/SageMaker Random Cut Forest and filter-based pipelines predicting failures 7–14 days in advance); the same architecture generalizes to other asset classes. Includes real implementation code in `guidance-for-predictive-maintenance/`.
+  **Telemetry Normalization** — Living pattern catalog for multi-source telemetry normalization architecture: ingestion, windowing, stateful processing, pattern/anomaly detection, and Redis baseline store — with CMS cited as one reference implementation.
+  **Automotive Data Governance** — Architecture pattern for multi-region EU Data Act and GDPR compliance, separating PII in EU producer regions from anonymized data accessible to global R&D teams via Lake Formation resource links.
+  **Update the Guidance** — v0.1.0 → v0.2 migration steps; foundation update flow
+  **Troubleshooting** — Common issues and debugging techniques for the foundation deploy, DataZone subscriptions, Glue, Athena, and Bedrock KB
+  **Uninstall the Guidance** — Six-step teardown procedure per `docs/DEPLOYMENT.md` 
+  **Developer Guide** — `platform-foundation/` layout, `make venv` / `make install` / `make bootstrap` / `make deploy` / `make seed` / `make smoke-test` flow, customization patterns
+  **Reference** — GitHub repository tree, AWS service documentation links, related solutions
+  **Revisions** — Changelog of implementation guide updates
+  **Notices** — Legal notices and trademarks