# Atlassian Confluence Cloud action integration

Use the Atlassian Confluence Cloud connector to create, update, and manage
Confluence pages and spaces directly in Amazon Quick through natural language.

To set up this integration, you first create an OAuth 2.0 (3LO) app in the Atlassian
Developer Console and configure its permissions. Then, you create the integration in
Amazon Quick and connect it to your Atlassian app. For information about the
authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Before you begin

Make sure you have the following before you set up the integration.

- Atlassian Confluence Cloud.
- Access to the [Atlassian
  Developer Console](https://developer.atlassian.com/console/myapps/ "https://developer.atlassian.com/console/myapps/") to create or manage an OAuth app.
- For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configure the Atlassian Developer Console

If you plan to use user authentication (3LO), create an OAuth 2.0 app in the
Atlassian Developer Console before you configure Amazon Quick. Complete all of the
following steps before moving to the Amazon Quick console.

If you plan to use service authentication (API Key) only, you can skip this
section and proceed to [Prepare authentication](#confluence-action-auth-setup "#confluence-action-auth-setup").

For more information about OAuth 2.0 (3LO) apps, see [OAuth 2.0 (3LO) apps](https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/ "https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/") in the Atlassian developer
documentation.

### Create an OAuth 2.0 (3LO) app

Amazon Quick uses an Atlassian OAuth 2.0 (3LO) app to authenticate with
your Atlassian Cloud product on behalf of your users. Create this app in the
Atlassian Developer Console before you configure Amazon Quick.

1. Open the [Atlassian
   Developer Console](https://developer.atlassian.com/console/myapps/ "https://developer.atlassian.com/console/myapps/") and sign in with your Atlassian
   account.
2. Choose **Create**, then choose **OAuth 2.0
   integration**.
3. For **Name**, enter a descriptive name for your
   integration, for example
   ``your-app-name`
 connector`.
4. Review and accept the Atlassian developer terms.
5. Choose **Create**.

### Configure permissions

After you create the OAuth 2.0 app, add the API permissions that
Amazon Quick needs to interact with your Atlassian product.

1. From your app in the Atlassian Developer Console, choose
   **Permissions** in the left navigation.
2. Find the API for your Atlassian product (for example,
   **Jira API** or
   **Confluence API**) and choose
   **Add**. The button changes to
   **Configure** after the API is added.
3. Choose **Configure**. The scopes page opens with
   **Classic scopes** and
   **Granular scopes** tabs.
4. On the **Classic scopes** tab, choose
   **Edit Scopes**. Select the required classic
   scopes and choose **Save**.
5. Choose the **Granular scopes** tab, then choose
   **Edit Scopes**. Select the required granular
   scopes and choose **Save**.

For the specific scopes required for your integration, see the scopes
section that follows.

### Required scopes for Confluence

Add the following scopes to your OAuth 2.0 app for the Confluence Cloud action
integration.

**Classic scope**

On the **Classic scopes** tab, choose
**Edit Scopes** and select the following scope.

Confluence action integration – classic scope| Scope | Description |
| --- | --- |
| `search:confluence` | Search Confluence content and space summaries. |

**Granular scopes**

Choose the **Granular scopes** tab, then choose
**Edit Scopes**. Select the following scopes.

Confluence action integration – granular scopes| Scope | Description |
| --- | --- |
| `read:page:confluence` | View page content. |
| `write:page:confluence` | Create and update pages. |
| `read:space:confluence` | Access space information. |

### Configure authorization

Set the callback URL so that Atlassian can redirect users back to
Amazon Quick after they authorize the app.

1. From your app in the Atlassian Developer Console, choose
   **Authorization** in the left navigation.
2. Next to **OAuth 2.0 (3LO)**, choose
   **Add**.
3. For **Callback URLs**, enter
   `https://`region`.quicksight.aws.amazon.com/sn/oauthcallback`.
   Replace `region` with the AWS Region
   where your Amazon Quick instance is deployed, for example
   `us-east-1`.
4. Choose **Save changes**.

### Record your credentials

Before you leave the Atlassian Developer Console, confirm that you have
the following values. You need them for the Amazon Quick configuration.

1. From your app in the Atlassian Developer Console, choose
   **Settings** in the left navigation.
2. Under **Authentication details**, copy the
   **Client ID** and **Secret**
   values.

Required credentials from Atlassian Developer Console| Value | Where to find it |
| --- | --- |
| Client ID | Settings page, under Authentication details |
| Secret | Settings page, under Authentication details |

## Prepare authentication

Confluence Cloud connectors support two authentication methods. Gather the
required credentials before configuring Amazon Quick.

**User authentication (3LO)**

If you completed the Atlassian Developer Console setup in the previous
section, you should have the following values ready. Enter these when you
configure the integration in Amazon Quick.

- **Base URL** – Your Confluence instance URL
  for API calls. This is not the same URL that users log into. It
  resembles the following:
  `https://api.atlassian.com/ex/confluence/`yourInstanceId``.
  To find your instance ID, navigate to
  `https://`your-domain`.atlassian.net/_edge/tenant_info`.
- **Client ID** – From the Settings page of your Atlassian OAuth app.
- **Client secret** – From the Settings page of your Atlassian OAuth app.
- **Token URL** –
  `https://auth.atlassian.com/oauth/token`
- **Authorization URL** –
  `https://auth.atlassian.com/authorize`
- **Redirect URL** –
  `https://`region`.quicksight.aws.amazon.com/sn/oauthcallback`

**Service authentication (API Key)**

Gather the following information from your Confluence Cloud administrator:

- **API Key** – Confluence API token.
- **Base URL** – Your Confluence instance URL for API calls.
- **Email** – Associated user account email.

## Set up the integration in Amazon Quick

After you prepare your authentication credentials, create the integration in
Amazon Quick.

1. In the Amazon Quick console, choose **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Atlassian Confluence Cloud**.
4. On the **Integration type** page, select
   **Perform actions in Atlassian Confluence Cloud** and
   choose **Next**.
5. In the **Create integration** form, fill in the
   following fields:

   - **Name** – Descriptive name for your Confluence
     integration.
   - **Description** (Optional) – Notes about how
     this connection will be used.
   - **Connection type** – Choose
     **Public network**.

6. Under **Authentication settings**, choose your
   authentication method and fill in the required fields:

   1. For **User authentication**,
      configure the following fields:

      - **Base URL** – Your Confluence instance URL for API calls,
        in the format
        `https://api.atlassian.com/ex/confluence/`yourInstanceId``.
        To find your instance ID, navigate to
        `https://`your-domain`.atlassian.net/_edge/tenant_info`.
      - **Client ID** – Client ID from the Settings page of your Atlassian OAuth app.
      - **Client secret** – Secret from the Settings page of your Atlassian OAuth app.
      - **Token URL** –
        `https://auth.atlassian.com/oauth/token`
      - **Authorization URL** –
        `https://auth.atlassian.com/authorize`
      - **Redirect URL** – This field is
        pre-populated with your Amazon Quick callback URL.

   2. For **Service authentication**,
      configure the following fields:

      - **API Key** – Confluence API token.
      - **Base URL** – Your Confluence instance URL for API calls.
      - **Email** – Associated user account email.

7. Choose **Create and continue**.
8. (Optional) On the **Share integration** page, choose
   users to share the integration with.

## Available actions

After you set up the integration, the following actions are available.

Confluence Cloud available actions| Action | Description |
| --- | --- |
| Create Page | Create a new page. |
| Get Pages | View all pages. |
| Search | Search content using CQL. |
| Update Page | Update page content. |

## Manage and troubleshoot

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **Incorrect app configuration** – Verify
  the OAuth app in the Atlassian Developer Console includes the required
  scopes and that the redirect URI matches your Amazon Quick
  configuration.
- **Expired API token** – If using service
  authentication, check that the API token has not expired and generate a
  new one if needed.
- **Incorrect Base URL** – The Base URL for
  API calls is not the same as the Confluence Cloud login URL. Verify you are
  using the API URL format:
  `https://api.atlassian.com/ex/confluence/`yourInstanceId``.
  To find your instance ID, navigate to
  `https://`your-domain`.atlassian.net/_edge/tenant_info`.

### Common error messages

- **`Access denied. You do not have
 permission to perform this action`** – The
  authenticated user does not have the required permissions in Confluence Cloud.
  Contact your Confluence Cloud administrator to verify and grant appropriate
  permissions.
- **`OAuth 2.0 authorization failed`** –
  Verify the client ID, client secret, and OAuth scopes are configured
  correctly in both the Atlassian Developer Console and Amazon Quick.
