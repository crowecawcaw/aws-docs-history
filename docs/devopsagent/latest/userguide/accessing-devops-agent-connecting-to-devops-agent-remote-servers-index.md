

# Connecting to DevOps Agent Remote Servers
<a name="accessing-devops-agent-connecting-to-devops-agent-remote-servers-index"></a>

AWS DevOps Agent provides dedicated remote servers for the Model Context Protocol (MCP) and Agent-to-Agent (A2A) protocol. Use these servers to connect your IDE, CLI, or custom agent integrations to an Agent Space.

## Supported protocols
<a name="supported-protocols"></a>
+ **MCP (Model Context Protocol)** – Connect IDE and CLI clients such as Kiro, Claude Code, Cursor, and other MCP-compatible tools. For setup instructions, see [Connecting to the DevOps Agent MCP server](connecting-to-devops-agent-remote-servers-connecting-to-the-devops-agent-mcp-server.md).
+ **A2A (Agent-to-Agent) v1.0** – Connect autonomous agents for agent-to-agent communication. For protocol details, see [Integrating with the DevOps Agent A2A server](connecting-to-devops-agent-remote-servers-integrating-with-the-devops-agent-a2a-server.md).

## Endpoints
<a name="endpoints"></a>

Remote servers are available at a regional URL:

```
https://connect.aidevops.{region}.api.aws
```


| Protocol | Path | Method | 
| --- | --- | --- | 
| MCP | /mcp | POST | 
| A2A | /a2a/\* | POST | 
| A2A agent card | /.well-known/agent-card.json | GET | 

For the list of available Regions, see [Supported Regions](about-aws-devops-agent-supported-regions.md).

## Authentication and security
<a name="authentication-and-security"></a>

Both MCP and A2A endpoints share the same authentication methods (access tokens and AWS SigV4), token lifecycle, and security guidance. For setup, scoping, rotation, revocation, CloudTrail traceability, and troubleshooting, see [Authentication and security](connecting-to-devops-agent-remote-servers-authentication-and-security.md).