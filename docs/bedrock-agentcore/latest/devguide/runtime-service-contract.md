# Understand the AgentCore Runtime service

contract

The AgentCore Runtime service contract defines the standardized communication protocol that
your agent application must implement to integrate with the Amazon Bedrock agent hosting
infrastructure. This contract ensures seamless communication between your custom agent code
and AWS's managed hosting environment.

## Supported protocols

The AgentCore Runtime service contract supports the following communication
protocols:

- [HTTP](runtime-http-protocol-contract.md "runtime-http-protocol-contract.md"): Direct REST API
  endpoints for traditional request/response patterns
- [MCP](runtime-mcp-protocol-contract.md "runtime-mcp-protocol-contract.md"): Model Context
  Protocol for tools and agent servers
- [A2A](runtime-a2a-protocol-contract.md "runtime-a2a-protocol-contract.md"): Agent-to-Agent
  protocol for multi-agent communication and discovery

## Compare supported protocols

Compare the A2A, HTTP, and MCP protocols to understand the differences and use
cases.

| Protocol Comparison | Feature                                                                | HTTP Protocol    | MCP Protocol                 | A2A Protocol |
| ------------------- | ---------------------------------------------------------------------- | ---------------- | ---------------------------- | ------------ |
| **Port**            | 8080                                                                   | 8000             | 9000                         |
| **Mount Path**      | /invocations (HTTP), /ws (WebSocket)                                   | /mcp             | / (root)                     |
| **Message Format**  | REST JSON/SSE, WebSocket (text/binary)                                 | JSON-RPC         | JSON-RPC 2.0                 |
| **Discovery**       | N/A                                                                    | Tool listing     | Agent Cards                  |
| **Authentication**  | SigV4, OAuth 2.0; WebSocket supports SigV4 by headers and query params | SigV4, OAuth 2.0 | SigV4, OAuth 2.0             |
| **Use Case**        | Direct API calls, real-time streaming                                  | Tool servers     | Agent-to-agent communication |

###### Topics

- [HTTP protocol contract](runtime-http-protocol-contract.md "runtime-http-protocol-contract.md")
- [MCP protocol contract](runtime-mcp-protocol-contract.md "runtime-mcp-protocol-contract.md")
- [A2A protocol contract](runtime-a2a-protocol-contract.md "runtime-a2a-protocol-contract.md")
