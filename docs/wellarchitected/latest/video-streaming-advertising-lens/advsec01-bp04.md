

# ADVSEC01-BP04 Implement least privilege access to protect programmatic workloads

 Ad tech systems process data across organizational boundaries where advertisers, publishers, agencies, and measurement vendors each require different access scopes. Without authorization policies that reflect advertising-specific data boundaries, authenticated users can access campaign data, audience segments, or financial information outside their business relationship. 

 **Desired outcome:** 
+  You have authorization policies scoped to advertising-specific boundaries: per-campaign, per-advertiser, per-publisher, and per-data-type access controls. 
+  Your agentic AI workloads (campaign optimization agents, creative agents, and measurement agents) operate with minimal permissions scoped to their specific function. 
+  You have standardized identity alignment across coupled ad-tech systems so authorization decisions are consistent regardless of which component processes the request. 

 **Common anti-patterns:** 
+  Granting broad read access to all campaign data when a partner only needs performance metrics for their specific campaigns. 
+  Deploying AI agents with the same permissions as human administrators, so agents can reach audience data, creative assets, and financial records without limit. 
+  Using a single service account for all inter-system communication between DSP, data clean rooms, measurement pipelines, and delivery engines. 

 **Benefits of establishing this best practice:** 
+  Reduces the risk of advertiser A accessing advertiser B's campaign performance data or audience segments within a shared environment. 
+  Limits the scope of compromised AI agent credentials to a single function rather than the entire advertising data estate. 
+  Enables auditable, per-party data access that supports regulatory adherence and contractual data handling obligations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising platforms operate as multitenant environments where competing advertisers share infrastructure. The authorization model must enforce data isolation between tenants (advertisers and agencies) while enabling controlled collaboration where business relationships require it (publisher-advertiser measurement and agency-client reporting). 

 Attribute-based access control fits advertising platforms better than role-based access control, because the entities that need isolation (advertisers, campaigns, and data classifications) change frequently and have variable lifespans. In RBAC, adding a new advertiser requires creating new roles, policies, and group memberships. In ABAC, the same policy set works for any advertiser because isolation is enforced through resource tags matched against session tags on the requesting principal. A system serving 10,000 advertisers with RBAC needs 10,000 or more policy configurations. With ABAC, it needs one policy template and consistent tagging. 

 Without continuous authorization monitoring, permission drift accumulates unnoticed as campaigns end and partner relationships change. A role granted temporary broad access for a campaign launch retains that access indefinitely unless revoked. Stale permissions are the most common finding in advertising system security audits because the business often changes faster than people can perform access reviews. Scope expands gradually, until a former partner's service account can still read audience data months after contract termination. 

 Agentic workloads in advertising (campaign optimization agents, creative generation agents, and bid strategy agents) require least privilege scoping across multiple components, such as: 
+  Framework access 
+  Tooling access 
+  Code execution capabilities 
+  Agent memory (short and long term) 
+  LLM access 
+  Traces 
+  Execution logs 
+  Prompt logs 
+  RAG data access 
+  Unstructured data access 

 Each component must receive the requester identity when it processes a request and constrain its behavior based on that identity and authorization. 

 Authorization for agentic identities must use short-lived credential mechanisms such as OAuth 2.0/2.1 and AWS STS. Secure machine-to-machine communications with mutual TLS and hardware-backed key storage (HSMs). Grant each agent minimal permissions, scope API keys tightly, and enforce micro-segmentation so the agent can only interact with explicitly authorized data sources and actions. 

 Standardize user and audience identifiers across coupled ad-tech systems including DSPs, data clean rooms, measurement pipelines, and delivery engines, so authorization decisions stay consistent across system boundaries. 

 For collaboration between independent parties with competing interests, use clean rooms with cryptographic isolation and query restrictions so each party can verify the other cannot extract raw data. For multitenant access within a single organization, use row-level security with tag-based conditions, where the system operator mediates access. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define advertising-specific permission boundaries:** Create IAM permission boundaries scoped to advertising data domains (campaign data, audience segments, financial and billing, and creative assets). Apply boundaries to all roles accessing the advertising platform to limit cross-domain escalation. 

1.  **Implement tenant isolation for multi-advertiser platforms:** Use IAM conditions with advertiser and campaign tags to enforce per-tenant data isolation. Configure S3 bucket policies, DynamoDB conditions, and Amazon Redshift row-level security to restrict data access to the owning advertiser's records. 

1.  **Scope agentic workload permissions to specific functions:** Create dedicated IAM roles per agent type (bid optimization agent, creative agent, and measurement agent). Each role should have access only to the data and APIs required for its specific function. Use [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) for credential management and [AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) for agent-to-tool interaction controls. 

1.  **Configure cross-party access rules in AWS Clean Rooms:** Define collaboration-level analysis rules that enforce what queries each party can run, minimum aggregation thresholds, and which columns are accessible. This reduces the risk of any single party extracting individual-level data from collaborative datasets. 

1.  **Implement continuous authorization monitoring:** Use IAM Access Analyzer to regularly monitor for unintended access grants. Configure CloudTrail for all authorization decisions. Set up alerts for permission changes that broaden access beyond defined advertising-specific boundaries. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC01-BP01 Implement user authentication and access control to protect bidding process and content](advsec01-bp01.md) 
+  [ADVSEC01-BP05 Implement cross-platform identity governance for converged linear and digital operations](advsec01-bp05.md) 
+  [ADVSEC02-BP03 Implement secure data collaboration with least privileged access and privacy controls](advsec02-bp03.md) 

 **Related documents:** 
+  [Amazon Cognito - Using role-based access control](https://docs.aws.amazon.com/cognito/latest/developerguide/role-based-access-control.html) 
+  [AWS IAM - Attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) 
+  [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) 
+  [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) 
+  [GENSEC01-BP01 Grant least privilege access to foundation model endpoints](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec01-bp01.html) 
+  [Security for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/introduction.html) 
+  [OWASP MAESTRO Threat Modeling for agentic AI](https://agentic-threat-modeling.github.io/MAESTRO/) 
+  [IAB Agentic Real Time Framework (ARTF)](https://iabtechlab.com/standards/artf/) 

 **Related services:** 
+  [AWS Identity and Access Management](https://aws.amazon.com/iam/) 
+  [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) 
+  [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 