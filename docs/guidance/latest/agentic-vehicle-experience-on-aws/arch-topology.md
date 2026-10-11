

# Deployment topology
<a name="arch-topology"></a>

AVX deploys as a single-region application, co-located with CMS, ADP, and Amazon Connect in `us-east-1`. All components — the AgentCore runtimes, the Lambda proxy handlers, the API Gateway, the Cognito user pools, and the CDK-provisioned infrastructure stacks — run in the same region.

## CDK stacks
<a name="arch-topology-stacks"></a>

AVX provisions three CDK stacks per stage:


| Stack | Contents | 
| --- | --- | 
|  `vsa-{stage}-core`  | AgentCore Memory resource, IAM execution roles (scoped to specific Bedrock model ARNs and the specific KB ARN), DynamoDB tables for triage decisions and tenant config, KMS keys for Memory encryption, and the Lambda functions backing the agent tools. | 
|  `vsa-{stage}-triage-classifier`  | The triage classifier Lambda (deterministic rules engine). Deployed separately to allow independent scaling and versioning from the supervisor runtime. | 
|  `vsa-{stage}-api`  | API Gateway REST API, the Lambda proxy handler for the `/assistant/chat` route, the Cognito authorizer, and the WebSocket API for the reasoning feed (the tool-call trace streamed to the web UI reasoning panel). | 

## AgentCore runtime registration
<a name="arch-topology-agentcore"></a>

The two AgentCore runtimes (`vsa_supervisor_bidi_*` and `vsa_supervisor_text_*`) are registered and deployed via the AgentCore CLI (`agentcore configure` and `agentcore deploy`), not directly managed as CloudFormation resources. Runtime names use the logical `vsa_supervisor_*` prefix and a stage qualifier; deployment-specific suffixes generated at registration time are opaque to the operator. The `make deploy-staging` target redeploys both runtimes when both are registered locally in `.bedrock_agentcore.yaml`.

## Cross-account and cross-region data access
<a name="arch-topology-cross-account"></a>

In the current staging topology, AVX and ADP share the same AWS account but deploy to different regions: AVX in `us-east-1` and ADP in `us-east-1` (co-located in the reference deploy). Customer deployments typically place ADP and AVX in separate AWS accounts, with cross-account Lake Formation v4 grants authorizing the AVX AgentCore execution role to query ADP Glue databases, and a Bedrock KB resource policy authorizing the AVX role to call Bedrock Retrieve against the ADP Knowledge Base. These boundaries are parameterized via CDK context (`adpAccountId` on the AVX side; `cvxKbPrincipals` on the ADP side) so the same CDK code supports both same-account and cross-account topologies.

Amazon Nova 2 Sonic for voice is available in select Regions, including `us-west-2`. Deploy AVX in a Region where Nova 2 Sonic is available so the bidirectional stream stays in-Region. In a Region without Nova 2 Sonic, use Amazon Transcribe (speech-to-text) with Amazon Polly (text-to-speech) for voice; the supervisor handler defines that route as an alternative to the default.