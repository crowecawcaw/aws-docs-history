

# AGENTCOST04-BP02 Cost optimize tool serving through serverless and resource sharing
<a name="agentcost04-bp02"></a>

 Tool infrastructure that runs constantly to serve unpredictable agent traffic carries the highest idle cost in an agent stack. Serverless tool serving with shared infrastructure across agents aligns spend with actual invocations and removes the fixed overhead of per-agent dedicated instances. 

 **Desired outcome:** 
+  You have tool-serving infrastructure that scales dynamically with agent usage and charges only for actual invocations. 
+  You share stateless tool services across agents while maintaining security isolation. 
+  You use private networking and compact serialization to reduce data transfer costs on high-frequency tool invocations. 
+  You track per-agent cost attribution for targeted optimization. 

 **Common anti-patterns:** 
+  Running persistent servers for tool serving that incur charges during hours or days when no agents invoke tools. 
+  Creating dedicated tool server instances per agent rather than shared stateless services, producing dozens of underutilized servers. 
+  Routing tool invocations through NAT Gateways when agents and tools live in the same VPC, incurring unnecessary per-GB data processing charges. 

 **Benefits of establishing this best practice:** 
+  Serverless tool serving scales to zero when agents are inactive, reducing idle costs through consumption-based pricing. 
+  Shared tool infrastructure spreads fixed hosting overhead across all agents while maintaining security isolation. 
+  VPC endpoints and compact serialization reduce data transfer costs for high-frequency tool invocations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Agent tool traffic is inherently bursty. An agent fleet is active during business hours, idle overnight, and heavily uneven across agent types. Provisioned tool infrastructure pays for that shape by keeping compute warm through idle hours, which can be a significant hidden cost in agent stacks. [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) provides fully-managed, serverless tool serving that converts APIs and existing services into MCP-compatible tools without infrastructure management. AgentCore Gateway handles authentication, scales automatically, and combines multiple APIs into unified endpoints. 

 Because tools exposed through AgentCore Gateway are available to all authorized agents, one endpoint can serve an entire fleet rather than one endpoint per agent. [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) and [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) supply the fine-grained access control that keeps sharing safe. 

 For tools that need extended execution, [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) supports workloads up to 8 hours with consumption-based pricing calculated at per-second increments. Consumption pricing is the right default for unpredictable tool invocation patterns because it charges only during active processing. 

 Cold starts are a failure mode worth planning for. A cold tool extends the agent's reasoning cycle and may trigger retries, which can push per-session token costs up on cold paths. Monitor cold start frequency in Amazon CloudWatch and evaluate Lambda SnapStart or scheduled warming when cold starts are material. 

 Networking and serialization are the foundation of planning for these failure modes. VPC endpoints for private data paths avoid NAT Gateway processing charges for high-frequency tool invocations between agents and tools in the same VPC. Compact JSON (or binary formats where supported) reduces payload sizes on repeated high-frequency calls. Tagging every invocation with agent ID and workflow ID lets [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and AWS Cost Explorer reveal which agents and tools drive the highest spend. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Expose tools through serverless Gateway:** Deploy agent tools through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) MCP server capabilities for serverless infrastructure with automatic scaling and shared access across agents. 

1.  **Apply fine-grained access control:** Configure [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies for per-agent tool access, preserving security isolation while sharing infrastructure. 

1.  **Attribute cost per agent:** Use [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) telemetry tags with agent ID and workflow ID, and generate periodic AWS Cost Explorer reports by agent and tool type. 

1.  **Monitor invocation patterns and cold starts:** Expose tool invocation patterns through AgentCore Observability, and set Amazon CloudWatch alarms for patterns that exceed expected bounds, including cold start frequency. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTCOST04-BP01 Design cost effective tool selection to minimize unnecessary invocations](agentcost04-bp01.html) 
+  [AGENTCOST04-BP03 Implement intelligent caching and failure handling for tool results](agentcost04-bp03.html) 
+  [AGENTCOST05-BP01 Establish agent-level reasoning cost tracking and attribution](agentcost05-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Guidance for Cost Analysis and Optimization with Amazon Bedrock Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/) 

 **Related videos:** 
+  [AWS 2025 - AgentCore Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8) 
+  [AWS 2025 - AgentCore Deep Dive: Runtime](https://www.youtube.com/watch?v=wizEw5a4gvM) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Gateway tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway) 

 **Related workshops:** 
+  [Getting started with Amazon Bedrock AgentCore - Lab 3: Gateway, Identity & Policy](https://catalog.workshops.aws/agentcore-getting-started/en-US/50-add-tool-gateway) 
+  [Diving Deep into Bedrock AgentCore - Gateway](https://catalog.workshops.aws/agentcore-deep-dive/en-US/30-agentcore-gateway) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 