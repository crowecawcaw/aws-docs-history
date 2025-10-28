# MCP security

When using MCP servers with Amazon Q Developer CLI, it's important to understand the security implications and best practices.

## Security model

The MCP security model in Amazon Q Developer CLI is designed with these principles:

1. **Explicit Permission**: Tools require explicit user permission before execution
2. **Local Execution**: MCP servers run locally on your machine
3. **Isolation**: Each MCP server runs as a separate process
4. **Transparency**: Users can see what tools are available and what they do

## Security considerations

Key security considerations when using MCP:

- Only install servers from trusted sources
- Review tool descriptions and annotations before approving
- Use environment variables for sensitive configuration
- Keep MCP servers and the Q CLI updated
- Monitor MCP logs for unexpected activity
