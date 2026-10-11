

# Cross-account grounding model
<a name="bca-cross-account"></a>

AVX is architected so that the same code path supports two deployment topologies: a same-account cross-region staging configuration and a full split-account production configuration. The authorization boundaries between AVX and ADP are parameterized; no code changes are required to move between topologies.

## Lake Formation cross-account grants (tabular data)
<a name="bca-lakeformation"></a>

ADP provisions its Glue catalog databases with AWS Lake Formation v4 wildcard cross-account shares. A share grants the AVX AgentCore execution role the `lakeformation:GetDataAccess` permission on the named databases, which in turn allows that role to obtain temporary S3 credentials via the Lake Formation token vending machine and read the underlying Iceberg files in the ADP data lake.

The grant is scoped by database — only the six in-scope ADP databases (vehicle identity, service records, charging sessions, customer 360, customer interactions, OTA campaigns) are shared. The underlying S3 data lake and KMS key remain owned and encrypted by ADP; the agent layer never receives the KMS key, only session-scoped S3 read tokens for the objects it is authorized to read.

On the AVX side, the CDK stack provides the `adpAccountId` context variable. The AgentCore execution role’s trust policy and IAM permission set reference this account ID when constructing the Lake Formation Assume-role chain. Setting `adpAccountId` to the deploying account ID itself configures the same-account cross-region path used in the current staging topology.

## Bedrock KB resource policy (reference data)
<a name="bca-bedrock-kb-policy"></a>

ADP attaches a resource-based policy to the Bedrock Knowledge Base that explicitly authorizes a list of IAM principal ARNs to invoke `bedrock-agent-runtime:Retrieve`. The list is supplied via the `cvxKbPrincipals` CDK context variable on the ADP side.

The authorized principals are the supervisor Lambda execution role and the AgentCore execution role. Both receive `Retrieve` permission scoped to the specific Knowledge Base ARN — no wildcard on the Bedrock service. Cross-account Retrieve calls are signed with SigV4 by the caller’s temporary credentials and validated against the resource policy by the Bedrock service in the ADP account.

CloudTrail data-event logging is enabled on the Bedrock Knowledge Base. Every cross-account Retrieve call — including the caller identity, the query text hash, the filter applied, and the number of chunks returned — is logged in the ADP account’s CloudTrail for compliance audit.

## CDK context parameters
<a name="bca-cdkcontext"></a>

The following CDK context variables are the wiring points between an AVX deployment and its ADP foundation. They are passed at `cdk deploy` time and do not require any code change.


| Variable | Side | Purpose | 
| --- | --- | --- | 
|  `adpAccountId`  | AVX stack | The AWS account ID of the ADP deployment. Used to construct the cross-account IAM trust chain for Lake Formation and the Bedrock KB ARN. Set to the AVX account ID for same-account cross-region deployments. Use the placeholder `<adp-account-id>` in any config templates. | 
|  `cvxAccountId`  | ADP stack | The AWS account ID of the AVX deployment. Added to the Lake Formation cross-account share principal list and referenced in the Bedrock KB resource policy. Use the placeholder `<cvx-account-id>` in any config templates. | 
|  `cvxKbPrincipals`  | ADP stack | Comma-separated list of AVX IAM role ARNs (supervisor Lambda execution role, AgentCore execution role) that are granted `bedrock-agent-runtime:Retrieve` on the ADP Knowledge Base. Must be updated whenever a new AVX role needs KB access. | 

**Note**  
The AVX CDK stacks are authored so that `adpAccountId` defaults to the deploying account when the context variable is absent. This means `cdk deploy` without any context flags produces a same-account cross-region configuration — suitable for staging — and an explicit `adpAccountId=<adp-account-id>` context flag switches to split-account production without any template modification.