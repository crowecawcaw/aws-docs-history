# Working with AI and LLMs

AI and LLMs can significantly accelerate development with Amazon Location Service by providing
intelligent assistance for API usage, code generation, and troubleshooting. By configuring
your LLM client with the right MCP servers and context, you can create a powerful
development assistant that understands AWS services and Amazon Location Service specifics.

## Recommended MCP Servers

Model Context Protocol (MCP) servers extend LLM capabilities by providing access to
external tools, documentation, and APIs. While these MCP servers are not required,
they can help the LLM look up additional information about the service and let you
stay up to date on the latest Amazon Location Service developer guidance. For Amazon Location Service
development, the following MCP servers are recommended:

- **aws-knowledge-mcp-server** - Access to AWS
  documentation, API references, best practices, and knowledge bases. Does not
  require AWS credentials or authentication, making it ideal for documentation
  lookup without credential management.
  [Learn more](https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server "https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server")
- **aws-api-mcp-server** - Direct AWS API
  interactions and CLI command execution. Requires AWS credentials.
  [Learn more](https://awslabs.github.io/mcp/servers/aws-api-mcp-server "https://awslabs.github.io/mcp/servers/aws-api-mcp-server")

You can use either server individually or both together for comprehensive functionality.
