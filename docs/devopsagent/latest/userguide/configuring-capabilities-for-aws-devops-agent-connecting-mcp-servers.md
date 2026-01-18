# Connecting MCP Servers

Model Context Protocol (MCP) servers extend AWS DevOps Agent's investigation capabilities by providing access to data from your external observability tools, custom monitoring systems, and operational data sources. This guide explains how to connect an MCP server to AWS DevOps Agent.

## Requirements

Before connecting an MCP server, ensure your server meets these requirements:

- **Publicly accessible endpoint** – MCP servers must be accessible from the public internet over HTTPS. AWS DevOps Agent does not support connecting to servers hosted in VPCs.
- **Streamable HTTP transport protocol** – Only MCP servers that implement the Streamable HTTP transport protocol are supported.
- **Authentication support** – Your MCP server must support OAuth 2.0 authentication flows or API key/token-based authentication.

## Security considerations

When connecting MCP servers to AWS DevOps Agent, consider these security aspects:

- **Tool allowlisting –** You should allowlist only the specific tools your Agent Space needs, rather than exposing all tools from your MCP server. See [Connecting MCP Servers](configuring-capabilities-for-aws-devops-agent-connecting-mcp-servers.md "configuring-capabilities-for-aws-devops-agent-connecting-mcp-servers.md") for how to allow list tools per Agent Space.

Please note that the maximum tool length of any MCP tool is 64.

- **Prompt injection risks** – Custom MCP servers can introduce additional risk of prompt injection attacks. See [AWS DevOps Agent Security](aws-devops-agent-security.md "aws-devops-agent-security.md") for more information.
- **Read-only tools and access –** Only allowlist read-only MCP tools and ensure that authentication credentials are only permitted read-only access.

See [AWS DevOps Agent Security](aws-devops-agent-security.md "aws-devops-agent-security.md") for more information on prompt injection and the shared responsibility model.

## Registering an MCP server (account-level)

MCP servers are registered at the AWS account level and shared among all Agent Spaces in that account. Individual Agent Spaces can then choose which specific tools they need from each MCP server.

### Step 1: MCP server details

1. Sign in to the AWS Management Console
2. Navigate to the AWS DevOps Agent console
3. Go to the **Capabilities** tab
4. In the **MCP Servers** section, click **Add**
5. On the **MCP server details** page, enter the following information:
   - **Name** – Enter a descriptive name for your MCP server
   - **Endpoint URL** – Enter the full HTTPS URL of your MCP server endpoint
   - **Description** (optional) – Add a description to help identify the server's purpose
   - **Enable Dynamic Client Registration** – Select this checkbox if you want to allow AWS DevOps Agent to automatically register with your MCP server's authorization server

6. Click **Next**

###### Note

The MCP server endpoint URL will be displayed in AWS CloudTrail logs in your account.

### Step 2: Authorization flow

Select the authentication method for your MCP server:

**OAuth Client Credentials** – If your MCP server uses OAuth Client Credentials flow:

1. Select **OAuth Client Credentials**
2. Click **Next**

**OAuth 3LO (Three-Legged OAuth)** – If your MCP server uses OAuth 3LO for authentication:

1. Select **OAuth 3LO**
2. Click **Next**

**API Key** – If your MCP server uses API key authentication:

1. Select **API Key**
2. Click **Next**

### Step 3: Authorization configuration

Configure additional authorization parameters based on the selected authentication method:

**For OAuth Client Credentials:**

1. **Client ID** – Enter the client ID of the OAuth client
2. **Client Secret** – Enter the client secret of the OAuth client
3. **Exchange URL** – Enter the OAuth token exchange endpoint URL
4. **Exchange Parameters** – Enter OAuth token exchange parameters for authenticating with the service
5. **Add Scope** – Add OAuth scopes for authentication
6. Click **Next**

**For OAuth 3LO:**

1. **Client ID** – Enter the client ID of the OAuth client
2. **Client Secret** – Enter the client secret of the OAuth client if it’s required by your OAuth client
3. **Exchange URL** – Enter the OAuth token exchange endpoint URL
4. **Authorization URL** - Enter the OAuth authorization endpoint URL
5. **Code Challenge Support** - Select this checkbox if your OAuth client supports code challenge
6. **Add Scope** – Add OAuth scopes for authentication
7. Click **Next**

**For API Key:**

1. Enter an API key name
2. Enter the the name of the header that will contain the API key in the request
3. Enter your API key value
4. Click **Next**

### Step 4: Review and submit

1. Review all the MCP server configuration details
2. Click **Submit** to complete the registration
3. AWS DevOps Agent will validate the connection to your MCP server
4. Upon successful validation, your MCP server will be registered at the account level

## Configuring MCP tools in an Agent Space

After registering an MCP server at the account level, you can configure which tools from that server are available to specific Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space
2. Go to the **Capabilities** tab
3. In the **MCP Servers** section, click **Add**
4. Select the registered MCP server you want to connect to this Agent Space
5. Configure which tools from this MCP server should be available to the Agent Space:
   - **Allow all tools** – Makes all tools from the MCP server available
   - **Select specific tools** – Allows you to choose which tools to allowlist

6. Click **Add** to connect the MCP server to your Agent Space

AWS DevOps Agent will now be able to use the allowlisted tools from your MCP server during investigations in this Agent Space.

## Managing MCP server connections

**Updating authentication credentials** – If your authentication credentials need to be updated, you will need to re-register your MCP server. Navigate to the **Settings** page the AWS DevOps Agent console, locate your MCP server, remove any active associations, and click **Deregister**. Next, **register** your MCP server with the new authentication credentials and re-create any necessary associations with your Agent Space.

**Viewing connected MCP servers** – To see all MCP servers connected to your Agent Space, select your Agent Space, go to the **Capabilities** tab, and check the **MCP Servers** section. You can also update selected tools here.

**Removing MCP server connections** – To disconnect an MCP server from an Agent Space, select the server in the **MCP Servers** section and click **Remove**. To completely delete an MCP server registration, remove it from all Agent Spaces first, then delete the account-level registration.

## Related topics

- Security in AWS DevOps Agent
- Setting up an Agent Space
- Prompt Injection Protection
