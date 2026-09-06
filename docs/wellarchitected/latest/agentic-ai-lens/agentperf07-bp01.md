

# AGENTPERF07-BP01 Design efficient multitenant agent deployment models
<a name="agentperf07-bp01"></a>

 Organizations that serve multiple tenants from a shared agent service get better resource efficiency and faster tenant onboarding when the deployment model delivers consistent performance for every tenant. Siloed deployments provide strong isolation at higher cost. Pooled deployments maximize efficiency but need mechanisms to help prevent noisy neighbor effects. Hybrid models combine both, using pooled resources for standard tenants and dedicated resources for premium tenants. 

 **Desired outcome:** 
+  You have multitenant agent deployments that use deployment models matched to tenant requirements. 
+  You have deployment models documented with clear performance characteristics and SLA commitments for each tier. 
+  You have a deployment model that supports efficient tenant onboarding through configuration rather than infrastructure provisioning. 

 **Common anti-patterns:** 
+  Deploying fully siloed infrastructure for every tenant regardless of their performance requirements, creating resource waste for tenants that would be well-served by pooled resources. 
+  Using a single pooled deployment without isolation mechanisms, allowing high-volume tenants to consume disproportionate resources and degrade performance for others. 
+  Skipping tenant tiers with different performance SLAs, treating all tenants identically regardless of business value. 

 **Benefits of establishing this best practice:** 
+  Resource investment stays proportional to tenant value and performance requirements. 
+  Appropriate isolation mechanisms deliver consistent performance for every tenant. 
+  Configuration-driven provisioning speeds tenant onboarding. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Define tenant tiers based on performance requirements and business value: 
+  A standard tier using pooled resources with best-effort performance 
+  A premium tier using dedicated resources with stronger SLA targets 
+  (Optional) An enterprise tier with fully isolated infrastructure 

 For pooled deployments, [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) provides session-isolated execution that naturally helps prevent cross-tenant interference at the agent execution level. For tenants that need custom container environments, deploy on [Amazon EKS](https://aws.amazon.com/eks/) or [Amazon ECS](https://aws.amazon.com/ecs/) with namespace-level or task-level isolation. For simpler tenant needs such as team-specific chat assistants or enterprise Q&A, [Amazon Quick Suite](https://aws.amazon.com/quicksuite/) provides a managed no-code option where business users create and deploy agents without custom infrastructure. 

 Tenant-aware routing at the API layer uses [Amazon API Gateway](https://aws.amazon.com/api-gateway/) with usage plans that enforce per-tenant rate limits and throttling. At the inference layer, Amazon Bedrock's provisioned throughput gives premium tenants reserved capacity while standard tenants use on-demand capacity. Tenant context propagates through the agent stack so every component (runtime, memory, tools) applies tenant-specific configurations. For data isolation, use [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with tenant partition keys for pooled access, or separate tables for siloed tenants. Tenant onboarding automated through [AWS CDK](https://aws.amazon.com/cdk/) or CloudFormation makes new standard tenants a configuration change rather than an infrastructure provisioning project. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define tenant tiers with specific performance SLAs, isolation requirements, and pricing:** Define standard, premium, and optional enterprise tiers with explicit SLAs and isolation expectations. 

1.  **Design the deployment architecture for each tier:** Architect pooled (shared AgentCore Runtime, on-demand Amazon Bedrock), premium (dedicated resources, provisioned throughput), and enterprise (fully isolated) deployments. 

1.  **Implement tenant-aware routing using API Gateway with per-tenant usage plans and rate limits:** Use [Amazon API Gateway](https://aws.amazon.com/api-gateway/) usage plans with per-tenant rate and burst limits. 

1.  **Configure data isolation using DynamoDB tenant partition keys (pooled) or separate tables (siloed):** Enforce data isolation at the data layer with partition keys or separate tables as appropriate for the tier. 

1.  **Automate tenant onboarding for each tier using CDK/CloudFormation templates:** Template onboarding so new tenants are provisioned through configuration rather than manual infrastructure work. 

1.  **Monitor per-tenant performance metrics to validate SLA compliance:** Publish per-tenant metrics to CloudWatch and alert when observed performance drifts outside SLA. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF07-BP02 Implement tenant-aware performance isolation and throttling](agentperf07-bp02.html) 
+  [AGENTPERF02-BP01 Design efficient reasoning pipelines](agentperf02-bp01.html) 

 **Related documents:** 
+  [Building multi-tenant architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/introduction.html) 
+  [Enforcing tenant isolation, Multi-tenant agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/enforcing-tenant-isolation.html) 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 

 **Related videos:** 
+  [Building multi-tenant SaaS agents with AgentCore (SAS407)](https://www.youtube.com/watch?v=uwXrtyXXuy8) 
+  [Transforming from SaaS to multi-tenant agentic SaaS (SAS304)](https://www.youtube.com/watch?v=YOQlbZojPB4) 
+  [Deploy Production-Ready Agents in 22 Minutes with AgentCore Runtime](https://www.youtube.com/watch?v=Q-tYIAuv9WI) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon EKS](https://aws.amazon.com/eks/) 
+  [AWS CDK](https://aws.amazon.com/cdk/) 