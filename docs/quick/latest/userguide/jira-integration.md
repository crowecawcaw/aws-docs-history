

# Atlassian Jira Cloud integration
<a name="jira-integration"></a>

Use the Atlassian Jira Cloud connector to create, update, search, and manage Jira issues, projects, sprints, and users directly in Amazon Quick through natural language.

Setting up this integration involves two steps. First, you create an OAuth 2.0 (3LO) app in the Atlassian Developer Console and configure its permissions. Then, you create the integration in Amazon Quick and connect it to your Atlassian app. For information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="jira-integration-prerequisites"></a>

Make sure you have the following before you set up the integration.
+ Atlassian Jira Cloud.
+ Access to the [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/) to create or manage an OAuth app.
+ For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configure the Atlassian Developer Console
<a name="jira-atlassian-setup"></a>

If you plan to use user authentication (3LO), create an OAuth 2.0 app in the Atlassian Developer Console before you configure Amazon Quick. Complete all of the following steps before moving to the Amazon Quick console.

If you plan to use service authentication (API Key) only, you can skip this section and proceed to [Set up the integration in Amazon Quick](#jira-integration-setup).

For more information about OAuth 2.0 (3LO) apps, see [OAuth 2.0 (3LO) apps](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/) in the Atlassian developer documentation.

### Create an OAuth 2.0 (3LO) app
<a name="atlassian-oauth-app"></a>

Amazon Quick uses an Atlassian OAuth 2.0 (3LO) app to authenticate with your Atlassian Cloud product on behalf of your users. Create this app in the Atlassian Developer Console before you configure Amazon Quick.

1. Open the [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/) and sign in with your Atlassian account.

1. Choose **Create**, then choose **OAuth 2.0 integration**.

1. For **Name**, enter a descriptive name for your integration, for example `{{your-app-name}} connector`.

1. Review and accept the Atlassian developer terms.

1. Choose **Create**.

### Configure permissions
<a name="atlassian-oauth-permissions"></a>

After you create the OAuth 2.0 app, add the API permissions that Amazon Quick needs to interact with your Atlassian product.

1. From your app in the Atlassian Developer Console, choose **Permissions** in the left navigation.

1. Find the API for your Atlassian product (for example, **Jira API** or **Confluence API**) and choose **Add**. The button changes to **Configure** after the API is added.

1. Choose **Configure**. The scopes page opens with **Classic scopes** and **Granular scopes** tabs.

1. On the **Classic scopes** tab, choose **Edit Scopes**. Select the required classic scopes and choose **Save**.

1. Choose the **Granular scopes** tab, then choose **Edit Scopes**. Select the required granular scopes and choose **Save**.

For the specific scopes required for your integration, see the scopes section that follows.

### Configure API permissions
<a name="jira-oauth-scopes"></a>

Add the following scopes to your OAuth 2.0 app for the Jira Cloud action integration.

**Classic scopes**

On the **Classic scopes** tab, choose **Edit Scopes** and select the following scopes.


**Jira action integration – classic scopes**  

| Scope | Description | 
| --- | --- | 
| read:jira-work | Read Jira project and issue data, search for issues, and objects associated with issues like attachments and worklogs. | 
| manage:jira-project | Create and edit project settings and create new project-level objects (for example, versions and components). | 
| manage:jira-configuration | Take Jira administration actions (for example, create projects and custom fields, view workflows, manage issue link types). | 
| read:jira-user | View user information in Jira that the user has access to, including usernames, email addresses, and avatars. | 
| write:jira-work | Create and edit issues in Jira, post comments as the user, create worklogs, and delete issues. | 
| manage:jira-webhook | Fetch, register, refresh, and delete dynamically declared Jira webhooks. | 

**Granular scopes**

Choose the **Granular scopes** tab, then choose **Edit Scopes**. Use the search bar to find the scopes below. For example, search for `sprint:jira-software` to find sprint-related scopes.


**Jira action integration – granular scopes**  

| Scope | Description | 
| --- | --- | 
| read:board-scope:jira-software | Read board configurations. | 
| read:sprint:jira-software | Read sprint information. | 
| write:sprint:jira-software | Create and modify sprints. | 
| delete:sprint:jira-software | Delete sprints. | 
| write:board-scope:jira-software | Manage board configurations. | 
| read:project:jira | Read project details. | 

### Configure authorization
<a name="atlassian-oauth-authorization"></a>

Set the callback URL so that Atlassian can redirect users back to Amazon Quick after they authorize the app.

1. From your app in the Atlassian Developer Console, choose **Authorization** in the left navigation.

1. Next to **OAuth 2.0 (3LO)**, choose **Add**.

1. For **Callback URLs**, enter `https://{{region}}.quicksight.aws.amazon.com/sn/oauthcallback`. Replace {{region}} with the AWS Region where your Amazon Quick instance is deployed, for example `us-east-1`.

1. Choose **Save changes**.

### Record your credentials
<a name="atlassian-oauth-credentials"></a>

Before you leave the Atlassian Developer Console, confirm that you have the following values. You need them for the Amazon Quick configuration.

1. From your app in the Atlassian Developer Console, choose **Settings** in the left navigation.

1. Under **Authentication details**, copy the **Client ID** and **Secret** values.


**Required credentials from Atlassian Developer Console**  

| Value | Where to find it | 
| --- | --- | 
| Client ID | Settings page, under Authentication details | 
| Secret | Settings page, under Authentication details | 

## Set up the integration in Amazon Quick
<a name="jira-integration-setup"></a>

After you prepare your authentication credentials, create the integration in Amazon Quick.

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Atlassian Jira Cloud**.

1. In the **Create integration** wizard, fill in the following fields:
   + **Name** – Descriptive name for your Jira integration.
   + **Description** (Optional) – Notes about how this connection will be used.
   + **Connection type** – Choose **Public network**.

1. Under **Authentication settings**, choose your authentication method and fill in the required fields:

   1. For **User authentication**, configure the following fields:
      + **Base URL** – Your Jira instance URL for API calls. This is not the same URL that users log into. It resembles the following: `https://api.atlassian.com/ex/jira/{{yourInstanceId}}`. To find your instance ID, navigate to `https://{{your-domain}}.atlassian.net/_edge/tenant_info`.
      + **Client ID** – Client ID from the Settings page of your Atlassian OAuth app.
      + **Client secret** – Secret from the Settings page of your Atlassian OAuth app.
      + **Token URL** – `https://auth.atlassian.com/oauth/token`
      + **Authorization URL** – `https://auth.atlassian.com/authorize`
      + **Redirect URL** – This field is pre-populated with your Amazon Quick callback URL.

   1. For **Service authentication**, configure the following fields:
      + **API Key** – Jira API token.
      + **Base URL** – Your Jira instance URL for API calls.
      + **Email** – Associated user account email.

1. Choose **Create and continue**.

1. (Optional) On the **Share integration** page, choose users to share the integration with.

**Important**  
Jira Cloud may return HTTP 200 success responses even when API tokens are revoked or improperly configured. For more information, see [JRACLOUD-82932](https://jira.atlassian.com/browse/JRACLOUD-82932). If your integration appears to connect successfully but actions fail unexpectedly, verify that your API token is valid and has not been revoked.

## Available actions
<a name="jira-integration-actions"></a>

After you set up the integration, the following actions are available.


**Jira Cloud available actions**  

| Action | Description | 
| --- | --- | 
| Add Attachment | Add an attachment to an issue. | 
| Add Comment | Add new comment. | 
| Change Issue Status | Change task status of an issue. | 
| Create Issue | Create new issue or subtask. | 
| Create Project | Create new project. | 
| Create Sprint | Create a sprint in a project. | 
| Delete Comment | Remove comment. | 
| Delete Issue | Delete an issue in a project. | 
| Delete Project | Remove project. | 
| Delete Sprint | Delete a sprint in a project. | 
| Edit Issue | Modify issue. | 
| Find Users | Search for a Jira user. | 
| Get All Labels | View all labels. | 
| Get All Users | List all Jira users. | 
| Get Attachment Content | View the contents of an attachment. | 
| Get Comments | View issue comments. | 
| Get Issue | View details of an issue in a project. | 
| Get Issue Types For Project | View project issue types. | 
| Get Priorities | View issue priorities. | 
| Get Project | View project details. | 
| Get Sprint | View details of a sprint in a project. | 
| Move Issues to Backlog | Move issues to backlog. | 
| Move Issues To Sprint And Rank | Assign an issue to a sprint. | 
| Search Issues | Search for issues. | 
| Search Projects | Find visible projects. | 
| Search Statuses | Search issue statuses. | 
| Update Comment | Edit comment. | 
| Update Project | Modify project. | 
| Update Sprint | Update sprint details. | 

**Note**  
The actions you can use depend on the permissions configured in your Jira Cloud instance and your authentication method.

## Manage and troubleshoot
<a name="jira-integration-troubleshooting"></a>

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Authentication issues
<a name="jira-troubleshooting-auth"></a>
+ **Incorrect app configuration** – Verify the OAuth app in the Atlassian Developer Console includes the required scopes and that the redirect URI matches your Amazon Quick configuration.
+ **Expired or revoked API token** – If using service authentication, check that the API token has not expired or been revoked. Due to a known Jira Cloud behavior ([JRACLOUD-82932](https://jira.atlassian.com/browse/JRACLOUD-82932)), the integration may appear to connect successfully even with invalid tokens.
+ **Incorrect Base URL** – The Base URL for API calls is not the same as the Jira Cloud login URL. Verify you are using the API URL format: `https://api.atlassian.com/ex/jira/{{yourInstanceId}}`. To find your instance ID, navigate to `https://{{your-domain}}.atlassian.net/_edge/tenant_info`.

### Common error messages
<a name="jira-troubleshooting-errors"></a>
+ **`Access denied. You do not have permission to perform this action`** – The authenticated user does not have the required permissions in Jira Cloud. Contact your Jira Cloud administrator to verify and grant appropriate permissions.
+ **`OAuth 2.0 authorization failed`** – Verify the client ID, client secret, and OAuth scopes are configured correctly in both the Atlassian Developer Console and Amazon Quick.