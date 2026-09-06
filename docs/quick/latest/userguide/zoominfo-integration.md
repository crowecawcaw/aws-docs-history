

# ZoomInfo integration
<a name="zoominfo-integration"></a>

With the ZoomInfo connector, you can look up company and contact data, and query firmographic and intent data directly in Amazon Quick through natural language.

Amazon Quick supports multiple authentication methods for ZoomInfo. Choose the method that best fits your organization's security requirements.
+ **Default OAuth app** – Uses an AWS-managed OAuth application. No additional credentials are needed. Users authenticate directly with their ZoomInfo account.
+ **Custom OAuth app** – Uses a customer-managed OAuth application. This option gives your organization full control over the OAuth configuration.
+ **Service-to-Service OAuth** – Uses client credentials for server-to-server authentication without user interaction. Suitable for automated workflows.
+ **API Key** – Uses an API key for authentication.

For more information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="zoominfo-integration-prerequisites"></a>

Make sure that you have the following before you set up the integration.
+ An active ZoomInfo account with access to the data products you want to query.
+ For **Custom OAuth app** or **Service-to-Service OAuth**: OAuth credentials from your ZoomInfo administrator. ZoomInfo uses Okta for OAuth.
+ For **API Key**: A ZoomInfo-issued API key.
+ For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configuring ZoomInfo
<a name="zoominfo-source-setup"></a>

If you are using **Default OAuth app** authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#zoominfo-quicksuite-setup).

For Custom OAuth app or Service-to-Service OAuth authentication, work with your ZoomInfo administrator to register an OAuth client in the ZoomInfo Okta tenant and add the Amazon Quick callback URL `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback` as a redirect URI. Replace {{{region}}} with your AWS Region (for example, `us-east-1`). For step-by-step instructions, see [ZoomInfo MCP Overview](https://docs.zoominfo.com/docs/zi-api-mcp-overview/) and [Developer Portal Guide](https://docs.zoominfo.com/docs/app-creation-developer-portal-guide) in the ZoomInfo documentation. Record the Client ID and Client Secret — you need them when you configure Amazon Quick. For API Key authentication, generate an API key from your ZoomInfo account.

## Setting up the connector in Amazon Quick
<a name="zoominfo-quicksuite-setup"></a>

### Connect from the Available tab
<a name="zoominfo-quick-connect"></a>

If you want to use Default OAuth app authentication, you can connect directly from the **Available** tab without additional configuration.

1. In the Amazon Quick console, choose **Connectors**.

1. On the **Available** tab, find **ZoomInfo** and choose **Connect**.

1. Complete the ZoomInfo sign-in flow and grant the requested permissions.

To configure a connector with one of the other authentication methods, use the **Create for your team** tab as described below.

### Create from the Create for your team tab
<a name="zoominfo-full-setup"></a>

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **ZoomInfo**.

1. Enter a **Name** for your connector. Optionally, choose **\+ Add Description** to add a description.

1. For **Connection type**, choose **Public network**.

1. For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.

   1. For **Default OAuth app**:

      No additional credentials are needed. Choose **Next** to continue.

   1. For **Custom OAuth app**, configure the following fields:
      + **Client ID** – The client ID from your ZoomInfo OAuth client.
      + **Public OAuth client** (Optional) – Select this option if your ZoomInfo OAuth client is configured as a public client (no client secret).
      + **Client secret** – The client secret from your ZoomInfo OAuth client.
      + **Token URL** – The token endpoint. Default: `https://okta-login.zoominfo.com/oauth2/default/v1/token`
      + **Authorization URL** – The authorization endpoint. Default: `https://okta-login.zoominfo.com/oauth2/default/v1/authorize`
      + **Redirect URL** – Pre-filled with the Amazon Quick callback URL.

   1. For **Service-to-Service OAuth**, configure the following fields:
      + **Client ID** – The client ID from your ZoomInfo OAuth client.
      + **Client secret** – The client secret from your ZoomInfo OAuth client.
      + **Token URL** – The token endpoint. Default: `https://okta-login.zoominfo.com/oauth2/default/v1/token`

   1. For **API Key**, configure the following fields:
      + **API Key** – The ZoomInfo API key.
      + **Email** (Optional) – The email address associated with the API key.

1. Choose **Next**.

1. If you chose **Default OAuth app** or **Custom OAuth app**, a ZoomInfo authorization window opens. Review the requested permissions and choose **Allow**.

1. On the **Review** page, review the available actions for the connector. Choose **Next**.

1. On the **Publish** page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.

1. Choose **Publish**.

## Available actions
<a name="zoominfo-integration-actions"></a>

After you set up the connector, the actions exposed by ZoomInfo are available. To see the current set of actions for your connector, go to the connector's **Available actions** view in the Amazon Quick console.

## Managing and troubleshooting
<a name="zoominfo-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Authentication issues
<a name="zoominfo-troubleshooting-auth"></a>
+ **Sign-in fails (Default OAuth app or Custom OAuth app)** – Verify that your ZoomInfo account is active. For Custom OAuth app, confirm that the redirect URI in your ZoomInfo OAuth client matches the Amazon Quick callback URL.
+ **Invalid client credentials (Custom OAuth app or Service-to-Service OAuth)** – Verify that the Client ID and Client secret match the values in your ZoomInfo OAuth client.
+ **API Key authentication fails** – Verify that the API key has not been revoked.