# Troubleshooting

This chapter provides solutions to common issues encountered when deploying and operating the Automotive Data Platform foundation (`platform-foundation/`). All commands assume `STAGE=staging` unless noted; substitute `prod` where applicable.

###### Note

The `Makefile` is the only sanctioned entry point for all deploy, seed, and smoke-test operations. Direct `cdk` invocations are noted only where specifically required for debugging.

## Deploy and Synth Issues

### `cdk synth` fails with "stage is required"

**Symptom**: Running `cdk synth` directly exits with an error such as `ValueError: stage is required` or `AssertionError`.

**Cause**: `app.py` validates the `-c stage=staging|prod` context flag on startup. Invoking `cdk` directly skips the Makefile’s stage injection.

**Fix**: Always use the Makefile entry point:

```
cd platform-foundation
make synth STAGE=staging
# OR
make deploy STAGE=staging
```

If you must invoke CDK directly for debugging, prefix with the stage context flag:

```
.venv/bin/cdk synth -c stage=staging adp-staging-foundation-lake
```

### `cdk-nag` errors on deploy

**Symptom**: `make deploy STAGE=staging` fails with `Error: Validation failed with the following errors` listing `AwsSolutions-*` rule IDs.

**Cause**: `cdk-nag` errors (not warnings) block deployment. Warnings are advisory only.

**Fix**: Run synth first to inspect the nag report, then locate the suppression in the stack source:

```
cd platform-foundation
make synth STAGE=staging
# Inspect per-stack nag CSV reports:
ls cdk.out/AwsSolutions-*-NagReport.csv
```

Existing suppressions live alongside their constructs — search for `NagSuppressions` in `platform-foundation/stacks/*.py`. Add a suppression with a `reason=` string for any newly introduced finding, or fix the underlying resource configuration.

### `cdk synth` fails on first run (missing dependencies)

**Symptom**: Import errors such as `ModuleNotFoundError: No module named 'aws_cdk'` or `node: command not found`.

**Fix**:

```
# Verify venv and install dependencies
cd platform-foundation
make venv
source .venv/bin/activate
pip show aws-cdk-lib        # must return a version
node --version              # must return v22.x (CDK jsii bridge requires Node.js)
```

Re-run `make venv` if the venv is incomplete or was built against a different Python version.

## DataZone and Identity Center Issues

### DataZone domain creation hangs

**Symptom**: `adp-{stage}-foundation-datazone` stack stays in `CREATE_IN_PROGRESS` for more than 20 minutes during domain creation.

**Cause**: IAM Identity Center (IDC) must be enabled in `us-east-1`. If the IDC instance is in another region, or if the domain name collides with an existing `automotive-data-platform` deployment, domain creation stalls.

**Fix**:

1. Confirm IDC is in `us-east-1`:

```
aws sso-admin list-instances --region us-east-1 \
    --query 'Instances[0].IdentityStoreId' --output text
```

If this returns `None` or an error, enable IAM Identity Center in us-east-1 before retrying. 2. Confirm no name collision:

```
aws datazone list-domains --region us-east-1 \
    --query 'items[?name==`adp-staging-foundation-domain`].id' --output text
```

If a domain already exists with that name from a legacy deploy, either reuse it (CDK import) or tear down the legacy domain first.

### IAM Identity Center group creation fails

**Symptom**: `adp-{stage}-foundation-governance` stack fails with `ConflictException` or `AlreadyExistsException` on IDC group creation.

**Cause**: The `identity_store_id` context value does not match the account’s actual IDC IdentityStore ID, or IDC has been recreated and the store ID changed.

**Fix**:

```
# Resolve the canonical store ID for this account
aws sso-admin list-instances --region us-east-1 \
    --query 'Instances[0].IdentityStoreId' --output text
```

Supply the resolved value at deploy time:

```
make deploy STAGE=staging   # Makefile reads IDC_STORE_ID from environment or prompts
# If passing manually:
.venv/bin/cdk deploy -c stage=staging -c identity_store_id=d-<idc-store-id> ...
```

IDC group creation is idempotent — re-running deploy after a partial failure will pick up where it left off.

## Bootstrap and Macie Issues

### Macie session error: "Macie is already enabled"

**Symptom**: `make bootstrap` fails with `ResourceConflictException: Macie is already enabled in this account`.

**Cause**: `adp-shared-bootstrap` creates `AWS::Macie::Session`. If Macie was already enabled by another workload, CloudFormation cannot create a second session.

**Fix** — choose one:

- **Import existing session** (preferred — preserves continuity):

```
.venv/bin/cdk import adp-shared-bootstrap -c stage=staging
```

- **Disable and re-enable** (lossy — 30-day cool-down applies):

```
aws macie2 disable-macie --region us-east-1
# Wait for disable to complete, then re-run:
make bootstrap
```

###### Warning

`aws macie2 disable-macie` triggers a 30-day cool-down period before Macie can be re-enabled. Do not use this path if Macie is in active use by another workload in the account.

## S3 and Naming Issues

### S3 bucket name conflict

**Symptom**: Stack creation fails with `BucketAlreadyOwnedByYou` or `BucketAlreadyExists` on the lake bucket.

**Cause**: S3 bucket names are globally unique. The foundation names buckets `adp-{stage}-foundation-lake-<account>-us-east-1`; the `<account>` suffix prevents most collisions, but a different AWS account could own the same name.

**Fix**: Verify whether the bucket belongs to your account:

```
ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
aws s3 ls s3://adp-staging-foundation-lake-${ACCOUNT}-us-east-1/ 2>&1 | head -3
```

If the bucket is owned by your account (e.g., from a partial prior deploy), the re-deploy will reuse it. If owned by a different account, use a one-off prefix override in `platform-foundation/lib/_naming.py` — this is a non-standard path; contact the platform team before proceeding.

## Smoke Test Issues

### Subscription smoke test fails with "asset not found"

**Symptom**: `make smoke-test STAGE=staging` logs `asset not found` or `No published asset for vehicle_telemetry_aggregated`.

**Cause**: The DataZone asset is published by the `vehicle_telemetry_aggregated` generator (Group 3 of the seeding flow). Before `make seed STAGE=staging` completes end-to-end, the asset does not exist in the DataZone catalog.

**Fix**: Run the full seed and re-test:

```
cd platform-foundation
make seed STAGE=staging
make smoke-test STAGE=staging
echo "Exit code: $?"   # Must be 0
```

The smoke test logs a warning and falls through to a direct Athena read of the Glue table during pre-seed deploys. Row count > 0 is required only after the seed generators have published the asset.

## Bedrock Knowledge Base and AOSS Issues

### Bedrock KB cross-account integration: `AccessDeniedException` on Retrieve

**Symptom**: CVX agent calling `bedrock-agent-runtime:Retrieve` against the ADP-owned Bedrock Knowledge Base receives `AccessDeniedException`, even after DataZone subscription is active.

**Cause**: Bedrock KB ingestion reads source documents via the KB’s data-source IAM role calling S3 directly (`s3:ListBucket` / `s3:GetObject`). It does **not** use Lake Formation vended credentials. DataZone subscription grants are LF-mediated and do not cover Bedrock KB S3 reads. Two valid integration patterns exist:

**Pattern (a) — Same-account** (recommended for the current single-account topology):

Deploy the Bedrock KB in the same account as the ADP lake. The KB data-source role inherits in-account IAM; no bucket policy or LF grant changes are required. The lake KMS CMK key policy already permits in-account principals via the `kms:ViaService = s3.us-east-1.amazonaws.com` condition.

**Pattern (b) — Cross-account** (CVX KB in a different account from ADP):

1. ADP must add an explicit S3 bucket policy on `adp-{stage}-foundation-lake-<account>-us-east-1` allowing the CVX KB data-source role ARN `s3:ListBucket` and `s3:GetObject` on the `knowledge/vehicle_knowledge_base/sources/*` prefix.
2. ADP must update the lake KMS key policy (`alias/adp-{stage}-foundation-lake`) to allow that role `kms:Decrypt` and `kms:DescribeKey`.

```
# Verify the lake KMS key alias resolves and is enabled
aws kms describe-key --key-id "alias/adp-staging-foundation-lake" \
    --region us-east-1 --no-cli-pager \
    --query 'KeyMetadata.[KeyState,Enabled]' --output text
# Expected: ENABLED  True
```

###### Important

Pattern (b) requires an explicit ADP-side IaC change (bucket policy + KMS key policy scoped to the CVX KB role ARN). It is not a default capability of the foundation. File an ADP-side spec before wiring cross-account access; do not add ad-hoc policies.

### VKB / AOSS stack deploy fails with hard-coded sentinel error or KB is missing

**Symptom A**: Attempting to deploy a legacy `guidance-for-vehicle-knowledge-base/` directory fails immediately with `collection_arn` set to a hard-coded sentinel string (for example, a literal `"unresolved"`) or a `ValueError` on an unresolved CDK token.

**Symptom B**: After deploying the platform-foundation stack set, no Bedrock Knowledge Base resource exists and CVX grounding returns empty results.

**Cause A**: The legacy `guidance-for-vehicle-knowledge-base/` directory was deprecated in v0.2 and has been deleted. Any reference to that path is invalid.

**Cause B**: The Vehicle Knowledge Base stack (`adp-{stage}-foundation-vehicle-knowledge-base`) is a separate, optional deploy that incurs ~$345/month for the AOSS vectorsearch collection (2-OCU minimum). It is **not** included in the base `make deploy STAGE=staging` run.

**Fix**:

1. Use the platform-foundation Makefile — do not reference the legacy directory.
2. Acknowledge the ~$345/month AOSS cost before proceeding.
3. Deploy the VKB stack explicitly. Follow `docs/DEPLOYMENT.md` § Vehicle Knowledge Base — the full operator runbook is there. Key commands:

```
cd platform-foundation

# Step 0: resolve your deploy-role ARN
DEPLOY_ROLE_ARN=$(aws sts get-caller-identity --query Arn --output text)

# Deploy the VKB stack (8-12 min)
make deploy STAGE=staging \
    -c adpKbDeployRoleArn=$DEPLOY_ROLE_ARN \
    -c cvxKbPrincipals=arn:aws:iam::<account>:role/cvx-staging-kb-retrieval-role

# Capture the KB ID from outputs
aws cloudformation describe-stacks \
    --stack-name adp-staging-foundation-vehicle-knowledge-base \
    --query 'Stacks[0].Outputs' \
    --region us-east-1
```

4. Trigger the initial ingestion job and poll until `"status": "COMPLETE"` (see `docs/DEPLOYMENT.md` § Steps 6–7).
5. Smoke-test retrieval:

```
aws bedrock-agent-runtime retrieve \
    --knowledge-base-id <KB_ID> \
    --retrieval-query '{"text":"P0301 misfire cylinder"}' \
    --retrieval-configuration '{"vectorSearchConfiguration":{"numberOfResults":3}}' \
    --region us-east-1
```

## PySpark / Glue Issues

### PySpark generators fail locally (Python 3.14 + PySpark 3.5.6 incompatibility)

**Symptom**: Running the `vehicle_telemetry_aggregated` or `energy_usage` generator locally via `make seed STAGE=staging` fails with `PicklingError: RecursionError: Stack overflow` or `cloudpickle` serialization error.

**Cause**: PySpark 3.5.x only supports Python 3.7–3.11. The local venv on Python 3.12+ (including 3.14) cannot serialize the generator closures via cloudpickle.

**Fix**: Use the Glue 5.1 managed-compute path instead of the local venv. Glue 5.1 pins Spark 3.5.6 + Python 3.11, bypassing the local incompatibility entirely:

```
cd platform-foundation
source .venv/bin/activate

python3 scripts/run-pyspark-products.py \
    --stage staging --product both \
    --action stage-and-run \
    --rows 10000000 --days 90 --partitions 256 --seed 42 \
    --workers 4 --worker-type G.2X \
    --timeout-min 30 --wait
```

The remaining 6 pandas-tier data products generate cleanly via `make seed STAGE=staging` — the PySpark path applies only to `vehicle_telemetry_aggregated` and `energy_usage`.

### Glue 5.1 job: `Format != ICEBERG` on `aws glue get-table`

**Symptom**: After the PySpark Glue job completes, `aws glue get-table` for `vehicle_telemetry_aggregated` or `energy_usage` reports `StorageDescriptor.SerdeInfo.Name` is not Iceberg — the table is plain parquet.

**Cause**: The Iceberg `writeTo` path failed silently; the generator fell back to a plain parquet write. Most common causes: missing Lake Formation grant for the Spark-ETL role, or the Iceberg + Glue Catalog Spark configuration block was stripped.

**Fix**: Check CloudWatch for the root cause, then re-apply LF grants and re-run:

```
# Check Glue job logs for Iceberg writeTo failure
aws logs filter-log-events \
    --log-group-name "/aws-glue/jobs/output" \
    --log-stream-name-prefix "adp-staging-foundation-data-products" \
    --filter-pattern "?Iceberg ?writeTo ?LakeFormation ?AccessDenied" \
    --limit 10 --region us-east-1 --no-cli-pager \
    --query 'events[].message' --output text
```

Re-apply Lake Formation grants if missing (see `docs/DEPLOYMENT.md` § Lake Formation grants for the exact grant commands referencing `adp-staging-foundation-spark-etl-role-us-east-1`), then re-run the PySpark script with `--action stage-and-run`.

### Glue 5.1 job: `MetadataFetchFailedException` or executor OOM

**Symptom**: PySpark Glue job fails with `MetadataFetchFailedException` or an executor container is killed (OOM) during the Iceberg V2 bucketed write.

**Cause**: Off-heap memory pressure during the bucketed write under-provisioned worker configuration.

**Fix**: Ensure workers and type are set to the recommended values:

```
python3 scripts/run-pyspark-products.py \
    --stage staging --product both \
    --action stage-and-run \
    --workers 4 --worker-type G.2X \
    --partitions 256 --timeout-min 30 --wait
```

The default `--conf` block includes `spark.executor.memoryOverhead=6g`; do not strip it.

## Data Integrity Issues

### Referential integrity tests fail with `DRIFT-` or `'None'` orphans

**Symptom**: After `make seed STAGE=staging`, running `pytest tests/test_referential_integrity.py -v` reports `test_zero_orphan_customer_ids` or `test_zero_orphan_station_ids` FAIL with 0.34% customer ID orphans or ~14% station ID orphans. Orphan values contain the prefix `DRIFT-` or the literal string `None`.

**Cause**: Two generator bugs (now patched):

1. `schema_drift` edge-case injection was bleeding into FK columns that were marked `edge_case_eligible: true`, prepending `DRIFT-` to FK values and breaking referential integrity.
2. Home-station NULL values in `charging_sessions/generator.py` were coerced to the string `'None'` via a `str(s)` list comprehension.

Both bugs were fixed in the 2026-06-03 patch. If tests fail, the local clone pre-dates the fix.

**Fix**:

```
# Pull the latest code
cd ~/automotive-data-platform-on-aws
git pull

# Re-generate and re-sync charging_sessions data
cd platform-foundation
python source/data-products/charging_sessions/generator.py

ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
aws s3 sync curated/charging_sessions/ \
    s3://adp-staging-foundation-lake-${ACCOUNT}-us-east-1/curated/charging_sessions/ \
    --region us-east-1

# Re-run integrity tests
pytest tests/test_referential_integrity.py -v
```

## Optional CMS→ADP Ingest Module Issues

### Glue MERGE job fails with `KMS AccessDenied`

**Symptom**: The `adp-{stage}-foundation-cms-ingest-merge` Glue job fails with `AccessDenied` on `kms:GenerateDataKey` or `s3:GenerateDataKey`.

**Cause**: The Firehose and Glue MERGE roles require KMS grants scoped to the lake bucket’s `bucket_key_enabled=True` encryption-context condition. Stacks deployed before the 2026-05-30 fix may lack these conditions.

**Fix**: Verify the cms-ingest stack was last updated on or after 2026-05-30:

```
aws cloudformation describe-stacks \
    --stack-name "adp-staging-foundation-cms-ingest" \
    --region us-east-1 --no-cli-pager \
    --query 'Stacks[0].LastUpdatedTime' --output text
# Must be >= 2026-05-30
```

If older, redeploy the cms-ingest stack:

```
cd platform-foundation
make deploy-cms-ingest STAGE=staging \
    CMS_TABLE_ARN=arn:aws:dynamodb:us-east-1:<account>:table/cms-prod-vehicle-state
```

### DynamoDB Streams view-type error

**Symptom**: The cms-ingest module is enabled but no records arrive in Firehose (`IncomingRecords` metric stays at 0), and CloudWatch logs show a Streams `view_type` mismatch.

**Cause**: The CMS DynamoDB table’s Streams must be enabled with `StreamViewType = NEW_AND_OLD_IMAGES`. A table with Streams set to `NEW_IMAGE` only (or disabled) will not produce the full record format the Firehose transformer expects.

**Fix**: Re-run the enable-streams helper (coordinate with the CMS operator before toggling, as this resets the shard iterator):

```
cd platform-foundation
source .venv/bin/activate

.venv/bin/python -m source.optional.cms_ingest.enable_streams \
    --table-arn arn:aws:dynamodb:us-east-1:<account>:table/cms-prod-vehicle-state \
    --enable
```

### Parquet files not appearing in S3 after cms-ingest enable

**Symptom**: After enabling the cms-ingest module, no parquet files appear under the `curated/cms-ingest/` or `cms-ingest/` prefix in the lake bucket, even after waiting several minutes.

**Cause**: One or more of the following:

- DynamoDB Streams not enabled with `NEW_AND_OLD_IMAGES` (see previous entry).
- The operator-supplied Lambda transformer is not yet wired — Firehose `IncomingRecords` will be 0.
- Firehose buffer has not yet flushed (60-second / 64 MiB buffer interval).
- Serialization errors are accumulating in the `_errors/` prefix.

**Fix**:

```
ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
STAGE=staging

# 1. Confirm DDB Streams config
.venv/bin/python -m source.optional.cms_ingest.enable_streams \
    --table-arn arn:aws:dynamodb:us-east-1:${ACCOUNT}:table/cms-prod-vehicle-state

# 2. Check Firehose IncomingRecords (wait up to 60s after first DDB write)
aws firehose describe-delivery-stream \
    --delivery-stream-name "adp-${STAGE}-foundation-cms-vehicle-state" \
    --region us-east-1 --no-cli-pager \
    --query 'DeliveryStreamDescription.DeliveryStreamStatus' --output text
# Expected: ACTIVE

# 3. Check for serialization errors in the _errors/ prefix
aws s3 ls s3://adp-${STAGE}-foundation-lake-${ACCOUNT}-us-east-1/cms-ingest/_errors/ \
    --region us-east-1 2>&1
```

## General Debugging

### CloudWatch log scan for runtime errors

Use this pattern after any deploy or enable operation to surface errors before they reach users:

```
STAGE=staging
REGION=us-east-1
START_MS=$(python3 -c "import time; print(int((time.time()-300)*1000))")

# Scan CloudFormation events across all 5 foundation stacks
for stack in adp-${STAGE}-foundation-network \
             adp-${STAGE}-foundation-lake \
             adp-${STAGE}-foundation-datazone \
             adp-${STAGE}-foundation-datazone-projects \
             adp-${STAGE}-foundation-governance; do
    aws cloudformation describe-stack-events \
        --stack-name "$stack" --region "$REGION" --no-cli-pager \
        --query 'StackEvents[?ResourceStatus==`CREATE_FAILED` || ResourceStatus==`UPDATE_FAILED` || ResourceStatus==`ROLLBACK_IN_PROGRESS`].[Timestamp,ResourceStatus,LogicalResourceId,ResourceStatusReason]' \
        --output text
done

# Verify CloudTrail trail is logging
aws cloudtrail get-trail-status \
    --name adp-${STAGE}-foundation-lake-trail \
    --region "$REGION" --no-cli-pager \
    --query 'LatestDeliveryTime' --output text

# Verify lake KMS key is enabled
aws kms describe-key --key-id "alias/adp-${STAGE}-foundation-lake" \
    --region "$REGION" --no-cli-pager \
    --query 'KeyMetadata.[KeyState,Enabled]' --output text
# Expected: ENABLED  True
```

## Getting Support

**AWS Support**:

- Open case in AWS Console.
- Include: stack name, error message, CloudWatch Logs.
- Attach: CloudFormation events output from the scan above.

**Community Support**:

- GitHub Issues: https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws/issues
- AWS re:Post: https://repost.aws/tags/automotive

**Documentation**:

- `docs/DEPLOYMENT.md` — canonical deploy runbook, stage gate, and full troubleshooting reference.
- `docs/cms-ingest-optional-module.md` — CMS→ADP ingest module operator guide.
- `docs/cvx-integration-contract.md` — CVX cross-account KB integration IAM contract.
