

# WhatsApp integration
<a name="whatsapp-integration"></a>

With the WhatsApp connector, you can send and manage messages through WhatsApp Business directly in Amazon Quick through natural language.

WhatsApp uses Custom OAuth app authentication. For more information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="whatsapp-prerequisites"></a>

Make sure that you have the following before you set up the integration.
+ An active WhatsApp Business account with access to the WhatsApp Business Platform.
+ A registered phone number for sending messages.
+ An app registered in the Meta for Developers portal with the WhatsApp Business product configured.
+ For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configuring Meta for Developers
<a name="whatsapp-source-setup"></a>

For Custom OAuth app authentication, register an app in [Meta for Developers](https://developers.facebook.com/) on the Meta website and add the WhatsApp Business product. Configure your phone number and message templates, and add the Amazon Quick callback URL `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback` as a valid OAuth redirect URI. Replace {{{region}}} with your AWS Region (for example, `us-east-1`). For step-by-step instructions, see [WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api) in the Meta for Developers documentation. Record the App ID (Client ID) and App Secret (Client Secret) — you need them when you configure Amazon Quick.

## Setting up the connector in Amazon Quick
<a name="whatsapp-quicksuite-setup"></a>

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **WhatsApp**.

1. Enter a **Name** for your connector. Optionally, choose **\+ Add Description** to add a description.

1. For **Connection type**, choose **Public network**.

1. For **OAuth Configuration**, choose **Custom OAuth app** and configure the following fields:
   + **Base URL** – The WhatsApp MCP base URL.
   + **Client ID** – The App ID from your Meta for Developers app.
   + **Public OAuth client** (Optional) – Select this option if your Meta app is configured as a public client (no client secret).
   + **Client secret** – The App Secret from your Meta for Developers app.
   + **Token URL** – The Meta OAuth token endpoint.
   + **Authorization URL** – The Meta OAuth authorization endpoint.
   + **Redirect URL** – Pre-filled with the Amazon Quick callback URL.

1. Choose **Next**.

1. A Meta authorization window opens. Review the requested permissions and choose **Continue**.

1. On the **Review** page, review the available actions for the connector. Choose **Next**.

1. On the **Publish** page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.

1. Choose **Publish**.

## Available actions
<a name="whatsapp-actions"></a>

After you set up the connector, the actions exposed by WhatsApp are available. To see the current set of actions for your connector, go to the connector's **Available actions** view in the Amazon Quick console.

## Managing and troubleshooting
<a name="whatsapp-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Authentication issues
<a name="whatsapp-troubleshooting-auth"></a>
+ **Sign-in fails** – Verify that your Meta for Developers app is active and that the WhatsApp Business product is configured. Confirm that the OAuth redirect URI in your Meta app matches the Amazon Quick callback URL.
+ **Invalid client credentials** – Verify that the App ID (Client ID) and App Secret (Client Secret) match the values in your Meta for Developers app.
+ **Phone number or template errors** – Verify that the phone number is registered and that any message templates you reference are approved in the WhatsApp Business Platform.