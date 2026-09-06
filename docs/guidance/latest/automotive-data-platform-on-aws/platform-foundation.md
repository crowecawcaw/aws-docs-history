

# Platform foundation
<a name="platform-foundation"></a>

**Note**  
 **Cost estimate**: Foundation-only (staging or prod stage) runs approximately **$300–600/month** in `us-east-1` at development-workload query volumes. The largest single component is the Vehicle Knowledge Base (Amazon OpenSearch Serverless), which commits \~$345/month per stage at the 2-OCU minimum regardless of query volume. Adding the optional CMS→ADP ingest module raises the estimate to \~$550–860/month. See `docs/DEPLOYMENT.md` § *Vehicle Knowledge Base (Bedrock KB \+ AOSS) deploy* for the AOSS cost warning before deploying to a second stage.

## Single-foundation-deploy model
<a name="single-foundation-deploy-model"></a>

ADP v0.2 is one foundation deploy — not five independently-deployable guidances. A single invocation of `make deploy STAGE=staging` (or `STAGE=prod`) deploys all infrastructure required to publish the full set of 9 governed data products. The five per-stage stacks and one account-singular bootstrap stack together constitute the entire platform:


| Deploy order | Stack logical name | Purpose | 
| --- | --- | --- | 
| Bootstrap (once per account) |  `adp-shared-bootstrap`  | Enables the Amazon Macie session at account level. Deployed once via `make bootstrap` before the first stage deploy; not stage-bound and not included in per-stage teardown. Re-running is idempotent (CloudFormation no-op when the stack is already up). | 
| 1 |  `adp-{stage}-foundation-network`  | VPC and VPC endpoints for S3, Glue, and Athena. | 
| 2 |  `adp-{stage}-foundation-lake`  | Amazon S3 lake bucket (Iceberg, KMS-encrypted, versioned), plus 10 AWS Glue databases: 9 per-product databases (`adp_{stage}_<product>`) and 1 shared dimensions database (`adp_{stage}_dimensions`). | 
| 3 |  `adp-{stage}-foundation-datazone`  | Amazon DataZone V2 domain (`adp-{stage}-foundation-domain`) and associated IAM roles. | 
| 4 |  `adp-{stage}-foundation-datazone-projects`  | 10 DataZone projects: 9 producer projects (one per governed data product) plus 1 smoke-test consumer project with auto-grant subscriptions. | 
| 5 |  `adp-{stage}-foundation-governance`  | AWS Lake Formation tag-based access control, AWS CloudTrail data-event trail on the lake bucket, and 3 IAM Identity Center groups per stage. The Macie session lives in `adp-shared-bootstrap`; the per-stage Macie classification job is created post-deploy via `scripts/macie-create-job.sh`. | 

Both `staging` and `prod` stages coexist in the same AWS account in `us-east-1`, isolated by resource-name prefix. The foundation publishes 9 governed data products consumed by the CVX agent platform and SageMaker Studio reference-consumer notebooks. For the complete product catalog, see [Data products](data-products.md).

## Stage gate
<a name="stage-gate"></a>

The Makefile is the only sanctioned entry point. All per-stage targets require `STAGE=staging|prod` (lower-case, case-sensitive). The stage value is propagated as the CDK context flag `-c stage=<stage>`, and `app.py` validates it before any resource synthesis. See `docs/DEPLOYMENT.md` § *Stage gate* for the full gate table.

Key properties of the gate:
+  `make deploy` without `STAGE=` exits 1 with `STAGE is required`.
+  `make deploy STAGE=foo` exits 1 — `foo` is not a sanctioned stage.
+  `make deploy STAGE=Staging` exits 1 — stage values are case-sensitive; only lower-case `staging` and `prod` are accepted.
+  `make bootstrap` does not require `STAGE=` — the bootstrap is account-singular.

**Warning**  
Do NOT run `cdk deploy` directly. The Makefile sets required CDK context flags and environment variables. Direct `cdk deploy` invocations bypass the `STAGE` validation guard and may produce stacks with unprefixed names that collide with existing deploys. See `docs/DEPLOYMENT.md` § *Stage gate* for the full sanctioned commands table.

## Naming convention
<a name="naming-convention"></a>

Resource names follow a deterministic pattern that is a function of stage and AWS account only — no timestamps, no random suffixes — to support idempotent re-deploys and cross-stage comparison.

### Stack and resource naming patterns
<a name="stack-and-resource-naming-patterns"></a>


| Resource class | Naming pattern (staging example) | 
| --- | --- | 
| Bootstrap stack |  `adp-shared-bootstrap` (account-singular — same name regardless of stage) | 
| Per-stage stack names |  `adp-staging-foundation-{network,lake,datazone,datazone-projects,governance}`  | 
| Optional CMS-ingest stack |  `adp-staging-foundation-cms-ingest`  | 
| Lake S3 bucket |  `adp-staging-foundation-lake-<account>-us-east-1`  | 
| KMS key aliases |  `alias/adp-staging-foundation-{lake,trail}`  | 
| DataZone domain |  `adp-staging-foundation-domain`  | 
| Glue databases (10 per stage) |  `adp_staging_<product>` (9 product databases) \+ `adp_staging_dimensions`  | 
| IAM Identity Center groups (3 per stage) |  `adp-staging-{data-owners,data-consumers,platform-admins}`  | 
| CloudTrail trail |  `adp-staging-foundation-lake-trail`  | 
| CloudFormation exports |  `adp-staging-foundation-*`  | 

Substitute `prod` for `staging` in every pattern above for production. DataZone project technical names (e.g., `vehicle_telemetry_aggregated`) remain unprefixed across stages — only the display name gets a `[Staging]` suffix. Production display names carry no suffix (asymmetric by design: prod is the canonical, staging is the variant).

### Why single-region us-east-1
<a name="why-single-region-us-east-1"></a>

ADP v0.2 is pinned to `us-east-1` throughout. The IAM Identity Center instance is regional and lives only in `us-east-1`. The `governance` stack creates IAM Identity Center groups against that store, so deployment in any other region fails at governance creation. This forecloses the CMS-style "region as stage" pattern for ADP — `staging` and `prod` are prefix-distinguished within the single `us-east-1` account. See `docs/DEPLOYMENT.md` § *Why single-region* for the definitive explanation. The v0.1 EU Data Act / GDPR multi-region split is out of foundation v1 scope.

## Deploy flow
<a name="deploy-flow"></a>

The standard deploy flow runs in five steps from `platform-foundation/`. The full sanctioned command table and exact invocations are in `docs/DEPLOYMENT.md` § *Stage deploy (`make deploy STAGE=…​`)* and § *Sanctioned commands* — this section describes the narrative sequence.

### Step 1: Install dependencies
<a name="step-1-install-dependencies"></a>

Set up the Python virtual environment and install CDK and project dependencies. The equivalent one-shot is `make venv`. Before proceeding, confirm all tool prerequisites (Python 3.12\+, Node.js 22.x, AWS CDK CLI 2.255\+, AWS CLI v2 2.15\+, Docker 24\+, jq) and AWS account prerequisites (default credentials, CDK bootstrapped in `us-east-1`, IAM Identity Center enabled in `us-east-1`). See `docs/DEPLOYMENT.md` § *Prereqs* for the full prerequisite checklist and verify commands.

### Step 2: Bootstrap (once per account)
<a name="step-2-bootstrap-once-per-account"></a>

Run `make bootstrap` before the first stage deploy. This deploys the `adp-shared-bootstrap` stack, which enables the Amazon Macie session at account level. The bootstrap is idempotent and safe to re-run. See `docs/DEPLOYMENT.md` § *One-time bootstrap (account-level)* for the expected outcome table and notes on the Macie 30-day cool-down.

### Step 3: Deploy the foundation stacks
<a name="step-3-deploy-the-foundation-stacks"></a>

```
make deploy STAGE=staging
```

or

```
make deploy STAGE=prod
```

This deploys all five per-stage stacks in dependency order (network → lake → datazone → datazone-projects → governance). Approximate time: 15–25 minutes per stage; DataZone domain creation is the slow step. See `docs/DEPLOYMENT.md` § *Stage deploy (`make deploy STAGE=…​`)* for the expected outcome verification table.

### Step 4: Seed the data lake
<a name="step-4-seed-the-data-lake"></a>

```
make seed STAGE=staging
```

 `make seed` is the master seed target: it generates dimension catalogs plus 9 product generators, runs referential-integrity tests, and uploads results to the stage’s lake bucket. For PySpark-tier products (`vehicle_telemetry_aggregated`, `energy_usage`), generation runs via AWS Glue 5.1 (managed compute) rather than the local venv. See `docs/DEPLOYMENT.md` § *Post-deploy seed validation* and § *PySpark generators (Glue 5.1) — sample tier* for the four-phase seeding flow.

### Step 5: Smoke-test
<a name="step-5-smoke-test"></a>

```
make smoke-test STAGE=staging
```

The smoke test validates the DataZone subscription flow end-to-end — domain availability, Glue catalog reachability, project exports, and a live `SELECT COUNT(*)` on `vehicle_telemetry_aggregated`. The deploy is not complete until the smoke test exits 0. See `docs/DEPLOYMENT.md` § *Smoke test* for the five-step test sequence and the post-deploy CloudWatch monitoring scan pattern.

## Cross-cutting governance layer
<a name="cross-cutting-governance-layer"></a>

The `governance` stack deploys four cross-cutting controls that apply to all 9 governed data products. These controls are not per-product — they are platform-wide and cannot be selectively disabled per product.

### Lake Formation tag-based access control
<a name="lake-formation-tag-based-access-control"></a>

The `governance` stack registers the S3 lake bucket with AWS Lake Formation and applies tag-based access control (LF-TBAC) across all 10 Glue databases. Access is governed by the three IAM Identity Center groups created in the same stack:
+  `adp-{stage}-data-owners` — Lake Formation data-owner permissions; intended for data product producers and platform engineers.
+  `adp-{stage}-data-consumers` — Lake Formation consumer permissions; intended for analysts, SageMaker Studio notebook users, and application consumers such as CVX agents.
+  `adp-{stage}-platform-admins` — Administrative permissions for platform operations and Lake Formation grant management.

Fine-grained column-level permissions are applied on PII-bearing tables. Bedrock Knowledge Base ingestion reads the lake via S3 directly (not via Lake Formation vended credentials) — see `docs/DEPLOYMENT.md` § *Bedrock KB cross-account integration* for the integration patterns and the cross-account grant requirement.

### Amazon Macie classification
<a name="amazon-macie-classification"></a>

The `adp-shared-bootstrap` stack enables an Amazon Macie session at account level. The per-stage Macie classification job is bucket-scoped and created post-deploy via `scripts/macie-create-job.sh`. Macie automated discovery jobs classify PII-bearing prefixes on the lake S3 bucket; findings surface in Amazon Security Hub.

Note: Macie has a 30-day cool-down period after disabling. If `make bootstrap` reports "Macie is already enabled," the session is already active and no action is required. See `docs/DEPLOYMENT.md` § *Troubleshooting* for the resolution path.

### CloudTrail data-event logging
<a name="cloudtrail-data-event-logging"></a>

The `governance` stack creates an AWS CloudTrail trail configured for data-event logging on the lake S3 bucket. Every `GetObject`, `PutObject`, and `DeleteObject` API call is recorded, providing an immutable audit trail of all data access within the lake. The trail name follows `adp-{stage}-foundation-lake-trail`; the KMS alias is `alias/adp-{stage}-foundation-trail`.

### IAM Identity Center groups
<a name="iam-identity-center-groups"></a>

The three IAM Identity Center (IDC) groups per stage are described in the Lake Formation section above. IDC groups are regional and live only in `us-east-1` — which is the primary reason ADP is single-region (`us-east-1`) in v0.2. See § *Why single-region us-east-1* above and `docs/DEPLOYMENT.md` § *Why single-region* for the authoritative explanation.

## Vehicle Knowledge Base
<a name="vehicle-knowledge-base"></a>

The Vehicle Knowledge Base (`vehicle_knowledge_base`) is the ninth governed data product. It differs from the other eight Iceberg-backed products in that it is stored as direct S3 artifacts (Markdown documents, DTC guides, TSBs, recall notices) backed by an Amazon Bedrock Knowledge Base with an Amazon OpenSearch Serverless (AOSS) vectorsearch collection.

**Warning**  
AOSS vectorsearch collections have a 2-OCU minimum. Each stage (staging, prod) costs **\~$345/month** at idle, even with `STANDBY_REPLICAS=DISABLED`. Two stages = \~$700/month continuous. Validate the staging-MVP business case before deploying the production stage. See `docs/DEPLOYMENT.md` § *Vehicle Knowledge Base (Bedrock KB \+ AOSS) deploy* for the full operator runbook including the eight-step deploy sequence and tear-down instructions.

The Vehicle Knowledge Base is consumed by the CVX agent platform for retrieval-augmented generation (RAG) over vehicle maintenance and diagnostic documentation. For the `vehicle_knowledge_base` data product’s technical specification — including its S3 prefix layout and DataZone project — see [Data products](data-products.md).

## Optional CMS→ADP ingest module
<a name="optional-cmsadp-ingest-module"></a>

The optional CMS→ADP ingest module is **off by default**. Running `make deploy STAGE=staging|prod` creates zero CMS-ingest resources. Enable only when CMS and ADP are deployed in the same AWS account, the CMS DynamoDB table is in `us-east-1`, and DynamoDB Streams are enabled with `StreamViewType = NEW_AND_OLD_IMAGES`.

When enabled, the module deploys an optional sixth per-stage stack (`adp-{stage}-foundation-cms-ingest`) that pipelines CMS DynamoDB Streams events through Amazon Kinesis Data Firehose into an Apache Iceberg table in the ADP lake, via a 15-minute AWS EventBridge-scheduled AWS Glue MERGE job. End-to-end wire-to-queryable latency is typically 1–16 minutes depending on EventBridge slot timing. Enabling raises the monthly cost estimate from \~$300–600 to \~$550–860.

The full operator runbook for this module — including the enable command, post-enable smoke test, and disable procedure — lives in `docs/cms-ingest-optional-module.md`. See also `docs/DEPLOYMENT.md` § *Optional: CMS→ADP ingest module*.

## Teardown
<a name="teardown"></a>

Per-stage teardown removes a single stage’s stacks while leaving the `adp-shared-bootstrap` stack and the other stage untouched.

**Warning**  
Teardown is destructive. The lake KMS CMK is retained (`RemovalPolicy.RETAIN`); encrypted data may outlive the stack. CloudFormation stack history, IAM Identity Center group IDs, and DataZone project IDs are not recoverable — new IDs are issued on the next deploy. Synthetic data is regenerable via `make seed STAGE=…​`.

The Makefile `teardown` target defaults to **dry-run** mode: it prints what would be deleted without destroying anything. Pass `YES=1` to execute:

```
make teardown STAGE=staging
```

```
make teardown STAGE=staging YES=1
```

The teardown script executes a six-step sequence (see `docs/DEPLOYMENT.md` § *Stage-side teardown* for the authoritative steps):

1. Stop the stage CloudTrail trail gracefully.

1. Empty the three S3 buckets (lake, lake-logs, trail-logs) including all versions and delete markers.

1. Pre-empt the DataZone domain delete via `aws datazone delete-domain --skip-deletion-check` to cascade through the 10 retained `CfnProject` resources.

1.  `cdk destroy --force -c stage=<stage>` with an explicit stack list. The optional `cms-ingest` stack is auto-detected and included if present. `--all` is never used — it would walk into `adp-shared-bootstrap`.

1. Idempotent IAM Identity Center group cleanup fallback.

1. Verify: assert no `adp-{stage}-foundation-*` stacks remain and `adp-shared-bootstrap` is still `CREATE_COMPLETE`/`UPDATE_COMPLETE`.

After successful teardown, re-deploy with:

```
make deploy STAGE=staging
make seed STAGE=staging
make smoke-test STAGE=staging
```

The new deploy creates fresh resources with the same stage-prefixed names but new CloudFormation stack IDs, DataZone project IDs, and IAM Identity Center group IDs. The lake KMS CMK is re-used (the deterministic alias `alias/adp-{stage}-foundation-lake` resolves to the retained key).