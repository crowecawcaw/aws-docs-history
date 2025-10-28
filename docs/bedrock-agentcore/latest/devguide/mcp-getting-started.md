# Amazon Bedrock AgentCore MCP Server: Vibe coding with your coding assistant

The Amazon Bedrock AgentCore Model Context Protocol (MCP) server helps you transform, deploy, and test Amazon Bedrock AgentCore-compatible agents directly from your preferred development environment. With built-in support for runtime integration, gateway connectivity, and agent lifecycle management, the MCP server simplifies moving from local development to production deployment on Amazon Bedrock AgentCore services.

The MCP server works with popular MCP clients including Kiro, Cursor, Claude Code, and Amazon Q CLI, providing conversational commands to automate complex agent development workflows.

###### Topics

- [Prerequisites](#mcp-prerequisites "#mcp-prerequisites")
- [Step 1: Install the MCP server](#mcp-install-server "#mcp-install-server")
- [Step 2: Transform an existing agent for AgentCore runtime](#mcp-transform-agent "#mcp-transform-agent")
- [Step 3: Deploy your agent to AgentCore runtime](#mcp-deploy-agent "#mcp-deploy-agent")
- [Step 4: Test your deployed agent](#mcp-test-agent "#mcp-test-agent")
- [Next steps](#mcp-next-steps "#mcp-next-steps")

## Prerequisites

Before you begin, verify that you have the following:

- An AWS account with Amazon Bedrock AgentCore permissions
- AWS CLI installed and configured with appropriate credentials. For setup instructions, see [Installing or updating to the latest version of the AWS CLI](../../../amazonq/latest/qdeveloper-ug/command-line-installing.md "../../../amazonq/latest/qdeveloper-ug/command-line-installing.md").
- One of the supported MCP clients:
  - Kiro
  - Cursor
  - Claude Code
  - Amazon Q CLI

- An existing AgentCore agent built with a supported framework (Strands Agents, LangGraph, CrewAI, or similar)

For more information about Amazon Bedrock AgentCore, see the [Amazon Bedrock AgentCore documentation](../../../bedrock-agentcore.md "../../../bedrock-agentcore.md").

### Install required dependencies

Install the necessary packages for Amazon Bedrock AgentCore development.

To install the required packages, run the following commands:

```

# Install AgentCore dependencies
pip install bedrock-agentcore
pip install bedrock-agentcore-starter-toolkit

```

## Step 1: Install the MCP server

To install the AgentCore MCP server, add it to your MCP client's configuration file. Each MCP client stores this configuration in a different location.

### Add MCP server configuration

Choose your MCP client and add the corresponding configuration:

#### For Kiro

Add to `.kiro/settings/mcp.json` (if it doesn't exist, see
[Creating Configuration Files](https://kiro.dev/docs/mcp/configuration/#creating-configuration-files "https://kiro.dev/docs/mcp/configuration/#creating-configuration-files") ):

```
{
  "mcpServers": {
    "bedrock-agentcore-mcp-server": {
      "command": "uvx",
      "args": [
        "awslabs.amazon-bedrock-agentcore-mcp-server@latest"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "search_agentcore_docs",
        "fetch_agentcore_doc"
      ]
    }
  }
}

```

#### For Cursor

Add to `.cursor/mcp.json`:

```

{
  "mcpServers": {
    "bedrock-agentcore-mcp-server": {
      "command": "uvx",
      "args": [
        "awslabs.amazon-bedrock-agentcore-mcp-server@latest"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "search_agentcore_docs",
        "fetch_agentcore_doc"
      ]
    }
  }
}

```

#### For Amazon Q

The best practice is to configure MCP servers for individual Q CLI agents. For configuration instructions, see [Configuring MCP servers for Amazon Q CLI](../../../amazonq/latest/qdeveloper-ug/command-line-mcp-config-CLI.md "../../../amazonq/latest/qdeveloper-ug/command-line-mcp-config-CLI.md").

For Amazon Q in IDEs (VS Code and JetBrains), see [Using MCP servers with Amazon Q in your IDE](../../../amazonq/latest/qdeveloper-ug/mcp-ide.md "../../../amazonq/latest/qdeveloper-ug/mcp-ide.md").

#### For Claude Code

Configuration depends on your installation:

- **Standalone app**: Add to `~/.claude/mcp.json`
- **VS Code extension**: Configure MCP servers through the Claude Code CLI first, then the extension will automatically use them. See the [Claude Code VS Code documentation](https://docs.claude.com/en/docs/claude-code/vs-code "https://docs.claude.com/en/docs/claude-code/vs-code") for setup details.

For standalone Claude Code app:

```
{
  "mcpServers": {
    "bedrock-agentcore-mcp-server": {
      "command": "uvx",
      "args": [
        "awslabs.amazon-bedrock-agentcore-mcp-server@latest"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "search_agentcore_docs",
        "fetch_agentcore_doc"
      ]
    }
  }
}

```

### Verify MCP server installation

To verify that the MCP server is connected and working successfully, restart your MCP client after adding the configuration and confirm that the following tools are available:

- `search_agentcore_docs` - Search Amazon Bedrock AgentCore documentation
- `fetch_agentcore_doc` - Fetch specific Amazon Bedrock AgentCore documentation pages

## Step 2: Transform an existing agent for AgentCore runtime

To make your existing AgentCore agent code compatible with Amazon Bedrock AgentCore Runtime, use the MCP server to guide the transformation process. For example, if you have a Strands AgentCore agent, the transformation helps convert it to be Amazon Bedrock AgentCore-compatible by updating imports, dependencies, and application structure.

### Transform your agent code

The MCP server guides your MCP client to make the following changes to your AgentCore agent code:

#### Add runtime library imports

The MCP server adds the required AgentCore imports:

```

from bedrock_agentcore.runtime import BedrockAgentCoreApp

```

#### Update dependencies

The MCP server updates your `requirements.txt` file:

```

bedrock-agentcore
strands-agents

```

#### Initialize the AgentCore application

The MCP server adds application initialization:

```

app = BedrockAgentCoreApp()

```

#### Decorate the main entrypoint

The MCP server converts your handler function:

```

@app.entrypoint
def handler(event, context):
    # Your agent logic here
    pass

```

#### Add application runner

The MCP server adds the application runner:

```

if __name__ == "__main__":
    app.run()

```

### Transformation procedure

To transform your AgentCore agent, open your existing AgentCore agent file (for example, `weather_agent.py`) in your MCP client and use your MCP client's AI assistant with the following prompt:

```

Transform this AgentCore agent code to be compatible with AgentCore runtime. Update the imports, dependencies, and application structure as needed.

```

## Step 3: Deploy your agent to AgentCore runtime

After you transform your AgentCore agent for AgentCore compatibility, deploy it using the AgentCore CLI through your MCP client.

### Deploy using the AgentCore CLI

The MCP server uses the AgentCore CLI to deploy your AgentCore agent. The deployment process includes:

- Creating the deployment configuration
- Building and containerizing the AgentCore agent
- Deploying to Amazon Bedrock AgentCore Runtime
- Providing the deployment details and AgentCore agent ARN

To deploy your AgentCore agent, use your MCP client's AI assistant with the following prompt:

```

Deploy this AgentCore agent to AgentCore runtime using the AgentCore CLI.

```

The MCP server executes the necessary CLI commands automatically.

### Verify deployment

After deployment completes, you receive confirmation with the following details:

- AgentCore agent ARN
- Runtime configuration
- Deployment status

## Step 4: Test your deployed agent

Test your deployed AgentCore agent by invoking it through Amazon Bedrock AgentCore Runtime.

### Invoke the agent

The MCP server uses the AgentCore CLI to invoke your AgentCore agent and display results including:

- AgentCore agent response
- Execution logs
- Performance metrics

To test your deployed AgentCore agent, use your MCP client's AI assistant with the following prompt:

```

Test the deployed AgentCore agent with a sample request.

```

Review the invocation output:

```

AgentCore Agent Response: Hello! I can help you with weather information.
Execution Time: 1.2s
Status: Success

```

## Next steps

After you successfully deploy and test your first AgentCore agent with the AgentCore MCP server, you can explore additional capabilities:

- _Tool integration_ - Connect your AgentCore agent to Amazon Bedrock AgentCore Gateway for external tool access
- _Memory integration_ - Add Amazon Bedrock AgentCore Memory for conversation context
- _Identity management_ - Implement Amazon Bedrock AgentCore Identity for secure access control
- _Advanced frameworks_ - Explore integration with LangGraph, CrewAI, and other frameworks

For more information, see the following:

- [Get started with AgentCore Runtime](runtime-getting-started.md "runtime-getting-started.md")
- [Get started with AgentCore Gateway](gateway-quick-start.md "gateway-quick-start.md")
- [AgentCore CLI reference](https://aws.github.io/bedrock-agentcore-starter-toolkit/api-reference/cli.html "https://aws.github.io/bedrock-agentcore-starter-toolkit/api-reference/cli.html")
