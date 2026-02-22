# Zendesk Suite integration

With Zendesk Suite integration in Amazon Quick, you can perform actions within Zendesk instances, including managing tickets, users, and customer support workflows. This integration supports action execution only and requires Amazon Quick Pro tier or higher.

## What you can do

With Zendesk Suite integration, you can perform actions within your Zendesk instances through the action connector.

**Action connector**

Create, update, and manage tickets, users, and customer support processes through the Zendesk API.

## Set up Zendesk integration

Follow these steps to create your Zendesk integration:

1.  In the Amazon Quick console, choose **Integrations**.
2.  Choose **Zendesk Suite** from the integration options, click
    the Add (plus "+") button.
3.  Fill in the integration details:
    - **Name** - Descriptive name for your Zendesk integration.
    - **Description** (Optional) - Purpose of the integration.

4.  Choose your connection type:
    - **User authentication** - OAuth-based authentication for individual user access.
    - **Service authentication** - API key-based authentication for service access.

5.  Fill in the connection settings based on your selected authentication method (either user or service):
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

6.  Select **Create and continue**.
7.  Choose users to share the integration with.
8.  Click **Next**.

## Manage Zendesk integrations

After you create your Zendesk integration, you can manage it using these options:

- **Edit integration** - Update authentication settings or Zendesk configuration.
- **Share integration** - Make the integration available to other users.
- **Delete integration** - Remove the integration and revoke authentication.
