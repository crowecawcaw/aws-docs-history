# Google Chat integration

With the Google Chat action connector, you can send messages, manage spaces,
and interact with chat threads from your Google Workspace account directly in
Amazon Quick through natural language.

Google Chat uses Custom OAuth app authentication. For more information about
the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Before you begin

Make sure that you have the following before you set up the integration.

- An active Google Workspace account with access to the Google Chat
  spaces that you want to use.
- An OAuth 2.0 client registered in the Google Cloud console for your
  Google Workspace project, with the Google Chat API enabled.
- For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configuring Google Cloud

For Custom OAuth app authentication, create an OAuth 2.0 client in
the [Google Cloud
console](https://console.cloud.google.com/ "https://console.cloud.google.com/"), enable the Google Chat API for your project,
configure the OAuth consent screen with the Chat scopes that you
need (for example, `chat.messages`,
`chat.spaces`), and add the Amazon Quick callback URL
`https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`
as an authorized redirect URI. Replace
`{region}` with your AWS Region (for
example, `us-east-1`). For step-by-step instructions,
see [Google Chat API](https://developers.google.com/workspace/chat "https://developers.google.com/workspace/chat") in the Google Workspace developer
documentation. Record the Client ID and Client Secret — you need
them when you configure Amazon Quick.

## Setting up the connector in Amazon Quick

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Google Chat**.
4. Enter a **Name** for your connector. Optionally,
   choose **+ Add Description** to add a description.
5. For **Connection type**, choose **Public
   network**.
6. For **OAuth Configuration**, choose **Custom
   OAuth app** and configure the following fields:

   - **Base URL** – The Google Chat MCP base
     URL.
   - **Client ID** – The OAuth client ID from
     your Google Cloud OAuth 2.0 client.
   - **Public OAuth client** (Optional) –
     Select this option if your Google Cloud OAuth 2.0 client is
     configured as a public client (no client secret).
   - **Client secret** – The client secret from
     your Google Cloud OAuth 2.0 client.
   - **Token URL** – The Google OAuth token
     endpoint.
   - **Authorization URL** – The Google OAuth
     authorization endpoint.
   - **Redirect URL** – Pre-filled with the
     Amazon Quick callback URL.

7. Choose **Next**.
8. A Google sign-in window opens. Review the requested permissions and
   choose **Allow**.
9. On the **Review** page, review the available
   actions for the connector. Choose **Next**.
10. On the **Publish** page, choose who can access the
    connector. You can enable access for everyone in your organization or
    search for specific teams or groups.
11. Choose **Publish**.

## Available actions

After you set up the connector, the actions exposed by Google Chat are
available. To see the current set of actions for your connector, go to the
connector's **Available actions** view in the Amazon Quick
console.

## Managing and troubleshooting

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **Sign-in fails** – Verify that
  your Google Workspace account is active and that you can sign in
  to Google Chat directly. Confirm that the authorized redirect URI
  in your Google Cloud OAuth 2.0 client matches the Amazon Quick
  callback URL.
- **Invalid client credentials** –
  Verify that the Client ID and Client Secret match the values in
  your Google Cloud OAuth 2.0 client.
- **Insufficient permissions** –
  Verify that the Chat API is enabled and that your OAuth consent
  screen includes the required scopes for the operations you want
  to use.
