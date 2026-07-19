# Dun & Bradstreet integration

With the Dun & Bradstreet action connector, you can look up company
profiles, credit risk data, and business intelligence directly in Amazon Quick
through natural language.

Amazon Quick supports multiple authentication methods for Dun & Bradstreet.
Choose the method that best fits your organization's security
requirements.

- **Custom OAuth app** – Uses a
  customer-managed OAuth application registered in the Dun & Bradstreet
  developer portal. This option gives your organization full control over
  the OAuth configuration.
- **Service-to-Service OAuth** – Uses
  client credentials for server-to-server authentication without user
  interaction. Suitable for automated workflows.
  For more information about the authentication methods that Amazon Quick
  supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Before you begin

Make sure that you have the following before you set up the
integration.

- An active Dun & Bradstreet D&B Direct+ account with access
  to the data products you want to query.
- For **Custom OAuth app** or
  **Service-to-Service OAuth**: OAuth
  credentials from your Dun & Bradstreet developer portal.
- For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configuring Dun & Bradstreet

For Custom OAuth app or Service-to-Service OAuth authentication,
register an OAuth app in the Dun & Bradstreet developer portal and
add the Amazon Quick callback URL
`https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`
as a redirect URI. Replace `{region}` with
your AWS Region (for example, `us-east-1`). For
authentication details, see [Authentication](https://directplus.documentation.dnb.com/html/pages/Authentication.html "https://directplus.documentation.dnb.com/html/pages/Authentication.html") in the [D&B Direct+
documentation](https://directplus.documentation.dnb.com/ "https://directplus.documentation.dnb.com/"). Record the Client ID and Client Secret —
you need them when you configure Amazon Quick.

## Setting up the connector in Amazon Quick

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Dun & Bradstreet**.
4. Enter a **Name** for your connector. Optionally,
   choose **+ Add Description** to add a description.
5. For **Connection type**, choose **Public
   network**.
6. For **OAuth Configuration**, choose one of the
   following authentication methods and configure the required
   fields.

   1. For **Custom OAuth app**,
      configure the following fields:

      - **Base URL** – The Dun &
        Bradstreet MCP base URL. Default:
        `https://plus.dnb.com/v2/mcp`
      - **Client ID** – The client ID from
        your Dun & Bradstreet OAuth app.
      - **Public OAuth client** (Optional) –
        Select this option if your Dun & Bradstreet OAuth
        app is configured as a public client (no client
        secret).
      - **Client secret** – The client
        secret from your Dun & Bradstreet OAuth app.
      - **Token URL** – The token endpoint.
        Default:
        `https://plus.dnb.com/v2/mcp/token`
      - **Authorization URL** – The
        authorization endpoint. Default:
        `https://plus.dnb.com/v2/mcp/authorize`
      - **Redirect URL** – Pre-filled with
        the Amazon Quick callback URL.

   2. For **Service-to-Service
      OAuth**, configure the following fields:

      - **Base URL** – The Dun &
        Bradstreet MCP base URL. Default:
        `https://plus.dnb.com/v2/mcp`
      - **Client ID** – The client ID from
        your Dun & Bradstreet OAuth app.
      - **Client secret** – The client
        secret from your Dun & Bradstreet OAuth app.
      - **Token URL** – The token endpoint.
        Default:
        `https://plus.dnb.com/v2/mcp/token`

7. Choose **Next**.
8. If you chose **Custom OAuth app**, a
   Dun & Bradstreet authorization window opens. Review the requested
   permissions and choose **Allow**.
9. On the **Review** page, review the available
   actions for the connector. Choose **Next**.
10. On the **Publish** page, choose who can access the
    connector. You can enable access for everyone in your organization or
    search for specific teams or groups.
11. Choose **Publish**.

## Available actions

After you set up the connector, the actions exposed by Dun &
Bradstreet are available. To see the current set of actions for your
connector, go to the connector's **Available actions** view
in the Amazon Quick console.

## Managing and troubleshooting

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **Sign-in fails (Custom OAuth
  app)** – Verify that your Dun & Bradstreet
  account is active. Confirm that the redirect URI in your Dun
  & Bradstreet OAuth app matches the Amazon Quick callback
  URL.
- **Invalid client credentials** –
  Verify that the Client ID and Client secret match the values in
  your Dun & Bradstreet OAuth app.
