

# Gmail integration
<a name="gmail-integration"></a>

With the Gmail connector, you can access Gmail directly in Amazon Quick through natural language. You can read and send emails, manage labels and drafts, organize threads, and search contacts without leaving Amazon Quick.

Amazon Quick supports multiple authentication methods for Gmail. Choose the method that best fits your organization's security requirements.
+ **Default OAuth app** – Uses an AWS-managed OAuth application. No additional credentials are needed. You authenticate directly with your Google account.
+ **Custom OAuth app** – Uses a customer-managed OAuth client created in the Google Cloud Console. This option gives your organization full control over the OAuth configuration.

For more information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="gmail-integration-prerequisites"></a>

Make sure that you have the following before you set up the integration.
+ A Google account with access to Gmail.
+ For **Custom OAuth app**: Access to the [Google Cloud Console](https://console.cloud.google.com/) on the Google website with permissions to create OAuth clients.
+ For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configuring Google Cloud
<a name="gmail-source-setup"></a>

If you use **Default OAuth app** authentication, skip this section and see [Setting up the connector in Amazon Quick](#gmail-quicksuite-setup).

For Custom OAuth app authentication, complete the following steps in the Google Cloud Console before you configure Amazon Quick. When you enable the API in step 3, search for and enable the **Gmail API**.

### Create an OAuth client in Google Cloud Console
<a name="w2aac46c28c89c19b7"></a>

Create an OAuth client in the Google Cloud Console to get the client credentials that you need for Amazon Quick. For more information, see [Using OAuth 2.0 to Access Google APIs](https://developers.google.com/identity/protocols/oauth2) on the Google website.

1. Sign in to the [Google Cloud Console](https://console.cloud.google.com/) on the Google website.

1. Create a new project or select an existing project.

1. In the left navigation pane, choose **APIs & Services**, then choose **Library**. Search for the API that your integration requires and choose **Enable**.

1. Choose **OAuth consent screen** and choose **Get Started**.

1. Configure the consent screen:
   + Enter an **App Name** and select a **User support email**.
   + For **Audience**, choose **Internal** (your organization only) or **External** (any Google user).
   + Add developer contact details and choose **Create**.

1. Choose **Create OAuth client**.

1. Configure the client:
   + For **Application type**, choose **Web application**.
   + Enter a **Name** for your client.
   + Under **Authorized redirect URIs**, add the Amazon Quick callback URL: `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback`

1. Choose **Create**.

1. Record the following values. You need them when you configure Amazon Quick.
   + **Client ID**
   + **Client secret**

### Recommended scopes
<a name="gmail-oauth-scopes"></a>

The following scopes are requested when you connect to Gmail.


**Gmail recommended scopes**  

| Scope | Description | 
| --- | --- | 
| https://www.googleapis.com/auth/gmail.modify | Reads, sends, and manages emails and labels. | 
| https://www.googleapis.com/auth/gmail.send | Sends emails on behalf of the user. | 
| https://www.googleapis.com/auth/contacts.readonly | Reads contact information. | 
| openid | Authenticates the user's identity. | 
| email | Reads the user's email address. | 

**Note**  
The `openid` and `email` scopes are automatically included in the OAuth consent flow for user authentication. They are not required for Service-to-Service OAuth.

## Setting up the connector in Amazon Quick
<a name="gmail-quicksuite-setup"></a>

### Connect from the Available tab
<a name="gmail-quick-connect"></a>

If you want to use Default OAuth app authentication, you can connect directly from the **Available** tab without additional configuration.

1. In the Amazon Quick console, choose **Connectors**.

1. On the **Available** tab, find **Gmail** and choose **Connect**.

1. Complete the Google sign-in flow and grant the requested permissions.

To configure a connector with Custom OAuth app instead, use the **Create for your team** tab as described below.

### Create from the Create for your team tab
<a name="gmail-full-setup"></a>

After you complete any required Google Cloud configuration, create the connector in Amazon Quick.

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Gmail**.
**Note**  
If a Gmail connector already exists, a dialog appears with your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.

1. Enter a **Name** for your connector. Optionally, choose **\+ Add Description** to add a description.

1. For **Connection type**, choose **Public network**.

1. For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.

   1. For **Default OAuth app**:

      No additional credentials are needed. Choose **Next** to continue.

   1. For **Custom OAuth app**, configure the following fields:
      + **Base URL** (Optional) – The Gmail API base URL. For example: `https://gmail.googleapis.com`
      + **Client ID** – The client ID from your Google Cloud OAuth client.
      + **Client secret** – The client secret from your Google Cloud OAuth client.
      + **Token URL** – The token endpoint. For example: `https://oauth2.googleapis.com/token`
      + **Authorization URL** – The authorization endpoint. For example: `https://accounts.google.com/o/oauth2/v2/auth`
      + **Redirect URL** – Pre-filled with the Amazon Quick callback URL.

1. Choose **Next**.

1. If you chose **Default OAuth app** or **Custom OAuth app**, a Google authorization window opens. Review the requested permissions and choose **Allow**.

1. On the **Review** page, review the available actions for the connector. Choose **Next**.

1. On the **Publish** page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.

1. Choose **Publish**.

## Available actions
<a name="gmail-integration-actions"></a>

After you set up the connector, the following actions are available.


**Gmail available actions**  

| Category | Action | Description | 
| --- | --- | --- | 
| Messages | Get Emails | Retrieves emails from the mailbox. | 
| Messages | Get Message By Thread Id | Retrieves a message by its thread ID. | 
| Messages | Get Message By Message Id | Retrieves a message by its message ID. | 
| Messages | Send Email | Sends a new email message. | 
| Messages | Send Thread Reply | Replies to an existing email thread. | 
| Messages | Forward Message | Forwards an email to other recipients. | 
| Messages | Get Attachment | Retrieves an email attachment. | 
| Messages | Batch Update Message | Modifies labels on multiple messages in a single operation. | 
| Threads | List Threads | Lists email threads in the mailbox. | 
| Threads | Update Thread Labels | Modifies labels on a thread. | 
| Trash | Delete Email | Moves an email to the trash. | 
| Trash | Delete Thread | Moves a thread to the trash. | 
| Trash | Restore Message | Restores an email from the trash. | 
| Trash | Restore Thread | Restores a thread from the trash. | 
| Labels | List Labels | Lists all labels in the mailbox. | 
| Labels | Get Label | Retrieves details for a specific label. | 
| Labels | Create Label | Creates a new label. | 
| Labels | Update Label | Updates a label's properties. | 
| Labels | Tag Email | Adds a label to an email. | 
| Drafts | List Drafts | Lists email drafts. | 
| Drafts | Get Draft | Retrieves a specific draft. | 
| Drafts | Create Draft | Creates a new email draft. | 
| Drafts | Update Draft | Updates an existing draft. | 
| Drafts | Send Draft | Sends an existing draft. | 
| Contacts | Search Contacts | Searches for contacts by name or email. | 
| Contacts | Get Contacts | Retrieves contact information. | 
| History | List History | Lists mailbox change history. | 
| Settings | Get Profile | Retrieves the authenticated user's Gmail profile. | 
| Settings | Get Send As Alias | Retrieves a specific send-as alias configuration. | 
| Settings | List Send As Aliases | Lists all send-as aliases for the account. | 

**Note**  
The actions that you can use depend on the data accessible to the authenticated user.

## Manage and troubleshoot
<a name="gmail-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Common Google authentication issues
<a name="w2aac46c28c89c43b5"></a>
+ **Sign-in fails (Default OAuth app or Custom OAuth app)** – Verify that your Google account is active and that you can sign in to [the Google website](https://accounts.google.com) directly. For Custom OAuth app, confirm that the redirect URI in your Google Cloud OAuth client matches the Amazon Quick callback URL.
+ **App blocked by administrator** – If your Google Workspace administrator restricts third-party app access, you might see an error when you attempt to sign in. Contact your Google Workspace administrator to allow the Amazon Quick app.
+ **Invalid client credentials (Custom OAuth app)** – Verify that the Client ID and Client secret match the values in your Google Cloud OAuth client.
+ **Authentication popup fails** – Verify that your browser allows popups from the Amazon Quick console domain. Try using a different browser or clearing your browser cache.
+ **Permissions revoked** – If you previously revoked Amazon Quick access from your Google Account permissions settings, you need to re-authenticate by editing the connector and signing in again.
+ **Google API rate limiting** – Google might limit requests during high usage periods. If actions fail, retry after a few minutes.

### Gmail-specific issues
<a name="gmail-troubleshooting-service"></a>
+ **Gmail API not enabled** – Verify that the Gmail API is enabled in your Google Cloud project under **APIs & Services**, **Library**.