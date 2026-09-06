

# Update the guidance
<a name="update-the-guidance"></a>

This chapter describes how to update the Automotive Data Platform foundation and migrate from previous releases.

## Migrating from v0.1.0
<a name="migrating-from-v0-1-0"></a>

v0.2 is a deliberate scope re-frame, not an incremental upgrade. The five independently-deployable guidances (`guidance-for-agentic-customer-360`, `guidance-for-predictive-maintenance`, `guidance-for-telemetry-normalization`, `guidance-for-data-governance`, `guidance-for-vehicle-knowledge-base`) have been demoted in favour of a single unified foundation deploy under `platform-foundation/` that publishes 9 DataZone-cataloged data products sharing dimension keys (VIN, customer\_id, dealer\_id, supplier\_id, part\_number, station\_id). Operational layers that v0.1.0 shipped — QuickSight dashboards, custom Bedrock-Agent CDK, Aurora pgvector, SageMaker tire-anomaly API, and Flink-based real-time normalization — are intentionally not in v0.2; downstream consumers (CVX, notebooks, BI tools) own those concerns. There is **no in-place upgrade path**: tear down all v0.1.0 stacks (`cdk destroy --all` per guidance subdir), empty and delete v0.1.0 S3 buckets, then follow `docs/DEPLOYMENT.md` to deploy the v0.2 foundation from scratch.

For the complete disposition table of every v0.1.0 subdir, the full list of what was added and what was dropped, and the step-by-step teardown-and-redeploy sequence, see [docs/MIGRATION-FROM-V0.1.0.md](../../../docs/MIGRATION-FROM-V0.1.0.md).

## Update Strategy
<a name="update-strategy"></a>

The foundation follows a pull-review-deploy-verify cycle for all updates. The `Makefile` is the only sanctioned entry point — do not invoke `cdk deploy` directly, as this bypasses the `STAGE` validation guard.

### Standard foundation update flow
<a name="standard-foundation-update-flow"></a>

```
# 1. Pull the latest code
cd automotive-data-platform-on-aws
git pull

# 2. Review what changed
#    - Migration notes for breaking changes:
cat docs/MIGRATION-FROM-V0.1.0.md

#    - Revision history and per-release notes:
cat docs/revisions.adoc

#    - Changelog for version-by-version diff:
cat CHANGELOG.md

# 3. Deploy the updated foundation (staging first)
cd platform-foundation
make deploy STAGE=staging

# 4. Verify the deploy with the smoke-test contract
#    (deploy is not complete until smoke-test exits 0)
make smoke-test STAGE=staging
echo "Exit code: $?"   # Must be 0

# 5. Promote to prod after staging smoke-test passes
make deploy STAGE=prod
make smoke-test STAGE=prod
echo "Exit code: $?"   # Must be 0
```

The `make smoke-test STAGE=<stage>` target satisfies the deploy-validation contract defined in `~/.kiro/steering/deploy-validation.md`: it exits non-zero on any check failure, so a failed smoke test is treated as a failed deploy. Do not run downstream operator tasks (seed refresh, new subscriptions, queries) until the smoke test exits 0.

For the full deploy prereq checklist, expected CloudFormation outcomes, and post-deploy CloudWatch scan, see `docs/DEPLOYMENT.md`.

## Schema Evolution
<a name="schema-evolution"></a>

The foundation uses Apache Iceberg as the table format for all v0.2 data products. Iceberg supports non-destructive schema evolution without requiring a full re-seed.

### Supported Iceberg schema changes
<a name="supported-iceberg-schema-changes"></a>

The following schema changes are backwards-compatible and do not break existing Athena or DataZone consumers:
+  **Add a nullable column** — consumers that do not reference the new column continue to read existing data unchanged.
+  **Rename a column** — Iceberg tracks column identity by ID, not name. Existing Parquet files are re-read correctly after a rename; consumers must update column references in their queries.
+  **Widen a numeric type** — e.g., `int` to `long`. Existing data is automatically widened on read.
+  **Reorder columns** — column order in Parquet files is decoupled from logical schema order.

The following changes are **breaking** and require coordination:
+  **Drop a required column** — breaks any consumer that selects or filters on that column.
+  **Narrow a type** — e.g., `long` to `int` — may truncate existing values.
+  **Change partition spec** — existing partition directories are not retroactively reorganised; new writes go to new partition paths, but old data is still readable via the Iceberg metadata layer.

For identifier conventions, VSS signal vocabulary subset, and explicit non-dependencies between ADP and CMS, see [docs/data-contracts.md](../../../docs/data-contracts.md).

### Applying a schema change
<a name="applying-a-schema-change"></a>

```
# 1. Update the Glue catalog table definition (Iceberg ALTER TABLE via Athena)
aws athena start-query-execution \
  --query-string "ALTER TABLE adp_staging_vehicle_telemetry_aggregated.vehicle_telemetry_aggregated ADD COLUMNS (new_column STRING COMMENT 'added in v0.2.1')" \
  --query-execution-context Database=adp_staging_vehicle_telemetry_aggregated \
  --result-configuration OutputLocation=s3://adp-staging-foundation-lake-${ACCOUNT}-us-east-1/athena-results/ \
  --region us-east-1

# 2. Update the generator schema definition and data-contracts.md
#    (schema change is not complete until both the catalog and the
#     source of truth in data-contracts.md reflect the change)
# Edit: platform-foundation/source/data-products/<product>/schema.json
# Edit: docs/data-contracts.md

# 3. Re-publish the DataZone asset so downstream subscribers see the updated schema
aws datazone create-asset-revision \
  --domain-identifier $DOMAIN_ID \
  --identifier $ASSET_ID \
  --name "<product-name>" \
  --region us-east-1
```

## New Data Product Onboarding
<a name="new-data-product-onboarding"></a>

To onboard a new data product into the foundation, follow the pattern established by the 9 existing products under `platform-foundation/source/data-products/`.

### Onboarding checklist
<a name="onboarding-checklist"></a>

1.  **Define the schema** in `platform-foundation/source/data-products/<product>/schema.json` following the conventions in `docs/data-contracts.md` — identifier formats, VSS signal subset (if applicable), partition conventions, and calibrated edge-case injection rates (1–3% across six taxonomy codes).

1.  **Write the generator** at `platform-foundation/source/data-products/<product>/generator.py` using the same deterministic-seed pattern as existing products (seed-42 default → byte-identical regeneration).

1.  **Add a per-product README** at `platform-foundation/source/data-products/<product>/README.md` with schema, partitions, sample queries, lineage, and data-quality summary.

1.  **Register a Glue database and Iceberg table** in `platform-foundation/stacks/lake_stack.py` following the existing `adp_{stage}_<product>` naming convention.

1.  **Create a DataZone project** in `platform-foundation/stacks/datazone_projects_stack.py` following the existing 9-project pattern (one project per product).

1.  **Update `docs/data-contracts.md` ** to document the new product’s identifier formats, partition spec, and any cross-product FK relationships.

1.  **Add referential-integrity tests** in `platform-foundation/tests/test_referential_integrity.py` asserting FK closure for any dimension keys the new product references (VIN, customer\_id, dealer\_id, supplier\_id, part\_number, station\_id, or charging\_station\_id).

1.  **Re-run the full seed and smoke-test**:

   ```
   make seed STAGE=staging
   make smoke-test STAGE=staging
   ```

### Dimension key requirements
<a name="dimension-key-requirements"></a>

All new data products **must** join on the canonical dimension keys defined in `docs/data-contracts.md`. Do not introduce a new top-level identifier type without updating the dimensions catalog and the data-contracts spec. FK closure is enforced by `tests/test_referential_integrity.py` and must pass before a new product is promoted to staging.

## Rollback Procedures
<a name="rollback-procedures"></a>

### Rollback a CDK stack update
<a name="rollback-a-cdk-stack-update"></a>

```
# Cancel an in-progress update
aws cloudformation cancel-update-stack \
  --stack-name adp-staging-foundation-lake

# Or redeploy from a prior Git commit
git checkout <prior-commit>
cd platform-foundation
make deploy STAGE=staging
make smoke-test STAGE=staging
```

### Rollback a seed run
<a name="rollback-a-seed-run"></a>

The seed is fully reversible per `docs/DEPLOYMENT.md`:

```
ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
BUCKET="adp-staging-foundation-lake-${ACCOUNT}-us-east-1"

# Remove curated data, dimensions, and quality reports from S3
aws s3 rm --recursive s3://${BUCKET}/curated/
aws s3 rm --recursive s3://${BUCKET}/dimensions/
aws s3 rm --recursive s3://${BUCKET}/quality-reports/

# Re-seed from a deterministic seed (byte-identical regeneration)
cd platform-foundation
make seed STAGE=staging
make smoke-test STAGE=staging
```

## Update Best Practices
<a name="update-best-practices"></a>
+ Always deploy staging before prod — let `make smoke-test STAGE=staging` pass before promoting.
+ Run `git pull` and review `docs/MIGRATION-FROM-V0.1.0.md`, `docs/revisions.adoc`, and `CHANGELOG.md` before any deploy to catch breaking changes.
+ Use `cdk diff` (`make diff STAGE=staging`) to preview CloudFormation changes before applying.
+ A deploy is not complete until `make smoke-test STAGE=<stage>` exits 0.
+ Schema changes require updating both the Glue catalog and `docs/data-contracts.md` in the same commit.
+ New data products require FK closure tests before promotion to staging.