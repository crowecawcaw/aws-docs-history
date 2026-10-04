

# Gong integration
<a name="gong-integration"></a>

Gong is a revenue intelligence platform that captures and analyzes your customer interactions across calls, emails, and meetings. The Gong connector brings that data into Amazon Quick. You can ask questions in natural language and get answers grounded in your team's sales activity. For example, you can check the health of a deal, summarize a recent call, or prepare for an upcoming meeting without switching to the Gong application.

With Amazon Quick, you can use two authentication methods for Gong. Choose the method that best fits your organization's security requirements:
+ **Default OAuth app** – Uses an OAuth application managed by AWS. No additional credentials are needed. Users authenticate directly with their Gong account.
+ **Custom OAuth app** – Uses a customer-managed OAuth application. This option gives your organization full control over the OAuth configuration, including the authorization scopes that the app requests.

For more information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="gong-integration-prerequisites"></a>

Make sure that you have the following before you set up the integration:
+ An active Gong account.
+ For **Custom OAuth app**: A Gong user with the **Tech admin** role. You need this role to create and manage OAuth applications in Gong. You also need an OAuth app registered in your Gong admin center with the Amazon Quick callback URL added as a redirect URI. For instructions, see [Configuring Gong](#gong-source-setup).
+ For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configuring Gong
<a name="gong-source-setup"></a>

If you are using **Default OAuth app** authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#gong-quicksuite-setup).

For Custom OAuth app authentication, create an OAuth app in your Gong admin center and configure it to work with Amazon Quick.

1. Sign in to your Gong account as a Tech admin.

1. Go to **Admin center** > **Settings** > **Ecosystem** > **API**.

1. On the **INTEGRATIONS** tab, choose **Create Integration**.

1. Enter an integration name and description for your application.

1. In the **Required authorization scopes** section, select the scopes that your integration needs. For information about which APIs use which scopes, see the [Gong API documentation](https://gong.app.gong.io/settings/api/documentation).

1. For **Redirect URI**, enter the Amazon Quick callback URL: `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback`. Replace {{{region}}} with your AWS Region (for example, `us-east-1`).

1. Choose **Save**.

1. Record the **Client ID** and **Client Secret** that Gong generates. You need these values when you configure the connector in Amazon Quick.

For more information about creating OAuth apps in Gong, see [Create an OAuth app for Gong](https://help.gong.io/docs/create-an-app-for-gong) in the Gong documentation.

## Setting up the connector in Amazon Quick
<a name="gong-quicksuite-setup"></a>

### Connect from the Available tab
<a name="gong-quick-connect"></a>

If you want to use Default OAuth app authentication, you can connect directly from the **Available** tab without additional configuration.

1. In the Amazon Quick console, choose **Connectors**.

1. On the **Available** tab, find **Gong** and choose **Connect**.

1. Complete the Gong sign-in flow and grant the requested permissions.

To configure a connector with Custom OAuth app instead, use the **Create for your team** tab, as described in the following section.

### Create from the Create for your team tab
<a name="gong-full-setup"></a>

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Gong**.

1. Enter a **Name** for your connector. Optionally, choose **\+ Add Description** to add a description.

1. For **Connection type**, choose **Public network**.

1. For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.

   1. For **Default OAuth app**:

      No additional credentials are needed. Choose **Next** to continue.

   1. For **Custom OAuth app**, configure the following fields:
      + **Client ID** – The client ID from your Gong OAuth app.
      + (Optional) **Public OAuth client** – Select this option if your Gong OAuth app is configured as a public client (no client secret).
      + **Client secret** – The client secret from your Gong OAuth app.
      + **Token URL** – The token endpoint. Default: `https://app.gong.io/oauth2/generate-customer-token`
      + **Authorization URL** – The authorization endpoint. Default: `https://app.gong.io/oauth2/authorize`
      + **Redirect URL** – Pre-filled with the Amazon Quick callback URL.

1. Choose **Next**.

1. A Gong authorization window opens. Review the requested permissions and choose **Allow**.

1. On the **Review** page, review the available actions for the connector. Choose **Next**.

1. On the **Publish** page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.

1. Choose **Publish**.

## Available actions
<a name="gong-integration-actions"></a>

After you set up the connector, you can use the following Gong tools in Amazon Quick to analyze your conversation and revenue data:

**`ask_account` and `ask_deal`**  
Analyze the calls and emails associated with the selected account or deal. Each request analyzes the selected data independently. If you ask the same question multiple times, or ask multiple questions about the same account or deal, each request consumes Gong credits based on the data analyzed for that request. The amount of consumption depends on the volume of calls and emails included in the analysis.

**`generate_brief`**  
Analyzes the calls and emails associated with the selected account, deal, or contact and returns a structured summary. Brief consumption depends on both the amount of data analyzed and the number of sections included in the brief. Each open-ended section performs its own analysis of the selected conversations. Briefs with more open-ended sections consume more Gong credits than briefs with fewer sections.

**Gong credit consumption**  
All Gong actions consume Gong credits based on the volume of conversation data that each request analyzes. Repeated questions and briefs with more open-ended sections increase consumption.

## Managing and troubleshooting
<a name="gong-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Authentication issues
<a name="gong-troubleshooting-auth"></a>
+ **Sign-in fails (Default OAuth app or Custom OAuth app)** – Verify that your Gong account is active and that you can sign in to Gong directly. Confirm that the user has the Tech admin role or has been granted the required permissions. For Custom OAuth app, confirm that the redirect URI in your Gong OAuth app matches the Amazon Quick callback URL.
+ **Invalid client credentials (Custom OAuth app)** – Verify that the Client ID and Client secret match the values in your Gong OAuth app. Gong uses a global-level OAuth flow rather than user-level OAuth.
+ **Insufficient scopes** – If actions return authorization errors, verify that the OAuth app in Gong has the required authorization scopes selected. You can update scopes in the Gong admin center under **Settings** > **Ecosystem** > **API**.