

# Overview
<a name="agent-access-mcp-server-overview"></a>

This section explains how to connect to and operate the WorkSpaces Applications Model Context Protocol (MCP) server, the endpoint your agent uses to work in a desktop session. For a conceptual overview of WorkSpaces for AI agents and agent access, see [Why WorkSpaces for AI agents?](agent-access-learn-more.md) and [How it works](agent-access-concepts.md).

An agent works with the MCP server in four stages:

1. **Authenticate**. The agent authenticates to the MCP server before it can connect.

1. **Initiate the connection**. The agent opens a session and retrieves the list of available tools.

1. **Make tool calls**. The agent calls tools to operate the desktop, such as moving the mouse, typing, or taking a screenshot.

1. **End the session**. The agent ends the session when the task is complete.

Throughout these stages, WorkSpaces Applications handles the connection between the MCP calls and the underlying desktop. The topics in this section describe each stage. To authenticate and open a connection, see [Connecting to the MCP server](agent-access-mcp-server-endpoint.md). For the tools your agent can call, see [Available tools](agent-access-mcp-server-tools.md). To end a session, see [Session cleanup](agent-access-mcp-server-session-cleanup.md).

You enable agent access when you create a stack, using the WorkSpaces Applications console, AWS CLI, or API. Before you connect an agent, review [Prerequisites](agent-access-mcp-prerequisites.md).