# Slack integration

With Slack integration in Amazon Quick, you can perform actions within Slack workspaces, including sending messages, managing channels, and interacting with Slack APIs. This integration supports action execution only and requires Amazon Quick Pro tier or higher.

## What you can do

With Slack integration, you can perform actions through the action connector.

**Action connector**

Send messages, manage channels, and access Slack APIs through authenticated connections.

## Before you begin

Before you set up Slack integration, make sure you have the following:

- Slack workspace with appropriate permissions.
- Slack app or bot token with required scopes.
- Amazon Quick Author or higher.
- Administrative access to configure OAuth applications (if using user authentication).

## Set up Slack OAuth app

Before you configure the integration, you need to create a Slack app with OAuth capabilities. Follow these steps:

1. Go to the Slack API website and create a new Slack app.
2. Configure OAuth scopes based on the actions you want to perform.
3. Set up redirect URLs to match your Amazon Quick integration configuration.
4. Note the client ID and client secret for use in Amazon Quick integration setup.

## Set up Slack integration

Use the unified Integrations tab in the Amazon Quick console to set up Slack integration for task execution. Follow these steps:

1. In the Amazon Quick console, choose **Integrations**.
2. Choose **Slack** from the integration options, click the Add
   (plus "+") button.
3. Fill in the integration details:
   - **Name** - Descriptive name for your Slack integration.
   - **Description** (Optional) - Purpose of the integration.

4. Choose your connection type (user authentication for Slack).
5. Fill in the connection settings for user authentication:
   1. Configure the following OAuth fields:
      - **Base URL** - Slack API base URL (typically https://slack.com/api).
      - **Client ID** - Slack app client ID.
      - **Client Secret** - Slack app client secret.
      - **Token URL** - Slack OAuth token endpoint.
      - **Auth URL** - Slack OAuth authorization endpoint.
      - **Redirect URL** - OAuth redirect URI configured in your Slack app.

6. Select **Create and continue**.
7. Choose users to share the integration with.
8. Click **Next**.

## Available task actions

After you create your Slack integration, you can review the available actions for interacting with Slack workspaces. Common Slack actions include:

- Send messages to channels or direct messages.
- Create and manage channels.
- Retrieve channel information and member lists.
- Upload and share files.
- Manage user presence and status.
- Access workspace and team information.

###### Note

The specific actions available depend on the OAuth scopes configured in your Slack app and the permissions granted during authentication.

## Share integrations

You can share Slack action connectors with other users in your organization. Follow these steps:

1. After you create the integration, choose **Share integration**.
2. Select users or groups to share the integration with.
3. Set appropriate permissions for shared access.
4. Confirm sharing settings.

Shared users can use the Slack integration to perform actions within the connected Slack workspace, subject to the permissions configured in the original OAuth setup.

## Manage Slack integrations

After you create your Slack integration, you can manage it through the Integrations console using these options:

- **Edit integration** - Update authentication settings or OAuth configuration.
- **Share integration** - Make the integration available to other users in your organization.
- **Monitor usage** - View integration activity and API usage metrics.
- **Review actions** - See the complete list of available Slack actions.
- **Delete integration** - Remove the integration and revoke associated OAuth tokens.

###### Important

Deleting a Slack integration will revoke the OAuth tokens and prevent any shared users from accessing the Slack workspace through Amazon Quick.
