

# MCP security
<a name="command-line-mcp-security"></a>

When using MCP servers with Amazon Q Developer CLI, it's important to understand the security implications and best practices.

## Security model
<a name="command-line-mcp-security-model"></a>

The MCP security model in Amazon Q Developer CLI is designed with these principles:

1.  **Explicit Permission**: Tools require explicit user permission before execution

1.  **Local Execution**: MCP servers run locally on your machine

1.  **Isolation**: Each MCP server runs as a separate process

1.  **Transparency**: Users can see what tools are available and what they do

## Security considerations
<a name="command-line-mcp-security-considerations"></a>

Key security considerations when using MCP:
+ Only install servers from trusted sources
+ Review tool descriptions and annotations before approving
+ Use environment variables for sensitive configuration
+ Keep MCP servers and the Q CLI updated
+ Monitor MCP logs for unexpected activity