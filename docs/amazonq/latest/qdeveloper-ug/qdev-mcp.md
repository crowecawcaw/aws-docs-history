# Using MCP with Amazon Q Developer

The Model Context Protocol (MCP) is an open standard that enables AI assistants to interact with external tools and services. Amazon Q Developer CLI now supports MCP, allowing you to extend Q's capabilities by connecting it to custom tools and services.

###### Topics

- [MCP overview](qdev-mcp-overview.md "qdev-mcp-overview.md")
- [MCP configuration in the CLI](command-line-mcp-config-CLI.md "command-line-mcp-config-CLI.md")
- [MCP configuration](#mcp-configuration "#mcp-configuration")
- [Tools and prompts](#command-line-mcp-tools-prompts "#command-line-mcp-tools-prompts")
- [MCP configuration for Q Developer in the IDE](mcp-ide.md "mcp-ide.md")
- [Key benefits](#command-line-mcp-benefits "#command-line-mcp-benefits")
- [MCP architecture](#command-line-mcp-architecture "#command-line-mcp-architecture")
- [Core MCP concepts](#command-line-mcp-concepts "#command-line-mcp-concepts")
- [MCP security](command-line-mcp-security.md "command-line-mcp-security.md")

## MCP configuration

### Disabling MCP for your organization

Depending on your setup, you may have the option to disable MCP servers for your AWS account or [organization](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") in the Amazon Q Developer console. This applies if:

- You are managing an organization from your management account, or you are using a standalone account.
- You are using Amazon Q Developer in a supported IDE.

###### Note

This setting is enforced on the client side. Be aware that your end users could circumvent it.

To disable MCP in your account or organization:

1. Open the Amazon Q Developer console.
2. Choose **Settings**.
3. Under **Preferences**, choose **Edit**.
4. In the **Edit Preferences** pop-up, toggle **Model Context Protocol (MCP)**.
5. Choose **Save**.

### Setting up MCP servers with the Q CLI

The globally defined MCP configuration for Amazon Q CLI is handled at:

```
~/.aws/amazonq/cli-agents
```

Amazon Q Developer CLI supports both local MCP servers (that run as processes) and remote MCP servers (that communicate over HTTP). Remote servers can use OAuth authentication or be open with no authentication required.

For more information, see [the custom agent configuration guide on the Q CLI Github repo](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md#mcpservers-field "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md#mcpservers-field") and [Remote MCP servers](command-line-mcp-config-CLI.md#command-line-mcp-remote-servers "command-line-mcp-config-CLI.md#command-line-mcp-remote-servers").

### Setting up MCP servers with Q in the IDE

The globally defined MCP configuration for Amazon Q in the IDE is handled at:

```
~/.aws/amazonq/agents/default.json
```

For more information, see [MCP configuration for Q Developer in the IDE](mcp-ide.md "mcp-ide.md").

### MCP server loading

Amazon Q loads MCP servers in the background, allowing you to start interacting immediately without waiting for all servers to initialize. Tools become available progressively as their respective servers finish loading.

#### Checking server status

You can use the `/tools` command to see which servers are still loading and which tools are already available.

#### Configuring server initialization

You can customize the server initialization timeout using:

```
$ q settings mcp.initTimeout [value]
```

Where `[value]` is the timeout in milliseconds. This setting controls how long Amazon Q will wait for servers to initialize before allowing you to start interacting.

## Tools and prompts

This section covers how to use MCP tools and prompts with Amazon Q Developer CLI.

### Understanding MCP tools

MCP tools are executable functions that MCP servers expose to Amazon Q Developer CLI. They enable Amazon Q Developer to perform actions, process data, and interact with external systems on your behalf.

Each tool in MCP has:

- **Name**: A unique identifier for the tool
- **Description**: A human-readable description of what the tool does
- **Input Schema**: A JSON Schema defining the parameters the tool accepts
- **Annotations**: Optional hints about the tool's behavior and effects

### Discovering available tools

To see what tools are available in your Q CLI session:

```
/tools
```

This command displays all available tools, including both built-in tools and those provided by MCP servers.

Tools can have different permission levels that determine how they're used:

- **Auto-approved**: These tools can be used without explicit permission for each invocation
- **Requires approval**: These tools need your explicit permission each time they're used
- **Dangerous**: These tools are marked as potentially risky and require careful consideration before approval

### Using tools

You can use MCP tools in two ways:

1. **Natural Language Requests**: Simply describe what you want to do, and Q will determine which tool to use.
2. **Direct Tool Invocation**: You can also explicitly request Q to use a specific tool.

### Working with prompts

MCP servers can provide predefined prompts that help guide Q in specific tasks:

- List available prompts: `/prompts`
- Use a prompt:
  - `@ `prompt-name` arg1 arg2`

Example of using a prompt with arguments:

```
@fetch https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-mcp-configuration.html
```

## Key benefits

- **Extensibility**: Connect Amazon Q to specialized tools for specific domains or workflows
- **Customization**: Create custom tools tailored to your specific needs
- **Ecosystem Integration**: Leverage the growing ecosystem of MCP-compatible tools
- **Standardization**: Use a consistent protocol supported by multiple AI assistants
- **Flexibility**: MCP allows you to switch between different LLM providers while maintaining the same tool integrations
- **Security**: Keep your data within your infrastructure with local MCP servers

## MCP architecture

MCP follows a client-server architecture where:

- **MCP Hosts**: Programs like Amazon Q Developer CLI that want to access data through MCP
- **MCP Clients**: Protocol clients that maintain 1:1 connections with servers
- **MCP Servers**: Lightweight programs that each expose specific capabilities through the standardized Model Context Protocol
- **Local Data Sources**: Your computer's files, databases, and services that MCP servers can securely access
- **Remote Services**: External systems available over the internet (e.g., through APIs) that MCP servers can connect to

###### Example MCP Communication Flow

```

  User
   |
   v
+------------------+     +-----------------+     +------------------+
|                  |     |                 |     |                  |
| Amazon Q Dev     | --> | MCP Client API  | --> | MCP Server       |
|                  |     |                 |     |                  |
+------------------+     +-----------------+     +------------------+
                                                        |
                                                        v
                                                 +------------------+
                                                 |                  |
                                                 | External Service |
                                                 |                  |
                                                 +------------------+

```

Communication flow between user, Amazon Q Developer CLI, and external services through MCP

## Core MCP concepts

### Tools

Tools are executable functions that MCP servers expose to clients. They allow Amazon Q to:

- Perform actions in external systems
- Process data in specialized ways
- Interact with APIs and services
- Execute commands on your behalf

Tools are defined with a unique name, a description, an input schema (using JSON Schema), and optional annotations about the tool's behavior.

### Prompts

Prompts are predefined templates that help guide Amazon Q in specific tasks. They can:

- Accept dynamic arguments
- Include context from resources
- Chain multiple interactions
- Guide specific workflows
- Surface as UI elements (like slash commands)

### Resources

Resources represent data that MCP servers can provide to Amazon Q, such as:

- File contents
- Database records
- API responses
- Documentation
- Configuration data
