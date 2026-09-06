# Adobe Marketing Agent integration

With the Adobe Marketing Agent connector, you can work with Adobe
Experience Platform marketing data and AI-powered marketing capabilities directly
in Amazon Quick through natural language.

Amazon Quick supports multiple authentication methods for Adobe Marketing
Agent. Choose the method that best fits your organization's security
requirements.

- **Default OAuth app** – Uses an
  AWS-managed OAuth application. No additional credentials are needed.
  Users authenticate directly with their Adobe account.
- **Custom OAuth app** – Uses a
  customer-managed application registered in Adobe Developer Console. This
  option gives your organization full control over the OAuth
  configuration.
- **Service-to-Service OAuth** – Uses
  client credentials for server-to-server authentication without user
  interaction. Suitable for automated workflows.
- **API Key** – Uses an API key for
  authentication. Suitable for service-account access patterns.
  For more information about the authentication methods that Amazon Quick
  supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Before you begin

Make sure that you have the following before you set up the
integration.

- An active Adobe account with access to Adobe Marketing Agent.
- For **Custom OAuth app** or
  **Service-to-Service OAuth**: Access to
  [Adobe Developer
  Console](https://developer.adobe.com/console "https://developer.adobe.com/console") on the Adobe website to create an app and obtain
  client credentials.
- For **API Key**: An Adobe-issued API
  key with the required marketing data access scopes.
- For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configuring Adobe

If you are using **Default OAuth app**
authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#adobe-quicksuite-setup "#adobe-quicksuite-setup").

For Custom OAuth app or Service-to-Service OAuth authentication,
register an app in [Adobe Developer
Console](https://developer.adobe.com/console "https://developer.adobe.com/console") on the Adobe website and add the Amazon Quick
callback URL
`https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`
as a redirect URI. Replace `{region}` with
your AWS Region (for example, `us-east-1`). Record the
Client ID and Client Secret — you need them when you configure
Amazon Quick. For API Key authentication, generate an API key from
your Adobe account.

## Setting up the connector in Amazon Quick

### Connect from the Available tab

If you want to use Default OAuth app authentication, you can connect
directly from the **Available** tab without additional
configuration.

1. In the Amazon Quick console, choose
   **Connectors**.
2. On the **Available** tab, find **Adobe
   Marketing Agent** and choose
   **Connect**.
3. Complete the Adobe sign-in flow and grant the requested
   permissions.

To configure a connector with one of the other authentication methods,
use the **Create for your team** tab as described
below.

### Create from the Create for your team tab

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Adobe Marketing Agent**.
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
         from your Adobe Developer Console app.
        * **Public OAuth client**
         (Optional) – Select this option if your Adobe
         Developer Console app is configured as a public
         client (no client secret).
        * **Client secret** – The client
         secret from your Adobe Developer Console app.
        * **Token URL** – The token
         endpoint. Default:
         `https://aep-ai-ama.adobe.io/token`
        * **Authorization URL** – The
         authorization endpoint. Default:
         `https://aep-ai-ama.adobe.io/authorize`
        * **Redirect URL** – Pre-filled
         with the Amazon Quick callback URL.

   3. For **Service-to-Service
   OAuth**, configure the following fields:

        * **Client ID** – The client ID
         from your Adobe Developer Console
         Server-to-Server credential.
        * **Client secret** – The client
         secret from your Adobe Developer Console
         Server-to-Server credential.
        * **Token URL** – The token
         endpoint. Default:
         `https://aep-ai-ama.adobe.io/token`

   4. For **API Key**, configure
   the following fields:

        * **API Key** – The Adobe API
         key.
        * **Email** (Optional) – The
         email address associated with the API key.

7. Choose **Next**.
8. If you chose **Default OAuth app**
   or **Custom OAuth app**, an Adobe
   authorization window opens. Review the requested permissions and
   choose **Allow**.
9. On the **Review** page, review the available
   actions for the connector. Choose **Next**.
10. On the **Publish** page, choose who can access
    the connector. You can enable access for everyone in your
    organization or search for specific teams or groups.
11. Choose **Publish**.

## Available actions

After you set up the connector, the actions exposed by Adobe Marketing
Agent are available. To see the current set of actions for your connector,
go to the connector's **Available actions** view in the
Amazon Quick console.

## Managing and troubleshooting

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **Sign-in fails (Default OAuth app or
  Custom OAuth app)** – Verify that your Adobe account
  is active and that you can sign in to Adobe directly. For Custom
  OAuth app, confirm that the redirect URI in your Adobe Developer
  Console app matches the Amazon Quick callback URL.
- **Invalid client credentials (Custom
  OAuth app or Service-to-Service OAuth)** – Verify
  that the Client ID and Client secret match the values in your
  Adobe Developer Console app.
- **API Key authentication fails** –
  Verify that the API key has not been revoked and that it has the
  required scopes for the operations you want to perform.
