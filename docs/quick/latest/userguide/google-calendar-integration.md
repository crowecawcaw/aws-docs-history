

# Google Calendar integration
<a name="google-calendar-integration"></a>

With the Google Calendar connector, you can access Google Calendar directly in Amazon Quick through natural language. You can create and update events, check availability, manage calendars, and organize attendees without leaving Amazon Quick.

Amazon Quick supports multiple authentication methods for Google Calendar. Choose the method that best fits your organization's security requirements.
+ **Default OAuth app** – Uses an AWS-managed OAuth application. No additional credentials are needed. You authenticate directly with your Google account.
+ **Custom OAuth app** – Uses a customer-managed OAuth client created in the Google Cloud Console. This option gives your organization full control over the OAuth configuration.

For more information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="google-calendar-integration-prerequisites"></a>

Make sure that you have the following before you set up the integration.
+ A Google account with access to Google Calendar.
+ For **Custom OAuth app**: Access to the [Google Cloud Console](https://console.cloud.google.com/) on the Google website with permissions to create OAuth clients.
+ For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configuring Google Cloud
<a name="google-calendar-source-setup"></a>

If you are using **Default OAuth app** authentication, skip this section and go to [Setting up the connector in Amazon Quick](#google-calendar-quicksuite-setup).

For Custom OAuth app authentication, complete the following steps in the Google Cloud Console before you configure Amazon Quick. When you enable the API in step 3, search for and enable the **Google Calendar API**.

### Create an OAuth client in Google Cloud Console
<a name="w2aac46c28c97c13b7"></a>

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
<a name="google-calendar-oauth-scopes"></a>

The following scopes are requested when you connect to Google Calendar.


**Google Calendar recommended scopes**  

| Scope | Description | 
| --- | --- | 
| https://www.googleapis.com/auth/calendar | Reads and writes calendar events and settings. | 
| openid | Authenticates the user's identity. | 
| email | Reads the user's email address. | 

**Note**  
The `openid` and `email` scopes are automatically included in the OAuth consent flow for user authentication. They are not required for Service-to-Service OAuth.

## Setting up the connector in Amazon Quick
<a name="google-calendar-quicksuite-setup"></a>

### Connect from the Available tab
<a name="google-calendar-quick-connect"></a>

If you want to use Default OAuth app authentication, you can connect directly from the **Available** tab without additional configuration.

1. In the Amazon Quick console, choose **Connectors**.

1. On the **Available** tab, find **Google Calendar** and choose **Connect**.

1. Complete the Google sign-in flow and grant the requested permissions.

To configure a connector with Custom OAuth app instead, use the **Create for your team** tab as described below.

### Create from the Create for your team tab
<a name="google-calendar-full-setup"></a>

After you complete any required Google Cloud configuration, create the connector in Amazon Quick.

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Google Calendar**.
**Note**  
If a Google Calendar connector already exists, a dialog appears with your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.

1. Enter a **Name** for your connector. Optionally, choose **\+ Add Description** to add a description.

1. For **Connection type**, choose **Public network**.

1. For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.

   1. For **Default OAuth app**:

      No additional credentials are needed. Choose **Next** to continue.

   1. For **Custom OAuth app**, configure the following fields:
      + **Base URL** (Optional) – The Google Calendar API base URL. Example: `https://www.googleapis.com/calendar`
      + **Client ID** – The client ID from your Google Cloud OAuth client.
      + **Client secret** – The client secret from your Google Cloud OAuth client.
      + **Token URL** – The token endpoint. Example: `https://oauth2.googleapis.com/token`
      + **Authorization URL** – The authorization endpoint. Example: `https://accounts.google.com/o/oauth2/v2/auth`
      + **Redirect URL** – Pre-filled with the Amazon Quick callback URL.

1. Choose **Next**.

1. If you chose **Default OAuth app** or **Custom OAuth app**, a Google authorization window opens. Review the requested permissions and choose **Allow**.

1. On the **Review** page, review the available actions for the connector. Choose **Next**.

1. On the **Publish** page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.

1. Choose **Publish**.

## Available actions
<a name="google-calendar-integration-actions"></a>

After you set up the connector, the following actions are available.


**Google Calendar available actions**  

| Category | Action | Description | 
| --- | --- | --- | 
| Events | List Events | Lists events on a calendar. | 
| Events | Search Events | Searches for events by keyword or criteria. | 
| Events | Get Event | Retrieves details for a specific event. | 
| Events | Create Event | Creates a new calendar event. | 
| Events | Create Quick Event | Creates an event from a text string. | 
| Events | Update Event | Updates an existing event. | 
| Events | Update Event Calendar | Moves an event to a different calendar. | 
| Events | Import Events | Imports events into a calendar. | 
| Events | List Event Instances | Lists instances of a recurring event. | 
| Events | Delete Attendee | Removes an attendee from an event. | 
| Availability | List Free Slots | Finds available time slots across calendars. | 
| Calendars | List Calendars | Lists calendars for the authenticated user. | 
| Calendars | List Calendar Events | Lists events across all calendars. | 
| Calendars | Get Calendar | Retrieves details for a specific calendar. | 
| Calendars | Get Calendar List | Retrieves a calendar list entry. | 
| Calendars | Update Calendar List | Updates a calendar list entry. | 
| Settings | List Settings | Lists calendar settings for the user. | 
| Utilities | Get Current Date Time | Retrieves the current date and time. | 

**Note**  
The actions that you can use depend on the calendars accessible to the authenticated user.

## Managing and troubleshooting
<a name="google-calendar-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Common Google authentication issues
<a name="w2aac46c28c97c19b5"></a>
+ **Sign-in fails (Default OAuth app or Custom OAuth app)** – Verify that your Google account is active and that you can sign in to [the Google website](https://accounts.google.com) directly. For Custom OAuth app, confirm that the redirect URI in your Google Cloud OAuth client matches the Amazon Quick callback URL.
+ **App blocked by administrator** – If your Google Workspace administrator restricts third-party app access, you might see an error when you attempt to sign in. Contact your Google Workspace administrator to allow the Amazon Quick app.
+ **Invalid client credentials (Custom OAuth app)** – Verify that the Client ID and Client secret match the values in your Google Cloud OAuth client.
+ **Authentication popup fails** – Verify that your browser allows popups from the Amazon Quick console domain. Try using a different browser or clearing your browser cache.
+ **Permissions revoked** – If you previously revoked Amazon Quick access from your Google Account permissions settings, you need to re-authenticate by editing the connector and signing in again.
+ **Google API rate limiting** – Google might limit requests during high usage periods. If actions fail, retry after a few minutes.

### Google Calendar-specific issues
<a name="google-calendar-troubleshooting-service"></a>
+ **Google Calendar API not enabled** – Verify that the Google Calendar API is enabled in your Google Cloud project under **APIs & Services**, **Library**.