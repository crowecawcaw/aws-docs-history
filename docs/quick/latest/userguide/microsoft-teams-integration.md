

# Microsoft Teams integration
<a name="microsoft-teams-integration"></a>

Use the Microsoft Teams connector to send messages, manage channels, schedule meetings, and manage team collaboration directly in Amazon Quick through natural language.

Amazon Quick supports multiple authentication methods for Microsoft Teams. Choose the method that best fits your organization's security requirements.
+ **Default OAuth app** – Uses an AWS-managed OAuth application. No additional credentials are needed. Users authenticate directly with their Microsoft account.
+ **Custom OAuth app** – Uses a customer-managed application registered in Microsoft Entra. This option gives your organization full control over the OAuth configuration. Users authenticate on behalf of a signed-in user (delegated permissions).
+ **Service-to-Service OAuth** – Uses client credentials for server-to-server authentication without user interaction (application permissions). Suitable for automated workflows.

For more information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="msteams-integration-prerequisites"></a>

Make sure you have the following before you set up the integration.
+ A Microsoft 365 account with Teams access.
+ For **Custom OAuth app** or **Service-to-Service OAuth**: Access to the [Microsoft Entra admin center](https://entra.microsoft.com/) on the Microsoft website with at least Application Developer permissions.
+ For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configure Microsoft Entra
<a name="msteams-entra-setup"></a>

If you are using **Default OAuth app** authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#msteams-action-connector-setup).

Before you configure Amazon Quick, create an app registration in Microsoft Entra. Complete all of the following steps in Entra before moving to the Amazon Quick console.

For more information about app registrations, see [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) in the Microsoft documentation.

### Register the application
<a name="entra-app-registration"></a>

1. Open the [Microsoft Entra admin center](https://entra.microsoft.com/).

1. In the left navigation, choose **Entra ID**, then choose **App registrations**.

1. Choose **New registration**.

1. For **Name**, enter a descriptive name for your integration.

1. For **Supported account types**, choose **Accounts in this organizational directory only**.

1. For **Redirect URI**, select **Web** and enter `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback`. Replace {{{region}}} with the AWS Region where your Amazon Quick instance is deployed.

1. Choose **Register**.

1. On the overview page, copy the **Application (client) ID** and **Directory (tenant) ID**. You need these values for the Amazon Quick configuration.

### Create a client secret
<a name="entra-client-secret"></a>

Amazon Quick needs a client secret to authenticate with Microsoft Entra. This secret acts as a password for the app registration.

1. From your app registration, choose **Certificates & secrets**.

1. Choose **New client secret**.

1. Enter a description and choose an expiration period.

1. Choose **Add**.

1. Copy the **Value** immediately. This value is only displayed once.

**Important**  
Copy the secret **Value**, not the Secret ID. The Value is the longer string used for authentication.

### Configure API permissions
<a name="msteams-entra-api-permissions"></a>

Microsoft Graph supports two permission types for this integration. Delegated permissions allow the app to act on behalf of a signed-in user. Application permissions allow the app to act without a signed-in user. For more information, see [Overview of Microsoft Graph permissions](https://learn.microsoft.com/en-us/graph/permissions-overview) in the Microsoft documentation.

1. From your app registration, choose **API permissions**.

1. Choose **Add a permission**, then choose **Microsoft Graph**.

1. Choose **Delegated permissions** or **Application permissions** based on your authentication method, and add the permissions from the appropriate table below.

1. Choose **Grant admin consent for [your tenant name]** to approve the permissions.

**For user authentication (delegated permissions):**

Add the following as Delegated permissions in your Entra app registration. For the full permissions reference, see [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference) in the Microsoft documentation.


**Teams action integration – delegated permissions**  

| Permission | Description | 
| --- | --- | 
| Calendars.ReadWrite | Allows the app to read and write events in user calendars on behalf of the signed-in user. | 
| Channel.Create | Allows the app to create channels in any team on behalf of the signed-in user. | 
| Channel.ReadBasic.All | Allows the app to read channel names and descriptions on behalf of the signed-in user. | 
| ChannelMessage.Read.All | Allows the app to read all channel messages on behalf of the signed-in user. | 
| ChannelMessage.ReadWrite | Allows the app to read, send, update, and delete messages in channels on behalf of the signed-in user. | 
| ChannelMessage.Send | Allows the app to send messages in channels on behalf of the signed-in user. | 
| ChannelSettings.ReadWrite.All | Allows the app to read and write the settings of all channels on behalf of the signed-in user. | 
| Chat.Create | Allows the app to create chats on behalf of the signed-in user. | 
| Chat.ReadWrite | Allows the app to read and write the signed-in user's chat messages. | 
| ChatMessage.Send | Allows the app to send chat messages on behalf of the signed-in user. | 
| Files.Read | Allows the app to read the signed-in user's files. | 
| offline\_access | Allows the app to refresh access tokens without requiring the user to sign in again. This reduces how often users need to re-authenticate. | 
| OnlineMeetingRecording.Read.All | Allows the app to read all recordings of online meetings on behalf of the signed-in user. | 
| OnlineMeetings.ReadWrite | Allows the app to read and create online meetings on behalf of the signed-in user. | 
| OnlineMeetingTranscript.Read.All | Allows the app to read all transcripts of online meetings on behalf of the signed-in user. | 
| People.Read | Allows the app to read a list of people relevant to the signed-in user. | 
| Presence.ReadWrite | Allows the app to read and write the presence information of the signed-in user. | 
| Sites.Read.All | Allows the app to read documents and list items in all site collections on behalf of the signed-in user. | 
| Team.Create | Allows the app to create teams on behalf of the signed-in user. | 
| Team.ReadBasic.All | Allows the app to read the names and descriptions of teams on behalf of the signed-in user. | 
| TeamMember.ReadWrite.All | Allows the app to add and remove members from all teams on behalf of the signed-in user. | 
| User.Read | Allows the app to read the signed-in user's profile. | 
| User.Read.All | Allows the app to read the full set of profile properties of all users on behalf of the signed-in user. | 
| User.ReadBasic.All | Allows the app to read a basic set of profile properties of all users on behalf of the signed-in user. | 

**For service authentication (application permissions):**

Add the following as Application permissions in your Entra app registration.


**Teams action integration – application permissions**  

| Permission | Description | 
| --- | --- | 
| Chat.Read.All | Allows the app to read all chat messages in your organization without a signed-in user. | 
| Chat.Send | Allows the app to send chat messages without a signed-in user. | 
| Team.ReadBasic.All | Allows the app to read the names and descriptions of all teams without a signed-in user. | 
| Channel.ReadBasic.All | Allows the app to read all channel names and descriptions without a signed-in user. | 
| ChannelMessage.Read.All | Allows the app to read all channel messages without a signed-in user. | 
| ChannelMessage.Send | Allows the app to send messages to any channel without a signed-in user. | 
| ChannelMember.ReadWrite.All | Allows the app to add and remove members from all channels without a signed-in user. | 
| TeamMember.ReadWrite.All | Allows the app to add and remove members from all teams without a signed-in user. | 
| User.Read.All | Allows the app to read the full set of profile properties of all users without a signed-in user. | 
| OnlineMeetingTranscript.Read.All | Allows the app to read all transcripts of online meetings without a signed-in user. | 

**Important**  
With service authentication, all actions execute as the service account. Any user with access to this integration can perform actions across all teams and channels that the service account can access. Scope the application permissions appropriately for your organization's security requirements.

### Record your credentials
<a name="entra-record-credentials"></a>

Before leaving the Microsoft Entra admin center, confirm you have the following values. You need them for the Amazon Quick configuration.


**Required credentials from Microsoft Entra**  

| Value | Where to find it | 
| --- | --- | 
| Application (client) ID | App registration overview page | 
| Directory (tenant) ID | App registration overview page | 
| Client secret value | Certificates & secrets page | 

## Setting up the connector in Amazon Quick
<a name="msteams-action-connector-setup"></a>

### Connect from the Available tab
<a name="msteams-quick-connect"></a>

If you want to use Default OAuth app authentication, you can connect directly from the **Available** tab without additional configuration.

1. In the Amazon Quick console, choose **Connectors**.

1. On the **Available** tab, find **MSTeams** and choose **Connect**.

1. Complete the Microsoft sign-in flow and grant the requested permissions.

To configure a connector with Custom OAuth app or Service-to-Service OAuth instead, use the **Create for your team** tab as described below.

### Create from the Create for your team tab
<a name="msteams-full-setup"></a>

After you complete any required Entra configuration, create the connector in Amazon Quick.

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Microsoft Teams**.
**Note**  
If a Microsoft Teams connector already exists, a dialog appears with your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.

1. Enter a **Name** for your connector. Optionally, choose **\+ Add Description** to add a description.

1. For **Connection type**, choose **Public network**.

1. For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.

   1. For **Default OAuth app**:

      No additional credentials are needed. Choose **Next** to continue.

   1. For **Custom OAuth app** (user authentication with delegated permissions), configure the following fields:
      + **Base URL** (Optional) – The Microsoft Graph API base URL. Example: `https://graph.microsoft.com/v1.0`
      + **Client ID** – The Application (client) ID from your Entra app registration.
      + **Client secret** – The client secret value from your Entra app registration.
      + **Token URL** – The token endpoint. Example: `https://login.microsoftonline.com/{{{tenant-id}}}/oauth2/v2.0/token`
      + **Authorization URL** – The authorization endpoint. Example: `https://login.microsoftonline.com/{{{tenant-id}}}/oauth2/v2.0/authorize`
      + **Redirect URL** – Pre-filled with the Amazon Quick callback URL.

   1. For **Service-to-Service OAuth** (service authentication with application permissions), configure the following fields:
      + **Base URL** (Optional) – The Microsoft Graph API base URL. Example: `https://graph.microsoft.com/v1.0`
      + **Client ID** – The Application (client) ID from your Entra app registration.
      + **Client secret** – The client secret value from your Entra app registration.
      + **Token URL** – The token endpoint. Example: `https://login.microsoftonline.com/{{{tenant-id}}}/oauth2/v2.0/token`
**Note**  
The scope for the client credentials token request (`https://graph.microsoft.com/.default`) is set automatically by Amazon Quick. You do not need to configure it manually.

1. Choose **Next**.

1. If you chose **Default OAuth app** or **Custom OAuth app**, a Microsoft authorization window opens. Review the requested permissions and choose **Accept**.

   If you see an error instead of the consent dialog, your organization might restrict third-party app access. See [Admin consent for Microsoft 365](#msteams-admin-consent).

1. On the **Review** page, review the available actions for the connector. Choose **Next**.

1. On the **Publish** page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.

1. Choose **Publish**.

## Available actions
<a name="msteams-integration-actions"></a>

After you set up the integration, the following actions are available.


**Microsoft Teams available actions**  

| Category | Action | Description | 
| --- | --- | --- | 
| Chats | List Chats | View your chat conversations. | 
| Chats | Create Chat | Start a new chat conversation. | 
| Chats | Send Chat Message | Send a message in a chat. | 
| Teams | List Teams | View teams you're a member of. | 
| Teams | List Team Members | View members of a team. | 
| Teams | Add Team Member | Add a member to a team. | 
| Channels | List Channels | View channels in a team. | 
| Channels | Create Channel | Create a new channel in a team. | 
| Channels | List Channel Messages | View messages in a channel. | 
| Channels | Send Channel Message | Post a message to a channel. | 
| Channels | List Channel Members | View members of a channel. | 
| Channels | Add Channel Member | Add a member to a channel. | 
| Users | List Users | View users in your organization. | 
| Meetings | List Online Meetings | View your scheduled online meetings. | 
| Meetings | Create Online Meeting | Schedule a new online meeting. | 
| Meetings | List Meeting Transcripts | View transcripts from meetings. | 
| Calendar | List Calendar Events | View events on your calendar. | 
| Calendar | Create Calendar Event | Create a new calendar event. | 

## Manage and troubleshoot
<a name="entra-troubleshooting"></a>

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Authentication issues
<a name="entra-troubleshooting-auth"></a>
+ **Incorrect app registration** – Verify the app registration in Microsoft Entra includes the required API permissions and that admin consent has been granted.
+ **Expired client secret** – Check if the client secret has expired in **Certificates & secrets** and generate a new one if needed.
+ **Incorrect redirect URI** – Verify the redirect URI in Microsoft Entra matches `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback`.

### Common error messages
<a name="entra-troubleshooting-errors"></a>
+ **`Access denied. You do not have permission to perform this action`** – The authenticated user does not have the required permissions. Contact your administrator to verify and grant appropriate permissions.
+ **`AADSTS50020: User account from identity provider does not exist in tenant`** – The user account is not configured in the correct Microsoft Entra tenant. Verify the user account exists in the tenant that matches the Directory (tenant) ID in your app registration.

## Admin consent for Microsoft 365
<a name="msteams-admin-consent"></a>

When you use the **Default OAuth app** authentication method, Amazon Quick uses an AWS-managed application to access Microsoft Teams on behalf of the signed-in user. Most users can complete setup without any extra steps. However, if your Microsoft 365 tenant restricts third-party app access, a Microsoft 365 administrator must grant one-time consent before users can connect.

If you see an error when you sign in during connector setup, your organization might restrict third-party app access. Share the following information with your Microsoft 365 administrator:
+ **What to do:** Grant admin consent for the Amazon Quick Microsoft Teams integration application.
+ **Why:** Amazon Quick needs delegated access to Teams channels, chats, meetings, and calendar data to perform actions on behalf of users.

An administrator can grant consent in one of the following ways:
+ **Through the consent dialog** – A Global Administrator or Privileged Role Administrator initiates the connector setup flow. In the Microsoft sign-in dialog, they select the **Consent on behalf of your organization** check box and choose **Accept**.
+ **Through the Microsoft Entra admin center** – Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) on the Microsoft website. Choose **Enterprise applications**, locate the Amazon Quick application, choose **Permissions**, and choose **Grant admin consent for {{Your Organization}}**.

After consent is granted, any user in your organization can connect without being prompted for individual consent.

**Note**  
To check whether your tenant restricts user consent, go to the Microsoft Entra admin center and choose **Enterprise applications**, **Consent and permissions**, **User consent settings**. If the setting is **Do not allow user consent**, an administrator must grant consent before users can use the connector.