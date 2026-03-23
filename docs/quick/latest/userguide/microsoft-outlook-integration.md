# Microsoft Outlook integration

Use the Microsoft Outlook action connector to access Outlook's email, calendar, and
contact APIs directly in Amazon Quick through natural language.

Setting up this integration involves two steps. First, you register an application in
Microsoft Entra and configure its permissions. Then, you create the integration in
Amazon Quick and connect it to your Entra app. For information about the authentication
methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Before you begin

Make sure you have the following before you set up the integration.

- A Microsoft 365 account with Outlook or Exchange Online access.
- Access to the [Microsoft Entra
  admin center](https://entra.microsoft.com/ "https://entra.microsoft.com/") with at least Application Developer
  permissions.
- For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configure Microsoft Entra

Before you configure Amazon Quick, create an app registration in Microsoft Entra.
Complete all of the following steps in Entra before moving to the Amazon Quick
console.

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

| Outlook action integration – delegated permissions | Permission                                                                                                                                                   | Description |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `Mail.ReadWrite`                                   | Allows the app to create, read, update, and delete email in<br>user mailboxes.                                                                               |
| `Mail.Send`                                        | Allows the app to send mail as users in the<br>organization.                                                                                                 |
| `Calendars.ReadWrite`                              | Allows the app to create, read, update, and delete events in<br>user calendars.                                                                              |
| `Calendars.ReadWrite.Shared`                       | Allows the app to create, read, update and delete events in<br>all calendars the user has permissions to access, including<br>delegate and shared calendars. |
| `User.Read`                                        | Allows users to sign in to the app and allows the app to read<br>the profile of signed-in users.                                                             |
| `User.Read.All`                                    | Allows the app to read the full set of profile properties of<br>other users in your organization.                                                            |
| `Contacts.Read`                                    | Allows the app to read user contacts.                                                                                                                        |
| `Place.Read.All`                                   | Allows the app to read company places (conference rooms and<br>room lists) for calendar events and other<br>applications.                                    |
| `MailboxSettings.Read`                             | Allows the app to read the user's mailbox settings.                                                                                                          |
| `offline_access`                                   | Allows the app to refresh access tokens without requiring<br>the user to sign in again. This reduces how often users need<br>to re-authenticate.             |

###### Note

`User.Read.All` and `Place.Read.All` require
administrator consent. An administrator must grant consent before users can
authenticate.

**For service authentication (application
permissions):**

Add the following as Application permissions in your Entra app
registration.

| Outlook action integration – application permissions | Permission                                                                                                                | Description |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `Mail.ReadWrite`                                     | Allows the app to create, read, update, and delete mail in<br>all mailboxes.                                              |
| `Mail.Send`                                          | Allows the app to send mail as any user.                                                                                  |
| `Calendars.ReadWrite`                                | Allows the app to create, read, update, and delete events of<br>all calendars.                                            |
| `User.Read.All`                                      | Allows the app to read user profiles.                                                                                     |
| `Contacts.Read`                                      | Allows the app to read all contacts in all<br>mailboxes.                                                                  |
| `Place.Read.All`                                     | Allows the app to read company places (conference rooms and<br>room lists) for calendar events and other<br>applications. |
| `MailboxSettings.Read`                               | Allows the app to read user's mailbox settings.                                                                           |

###### Important

With service authentication, all actions execute as the service account.
Any user with access to this integration can perform actions across all
mailboxes that the service account can access. Scope the application
permissions appropriately for your organization's security
requirements.

### Record your credentials

Before leaving the Microsoft Entra admin center, confirm you have the
following values. You need them for the Amazon Quick configuration.

| Required credentials from Microsoft Entra | Value                          | Where to find it |
| ----------------------------------------- | ------------------------------ | ---------------- |
| Application (client) ID                   | App registration overview page |
| Directory (tenant) ID                     | App registration overview page |
| Client secret value                       | Certificates & secrets page    |

## Set up the integration in Amazon Quick

After you complete the Entra configuration, create the integration in
Amazon Quick.

1. In the Amazon Quick console, choose
   **Integrations**.
2. Choose the **Actions** tab.
3. Choose **Microsoft Outlook** and choose the Add
   (plus "+") button.
4. Fill in the integration details:
   - **Name** – Descriptive name for your Outlook
     integration.
   - **Description** (Optional) – Purpose of the
     integration.

5. Choose your connection type and fill in the connection settings:
   1. For **User authentication
      (OAuth)**, configure the following fields:
      - **Base URL** –
        `https://graph.microsoft.com/v1.0`
      - **Client ID** – Application
        (client) ID from your Entra app
        registration.
      - **Client Secret** – Client secret
        value from your Entra app
        registration.
      - **Token URL** –
        `https://login.microsoftonline.com/`{tenant-id}`/oauth2/v2.0/token`
      - **Auth URL** –
        `https://login.microsoftonline.com/`{tenant-id}`/oauth2/v2.0/authorize`
      - **Redirect URL** –
        `https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`

   2. For **Service authentication**,
      configure the following fields:
      - **Client ID** – Application
        (client) ID from your Entra app
        registration.
      - **Client Secret** – Client secret
        value from your Entra app
        registration.
      - **Token URL** –
        `https://login.microsoftonline.com/`{tenant-id}`/oauth2/v2.0/token`
      - **Scope** –
        `.default`

6. Choose **Create and continue**.
7. Choose users to share the integration with.
8. Choose **Next**.

## Available actions

After you set up the integration, the following actions are available.

| Microsoft Outlook available actions | Category               | Action                                                   | Description |
| ----------------------------------- | ---------------------- | -------------------------------------------------------- | ----------- |
| Email                               | List User Mails        | View emails in a mailbox.                                |
| Email                               | List Folder Messages   | View messages in a specific mail folder.                 |
| Email                               | View Email             | Get email details by ID.                                 |
| Email                               | Send User Email        | Send a new email message.                                |
| Email                               | Reply To Email         | Reply to an existing email.                              |
| Email                               | Forward User Email     | Forward an email to other recipients.                    |
| Email                               | Update Email           | Edit email properties.                                   |
| Email                               | Delete Email           | Remove an email from a mailbox.                          |
| Email                               | Move Email To Folder   | Move an email to a different folder.                     |
| Email                               | List Email Attachments | View attachments on an email.                            |
| Email                               | Get Attachment         | Get attachment details and content by ID.                |
| Calendar                            | List Calendar Events   | View events on a calendar.                               |
| Calendar                            | List Calendar View     | View meetings in a specified date range.                 |
| Calendar                            | Create Calendar Event  | Create a new meeting or appointment.                     |
| Calendar                            | Update Calendar Event  | Modify an existing event.                                |
| Calendar                            | Delete Calendar Event  | Remove an event from a calendar.                         |
| Calendar                            | Find Meeting Times     | Suggest meeting times based on attendee<br>availability. |
| Contacts                            | List Contacts          | View contacts.                                           |
| Users                               | List Users             | View users in the organization.                          |
| Settings                            | Get Mailbox Settings   | Read mailbox configuration.                              |
| Places                              | List Places            | View meeting rooms and room lists.                       |

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
