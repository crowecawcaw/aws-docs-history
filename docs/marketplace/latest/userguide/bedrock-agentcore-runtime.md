# Amazon Bedrock AgentCore Runtime for AWS Marketplace

This document provides information for AWS Marketplace sellers who want to list AI agents or tools that can be deployed on Bedrock AgentCore Runtime.
It outlines the technical requirements, configuration guidelines, and best practices for preparing your Bedrock AgentCore Runtime supported container for AWS Marketplace.

###### Topics

- [Overview](#agentcore-runtime-overview "#agentcore-runtime-overview")
- [Bedrock AgentCore container technical requirements](#agentcore-container-requirements "#agentcore-container-requirements")
- [Testing your Bedrock AgentCore Runtime container](#testing-agentcore-container "#testing-agentcore-container")
- [Best practices for container configuration](#container-best-practices "#container-best-practices")
- [Requirements for AWS Marketplace submission](#marketplace-submission-requirements "#marketplace-submission-requirements")
- [Additional Resources](#agentcore-additional-resources "#agentcore-additional-resources")
- [Support for AgentCore Runtime on AWS Marketplace](#agentcore-support "#agentcore-support")

## Overview

Amazon Bedrock AgentCore Runtime provides a secure, serverless and purpose-built hosting environment for deploying and running AI agents or tools. When listing your Bedrock AgentCore Runtime container on AWS Marketplace, you need to ensure it meets specific requirements to function properly within the Bedrock AgentCore environment.

###### Note

To learn more see the [Getting started with Amazon Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/runtime-getting-started.md "../../../bedrock-agentcore/latest/devguide/runtime-getting-started.md").

## Bedrock AgentCore container technical requirements

Amazon Bedrock AgentCore Runtime has different technical requirements for listing AI agents and MCP servers.

- **Agent requirements**
- **MCP server requirements**

### Agent requirements

Your containerized agent must fulfill the following core requirements:

- **/ping** Endpoint: GET endpoint for health checks
- **/invocations** Endpoint: POST endpoint for agent interactions
- **Docker Container**: ARM64 containerized deployment package
- **Port**: Container must expose port `8080` for HTTP-based agent communication

#### `/ping` - GET

This endpoint verifies that your agent is operational and ready to handle requests.

**Example Response:**

```

{
  "status": "Healthy"
}

```

#### `/invocations` - POST

This is the primary agent interaction endpoint when customers call the agent with InvokeAgentRuntime action with the payload in JSON format. InvokeAgentRuntime supports streaming responses, allowing customers to receive partial responses as they become available.

**Example Request:**

```

Content-Type: application/json
{
  "prompt": "What's the weather today?"
}

```

**Example Responses:**

- JSON response (non-streaming):

```

Content-Type: application/json
{
  "response": "Your agent's response here",
  "status": "success"
}

```

- SSE response (streaming):

```

Content-Type: text/event-stream
data: {"event": "partial response 1"}
data: {"event": "partial response 2"}
data: {"event": "final response"}

```

### MCP server requirements

Amazon Bedrock AgentCore Runtime enables you to deploy and run Model Context Protocol (MCP) servers. When you configure Amazon Bedrock AgentCore Runtime with the MCP protocol, the service expects MCP server containers at the path `0.0.0.0:8000/mcp`. This is the default path that most official MCP server SDKs support.

Because Amazon Bedrock AgentCore Runtime provides session isolation by default, it requires stateless streamable-HTTP servers. The runtime automatically adds an `Mcp-Session-Id` header for any request that doesn't include one. This allows MCP clients to maintain connection continuity to the same Amazon Bedrock AgentCore Runtime session.

The `InvokeAgentRuntime` API passes through payload data directly, which enables easy proxying of RPC messages for protocols like MCP.

Requirements:

- **Transport** - Must use stateless streamable-http only
- **Session Management** - Platform automatically adds `Mcp-Session-Id` header for session isolation
- **Host** - Container must listen on `0.0.0.0`
- **Port** - Container must expose port `8000` for MCP server communication
- **Path** - Must expose `/mcp` as a POST endpoint to receive MCP RPC messages. The `InvokeAgentRuntime` API passes through requests to this path for MCP servers.
- **Protocol** - MCP server must support the MCP protocol, including the following protocol messages:
  - `tools/list`
  - `tools/call` (supported by common frameworks like FastMCP)

To learn more about MCP server requirements, see [Deploy MCP servers in AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/runtime-mcp.md "../../../bedrock-agentcore/latest/devguide/runtime-mcp.md").

#### `/mcp` - POST

This is the primary agent interaction endpoint when customers call the MCP server with InvokeAgentRuntime.

**Example list request:**

```

Content-Type: application/json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
}

```

**Example list response:**

JSON response (non-streaming):

```

Content-Type: application/json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_weather",
        "title": "Weather Information Provider",
        "description": "Get current weather information for a location",
        "inputSchema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "City name or zip code"
            }
          },
          "required": ["location"]
        }
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}

```

**Example tool call request:**

```

Content-Type: application/json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "New York"
    }
  }
}

```

**Example tool call response:**

JSON response (non-streaming):

```

Content-Type: application/json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Current weather in New York:\nTemperature: 72°F\nConditions: Partly cloudy"
      }
    ],
    "isError": false
  }
}

```

## Testing your Bedrock AgentCore Runtime container

Before submitting your container to AWS Marketplace, test it thoroughly:

### Local Agent Testing

Test your agent locally using Docker

```

docker run -p 8080:8080 <your-container-image>

# Test ping endpoint
curl http://localhost:8080/ping

# Test agent invocation endpoint
curl -X POST http://localhost:8080/invocations \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Hello world!"}'

```

### Local MCP Server Testing

Test your MCP server locally using Docker

```

docker run -p 8000:8000 <your-container-image>

# Test ping endpoint
curl http://localhost:8000/ping

# Test MCP endpoint with tools/list
curl -X POST http://localhost:8000/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc": "2.0","id": 1,"method": "tools/list"}'

# Test MCP endpoint with tools/call
curl -X POST http://localhost:8000/mcp \
     -H "Content-Type: application/json" \
     -d '{ "jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "get_weather", "arguments": {"location": "New York"}}}'

```

### Testing on Bedrock AgentCore Runtime

After you test your container locally, upload it to Amazon Elastic Container Registry (Amazon ECR) and deploy it to Amazon Bedrock AgentCore Runtime. You can deploy using either the Amazon Bedrock AgentCore Runtime console or the AWS Command Line Interface (AWS CLI).

## Best practices for container configuration

### Security considerations

- **Isolation** - Don't store sensitive data between invocations
- **Authentication** - Validate all incoming requests
- **Logging** - Log appropriate information but avoid including sensitive data
- **Dependencies** - Keep all dependencies current to prevent security vulnerabilities

### Performance optimization

- **Cold start** - Optimize your container for fast cold starts
- **Memory Usage** - Minimize memory footprint to improve performance
- **Concurrency** - Design your agent to handle concurrent requests efficiently
- **Timeouts** - Implement proper timeout handling

### Error handling

- **Graceful degradation** - Implement fallback mechanisms for when services are unavailable
- **Structured errors** - Return well-structured error responses with appropriate HTTP status codes
- **Retry logic** - Implement appropriate retry logic for transient failures

## Requirements for AWS Marketplace submission

When you submit your AgentCore Runtime container to AWS Marketplace, include:

- **Container image** - Your container image pushed to Amazon ECR
- **Documentation** - Comprehensive documentation on how to use your agent or MCP server
- **Usage examples** - Clear examples of how to invoke your agent or MCP server
- **Support information** - Contact information for support
- **Pricing information** - Clear pricing structure for your agent or MCP server

## Additional Resources

For more information, see the following:

- [What is Amazon Bedrock AgentCore?](../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md "../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md")
- [What is AWS Marketplace?](what-is-marketplace.md "what-is-marketplace.md")
- [Getting started with container
  products](container-product-getting-started.md "container-product-getting-started.md")

## Support for AgentCore Runtime on AWS Marketplace

For questions related to listing your AgentCore Runtime container on AWS Marketplace, see [Getting support for AWS Marketplace](../buyerguide/buyer-support.md "../buyerguide/buyer-support.md").

For technical questions about AgentCore Runtime, see [AWS Support and Customer Service](https://console.aws.amazon.com/support/home#/case/create?issueType=technical "https://console.aws.amazon.com/support/home#/case/create?issueType=technical").
