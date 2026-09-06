

# Secure agent tool usage
<a name="agentsec02"></a>

 Agents interact with external systems through tools such as APIs, databases, file systems, and other services. Without proper controls, an agent with tool access can be directed to perform unintended actions. Authorization, input validation, and tool governance reduce the risk of tool misuse and unauthorized operations. 


|  AGENTSEC02: How do you control and secure agent tool usage?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-1"></a>
+  Every tool invocation is authorized against a declarative policy before execution, with the agent identity and the originating user context propagated through the authorization chain. 
+  Agents invoke only tools within their approved scope, and tool parameters and responses pass through schema and policy checks that keep operations inside defined boundaries. 
+  High-risk mutating operations stop at a human-in-the-loop checkpoint, and rate limits cap the impact scope when an agent enters a runaway loop. 
+  Tools and the MCP servers that host them are available to agents only after going through a documented security review and being registered with a pinned version, data classification, and review expiry. 
+  Tool usage is observable end to end, with authorization decisions, validation failures, and invocation rates feeding detection and compliance workflows. 

## Maturity levels
<a name="maturity-levels-1"></a>

 These levels summarize what each stage of maturity looks like for secure agent tool usage as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Agents are granted blanket access to available tools, and authorization is delegated to the agent's own reasoning. Parameters flow to tools without schema enforcement, error responses return raw stack traces, internal endpoint addresses, or database schema details to the agent's context, and there is no registry or version control over tools or the MCP servers that host them. High-risk writes, deletes, and financial actions execute without review.  | 
|  2  |  Emerging  |  Each agent runs under a dedicated identity with scoped permissions on the tools it needs. Schema validation is applied in the tool handler for user-facing parameters, error responses are sanitized so internal details don't reach the agent or the user, and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) timeouts and memory allocations bound the runtime cost and execution time of any single tool invocation. Tools and the MCP servers hosting them are documented in a shared list, but enforcement depends on reviewer discipline.  | 
|  3  |  Defined  |  Agent-to-tool traffic flows through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html), which centralizes OAuth-based inbound authorization and target-specific outbound authentication. Tools and the MCP servers that host them are registered in a version-controlled registry with documented permissions, data classification, and review expiry, and [strict tool use](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) constrains model-generated parameters to conform to the tool schema at the decoding layer.  | 
|  4  |  Proactive  |  [Policy in Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-policy.html) enforces [Cedar](https://docs.cedarpolicy.com/) policies with a default-deny posture at the gateway, evaluating every tool call against identity-aware conditions and parameter constraints outside the agent's reasoning loop. Human-in-the-loop checkpoints intercept high-risk mutating operations through [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) callback patterns, rate limits run at both the gateway and tool tiers, and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms fire on authorization failures and validation spikes.  | 
|  5  |  Optimized  |  Tool authorization, validation, and registry controls are codified end to end and validated continuously through red-team exercises and automated drift detection with [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html). Deprecation workflows remove expired tools and MCP server entries automatically, policies adapt from observed behavior, and centralized MCP server governance (covering registration, version pinning, network egress controls, and shared discovery) is enforced consistently across accounts.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-1"></a>
+  Tool access granted at the agent level but enforced only by the agent's reasoning, so nothing outside the model helps prevent an injected or poisoned prompt from invoking tools that sit outside the agent's intended scope. 
+  Schema validation applied to user-facing parameters but not to parameters the model generates, on the assumption that the model can't produce malformed output. In practice, model-generated parameters are an attack surface that carries injection payloads and invalid types. 
+  Registries maintained as static documents rather than as enforced controls at the gateway or the MCP client, so agents continue to discover and invoke tools that no one has reviewed. 
+  Remote Model Context Protocol (MCP) servers adopted with the same risk assumptions as local tools, which understates the exposure introduced by network connectivity, third-party authentication, and external data handling. 
+  Rate limiting treated as a cost control rather than as a security control, so a runaway loop or a prompt injection that triggers mass tool calls runs long enough to affect downstream systems before human responders intervene. 

**Topics**
+ [Capability intent](#capability-intent-1)
+ [Maturity levels](#maturity-levels-1)
+ [Common issues to watch for](#common-issues-to-watch-for-1)
+ [AGENTSEC02-BP01 Implement tool authorization](agentsec02-bp01.md)
+ [AGENTSEC02-BP02 Validate tool inputs and outputs](agentsec02-bp02.md)
+ [AGENTSEC02-BP03 Maintain approved tool registry with security assessments](agentsec02-bp03.md)