# Smartsheet integration

With Smartsheet integration in Amazon Quick Suite, you can perform actions within Smartsheet workspaces, including managing sheets, rows, and collaborative work. This integration supports action execution only and requires Amazon Quick Suite Pro tier or higher.

## What you can do

With Smartsheet integration, you can perform actions within your Smartsheet workspaces through the action connector.

**Action connector**

Create, update, and manage sheets, rows, columns, and collaborative features through the Smartsheet API.

## Set up Smartsheet integration

Follow these steps to create your Smartsheet integration:

1.  In the Amazon Quick Suite console, choose **Integrations**.
2.  Choose **Smartsheet** from the integration options, click the
    Add (plus "+") button.
3.  Fill in the integration details:
    - **Name** - Descriptive name for your Smartsheet integration.
    - **Description** (Optional) - Purpose of the integration.

4.  Choose your connection type:
    - **User authentication** - OAuth-based authentication for individual user access.
    - **Service authentication** - API key-based authentication for service access.

5.  Fill in the connection settings based on your selected authentication method (either user or service):
    1.  For **User authentication (OAuth)**, configure the following fields:

            * **Base URL** - Smartsheet API base URL.
            * **Client ID** - Smartsheet OAuth app client ID.
            * **Client Secret** - Smartsheet OAuth app client secret.
            * **Token URL** - Smartsheet OAuth token endpoint.
            * **Auth URL** - Smartsheet OAuth authorization endpoint.
            * **Redirect URL** - OAuth redirect URI.

        Required OAuth scopes are `READ_SHEETS` and `WRITE_SHEETS`.

    2.  For **Service authentication (API Key)**, configure the following fields:
        - **API Key** - Smartsheet API access token.
        - **Base URL** - Smartsheet API base URL.
        - **Email** - Associated Smartsheet user email.

6.  Select **Create and continue**.
7.  Choose users to share the integration with.
8.  Click **Next**.

## Manage Smartsheet integrations

After you create your Smartsheet integration, you can manage it using these options:

- **Edit integration** - Update authentication settings or Smartsheet configuration.
- **Share integration** - Make the integration available to other users.
- **Delete integration** - Remove the integration and revoke authentication.
