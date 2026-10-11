

# Figma integration
<a name="figma-integration"></a>

Figma is a collaborative design platform where teams create, share, and manage design files and prototypes. The Figma connector brings your design work into Amazon Quick. You can ask questions in natural language to manage design files, retrieve file metadata, and access design assets without switching to the Figma application.

With Amazon Quick, you can use two authentication methods for Figma. Choose the method that best fits your organization's security requirements:
+ **Default OAuth app** – Uses an OAuth application managed by AWS. No additional credentials are needed. Users authenticate directly with their Figma account.
+ **Custom OAuth app** – Uses a customer-managed OAuth application. This option gives your organization full control over the OAuth configuration.

For more information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="figma-integration-prerequisites"></a>

Make sure that you have the following before you set up the integration:
+ An active Figma account with access to the files and projects that you want to use.
+ For **Custom OAuth app**: An OAuth app configured in the Figma Developer settings. For more information, see [Figma OAuth 2.0](https://www.figma.com/developers/api#oauth2) in the Figma developer documentation.
+ For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configuring Figma
<a name="figma-source-setup"></a>

If you are using **Default OAuth app** authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#figma-quicksuite-setup).

For Custom OAuth app authentication, create an OAuth app in your Figma Developer settings and configure it to work with Amazon Quick.

1. Sign in to Figma and go to your Figma Developer settings.

1. Create an OAuth app. For step-by-step instructions, see [Figma OAuth 2.0](https://www.figma.com/developers/api#oauth2) in the Figma developer documentation.

1. Add the Amazon Quick callback URL as a redirect URI: `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback`. Replace {{{region}}} with your AWS Region (for example, `us-east-1`).

1. Record the Client ID and Client Secret that Figma generates. You need these values when you configure the connector in Amazon Quick.

## Setting up the connector in Amazon Quick
<a name="figma-quicksuite-setup"></a>

### Connect from the Available tab
<a name="figma-quick-connect"></a>

If you want to use Default OAuth app authentication, you can connect directly from the **Available** tab without additional configuration.

1. In the Amazon Quick console, choose **Connectors**.

1. On the **Available** tab, find **Figma** and choose **Connect**.

1. Complete the Figma sign-in flow and grant the requested permissions.

To configure a connector with Custom OAuth app instead, use the **Create for your team** tab, as described in the following section.

### Create from the Create for your team tab
<a name="figma-full-setup"></a>

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Figma**.

1. Enter a **Name** for your connector. Optionally, choose **\+ Add Description** to add a description.

1. For **Connection type**, choose **Public network**.

1. For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.

   1. For **Default OAuth app**:

      No additional credentials are needed. Choose **Next** to continue.

   1. For **Custom OAuth app**, configure the following fields:
      + **Client ID** – The client ID from your Figma OAuth app.
      + (Optional) **Public OAuth client** – Select this option if your Figma OAuth app is configured as a public client (no client secret).
      + **Client secret** – The client secret from your Figma OAuth app.
      + **Token URL** – The token endpoint. Default: `https://api.figma.com/v1/oauth/token`
      + **Authorization URL** – The authorization endpoint. Default: `https://www.figma.com/oauth/mcp`
      + **Redirect URL** – Pre-filled with the Amazon Quick callback URL.

1. Choose **Next**.

1. A Figma authorization window opens. Review the requested permissions and choose **Allow access**.

1. On the **Review** page, review the available actions for the connector. Choose **Next**.

1. On the **Publish** page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.

1. Choose **Publish**.

## Available actions
<a name="figma-integration-actions"></a>

After you set up the connector, the actions exposed by Figma are available. To see the current set of actions for your connector, go to the connector's **Available actions** view in the Amazon Quick console.

## Managing and troubleshooting
<a name="figma-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Authentication issues
<a name="figma-troubleshooting-auth"></a>
+ **Sign-in fails (Default OAuth app or Custom OAuth app)** – Verify that your Figma account is active and that you can sign in to Figma directly. For Custom OAuth app, confirm that the redirect URI in your Figma OAuth app matches the Amazon Quick callback URL.
+ **Invalid client credentials (Custom OAuth app)** – Verify that the Client ID and Client secret match the values in your Figma OAuth app.