# Understand the available interfaces for using

Amazon Bedrock AgentCore

Amazon Bedrock AgentCore supports various interfaces for developing and deploying your agent
code. The simplest approach is to use the AgentCore Python SDK to create your agent code and use
the AgentCore starter toolkit to deploy your agent.

The AgentCore starter toolkit and AgentCore Python SDK don't support all AgentCore
operations that the AWS SDK supplies. If they don't support a specific AgentCore
operation, use the AWS SDK.

###### Topics

- [Amazon Bedrock AgentCore
  starter toolkit](#bedrock-agentcore-configure-deploy-starter-toolkit "#bedrock-agentcore-configure-deploy-starter-toolkit")
- [AgentCore Python SDK](#develop-agents-bedroock-agentcore-sdk "#develop-agents-bedroock-agentcore-sdk")
- [Amazon Bedrock AgentCore MCP
  server](#develop-agents-bedroock-agentcore-mcp-server "#develop-agents-bedroock-agentcore-mcp-server")
- [AWS SDK](#develop-agents-bedrock-agentcore-aws-sdk "#develop-agents-bedrock-agentcore-aws-sdk")
- [Amazon Bedrock AgentCore
  console](#develop-agents-console "#develop-agents-console")
- [AWS Command Line Interface](#bedrock-agentcore-configure-deploy-cli "#bedrock-agentcore-configure-deploy-cli")

## Amazon Bedrock AgentCore

starter toolkit

The [AgentCore starter toolkit](https://github.com/aws/bedrock-agentcore-starter-toolkit "https://github.com/aws/bedrock-agentcore-starter-toolkit") provides CLI tools and higher-level
abstractions for:

- _Create_: Set up a skeleton agent project with your preferred framework and model provider
- _Deployment_: Containerize and deploy agents to AWS
  infrastructure
- _Import Agent_: Migrate existing Bedrock Agents to
  AgentCore with framework conversion
- _Gateway Integration_: Create and manage gateways for agent
  tools using the CLI
- _Memory Management_: Create and manage memory for
  agents
- _Configuration Management_: Manage environment and
  deployment settings
- _Observability_: Monitor agents in production
  environments
- _AgentCore Evaluations_: Assess agent performance and quality

The getting started instructions in this guide use the AgentCore starter
toolkit.

## AgentCore Python SDK

The [AgentCore Python SDK](https://github.com/aws/bedrock-agentcore-sdk-python "https://github.com/aws/bedrock-agentcore-sdk-python") provides Python primitives for agent
development with built-in support for:

- _Runtime_: Lightweight wrapper over the AgentCore
  operations in the AWS SDK that lets you easily write Python
  code for an agent.
- _Memory_: Persistent storage for conversation history and
  agent context
- _Tools_: Built-in clients for code interpretation and
  browser automation
- _Identity_: Secure authentication and access
  management
- _AgentCore Evaluations_: Automated assessment tools for measuring agent performance

The AgentCore Python SDK supports multiple frameworks, such as Strands Agents and
LangGraph. If you are using other AWS services, you'll need to use
the AWS SDK to integrate those services into your agent, alongside your AgentCore Python SDK
code.

## Amazon Bedrock AgentCore MCP

server

The AgentCore Model Context Protocol (MCP) server helps you transform, deploy,
and test AgentCore-compatible agents directly from your preferred development
environment. With built-in support for runtime integration, gateway connectivity, and
agent lifecycle management, the MCP server simplifies moving from local development to
production deployment on AgentCore services.

The MCP server works with popular MCP clients including Kiro, Cursor, Claude Code, and
Amazon Q CLI, providing conversational commands to automate complex agent development
workflows.

For more information, see [Amazon Bedrock AgentCore MCP Server: Vibe coding with your coding assistant](mcp-getting-started.md "mcp-getting-started.md").

## AWS SDK

You can use the AWS SDK to achieve the same results as the AgentCore Python SDK, as well as
other tasks that the AgentCore Python SDK doesn't support. You'll need to use the AWS SDK to
interact with other AWS services such as AWS Lambda and Amazon S3. You'll also need to the
AWS SDK if you aren't using Python as your coding language.

To configure and deploy an agent, you use the [AgentCore control plane
API](../../../bedrock-agentcore-control/latest/APIReference/Welcome.md "../../../bedrock-agentcore-control/latest/APIReference/Welcome.md"). For example, you can create an AgentCore Runtime or create an
AgentCore Memory.

At runtime, you use the [AgentCore data plane
API](../APIReference/Welcome.md "../APIReference/Welcome.md") for tasks such as adding a memory event to an AgentCore Memory. The client
code that calls your agent uses the `InvokeAgentRuntime` data plane operation
to invoke an agent that you have hosted in an AgentCore Runtime.

## Amazon Bedrock AgentCore

console

You can use the AgentCore console to create and manage the AgentCore
services that your agent code uses. You can get code snippets that show to call an agent
hosted in an AgentCore Runtime. You can also test your agent in the agent sandbox. Open
the console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").

## AWS Command Line Interface

You can use the AWS CLI with the AgentCore services that you use. Use [control plane api](../../../cli/latest/reference/bedrock-agentcore-control.md "../../../cli/latest/reference/bedrock-agentcore-control.md") to create and manage services. For example you can create
an AgentCore Memory or update the endpoint for an AgentCore Runtime. You can also perform
runtime actions with the [data plane API](../../../cli/latest/reference/bedrock-agentcore.md "../../../cli/latest/reference/bedrock-agentcore.md"), which can be
useful for testing an agent.
