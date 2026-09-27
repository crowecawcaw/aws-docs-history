

# Asana integration
<a name="asana-integration"></a>

Connect Amazon Quick to your Asana workspace to manage projects, tasks, and team collaboration. The Asana connector uses the Asana V2 Model Context Protocol (MCP) server. You can create, update, and manage Asana content without leaving your Amazon Quick environment. Every action runs as the authenticated user, and the connector limits access to what that user can do in Asana. For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Supported authentication methods
<a name="asana-integration-authentication"></a>

The Asana connector supports a single authentication method: **Custom OAuth app**. This method uses user-based Open Authorization (OAuth) to connect to the Asana V2 MCP server.

Note the following behavior when you authenticate with the Asana MCP server:
+ The Asana MCP server does not support Dynamic Client Registration. You must pre-register an OAuth app in the Asana developer console before you set up the connector.
+ MCP apps do not use scopes. Remove the scope parameter entirely from your authorization URL.
+ Tokens issued for MCP apps work only with the MCP server, not with the standard Asana API.
+ Access tokens expire after 1 hour. The connector uses refresh tokens to maintain access.

## Before you begin
<a name="asana-integration-prerequisites"></a>

Before you set up the Asana connector, make sure you have the following:
+ An Asana account with access to the Asana developer console.
+ Permission to create and distribute apps in the Asana workspaces you want to connect.
+ A Amazon Quick subscription that meets the integration requirements. For more information, see [Set up integrations in the console](integration-console-setup-process.md).

## Configuring the Asana OAuth MCP app
<a name="asana-integration-setup"></a>

Create an OAuth MCP app in the Asana developer console, configure its OAuth settings, and configure workspace access before you set up the connector in Amazon Quick.

### Create an OAuth MCP app
<a name="asana-create-mcp-app"></a>

1. Go to the Asana developer console and sign in.

1. Choose **Create new app**.

1. Enter the app name.

1. For app type, choose **MCP app**.

1. Choose **Create app**.

1. Record the **Client ID** and **Client Secret**. You enter these values when you set up the connector in Amazon Quick.

### Configure OAuth settings
<a name="asana-configure-oauth"></a>

1. In the sidebar, choose **OAuth**.

1. Add the Amazon Quick callback URL as the redirect URL. You can copy this value from the connector setup page in Amazon Quick.

### Configure workspace access
<a name="asana-configure-workspace-access"></a>

1. In the sidebar, choose **Manage distribution**.

1. Choose how the app can be used:  
**Specific workspaces**  
Choose the individual workspaces where the app can be used.  
**Any workspace**  
Allow the app to be used in any workspace.

**Important**  
If you choose **Specific workspaces** but do not choose any workspaces, users receive an error when they try to authenticate.

## Setting up the connector in Amazon Quick
<a name="asana-integration-connector-setup"></a>

After you configure your Asana OAuth MCP app, set up the connector in Amazon Quick.

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Asana**.

1. Fill in the following details:
   + **Name** - Enter a descriptive name for your Asana integration.
   + **Description** - Describe the purpose of this integration.

1. Choose the connection type and configure the network type settings.

1. Configure the authentication settings. Use the values from your Asana OAuth MCP app.  
**Auth Type**  
Choose **Custom OAuth app**.  
**Client ID**  
Enter the client ID from the Asana developer console.  
**Client Secret**  
Enter the client secret from the Asana developer console.  
**Authorization URL**  
Enter `https://app.asana.com/-/oauth_authorize`. Do not include a scope parameter.  
**Token URL**  
Enter `https://app.asana.com/-/oauth_token`.  
**Redirect URL**  
This field is pre-filled with the Amazon Quick callback URL. Use this value as the redirect URL in your Asana OAuth app.

1. Choose **Create and continue**.

1. Add users to share the integration with.

1. Choose **Next**.

## Managing and troubleshooting
<a name="asana-integration-management"></a>

You can edit, share, and delete your Asana integrations after you create them. For more information, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

If you run into problems with your Asana integration, use the following guidance to resolve common issues.

**This app is not available to your workspace**  
The user's workspace is not included in the app's distribution settings. In the Asana developer console, choose **Manage distribution** and add the workspace, or choose **Any workspace**.

**Invalid scope(s) requested**  
Remove the scope parameter from the authorization URL. MCP apps do not use scopes.

**Authentication failures**  
Verify that the redirect URL matches the Amazon Quick callback URL, that the client ID and client secret are correct, and that the app is properly configured in **Manage distribution**.

**Connection issues**  
Verify that the access token is included in your requests and has not expired. Access tokens have a 1-hour lifetime. If the token has expired, the connector uses refresh tokens to obtain a new one automatically.