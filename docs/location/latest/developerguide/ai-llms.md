# Working with AI and LLMs

AI and LLMs can significantly accelerate development with Amazon Location Service by providing
intelligent assistance for API usage, code generation, and troubleshooting. By configuring
your LLM client with the right MCP servers and context, you can create a powerful
development assistant that understands AWS services and Amazon Location Service specifics. Using a
minimal context and MCP configuration as recommended on this page can ensure your LLM
model of choice has enough context to lead to correct results without overwhelming the
context window. This can reduce hallucinations and increase result accuracy. This
configuration also ensures that model knowledge cutoff does not impact the quality of
the results.

## Recommended MCP Servers

Model Context Protocol (MCP) servers extend LLM capabilities by providing access to
external tools, documentation, and APIs. While these MCP servers are not required,
they can help the LLM look up additional information about the service and let you
stay up to date on the latest Amazon Location Service developer guidance. For Amazon Location Service
development, the following MCP servers are recommended:

- **[aws-knowledge-mcp-server](https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server "https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server")** - Access to AWS
  documentation, API references, best practices, and knowledge bases. Does not
  require AWS credentials or authentication, making it ideal for documentation
  lookup without credential management.
- **[aws-api-mcp-server](https://awslabs.github.io/mcp/servers/aws-api-mcp-server "https://awslabs.github.io/mcp/servers/aws-api-mcp-server")** - Direct AWS API
  interactions and CLI command execution. Requires AWS credentials.

### Client Configuration

Configure your LLM client with the MCP servers using the appropriate configuration
format for your client.

Kiro

**One-click install:**

- [AWS Knowledge MCP Server](https://kiro.dev/launch/mcp/add?name=aws-knowledge-mcp&config=%7B%22url%22%3A%22https%3A%2F%2Fknowledge-mcp.global.api.aws%22%2C%22type%22%3A%22http%22%7D "https://kiro.dev/launch/mcp/add?name=aws-knowledge-mcp&config=%7B%22url%22%3A%22https%3A%2F%2Fknowledge-mcp.global.api.aws%22%2C%22type%22%3A%22http%22%7D")
- [AWS API MCP Server](https://kiro.dev/launch/mcp/add?name=awslabs.aws-api-mcp-server&config=%7B%22command%22%3A%20%22uvx%22%2C%20%22args%22%3A%20%5B%22awslabs.aws-api-mcp-server%40latest%22%5D%2C%20%22disabled%22%3A%20false%2C%20%22autoApprove%22%3A%20%5B%5D%7D "https://kiro.dev/launch/mcp/add?name=awslabs.aws-api-mcp-server&config=%7B%22command%22%3A%20%22uvx%22%2C%20%22args%22%3A%20%5B%22awslabs.aws-api-mcp-server%40latest%22%5D%2C%20%22disabled%22%3A%20false%2C%20%22autoApprove%22%3A%20%5B%5D%7D")

**Manual configuration:**

Add the following to your Kiro agent configuration. For more information about
[Kiro configuration](https://kiro.dev/docs/mcp/configuration/ "https://kiro.dev/docs/mcp/configuration/"), see the Kiro documentation.

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

VSCode with Copilot

**One-click install:**

- [AWS Knowledge MCP Server](https://vscode.dev/redirect/mcp/install?name=aws-knowledge-mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fknowledge-mcp.global.api.aws%22%7D "https://vscode.dev/redirect/mcp/install?name=aws-knowledge-mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fknowledge-mcp.global.api.aws%22%7D")
- [AWS API MCP Server](https://insiders.vscode.dev/redirect/mcp/install?name=AWS%20API%20MCP%20Server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22awslabs.aws-api-mcp-server%40latest%22%5D%2C%22env%22%3A%7B%22AWS_REGION%22%3A%22us-east-1%22%7D%2C%22type%22%3A%22stdio%22%7D "https://insiders.vscode.dev/redirect/mcp/install?name=AWS%20API%20MCP%20Server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22awslabs.aws-api-mcp-server%40latest%22%5D%2C%22env%22%3A%7B%22AWS_REGION%22%3A%22us-east-1%22%7D%2C%22type%22%3A%22stdio%22%7D")

**Manual configuration:**

Add the following to your VSCode mcp.json file. For more information about
[MCP servers in VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers "https://code.visualstudio.com/docs/copilot/customization/mcp-servers"), see the VSCode documentation.

```
{
  "servers": {
    "aws-knowledge-mcp-server": {
      "type": "http",
      "url": "https://knowledge-mcp.global.api.aws"
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

VSCode with Cline

**Manual configuration:**

Add the following to your Cline MCP settings file (cline_mcp_settings.json). For more information about
[Cline MCP configuration](https://docs.cline.bot/mcp/configuring-mcp-servers "https://docs.cline.bot/mcp/configuring-mcp-servers"), see the Cline documentation.

```
{
  "mcpServers": {
    "aws-knowledge-mcp-server": {
      "type": "streamableHttp",
      "url": "https://knowledge-mcp.global.api.aws"
    },
    "aws-api-mcp-server": {
      "type": "stdio",
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

Cursor

**Manual configuration:**

Add the following to your Cursor mcp.json file. For more information about
[Cursor MCP configuration](https://cursor.com/docs/context/mcp "https://cursor.com/docs/context/mcp"), see the Cursor documentation.

```
{
  "mcpServers": {
    "aws-knowledge-mcp-server": {
      "url": "https://knowledge-mcp.global.api.aws"
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

Claude Code

**Manual configuration:**

Add MCP servers using the Claude CLI commands. For more information about
[Claude Code MCP setup](https://code.claude.com/docs/en/mcp "https://code.claude.com/docs/en/mcp"), see the Claude Code documentation.

```
# Add AWS Knowledge MCP Server (HTTP)
claude mcp add --transport http aws-knowledge-mcp-server https://knowledge-mcp.global.api.aws

# Add AWS API MCP Server (stdio)
claude mcp add --transport stdio aws-api-mcp-server -- uvx awslabs.aws-api-mcp-server@latest
```

Gemini Code Assist

**Manual configuration:**

Add the following to your Gemini settings JSON file (~/.gemini/settings.json). For more information about
[Gemini Code Assist MCP configuration](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer#configure-mcp-servers "https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer#configure-mcp-servers"), see the Google Cloud documentation.

```
{
  "mcpServers": {
    "aws-knowledge-mcp-server": {
      "httpUrl": "https://knowledge-mcp.global.api.aws"
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

To use this context file, first download it locally:

```
curl -o `path/to/AGENTS.md` https://raw.githubusercontent.com/aws-geospatial/amazon-location-docs-resources/main/developer-tools/ai-and-llms/AGENTS.md
```

Then configure your LLM client to use the downloaded file:

Kiro

Add the local file to your agent configuration:

```
{
  "resources": [
    "file://`path/to/AGENTS.md`"
  ]
}
```

VSCode with Copilot

Place the downloaded AGENTS.md file at the root of your workspace. VSCode will automatically apply the instructions to all chat requests. To enable this feature, ensure the [chat.useAgentsMdFile](vscode://settings/chat.useAgentsMdFile "vscode://settings/chat.useAgentsMdFile") setting is enabled. For more information, see [custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions "https://code.visualstudio.com/docs/copilot/customization/custom-instructions") in the VSCode documentation.

VSCode with Cline

Place the downloaded AGENTS.md file in your project root or use @ mentions to reference it in your conversations. Cline will automatically discover project files and you can reference the context using `@AGENTS.md` in your prompts. For more information about [context management](https://docs.cline.bot/prompting/understanding-context-management "https://docs.cline.bot/prompting/understanding-context-management"), see the Cline documentation.

Cursor

Use @ mentions to reference the downloaded AGENTS.md file in your conversations. You can reference files using `@Files & Folders` and then search for the AGENTS.md file, or drag the file directly into the chat. For more information about [@ mentions](https://cursor.com/docs/context/mentions "https://cursor.com/docs/context/mentions"), see the Cursor documentation.

Claude Code

Add the downloaded AGENTS.md file to your project directory. You can include it in your project's CLAUDE.md file or reference it directly in your current session. For more information about [Claude Code MCP setup](https://code.claude.com/docs/en/mcp "https://code.claude.com/docs/en/mcp"), see the Claude Code documentation.

Gemini Code Assist

Create a GEMINI.md file in your project root or ~/.gemini/GEMINI.md for global context, and include the contents of the downloaded AGENTS.md file. For more information about [context files](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer#create-a-context-file "https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer#create-a-context-file"), see the Google Cloud documentation.

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
