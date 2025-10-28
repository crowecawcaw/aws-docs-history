# ServiceNow integration

With ServiceNow integration in Amazon Quick Suite, you can perform actions within ServiceNow instances, including managing incidents, requests, and other ServiceNow records. This integration supports action execution only and requires Amazon Quick Suite Pro tier or higher.

## What you can do

With ServiceNow integration, you can perform actions within your ServiceNow instances through the action connector.

**Action connector**

Create, update, and query ServiceNow records such as incidents, requests, changes, and custom tables.

###### Note

ServiceNow integration doesn't support data access or knowledge base creation. It's designed specifically for action execution and API interactions with ServiceNow instances.

## Before you begin

Before you set up ServiceNow integration, make sure you have the following:

- ServiceNow instance with appropriate permissions.
- ServiceNow user account or service account credentials.
- Amazon Quick Suite Author or higher.
- Administrative access to configure OAuth applications (if using user authentication).

## Set up ServiceNow integration

Follow these steps to create your ServiceNow integration:

1.  In the Amazon Quick Suite console, choose **Integrations**.
2.  Choose **ServiceNow** from the integration options, click the
    Add (plus "+") button.
3.  Fill in the integration details:
    - **Name** - Descriptive name for your ServiceNow integration.
    - **Description** (Optional) - Purpose of the integration.

4.  Choose your connection type:
    - **User authentication** - OAuth-based authentication for individual user access.
    - **Service authentication** - API key-based authentication for service access.

5.  Fill in the connection settings based on your selected authentication method (either user or service):
    1.  For **User authentication (OAuth)**, configure the following fields:

            * **Base URL** - ServiceNow instance URL (for example, https://your-instance.service-now.com).
            * **Client ID** - ServiceNow OAuth application client ID.
            * **Client Secret** - ServiceNow OAuth application client secret.
            * **Token URL** - ServiceNow OAuth token endpoint.
            * **Auth URL** - ServiceNow OAuth authorization endpoint.
            * **Redirect URL** - OAuth redirect URI.

        ServiceNow OAuth authentication doesn't require specific OAuth scopes - access is controlled through ServiceNow's role-based permissions system.

    2.  For **Service authentication (API Key)**, configure the following fields:
        - **API Key** - ServiceNow API access token.
        - **Base URL** - ServiceNow instance URL.
        - **Email** - Associated ServiceNow user email.

6.  Select **Create and continue**.
7.  Choose users to share the integration with.
8.  Click **Next**.

## Available actions

After you create your ServiceNow integration, you can review the available actions for interacting with ServiceNow instances. Common ServiceNow actions include:

- Create, read, update, and delete (CRUD) operations on ServiceNow tables.
- Manage incidents, requests, and change records.
- Query ServiceNow data using REST API.
- Execute ServiceNow workflows and business rules.
- Manage user accounts and group memberships.
- Access ServiceNow reports and analytics.

###### Note

The specific actions available depend on the permissions configured in your ServiceNow instance and the authentication method used.

## Manage ServiceNow integrations

After you create your ServiceNow integration, you can manage it using these options:

- **Edit integration** - Update authentication settings or ServiceNow instance configuration.
- **Share integration** - Make the integration available to other users in your organization.
- **Monitor usage** - View integration activity and API usage metrics.
- **Review actions** - See the complete list of available ServiceNow actions.
- **Delete integration** - Remove the integration and revoke associated authentication.
