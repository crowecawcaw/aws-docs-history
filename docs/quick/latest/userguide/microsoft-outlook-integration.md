# Microsoft Outlook integration

With the Microsoft Outlook connector, you can access Outlook's email,
calendar, and contact APIs directly in Amazon Quick through natural language.

Amazon Quick supports multiple authentication methods for Microsoft Outlook.
Choose the method that best fits your organization's security requirements.

- **Default OAuth app** – Uses an
  AWS-managed OAuth application. No additional credentials are needed.
  Users authenticate directly with their Microsoft account.
- **Custom OAuth app** – Uses a
  customer-managed application registered in Microsoft Entra. This option
  gives your organization full control over the OAuth configuration.
  Users authenticate on behalf of a signed-in user (delegated
  permissions).
- **Service-to-Service OAuth** – Uses
  client credentials for server-to-server authentication without user
  interaction (application permissions). Suitable for automated
  workflows.
  For more information about the authentication methods that Amazon Quick
  supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Before you begin

Make sure that you have the following before you set up the
integration.

- A Microsoft 365 account with Outlook or Exchange Online
  access.
- For **Custom OAuth app** or
  **Service-to-Service OAuth**: Access
  to the [Microsoft Entra
  admin center](https://entra.microsoft.com/ "https://entra.microsoft.com/") on the Microsoft website with at least
  Application Developer permissions.
- For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configuring Microsoft Entra

If you are using **Default OAuth app**
authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#exchange-integration-setup "#exchange-integration-setup").

Before you configure Amazon Quick, create an app registration in Microsoft
Entra. Complete all of the following steps in Entra before moving to the
Amazon Quick console.

For more information about app registrations, see [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app "https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app") in the
Microsoft documentation.

### Register the application

1. Open the [Microsoft Entra
   admin center](https://entra.microsoft.com/ "https://entra.microsoft.com/").
2. In the left navigation, choose **Entra ID**, then
   choose **App registrations**.
3. Choose **New registration**.
4. For **Name**, enter a descriptive name for your
   integration.
5. For **Supported account types**, choose
   **Accounts in this organizational directory
   only**.
6. For **Redirect URI**, select
   **Web** and enter
   `https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`.
   Replace `{region}` with the AWS Region
   where your Amazon Quick instance is deployed.
7. Choose **Register**.
8. On the overview page, copy the **Application (client)
   ID** and **Directory (tenant) ID**. You
   need these values for the Amazon Quick configuration.

### Create a client secret

Amazon Quick needs a client secret to authenticate with Microsoft Entra.
This secret acts as a password for the app registration.

1. From your app registration, choose **Certificates &
   secrets**.
2. Choose **New client secret**.
3. Enter a description and choose an expiration period.
4. Choose **Add**.
5. Copy the **Value** immediately. This value is only
   displayed once.

###### Important

Copy the secret **Value**, not the Secret
ID. The Value is the longer string used for authentication.

### Configure API permissions

Microsoft Graph supports two permission types for this integration.
Delegated permissions allow the app to act on behalf of a signed-in user.
Application permissions allow the app to act without a signed-in user. For
more information, see [Overview of Microsoft Graph permissions](https://learn.microsoft.com/en-us/graph/permissions-overview "https://learn.microsoft.com/en-us/graph/permissions-overview") in the Microsoft
documentation.

1. From your app registration, choose **API
   permissions**.
2. Choose **Add a permission**, then choose
   **Microsoft Graph**.
3. Choose **Delegated permissions** or
   **Application permissions** based on your
   authentication method, and add the permissions from the appropriate
   table below.
4. Choose **Grant admin consent for [your tenant
   name]** to approve the permissions.

**For user authentication (delegated
permissions):**

Add the following as Delegated permissions in your Entra app registration.
For the full permissions reference, see [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference "https://learn.microsoft.com/en-us/graph/permissions-reference") in the Microsoft
documentation.

Outlook action integration – delegated permissions| Permission | Description |
| --- | --- |
| `Mail.ReadWrite` | Allows the app to create, read, update, and delete email in<br>user mailboxes. |
| `Mail.Send` | Allows the app to send mail as users in the<br>organization. |
| `Mail.Read.Shared` | Allows the app to read mail that the user can access,<br>including the user's own mail and shared mail. |
| `Calendars.ReadWrite` | Allows the app to create, read, update, and delete events in<br>user calendars. |
| `Calendars.ReadWrite.Shared` | Allows the app to create, read, update and delete events in<br>all calendars the user has permissions to access, including<br>delegate and shared calendars. |
| `User.Read` | Allows users to sign in to the app and allows the app to read<br>the profile of signed-in users. |
| `User.Read.All` | Allows the app to read the full set of profile properties of<br>other users in your organization. |
| `Contacts.Read` | Allows the app to read user contacts. |
| `Place.Read.All` | Allows the app to read company places (conference rooms and<br>room lists) for calendar events and other<br>applications. |
| `MailboxSettings.Read` | Allows the app to read the user's mailbox settings. |
| `offline_access` | Allows the app to refresh access tokens without requiring<br>the user to sign in again. This reduces how often users need<br>to re-authenticate. |

###### Note

`User.Read.All` and `Place.Read.All` require
administrator consent. An administrator must grant consent before users can
authenticate.

**For service authentication (application
permissions):**

Add the following as Application permissions in your Entra app
registration.

Outlook action integration – application permissions| Permission | Description |
| --- | --- |
| `Mail.ReadWrite` | Allows the app to create, read, update, and delete mail in<br>all mailboxes. |
| `Mail.Send` | Allows the app to send mail as any user. |
| `Calendars.ReadWrite` | Allows the app to create, read, update, and delete events of<br>all calendars. |
| `User.Read.All` | Allows the app to read user profiles. |
| `Contacts.Read` | Allows the app to read all contacts in all<br>mailboxes. |
| `Place.Read.All` | Allows the app to read company places (conference rooms and<br>room lists) for calendar events and other<br>applications. |
| `MailboxSettings.Read` | Allows the app to read user's mailbox settings. |

###### Important

With service authentication, all actions execute as the service account.
Any user with access to this integration can perform actions across all
mailboxes that the service account can access. Scope the application
permissions appropriately for your organization's security
requirements.

### Record your credentials

Before leaving the Microsoft Entra admin center, confirm you have the
following values. You need them for the Amazon Quick configuration.

Required credentials from Microsoft Entra| Value | Where to find it |
| --- | --- |
| Application (client) ID | App registration overview page |
| Directory (tenant) ID | App registration overview page |
| Client secret value | Certificates & secrets page |

## Setting up the connector in Amazon Quick

### Connect from the Available tab

If you want to use Default OAuth app authentication, you can connect
directly from the **Available** tab without additional
configuration.

1. In the Amazon Quick console, choose
   **Connectors**.
2. On the **Available** tab, find
   **Microsoft Outlook** and choose
   **Connect**.
3. Complete the Microsoft sign-in flow and grant the requested
   permissions.

To configure a connector with Custom OAuth app or Service-to-Service
OAuth instead, use the **Create for your team** tab as
described below.

### Create from the Create for your team tab

After you complete any required Entra configuration, create the connector
in Amazon Quick.

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Microsoft Outlook**.

###### Note

If a Microsoft Outlook connector already exists, a dialog
appears with your existing connectors. To use an existing
connector, choose it. To create a new
one, choose **No, create new**. 4. Enter a **Name** for your connector. Optionally,
choose **+ Add Description** to add a
description. 5. For **Connection type**, choose **Public
network**. 6. For **OAuth Configuration**, choose one of the
following authentication methods and configure the required
fields.

    1. For **Default OAuth
     app**:


    No additional credentials are needed. Choose
     **Next** to continue.
    2. For **Custom OAuth app**
     (user authentication with delegated permissions), configure
     the following fields:




    	* **Base URL** (Optional) – The
    	 Microsoft Graph API base URL. Example:
    	 `https://graph.microsoft.com/v1.0`
    	* **Client ID** – The Application
    	 (client) ID from your Entra app
    	 registration.
    	* **Client secret** – The client
    	 secret value from your Entra app
    	 registration.
    	* **Token URL** – The token
    	 endpoint. Example:
    	 `https://login.microsoftonline.com/`{tenant-id}`/oauth2/v2.0/token`
    	* **Authorization URL** – The
    	 authorization endpoint. Example:
    	 `https://login.microsoftonline.com/`{tenant-id}`/oauth2/v2.0/authorize`
    	* **Redirect URL** – Pre-filled
    	 with the Amazon Quick callback URL.
    3. For **Service-to-Service
     OAuth** (service authentication with
     application permissions), configure the following
     fields:




    	* **Base URL** (Optional) – The
    	 Microsoft Graph API base URL. Example:
    	 `https://graph.microsoft.com/v1.0`
    	* **Client ID** – The Application
    	 (client) ID from your Entra app
    	 registration.
    	* **Client secret** – The client
    	 secret value from your Entra app
    	 registration.
    	* **Token URL** – The token
    	 endpoint. Example:
    	 `https://login.microsoftonline.com/`{tenant-id}`/oauth2/v2.0/token`
    ###### Note

    The scope for the client credentials token request
     (`https://graph.microsoft.com/.default`)
     is set automatically by Amazon Quick. You do not need
     to configure it manually.

7. Choose **Next**. 8. If you chose **Default OAuth app**
or **Custom OAuth app**, a Microsoft
authorization window opens. Review the requested permissions and
choose **Accept**.

If you see an error instead of the consent dialog, your
organization might restrict third-party app access. See
[Admin consent for Microsoft 365](#exchange-admin-consent "#exchange-admin-consent"). 9. On the **Review** page, review the available
actions for the connector. Choose
**Next**. 10. On the **Publish** page, choose who can access
the connector. You can enable access for everyone in your
organization or search for specific teams or groups. 11. Choose **Publish**.

## Available actions

After you set up the connector, the following actions are available.

Microsoft Outlook available actions| Category | Action | Description |
| --- | --- | --- |
| Email | List User Mails | Lists emails in a mailbox. |
| Email | List Folder Messages | Lists messages in a specific mail folder. |
| Email | View Email | Retrieves email details by ID. |
| Email | Send User Email | Sends a new email message. |
| Email | Reply To Email | Replies to an existing email. |
| Email | Forward User Email | Forwards an email to other recipients. |
| Email | Update Email | Edits email properties. |
| Email | Delete Email | Removes an email from a mailbox. |
| Email | Move Email To Folder | Moves an email to a different folder. |
| Email | List Email Attachments | Lists attachments on an email. |
| Email | Get Attachment | Retrieves attachment details and content by ID. |
| Calendar | List Calendar Events | Lists events on a calendar. |
| Calendar | List Calendar View | Lists meetings in a specified date range. |
| Calendar | Create Calendar Event | Creates a new meeting or appointment. |
| Calendar | Update Calendar Event | Modifies an existing event. |
| Calendar | Delete Calendar Event | Removes an event from a calendar. |
| Calendar | Find Meeting Times | Suggests meeting times based on attendee<br>availability. |
| Contacts | List Contacts | Lists contacts. |
| Users | List Users | Lists users in the organization. |
| Settings | Get Mailbox Settings | Reads mailbox configuration. |
| Places | List Places | Lists meeting rooms and room lists. |

## Manage and troubleshoot

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **Incorrect app registration** – Verify
  the app registration in Microsoft Entra includes the required API
  permissions and that admin consent has been granted.
- **Expired client secret** – Check if
  the client secret has expired in **Certificates &
  secrets** and generate a new one if needed.
- **Incorrect redirect URI** – Verify the
  redirect URI in Microsoft Entra matches
  `https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`.

### Common error messages

- **`Access denied. You do not have
 permission to perform this action`** – The
  authenticated user does not have the required permissions. Contact your
  administrator to verify and grant appropriate permissions.
- **`AADSTS50020: User account from identity
 provider does not exist in tenant`** – The user
  account is not configured in the correct Microsoft Entra tenant. Verify
  the user account exists in the tenant that matches the Directory
  (tenant) ID in your app registration.

## Admin consent for Microsoft 365

When you use the **Default OAuth app**
authentication method, Amazon Quick uses an AWS-managed application to
access Microsoft Outlook on behalf of the signed-in user. Most users can
complete setup without any extra steps. However, if your Microsoft 365
tenant restricts third-party app access, a Microsoft 365 administrator
must grant one-time consent before users can connect.

If you see an error when you sign in during connector setup, your
organization might restrict third-party app access. Share the following
information with your Microsoft 365 administrator:

- **What to do:** Grant admin consent
  for the Amazon Quick Microsoft Outlook integration
  application.
- **Why:** Amazon Quick needs
  delegated access to Outlook email, calendar, and contact data to
  perform actions on behalf of users.

An administrator can grant consent in one of the following ways:

- **Through the consent dialog** – A
  Global Administrator or Privileged Role Administrator initiates the
  connector setup flow. In the Microsoft sign-in dialog, they select
  the **Consent on behalf of your organization**
  check box and choose **Accept**.
- **Through the Microsoft Entra admin
  center** – Sign in to the [Microsoft Entra admin
  center](https://entra.microsoft.com/ "https://entra.microsoft.com/") on the Microsoft website. Choose **Enterprise
  applications**, locate the Amazon Quick application,
  choose **Permissions**, and choose
  **Grant admin consent for `Your
 Organization`**.

After consent is granted, any user in your organization can connect
without being prompted for individual consent.

###### Note

To check whether your tenant restricts user consent, go to the
Microsoft Entra admin center and choose **Enterprise
applications**, **Consent and
permissions**, **User consent
settings**. If the setting is **Do not allow user
consent**, an administrator must grant consent before
users can use the connector.
