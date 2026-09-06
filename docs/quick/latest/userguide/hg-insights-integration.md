

# HG Insights integration
<a name="hg-insights-integration"></a>

With the HG Insights connector, you can access technographic data, query company technology profiles, and retrieve market intelligence directly in Amazon Quick through natural language.

Amazon Quick supports multiple authentication methods for HG Insights. Choose the method that best fits your organization's security requirements.
+ **Default OAuth app** – Uses an AWS-managed OAuth application. No additional credentials are needed. Users authenticate directly with their HG Insights account.
+ **Custom OAuth app** – Uses a customer-managed OAuth application. This option gives your organization full control over the OAuth configuration.
+ **Service-to-Service OAuth** – Uses client credentials for server-to-server authentication without user interaction. Suitable for automated workflows.
+ **API Key** – Uses an API key for authentication.

For more information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="hg-insights-integration-prerequisites"></a>

Make sure that you have the following before you set up the integration.
+ An active HG Insights account with access to the data products you want to query.
+ For **Custom OAuth app** or **Service-to-Service OAuth**: OAuth credentials from your HG Insights account.
+ For **API Key**: An HG Insights-issued API key.
+ For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configuring HG Insights
<a name="hg-insights-source-setup"></a>

If you are using **Default OAuth app** authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#hg-insights-quicksuite-setup).

For Custom OAuth app or Service-to-Service OAuth authentication, register an OAuth client in your HG Insights Phoenix account and add the Amazon Quick callback URL `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback` as a redirect URI. Replace {{{region}}} with your AWS Region (for example, `us-east-1`). For step-by-step instructions, see [Phoenix by HG Insights](https://phoenix.hginsights.com/docs/intro) documentation. Record the Client ID and Client Secret — you need them when you configure Amazon Quick. For API Key authentication, generate an API key from your Phoenix account.

## Setting up the connector in Amazon Quick
<a name="hg-insights-quicksuite-setup"></a>

### Connect from the Available tab
<a name="hg-insights-quick-connect"></a>

If you want to use Default OAuth app authentication, you can connect directly from the **Available** tab without additional configuration.

1. In the Amazon Quick console, choose **Connectors**.

1. On the **Available** tab, find **HG Insights** and choose **Connect**.

1. Complete the HG Insights sign-in flow and grant the requested permissions.

To configure a connector with one of the other authentication methods, use the **Create for your team** tab as described below.

### Create from the Create for your team tab
<a name="hg-insights-full-setup"></a>

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **HG Insights**.

1. Enter a **Name** for your connector. Optionally, choose **\+ Add Description** to add a description.

1. For **Connection type**, choose **Public network**.

1. For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.

   1. For **Default OAuth app**:

      No additional credentials are needed. Choose **Next** to continue.

   1. For **Custom OAuth app**, configure the following fields:
      + **Client ID** – The client ID from your HG Insights OAuth app.
      + **Public OAuth client** (Optional) – Select this option if your HG Insights OAuth app is configured as a public client (no client secret).
      + **Client secret** – The client secret from your HG Insights OAuth app.
      + **Token URL** – The token endpoint. Default: `https://phoenix.hginsights.com/api/ai/token`
      + **Authorization URL** – The authorization endpoint. Default: `https://phoenix.hginsights.com/api/ai/authorize`
      + **Redirect URL** – Pre-filled with the Amazon Quick callback URL.

   1. For **Service-to-Service OAuth**, configure the following fields:
      + **Client ID** – The client ID from your HG Insights OAuth app.
      + **Client secret** – The client secret from your HG Insights OAuth app.
      + **Token URL** – The token endpoint. Default: `https://phoenix.hginsights.com/api/ai/token`

   1. For **API Key**, configure the following fields:
      + **API Key** – The HG Insights API key.
      + **Email** (Optional) – The email address associated with the API key.

1. Choose **Next**.

1. If you chose **Default OAuth app** or **Custom OAuth app**, an HG Insights authorization window opens. Review the requested permissions and choose **Allow**.

1. On the **Review** page, review the available actions for the connector. Choose **Next**.

1. On the **Publish** page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.

1. Choose **Publish**.

## Available actions
<a name="hg-insights-integration-actions"></a>

After you set up the connector, the actions exposed by HG Insights are available. To see the current set of actions for your connector, go to the connector's **Available actions** view in the Amazon Quick console.

## Managing and troubleshooting
<a name="hg-insights-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Authentication issues
<a name="hg-insights-troubleshooting-auth"></a>
+ **Sign-in fails (Default OAuth app or Custom OAuth app)** – Verify that your HG Insights account is active. For Custom OAuth app, confirm that the redirect URI in your HG Insights OAuth app matches the Amazon Quick callback URL.
+ **Invalid client credentials (Custom OAuth app or Service-to-Service OAuth)** – Verify that the Client ID and Client secret match the values in your HG Insights OAuth app.
+ **API Key authentication fails** – Verify that the API key has not been revoked.