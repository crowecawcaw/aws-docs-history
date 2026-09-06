# Cisco Webex Meetings integration

With the Cisco Webex Meetings connector, you can schedule and manage
meetings, retrieve recordings, and access participant information directly in
Amazon Quick through natural language.

Amazon Quick supports multiple authentication methods for Cisco Webex Meetings.
Choose the method that best fits your organization's security
requirements.

- **Custom OAuth app** – Uses a
  customer-managed application registered in the Webex Developer portal.
  This option gives your organization full control over the OAuth
  configuration.
- **Service-to-Service OAuth** – Uses
  client credentials for server-to-server authentication without user
  interaction. Suitable for automated workflows.
- **API Key** – Uses an API key for
  authentication.
  For more information about the authentication methods that Amazon Quick
  supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Before you begin

Make sure that you have the following before you set up the
integration.

- An active Cisco Webex account with access to Webex Meetings.
- For **Custom OAuth app** or
  **Service-to-Service OAuth**: Access to
  the [Webex Developer
  portal](https://developer.webex.com/ "https://developer.webex.com/") on the Cisco website to create an integration and
  obtain client credentials.
- For **API Key**: A Webex personal
  access token or API key with the required scopes.
- For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configuring Cisco Webex

For Custom OAuth app or Service-to-Service OAuth authentication,
create an integration in the [Webex Developer portal](https://developer.webex.com/ "https://developer.webex.com/")
on the Cisco website and add the Amazon Quick callback URL
`https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`
as a redirect URI. Replace `{region}` with
your AWS Region (for example, `us-east-1`). For
step-by-step instructions, see [Webex Meetings MCP Server](https://developer.webex.com/meeting/docs/meetings-mcp-server "https://developer.webex.com/meeting/docs/meetings-mcp-server") in the Webex developer
documentation. Record the Client ID and Client Secret — you need
them when you configure Amazon Quick. For API Key authentication,
generate a Webex personal access token or API key with the required
scopes.

## Setting up the connector in Amazon Quick

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Cisco Webex Meetings**.
4. Enter a **Name** for your connector. Optionally,
   choose **+ Add Description** to add a description.
5. For **Connection type**, choose **Public
   network**.
6. For **OAuth Configuration**, choose one of the
   following authentication methods and configure the required
   fields.

   1. For **Custom OAuth app**,
      configure the following fields:

      - **Base URL** – The Webex Meetings
        MCP base URL. Default:
        `https://mcp.webexapis.com/mcp/webex-meeting`
      - **Client ID** – The client ID from
        your Webex Developer portal integration.
      - **Public OAuth client** (Optional) –
        Select this option if your Webex integration is
        configured as a public client (no client secret).
      - **Client secret** – The client
        secret from your Webex Developer portal
        integration.
      - **Token URL** – The token endpoint.
        Default:
        `https://webexapis.com/v1/access_token`
      - **Authorization URL** – The
        authorization endpoint. Default:
        `https://webexapis.com/v1/authorize`
      - **Redirect URL** – Pre-filled with
        the Amazon Quick callback URL.

   2. For **Service-to-Service
      OAuth**, configure the following fields:

      - **Base URL** – The Webex Meetings
        MCP base URL. Default:
        `https://mcp.webexapis.com/mcp/webex-meeting`
      - **Client ID** – The client ID from
        your Webex Service App.
      - **Client secret** – The client
        secret from your Webex Service App.
      - **Token URL** – The token endpoint.
        Default:
        `https://webexapis.com/v1/access_token`

   3. For **API Key**, configure the
      following fields:

      - **Base URL** – The Webex Meetings
        MCP base URL. Default:
        `https://mcp.webexapis.com/mcp/webex-meeting`
      - **API Key** – The Webex API
        key or personal access token.
      - **Email** (Optional) – The email
        address associated with the API key.

7. Choose **Next**.
8. If you chose **Custom OAuth app**, a
   Webex authorization window opens. Review the requested permissions
   and choose **Accept**.
9. On the **Review** page, review the available
   actions for the connector. Choose **Next**.
10. On the **Publish** page, choose who can access the
    connector. You can enable access for everyone in your organization or
    search for specific teams or groups.
11. Choose **Publish**.

## Available actions

After you set up the connector, the actions exposed by Cisco Webex
Meetings are available. To see the current set of actions for your
connector, go to the connector's **Available actions** view
in the Amazon Quick console.

## Managing and troubleshooting

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **Sign-in fails (Custom OAuth
  app)** – Verify that your Cisco Webex account is
  active and that you can sign in to Webex directly. Confirm that
  the redirect URI in your Webex Developer portal integration
  matches the Amazon Quick callback URL.
- **Invalid client credentials** –
  Verify that the Client ID and Client secret match the values in
  your Webex Developer portal integration or Service App.
- **API Key authentication fails** –
  Verify that the API key has not been revoked and that it has the
  required scopes for Webex Meetings operations.
