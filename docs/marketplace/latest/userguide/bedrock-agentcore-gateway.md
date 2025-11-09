# Amazon Bedrock AgentCore Gateway

This document provides information for AWS Marketplace sellers who want to list API-based AI agent products or tools that can be integrated with Amazon Bedrock AgentCore Gateway.

###### Topics

- [Overview](#agentcore-overview "#agentcore-overview")
- [Integration with Bedrock AgentCore Gateway](#bedrock-agentcore-integration "#bedrock-agentcore-integration")

## Overview

Amazon Bedrock AgentCore Gateway helps developers build, deploy, discover, and connect to tools at scale. The service enables you to:

- Convert APIs, Lambda functions, and existing services into Model Context Protocol (MCP)-compatible tools
- Make tools available to agents through Gateway endpoints
- Use comprehensive ingress and egress authentication in a fully managed service

AI agents use these tools to perform tasks such as:

- Querying databases
- Sending messages
- Analyzing documents

For more information, see [Amazon Bedrock AgentCore Developer Guide](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md").

## Integration with Bedrock AgentCore Gateway

You can enable Amazon Bedrock AgentCore Gateway integration for your SaaS API-based AI agent products in one of the following ways, depending on your product:

- if you list an MCP server with OAuth authentication, you can opt-in to offer your buyers the integration with no additional requirements.
  The MCP server endpoint you provide as part of your listing process will be used for the integration.
  However, you must ensure your MCP server meets the requirements listed below.
- For all other products, you can provide an OpenAPI specification to enable the integration.

### MCP server requirements

Your MCP server must meet the following requirements:

- OAuth authentication with one of following configurations:
  - client id, client secret, and discovery URL
  - client id, client secret, issuer, authorization endpoint and token endpoint.

- The MCP server must have tool capabilities.
- Supported MCP protocol versions: **2025-06-18** and **2025-03-26**.
- For the provided URL or endpoint of the server, the URL should be encoded. The Gateway uses the same URL to invoke the server.

### OpenAPI specification requirements

Your OpenAPI specification must:

- Include `operationId` fields for all operations
- Be free of semantic errors
- Include a valid secure (https) endpoint URL in the server attribute

The following table shows supported and unsupported OpenAPI features:

| Category             | Supported                                                                             | Not Supported                        |
| -------------------- | ------------------------------------------------------------------------------------- | ------------------------------------ |
| Version              | 3.0 and 3.1                                                                           | 2                                    |
| Schema definitions   | Basic data types (string, number, boolean, etc.)                                      | oneOf specifications                 |
|                      | Required field validation                                                             | anyOf specifications                 |
|                      | Nested objects                                                                        |                                      |
|                      | Arrays with item specs                                                                |                                      |
|                      | Standard HTTP methods                                                                 |                                      |
| Media types          | application/json                                                                      | Custom media types                   |
|                      | application/xml                                                                       | Binary media types                   |
|                      | multipart/form-data                                                                   |                                      |
|                      | x-www-form-urlencoded                                                                 |                                      |
| Parameters           | Simple path parameters and basic query parameters such as string/number/boolean types | Complex path parameter serialization |
|                      |                                                                                       | Complex query parameter arrays       |
|                      |                                                                                       | Header parameter serialization       |
|                      |                                                                                       | Cookie parameter serialization       |
| Request and response | JSON bodies                                                                           |                                      |
|                      | XML bodies                                                                            |                                      |
|                      | Standard HTTP status codes                                                            |                                      |
| Validation           | Basic field validation                                                                | Regex pattern validation             |
|                      |                                                                                       | Min/max value validation             |
| Security             | N/A                                                                                   | Security schemes at spec level       |
|                      |                                                                                       | Multiple security schemes            |
|                      |                                                                                       | OAuth 2.0 at spec level              |
|                      |                                                                                       | API Key at spec level                |
|                      |                                                                                       | HTTP Basic auth at spec level        |
| Server configuration | Basic URL                                                                             |                                      |
|                      | URL with placeholders                                                                 |                                      |

### Enabling Bedrock AgentCore Gateway

Before you enable Gateway integration, test your OpenAPI specification or MCP
server with Amazon Bedrock AgentCore Gateway by completing these tasks:

- [Create a gateway](../../../bedrock-agentcore/latest/devguide/gateway-building.md "../../../bedrock-agentcore/latest/devguide/gateway-building.md")
- [Attach a Target](../../../bedrock-agentcore/latest/devguide/gateway-building-adding-targets.md "../../../bedrock-agentcore/latest/devguide/gateway-building-adding-targets.md")
- [Test your Gateway](../../../bedrock-agentcore/latest/devguide/gateway-building-testing.md "../../../bedrock-agentcore/latest/devguide/gateway-building-testing.md")

You can enable integration with Amazon Bedrock AgentCore by providing OpenAPI spec.

###### To enable Gateway integration

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management").
2. Open the [AI agents and tools](https://aws.amazon.com/marketplace/management/products/aiagents "https://aws.amazon.com/marketplace/management/products/aiagents") page.
3. On the **AI agents and tools products** tab,
   select the product to modify.
4. From the **Request changes** dropdown list, select **Update fulfillment options**.
5. Choose **Enable tool for Amazon Bedrock AgentCore integration**.
6. Upload your OpenAPI specification or use your MCP endpoint for MCP servers
   with OAuth authentication..
7. Choose **Submit**.

After you submit, the request status appears as **Under review** in the **Requests** tab. When processing completes, the status changes to **Succeeded**.
