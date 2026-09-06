# Zapier integration

With the Zapier connector, you can trigger workflows across thousands
of applications that Zapier connects to, directly in Amazon Quick through natural
language. Use this connector to extend the action capabilities of Amazon Quick
to any application that you have already configured in your Zapier
account.

Amazon Quick supports multiple authentication methods for Zapier. Choose the
method that best fits your organization's security requirements.

- **Default OAuth app** – Uses an
  AWS-managed OAuth application. No additional credentials are needed.
  Users authenticate directly with their Zapier account.
- **Custom OAuth app** – Uses a
  customer-managed OAuth application configured in your Zapier account.
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

- An active Zapier account with the actions or Zaps that you want to
  expose configured.
- The Amazon Quick integration requires Zapier MCP **Agentic Mode** to work correctly.
  Managed Mode is not supported.
- For **Custom OAuth app** or
  **Service-to-Service OAuth**: OAuth
  credentials from your Zapier MCP configuration.
- For **API Key**: A Zapier-issued API
  key.
- For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configuring Zapier

If you are using **Default OAuth app**
authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#zapier-quicksuite-setup "#zapier-quicksuite-setup").

For Custom OAuth app or Service-to-Service OAuth authentication,
configure your [Zapier
MCP](https://mcp.zapier.com/ "https://mcp.zapier.com/") settings on the Zapier website and add the
Amazon Quick callback URL
`https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`
as a redirect URI. Replace `{region}` with
your AWS Region (for example, `us-east-1`). Record the
Client ID and Client Secret — you need them when you configure
Amazon Quick. For API Key authentication, generate an API key from
your Zapier account.

## Setting up the connector in Amazon Quick

### Connect from the Available tab

If you want to use Default OAuth app authentication, you can connect
directly from the **Available** tab without additional
configuration.

1. In the Amazon Quick console, choose
   **Connectors**.
2. On the **Available** tab, find
   **Zapier** and choose
   **Connect**.
3. Complete the Zapier sign-in flow and grant the requested
   permissions.

To configure a connector with one of the other authentication methods,
use the **Create for your team** tab as described
below.

### Create from the Create for your team tab

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Zapier**.
4. Enter a **Name** for your connector. Optionally,
   choose **+ Add Description** to add a
   description.
5. For **Connection type**, choose **Public
   network**.
6. For **OAuth Configuration**, choose one of the
   following authentication methods and configure the required
   fields.

   1. For **Default OAuth app**:

   No additional credentials are needed. Choose
   **Next** to continue. 2. For **Custom OAuth app**,
   configure the following fields:

        * **Client ID** – The client ID
         from your Zapier OAuth app.
        * **Public OAuth client**
         (Optional) – Select this option if your Zapier
         OAuth app is configured as a public client (no
         client secret).
        * **Client secret** – The client
         secret from your Zapier OAuth app.
        * **Token URL** – The token
         endpoint. Default:
         `https://mcp.zapier.com/token`
        * **Authorization URL** – The
         authorization endpoint. Default:
         `https://mcp.zapier.com/authorize`
        * **Redirect URL** – Pre-filled
         with the Amazon Quick callback URL.

   3. For **Service-to-Service
   OAuth**, configure the following fields:

        * **Client ID** – The client ID
         from your Zapier OAuth app.
        * **Client secret** – The client
         secret from your Zapier OAuth app.
        * **Token URL** – The token
         endpoint. Default:
         `https://mcp.zapier.com/token`

   4. For **API Key**, configure
   the following fields:

        * **API Key** – The Zapier API
         key.
        * **Email** (Optional) – The
         email address associated with the API key.

7. Choose **Next**.
8. If you chose **Default OAuth app**
   or **Custom OAuth app**, a Zapier
   authorization window opens. Review the requested permissions and
   choose **Allow**.
9. On the **Review** page, review the available
   actions for the connector. The available actions depend on the
   Zaps that you have configured in your Zapier account. Choose
   **Next**.
10. On the **Publish** page, choose who can access
    the connector. You can enable access for everyone in your
    organization or search for specific teams or groups.
11. Choose **Publish**.

## Available actions

After you set up the connector, the actions that you exposed in your
Zapier account are available. Each Zap or action that you authorized in
Zapier registers as a callable tool in Amazon Quick. To see the current set
of actions for your connector, go to the connector's **Available
actions** view in the Amazon Quick console.

## Managing and troubleshooting

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **Sign-in fails (Default OAuth app or
  Custom OAuth app)** – Verify that your Zapier
  account is active and that you can sign in to Zapier directly.
  For Custom OAuth app, confirm that the redirect URI in your
  Zapier OAuth app matches the Amazon Quick callback URL.
- **Invalid client credentials (Custom
  OAuth app or Service-to-Service OAuth)** – Verify
  that the Client ID and Client secret match the values in your
  Zapier OAuth app.
- **API Key authentication fails** –
  Verify that the API key has not been revoked.
- **Expected actions are missing** –
  Verify that the Zaps or actions that you want to use are
  configured and enabled in your Zapier account.
