

# AGENTPERF06-BP02 Implement efficient tool invocation patterns
<a name="agentperf06-bp02"></a>

 Well-tuned tool invocation patterns help the agent's responsiveness reflect the tool's actual processing time, not infrastructure overhead. Each tool invocation involves connection establishment, serialization, network transfer, processing, and deserialization, trimming each component compounds across the many tool calls in a typical agent task. 

 **Desired outcome:** 
+  You have individual tool invocations that execute with minimal overhead beyond the tool's inherent processing time. 
+  You have connection pooling that removes repeated connection establishment costs. 
+  You have timeouts that help prevent slow tools from blocking agent execution. 
+  You have automatic cutoffs that detect degraded tools and route to alternatives. 
+  You have per-tool invocation metrics that provide visibility into performance characteristics. 

 **Common anti-patterns:** 
+  Establishing new connections for every tool invocation rather than maintaining connection pools, adding hundreds of milliseconds of TLS handshake latency to each call. 
+  Implementing aggressive retry strategies without backoff or jitter, creating retry storms that overwhelm already-degraded tools. 
+  Setting tool invocation timeouts too high or not at all, letting a single slow tool call block the agent for seconds and exceed the overall task latency budget. 

 **Benefits of establishing this best practice:** 
+  Connection pooling and persistent connections reduce per-tool-call overhead. 
+  Appropriate timeouts protect the agent latency budget. 
+  Automatic cutoffs support fast failover to alternatives. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 For tools accessed through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), the gateway handles connection management, authentication, and routing automatically. For custom tool endpoints, connection pooling through HTTP keep-alive connections or framework-specific pool configurations keeps TLS sessions warm across invocations. 

 For [AWS Lambda](https://aws.amazon.com/lambda/)-based tools, initializing connections outside the handler function so they persist across invocations within the same execution environment turns a handshake for each request into one per environment. Tool invocation timeouts should be set based on the tool's expected response time, typically two to three times the p95 latency. 

 Retry strategies with exponential backoff and jitter handle transient failures, with a maximum of two to three retries and a total retry budget that doesn't exceed the tool's timeout. Automatic cutoff patterns track tool failure rates and open the circuit when failures exceed a threshold, returning a cached result or error immediately rather than waiting for another timeout. 

 For tools that support batch operations, request batching (a batch API for multiple item lookups) reduces overhead for each call across the set. Per-tool invocation metrics (latency percentiles, error rates, timeout rates, and automatic cutoff state) belong on the agent performance dashboard alongside reasoning-loop metrics. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Use AgentCore Gateway for managed tool access where possible, and implement connection pooling for custom tool endpoints:** Use [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) for managed tool access. For custom endpoints, enable HTTP keep-alive and framework-level connection pools. 

1.  **Configure per-tool timeouts based on profiled p95 latency:** Size each tool's timeout to two to three times its measured p95 latency so slow individual calls don't stall the agent. 

1.  **Implement retry strategies with exponential backoff and jitter:** Use exponential backoff with jitter and cap retries at two to three so transient failures recover without overwhelming already-degraded tools. 

1.  **Deploy automatic cutoff patterns that fast-fail when tools are degraded:** Track failure rate per tool and open the circuit when failures exceed a threshold, returning a cached result or error immediately. 

1.  **Implement request batching for tools that support batch operations:** Use batch APIs when multiple items are needed so per-call overhead amortizes across the set. 

1.  **Monitor per-tool invocation metrics and establish alerting for latency and error rate anomalies:** Publish per-tool latency percentiles, error rates, timeout rates, and cutoff state to CloudWatch with alarms on anomalies. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF06-BP01 Design optimized tool integration strategies](agentperf06-bp01.html) 
+  [AGENTPERF02-BP03 Optimize agent execution paths for reduced latency](agentperf02-bp03.html) 
+  [AGENTPERF03-BP04 Establish efficient agent caching and data access patterns](agentperf03-bp04.html) 

 **Related documents:** 
+  [Blog: Build long-running MCP servers on Amazon Bedrock AgentCore with Strands Agents integration](https://aws.amazon.com/blogs/machine-learning/build-long-running-mcp-servers-on-amazon-bedrock-agentcore-with-strands-agents-integration/) 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Agentic AI frameworks, protocols, and tools on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/introduction.html) 

 **Related examples:** 
+  [GitHub: Amazon Bedrock AgentCore samples, Gateway tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 