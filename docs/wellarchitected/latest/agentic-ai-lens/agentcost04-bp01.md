

# AGENTCOST04-BP01 Design cost effective tool selection to minimize unnecessary invocations
<a name="agentcost04-bp01"></a>

 Often, the most cost-effective tool call is the one an agent decides not to make because the answer is already in context. Context-first reasoning, cost-ranked selection, and duplicate detection tie tool invocation to the value of the information retrieved. 

 **Desired outcome:** 
+  You have agents checking context and managed memory before invoking tools. 
+  You have a cost-ranked selection rubric that points agents to cheaper alternatives first. 
+  You batch requests where possible and cache results within sessions to avoid duplicate calls. 
+  You monitor per-tool invocation frequency and cache hit rates as distinct metrics. 

 **Common anti-patterns:** 
+  Invoking tools without checking whether required information already exists in context or managed memory, adding cost without improving results. 
+  Creating narrow tool interfaces that return minimal data, forcing follow-up calls to assemble complete context. 
+  Implementing retry logic without exponential backoff or automatic cutoffs, causing retry storms that multiply costs during service degradation. 
+  Operating without tool invocation metrics, so no one can identify which tools are most expensive or most frequently called. 

 **Benefits of establishing this best practice:** 
+  Context-first evaluation reduces unnecessary tool invocations for agents with rich context from prior reasoning steps. 
+  Cost-ranked tool selection rubrics direct agents to cheaper alternatives, reserving expensive external APIs for cases where lower-cost options are insufficient. 
+  Batched tool interfaces and complete result sets reduce per-call overhead and the need for follow-up invocations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Tool necessity belongs in the agent's reasoning prompt, not as an afterthought in monitoring. The system prompt should instruct the model to assess whether the answer can be derived from information already in context, from conversation history stored in [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html), or from prior tool results within the same reasoning cycle, before selecting a tool. Pair this with a cost-ranked selection rubric that places cheaper alternatives first: if a local computation or a cached result produces the same answer as an external API call, the agent should take the cheaper path. 

 Tool interface design matters as much as agent instructions. Narrow interfaces that return minimal data force agents to make follow-up calls to assemble the context they need, which inflates per-reasoning-cycle tool cost. [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) provides MCP-based tool discovery with composition features that combine multiple APIs into single endpoints, reducing invocation overhead. Design tool interfaces to accept batch inputs and return complete result sets so a single call does the work of many. 

 Consider how you implement duplicate detection. Agents often invoke the same tool with identical parameters across reasoning iterations, especially when revisiting a branch. Implement a session-scoped tool result cache in your action group Lambda functions or AgentCore Gateway MCP servers so the agent doesn't re-invoke the same tool with the same parameters. Store results in AgentCore Memory's short-term memory so the agent's reasoning prompt can reveal prior results before deciding to make another call. 

 For enforcement and measurement, [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) applies Cedar policies that halt retries when failure rates indicate persistent degradation and cap tool calls per reasoning cycle. [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes tool selection patterns, Amazon CloudWatch tracks invocation frequency and deduplication hit rates, and [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) scores tool selection accuracy so patterns of over-invocation appear as quality data, not just cost data. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Embed tool necessity evaluation in system prompts:** Direct the model to check context and [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) before invoking tools, and include a cost-ranked selection rubric that places cheaper alternatives first. 

1.  **Redesign tool interfaces for batching:** Expose tools through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) with batch inputs and complete result sets so one call carries the payload that previously required several. 

1.  **Cache tool results within sessions:** Implement session-scoped caches in action group Lambda functions or Gateway MCP servers to deduplicate identical tool calls, storing results in AgentCore Memory so the agent can surface them before the next call. 

1.  **Apply automatic cutoffs through policy:** Configure [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies that cap tool calls per reasoning cycle and halt retries on persistent failures. 

1.  **Monitor tool selection patterns:** Use [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to surface tool selection patterns and create Amazon CloudWatch metrics for tool invocation frequency and deduplication hit rates. 

1.  **Score tool selection accuracy:** Use [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to periodically score tool selection accuracy, flagging patterns where agents choose expensive tools when cheaper alternatives would suffice. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTCOST01-BP01 Use the reflection pattern to design efficient agent reasoning loops](agentcost01-bp01.html) 
+  [AGENTCOST02-BP02 Cost optimize token consumption through efficient prompt engineering](agentcost02-bp02.html) 
+  [AGENTCOST04-BP02 Cost optimize tool serving through serverless and resource sharing](agentcost04-bp02.html) 
+  [AGENTCOST04-BP03 Implement intelligent caching and failure handling for tool results](agentcost04-bp03.html) 
+  [AGENTCOST05-BP01 Establish agent-level reasoning cost tracking and attribution](agentcost05-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) 
+  [Guidance for Cost Analysis and Optimization with Amazon Bedrock Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/) 

 **Related videos:** 
+  [AWS 2025 - AgentCore Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8) 
+  [AWS re:Invent 2024 - Scale agent tools with AgentCore Gateway (AIM3313)](https://www.youtube.com/watch?v=DlIHB8i6uyE) 
+  [Integrating MCP Tools with Strands Agents](https://www.youtube.com/watch?v=bHSbjCZZFjE) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Gateway tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway) 

 **Related workshops:** 
+  [Diving Deep into Bedrock AgentCore - Gateway](https://catalog.workshops.aws/agentcore-deep-dive/en-US/30-agentcore-gateway) 

 **Related tools:** 
+  [Strands Agents MCP Tools](https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 