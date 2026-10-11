

# Overview
<a name="deploy-overview"></a>

1.  **Foundation prerequisites** — CMS and ADP deployed and seeded with their demo data; Amazon Connect instance available.

1.  **AVX infrastructure** — CDK stacks deployed in order, producing Lambda endpoints, DynamoDB tables, Cognito pools, and the AgentCore execution role.

1.  **AgentCore runtime** — the `agentcore` CLI packages the agent source and deploys it as a managed runtime (text-mode HTTP and bidirectional voice via Amazon Nova 2 Sonic).

1.  **Tenant onboarding** — a configuration record in DynamoDB activates the first tenant; no code change is required to add a subsequent tenant.

The guidance deploys one environment, staging (us-west-2). A second environment can be built by mirroring the same sequence — the Makefile encapsulates the region and stage difference so the commands below remain nearly identical; where they diverge, staging-specific notes are called out.