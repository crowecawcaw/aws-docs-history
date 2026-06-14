# Secure agent tool usage

Agents interact with external systems through tools such as APIs,
databases, file systems, and other services. Without proper
controls, an agent with tool access can be directed to perform
unintended actions. Authorization, input validation, and tool
governance reduce the risk of tool misuse and unauthorized
operations.

| AGENTSEC02: How do you control and secure agent tool<br>usage? |
| -------------------------------------------------------------- |
|                                                                |

## Capability intent

- Every tool invocation is authorized against a declarative
  policy before execution, with the agent identity and the
  originating user context propagated through the
  authorization chain.
- Agents invoke only tools within their approved scope, and
  tool parameters and responses pass through schema and policy
  checks that keep operations inside defined boundaries.
- High-risk mutating operations stop at a human-in-the-loop
  checkpoint, and rate limits cap the impact scope when an
  agent enters a runaway loop.
- Tools and the MCP servers that host them are available to
  agents only after going through a documented security review
  and being registered with a pinned version, data
  classification, and review expiry.
- Tool usage is observable end to end, with authorization
  decisions, validation failures, and invocation rates feeding
  detection and compliance workflows.

## Maturity levels

These levels summarize what each stage of maturity looks like
for secure agent tool usage as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agents are granted blanket access to available tools,<br>and authorization is delegated to the agent's own<br>reasoning. Parameters flow to tools without schema<br>enforcement, error responses return raw stack traces,<br>internal endpoint addresses, or database schema details<br>to the agent's context, and there is no registry or<br>version control over tools or the MCP servers that host<br>them. High-risk writes, deletes, and financial actions<br>execute without review.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 2     | Emerging  | Each agent runs under a dedicated identity with scoped<br>permissions on the tools it needs. Schema validation is<br>applied in the tool handler for user-facing parameters,<br>error responses are sanitized so internal details don't<br>reach the agent or the user, and<br>[AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") timeouts and memory allocations bound the<br>runtime cost and execution time of any single tool<br>invocation. Tools and the MCP servers hosting them are<br>documented in a shared list, but enforcement depends on<br>reviewer discipline.                                                                                                                                                                                                                                                                                                                               |
| 3     | Defined   | Agent-to-tool traffic flows through<br>[Amazon<br>Bedrock AgentCore Gateway](../../../bedrock/latest/userguide/agentcore-gateway.md "../../../bedrock/latest/userguide/agentcore-gateway.md"), which centralizes<br>OAuth-based inbound authorization and target-specific<br>outbound authentication. Tools and the MCP servers that<br>host them are registered in a version-controlled<br>registry with documented permissions, data<br>classification, and review expiry, and<br>[strict<br>tool use](../../../bedrock/latest/userguide/tool-use.md "../../../bedrock/latest/userguide/tool-use.md") constrains model-generated parameters to<br>conform to the tool schema at the decoding layer.                                                                                                                                                                                                                                               |
| 4     | Proactive | [Policy<br>in Amazon Bedrock AgentCore](../../../bedrock/latest/userguide/agentcore-policy.md "../../../bedrock/latest/userguide/agentcore-policy.md") enforces<br>[Cedar](https://docs.cedarpolicy.com/ "https://docs.cedarpolicy.com/")<br>policies with a default-deny posture at the gateway,<br>evaluating every tool call against identity-aware<br>conditions and parameter constraints outside the agent's<br>reasoning loop. Human-in-the-loop checkpoints intercept<br>high-risk mutating operations through<br>[AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") callback patterns, rate limits run<br>at both the gateway and tool tiers, and<br>[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") alarms fire on authorization failures<br>and validation spikes. |
| 5     | Optimized | Tool authorization, validation, and registry controls<br>are codified end to end and validated continuously<br>through red-team exercises and automated drift detection<br>with<br>[AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md"). Deprecation workflows remove expired<br>tools and MCP server entries automatically, policies<br>adapt from observed behavior, and centralized MCP server<br>governance (covering registration, version pinning,<br>network egress controls, and shared discovery) is<br>enforced consistently across accounts.                                                                                                                                                                                                                                                                                                                      |

## Common issues to watch for

- Tool access granted at the agent level but enforced only by
  the agent's reasoning, so nothing outside the model helps
  prevent an injected or poisoned prompt from invoking tools
  that sit outside the agent's intended scope.
- Schema validation applied to user-facing parameters but not
  to parameters the model generates, on the assumption that
  the model can't produce malformed output. In practice,
  model-generated parameters are an attack surface that
  carries injection payloads and invalid types.
- Registries maintained as static documents rather than as
  enforced controls at the gateway or the MCP client, so
  agents continue to discover and invoke tools that no one has
  reviewed.
- Remote Model Context Protocol (MCP) servers adopted with the
  same risk assumptions as local tools, which understates the
  exposure introduced by network connectivity, third-party
  authentication, and external data handling.
- Rate limiting treated as a cost control rather than as a
  security control, so a runaway loop or a prompt injection
  that triggers mass tool calls runs long enough to affect
  downstream systems before human responders intervene.

###### Best practices

- [AGENTSEC02-BP01 Implement tool authorization](agentsec02-bp01.md "agentsec02-bp01.md")
- [AGENTSEC02-BP02 Validate tool inputs and outputs](agentsec02-bp02.md "agentsec02-bp02.md")
- [AGENTSEC02-BP03 Maintain approved tool registry with security assessments](agentsec02-bp03.md "agentsec02-bp03.md")
