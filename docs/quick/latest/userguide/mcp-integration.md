# Model Context Protocol (MCP) integration

Model Context Protocol (MCP) is an open standard that defines how AI applications communicate with external tools and data sources. MCP uses a client-server architecture. AI applications act as clients that connect to MCP servers. Each MCP server exposes a set of tools. These tools are structured operations that the AI application can invoke to perform tasks, such as querying databases, calling APIs, or interacting with third-party services.

With MCP integration in Amazon Quick, you can connect to remote MCP servers so that your AI assistant can use the tools that those servers provide. For example, you can connect to an MCP server that provides access to your project management system. This connection allows the assistant to create tickets, look up issues, or update statuses as part of a conversation. Because MCP is an open standard, you can connect to any compatible server without building custom integrations for each tool.

## What you can do

MCP integration registers MCP server tools as actions in Amazon Quick.

**Action connector**

Each tool that is exposed by an MCP server is registered as an action that your AI assistant can invoke during conversations. The integration secures these connections by using Proof Key for Code Exchange (PKCE) with the S256 challenge method and Resource Indicators (RFC 8707) to bind access tokens to specific MCP servers.

## Before you begin

Before you set up MCP integration, make sure that you have the following:

- An MCP server endpoint with appropriate access.
- Authentication credentials for the MCP server, if required. For more information, see [Prepare MCP server setup and authentication](#mcp-integration-authentication "#mcp-integration-authentication").
- An Amazon Quick Enterprise subscription.

###### Note

MCP integration supports remote servers only. HTTP streaming is preferred over Server-Sent Events (SSE). Local stdio connections and VPC connectivity are not supported.

## Prepare MCP server setup and authentication

When you connect to an MCP server, Amazon Quick uses OAuth 2.0 Protected Resource Metadata (RFC 9728) to automatically discover authorization server information. The client sends an initial unauthenticated request to the MCP server. If the server responds with a 401 status that contains a `WWW-Authenticate` header with a `resource_metadata` URL, then Amazon Quick uses that URL to fetch the metadata document. If the header is not present, Amazon Quick falls back to the well-known URI at the server root.

If the authorization server supports Dynamic Client Registration (DCR), Amazon Quick automatically registers itself by using the discovered `registration_endpoint` from the authorization server metadata. No manual credential configuration is required. Both confidential and public client flows are supported. DCR applies regardless of the authentication method that you choose.

If the authorization server does not support DCR, you must manually provide credentials. Choose the authentication method that matches your MCP server requirements.

**User authentication (OAuth)**

Gather the following information from your MCP server configuration:

- **Client ID** – The OAuth client ID.
- **Client Secret** – The OAuth client secret.
- **Token URL** – The OAuth token endpoint.
- **Authorization URL** – The OAuth authorization endpoint.
- **Redirect URL** – The OAuth redirect URI.

**Service authentication (Service-to-Service)**

Gather the following information from your MCP server configuration:

- **Client ID** – The service client ID.
- **Client Secret** – The service client secret.
- **Token URL** – The service token endpoint.

**No authentication**

If the MCP server does not require authentication, no credentials are needed. Select this option for MCP servers that allow unauthenticated access.

## Set up MCP integration

After you prepare your MCP server configuration and authentication credentials, create your MCP integration.

1. In the Amazon Quick console, choose **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Model Context Protocol (MCP)**.
4. On the **Create Integration** page, enter the integration details:
   - **Name** – A descriptive name for your MCP integration.
   - **Description** (Optional) – The purpose of the integration.
   - **MCP server endpoint** – The URL of the MCP server.

5. Choose **Next**.
6. Select the authentication method (user, service, or no authentication).
7. Provide the appropriate configuration details.
8. Choose **Create and continue**.
9. Review the integration details.
10. Choose **Next**.
11. Share the integration with other users if needed.

After you create your MCP integration, the available tools are discovered and registered as actions.

## Review integration

After you configure authentication, review the MCP integration capabilities:

1. The system connects to the MCP server and discovers available capabilities.
2. Review the list of available actions and tasks that the MCP server provides.
3. Confirm the integration configuration and capabilities.

### Capability discovery

During the connection process that is described in [Prepare MCP server setup and authentication](#mcp-integration-authentication "#mcp-integration-authentication"), Amazon Quick also discovers and registers the tools that are available on the MCP server. After discovery completes, each tool is listed as an action that you can review and turn on.

## Manage MCP integrations

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

## Limitations

When you use MCP integrations in Amazon Quick, be aware of the following limitations:

- MCP operations have a fixed 60-second timeout. Operations that exceed this limit automatically fail with an HTTP 424 error.
- Custom HTTP headers are not supported in MCP operations. Only standard system headers are transmitted.
- Tool lists remain static after initial registration. To pick up server-side tool changes, you must delete the integration and recreate it.
- Connector creation might fail if the Amazon Quick callback URI is not allow-listed by third-party providers.
- Server connectivity issues result in immediate failure without retry attempts.
- Step-up authorization is not supported. If an MCP server requires additional scopes after the initial authorization (HTTP 403 with `insufficient_scope`), you must re-authorize the entire connection. Incremental permission upgrades are not available.
- Scope handling has the following limitations:
  - Amazon Quick does not extract the `scope` parameter from the server's initial 401 `WWW-Authenticate` challenge. Scopes are determined from the Protected Resource Metadata document instead.
  - When the metadata does not specify supported scopes, Amazon Quick applies default scopes rather than omitting them. This behavior might cause authentication failures with servers that do not recognize the default scopes.

- Only Dynamic Client Registration (DCR) is supported for automatic client registration. Client ID Metadata Documents are not supported.
- Well-known URI discovery uses the server root path only. Path-specific metadata locations (path-insertion discovery) are not supported. This limitation might prevent discovery of servers that serve metadata only at path-specific URIs.
