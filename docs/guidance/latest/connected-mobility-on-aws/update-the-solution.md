

# Update the guidance
<a name="update-the-solution"></a>

This chapter describes how to update a previously deployed instance of the Guidance for Connected Mobility on AWS. Choose the appropriate update path based on the scope of changes you are applying.

**Note**  
For complete, authoritative deploy commands and environment variable requirements, see the project `docs/DEPLOYMENT.md` file in the source repository.

## Update paths overview
<a name="update-paths-overview"></a>

The guidance supports five distinct update paths. Selecting the correct path avoids unnecessary redeployment of unaffected stacks and reduces update time.


| Update type | Scope | Approximate time | 
| --- | --- | --- | 
|  [UI assets only](#update-ui-only)  | React frontend bundle; no infrastructure changes | 2-5 min | 
|  [Backend Lambda or CDK changes](#update-backend-lambda-cdk)  | Lambda functions, stack parameters, or CDK constructs | 15-45 min | 
|  [Flink streaming processor](#update-flink-processor)  | Kinesis Data Analytics Apache Flink application code or configuration | 5-15 min | 
|  [Bedrock agents](#update-bedrock-agents)  | Agent definitions, knowledge base, or Bedrock stack configuration | 10-20 min | 
|  [Cross-major-version upgrade](#update-cross-major-version)  | Breaking changes between major guidance versions | 45-65 min (full redeploy) | 

## Update 1 - UI assets only
<a name="update-ui-only"></a>

Use this path when your changes are limited to frontend source files under `modules/cms_ui/source/frontend/src/` — for example, label edits, component layout changes, or static content updates — and no infrastructure constructs have changed.

This path skips the CDK synthesis and CloudFormation change-set cycle. It performs a Yarn production build, syncs the output to the AWS S3 frontend bucket, and creates an Amazon CloudFront invalidation.

 **Pre-conditions (all must be true):** 
+ Only files under `modules/cms_ui/source/frontend/src/` were modified.
+  `npx tsc --noEmit` produces no new TypeScript errors.
+ No `runtimeConfig` inputs changed. If they did, run `make regenerate-runtime-config` first and use the [backend/CDK update path](#update-backend-lambda-cdk) instead.
+ The change is already committed to the working branch.

 **Deploy command:** 

```
make ui-quick-deploy DEPLOYMENT_STAGE=staging
```

Run from the `deployment/` directory, or pass `-C deployment` from the repository root:

```
make -C deployment ui-quick-deploy DEPLOYMENT_STAGE=staging
```

 **Expected outcome:** 

The command performs a Yarn production build, uploads all changed assets to the S3 frontend bucket, and creates a CloudFront invalidation. CloudFront edge propagation takes 60-120 seconds after the invalidation is created. The terminal output ends with an invalidation ID confirming success.

 **Do not use this path if:** 
+ CDK constructs changed (authentication, S3 bucket policies, Lambda functions, or CloudFront distribution configuration). Use the [backend/CDK update path](#update-backend-lambda-cdk) instead.
+ The change is security-relevant (authorization rules, CORS policy, Content Security Policy headers).

## Update 2 - Backend Lambda or CDK changes
<a name="update-backend-lambda-cdk"></a>

Use this path when Lambda function code, CDK stack constructs, environment variables, IAM policies, or any CloudFormation-managed resource has changed.

 **Full staging redeploy:** 

```
export CMS_DEMO_DEFAULT_PASSWORD='your-staging-password'
make -C deployment staging-deploy
```

This runs preflight checks, synthesizes all CDK stacks, and deploys only the stacks with pending changes. Total time is 15-45 minutes depending on which stacks changed.

 **Deploy a single stack (faster iteration):** 

```
DEPLOYMENT_STAGE=staging \
AWS_REGION=us-west-2 \
CMS_DEMO_DEFAULT_PASSWORD='your-staging-password' \
cdk deploy cms-staging-<stack-name> \
  --require-approval never \
  --profile default
```

Replace `<stack-name>` with the stack you changed, for example `cms-staging-ui`, `cms-staging-storage`, or `cms-staging-commands`.

 **Pre-deployment checks:** 

Always run the preflight script before a full redeploy. It verifies AWS credentials, CDK bootstrap state, Bedrock model availability, and required environment variables in approximately 30 seconds:

```
bash deployment/scripts/preflight-staging.sh
```

 **Expected outcome:** 

All modified CloudFormation stacks reach `UPDATE_COMPLETE` state. Check the AWS CloudFormation console if a stack fails; the stack events surface the specific resource and error message.

 **Post-deploy validation:** 

After the deploy completes, run the publish-gate validator to confirm the environment is healthy before sharing it or cutting a release tag:

```
AWS_PROFILE=default AWS_REGION=us-west-2 DEPLOYMENT_STAGE=staging \
  bash deployment/scripts/validate_staging_publish_gate.sh
```

## Update 3 - Flink streaming processor
<a name="update-flink-processor"></a>

The guidance uses Kinesis Data Analytics for Apache Flink for real-time telemetry processing. Flink application updates require a snapshot stop-and-restart cycle. Two options are available.

 **Option A - Fast deploy (skip snapshot, \~5 minutes):** 

Use when the Flink application state schema has not changed and it is acceptable to resume processing from the latest checkpoint rather than a clean snapshot.

```
make -C deployment deploy-flink-fast \
  DEPLOYMENT_STAGE=staging \
  AWS_REGION=us-west-2
```

 **Option B - Full rebuild (\~10-15 minutes):** 

Use when the Flink application JAR, state schema, or CDK stack configuration has changed, or when you want a clean snapshot before transitioning to the new application version.

```
make -C deployment staging-deploy
```

This redeploys all stacks with pending changes, including the Flink stack with the updated JAR and configuration.

 **Post-update smoke check:** 

After either option, verify that all Flink applications return to `RUNNING` state:

```
AWS_PROFILE=default AWS_REGION=us-west-2 DEPLOYMENT_STAGE=staging \
  bash deployment/scripts/validate_staging_publish_gate.sh
```

The publish-gate validator checks that every `cms-{stage}-flink-*` Kinesis Analytics application is in the `RUNNING` state (check 2 of 7).

**Note**  
The FWE decoder manifest is managed by the Flink CDK stack. To regenerate it: run `DRY_RUN=1 python3 deployment/scripts/generate_decoder_manifest.py` to validate, then remove `DRY_RUN=1` to write the updated `deployment/fwe-config/DecoderManifest.bin`, commit the file, and redeploy the Flink stack. Do not upload the manifest manually — that causes bucket drift.

## Update 4 - Bedrock agents
<a name="update-bedrock-agents"></a>

The `cms-{stage}-bedrock-agents` stack is deployed independently and is not included in the `deploy-all` target. Use the dedicated target when updating agent definitions, knowledge base configuration, or the Bedrock model identifier.

```
make -C deployment deploy-bedrock-agents \
  DEPLOYMENT_STAGE=staging \
  AWS_REGION=us-west-2
```

 **Bedrock model identifier validation:** 

Before deploying, the Makefile automatically validates the configured Bedrock model identifier against the live AWS Bedrock catalog. If the model is not available or has been deprecated, the deploy aborts with a clear error. To run the validation separately:

```
make -C deployment validate-bedrock-model \
  BEDROCK_AGENT_MODEL=us.anthropic.claude-sonnet-4-6 \
  AWS_REGION=us-west-2 \
  AWS_PROFILE=default
```

 **Expected outcome:** 

The `cms-{stage}-bedrock-agents` CloudFormation stack reaches `UPDATE_COMPLETE` state. The Bedrock agent aliases are updated and the knowledge base remains attached.

**Note**  
The Bedrock agents stack is independent of the other guidance stacks. You can update it without redeploying the data-processing, storage, or Flink stacks.

## Update 5 - Cross-major-version upgrade
<a name="update-cross-major-version"></a>

Major guidance versions introduce breaking infrastructure changes such as renamed stacks, changed DynamoDB table schemas, or replacement of core resources. There is no in-place upgrade path between major versions.

The safe update path is to [uninstall the existing deployment](uninstall-the-solution.md) and then [deploy the new version](deploy-the-solution.md) from a clean state.

 **Recommended procedure:** 

1. Back up any data you need to preserve. DynamoDB tables, S3 objects, and Cognito user pools are deleted during teardown.

1. Run the uninstall procedure described in [Uninstall the guidance](uninstall-the-solution.md).

1. Follow the deployment procedure in [Deploy the guidance](deploy-the-solution.md) using the new version of the source repository.

**Warning**  
Teardown deletes all DynamoDB tables, the MSK cluster, Cognito user pools, and all associated data permanently. Export or back up any data you require before running the uninstall procedure.