# MCP protocol contract

Understand the requirements for implementing the Model Context Protocol (MCP)
so that agents can call tools and agent servers.

For example code, see [Deploy MCP servers in AgentCore Runtime](runtime-mcp.md "runtime-mcp.md").

###### Topics

- [Protocol implementation requirements](#protocol-implementation-requirements "#protocol-implementation-requirements")
- [Container requirements](#container-requirements-mcp "#container-requirements-mcp")
- [Path requirements](#path-requirements-mcp "#path-requirements-mcp")

## Protocol implementation requirements

Your MCP server must implement these specific protocol requirements:

- **Transport**: Stateless streamable-http only

* Ensures compatibility with AWS's session management and load
  balancing

- **Session Management**: Platform
  automatically adds `Mcp-Session-Id` header for session isolation,
  servers must support stateless operation so as to not reject platform
  generated `Mcp-Session-Id` header

## Container requirements

Your MCP server must be deployed as a containerized application meeting these
specifications:

- **Host**: `0.0.0.0`
- **Port**: `8000` - Standard port
  for MCP server communication (different from HTTP protocol)
- **Platform**: ARM64 container - Required for
  compatibility with AWS Amazon Bedrock AgentCore runtime environment

## Path requirements

### /mcp - POST

###### Purpose

Receives MCP RPC messages and processes them through your agent's tool
capabilities, complete pass-through of [InvokeAgentRuntime](../APIReference/API_InvokeAgentRuntime.md "../APIReference/API_InvokeAgentRuntime.md") API payload with standard MCP RPC
messages

###### Response format

JSON-RPC based request/response format, supporting both
`application/json` and `text/event-stream` as
response content-types

###### Use cases

The `/mcp` endpoint serves several key purposes:

- Tool invocation and management
- Agent capability discovery
- Resource access and manipulation
- Multi-step agent workflows
