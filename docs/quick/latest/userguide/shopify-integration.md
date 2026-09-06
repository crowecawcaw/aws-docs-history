# Shopify integration

With the Shopify connector, you can manage products, orders, customers,
and store operations directly in Amazon Quick through natural language.

Shopify uses Custom OAuth app authentication. For more information about the
authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Before you begin

Make sure that you have the following before you set up the integration.

- An active Shopify store with admin access.
- A custom app registered in your Shopify admin or in the Shopify
  Partners portal, with the Admin API access scopes that you need.
- For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configuring Shopify

For Custom OAuth app authentication, create a custom app in your
Shopify store admin or in the [Shopify Partners
portal](https://partners.shopify.com/ "https://partners.shopify.com/") on the Shopify website. Configure the Admin API
access scopes that match the operations you want to use, and add the
Amazon Quick callback URL
`https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`
as an allowed redirection URL. Replace
`{region}` with your AWS Region (for
example, `us-east-1`). For step-by-step instructions, see
[Authentication and authorization](https://shopify.dev/docs/apps/build/authentication-authorization "https://shopify.dev/docs/apps/build/authentication-authorization") in the Shopify
developer documentation. Record the Client ID (API key) and Client
Secret (API secret key) — you need them when you configure
Amazon Quick.

## Setting up the connector in Amazon Quick

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Shopify**.
4. Enter a **Name** for your connector. Optionally,
   choose **+ Add Description** to add a description.
5. For **Connection type**, choose **Public
   network**.
6. For **OAuth Configuration**, choose **Custom
   OAuth app** and configure the following fields:

   - **Base URL** – The Shopify MCP base URL
     for your store.
   - **Client ID** – The Client ID (API key)
     from your Shopify custom app.
   - **Public OAuth client** (Optional) –
     Select this option if your Shopify custom app is configured
     as a public client (no client secret).
   - **Client secret** – The Client Secret
     (API secret key) from your Shopify custom app.
   - **Token URL** – The Shopify OAuth token
     endpoint for your store.
   - **Authorization URL** – The Shopify OAuth
     authorization endpoint for your store.
   - **Redirect URL** – Pre-filled with the
     Amazon Quick callback URL.

7. Choose **Next**.
8. A Shopify authorization window opens. Review the requested
   permissions and choose **Install app** or the
   equivalent button.
9. On the **Review** page, review the available
   actions for the connector. Choose **Next**.
10. On the **Publish** page, choose who can access the
    connector. You can enable access for everyone in your organization or
    search for specific teams or groups.
11. Choose **Publish**.

## Available actions

After you set up the connector, the actions exposed by Shopify are
available. To see the current set of actions for your connector, go to the
connector's **Available actions** view in the Amazon Quick
console.

## Managing and troubleshooting

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **Sign-in fails** – Verify that
  you can sign in to your Shopify store admin directly. Confirm
  that the allowed redirection URL in your Shopify custom app
  matches the Amazon Quick callback URL.
- **Invalid client credentials** –
  Verify that the Client ID (API key) and Client Secret (API secret
  key) match the values in your Shopify custom app.
- **Insufficient permissions** –
  Verify that the Admin API access scopes configured on your
  Shopify custom app match the operations you want to use.
