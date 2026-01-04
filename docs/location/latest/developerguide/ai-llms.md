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

### Client Configuration

Configure your LLM client with the MCP servers using the appropriate configuration
format for your client.

#### One-click install

- [AWS Knowledge MCP Server](https://kiro.dev/launch/mcp/add?name=aws-knowledge-mcp&config=%7B%22url%22%3A%22https%3A%2F%2Fknowledge-mcp.global.api.aws%22%2C%22type%22%3A%22http%22%7D "https://kiro.dev/launch/mcp/add?name=aws-knowledge-mcp&config=%7B%22url%22%3A%22https%3A%2F%2Fknowledge-mcp.global.api.aws%22%2C%22type%22%3A%22http%22%7D")
- [AWS API MCP Server](https://kiro.dev/launch/mcp/add?name=awslabs.aws-api-mcp-server&config=%7B%22command%22%3A%20%22uvx%22%2C%20%22args%22%3A%20%5B%22awslabs.aws-api-mcp-server%40latest%22%5D%2C%20%22disabled%22%3A%20false%2C%20%22autoApprove%22%3A%20%5B%5D%7D "https://kiro.dev/launch/mcp/add?name=awslabs.aws-api-mcp-server&config=%7B%22command%22%3A%20%22uvx%22%2C%20%22args%22%3A%20%5B%22awslabs.aws-api-mcp-server%40latest%22%5D%2C%20%22disabled%22%3A%20false%2C%20%22autoApprove%22%3A%20%5B%5D%7D")

#### Manual configuration

To add these MCP servers to your Kiro agent configuration, use the following format:

```
{
  "mcpServers": {
    "aws-knowledge-mcp-server": {
      "url": "https://knowledge-mcp.global.api.aws",
      "type": "http"
    },
    "aws-api-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-api-mcp-server@latest"],
      "env": {
        "AWS_REGION": "`us-east-1`",
        "READ_OPERATIONS_ONLY": "true"
      }
    }
  }
}
```

## Useful Context

When working with AI and LLMs on Amazon Location Service projects, providing specific context
can help guide the AI toward better solutions. We continually improve
our published documentation and guides to better direct LLMs toward current best
practices, but we are hosting and maintaining a set of useful context which can
help while model training is catching up with the latest releases from Amazon Location Service.

There is a maintained [AGENTS.md](https://github.com/aws-geospatial/amazon-location-docs-resources/tree/main/developer-tools/ai-and-llms/AGENTS.md "https://github.com/aws-geospatial/amazon-location-docs-resources/tree/main/developer-tools/ai-and-llms/AGENTS.md")
file to provide a minimal useful context for working with Amazon Location.

To add this context to your Kiro agent configuration:

1. Download the AGENTS.md file locally to your desired context path:

```
curl -o `path/to/AGENTS.md` https://raw.githubusercontent.com/aws-geospatial/amazon-location-docs-resources/main/developer-tools/ai-and-llms/AGENTS.md
```

2. Add the local file to your agent configuration:

```
{
  "resources": [
    "file://`path/to/AGENTS.md`"
  ]
}
```

## Kiro Agent Configuration

For Kiro users, here is a complete agent configuration file that includes both the recommended MCP servers and the Amazon Location Service context file:

```
{
  "name": "amazon-location-agent",
  "description": "Agent configured for Amazon Location Service development",
  "prompt": null,
  "mcpServers": {
    "aws-knowledge-mcp-server": {
      "url": "https://knowledge-mcp.global.api.aws",
      "type": "http"
    },
    "aws-api-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-api-mcp-server@latest"],
      "env": {
        "AWS_REGION": "`us-east-1`",
        "READ_OPERATIONS_ONLY": "true"
      }
    }
  },
  "tools": [
    "@builtin",
    "@aws-knowledge-mcp-server/aws___read_documentation",
    "@aws-knowledge-mcp-server/aws___recommend",
    "@aws-knowledge-mcp-server/aws___search_documentation",
    "@aws-api-mcp-server/aws___call_aws",
    "@aws-api-mcp-server/aws___suggest_aws_commands"
  ],
  "allowedTools": [
    "web_fetch",
    "web_search",
    "fs_read",
    "@aws-knowledge-mcp-server/aws___read_documentation",
    "@aws-knowledge-mcp-server/aws___recommend",
    "@aws-knowledge-mcp-server/aws___search_documentation",
    "@aws-api-mcp-server/aws___suggest_aws_commands"
  ],
  "resources": [
    "file://`path/to/amazon-location-docs-resources`/developer-tools/ai-and-llms/AGENTS.md"
  ],
  "includeMcpJson": false
}
```
