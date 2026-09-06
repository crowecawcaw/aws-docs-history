

# Smartsheet integration
<a name="smartsheet-integration"></a>

With the Smartsheet connector, you can manage sheets, rows, reports, and search across your Smartsheet workspaces directly in Amazon Quick through natural language.

## Prerequisites
<a name="smartsheet-integration-prerequisites"></a>

Before you set up the integration, make sure that you meet the following requirements.
+ A Smartsheet account with a Business, Enterprise, or Advanced Work Management plan. Free accounts cannot generate API access tokens or register OAuth apps. For more information, see [Smartsheet pricing](https://www.smartsheet.com/pricing) on the Smartsheet website and [Smartsheet OAuth](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth) in the Smartsheet documentation.
+ [Smartsheet Developer Tools](https://developers.smartsheet.com/) activated for your account.
+ For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configure Smartsheet Developer Tools
<a name="smartsheet-source-setup"></a>

Before you configure Amazon Quick, set up credentials in Smartsheet. Each user signs in with their own Smartsheet account, and actions run with that user's permissions. This method uses Custom OAuth app. Complete the [Register for Developer Tools and create a developer profile](#smartsheet-register-developer-tools) and [Register the OAuth application](#smartsheet-register-oauth-app) sections below.

For more information about authentication methods, see [Authentication methods](quick-action-auth.md).

### Register for Developer Tools and create a developer profile
<a name="smartsheet-register-developer-tools"></a>

1. Go to the [Developer Tools Registration](https://developers.smartsheet.com/register) page and register the Smartsheet account you want to use with your apps. For more information, see [Register for Developer Tools](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#register-for-developer-tools) in the Smartsheet API documentation.

1. After Smartsheet activates Developer Tools, sign in to the Smartsheet application and choose your **Account** icon in the lower-left corner, then choose **Developer Tools**.

1. Choose **Create Developer Profile** and enter a profile name. For more information, see [Create your developer profile](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#create-your-developer-profile) in the Smartsheet API documentation.

**Tip**  
Smartsheet recommends using a dedicated service account for OAuth apps rather than a personal account.

### Register the OAuth application
<a name="smartsheet-register-oauth-app"></a>

1. In Smartsheet Developer Tools, choose **Create New App**.

1. Complete the form:
   + **App name** – A name to identify your app to users.
   + **App description** – A brief description of the integration.
   + **App URL** – The URL that launches your app, or a landing page.
   + **App contact/support** – Support contact information.
   + **App redirect URL** – `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback`

     Replace {{{region}}} with your AWS Region (for example, `us-east-1`).

1. Choose **Save**. Smartsheet generates the **App client ID** and **App secret**.

1. Copy the **Client ID** and **Client Secret** values. You need these when you configure the integration in Amazon Quick.

For more information, see [Register an app](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#register-an-app) in the Smartsheet API documentation.

**Note**  
When you configure the OAuth app, the connector requests access scopes from Smartsheet that determine what it can do on behalf of the authenticated user. Access scopes don't override existing sharing permissions. For more information, see [Access scopes](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#access-scopes) in the Smartsheet API documentation.

## Set up the integration in Amazon Quick
<a name="smartsheet-quicksuite-setup"></a>

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Smartsheet**.

1. Enter the integration details:
   + **Name** – Descriptive name for your Smartsheet integration.
   + **Description** (Optional) – Purpose of the integration.
   + **Base URL** – `https://mcp.smartsheet.com`
   + **Client ID** – App client ID from your Smartsheet Developer Tools app registration.
   + **Client Secret** – App secret from your Smartsheet Developer Tools app registration.
   + **Token URL** – `https://api.smartsheet.com/2.0/token`
   + **Auth URL** – `https://app.smartsheet.com/b/authorize`

1. Choose **Create and continue**.

1. Choose users to share the integration with.

1. Choose **Next**.

**Note**  
If you're using a Smartsheet regional server outside of the US, replace the MCP server URL with one for your region:  
For Europe, use `https://mcp.smartsheet.eu`
For Australia, use `https://mcp.smartsheet.au`

## Available actions
<a name="smartsheet-integration-actions"></a>

After you set up the connector, the actions exposed by the Smartsheet MCP server are available. To see the current set of actions for your connector, open the connector's **Available actions** view in the Amazon Quick console. For a full list of available MCP tools, see [MCP Server Tools](https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server-tools) in the Smartsheet documentation.

## Managing and troubleshooting
<a name="smartsheet-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Authentication issues
<a name="smartsheet-troubleshooting-auth"></a>
+ **OAuth authorization fails** – Verify that the Client ID and Client Secret match the values in your Smartsheet Developer Tools app registration. Confirm the redirect URL in Smartsheet matches the URL in your Amazon Quick configuration exactly. For a list of OAuth error types, see [OAuth error types](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#oauth-error-types) in the Smartsheet API documentation.
+ **Developer Tools not available** – Verify that Developer Tools is activated for your Smartsheet account. Free accounts do not support Developer Tools. If your request was denied, contact your Smartsheet Customer Success Manager.

### Common error messages
<a name="smartsheet-troubleshooting-errors"></a>
+ **Actions return permission errors** – Verify that the authenticated user has the required sharing permissions on the target sheets. OAuth scopes don't override sharing-level access controls. For more information, see [Resource access levels](https://developers.smartsheet.com/api/smartsheet/guides/basics/resource-access-levels) in the Smartsheet API documentation.
+ **Sheet not found** – Verify the sheet ID is correct and that the authenticated user has at least viewer access to the sheet.
+ **API rate limit errors** – The Smartsheet API enforces rate limits. For more information, see [Limitations](https://developers.smartsheet.com/api/smartsheet/guides/basics/limitations) in the Smartsheet API documentation.