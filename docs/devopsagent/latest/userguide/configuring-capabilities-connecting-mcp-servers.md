# Connecting MCP Servers

Model Context Protocol (MCP) servers extend AWS DevOps Agent's investigation capabilities by providing access to data from your external observability tools, custom monitoring systems, and operational data sources. This guide explains how to connect an MCP server to AWS DevOps Agent.

## Requirements

Before connecting an MCP server, ensure your server meets these requirements:

- **Publicly accessible endpoint**– MCP servers must be accessible from the public internet over HTTPS. AWS DevOps Agent does not support connecting to servers hosted in VPCs.
- **Streamable HTTP transport protocol**– Only MCP servers that
  implement the Streamable HTTP transport protocol are supported.
- **Authentication support**– Your MCP server must support OAuth 2.0 authentication flows or API key/token-based authentication.

## Security considerations

When connecting MCP servers to AWS DevOps Agent, consider these security aspects:

- **Tool allowlisting –**Allowlist only the specific tools your
  Agent Space needs, rather than exposing all tools from your MCP server. See [Connecting MCP Servers](configuring-capabilities-connecting-mcp-servers.md "configuring-capabilities-connecting-mcp-servers.md") for how to allow list tools per
  Agent Space.
- **Prompt injection risks**– Custom MCP servers can introduce
  additional risk of prompt injection attacks. See [AWS DevOps Agent Security](aws-devops-agent-security.md "aws-devops-agent-security.md")
  for more information.
- **Read-only tools and access –**Only allowlist read-only MCP tools and ensure that authentication credentials are only permitted read-only access.

See [AWS DevOps Agent Security](aws-devops-agent-security.md "aws-devops-agent-security.md") for more information on prompt injection and
the shared responsibility model. ​

## Registering an MCP server (account-level)

MCP servers are registered at the AWS account level and shared among all Agent Spaces in that account. Individual Agent Spaces can then choose which specific tools they need from each MCP server.

### Step 1: MCP server details

- Sign in to the AWS Management Console
- Navigate to the AWS DevOps Agent console
- Go to the **Capabilities** tab
- In the **MCP Servers** section, click **Add**
- On the **MCP server details** page, enter the following information:
- **Name**– Enter a descriptive name for your MCP server
- **Endpoint URL**– Enter the full HTTPS URL of your MCP server endpoint
- **Description**(optional) – Add a description to help identify the server's purpose
- **Enable Dynamic Client Registration**– Select this checkbox if you want to allow AWS DevOps Agent to automatically register with your MCP server's authorization server
- Click **Next**

**Note:**The MCP server endpoint URL will be displayed in AWS CloudTrail logs in your account. ​

### Step 2: Authorization flow

Select the authentication method for your MCP server: **OAuth Client Credentials**– If your MCP server uses OAuth Client Credentials flow:

- Select **OAuth Client Credentials**
- Click **Next**

**OAuth 3LO (Three-Legged OAuth)**– If your MCP server uses OAuth 3LO for authentication:

- Select **OAuth 3LO**
- Click **Next**
- **API Key**– If your MCP server uses API key authentication:
- Select **API Key**
- Click **Next**

### Step 3: Authorization configuration

Configure additional authorization parameters based on the selected authentication method: **For OAuth Client Credentials:**

- **Client ID**– Enter the client ID for your MCP server
- **Client Secret**– Enter the client secret for your MCP server
- **Exchange URL**– Enter the OAuth token exchange URL
- **Exchange Parameters**– Enter OAuth token exchange parameters for authenticating with the service
- **Add Scope**– Add OAuth scopes for authentication (the service will always request scope`offline_access`)
- Click **Next**

**For OAuth 3LO:**

- Configure the OAuth 3LO parameters as required by your MCP server
- The service will always request scope`offline_access`
- Click **Next**

**For API Key:**

- Enter your API key
- Configure header name (default: "Authorization")
- Configure token prefix (if needed)
- Click **Next**

### Step 4: Authorization configuration

Configure additional authorization parameters based on the selected authentication method: **For OAuth 2.0:**

- Enter Client ID and Client Secret (if not using Dynamic Client Registration)
- Configure scopes required for accessing your MCP server
- Add any additional OAuth parameters required by your server
- Click **Next**

**For API Key or Bearer Token:**

- Enter your API key or bearer token
- Configure header name (default: "Authorization")
- Configure token prefix (if needed)
- Click **Next**

### Step 5: Review and submit

- Review all the MCP server configuration details
- Click **Submit** to complete the registration
- AWS DevOps Agent will validate the connection to your MCP server
- Upon successful validation, your MCP server will be registered at the account level

## Configuring MCP tools in an Agent Space

After registering an MCP server at the account level, you can configure which tools from that server are available to specific Agent Spaces:

- In the AWS DevOps Agent console, select your Agent Space
- Go to the **Capabilities** tab
- In the **MCP Servers** section, click **Add**
- Select the registered MCP server you want to connect to this Agent Space
- Configure which tools from this MCP server should be available to the Agent Space:
- **Allow all tools**– Makes all tools from the MCP server available
- **Select specific tools**– Allows you to choose which tools to allowlist
- Click **Add** to connect the MCP server to your Agent Space

AWS DevOps Agent will now be able to use the allowlisted tools from your MCP server during investigations in this Agent Space.

## Managing MCP server connections

- **Updating authentication credentials** – If your authentication credentials need to be updated, navigate to the **Capabilities** tab in the AWS DevOps Agent console, select your MCP server, click **Edit**, update the authentication configuration, and click **Save**.
- **Viewing connected MCP servers** – To see all MCP servers connected to your Agent Space, select your Agent Space, go to the **Capabilities** tab, and check the **MCP Servers** section.
- **Removing MCP server connections** – To disconnect an MCP server from an Agent Space, select the server in the **MCP Servers** section and click **Remove**. To completely delete an MCP server registration, remove it from all Agent Spaces first, then delete the account-level registration.
