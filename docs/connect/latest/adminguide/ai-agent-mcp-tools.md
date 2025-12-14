# Enable AI agents to retrieve information and complete

actions with MCP tools

Amazon Connect supports Model Context Protocol (MCP), enabling AI agents for both end-customer
self-service and employee assistance to use standardized tools for retrieving information
and completing actions. With MCP support, you can enhance your AI agents with extensible
tool capabilities that reduce contact handle time and increase issue resolution across
customer and agent interactions.

MCP provides AI agents with the ability to automatically perform tasks such as looking up
order status, processing refunds, and updating customer records during interactions without
requiring human intervention. This standardized protocol enables AI agents to access and
execute tools from multiple sources while maintaining consistent security and governance
controls.

## Tool types and integration options

Amazon Connect provides multiple ways to add tools to AI agent configurations:

Out-of-the-box tools

Amazon Connect includes prebuilt tools for common tasks such as updating contact
attributes and retrieving case information, enabling immediate functionality
without additional configuration.

Flow module tools

You can create new or convert existing flow modules into MCP tools,
enabling you to reuse the same business logic across both static and
generative AI workflows. Flow modules can connect to third-party sources and
integrate with existing business systems.

Third-party MCP tools

You can use third-party integrations through Amazon Bedrock AgentCore Gateway. By
registering AgentCore Gateways in the AWS Management Console, similar to
how third-party applications are registered to Amazon Connect today, you gain access
to whatever tools are available on those servers, including remote MCP
servers.

## Tool configuration and governance

When you add tools to AI agents, you can enhance tool accuracy and control through
advanced configuration options:

- Add additional instructions to AI agents on how to use specific tools.
- Override input values to ensure proper tool execution.
- Filter output values to boost accuracy and relevance.

Amazon Connect reuses security profiles for Amazon Connect users for AI agents, allowing you to govern
the boundaries of what abilities your AI agents can perform, just as you govern the
abilities your customer service representatives can take in the Amazon Connect system.

MCP support is available through the same interfaces as other Amazon Connect AI agent features
and integrates seamlessly with existing Amazon Connect workflows and third-party systems. For
more information, see the [Amazon Connect Model Context Protocol API
Reference Guide](../APIReference/Welcome.md "../APIReference/Welcome.md").
