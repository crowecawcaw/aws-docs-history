

# Step 3: Build and deploy the AVX CDK infrastructure
<a name="deploy-step3-cdk-infrastructure"></a>

## Build Lambda assets
<a name="build-lambda-assets"></a>

Three Lambda functions bundle their dependencies at build time. Run the build scripts before the first deploy and after any Lambda dependency change:

```
scripts/build-triage-classifier.sh
scripts/build-api-ws-authorizer.sh
scripts/build-api-vehicle-live-state.sh
```

Each script packages the Lambda source directory with its dependencies into the expected CDK asset path.

## Deploy for staging
<a name="deploy-for-staging"></a>

AVX deploys one environment, staging. All commands in this chapter target staging. Producing a second environment is left to the operator as a customization — the same CDK stacks, Makefile targets, and IAM patterns apply, but the AgentCore Runtime allow-list requires the execution role name `AmazonBedrockAgentCoreSDKRuntime-{region}-vsa-{stage}` be present in the target account before the runtime deploy succeeds.

Staging deploys to us-west-2. The `deploy-staging` Makefile target requires `VSA_ADP_KB_ID` to tighten the cross-account IAM grant to the specific ADP Knowledge Base ARN:

```
source .env
VSA_ADP_KB_ID=<adp-kb-id> make deploy-staging
```

The `deploy-staging` target runs a pre-flight check (AWS credentials, `agentcore` CLI presence, KB ID format validation), then:

1. Deploys all AVX CDK stacks to us-west-2 with the KB ID threaded as CDK context.

1. Patches `.bedrock_agentcore.yaml` with the CDK stack outputs (execution role ARN, S3 bucket path).

1. Deploys the AgentCore voice runtime (`vsa_supervisor_bidi_<stage>`).

1. If the text runtime (`vsa_supervisor_text_<stage>`) is registered locally, deploys it too — this runtime powers the CMS Fleet Intelligence portal’s `/assistant/chat` route.

1. Seeds all demo personas and tenant records.

## A note on production
<a name="a-note-on-production"></a>

The guidance deploys staging and has no `deploy-prod` target. To add a production environment, deploy the same stacks under a second stage name, as described below.

## CDK stack deploy order
<a name="cdk-stack-deploy-order"></a>

CDK resolves inter-stack dependencies automatically. The logical order is:

1.  `vsa-<stage>-foundation` — AgentCore Memory resource and KMS CMK (created once per environment).

1.  `vsa-<stage>-analytics` — Athena workgroup and results bucket for cross-region ADP Glue catalog queries (deployed to us-east-1 even in a us-west-2 staging environment).

1.  `vsa-<stage>-core` — DynamoDB tables (`vsa-<stage>-tenants`, `vsa-<stage>-actions`, `vsa-<stage>-triage-decisions`), Cognito user pool, AgentCore execution role with all IAM grants.

1.  `vsa-<stage>-triage-classifier` — the DTC triage classifier Lambda.

1.  `vsa-<stage>-api` — API Gateway REST and WebSocket APIs, all Lambda handlers including the `/assistant/chat` route for the CMS Fleet Intelligence portal.

To verify the stacks are healthy after deploy:

```
aws cloudformation describe-stacks \
  --region <region> \
  --query 'Stacks[?starts_with(StackName, `vsa-`)].{Name:StackName,Status:StackStatus}' \
  --output table
```

All stacks should be in `CREATE_COMPLETE` or `UPDATE_COMPLETE`.