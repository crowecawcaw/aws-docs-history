

# Snowflake Cortex Agent integration
<a name="snowflake-integration"></a>

**Note**  
This guide covers an integration validated with a third-party MCP server. Snowflake manages the setup and availability of the Cortex Agent MCP server.

With the Snowflake Cortex Agent connector, you can query Snowflake data and run AI-powered analytics through Cortex Agent directly in Amazon Quick via Model Context Protocol (MCP) server connectivity.

Snowflake Cortex Agent uses MCP server connectivity. To set up this integration, complete the following two steps. First, enable the Cortex Agent MCP server in your Snowflake account and obtain the server endpoint URL. Then, create the integration in Amazon Quick. For more information about Snowflake's Cortex Agent MCP server, see [Cortex Agents MCP server](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) in the Snowflake documentation.

## Prerequisites
<a name="snowflake-integration-prerequisites"></a>

Before you set up the integration, make sure that you have the following resources and access.
+ An active Snowflake account with Cortex Agent enabled and the Cortex Agent MCP server configured. For information about enabling the Cortex Agent MCP server, see [Cortex Agents MCP server](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) in the Snowflake documentation.
+ The MCP server endpoint URL from your Snowflake account.
+ Appropriate roles, warehouses, databases, and schemas configured in your Snowflake account for the operations you want to perform.
+ For information about subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Set up the integration in Amazon Quick
<a name="snowflake-integration-setup"></a>

After you verify your Snowflake account and obtain the MCP server endpoint, create the integration in Amazon Quick.

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Snowflake Cortex Agent**.

1. On the **Connect to Snowflake Cortex Agent** page, enter the following fields:
   + **Name** – A descriptive name for your Snowflake Cortex Agent connector.
   + **Description** (Optional) – Notes about how you plan to use this connection.
   + **MCP server endpoint** – The Cortex Agent MCP server endpoint URL from your Snowflake account. Example: `https://mcp.example.com/sse`.
   + **Connection type** – Choose **Public network**.

1. Choose **Next**.

1. If the Cortex Agent MCP server requires authentication, Amazon Quick uses MCP OAuth discovery to handle the sign-in flow. If a Snowflake sign-in popup appears, enter your Snowflake credentials and grant the requested permissions. For more information about how Amazon Quick handles MCP authentication, see [Prepare MCP server setup and authentication](mcp-integration.md#mcp-integration-authentication).

1. On the **Review** page, Amazon Quick discovers the tools that Cortex Agent exposes and displays them in a table. Review the list of available actions and choose **Next**.

1. (Optional) On the **Share integration** page, search for teams or groups to share the integration with.

1. Choose **Done**.

The integration appears in the **Existing actions** panel with a status of **Available**.

## Available actions
<a name="snowflake-integration-actions"></a>

After you set up the integration, the actions exposed by Snowflake Cortex Agent are available. To see the current set of actions for your connector, go to the connector's **Available actions** view in the Amazon Quick console.

## Manage and troubleshoot
<a name="snowflake-integration-troubleshooting"></a>

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations). For general MCP integration troubleshooting, see [Troubleshooting](mcp-integration.md#mcp-integration-troubleshooting).