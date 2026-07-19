# Developer guide

This chapter explains how to work in this repository as a developer or contributor.
It covers the canonical directory layout (v0.2+), local environment setup, the
Makefile-driven workflow, how to add or extend a data product, and the one-time
cost-allocation tag activation procedure.

## Repository layout

The v0.2 re-framing collapses the former collection of five independently-deployable
guidances into one foundation deploy under `platform-foundation/`.

```
automotive-data-platform-on-aws/
├── platform-foundation/          # ← canonical foundation deploy (v0.2+)
│   ├── app.py                    # CDK app (5 stage stacks + bootstrap)
│   ├── stacks/                   # network, lake, datazone, datazone-projects,
│   │                             #   governance, vehicle_knowledge_base
│   ├── source/
│   │   ├── data-products/        # 9 product generators + per-product schemas
│   │   ├── dimensions/           # 7 dimension-catalog generators
│   │   ├── athena-queries/       # cross-product join examples
│   │   ├── reference-consumers/  # predictive-maintenance SageMaker notebook
│   │   ├── quality-dashboard/    # CloudWatch data-quality dashboard
│   │   └── optional/cms_ingest/  # opt-in CMS DDB → ADP Iceberg ingest
│   ├── scripts/                  # deploy, smoke-test, verify, teardown, profile
│   └── tests/                    # 150+ schema, FK, edge-case, distribution tests
│
├── docs/
│   ├── DEPLOYMENT.md             # per-stage runbook (authoritative for deploy)
│   ├── data-contracts.md         # VSS subset, identifier formats, partitions
│   ├── cvx-integration-contract.md  # contract for CVX consumers
│   ├── cms-ingest-optional-module.md # opt-in CMS ingest doc
│   └── tech.md                   # SDK/framework verification notes (see below)
│
├── guidance-for-*/               # demoted — source-of-logic only (see Migration)
└── datasource/                   # demoted — superseded by platform-foundation/
```

### v0.1 paths are demoted

The legacy subdirectories still exist for historical reference but are **not**
independently deployable in v0.2.

| v0.1 location                                 | v0.2 disposition                                                                                                                        |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Agentic Customer 360 subdir                   | Demoted — generation logic ported into `platform-foundation/source/data-products/{customer_360,customer_interactions,service_records}/` |
| Vehicle Knowledge Base subdir                 | Deleted — generators ported into `platform-foundation/source/data-products/vehicle_knowledge_base/`                                     |
| Telemetry Normalization subdir                | Demoted — patterns inform the `vehicle_telemetry_aggregated` generator                                                                  |
| Data Governance subdir                        | Demoted — replaced by foundation’s Lake Formation + Macie + CloudTrail layer                                                            |
| Predictive Maintenance subdir                 | Demoted — replaced by `platform-foundation/source/reference-consumers/`                                                                 |
| `datasource/cx-analytics/`, `datasource/crm/` | Demoted — superseded by `platform-foundation/source/data-products/`                                                                     |

Each demoted subdir’s `README.md` carries a `DEPRECATED — see platform-foundation/`
notice at the top.

### Per-product documentation

Each of the 9 data products has its own README that is the authoritative reference
for schema, partitions, sample queries, edge-case injection rules, and lineage:

```
platform-foundation/source/data-products/<product>/README.md
```

For example:

```
platform-foundation/source/data-products/vehicle_identity/README.md
platform-foundation/source/data-products/charging_sessions/README.md
platform-foundation/source/data-products/vehicle_knowledge_base/README.md
```

Cross-product join examples live in:

```
platform-foundation/source/athena-queries/
```

### SDK verification notes

`docs/tech.md` contains verified import paths, constructor signatures, and usage
patterns for the key dependencies used in this repo — DataZone V2, Glue Iceberg,
Athena Engine V3, Lake Formation, Bedrock KB, PyIceberg, Kinesis Firehose, and the
VSS spec. Consult `docs/tech.md`
**before** writing code that calls any of these
APIs to avoid writing against unverified or stale SDK surfaces.

## Development prerequisites

For the full, verifiable prerequisites table with exact version-check commands see
`docs/DEPLOYMENT.md` § Prereqs. Summary:

| Tool + minimum version        | Notes                                       |
| ----------------------------- | ------------------------------------------- |
| Python 3.12+ (3.14 supported) | Used for CDK app, generators, tests         |
| Node 22.x LTS                 | Required by AWS CDK CLI (jsii bridge)       |
| AWS CDK CLI 2.255+            | Install via `npm install -g aws-cdk`        |
| AWS CLI v2 2.15+              | Must be v2; v1 is not supported             |
| Docker 24+                    | Required for CDK bootstrap asset publishing |
| jq (any)                      | Used by helper scripts for JSON parsing     |

All tools must be on `PATH` and pass the verify commands listed in
`docs/DEPLOYMENT.md` § Prereqs before proceeding.

## Setting up a local environment

### Create the virtual environment

All Python work — CDK synthesis, generators, tests — runs inside the project
venv. Run from `platform-foundation/`:

```
make venv
```

This is equivalent to:

```
cd platform-foundation
python3 -m venv .venv
source .venv/bin/activate
pip install -q --upgrade pip
pip install -r requirements.txt
```

Verify the venv is functional:

```
.venv/bin/python -c "import aws_cdk, constructs, cdk_nag; print('OK')"
```

### Install project dependencies

If `make venv` did not install everything, or after pulling changes:

```
make install
```

This installs the pinned versions from `requirements.txt` into `.venv`.

## Development workflow

###### Important

**The `Makefile` is the only sanctioned entry point.**
Direct `cdk deploy` without `-c stage=…​` triggers `app.py’s fail-closed guard and
may produce stacks with unprefixed names that collide with existing deploys.
All commands in this section run from `platform-foundation/`.

The standard contributor workflow proceeds through six steps.

### Step 1 — Create the virtual environment

```
make venv
```

### Step 2 — Install dependencies

```
make install
```

### Step 3 — Bootstrap (one-time per account)

```
make bootstrap
```

Deploys `adp-shared-bootstrap` (the Macie session stack).
Safe to re-run; CloudFormation no-ops when the stack is already `CREATE_COMPLETE`.

### Step 4 — Deploy a stage

```
make deploy STAGE=staging
```

`STAGE` is required and fail-closed. Supported values: `staging`, `prod`
(lower-case, case-sensitive). `make deploy` with no `STAGE` exits non-zero.

### Step 5 — Seed data

```
make seed STAGE=staging
```

Runs the master seed pipeline: dimensions first, then all 9 product generators in
order, then referential-integrity tests. Requires `make deploy STAGE=staging` to
have completed successfully.

### Step 6 — Smoke test

```
make smoke-test STAGE=staging
```

Validates the DataZone subscription end-to-end. Exits non-zero on any failure.
A deploy is not considered complete until the smoke test passes.

### Full command reference

The complete list of sanctioned Makefile targets:

| Command                                            | Purpose                                                              |
| -------------------------------------------------- | -------------------------------------------------------------------- |
| `make venv`                                        | Create `.venv` and install dependencies                              |
| `make install`                                     | Install / refresh dependencies into existing `.venv`                 |
| `make bootstrap`                                   | Deploy account-level `adp-shared-bootstrap` stack (once per account) |
| `make deploy STAGE=staging                         | prod`                                                                | Deploy the 5 per-stage foundation stacks                 |
| `make seed STAGE=staging                           | prod`                                                                | Master seed: dimensions + 9 generators + integrity tests |
| `make seed-dimensions STAGE=staging                | prod`                                                                | Generate dimension catalog only                          |
| `make smoke-test STAGE=staging                     | prod`                                                                | Post-deploy DataZone subscription smoke test             |
| `make verify-standalone STAGE=staging              | prod`                                                                | Synth-time check — no CMS ARNs leak into templates       |
| `make synth STAGE=staging                          | prod`                                                                | CDK synthesis only (no deploy)                           |
| `make teardown STAGE=staging                       | prod [YES=1]`                                                        | Tear down per-stage stacks (default dry-run)             |
| `make deploy-cms-ingest STAGE=…​ CMS_TABLE_ARN=…​` | Deploy with optional CMS→ADP ingest enabled                          |

For deploy-runbook details (expected outcomes, post-deploy checks, tear-down) see
`docs/DEPLOYMENT.md`.

## Adding a new data product

Each data product in `platform-foundation/source/data-products/` follows a
consistent structure. To add a new product:

### 1. Create the product directory

```
mkdir -p platform-foundation/source/data-products/<product_name>
```

### 2. Write the generator

Create `platform-foundation/source/data-products/<product_name>/generator.py`.
Follow the conventions used by existing generators:

- Accept a `--stage` argument and a `--seed` argument (default `42`) for
  deterministic output.
- Read shared dimension catalogs from `platform-foundation/dimensions/` via the
  shared dimension-loader helper.
- Write output as Parquet files to `platform-foundation/curated/<product_name>/`
  partitioned per the conventions in `docs/data-contracts.md`.
- Preserve referential integrity with shared dimension keys (VIN, `customer_id`,
  `dealer_id`, etc.) — use `UUIDv5` generation for deterministic IDs.

### 3. Write the per-product README

Create `platform-foundation/source/data-products/<product_name>/README.md`.
This file is the authoritative reference for:

- Schema (column names, types, nullable flags)
- Partition strategy
- Edge-case injection rules
- Sample Athena queries
- Lineage (which dimension catalogs are consumed)

### 4. Register the Glue database and table

Add a new `CfnDatabase` and `CfnTable` (or Iceberg table) to the appropriate stack
in `platform-foundation/stacks/`. Follow the naming convention
`adp_{stage}_<product_name>`.

### 5. Add Lake Formation grants

Grant the DataZone producer project and any consumer roles the appropriate Lake
Formation permissions on the new database. See existing grant patterns in
`platform-foundation/stacks/governance_stack.py`.

### 6. Add the product to the seed pipeline

Register the new generator in the `make seed` pipeline so it runs after the
dimension catalogs are generated. Update the `Makefile’s `seed` target to include:

```
python source/data-products/<product_name>/generator.py --stage $(STAGE)
```

### 7. Write tests

Add schema, referential-integrity, and distribution tests in
`platform-foundation/tests/` following the pattern of existing test files. The
test suite is run as part of `make seed` and must remain at 0 failures.

### 8. Publish to DataZone

Create a DataZone data asset in the producer project for the new product and
configure the auto-grant policy so downstream consumers can subscribe. See
existing DataZone project setup in
`platform-foundation/stacks/datazone_projects_stack.py`.

## Extending a generator

To extend an existing generator (e.g., add a column, change a distribution,
increase row count):

1. Edit the generator at
   `platform-foundation/source/data-products/<product_name>/generator.py`.
2. Update the schema in the Glue table definition (or Iceberg schema evolution).
3. Update `platform-foundation/source/data-products/<product_name>/README.md` to
   reflect the schema change.
4. Update the contract test in `platform-foundation/tests/` to assert the new
   column’s presence and type.
5. Run `make seed STAGE=staging` and verify `make smoke-test STAGE=staging` still
   passes before committing.
6. Consult `docs/tech.md` for verified Iceberg / PyIceberg / Glue API patterns
   before writing schema-evolution code.

## Cost-allocation tag activation (one-time)

The foundation tags every per-stage stack resource with `adp:stage = <stage>`.
Per-stage cost reporting in AWS Cost Explorer and Budgets requires a **one-time
activation** of this tag:

```
aws ce update-cost-allocation-tags-status \
    --region us-east-1 \
    --cost-allocation-tags-status TagKey=adp:stage,Status=Active
```

###### Note

This is an account-level, one-time operation. After activation, allow up to 24 hours
for the tag to populate Cost Explorer. Until activated, Cost Explorer reports
aggregate ADP spend without a per-stage breakdown.

If the AWS CLI is unavailable, activate the tag in the **Billing console →
Cost Allocation Tags → User-defined tags → activate `adp:stage`**.

The `adp-shared-bootstrap` stack intentionally does **not** carry the `adp:stage`
tag — the bootstrap is account-singular, not stage-bound.

## Running tests

The test suite lives in `platform-foundation/tests/`.

```
cd platform-foundation
source .venv/bin/activate
pytest tests/ -v
```

Tests that require curated data (generated by `make seed`) are decorated with
`@pytest.mark.needs_curated` and skip automatically when the data is absent.
The offline suite (schema, referential-integrity contracts, distribution contracts)
runs without any deployed infrastructure.

Expected baseline: 150+ passing, some skipped when curated data is absent, 0 failures.

## Security practices for contributors

- IAM policies must follow least-privilege. When adding a new resource, scope its
  IAM grants to the specific resource ARN, not a wildcard `*` unless a named
  exception is suppressed in `NagSuppressions` with a documented rationale.
- Every new S3 bucket must use the project’s KMS CMK (`alias/adp-{stage}-foundation-lake`)
  and carry `RemovalPolicy.RETAIN` if it holds globally-namespaced names.
- Verify all SDK calls against `docs/tech.md` before implementation. Do not rely
  on memory or model knowledge for IAM ARN formats, constructor signatures, or
  Iceberg API surface — consult `docs/tech.md` or the official AWS documentation.
- Run `make verify-standalone STAGE=staging` before opening a pull request. This
  synth-time check confirms no CMS ARNs have leaked into the foundation templates.

## CI gates

The CI pipeline enforces the following gates on every pull request:

| Gate                     | Command                                  | Pass condition         |
| ------------------------ | ---------------------------------------- | ---------------------- |
| Standalone-deploy verify | `make verify-standalone STAGE=staging`   | exits 0                |
| CMS-standalone verify    | `./scripts/verify-cms-standalone.sh dev` | exits 0                |
| Pytest suite             | `pytest tests/ -v`                       | 0 failures             |
| CDK synth (staging)      | `make synth STAGE=staging`               | exits 0, cdk-nag clean |
| CDK synth (prod)         | `make synth STAGE=prod`                  | exits 0, cdk-nag clean |

The smoke test runs against the live staging environment after each merge to `main`
that touches `platform-foundation/`.

## Additional resources

| Resource                                                       | What it covers                                                                           |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `docs/DEPLOYMENT.md`                                           | Per-stage deploy runbook, prereqs, smoke tests, tear-down, troubleshooting               |
| `docs/data-contracts.md`                                       | VSS signal subset, identifier formats, partition conventions                             |
| `docs/cvx-integration-contract.md`                             | CVX subscription flow, sample Athena queries, Bedrock KB seeding                         |
| `docs/cms-ingest-optional-module.md`                           | Opt-in CMS → ADP ingest module                                                           |
| `docs/tech.md`                                                 | SDK/framework verification notes — DataZone V2, Glue Iceberg, Bedrock KB, Lake Formation |
| `platform-foundation/README.md`                                | Foundation-level overview                                                                |
| `platform-foundation/source/data-products/<product>/README.md` | Per-product schema, partitions, sample queries, lineage                                  |
| `platform-foundation/source/athena-queries/`                   | Cross-product join examples                                                              |
