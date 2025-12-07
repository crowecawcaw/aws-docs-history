# Supported targets for Amazon Bedrock AgentCore gateways

Targets define the tools that your gateway will host. Amazon Bedrock AgentCore Gateway supports multiple target types that are detailed in the following topics. You can attach different credential providers to different targets, which lets you securely control access to targets. By adding targets, your gateway becomes a single MCP URL that enables access to all of the relevant tools for an agent.

The following topics explain the target types that are supported for AgentCore Gateway and how they integrate into your gateway. You should review these pages to make sure that a resource that you want to add as a target for your gateway is compatible. The final topic discusses how target names are constructed for a gateway so you can understand how to incorporate them.

###### Topics

- [AWS Lambda function targets](gateway-add-target-lambda.md "gateway-add-target-lambda.md")
- [Amazon API Gateway REST API stages as targets](gateway-target-api-gateway.md "gateway-target-api-gateway.md")
- [OpenAPI schema targets](gateway-schema-openapi.md "gateway-schema-openapi.md")
- [Smithy model targets](gateway-building-smithy-targets.md "gateway-building-smithy-targets.md")
- [MCP servers targets](gateway-target-MCPservers.md "gateway-target-MCPservers.md")
- [Built-in templates from integration providers as targets](gateway-target-integrations.md "gateway-target-integrations.md")
- [Understand how AgentCore Gateway tools are named](gateway-tool-naming.md "gateway-tool-naming.md")
