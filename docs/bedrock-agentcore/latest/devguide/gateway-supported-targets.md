# Supported targets for Amazon Bedrock AgentCore gateways

Targets define the tools that your gateway will host. Amazon Bedrock AgentCore Gateway supports two categories of targets:

- **MCP targets** – Operate in aggregation mode. The gateway acts as an MCP server whose capabilities combine those of all its MCP targets into a single unified virtual MCP server.
- **HTTP targets** – The gateway sends traffic directly to HTTP targets without aggregation or protocol translation.
  You can attach different credential providers to different targets, which lets you securely control access to targets. The following topics explain the target types in each category and how they integrate into your gateway. The final topic discusses how target names are constructed for a gateway.

###### Topics

- [MCP targets](gateway-targets-mcp.md "gateway-targets-mcp.md")
- [HTTP targets](gateway-targets-http.md "gateway-targets-http.md")
