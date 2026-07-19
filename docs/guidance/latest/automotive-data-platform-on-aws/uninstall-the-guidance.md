# Uninstall the guidance

This chapter describes how to completely remove the Automotive Data Platform foundation from your AWS account.

###### Warning

Uninstalling the solution will permanently delete all data, configurations, and resources. This action cannot be undone. Ensure you have backups of any data you wish to retain.

## Overview

The foundation uses a **per-stage** teardown model. Each stage (`staging`, `prod`) is torn down independently. The account-level bootstrap stack (`adp-shared-bootstrap`) is **not** torn down by per-stage teardown — it is shared across stages and retained.

The Makefile target `make teardown STAGE=<stage> YES=1` is the only sanctioned entry point. Running the target without `YES=1` performs a safe **dry-run** that prints what would be deleted without destroying anything.

###### Important

The `adp-shared-bootstrap` stack (which enables the Macie session) is intentionally excluded from per-stage teardown. It is retained across stage lifecycles. If you must disable it, note that Macie has a **30-day cool-down period** before it can be re-enabled after being disabled.

## Pre-teardown: Vehicle Knowledge Base

If the optional Vehicle Knowledge Base stack (`adp-<stage>-foundation-vehicle-knowledge-base`) is deployed, you must stop any in-flight Bedrock ingestion jobs **before** running teardown. Deleting the Knowledge Base while an ingestion job is running will cause deletion conflicts.

```
# List all ingestion jobs for the Knowledge Base.
# Replace <kb-id> with your Knowledge Base ID (from the stack's KnowledgeBaseId output).
DS_ID=$(aws bedrock-agent list-data-sources \
  --knowledge-base-id <kb-id> \
  --region us-east-1 \
  --query 'dataSourceSummaries[?name==`vehicle-knowledge-base-sources`].dataSourceId' \
  --output text)

aws bedrock-agent list-ingestion-jobs \
  --knowledge-base-id <kb-id> \
  --region us-east-1

# Stop any job with status IN_PROGRESS (replace <JOB_ID> with the actual ingestion job ID).
aws bedrock-agent stop-ingestion-job \
  --knowledge-base-id <kb-id> \
  --data-source-id $DS_ID \
  --ingestion-job-id <JOB_ID> \
  --region us-east-1 || true
```

For the full Vehicle Knowledge Base teardown procedure, see `docs/DEPLOYMENT.md` § Vehicle Knowledge Base (Bedrock KB + AOSS) deploy — Tear-down.

## Teardown command

All teardown commands run from the `platform-foundation/` directory.

```
cd platform-foundation

# Dry-run — prints what WOULD be deleted (default, safe).
make teardown STAGE=staging

# Actually destroy the staging stage.
make teardown STAGE=staging YES=1

# Same for prod:
make teardown STAGE=prod YES=1
```

## Six-step teardown sequence

The `make teardown STAGE=<stage> YES=1` command executes the following six steps in order. Each step is automated by the teardown script (`scripts/teardown.sh`).

### Step 1: Stop the CloudTrail trail

The stage CloudTrail trail is stopped gracefully before S3 buckets are emptied, to prevent log delivery attempts into a bucket that is about to be deleted.

### Step 2: Empty S3 buckets

All three S3 buckets for the stage are emptied — current objects, every object version, and every delete marker. Versioned buckets cannot be deleted by CloudFormation without first being emptied.

Buckets emptied:

- `adp-<stage>-foundation-lake-<account>-us-east-1` — the data lake bucket
- Lake-logs bucket
- Trail-logs bucket

### Step 3: DataZone domain force-delete

The DataZone domain is deleted via `aws datazone delete-domain --skip-deletion-check`. This cascades through the 10 retained `CfnProject` resources that would otherwise block the CloudFormation stack deletion.

### Step 4: CDK destroy with explicit stack list

CloudFormation stacks are destroyed using `cdk destroy --force -c stage=<stage>` with an **explicit stack list**. The script never uses `--all`, which would walk into `adp-shared-bootstrap`.

Stacks destroyed (in order):

- `adp-<stage>-foundation-governance`
- `adp-<stage>-foundation-datazone-projects`
- `adp-<stage>-foundation-datazone`
- `adp-<stage>-foundation-lake`
- `adp-<stage>-foundation-network`
- `adp-<stage>-foundation-vehicle-knowledge-base` (if deployed)
- `adp-<stage>-foundation-cms-ingest` (if deployed)

The `adp-shared-bootstrap` stack is **never** included in this list.

### Step 5: IDC group cleanup

An idempotent IAM Identity Center (IDC) group cleanup removes the three stage-prefixed groups (`adp-<stage>-{data-owners,data-consumers,platform-admins}`). This is a fallback step — some CDK and CloudFormation versions do not honor `RemovalPolicy.DESTROY` on `CfnGroup` resources.

### Step 6: Verify

The teardown script verifies that:

- No `adp-<stage>-foundation-*` stacks remain in `CREATE_COMPLETE` or `UPDATE_COMPLETE` state.
- The `adp-shared-bootstrap` stack is still `CREATE_COMPLETE` or `UPDATE_COMPLETE` — the Macie session is preserved.

## Bootstrap stack retention

The `adp-shared-bootstrap` stack is explicitly **excluded** from per-stage teardown. This stack manages the Macie session, which has a 30-day cool-down period before it can be re-enabled after being disabled. Because of this constraint, the bootstrap sets `RemovalPolicy.RETAIN` on the Macie session resource.

###### Important

Per-stage teardown does **not** touch the `adp-shared-bootstrap` stack. The Macie session remains `ENABLED` after a stage is torn down. If you need to remove the bootstrap stack entirely (for example, to decommission the account-level deployment), be aware of the 30-day cool-down before Macie can be re-enabled.

## Verify teardown

After `make teardown STAGE=<stage> YES=1` completes, run the following verification commands to confirm the stage is fully removed and the bootstrap is intact.

```
STAGE=staging   # or prod

# All stage stacks should be absent or DELETE_COMPLETE.
aws cloudformation list-stacks \
    --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE \
    --region us-east-1 \
    --query "StackSummaries[?starts_with(StackName, \`adp-${STAGE}-foundation-\`)].StackName" \
    --output text
# MUST be empty

# Lake bucket must be gone.
aws s3 ls s3://adp-${STAGE}-foundation-lake-<account>-us-east-1/ 2>&1 | head -1
# MUST report NoSuchBucket

# Stage IDC groups must be gone.
aws identitystore list-groups --identity-store-id <idc-store-id> --region us-east-1 \
    --query "Groups[?starts_with(DisplayName, \`adp-${STAGE}-\`)].DisplayName" --output text
# MUST be empty

# Bootstrap stack must be untouched.
aws cloudformation describe-stacks --stack-name adp-shared-bootstrap --region us-east-1 \
    --query 'Stacks[0].StackStatus' --output text
# MUST return CREATE_COMPLETE or UPDATE_COMPLETE — Macie session preserved.
```

Replace `<account>` with your 12-digit AWS account ID (obtain it via `aws sts get-caller-identity --query Account --output text`) and `<idc-store-id>` with your IAM Identity Center IdentityStore ID.

## Re-deployment after teardown

To re-deploy after teardown, follow the standard deployment procedure from the Deploy the Solution chapters. The bootstrap step can be skipped if `adp-shared-bootstrap` is still present.

```
cd platform-foundation

# Bootstrap is a no-op if adp-shared-bootstrap already exists.
make bootstrap

# Re-deploy the stage.
make deploy STAGE=staging

# Re-seed data products (once available).
make seed STAGE=staging

# Validate the deployment.
make smoke-test STAGE=staging
```

New CloudFormation stack IDs, DataZone project IDs, and IDC group IDs are issued on re-deployment. The lake KMS CMK is retained (bound to the deterministic alias `alias/adp-<stage>-foundation-lake`) and reused on the next deploy.

## Cost after uninstall

After teardown, you may still incur charges for:

- The `adp-shared-bootstrap` Macie session (retained by design — ~$0/month at idle if no classification jobs are running)
- CloudWatch Logs retention for any log groups not explicitly deleted
- CloudTrail logs that landed in S3 before the trail was stopped
- The lake KMS CMK (retained per `RemovalPolicy.RETAIN`)

To eliminate ongoing costs, verify the lake bucket is gone, delete any remaining CloudWatch log groups for the stage, and remove residual S3 objects in the trail-logs bucket if it was not fully emptied.
