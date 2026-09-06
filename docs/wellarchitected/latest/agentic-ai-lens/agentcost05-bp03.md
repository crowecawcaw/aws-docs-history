

# AGENTCOST05-BP03 Design tenant-aware cost allocation for agent as a service (AaaS) pricing models
<a name="agentcost05-bp03"></a>

 Agent as a service (AaaS) offerings without per-tenant cost attribution can bill only by capacity estimates, can't detect noisy neighbors until infrastructure has already scaled, and can't decide when a tenant should move to dedicated infrastructure. Propagating tenant context through every operation and tracking cost at the tenant level fixes all three problems at once. 

 **Desired outcome:** 
+  You propagate tenant identifiers through all agent operations: model invocations, tool executions, memory operations, and data storage. 
+  You have flexible cost allocation models supporting per-decision, per-task, and per-agent-hour pricing. 
+  You detect noisy neighbors before they drive infrastructure scaling that affects all customers. 
+  You enforce tenant-level budget controls that cap per-tenant spending. 

 **Common anti-patterns:** 
+  Tracking agent costs only at the account level without tenant context, making it impossible to generate accurate tenant invoices. 
+  Allowing high-usage tenants to consume shared resources without detection, driving infrastructure scaling costs that affect all customers. 
+  Implementing only one billing approach because the cost allocation system can't support multiple pricing dimensions. 
+  Allowing unbounded agent costs without tenant-level usage limits, creating financial risk when unexpected usage spikes occur. 
+  Building agent as a service offerings with a single fixed pricing model, reducing the risk of revenue optimization based on actual usage patterns. 

 **Benefits of establishing this best practice:** 
+  Per-tenant cost tracking enables billing based on actual resource consumption rather than capacity-based estimates. 
+  Noisy neighbor detection and tenant-level throttling help prevent unexpected infrastructure scaling from aggressive usage patterns. 
+  Cost allocation data enables data-driven decisions about when dedicated infrastructure becomes more cost-effective than pooled resources. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Tenant context has to travel with every billable event. [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) tags workload identities, credential providers, and API key providers with tenant metadata that propagates through downstream operations. Those tags integrate with AWS Cost Explorer for per-tenant cost breakdowns without requiring separate AWS accounts per tenant. For agents on [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), session-based architecture provides natural tenant boundaries, and consumption-based pricing means each session's bill reflects actual work done for that tenant. 

 [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) captures all billable events with tenant identifiers in metric dimensions: token consumption, tool invocation costs from [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), and memory operation costs from [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html). Tenant-level quota enforcement lives in [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) with Cedar policies, which is how you cap per-tenant spending without pushing the enforcement into application code where it can be bypassed. 

 A *noisy neighbor* is a virtual machine or container that consumes disproportionate system resources. Noisy neighbor detection needs a baseline and a deviation threshold that reflect how agent reasoning depth actually varies. Some tenants execute simple single-step decisions, while others trigger complex multi-turn reasoning chains. An Amazon CloudWatch alarm when a tenant's consumption exceeds three times their historical baseline catches abnormal usage early enough to help prevent infrastructure scaling that increases costs for every customer. The threshold is tuned per workload to avoid under- or over-firing. 

 Resource-sharing decisions need a cost model. Pooled infrastructure achieves higher utilization and lower per-tenant costs but requires strong isolation. Dedicated infrastructure provides stronger isolation and predictable performance at higher fixed costs. Build a per-tenant break-even model that calculates when a tenant's usage would be cheaper on dedicated infrastructure than on their proportional share of pooled resources, and use it to offer dedicated deployments to tenants who have crossed that line. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Tag identities for tenant attribution:** Configure [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) with tenant-specific tags on workload identities, and activate the tenant-id cost allocation tag in the AWS billing console. 

1.  **Deploy agents with session-level tenant tags:** Run agents on [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with session-level tenant tagging so cost attribution follows the session, not the pool. 

1.  **Capture all cost dimensions per tenant:** Configure [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to export telemetry to Amazon CloudWatch with tenant identifiers in metric dimensions. 

1.  **Enforce tenant quotas and noisy neighbor detection:** Implement tenant-level quota enforcement through [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html), and set CloudWatch alarms for consumption spikes exceeding three times the tenant's historical baseline. 

1.  **Build a flexible pricing engine:** Support per-decision, per-task, and per-agent-hour billing models with tenant-specific configurations so pricing can evolve without re-architecting the billing pipeline. 

1.  **Model pooled compared to dedicated break-even:** Use AWS Cost Explorer API data to calculate the break-even point per tenant, identifying tenants approaching the threshold where dedicated AgentCore deployments become cost-effective. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTCOST05-BP01 Establish agent-level reasoning cost tracking and attribution](agentcost05-bp01.html) 
+  [AGENTCOST05-BP02 Implement distributed cost tracing for multi-agent workflows](agentcost05-bp02.html) 
+  [AGENTCOST05-BP04 Create chargeback and ROI reporting](agentcost05-bp04.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Manage multi-tenant Amazon Bedrock costs using application inference profiles](https://aws.amazon.com/blogs/machine-learning/manage-multi-tenant-amazon-bedrock-costs-using-application-inference-profiles/) 
+  [AWS SaaS Lens](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-lens.html) 
+  [Using cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Building multi-tenant SaaS agents with AgentCore (SAS407)](https://www.youtube.com/watch?v=uwXrtyXXuy8) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Observability tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 