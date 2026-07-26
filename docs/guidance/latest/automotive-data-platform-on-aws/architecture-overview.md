# Architecture overview

This chapter provides a high-level overview of the Automotive Data Platform v0.2
architecture — its foundation topology, data product catalog, governance layer, and
two-stage rollout model. For deploy topology detail, see [Platform foundation](platform-foundation.md "platform-foundation.md"). For the
full data product catalog, see [Data products](data-products.md "data-products.md").

![Automotive Data Platform Architecture Overview](/images/guidance/latest/automotive-data-platform-on-aws/images/mesh.png)

###### Note

The architecture diagram in this section is being updated to reflect the platform-foundation (v0.2) model. The narrative text describes the current deployed architecture; the diagram may still show the earlier five-guidance structure.

## Foundation topology

The `platform-foundation/` CDK app is the single entry point for all ADP infrastructure.
It provisions five per-stage stacks plus one account-singular bootstrap stack. Stack names
follow the `adp-{stage}-foundation-` prefix pattern; resources within each stack follow
`adp_{stage}_` naming for Glue databases and `adp-{stage}-*` for IAM Identity Center
groups.

### Per-stage stacks

The five per-stage stacks deploy in dependency order (1–5) and are gated behind a
`STAGE`-required Makefile entry point. Both `staging` and `prod` stages are supported;
`staging` and `prod` deploy independently into the same AWS account in `us-east-1`.

| Deploy order     | Stack logical name                         | Purpose                                                                                                                                                                                                                              |
| ---------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Bootstrap (once) | `adp-shared-bootstrap`                     | Enables the Amazon Macie session at account level. Deployed once per account via<br>`make bootstrap`; not part of per-stage teardown.                                                                                                |
| 1                | `adp-{stage}-foundation-network`           | VPC and VPC endpoints.                                                                                                                                                                                                               |
| 2                | `adp-{stage}-foundation-lake`              | Amazon S3 lake bucket (Iceberg, KMS-encrypted, versioned), plus 10 AWS Glue<br>databases — 9 per-product (`adp_{stage}_<product>`) and 1 shared dimensions<br>database (`adp_{stage}_dimensions`).                                   |
| 3                | `adp-{stage}-foundation-datazone`          | Amazon DataZone V2 domain and associated IAM roles.                                                                                                                                                                                  |
| 4                | `adp-{stage}-foundation-datazone-projects` | 10 DataZone projects: 9 producer projects (one per data product) and 1 smoke-test<br>consumer project with auto-grant subscriptions.                                                                                                 |
| 5                | `adp-{stage}-foundation-governance`        | AWS Lake Formation tag-based access control, AWS CloudTrail data-event trail on the<br>lake bucket, and 3 IAM Identity Center groups<br>(`adp-{stage}-data-owners`, `adp-{stage}-data-consumers`,<br>`adp-{stage}-platform-admins`). |

Stage names and stack-name prefixes are strictly controlled. The Makefile fails closed
if `STAGE` is omitted. Resource naming is a deterministic function of `{stage}` — no
timestamps, no random suffixes — to support idempotent re-deploys and cross-stage
comparison.

### Two-stage rollout

ADP supports two stages: `staging` and `prod`. Each stage is a fully independent deploy
with its own S3 lake bucket, DataZone domain, Glue databases, and governance stack. The
staging stack names follow `adp-staging-foundation-`; production follows
`adp-prod-foundation-`. Resources are isolated by name prefix and by Lake Formation
permission scope — no cross-stage data access.

This prefix-based isolation means that `make deploy STAGE=staging` and
`make deploy STAGE=prod` can safely co-exist in the same AWS account.

## DataZone V2 domain and projects

The `adp-{stage}-foundation-datazone-projects` stack creates one Amazon DataZone V2
domain with 10 projects:

- **9 producer projects** — one per data product, each publishing its Glue
  database as a DataZone asset catalog entry with auto-granted access within the domain.
- **1 smoke-test consumer project** — subscribes to one or more products end-to-end;
  validates the DataZone subscription flow as part of `make smoke-test STAGE=`.

The DataZone domain name follows `adp-{stage}-foundation-domain`. All 9 data products are
governed within this domain; consumers (CVX agents, SageMaker Studio notebooks, BI tools)
subscribe via DataZone to access product assets under Lake Formation-enforced permissions.

For the complete data product catalog — technical names, domains, partitions, and
per-product subscription patterns — see [Data products](data-products.md "data-products.md").

## Cross-cutting governance layer

ADP’s governance layer is deployed as part of the `governance` stack rather than as an
independent guidance. It covers four dimensions:

### Lake Formation tag-based access control

The `governance` stack registers the S3 lake bucket with AWS Lake Formation and applies
tag-based access control (LF-TBAC) across all 10 Glue databases. Data owners are granted
access via the `adp-{stage}-data-owners` IAM Identity Center group; consumers via
`adp-{stage}-data-consumers`; platform administrators via `adp-{stage}-platform-admins`.
Fine-grained column-level permissions are applied on PII-bearing tables.

### Amazon Macie classification

The `adp-shared-bootstrap` stack enables an Amazon Macie session at account level (once
per account, not per stage). Macie automated discovery jobs classify PII-bearing prefixes
on the lake S3 bucket. Macie findings surface in Amazon Security Hub.

Note: Macie has a 30-day cool-down period after disabling. If you see "Macie is already
enabled" during bootstrap, the session is already active — no action required. See the
deployment runbook at `docs/DEPLOYMENT.md` for details.

### CloudTrail data events

The `governance` stack creates an AWS CloudTrail trail configured for data-event logging
on the lake S3 bucket. Every `GetObject`, `PutObject`, and `DeleteObject` API call is
recorded, providing an immutable audit log of all data access within the lake.

### IAM Identity Center groups

The `governance` stack provisions three IAM Identity Center (IDC) groups per stage:

- `adp-{stage}-data-owners` — Lake Formation data-owner permissions; intended for data
  product producers.
- `adp-{stage}-data-consumers` — Lake Formation consumer permissions; intended for
  analysts, notebook users, and application consumers.
- `adp-{stage}-platform-admins` — Administrative permissions for platform operations.

IDC groups are regional and live in `us-east-1`. This is the primary reason ADP is
single-region (`us-east-1`) in v0.2 — the IDC instance cannot be split across regions.
EU Data Act / GDPR cross-region split is out of scope for foundation v1.

## Platform layers

The platform-foundation model organizes the data platform into four integrated layers:

### DataZone catalog layer

Amazon DataZone V2 provides the data catalog, lineage tracking, and self-service
subscription surface. Producers publish data products to the domain; consumers discover,
subscribe, and access products via DataZone’s UI or API. The subscription model is
auto-granted within the domain — no manual approval step is required for intra-domain
subscriptions during smoke-test validation.

See [Data products](data-products.md "data-products.md") for the full catalog of 9 published data products.

### Lake layer

Amazon S3 provides the storage substrate for all data products. Eight of the 9 products
are stored as Apache Iceberg tables (ACID transactions, schema evolution, time-travel
queries). One product (`vehicle_knowledge_base`) uses direct S3 storage backed by a
Bedrock Knowledge Base with an Amazon OpenSearch Serverless index.

AWS Glue provides the catalog metadata layer (10 databases, one per product plus one
shared dimensions database) and the compute layer (Glue 5.1 Spark jobs for data
generation and transformation). Amazon Athena Engine V3 provides the serverless SQL
query layer for analyst and notebook consumers.

### Governance layer

The cross-cutting governance layer (Lake Formation, Macie, CloudTrail, IDC groups) is
described in the previous section. This layer ensures that every data access event is
logged, PII is classified, and fine-grained permissions are enforced at Glue
database / table / column level.

### Consumers layer

Consumers access data products via Amazon DataZone subscriptions. The primary consumer
patterns documented in this release are:

- **CVX agents** — subscribe to ADP products via DataZone to ground multi-channel
  customer conversations; see `docs/cvx-integration-contract.md` for the canonical
  Athena query patterns and cross-product join examples.
- **SageMaker Studio notebooks** — the reference predictive-maintenance notebook
  subscribes to four products, joins them in Athena, and trains an Isolation-Forest
  model. See `platform-foundation/source/reference-consumers/predictive-maintenance/`.
- **BI and analytics tools** — subscribe via DataZone; query via Athena; no direct
  S3 access required.

## AWS services used

This section lists the primary AWS services deployed by the foundation. For the complete
service footprint, see the stack definitions under `platform-foundation/stacks/`.

### Data lake and storage

- [**Amazon S3**](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") — lake bucket (Iceberg, KMS-encrypted, versioned, server-side access logging)
- [**AWS Glue Data Catalog**](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/") — 10 databases (9 products + 1 dimensions)
- [**AWS Lake Formation**](https://aws.amazon.com/lake-formation/ "https://aws.amazon.com/lake-formation/") — tag-based access control, fine-grained permissions
- [**Amazon Athena**](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/") — serverless SQL queries (Engine V3) with Lake Formation inheritance
- [**AWS Glue ETL**](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/") (Glue 5.1) — Spark-based data generation and transformation

### Catalog and governance

- [**Amazon DataZone**](https://aws.amazon.com/datazone/ "https://aws.amazon.com/datazone/") — V2 domain, 10 projects, auto-grant subscriptions, lineage
- [**AWS CloudTrail**](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") — data-event logging on lake bucket
- [**Amazon Macie**](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/") — automated PII classification on lake prefixes
- [**AWS IAM Identity Center**](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/") — 3 groups per stage (`data-owners`, `data-consumers`, `platform-admins`)
- [**AWS KMS**](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") — encryption key management for lake bucket and Glue catalog

### Knowledge and AI

- [**Amazon Bedrock Knowledge Bases**](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/") — `vehicle_knowledge_base` product (DTCs, TSBs, recalls, owner manuals)
- [**Amazon OpenSearch Serverless**](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/") — vector index backing the Bedrock Knowledge Base (~$345/mo AOSS commitment per stage)

### Analytics and machine learning

- [**Amazon SageMaker Studio**](https://aws.amazon.com/sagemaker/studio/ "https://aws.amazon.com/sagemaker/studio/") — reference-consumer predictive-maintenance notebook (Isolation-Forest)
- [**Amazon CloudWatch**](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") — data-quality dashboard

### Networking

- [**Amazon VPC**](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/") — `network` stack; VPC endpoints for S3, Glue, Athena

## Well-Architected Framework alignment

### Operational excellence

- CDK infrastructure-as-code with deterministic naming (no timestamps, idempotent re-deploys)
- Makefile entry point with fail-closed `STAGE` gate
- CloudTrail data-event logging for lake access audit
- CloudWatch data-quality dashboard

### Security

- Lake Formation fine-grained access control at database / table / column level
- Amazon Macie PII classification with Security Hub integration
- KMS encryption for data at rest
- VPC isolation via `network` stack with VPC endpoints
- IAM Identity Center group-based access (no user-level IAM policies)
- CloudTrail immutable audit trail

### Reliability

- S3 with 99.999999999% durability
- Apache Iceberg ACID transactions (schema evolution, time-travel)
- Smoke-test suite (`make smoke-test STAGE=`) validates end-to-end DataZone subscription flow

### Performance efficiency

- Athena partition pruning (per-product partition schemes; see [Data products](data-products.md "data-products.md") for partition columns)
- Glue Spark for distributed data generation at scale
- OpenSearch Serverless (AOSS) auto-scales for Knowledge Base queries

### Cost optimization

- Serverless architecture (Athena, Glue, Lambda) — pay-per-use
- S3 Intelligent-Tiering eligible for infrequently-accessed synthetic data
- Foundation-only cost estimate: ~$300–600/month; with optional CMS-ingest: ~$550–860/month
- Vehicle Knowledge Base (AOSS): ~$345/month per stage — largest single component
- No QuickSight, no Aurora, no Step Functions pipelines — v0.2 removes all v0.1 per-guidance overhead

### Sustainability

- Serverless architecture minimizes idle resources
- Single-region deployment (`us-east-1`) consolidates compute footprint
- Glue Graviton workers for improved energy efficiency

## Next steps

For detailed deployment procedures — including `make bootstrap`, `make deploy STAGE=`,
`make seed STAGE=`, and `make smoke-test STAGE=` — see [Platform foundation](platform-foundation.md "platform-foundation.md").

For the full data product catalog including technical names, partition schemes, and
DataZone subscription patterns, see [Data products](data-products.md "data-products.md").

For cross-product Athena query patterns and CVX agent integration, see
`docs/cvx-integration-contract.md`.
