

# Model Context Protocol (MCP) integration
<a name="mcp-integration"></a>

Model Context Protocol (MCP) is an open standard that defines how AI applications communicate with external tools and data sources. MCP uses a client-server architecture. AI applications act as clients that connect to MCP servers. Each MCP server exposes a set of tools. These tools are structured operations that the AI application can invoke to perform tasks, such as querying databases, calling APIs, or interacting with third-party services.

With MCP integration in Amazon Quick, you can connect to remote MCP servers so that your AI assistant can use the tools that those servers provide. For example, you can connect to an MCP server that provides access to your project management system. This connection allows the assistant to create tickets, look up issues, or update statuses as part of a conversation. Because MCP is an open standard, you can connect to any compatible server without building custom integrations for each tool.

You can connect to MCP servers that are reachable over the public internet. You can also connect to private MCP servers that are reachable from a virtual private cloud (VPC) in your AWS account by using a Amazon Quick VPC connection. The MCP server can be in the VPC, in another VPC reachable through peering or transit gateway, or on-premises reachable through AWS Direct Connect or VPN. For information about creating a VPC connection in Amazon Quick, see [Configuring VPC connections in Amazon Quick Sight](working-with-aws-vpc.md).

**Important**  
When you connect to a private MCP server through a VPC connection, you can configure two independent VPC connections:  
**Resource-server VPC connection** (`VpcConnectionArn`) – Carries traffic between Amazon Quick and the MCP server endpoint (tool invocations, capability discovery).
**Auth-server VPC connection** (`AuthVpcConnectionArn`) – Carries OAuth traffic between Amazon Quick and the authorization server (token requests, authorization code exchange, Dynamic Client Registration, and metadata discovery).
You can set one, both, or neither connection depending on your network topology. If you do not set an auth-server VPC connection, OAuth endpoints must be reachable over the public internet (the default behavior). If your OAuth provider is reachable only from within a VPC, set an auth-server VPC connection. The resource-server and auth-server VPC connections are independent. They can point to different VPCs. MCP servers that do not require authentication are also supported.

## Supported capabilities
<a name="mcp-integration-capabilities"></a>

MCP integration registers MCP server tools as actions in Amazon Quick.

**Connector**  
Each tool that an MCP server exposes registers as an action that your AI assistant can invoke during conversations. The integration secures these connections by using Proof Key for Code Exchange (PKCE) with the S256 challenge method and Resource Indicators (RFC 8707) to bind access tokens to specific MCP servers.

## Before you begin
<a name="mcp-integration-prerequisites"></a>

Before you set up MCP integration, make sure that you have the following:
+ An MCP server endpoint with appropriate access.
+ Authentication credentials for the MCP server, if required. For more information, see [Prepare MCP server setup and authentication](#mcp-integration-authentication).
+ An Amazon Quick Enterprise subscription.
+ If you are connecting to a private MCP server, an active Amazon Quick VPC connection that has network access to the MCP server. For more information, see [Configuring VPC connections in Amazon Quick Sight](working-with-aws-vpc.md).

**Note**  
MCP integration supports remote servers only. HTTP streaming is preferred over Server-Sent Events (SSE). Local stdio connections are not supported.

## Prepare MCP server setup and authentication
<a name="mcp-integration-authentication"></a>

When you connect to an MCP server, Amazon Quick uses OAuth 2.0 Protected Resource Metadata (RFC 9728) to automatically discover authorization server information. The client sends an initial unauthenticated request to the MCP server. If the server responds with a 401 status that contains a `WWW-Authenticate` header with a `resource_metadata` URL, then Amazon Quick uses that URL to fetch the metadata document. If the header is not present, then Amazon Quick falls back to the well-known URI at the server root.

When an auth-server VPC connection is configured, Amazon Quick performs all OAuth discovery over that connection instead of the public internet. This includes fetching the `/.well-known/oauth-authorization-server` document, the `resource_metadata` URL from the MCP server's `WWW-Authenticate` header, and the `registration_endpoint` for Dynamic Client Registration (DCR). DNS resolution for the authorization server hostname must be reachable from the subnets and DNS resolver endpoints that are associated with the auth-server VPC connection.

If the authorization server supports Dynamic Client Registration (DCR), then Amazon Quick automatically registers itself by using the discovered `registration_endpoint` from the authorization server metadata. No manual credential configuration is required. Amazon Quick supports both confidential and public client flows. DCR applies regardless of the authentication method that you choose.

If the authorization server does not support DCR, then you must manually provide credentials. Choose the authentication method that matches your MCP server requirements.

**User authentication (OAuth)**  
Gather the following information from your MCP server configuration:  
+ **Client ID** – The OAuth client ID.
+ **Public OAuth client** (Optional) – Select this checkbox if your OAuth application uses public client configuration (no client secret).
+ **Client Secret** – The OAuth client secret.
+ **Token URL** – The OAuth token endpoint.
+ **Authorization URL** – The OAuth authorization endpoint.
+ **Redirect URL** – The OAuth redirect URI.
Select **Public OAuth client** if your MCP server's OAuth application does not use a client secret. This is common for public clients that rely solely on PKCE for security. When this option is selected, the **Client Secret** field is not required.

**Service authentication (Service-to-Service)**  
Gather the following information from your MCP server configuration:  
+ **Client ID** – The service client ID.
+ **Client Secret** – The service client secret.
+ **Token URL** – The service token endpoint.

**No authentication**  
If the MCP server does not require authentication, no credentials are needed. Select this option for MCP servers that allow unauthenticated access.

## Set up MCP integration
<a name="mcp-integration-setup"></a>

After you prepare your MCP server configuration and authentication credentials, create your MCP integration.

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Model Context Protocol (MCP)**.

1. On the **Create Integration** page, enter the integration details:
   + **Name** – A descriptive name for your MCP integration.
   + **Description** (Optional) – The purpose of the integration.
   + **MCP server endpoint** – The URL of the MCP server.
   + **Connection type** – Choose how Amazon Quick connects to the MCP server (resource server):
     + **Public network** – Use this option for MCP servers that are reachable over the public internet.
     + A named VPC connection – Use this option for private MCP servers. The dropdown lists the VPC connections that are configured on your Amazon Quick account. Choose the connection that has network access to your MCP server. If you don't see your VPC connection in the list, confirm that it is fully provisioned and active. For more information, see [Configuring VPC connections in Amazon Quick Sight](working-with-aws-vpc.md).
   + **Auth server connection type** – Choose how Amazon Quick connects to the OAuth authorization server. This setting is independent of the resource-server connection type.
     + **Public network** (default) – Use this option when the OAuth endpoints (authorization, token, and registration endpoints) are reachable over the public internet. This preserves the default behavior for existing integrations.
     + A named VPC connection – Use this option when the OAuth provider is reachable only from within a VPC. Choose the VPC connection that has network access to the authorization server. The auth-server VPC connection can be the same as or different from the resource-server VPC connection. For example, your MCP server and OAuth provider might reside in separate VPCs.

1. Choose **Next**.

1. Select the authentication method (user, service, or no authentication).

1. Enter the appropriate configuration details.

1. Choose **Create and continue**.

1. Review the integration details.

1. Choose **Next**.

1. Share the integration with other users if needed.

After you create your MCP integration, Amazon Quick discovers the available tools and registers them as actions.

## Review integration
<a name="mcp-integration-review"></a>

After you configure authentication, review the MCP integration capabilities:

1. The system connects to the MCP server and discovers available capabilities.

1. Review the list of available actions and tasks that the MCP server provides.

1. Confirm the integration configuration and capabilities.

### Capability discovery
<a name="mcp-integration-capabilities-discovery"></a>

During the connection process that is described in [Prepare MCP server setup and authentication](#mcp-integration-authentication), Amazon Quick also discovers and registers the tools that the MCP server provides. After discovery completes, each tool is listed as an action that you can review and turn on.

## Manage MCP integrations
<a name="mcp-integration-management"></a>

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

## MCP Sync
<a name="mcp-integration-sync"></a>

As external MCP servers add new tools, update descriptions, and evolve their capabilities, MCP Sync keeps your connectors current. When an MCP server adds, removes, or modifies tools, MCP Sync updates your connector to reflect those changes without requiring you to reconnect.

Amazon Quick supports two connector types with different sync behaviors:

**Built-in MCP connectors**  
Built-in connectors sync automatically. When the MCP server updates its tools, Amazon Quick detects the change and applies it without any action from you. Auto-sync is mandatory for built-in connectors and cannot be turned off. This prevents action failures caused by schema changes or removed tools on the server side. Built-in connectors sync automatically twice a month, on the first and third Monday of each month at 9:00 AM Pacific time.

**Custom MCP connectors**  
Custom connectors require the connector owner to trigger a sync manually. To sync a custom connector, open the connector details page, and then choose **Sync**.  
Triggering a sync initiates a re-authorization flow. If the MCP server now requires OAuth scopes that were not granted during the original connection, the sync fails. Confirm that all required scopes are authorized before you sync.

## Security considerations
<a name="mcp-integration-security"></a>

When you use an auth-server VPC connection with MCP integrations, the following security behaviors apply.

**Data in transit**  
When an auth-server VPC connection (`AuthVpcConnectionArn`) is configured, all OAuth credential exchange, including authorization codes, refresh tokens, and ID tokens, transits your VPC over TLS. Tokens do not traverse the public internet on the auth-server path and remain within AWS internal infrastructure.

**Logging**  
The auth-server VPC connection does not introduce new AWS CloudTrail event types. Existing CloudTrail coverage on `CreateActionConnector`, `UpdateActionConnector`, and `PatchActionConnector` API operations continues to apply. The `AuthVpcConnectionArn` field appears in the request body of those existing events when it is set.

## Troubleshooting
<a name="mcp-integration-troubleshooting"></a>

Use the following guidance to diagnose and resolve common issues when you create or use an MCP integration in Amazon Quick.

### Connector creation issues
<a name="mcp-integration-troubleshooting-creation"></a>
+ **Connector passes discovery but fails at publish with `Creation failed`** – This error usually means that one or more tool definitions in your MCP server's `tools/list` response contain an invalid `inputSchema`. Amazon Quick validates each tool's `inputSchema` against JSON Schema Draft 7 or later during the publish phase.

  The most common cause is the deprecated Draft 3 syntax, where `required` is a boolean inside a property definition (for example, `"required": true`). In JSON Schema Draft 7 and later, `required` must be an array of property names at the schema root, as a sibling of `properties`.

  Update your tool definitions to use the correct format and redeploy your MCP server. After you redeploy, delete the failed connector and create a new one to retrigger discovery and publish.

  The following example shows the incorrect Draft 3 syntax:

  ```
  {
    "type": "object",
    "properties": {
      "logNumber": {
        "type": "string",
        "description": "The permit log number",
        "required": true
      }
    }
  }
  ```

  The following example shows the correct Draft 7 syntax:

  ```
  {
    "type": "object",
    "properties": {
      "logNumber": {
        "type": "string",
        "description": "The permit log number"
      }
    },
    "required": ["logNumber"]
  }
  ```

  Some MCP framework libraries and code generators emit Draft 3 syntax by default. Check your framework documentation for the option that selects the JSON Schema output version. You can also validate your schemas with any JSON Schema Draft 7 validator before you deploy. For more information about `inputSchema` requirements, see [Tools](https://modelcontextprotocol.io/specification/latest/server/tools) in the Model Context Protocol specification.

  You might also notice that connector creation hangs for two to five minutes before it fails. The elapsed time reflects internal retries during the publish phase, not a network timeout. The fix is the same: check your tool `inputSchema` definitions for JSON Schema Draft 7 compliance.

### VPC connection issues
<a name="mcp-integration-troubleshooting-vpc"></a>
+ **VPC connection is not listed in the **Connection type** dropdown, or MCP creation fails immediately after you select it** – The VPC connection might appear in the dropdown before provisioning is complete. Wait until the VPC connection shows as available on the Amazon Quick admin page before you create an MCP integration against it. For more information, see [Configuring VPC connections in Amazon Quick Sight](working-with-aws-vpc.md).
+ **MCP creation fails because the MCP server hostname cannot be resolved** – Amazon Quick does not use the default VPC DNS resolver for MCP integrations. You must populate the **DNS resolver endpoints** field on the VPC connection with Route 53 Resolver inbound endpoint IP addresses that can resolve your MCP server hostname. This requirement applies to both private hostnames and to public hostnames that you want to resolve to a private address from within the VPC, such as endpoints fronted by AWS PrivateLink or a Route 53 private hosted zone. Without these resolver endpoints, the MCP server hostname cannot be resolved and integration creation fails. For more information, see [Configuring VPC connections in Amazon Quick Sight](working-with-aws-vpc.md).
+ **MCP server is unreachable from the VPC connection** – Traffic from Amazon Quick to your MCP server originates from the subnets that you selected during VPC connection setup. Confirm that route tables, network ACLs, and security groups allow traffic between those subnets and the MCP server endpoint. For general VPC networking guidance, see [Configuring VPC connections in Amazon Quick Sight](working-with-aws-vpc.md).
+ **Authorization server hostname cannot be resolved from the auth-server VPC connection** – The same DNS resolver requirement that applies to the resource-server VPC connection also applies to the auth-server VPC connection. You must populate the **DNS resolver endpoints** field on the auth-server VPC connection with Route 53 Resolver inbound endpoint IP addresses that can resolve the authorization server hostname. If the resource server and authorization server are in different VPCs, each VPC connection needs its own DNS resolver endpoints. For more information, see [Configuring VPC connections in Amazon Quick Sight](working-with-aws-vpc.md).
+ **Authorization server is unreachable from the auth-server VPC connection** – Traffic from Amazon Quick to the authorization server originates from the subnets that are associated with the auth-server VPC connection. Confirm that route tables, network ACLs, and security groups in those subnets allow outbound traffic to the authorization server endpoints. The resource-server and auth-server VPC connections might use different subnets in different VPCs, so verify networking requirements independently for each connection.
+ **Authentication fails when you use a private MCP server** – If the OAuth endpoints that the MCP server advertises are reachable only from within a VPC, you must configure an auth-server VPC connection. Without an auth-server VPC connection, Amazon Quick attempts to reach the OAuth endpoints over the public internet, and requests fail if those endpoints are not publicly accessible.

  To resolve this issue, edit the MCP integration and set the **Auth server connection type** to the VPC connection that has network access to the authorization server. After you save the change, Amazon Quick routes all OAuth traffic (token requests, authorization code exchange, metadata discovery, and Dynamic Client Registration) through that VPC connection.

  If an auth-server VPC connection is already configured and authentication still fails, confirm the following:
  + The **DNS resolver endpoints** on the auth-server VPC connection can resolve the authorization server hostname.
  + Route tables, network ACLs, and security groups in the auth-server VPC connection's subnets allow outbound traffic to the authorization server endpoints.
  + The OAuth URLs returned in the MCP server's protected resource metadata match the endpoints that the auth-server VPC connection can reach.

### Microsoft Entra ID issues
<a name="mcp-integration-troubleshooting-entra"></a>

If your MCP server uses Microsoft Entra ID as the authorization server, the following errors are common during connector setup. These issues apply to both public network connections and private MCP servers that you reach through a VPC connection.
+ **`AADSTS9010010` – the v2.0 endpoint rejects the resource parameter** – Amazon Quick sends a `resource` parameter on OAuth requests as required by the MCP specification (RFC 8707). The Entra ID v2.0 endpoint rejects requests that include both a `resource` parameter and `scope` values. To resolve this error, configure your app registration to use the Entra ID v1.0 OAuth endpoints and set `accessTokenAcceptedVersion` to `2` in the app manifest.
+ **`AADSTS90009` – application requests a token for itself** – When you use user authentication (authorization code flow) and the OAuth client and the MCP resource resolve to the same Entra ID application, Entra ID blocks the request. Create two separate app registrations: one client app for Amazon Quick and one resource app for the MCP server. This issue does not affect service authentication (client credentials flow), where a single app registration works.

### Snowflake MCP server issues
<a name="mcp-integration-troubleshooting-snowflake"></a>

If your MCP server is hosted on Snowflake, the following issue is common during connector setup. This issue applies to both public network and VPC connection configurations.
+ **Connection fails or returns unexpected errors when the endpoint URL does not include the correct Region** – Snowflake MCP server endpoint URLs are Region-specific. If the endpoint URL omits the AWS Region or defaults to a different Region than where your Snowflake account is deployed, the connection fails.

  Verify that the **MCP server endpoint** URL that you provide during integration setup includes the Region where your Snowflake account is deployed. The general endpoint format is:

  ```
  https://{{account-identifier}}.{{region}}.snowflakecomputing.com/api/v2/cortex/mcp
  ```

  If you connect through AWS PrivateLink, use the following format:

  ```
  https://{{account-identifier}}.{{region}}.privatelink.snowflakecomputing.com/api/v2/cortex/mcp
  ```

  Replace {{account-identifier}} with your Snowflake account identifier and {{region}} with the AWS Region where your Snowflake account is deployed (for example, `us-east-1`). For the correct endpoint URL format for your account, see your Snowflake documentation.

If you encounter an issue that is not covered in the preceding sections, contact AWS Support through the Amazon Quick console or AWS Support Center.

## Limitations
<a name="mcp-integration-limitations"></a>

When you use MCP integrations in Amazon Quick, be aware of the following limitations:
+ MCP operations have a fixed 60-second timeout. Operations that exceed this limit automatically fail with an HTTP 424 error.
+ For MCP servers that you reach through a VPC connection, DNS resolution for the authorization server hostname must be reachable from the auth-server VPC connection's subnets and DNS resolver endpoints. This is the same constraint that applies to the resource-server VPC connection for the MCP server hostname. If you do not configure an auth-server VPC connection, the OAuth endpoints must be reachable over the public internet.
+ Custom HTTP headers are not supported in MCP operations. Only standard system headers are transmitted.
+ For custom MCP connectors, tool lists do not update automatically. To pick up server-side tool changes, open the connector details page and choose **Sync**. Built-in MCP connectors sync automatically. For more information, see [MCP Sync](#mcp-integration-sync).
+ Amazon Quick supports a maximum of 100 tools per MCP server connection. If the MCP server exposes more than 100 tools, only the first 100 are registered.
+ Connector creation might fail if the Amazon Quick callback URI is not allow-listed by third-party providers.
+ Server connectivity issues result in immediate failure without retry attempts.
+ Step-up authorization is not supported. If an MCP server requires additional scopes after the initial authorization (HTTP 403 with `insufficient_scope`), then you must re-authorize the entire connection. Incremental permission upgrades are not available.
+ Scope handling has the following limitations:
  + Amazon Quick does not extract the `scope` parameter from the server's initial 401 `WWW-Authenticate` challenge. Amazon Quick determines scopes from the Protected Resource Metadata document instead.
  + When the metadata does not specify supported scopes, Amazon Quick applies default scopes rather than omitting them. This behavior might cause authentication failures with servers that do not recognize the default scopes.
+ Only Dynamic Client Registration (DCR) is supported for automatic client registration. Client ID Metadata Documents are not supported.
+ Well-known URI discovery uses the server root path only. Path-specific metadata locations (path-insertion discovery) are not supported. This limitation might prevent discovery of servers that serve metadata only at path-specific URIs.