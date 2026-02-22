# Jira Cloud integration

Connect Amazon Quick to your Jira Cloud instance to manage issues, projects, and other Jira objects. You can create, update, and query Jira content without leaving your Amazon Quick environment. This integration requires Amazon Quick Pro tier or higher.

## What you can do

With Jira Cloud integration, you can perform actions within your Jira instances through the Jira REST API.

**Action connector**

Create, update, and query Jira issues, projects, and other objects through the Jira REST API.

###### Note

This integration supports action execution only. You can't use it to create knowledge bases or access Jira data for search purposes.

## Before you begin

You need the following to set up Jira integration:

- Jira Cloud instance with appropriate permissions.
- Jira user account or API token credentials.
- Amazon Quick Author or higher.
- Administrative access to configure OAuth applications (for user authentication).

## Create a Jira API token

To use API key authentication, create an API token in your Atlassian account.

1. Go to your Atlassian account settings and choose **Security**.
2. Create a new API token for Amazon Quick integration.
3. Copy the generated token to use in your Amazon Quick integration setup.
4. Note your Jira Cloud instance URL and user email address. Your Jira Cloud
   instance URL is a special value for API calls that can be found by navigating to
   `https://`your-domain`.atlassian.net/_edge/tenant_info`.

###### Important

Jira Cloud may return HTTP 200 success responses even when API tokens are revoked or improperly configured.
For more infomration see [JRACLOUD-82932](https://jira.atlassian.com/browse/JRACLOUD-82932 "https://jira.atlassian.com/browse/JRACLOUD-82932").
If your integration appears to connect successfully but actions fail unexpectedly, verify that your
API token is valid and has not been revoked.

## Set up Jira integration

Follow these steps to connect Amazon Quick to your Jira Cloud instance.

1. In the Amazon Quick console, choose **Integrations**.
2. Click **Add** (plus "+" button).
3. Complete the integration details:
   - **Name** - Enter a descriptive name for your Jira integration.
   - **Description** (Optional) - Describe the purpose of this integration.

4. Choose connection type (user or service authentication).
5. Complete the connection settings based on authentication method:
   - **For User authentication (OAuth):**
     - **Base URL** - Your Jira Cloud instance URL. This must be provided in the
       following format:
       `https://api.atlassian.com/ex/jira/`instanceid``.
Your `instanceid`can be found by
navigating to`https://`your-domain`.atlassian.net/\_edge/tenant_info`.
     - **Client ID** - Your Atlassian OAuth app client ID.
     - **Client Secret** - Your Atlassian OAuth app client secret.
     - **Token URL** - Atlassian OAuth token endpoint.
     - **Auth URL** - Atlassian OAuth authorization endpoint.
     - **Redirect URL** - OAuth redirect URI.

   - **For Service authentication (API Key):**
     - **Base URL** - Your Jira Cloud instance URL.
     - **API Key** - Your Jira API token.
     - **Email** - Email address associated with your Jira user account.

6. Select **Create and continue**.
7. Select users to share the integration with.
8. Click **Next**.

## Configure authentication

Jira Cloud integration supports two authentication methods. Choose the method that works best for your organization.

**User authentication (OAuth)**

Use OAuth when you want actions to be performed under individual user identities. Configure these fields:

- **Base URL** - Your Jira Cloud instance URL.
- **Client ID** - Your Atlassian OAuth app client ID.
- **Client Secret** - Your Atlassian OAuth app client secret.
- **Token URL** - Atlassian OAuth token endpoint.
- **Auth URL** - Atlassian OAuth authorization endpoint.
- **Redirect URL** - OAuth redirect URI.

**Required OAuth scopes:**

- `read:jira-user` - Read user information.
- `read:jira-work` - Read issues, projects, and work items.
- `write:jira-work` - Create and modify issues and work items.
- `manage:jira-project` - Manage project settings.
- `manage:jira-configuration` - Manage Jira configuration.
- `manage:jira-webhook` - Manage webhooks.
- `read:sprint:jira-software` - Read sprint information.
- `write:sprint:jira-software` - Create and modify sprints.
- `delete:sprint:jira-software` - Delete sprints.
- `write:board-scope:jira-software` - Manage board configurations.

**Service authentication (API Key)**

Use API key authentication for service-to-service connections. Configure these fields:

- **Base URL** - Your Jira Cloud instance URL.
- **API Key** - Your Jira API token.
- **Email** - Email address associated with your Jira user account.

###### Note

Due to a known Jira Cloud behavior, the integration may appear to connect successfully even with revoked or invalid API tokens. If actions fail unexpectedly after setup, verify your API token is still valid in your Atlassian account settings.

## Available actions

After you create your Jira integration, you can use these actions to interact with Jira Cloud:

- Create, read, update, and delete Jira issues.
- Manage issue transitions and workflows.
- Query issues using JQL (Jira Query Language).
- Manage projects, components, and versions.
- Add comments and attachments to issues.
- Manage user assignments and watchers.
- Access project and issue metadata.

###### Note

The actions you can use depend on the permissions configured in your Jira Cloud instance and your authentication method.

## Share integrations

You can share your Jira action connector with other users in your organization.

1. After you create the integration, choose **Share integration**.
2. Select the users or groups you want to share the integration with.
3. Set appropriate permissions for shared access.
4. Confirm your sharing settings.

## Manage Jira integrations

You can perform these management tasks for your Jira integrations:

- **Edit integration settings** - Update authentication settings or Jira instance configuration.
- **Share integration access** - Make the integration available to other users in your organization.
- **Monitor usage metrics** - View integration activity and API usage metrics.
- **Review available actions** - See the complete list of available Jira actions.
- **Delete integration** - Remove the integration and revoke associated authentication.
