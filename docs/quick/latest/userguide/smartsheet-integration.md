# Smartsheet integration

With the Smartsheet action connector, you can manage sheets, rows, reports,
and search across your Smartsheet workspaces directly in Amazon Quick through
natural language.

Amazon Quick supports two authentication methods for Smartsheet. Choose the
method that best fits your organization's security requirements.

- **Custom OAuth app** – Each user signs in
  with their own Smartsheet account. Actions run with that user's
  permissions. This method uses an OAuth app registered in Smartsheet
  Developer Tools.
- **API Key** – All actions run using a
  single Smartsheet API access token.
  For more information about the authentication methods that Amazon Quick
  supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md"). For more information about
  Smartsheet OAuth, see [OAuth](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth") in the Smartsheet API documentation.

## Before you begin

Make sure that you have the following before you set up the integration.

- A Smartsheet account with a Business or Enterprise plan. Free
  accounts cannot generate API access tokens or register OAuth apps.
  For more information, see [Smartsheet
  pricing](https://www.smartsheet.com/pricing "https://www.smartsheet.com/pricing") on the Smartsheet website.
- For **Custom OAuth app**: Access to
  [Smartsheet Developer
  Tools](https://developers.smartsheet.com/ "https://developers.smartsheet.com/") activated for your account. To register, go to the
  [Developer
  Tools Registration](https://developers.smartsheet.com/register "https://developers.smartsheet.com/register") page.
- For **API Key**: A Smartsheet API
  access token generated from your Smartsheet personal settings.
- For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configuring Smartsheet

Before you configure Amazon Quick, set up credentials in Smartsheet. The
steps you complete depend on which authentication method you plan to
use.

### Register for Developer Tools and create a developer profile (Custom OAuth app)

1. Go to the [Developer
   Tools Registration](https://developers.smartsheet.com/register "https://developers.smartsheet.com/register") page and register the Smartsheet
   account you want to use with your apps. For more information,
   see [Register for Developer Tools](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#register-for-developer-tools "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#register-for-developer-tools") in the Smartsheet API
   documentation.
2. After Smartsheet activates Developer Tools, sign in to the
   Smartsheet application and choose your
   **Account** icon in the lower-left corner, then
   choose **Developer Tools**.
3. Choose **Create Developer Profile** and enter
   a profile name. For more information, see [Create your developer profile](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#create-your-developer-profile "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#create-your-developer-profile") in the Smartsheet API
   documentation.

###### Tip

Smartsheet recommends using a dedicated service account for OAuth
apps rather than a personal account.

### Register the OAuth application (Custom OAuth app)

1. In Smartsheet Developer Tools, choose **Create New
   App**.
2. Complete the form:

   - **App name** – A name to identify your
     app to users.
   - **App description** – A brief
     description of the integration.
   - **App URL** – The URL that launches
     your app, or a landing page.
   - **App contact/support** – Support
     contact information.
   - **App redirect URL** –
     `https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`

   Replace `{region}` with your
   AWS Region (for example, `us-east-1`).

3. Choose **Save**. Smartsheet generates the
   **App client ID** and **App
   secret**.
4. Copy the **Client ID** and **Client
   Secret** values. You need them when you configure
   the connector in Amazon Quick.

For more information, see [Register an app](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#register-an-app "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#register-an-app") in the Smartsheet API documentation.

### Generate an API access token (API Key)

If you plan to use API Key authentication, generate an API access token.
You must have a Business or Enterprise plan to generate tokens. For more
information, see [Generate an API access token](https://help.smartsheet.com/articles/2482389-generate-API-key "https://help.smartsheet.com/articles/2482389-generate-API-key") in the Smartsheet Help Center.

1. In the Smartsheet application, choose your
   **Account** (profile image) at the bottom of
   the left navigation bar, then choose **Personal
   Settings**.
2. Choose the **API Access** tab and choose
   **Generate new access token**.
3. Name the token and choose **OK**. Copy the
   token value immediately — this is the only time it's
   visible.

###### Important

Store your access token securely. Anyone with the token can access
all Smartsheet data that the token owner has access to. Do not commit
tokens to version control systems. For best practices on storing
tokens, see [Authentication](https://developers.smartsheet.com/api/smartsheet/guides/basics/authentication "https://developers.smartsheet.com/api/smartsheet/guides/basics/authentication") in the Smartsheet API documentation.

### OAuth access scopes

When you configure Custom OAuth app, the connector requests the
following access scopes from Smartsheet. These scopes determine what the
connector can do on behalf of the authenticated user. If you use API Key
authentication instead, the connector uses the full permissions of the
token owner and scopes do not apply. For more information, see [Access scopes](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#access-scopes "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#access-scopes") in the Smartsheet API documentation.

Smartsheet OAuth access scopes| Scope | Description |
| --- | --- |
| `READ_SHEETS` | Read all sheet data, including attachments,<br>discussions, and cell data. |
| `WRITE_SHEETS` | Insert and modify sheet data, including attachments,<br>discussions, and cell data. |

###### Note

Access scopes don't override existing sharing permissions. For
example, having the `WRITE_SHEETS` scope doesn't allow the
connector to update a sheet on which the user has only viewer-level
access. For more information, see [Resource access levels](https://developers.smartsheet.com/api/smartsheet/guides/basics/resource-access-levels "https://developers.smartsheet.com/api/smartsheet/guides/basics/resource-access-levels") in the Smartsheet API
documentation.

## Setting up the connector in Amazon Quick

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Smartsheet**.
4. Enter a **Name** for your connector. Optionally,
   choose **+ Add Description** to add a description.
5. For **Connection type**, choose **Public
   network**.
6. For **OAuth Configuration**, choose one of the
   following authentication methods and configure the required
   fields.

   1. For **Custom OAuth app**,
      configure the following fields:

      - **Base URL** – The Smartsheet MCP
        base URL. Example:
        `https://mcp.smartsheet.com`
      - **Client ID** – The client ID from
        your Smartsheet Developer Tools app
        registration.
      - **Public OAuth client** (Optional) –
        Select this option if your Smartsheet OAuth app is
        configured as a public client (no client
        secret).
      - **Client secret** – The client
        secret from your Smartsheet Developer Tools app
        registration.
      - **Token URL** – The Smartsheet
        OAuth token endpoint. Example:
        `https://api.smartsheet.com/2.0/token`
      - **Authorization URL** – The
        Smartsheet OAuth authorization endpoint. Example:
        `https://app.smartsheet.com/b/authorize`
      - **Redirect URL** – Pre-filled with
        the Amazon Quick callback URL.

   2. For **API Key**, configure the
      following fields:

      - **Base URL** – The Smartsheet MCP
        base URL. Example:
        `https://mcp.smartsheet.com`
      - **API Key** – The Smartsheet API
        access token generated from your personal
        settings.
      - **Email** (Optional) – The email
        address associated with the Smartsheet account that
        generated the token.

7. Choose **Next**.
8. If you chose **Custom OAuth app**, a
   Smartsheet authorization window opens. Review the requested
   permissions and choose **Allow**.
9. On the **Review** page, review the available
   actions for the connector. Choose **Next**.
10. On the **Publish** page, choose who can access the
    connector. You can enable access for everyone in your organization or
    search for specific teams or groups.
11. Choose **Publish**.

###### Important

With API Key authentication, all actions run using the API token
owner's permissions. Any Amazon Quick user with access to this connector
can perform actions on all Smartsheet resources that the token owner can
access. Scope the token permissions appropriately for your organization's
security requirements.

###### Note

If you use Smartsheet Gov, Smartsheet Regions Europe, or Smartsheet
Regions Australia, contact Smartsheet for the corresponding MCP base URL
for your environment. The values shown in this guide assume the standard
Smartsheet environment.

## Available actions

After you set up the connector, the actions exposed by the Smartsheet MCP
server are available. To see the current set of actions for your connector,
go to the connector's **Available actions** view in the
Amazon Quick console.

## Managing and troubleshooting

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **OAuth authorization fails** –
  Verify that the Client ID and Client Secret match the values in
  your Smartsheet Developer Tools app registration. Confirm the
  redirect URL in Smartsheet matches the URL in your Amazon Quick
  configuration exactly. For a list of OAuth error types, see
  [OAuth error types](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#oauth-error-types "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#oauth-error-types") in the Smartsheet API
  documentation.
- **Developer Tools not available**
  – Verify that Developer Tools is activated for your Smartsheet
  account. Free accounts do not support Developer Tools. If your
  request was denied, contact your Smartsheet Customer Success
  Manager.
- **API Key authentication fails** –
  Verify that the access token has not been revoked. You can manage
  tokens from **Personal Settings** >
  **API Access** in the Smartsheet
  application. For more information, see [Generate an API access token](https://help.smartsheet.com/articles/2482389-generate-API-key "https://help.smartsheet.com/articles/2482389-generate-API-key") in the Smartsheet Help
  Center.
- **Access token expired** – OAuth
  access tokens expire after approximately 7 days. Amazon Quick
  handles token refresh automatically. If you encounter persistent
  token errors, sign out and sign in again from the connector
  settings. For more information, see [Make API calls](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#make-api-calls "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#make-api-calls") in the Smartsheet API
  documentation.

### Common error messages

- **Actions return permission
  errors** – Verify that the authenticated user has the
  required sharing permissions on the target sheets. OAuth scopes
  don't override sharing-level access controls. For more
  information, see [Resource access levels](https://developers.smartsheet.com/api/smartsheet/guides/basics/resource-access-levels "https://developers.smartsheet.com/api/smartsheet/guides/basics/resource-access-levels") in the Smartsheet API
  documentation.
- **Sheet not found** – Verify the
  sheet ID is correct and that the authenticated user has at least
  viewer access to the sheet.
- **API rate limit errors** – The
  Smartsheet API enforces rate limits. For more information, see
  [Limitations](https://developers.smartsheet.com/api/smartsheet/guides/basics/limitations "https://developers.smartsheet.com/api/smartsheet/guides/basics/limitations") in the Smartsheet API documentation.
