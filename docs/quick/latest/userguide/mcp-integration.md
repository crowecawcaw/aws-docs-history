# Model Context Protocol (MCP) integration

With Model Context Protocol (MCP) integration in Amazon Quick, you can connect to MCP servers for both task execution and data access capabilities. MCP provides a standardized way to connect AI systems with external tools and data sources.

## What you can do

With MCP integration, you can connect to MCP servers for both action execution and data access through standardized protocols.

**Action connector**

Connect to MCP servers to perform actions and execute tasks through standardized MCP protocols.

**Data access integration**

Access data sources through MCP servers to create knowledge bases and retrieve information.

## Before you begin

Before you set up MCP integration, make sure you have the following:

- MCP server endpoint with appropriate access.
- Authentication credentials for the MCP server.
- Amazon Quick Author or higher for action connectors.
- Amazon Quick Professional subscription

###### Note

MCP integration supports remote servers only. HTTP streaming is preferred over Server-Sent Events (SSE). Local stdio connections are not supported. VPC connectivity is not supported.

## Popular MCP servers

The following are examples of popular MCP servers being used with Amazon Quick and
the remote MCP server URLs:

:

| Popular MCP servers      | Provider                                                                                                            | MCP Server URL |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------- | -------------- |
| Asana                    | `https://mcp.asana.com/sse`                                                                                         |
| Atlassian                | `https://mcp.atlassian.com/v1/sse`                                                                                  |
| AWS Knowledge MCP Server | [https://knowledge-mcp.global.api.aws](https://knowledge-mcp.global.api.aws "https://knowledge-mcp.global.api.aws") |
| Box                      | `http://mcp.box.com/`                                                                                               |
| HubSpot                  | `https://mcp.hubspot.com`                                                                                           |
| HuggingFace              | `https://huggingface.co/mcp`                                                                                        |
| Intercom                 | `https://mcp.intercom.com/mcp`                                                                                      |
| Linear                   | `https://mcp.linear.app/mcp`                                                                                        |
| Monday                   | `https://mcp.monday.com/sse`                                                                                        |
| Notion                   | `https://mcp.notion.com/mcp`                                                                                        |
| PagerDuty                | `https://identity.pagerduty.com/global/oauth/anonymous/.well-known/openid-configuration`                            |
| Workato                  | `https://`MCP_ID`.apim.mcp.workato.com`                                                                             |
| Zapier                   | [https://mcp.zapier.com/MCP_ID](https://mcp.zapier.com/(unique "https://mcp.zapier.com/(unique")                    |

The proceeding table shows just some of the many MCPs supported for use with Amazon Quick.

###### Note

These servers require appropriate authentication credentials. Refer to each provider's documentation for specific authentication requirements.

## Prepare MCP server setup and authentication

Before setting up the integration in Amazon Quick, prepare your MCP server configuration and authentication credentials. MCP integration supports multiple authentication methods and configuration approaches. Choose the method that matches your MCP server requirements:

**User authentication (OAuth)**

MCP servers support two configuration approaches for OAuth authentication:

**Dynamic Client Registration (DCR)**

When your MCP server advertises Dynamic Client Registration support, no manual configuration is required. The MCP client automatically registers itself with the server and receives the necessary credentials during the connection process. This streamlined approach eliminates the need to manually gather client IDs, secrets, and endpoint URLs.

**Manual configuration**

For MCP servers that don't support DCR, gather the following information from your MCP server configuration:

- **Client ID** - OAuth client ID.
- **Client Secret** - OAuth client secret.
- **Token URL** - OAuth token endpoint.
- **Auth URL** - OAuth authorization endpoint.
- **Redirect URL** - OAuth redirect URI.

**Service authentication (Service-to-Service)**

Gather the following information from your MCP server configuration:

- **Client ID** - Service client ID.
- **Client Secret** - Service client secret.
- **Token URL** - Service token endpoint.

## Set up MCP integration

After preparing your MCP server configuration and authentication credentials, follow these steps to create your MCP integration:

1. In the Amazon Quick console, choose **Integrations**.
2. Click **Add** (plus "+" button).
3. On the Create Integration page, enter integration details:
   - **Name** - Descriptive name for your MCP integration.
   - **Description** (Optional) - Purpose of the integration.
   - **MCP server endpoint** - URL of the MCP server.

4. Click **Next**.
5. Select the authentication method (user or service).
6. Provide the appropriate configuration details.
7. Select **Create and continue**.
8. Review the integration details.
9. Select **Next**.
10. Share the integration with other users if needed.

After creating your MCP integration, a knowledge base is automatically created on completion of integration creation.

## Manage knowledge bases

After setting up your MCP integration, you can create and manage knowledge bases from your MCP data sources.

### Edit existing knowledge bases

You can modify your existing MCP knowledge bases:

1. In the Amazon Quick console, choose **Knowledge bases**.
2. Select your MCP knowledge base from the list.
3. Choose **Actions**, then choose **Edit knowledge base**.
4. Update your configuration settings as needed and choose **Save**.

### Create additional knowledge bases

You can create multiple knowledge bases from the same MCP integration:

1. In the Amazon Quick console, choose **Integrations**.
2. Choose your existing MCP integration from the list.
3. Choose **Actions**, then choose **Create knowledge base**.
4. Configure your knowledge base settings and choose **Create**.

For detailed information about knowledge base configuration options, see [Common configuration settings](knowledge-base-integrations.md#common-configuration-settings "knowledge-base-integrations.md#common-configuration-settings").

## Review integration

After you configure authentication, review the MCP integration capabilities:

1. The system connects to the MCP server and discovers available capabilities.
2. Review the list of available actions and tasks provided by the MCP server.
3. Verify data access capabilities if the MCP server provides data sources.
4. Confirm the integration configuration and capabilities.

### Capability discovery

MCP integration automatically discovers and lists:

- Available tools and actions.
- Data sources and resources.
- Supported protocols and methods.
- Server metadata and capabilities.

## Manage MCP integrations

After you create your MCP integration, you can manage it using these options:

- **Share integration** - Make the integration available to other users in your organization.
- **Review tools** - Review tools that are
  enabled.

###### Note

MCP integrations depend on the availability and configuration of the target MCP server. Changes to the server or authentication requirements may affect integration functionality.

## Limitations

When using MCP integrations in Amazon Quick, be aware of the following limitations:

- MCP operations have a fixed 60-second timeout. Operations that exceed this limit automatically fail with an HTTP 424 error.
- Custom HTTP headers are not supported in MCP operations. Only standard system headers are transmitted.
- Tool lists remain static after initial registration. You must manually refresh actions to detect server-side changes.
- Connector creation may fail if the Amazon Quick callback URI is not allow-listed by third-party providers.
- Server connectivity issues result in immediate failure without retry attempts.
