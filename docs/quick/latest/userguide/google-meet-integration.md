# Google Meet integration

With the Google Meet connector, you can access Google Meet directly in
Amazon Quick through natural language. You can schedule meetings, view conference
records, retrieve transcripts and recordings, and manage meeting spaces without
leaving Amazon Quick.

Amazon Quick supports multiple authentication methods for Google Meet. Choose
the method that best fits your organization's security requirements.

- **Default OAuth app** – Uses an
  AWS-managed OAuth application. No additional credentials are needed.
  You authenticate directly with your Google account.
- **Custom OAuth app** – Uses a
  customer-managed OAuth client created in the Google Cloud Console. This
  option gives your organization full control over the OAuth
  configuration.
  For more information about the authentication methods that Amazon Quick
  supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Before you begin

Make sure that you have the following before you set up the
integration.

- A Google account with access to Google Meet.
- For **Custom OAuth app**: Access
  to the [Google Cloud
  Console](https://console.cloud.google.com/ "https://console.cloud.google.com/") on the Google website with permissions to
  create OAuth clients.
- For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configuring Google Cloud

If you use **Default OAuth app**
authentication, skip this section and see [Setting up the connector in Amazon Quick](#google-meet-quicksuite-setup "#google-meet-quicksuite-setup").

For Custom OAuth app authentication,
complete the following steps in the Google Cloud Console before you
configure Amazon Quick. When you enable the API in step 3, search for
and enable the **Google Meet REST API**.

### Create an OAuth client in Google Cloud Console

Create an OAuth client in the Google Cloud Console to get the client
credentials that you need for Amazon Quick. For more information, see [Using OAuth
2.0 to Access Google APIs](https://developers.google.com/identity/protocols/oauth2 "https://developers.google.com/identity/protocols/oauth2") on the Google website.

1. Sign in to the [Google
   Cloud Console](https://console.cloud.google.com/ "https://console.cloud.google.com/") on the Google website.
2. Create a new project or select an existing project.
3. In the left navigation pane, choose **APIs &
   Services**, then choose **Library**.
   Search for the API that your integration requires and choose
   **Enable**.
4. Choose **OAuth consent screen** and choose
   **Get Started**.
5. Configure the consent screen:

   - Enter an **App Name** and select a
     **User support email**.
   - For **Audience**, choose
     **Internal** (your organization only) or
     **External** (any Google user).
   - Add developer contact details and choose
     **Create**.

6. Choose **Create OAuth client**.
7. Configure the client:

   - For **Application type**, choose
     **Web application**.
   - Enter a **Name** for your client.
   - Under **Authorized redirect URIs**, add
     the Amazon Quick callback URL:
     `https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`

8. Choose **Create**.
9. Record the following values. You need them when you configure
   Amazon Quick.

   - **Client ID**
   - **Client secret**

### Recommended scopes

The following scopes are requested when you connect to Google
Meet.

Google Meet recommended scopes| Scope | Description |
| --- | --- |
| `https://www.googleapis.com/auth/meetings.space.created` | Creates meeting spaces. |
| `https://www.googleapis.com/auth/meetings.space.readonly` | Reads meeting space information. |
| `https://www.googleapis.com/auth/meetings.space.settings` | Manages meeting space settings. |
| `openid` | Authenticates the user's identity. |
| `email` | Reads the user's email address. |

###### Note

The `openid` and `email` scopes are
automatically included in the OAuth consent flow for user
authentication. They are not required for Service-to-Service
OAuth.

## Setting up the connector in Amazon Quick

### Connect from the Available tab

If you want to use Default OAuth app authentication, you can connect
directly from the **Available** tab without additional
configuration.

1. In the Amazon Quick console, choose
   **Connectors**.
2. On the **Available** tab, find
   **Google Meet** and choose
   **Connect**.
3. Complete the Google sign-in flow and grant the requested
   permissions.

To configure a connector with Custom OAuth app instead, use the
**Create for your team** tab as described
below.

### Create from the Create for your team tab

After you complete any required Google Cloud configuration, create the
connector in Amazon Quick.

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Google Meet**.

###### Note

If a Google Meet connector already exists, a dialog
appears with your existing connectors. To use an existing
connector, choose it. To create a
new one, choose **No, create new**. 4. Enter a **Name** for your connector. Optionally,
choose **+ Add Description** to add a
description. 5. For **Connection type**, choose **Public
network**. 6. For **OAuth Configuration**, choose one of the
following authentication methods and configure the required
fields.

    1. For **Default OAuth
     app**:


    No additional credentials are needed. Choose
     **Next** to continue.
    2. For **Custom OAuth app**,
     configure the following fields:




    	* **Base URL** (Optional) – The
    	 Google Meet API base URL. For example:
    	 `https://meet.googleapis.com`
    	* **Client ID** – The client ID
    	 from your Google Cloud OAuth client.
    	* **Client secret** – The client
    	 secret from your Google Cloud OAuth
    	 client.
    	* **Token URL** – The token
    	 endpoint. For example:
    	 `https://oauth2.googleapis.com/token`
    	* **Authorization URL** – The
    	 authorization endpoint. For example:
    	 `https://accounts.google.com/o/oauth2/v2/auth`
    	* **Redirect URL** – Pre-filled
    	 with the Amazon Quick callback URL.

7. Choose **Next**. 8. If you chose **Default OAuth app**
or **Custom OAuth app**, a Google
authorization window opens. Review the requested permissions and
choose **Allow**. 9. On the **Review** page, review the available
actions for the connector. Choose
**Next**. 10. On the **Publish** page, choose who can access
the connector. You can enable access for everyone in your
organization or search for specific teams or groups. 11. Choose **Publish**.

## Available actions

After you set up the connector, the following actions are
available.

Google Meet available actions| Category | Action | Description |
| --- | --- | --- |
| Meetings | Create Meeting | Creates a new meeting. |
| Meetings | Get Meeting | Retrieves details for a specific meeting. |
| Meetings | List Conference Records | Lists conference records for past<br>meetings. |
| Spaces | Create Space | Creates a new meeting space. |
| Spaces | Get Space | Retrieves details for a meeting space. |
| Spaces | Update Space | Updates meeting space settings. |
| Participants | List Participants | Lists participants for a conference<br>record. |
| Participants | List Participant Sessions | Lists sessions for a participant. |
| Participants | Get Participant Session | Retrieves details for a participant<br>session. |
| Recordings | List Recordings | Lists recordings for a conference<br>record. |
| Recordings | Get Recordings | Retrieves recordings by conference record<br>ID. |
| Transcripts | Get Transcripts | Retrieves transcripts by conference record<br>ID. |
| Transcripts | List Transcript Entries | Lists individual entries in a<br>transcript. |
| Transcripts | Get Transcript Entry | Retrieves a specific transcript entry. |

###### Note

The actions that you can use depend on the meetings and
conference records accessible to the authenticated user.

## Managing and troubleshooting

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Common Google authentication issues

- **Sign-in fails (Default OAuth app or Custom
  OAuth app)** – Verify that your Google account is active
  and that you can sign in to
  [the Google website](https://accounts.google.com "https://accounts.google.com")
  directly. For Custom OAuth app, confirm that the redirect URI in your
  Google Cloud OAuth client matches the Amazon Quick callback URL.
- **App blocked by administrator** – If
  your Google Workspace administrator restricts third-party app access,
  you might see an error when you attempt to sign in. Contact your Google
  Workspace administrator to allow the Amazon Quick app.
- **Invalid client credentials (Custom OAuth app)** – Verify that the Client ID
  and Client secret match the values in your Google Cloud OAuth
  client.
- **Authentication popup fails** – Verify
  that your browser allows popups from the Amazon Quick console domain.
  Try using a different browser or clearing your browser cache.
- **Permissions revoked** – If you
  previously revoked Amazon Quick access from your Google Account
  permissions settings, you need to re-authenticate by editing the
  connector and signing in again.
- **Google API rate limiting** – Google
  might limit requests during high usage periods. If actions fail, retry
  after a few minutes.

### Google Meet-specific issues

- **Google Meet REST API not
  enabled** – Verify that the Google Meet REST
  API is enabled in your Google Cloud project under
  **APIs & Services**,
  **Library**.
