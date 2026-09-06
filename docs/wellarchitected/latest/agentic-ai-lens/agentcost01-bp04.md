

# AGENTCOST01-BP04 Design agent hierarchies and delegation patterns that reduce coordination overhead
<a name="agentcost01-bp04"></a>

 Supervisor cost in agent hierarchies grows with the verbosity of capability descriptions and the frequency of check-ins. Compact manifests and autonomous workers keep coordination cost proportional to workflow complexity rather than step count. 

 **Desired outcome:** 
+  Your agent hierarchies use the shallowest orchestration structure capable of managing the workflow. 
+  You have supervisor agents operating on compressed capability manifests that minimize input tokens per routing decision. 
+  Your worker agents complete multi-step sub-tasks autonomously, escalating to supervisors only for task assignment and result validation. 
+  You track orchestrator cost as a distinct category with a target supervisor-to-worker cost ratio. 

 **Common anti-patterns:** 
+  Including verbose natural-language descriptions of every worker's capabilities in routing prompts, which inflates token cost that then scales linearly with worker count. 
+  Requiring supervisor check-ins after each sub-step, which multiplies coordination overhead when workers could complete multi-step work autonomously. 
+  Tracking only aggregate workflow cost without decomposing orchestrator compared to worker expense, so disproportionate coordination overhead hides in the total. 

 **Benefits of establishing this best practice:** 
+  Compressed capability manifests reduce supervisor input-token cost per routing decision. 
+  Autonomous workers remove supervisor round-trips for intermediate decisions. 
+  Per-tier cost attribution surfaces optimization opportunities where coordination overhead exceeds execution value. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Supervisor cost has two main drivers: how expensive each routing decision is and how many times routing happens. 

 The first is controlled by manifest size. Supervisors that describe workers in paragraphs of natural language pay for those paragraphs on every routing call, and that cost scales linearly with worker count. Short, structured capability manifests (description, input schema, output schema, under 200 tokens each) cut this cost without sacrificing routing quality, because the supervisor doesn't need prose to choose between workers that have distinct schemas. 

 The second is controlled by context relay. When context flows from parent to worker through the supervisor, every byte of that context is transmitted twice: once into the supervisor, and once into the worker as part of the routing response. [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) removes that doubling by letting workers read shared context directly from memory using the session's actor ID and session ID, so the supervisor only routes rather than relays. [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) reduces it further by supporting runtime tool discovery through Model Context Protocol, so the supervisor prompt doesn't need to enumerate every tool the workers can call. [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) controls which tools each worker is allowed to invoke autonomously, making it safe to shift decisions downward without losing governance. 

 Workers designed with sufficient tool autonomy and clear success criteria can complete multi-step sub-tasks, returning a single structured result with a confidence score. The supervisor then makes an efficient accept-or-reject decision rather than re-reasoning from scratch at each intermediate step. For workflows with repeatable decomposition patterns, a plan-then-execute approach compresses this further, where one supervisor invocation generates the full task plan, then workers execute the plan without further supervision. 

 Track the supervisor-to-worker cost ratio. Set a target (for example, supervisor tokens no more than 15% of worker tokens) and alert when it is exceeded. A breach typically signals that manifest compression, worker autonomy, or plan-then-execute adoption is needed. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Compress worker capability descriptions:** Replace natural-language capability descriptions with structured manifests (description, input schema, output schema) under 200 tokens each, and use [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) runtime tool discovery to avoid listing tools in the supervisor prompt. 

1.  **Redesign workers for autonomous multi-step completion:** Give each worker sufficient tool autonomy and clear success criteria to complete its sub-task end-to-end, and require the worker to emit a confidence score in every response so the supervisor can make accept-or-reject decisions without re-reasoning. 

1.  **Apply policy and shared memory for direct context access:** Configure [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) through Gateway to enforce worker tool-access boundaries, and provision [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) so workers read shared context directly instead of receiving it relayed through the supervisor. 

1.  **Track supervisor-to-worker cost ratio:** Configure [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to attribute tokens per tier, build Amazon CloudWatch dashboards showing the supervisor-to-worker ratio per workflow, and alert when the ratio exceeds a 15% target. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTCOST01-BP02 Optimize multi-agent collaboration cost through efficient handoff patterns](agentcost01-bp02.html) 
+  [AGENTCOST01-BP03 Implement cost-effective patterns like hybrid supervisor for multi-agent coordination](agentcost01-bp03.html) 
+  [AGENTCOST05-BP01 Establish agent-level reasoning cost tracking and attribution](agentcost05-bp01.html) 
+  [AGENTCOST05-BP02 Implement distributed cost tracing for multi-agent workflows](agentcost05-bp02.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) 
+  [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Agentic AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html) 

 **Related videos:** 
+  [AWS 2025 - AgentCore Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8) 
+  [AWS 2025 - AgentCore Observability: Monitor and Debug with OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Multi-agent tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/03-advanced-concepts) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 