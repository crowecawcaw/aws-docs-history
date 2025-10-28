# Using Amazon Q Developer with Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio has an integration with Amazon Q Developer with which you can interact with AWS
resources through a conversational interface. You can ask questions about your assets in
Amazon SageMaker Unified Studio using simple, natural language queries within the Amazon Q Developer chat interface.

For getting started flows that walk you through implementing Amazon Q Developer in Amazon SageMaker Unified Studio, see
[Getting started with Amazon Q Developer generative AI chat and
command line tools](qdeveloper-integration.md "qdeveloper-integration.md").

Amazon Q Developer provides contextual generative AI assistance through Amazon Q chat or Amazon Q CLI.
It helps data engineers, ML data developers, and other users in Amazon SageMaker Unified Studio with:

- Creating and analyzing code
- Understanding and managing workspaces
- Running AWS CLI commands
- Setting up projects and pipelines
- Creating functions for you
- Configuring Jupyter notebooks
  Amazon Q Developer implements Model Context Protocol (MCP) integration, allowing you to configure
  your MCP information when using Q chat or Q CLI. For more information about MCP integration,
  see [Using MCP with Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/qdev-mcp.md "../../../amazonq/latest/qdeveloper-ug/qdev-mcp.md").

###### Topics

- [About signing up](#q-actions-aboutsignup "#q-actions-aboutsignup")
- [Prompts](#q-actions-aboutprompts "#q-actions-aboutprompts")
- [Context files](#q-actions-contextfiles "#q-actions-contextfiles")
- [Command reference](#q-actions-commandreference "#q-actions-commandreference")
- [Region](#q-actions-region "#q-actions-region")
- [Start using Amazon Q chat](#q-actions-start-chat "#q-actions-start-chat")
- [Start using Amazon Q CLI](#q-actions-start-CLI "#q-actions-start-CLI")

## About signing up

Users in Amazon SageMaker Unified Studio can access Amazon Q Developer by signing in with their Amazon SageMaker Unified Studio SSO that is
configured for either the Amazon Q Developer Free Tier or Pro Tier. For more information, see [Amazon Q Developer pricing](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/").

For more detail about setting up Q assistance in Amazon SageMaker Unified Studio, see [Using the coding assistant](using-the-coding-assistant.md "using-the-coding-assistant.md").

## Prompts

Include relevant information in your prompts to provide additional context for more
accurate assistance.

- Your level of familiarity or expertise
- Information about your role
- A brief description of the goal or outcome for the task

## Context files

Amazon Q Developer is contextually aware of your workspace and can use additional information that
you configure, such as:

- Python development rules loaded for a developer profile
- Public sources
- MCP sources
- Custom `context.json` file

For more information about managing context, see [Context management and
profiles](../../../amazonq/latest/qdeveloper-ug/command-line-context-profiles.md "../../../amazonq/latest/qdeveloper-ug/command-line-context-profiles.md") in the _Amazon Q Developer User Guide_.

## Command reference

Amazon Q Developer includes comprehensive command reference pages:

- **Q chat command reference** (beginning with a forward
  slash)
  - Example: Use `/tools` in Q chat to to list the built in and MCP
    provided tools.
  - Documentation: [Chat
    commands](../../../amazonq/latest/qdeveloper-ug/command-line-chat-commands.md "../../../amazonq/latest/qdeveloper-ug/command-line-chat-commands.md") in the _Amazon Q Developer User
    Guide_

- **Editor command**
  - Documentation: [Using the editor command
    in the CLI](../../../amazonq/latest/qdeveloper-ug/command-line-editor.md "../../../amazonq/latest/qdeveloper-ug/command-line-editor.md") in the _Amazon Q Developer User
    Guide_

- **Q CLI command line reference**
  - Documentation: [Amazon Q CLI command
    reference](../../../amazonq/latest/qdeveloper-ug/command-line-reference.md "../../../amazonq/latest/qdeveloper-ug/command-line-reference.md") in the _Amazon Q Developer User
    Guide_

- **MCP configuration commands**
  - Documentation: [MCP configuration in the CLI](../../../amazonq/latest/qdeveloper-ug/command-line-mcp-config-CLI.md "../../../amazonq/latest/qdeveloper-ug/command-line-mcp-config-CLI.md") in the _Amazon Q Developer User
    Guide_

## Region

When you use Amazon Q Developer in Amazon SageMaker Unified Studio, your content is stored in the US East (N. Virginia)
Region and may be processed in other US Regions. For more information, access Amazon Q Developer
documentation [here](../../../amazonq/latest/qdeveloper-ug/data-storage.md "../../../amazonq/latest/qdeveloper-ug/data-storage.md") and [here](../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md "../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md").

###### Note

Amazon Q Developer in Amazon SageMaker Unified Studio only supports Amazon Q Developer profiles configured in the
US East (N. Virginia) Region.

## Start using Amazon Q chat

To start using Amazon Q Developer to chat about your project and your assets:

1. Log in to your AWS account and navigate to Amazon SageMaker Unified Studio.
2. Select the Amazon Q Developer chat interface within Amazon SageMaker Unified Studio.
3. Begin typing your query in natural language, asking Q to list Amazon SageMaker AI
   catalog assets published in the catalog. For example, you can say: "Find me data on
   sales".
4. To open JupyterLab, choose **Build**, and then choose
   **JupyterLab**. If you are in JupyterLab, you can chat with Q with
   additional Amazon Q chat contextual awareness.

For a flow that walks you through getting started with Q chat in JupyterLab, see [Getting started using Q chat](qdeveloper-integration-start-chat.md "qdeveloper-integration-start-chat.md").

Amazon Q Developer interprets your query, executes the appropriate API calls, and returns the
results directly in the chat interface.

## Start using Amazon Q CLI

To start using Amazon Q Developer to interact with Q CLI about your project and your
assets:

1. Log in to your AWS account and navigate to Amazon SageMaker Unified Studio.
2. To open JupyterLab, choose **Build**, and then choose
   **JupyterLab**.

For a flow that walks you through getting started with Q CLI in JupyterLab, see [Getting started with Q CLI](qdeveloper-integration-start-CLI.md "qdeveloper-integration-start-CLI.md").
