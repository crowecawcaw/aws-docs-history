# Smartsheet integration

Use the Smartsheet action connector to manage sheets, rows, reports, and search
across your Smartsheet workspaces directly in Amazon Quick through natural language.
This integration uses the Smartsheet API. For more information, see [Smartsheet
API introduction](https://developers.smartsheet.com/api/smartsheet/introduction "https://developers.smartsheet.com/api/smartsheet/introduction") in the Smartsheet documentation.

Setting up this integration involves two steps. First, you configure credentials
in Smartsheet for your chosen authentication method. Then, you create the integration
in Amazon Quick and connect it to your Smartsheet account. For information about the
authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Prerequisites

Before you set up the integration, make sure that you meet the following requirements:

- A Smartsheet account with a Business or Enterprise plan. Free accounts
  cannot generate API access tokens or register OAuth apps. For more
  information, see [Smartsheet pricing](https://www.smartsheet.com/pricing "https://www.smartsheet.com/pricing") on the Smartsheet website.
- Access to [Smartsheet
  Developer Tools](https://developers.smartsheet.com/ "https://developers.smartsheet.com/") activated for your account. To register, go
  to the [Developer
  Tools Registration](https://developers.smartsheet.com/register "https://developers.smartsheet.com/register") page.
- For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configure Smartsheet Developer Tools

Before you configure Amazon Quick, set up credentials in Smartsheet. The steps
you complete depend on which authentication method you plan to use. Amazon Quick
supports two authentication methods for Smartsheet. For more information about
these methods, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

- **User authentication (OAuth)** – Each
  user signs in with their own Smartsheet account. Actions run with that
  user's permissions. This method uses [Custom OAuth app](quick-action-auth.md#quick-custom-user-auth "quick-action-auth.md#quick-custom-user-auth"). Complete the [Register for Developer Tools and create a developer profile](#smartsheet-register-developer-tools "#smartsheet-register-developer-tools") and [Register the OAuth application](#smartsheet-register-oauth-app "#smartsheet-register-oauth-app") sections below.
- **Service authentication (API key)** –
  All actions run using a single API token. This method uses [API key authentication](quick-action-auth.md#quick-actions-api-key-auth "quick-action-auth.md#quick-actions-api-key-auth"). Complete the [Generate an API access token (service authentication only)](#smartsheet-api-token-setup "#smartsheet-api-token-setup") section below.

For more information about Smartsheet OAuth, see [OAuth](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth") in the Smartsheet API documentation.

### Register for Developer Tools and create a developer profile

1. Go to the [Developer
   Tools Registration](https://developers.smartsheet.com/register "https://developers.smartsheet.com/register") page and register the Smartsheet
   account you want to use with your apps. For more information, see
   [Register for Developer Tools](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#register-for-developer-tools "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#register-for-developer-tools") in the Smartsheet API
   documentation.
2. After Smartsheet activates Developer Tools, sign in to the
   Smartsheet application and choose your **Account**
   icon in the lower-left corner, then choose **Developer
   Tools**.
3. Choose **Create Developer Profile** and enter a
   profile name. For more information, see [Create your developer profile](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#create-your-developer-profile "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#create-your-developer-profile") in the Smartsheet API
   documentation.

###### Tip

Smartsheet recommends using a dedicated service account for OAuth
apps rather than a personal account.

### Register the OAuth application

1. In Smartsheet Developer Tools, choose **Create New
   App**.
2. Complete the form:
   - **App name** – A name to identify your
     app to users.
   - **App description** – A brief description
     of the integration.
   - **App URL** – The URL that launches your
     app, or a landing page.
   - **App contact/support** – Support contact
     information.
   - **App redirect URL** –
     `https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`

   Replace `{region}` with your
   AWS Region (for example,
   `us-east-1`).

3. Choose **Save**. Smartsheet generates the
   **App client ID** and **App
   secret**.
4. Copy the **Client ID** and **Client
   Secret** values. You need these when you configure the
   integration in Amazon Quick.

For more information, see [Register an app](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#register-an-app "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#register-an-app") in the Smartsheet API documentation.

### Generate an API access token (service authentication only)

If you plan to use service authentication instead of OAuth, generate an
API access token. You must have a Business or Enterprise plan to generate
tokens. For more information, see [Generate an API access token](https://help.smartsheet.com/articles/2482389-generate-API-key "https://help.smartsheet.com/articles/2482389-generate-API-key") in the Smartsheet Help
Center.

1. In the Smartsheet application, choose your
   **Account** (profile image) at the bottom of
   the left navigation bar, then choose **Personal
   Settings**.
2. Choose the **API Access** tab and choose
   **Generate new access token**.
3. Name the token and choose **OK**. Copy the token
   value immediately — this is the only time it's visible.

###### Important

Store your access token securely. Anyone with the token can access all
Smartsheet data that the token owner has access to. Do not commit tokens
to version control systems. For best practices on storing tokens, see
[Authentication](https://developers.smartsheet.com/api/smartsheet/guides/basics/authentication "https://developers.smartsheet.com/api/smartsheet/guides/basics/authentication") in the Smartsheet API
documentation.

## OAuth access scopes

When you configure user authentication (OAuth), the integration requests the
following access scopes from Smartsheet. These scopes determine what the
integration can do on behalf of the authenticated user. If you use service
authentication (API key) instead, the integration uses the full permissions of
the token owner and scopes do not apply. For more information, see [Access scopes](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#access-scopes "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#access-scopes") in the Smartsheet API documentation.

| Smartsheet OAuth access scopes | Scope                                                                               | Description |
| ------------------------------ | ----------------------------------------------------------------------------------- | ----------- |
| `READ_SHEETS`                  | Read all sheet data, including attachments, discussions, and<br>cell data.          |
| `WRITE_SHEETS`                 | Insert and modify sheet data, including attachments,<br>discussions, and cell data. |

###### Note

Access scopes don't override existing sharing permissions. For example,
having the `WRITE_SHEETS` scope doesn't allow the integration to
update a sheet on which the user has only viewer-level access. For more
information, see [Resource access levels](https://developers.smartsheet.com/api/smartsheet/guides/basics/resource-access-levels "https://developers.smartsheet.com/api/smartsheet/guides/basics/resource-access-levels") in the Smartsheet API
documentation.

## Set up the integration in Amazon Quick

After you complete the Smartsheet Developer Tools configuration, create the
integration in Amazon Quick.

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Smartsheet**.
4. Enter the integration details:
   - **Name** – Descriptive name for your
     Smartsheet integration.
   - **Description** (Optional) – Purpose of the
     integration.

5. Choose your connection type and fill in the connection settings. For
   more information about these authentication methods, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").
   1. For **User authentication
      (OAuth)**, use the Client ID and Client Secret
      from your Smartsheet Developer Tools app registration.
      Configure the following fields:
      - **Base URL** –
        `https://api.smartsheet.com/2.0`
      - **Client ID** – App client ID from
        your Smartsheet Developer Tools app
        registration.
      - **Client Secret** – App secret from
        your Smartsheet Developer Tools app
        registration.
      - **Token URL** –
        `https://api.smartsheet.com/2.0/token`
      - **Auth URL** –
        `https://app.smartsheet.com/b/authorize`
      - **Redirect URL** –
        `https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`

   2. For **Service authentication (API
      key)**, use the API access token from your
      Smartsheet Personal Settings. Configure the following
      fields:
      - **API Key** – Smartsheet API access
        token generated from your Personal
        Settings.
      - **Base URL** –
        `https://api.smartsheet.com/2.0`
      - **Email** – Email address associated
        with the Smartsheet account that generated the
        token.

6. Choose **Create and continue**.
7. Choose users to share the integration with.
8. Choose **Next**.

For user authentication, go to **Connectors** >
your Smartsheet connector name, and choose
**Sign in** to complete the OAuth authorization flow. In the
Smartsheet consent window, choose **Allow** to grant
access.

###### Important

With service authentication, all actions run using the API token
owner's permissions. Any Amazon Quick user with access to this integration
can perform actions on all Smartsheet resources that the token owner can
access. Scope the token permissions appropriately for your organization's
security requirements.

###### Note

If you use Smartsheet Gov, Smartsheet Regions Europe, or Smartsheet
Regions Australia, use the corresponding base URL for your
environment:

| Smartsheet regional base URLs | Environment                         | Base URL |
| ----------------------------- | ----------------------------------- | -------- |
| Smartsheet                    | `https://api.smartsheet.com/2.0`    |
| Smartsheet Gov                | `https://api.smartsheetgov.com/2.0` |
| Smartsheet Regions Europe     | `https://api.smartsheet.eu/2.0`     |
| Smartsheet Regions Australia  | `https://api.smartsheet.au/2.0`     |

For more information, see [Base URL](https://developers.smartsheet.com/api/smartsheet/guides/basics/base-url "https://developers.smartsheet.com/api/smartsheet/guides/basics/base-url") in the Smartsheet API documentation.

## Available actions

After you set up the integration, the following actions are available.

| Smartsheet available actions | Category     | Action                                                              | Description |
| ---------------------------- | ------------ | ------------------------------------------------------------------- | ----------- |
| Search                       | List Search  | Searches all sheets that the user can access for specified<br>text. |
| Sheets                       | List Sheets  | Lists all sheets that are accessible to the authenticated<br>user.  |
| Sheets                       | Get Sheet    | Gets a sheet and its data based on the sheet ID.                    |
| Reports                      | List Reports | Lists all reports that are accessible to the user.                  |
| Reports                      | View Report  | Gets report details based on the report ID.                         |

## Manage and troubleshoot

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **OAuth authorization fails** –
  Verify that the Client ID and Client Secret match the values in your
  Smartsheet Developer Tools app registration. Confirm the redirect URL
  in Smartsheet matches the URL in your Amazon Quick configuration
  exactly. For a list of OAuth error types, see [OAuth error types](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#oauth-error-types "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#oauth-error-types") in the Smartsheet API
  documentation.
- **Developer Tools not available** –
  Verify that Developer Tools is activated for your Smartsheet account.
  Free accounts do not support Developer Tools. If your request was
  denied, contact your Smartsheet Customer Success
  Manager.
- **API key authentication fails** –
  Verify that the access token has not been revoked. You can manage
  tokens from **Personal Settings** >
  **API Access** in the Smartsheet application.
  For more information, see [Generate an API access token](https://help.smartsheet.com/articles/2482389-generate-API-key "https://help.smartsheet.com/articles/2482389-generate-API-key") in the Smartsheet Help
  Center.
- **Access token expired** – OAuth
  access tokens expire after approximately 7 days. Amazon Quick
  handles token refresh automatically. If you encounter persistent
  token errors, sign out and sign in again from the integration
  settings. For more information, see [Make API calls](https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#make-api-calls "https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth#make-api-calls") in the Smartsheet API
  documentation.

### Common error messages

- **Actions return permission
  errors** – Verify that the authenticated user has the
  required sharing permissions on the target sheets. OAuth scopes don't
  override sharing-level access controls. For more information, see
  [Resource access levels](https://developers.smartsheet.com/api/smartsheet/guides/basics/resource-access-levels "https://developers.smartsheet.com/api/smartsheet/guides/basics/resource-access-levels") in the Smartsheet API
  documentation.
- **Sheet not found** – Verify the
  sheet ID is correct and that the authenticated user has at least
  viewer access to the sheet.
- **API rate limit errors** – The
  Smartsheet API enforces rate limits. For more information, see [Limitations](https://developers.smartsheet.com/api/smartsheet/guides/basics/limitations "https://developers.smartsheet.com/api/smartsheet/guides/basics/limitations") in the Smartsheet API
  documentation.
