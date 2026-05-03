# Zendesk Suite integration

With Zendesk Suite integration in Amazon Quick, you can perform actions within Zendesk instances, including managing tickets, users, and customer support workflows. For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## What you can do

With Zendesk Suite integration, you can perform actions within your Zendesk instances through the action connector.

**Action connector**

Create, update, and manage tickets, users, and customer support processes through the Zendesk API.

## Set up Zendesk integration

Follow these steps to create your Zendesk integration:

1.  In the Amazon Quick console, choose **Connectors**.
2.  Choose the **Create for your team** tab.
3.  Find and choose **Zendesk Suite**.
4.  Fill in the integration details:
    - **Name** - Descriptive name for your Zendesk integration.
    - **Description** (Optional) - Purpose of the integration.

5.  Choose your connection type:
    - **User authentication** - OAuth-based authentication for individual user access.
    - **Service authentication** - API key-based authentication for service access.

6.  Fill in the connection settings based on your selected authentication method (either user or service):
    1.  For **User authentication (OAuth)**, configure the following fields:

            * **Base URL** - Zendesk instance URL.
            * **Client ID** - Zendesk OAuth app client ID.
            * **Client Secret** - Zendesk OAuth app client secret.
            * **Token URL** - Zendesk OAuth token endpoint.
            * **Auth URL** - Zendesk OAuth authorization endpoint.
            * **Redirect URL** - OAuth redirect URI.

        Required OAuth scopes are `tickets:read`, `tickets:write`, and `read`.

    2.  For **Service authentication (API Key)**, configure the following fields:
        - **API Key** - Zendesk API token.
        - **Base URL** - Zendesk instance URL.
        - **Email** - Associated Zendesk user email.

7.  Select **Create and continue**.
8.  Choose users to share the integration with.
9.  Click **Next**.

## Manage Zendesk integrations

After you create your Zendesk integration, you can manage it using these options:

- **Edit integration** - Update authentication settings or Zendesk configuration.
- **Share integration** - Make the integration available to other users.
- **Delete integration** - Remove the integration and revoke authentication.
