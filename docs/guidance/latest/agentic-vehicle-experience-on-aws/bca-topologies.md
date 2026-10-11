

# Deployment topologies
<a name="bca-topologies"></a>

## Same-account cross-region (current staging)
<a name="bca-staging-topology"></a>

The current staging topology runs both AVX and ADP in the same AWS account, separated by region. AVX components (AgentCore runtime, Memory, API Gateway, supervisor Lambda, Nova 2 Sonic inference) run in one region; ADP components (Glue catalog, Bedrock Knowledge Base, data lake) run in a second region.

This configuration is used for development, integration testing, and staged capability rollout. It exercises the full cross-account authorization code path — Lake Formation cross-account APIs, Bedrock KB resource policy, Athena cross-region queries — without requiring a second AWS account. When `adpAccountId` equals the AVX account ID, the CDK stacks produce same-account trust policies; the API calls are otherwise identical.

**Note**  
Even in the same-account topology, the AVX and ADP stacks are kept in separate CDK apps and deployed independently. This mirrors the governance boundary that applies in a production split-account deployment and ensures that the integration pattern is tested against real cross-stack IAM boundaries, not synthetic shortcuts.

Cross-region Athena queries at session initialization incur a small latency overhead (typically 100–300 ms) relative to a same-region query. This is acceptable for session initialization because it runs once per session, not once per turn. For production deployments with strict latency SLOs, co-locating AVX and ADP in the same region eliminates this overhead while keeping the account separation.

## Split-account (production pattern)
<a name="bca-splitaccount-topology"></a>

In a production customer deployment, AVX and ADP run in separate AWS accounts. The account boundary is the primary governance control: ADP owns its data lake, Glue catalog, and Knowledge Base; AVX holds no copy of the data. Cross-account access is granted on a least-privilege basis (per-database Lake Formation shares, per-KB resource policy) and is fully auditable via CloudTrail data-event logs in the ADP account.

The split-account configuration is activated by setting `adpAccountId` to the ADP account ID in the AVX stack and `cvxAccountId` to the AVX account ID in the ADP stack. No code changes are required relative to the same-account staging configuration.

The Lake Formation cross-account share is provisioned by the ADP CDK stack and takes effect within minutes of the ADP deploy completing. The Bedrock KB resource policy is similarly provisioned by ADP. AVX can begin making cross-account calls as soon as both policies are in effect and the AVX CDK stacks are deployed with the matching context values.

### Multi-tenant production considerations
<a name="bca-multi-tenant-split"></a>

In a deployment serving multiple tenants, each tenant may maintain its own ADP instance (separate account, separate data lake, separate KB) or share a common ADP instance with per-tenant row-level security. The AVX side accommodates both patterns:
+  **Shared ADP instance:** a single `adpAccountId` and `adpKbId` in AVX context; per-tenant isolation is enforced by Lake Formation column-level security and the `tenant_id` metadata filter on AgentCore Memory records.
+  **Per-tenant ADP instance:** the `vsa-tenant-config` DynamoDB table stores a per-tenant `adp_account_id` and `adp_kb_id`; the `persona_loader` selects the correct Athena endpoint and KB ARN at session-init time based on the resolved tenant ID.

The second pattern is the recommended production configuration for regulated or highly-separated tenants. It requires that the AVX AgentCore execution role is granted Lake Formation access and KB Retrieve permission in each tenant’s ADP account, which is managed by updating `cvxKbPrincipals` in each ADP deployment.