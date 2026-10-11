

# Wiring a new AVX deployment to existing CMS and ADP
<a name="bca-wiring"></a>

This section gives the prescriptive sequence for connecting a new AVX deployment to CMS and ADP foundations that are already deployed. Follow this sequence in order — each step depends on outputs from the prior step.

## Prerequisites
<a name="bca-prereqs"></a>

Before running any AVX deploy command, confirm all of the following:


| Prerequisite | What to verify | 
| --- | --- | 
| CMS deployed and healthy |  `aws cloudformation describe-stacks --stack-name cms-<stage>-storage` returns `CREATE_COMPLETE` or `UPDATE_COMPLETE`. The DynamoDB tables, Redis cluster, and KMS key must exist and be in a healthy state. | 
| CMS output values captured | The following CMS outputs must be in your AVX `.env` file: `CMS_VEHICLES_TABLE`, `CMS_TRIPS_TABLE`, `CMS_SERVICE_HISTORY_TABLE`, `CMS_REDIS_HOST`, `CMS_REDIS_PORT`, `CMS_KMS_KEY_ARN`, `CMS_COGNITO_USER_POOL_ID`, `CMS_VPC_ID`, `CMS_REDIS_SECURITY_GROUP_ID`. | 
| ADP deployed and healthy |  `aws cloudformation describe-stacks --stack-name adp-<stage>-knowledge-base` returns `CREATE_COMPLETE`. The ADP Glue catalog databases and the Bedrock Knowledge Base must exist. | 
| ADP Knowledge Base ID captured | The ADP Knowledge Base ID (`ADP_KB_ID`) must be available. Find it in the ADP stack’s CloudFormation outputs or via `aws bedrock-agent list-knowledge-bases --query 'knowledgeBases[?name contains `adp-<stage>`].knowledgeBaseId'`. | 
| ADP cross-account grants provisioned | The ADP CDK stacks must have been deployed with the AVX account ID in `cvxAccountId` and the AVX IAM role ARNs in `cvxKbPrincipals`. If deploying ADP and AVX simultaneously, deploy ADP first, then AVX. | 
| Bedrock model access enabled | In the AVX account and region, Claude Sonnet and Nova 2 Sonic v2 must be enabled in the Bedrock console under Model access. AgentCore will fail to start if the execution role cannot invoke these models. | 
| AgentCore execution role name matches pattern | The AgentCore execution role must be named `AmazonBedrockAgentCoreSDKRuntime-<region>-<stage>`. This name is required by the Bedrock AgentCore service for Nova 2 Sonic access. The AVX CDK stacks create this role with the correct name; verify it exists before deploying the AgentCore runtime. | 

## Deployment sequence
<a name="bca-deploy-sequence"></a>

1.  **Deploy CMS** (if not already deployed). Follow the CMS DEPLOYMENT.md. Wait for all CMS stacks to reach `CREATE_COMPLETE` before proceeding.

1.  **Deploy ADP** with AVX account context. From the ADP repo:

   ```
   cdk deploy --all \
     --context cvxAccountId=<cvx-account-id> \
     --context cvxKbPrincipals=<cvx-agentcore-role-arn>,<cvx-supervisor-lambda-role-arn>
   ```

   This provisions the Lake Formation cross-account grants and the Bedrock KB resource policy. If the AVX role ARNs are not yet known (first deploy), deploy the AVX CDK infrastructure first (step 3), capture the role ARNs from its stack outputs, then re-deploy ADP with those ARNs.

1.  **Deploy AVX CDK infrastructure**. From the AVX repo:

   ```
   source .env  # loads CMS table names, Redis endpoint, KMS ARN, Cognito pool ID
   cdk deploy --all \
     --context adpAccountId=<adp-account-id> \
     --context adpKbId=<adp-kb-id> \
     --context adpRegion=<adp-region>
   ```

   Stacks deployed: `vsa-core-stack`, `vsa-api-stack`, `triage-classifier-stack`, and one tenant pool stack per configured tenant. CDK resolves the inter-stack dependencies automatically.

1.  **Configure the AgentCore runtime**. Run the `agentcore configure` command pointing at the supervisor handler:

   ```
   agentcore configure -e agents/supervisor/agentcore_app.py
   ```

   Review the generated `.bedrock_agentcore.yaml` and confirm the `execution_role_arn` matches the role created by `vsa-core-stack`. Patch `source_path: .` if the tool generates an absolute path — a relative path ensures the deployment bundle is portable.

1.  **Deploy the AgentCore runtimes**. Deploy both the text and bidirectional runtimes:

   ```
   make deploy-staging   # deploys both vsa_supervisor_text_* and vsa_supervisor_bidi_*
   ```

   The `make deploy-staging` target checks whether both runtimes are registered locally and redeploys both. If a runtime is not registered (first deploy of a new stage), the target prints a configure command and exits — run `agentcore configure` for that runtime variant, then re-run `make deploy-staging`.

1.  **Seed tenant configuration**. Each tenant is onboarded by writing a config record to the `vsa-tenant-config` DynamoDB table. The seed script accepts tenant ID, KB IDs, Connect queue ARNs, escalation rules, and booking config:

   ```
   python3 scripts/seed-tenant.py \
     --tenant-id <tenant-id> \
     --kb-id <tenant-kb-id> \
     --connect-queue-arn arn:aws:connect:<region>:<cvx-account-id>:instance/<instance-id>/queue/<queue-id> \
     --booking-sink sqs
   ```

1.  **Validate end-to-end**. Run the smoke test to confirm that the AgentCore runtime can reach both foundations:

   ```
   python3 scripts/smoke-test-kb-retrieve.py --stage <stage>
   ```

   A passing smoke test confirms: (1) the Bedrock KB Retrieve cross-account call resolves and returns chunks; (2) the AgentCore Memory write succeeds; (3) the CMS Redis LKS read returns a valid telemetry snapshot for the seeded test VIN.

## Configuration touchpoints summary
<a name="bca-config-touchpoints"></a>


| Config item | Location | Description | 
| --- | --- | --- | 
|  `adpAccountId`  | AVX CDK context (`-c adpAccountId=…`) | ADP AWS account. Defaults to the AVX account (same-account staging). | 
|  `adpKbId`  | AVX CDK context and `.env`  | ADP Bedrock Knowledge Base ID. Sourced from the ADP stack CloudFormation output. | 
|  `adpRegion`  | AVX CDK context and `.env`  | AWS region where ADP is deployed. Used to construct Athena workgroup and KB ARNs. | 
|  `cvxKbPrincipals`  | ADP CDK context (`-c cvxKbPrincipals=…`) | AVX role ARNs granted KB Retrieve. Comma-separated. Updated when roles change. | 
|  `cvxAccountId`  | ADP CDK context (`-c cvxAccountId=…`) | AVX AWS account. Used in the Lake Formation cross-account share and KB policy. | 
|  `vsa-tenant-config` table | DynamoDB (AVX account) | Per-tenant config: KB IDs, Connect queue ARNs, branding, policy overrides, booking sink. | 
|  `.env`  | AVX repo root (gitignored) | Runtime environment: CMS table names, Redis endpoint, KMS ARN, Cognito pool ID, ADP KB ID, ADP region. | 
|  `.bedrock_agentcore.yaml`  | AVX repo root (gitignored) | AgentCore runtime config: execution role ARN, S3 bucket for deployment artifacts. | 