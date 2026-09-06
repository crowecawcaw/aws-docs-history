

# Moodys GenAI Ready Data integration
<a name="moodys-integration"></a>

With the Moodys GenAI Ready Data connector, you can access credit ratings, financial research, and risk analytics data directly in Amazon Quick through natural language.

Amazon Quick supports two authentication methods for Moodys GenAI Ready Data. Choose the method that best fits your organization's security requirements.
+ **Default OAuth app** – Uses an AWS-managed OAuth application. No additional credentials are needed. Users authenticate directly with their Moody's account.
+ **Custom OAuth app** – Uses a customer-managed OAuth application. This option gives your organization full control over the OAuth configuration.

For more information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="moodys-integration-prerequisites"></a>

Make sure that you have the following before you set up the integration.
+ An active Moody's account with access to Moodys GenAI Ready Data.
+ For **Custom OAuth app**: An OAuth app configured in your Moody's developer portal with the Amazon Quick callback URL added as a redirect URI.
+ For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configuring Moody's
<a name="moodys-source-setup"></a>

If you are using **Default OAuth app** authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#moodys-quicksuite-setup).

For Custom OAuth app authentication, register an OAuth app in your Moody's developer portal and add the Amazon Quick callback URL `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback` as a redirect URI. Replace {{{region}}} with your AWS Region (for example, `us-east-1`). Record the Client ID and Client Secret — you need them when you configure Amazon Quick.

## Setting up the connector in Amazon Quick
<a name="moodys-quicksuite-setup"></a>

### Connect from the Available tab
<a name="moodys-quick-connect"></a>

If you want to use Default OAuth app authentication, you can connect directly from the **Available** tab without additional configuration.

1. In the Amazon Quick console, choose **Connectors**.

1. On the **Available** tab, find **Moodys GenAI Ready Data** and choose **Connect**.

1. Complete the Moody's sign-in flow and grant the requested permissions.

To configure a connector with Custom OAuth app instead, use the **Create for your team** tab as described below.

### Create from the Create for your team tab
<a name="moodys-full-setup"></a>

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Moodys GenAI Ready Data**.

1. Enter a **Name** for your connector. Optionally, choose **\+ Add Description** to add a description.

1. For **Connection type**, choose **Public network**.

1. For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.

   1. For **Default OAuth app**:

      No additional credentials are needed. Choose **Next** to continue.

   1. For **Custom OAuth app**, configure the following fields:
      + **Client ID** – The client ID from your Moody's OAuth app.
      + **Public OAuth client** (Optional) – Select this option if your Moody's OAuth app is configured as a public client (no client secret).
      + **Client secret** – The client secret from your Moody's OAuth app.
      + **Token URL** – The token endpoint. Default: `https://api.moodys.com/genai-ready-data/oauth/token`
      + **Authorization URL** – The authorization endpoint. Default: `https://api.moodys.com/genai-ready-data/oauth/authorize`
      + **Redirect URL** – Pre-filled with the Amazon Quick callback URL.

1. Choose **Next**.

1. A Moody's authorization window opens. Review the requested permissions and choose **Allow**.

1. On the **Review** page, review the available actions for the connector. Choose **Next**.

1. On the **Publish** page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.

1. Choose **Publish**.

## Available actions
<a name="moodys-integration-actions"></a>

After you set up the connector, the actions exposed by Moodys GenAI Ready Data are available. To see the current set of actions for your connector, go to the connector's **Available actions** view in the Amazon Quick console.

## Managing and troubleshooting
<a name="moodys-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Authentication issues
<a name="moodys-troubleshooting-auth"></a>
+ **Sign-in fails (Default OAuth app or Custom OAuth app)** – Verify that your Moody's account is active and that you can sign in to the Moody's portal directly. For Custom OAuth app, confirm that the redirect URI in your Moody's OAuth app matches the Amazon Quick callback URL.
+ **Invalid client credentials (Custom OAuth app)** – Verify that the Client ID and Client secret match the values in your Moody's OAuth app.