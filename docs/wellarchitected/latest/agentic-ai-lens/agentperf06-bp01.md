

# AGENTPERF06-BP01 Design optimized tool integration strategies
<a name="agentperf06-bp01"></a>

 Agents that surface the right tools at the right time respond faster and make better decisions. LLMs make increasingly poor tool selection decisions once the candidate set grows beyond 10-15 tools, so dynamic filtering, parallel execution, and cached results keep the reasoning loop tight even as the tool catalog grows. Tool invocations happen inside the reasoning loop, which means their latency adds directly to response time. 

 **Desired outcome:** 
+  You have tool invocations that add minimal latency to the agent reasoning loop. 
+  You have tool selection that is fast and accurate, with agents choosing from a filtered set of 5-10 relevant options rather than evaluating the full catalog. 
+  You have independent tool calls executing in parallel. 
+  You have tool results cached where appropriate. 
+  You have per-tool latency, error rate, and usage metrics providing visibility into tool performance. 

 **Common anti-patterns:** 
+  Presenting all available tools to the agent on every reasoning iteration, forcing the LLM to evaluate dozens of tool descriptions, consuming context window capacity and degrading selection accuracy. 
+  Executing tool calls sequentially when they have no data dependencies, adding latency equal to the sum of all tool durations rather than the maximum. 
+  Skipping tool result caching, so agents re-invoke the same tool with identical parameters multiple times within a single task. 

 **Benefits of establishing this best practice:** 
+  Parallel tool execution and result caching reduce reasoning loop latency. 
+  Dynamic filtering that presents only relevant tools improves tool selection accuracy. 
+  Per-tool monitoring speeds detection of tool performance issues. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Adopt MCP as the standard tool integration protocol and use [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) to expose tools as MCP-compatible endpoints. AgentCore Gateway provides built-in semantic tool discovery (x\_amz\_bedrock\_agentcore\_search) so agents query for relevant tools by natural language description rather than receiving the full catalog. For agents with access to large tool catalogs, a two-stage selection pattern works well: a lightweight pre-filter narrows the full catalog to the 5-10 most relevant tools based on current task context, and only those filtered tools appear in the LLM's prompt. For agents built with Strands Agents or another agentic framework, built-in parallel tool execution runs independent tool calls concurrently. 

 Design tool APIs specifically for agent consumption, like compact response schemas that return only the fields the agent needs, pagination for large result sets, and partial response support. Cache tool results at multiple levels, request-scoped (within a single reasoning session), session-scoped (across reasoning iterations for the same user), and global (shared data with appropriate TTLs). Tool health monitoring tracks per-tool latency, error rates, and availability, and automatic cutoffs route around slow or failing tools. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Adopt MCP as the standard tool integration protocol and expose tools through AgentCore Gateway:** Expose tools as MCP-compatible endpoints through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) so agents use a single consistent interface. 

1.  **Enable AgentCore Gateway's semantic tool discovery to filter tools by task relevance:** Use x\_amz\_bedrock\_agentcore\_search to narrow the tool set per request so the LLM evaluates only the most relevant 5-10 tools. 

1.  **Implement parallel tool execution for independent tool calls within the same reasoning step:** Use your framework's native parallel tool execution (Strands Agents, LangGraph) so independent tool calls run concurrently. 

1.  **Deploy multi-level tool result caching with appropriate TTLs per tool:** Cache tool results at request-, session-, and global-scope with TTLs matched to each tool's freshness requirements. 

1.  **Configure tool health monitoring with per-tool latency and error rate metrics, and automatic cutoffs for degraded tools:** Track per-tool latency and error rate in Amazon CloudWatch and use automatic cutoffs to route around degraded tools. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF06-BP02 Implement efficient tool invocation patterns](agentperf06-bp02.html) 
+  [AGENTPERF06-BP03 Optimize meta-tool utilization and tool chaining](agentperf06-bp03.html) 
+  [AGENTPERF04-BP02 Implement efficient protocol-based agent communications](agentperf04-bp02.html) 

 **Related documents:** 
+  [Blog: Introducing Amazon Bedrock AgentCore Gateway: Transforming enterprise AI agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/) 
+  [Blog: Transform your MCP architecture: Unite MCP servers through AgentCore Gateway](https://aws.amazon.com/blogs/machine-learning/transform-your-mcp-architecture-unite-mcp-servers-through-agentcore-gateway/) 
+  [Blog: Open Protocols for Agent Interoperability Part 3: Strands Agents & MCP](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-3-strands-agents-mcp/) 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) 
+  [Agentic AI frameworks, protocols, and tools on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/introduction.html) 

 **Related videos:** 
+  [Scale agent tools with AgentCore Gateway (AIM3313)](https://www.youtube.com/watch?v=DlIHB8i6uyE) 
+  [Integrating MCP Tools with Strands Agents](https://www.youtube.com/watch?v=bHSbjCZZFjE) 
+  [Strands Tools: Building Custom AI Agents with Python](https://www.youtube.com/watch?v=EGhIZCfOvG4) 

 **Related examples:** 
+  [GitHub: Amazon Bedrock AgentCore samples, Gateway tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway) 

 **Related workshops:** 
+  [Getting started with Amazon Bedrock AgentCore, Lab 3: Gateway, Identity & Policy](https://catalog.workshops.aws/agentcore-getting-started/en-US/50-add-tool-gateway) 
+  [Diving Deep into Bedrock AgentCore, Gateway](https://catalog.workshops.aws/agentcore-deep-dive/en-US/30-agentcore-gateway) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 