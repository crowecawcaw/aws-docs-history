# Amazon Quick Suite Microsoft Outlook

extension

The Quick Suite extension for Microsoft Outlook integrates
AI-powered assistance directly into your email workflows. Users can access
Quick Suite capabilities within Outlook to enhance their email
communication and productivity without switching between applications.

The Outlook extension enables users to:

- Summarize emails for quick understanding.
- Draft contextual responses with AI assistance.
- Use actions from action connectors configured in Amazon Quick Suite.
- Access any company knowledge sources added to your Amazon Quick Suite instance from
  within Microsoft Outlook.

###### Important

- The Amazon Quick Suite customer integrating Microsoft Outlook
  must have a paid Microsoft Outlook organization with an
  _M365 subscription for their
  organization_.
- Amazon Quick Suite does not use your user data for service improvement or for
  training its underlying large language models (LLMs).

###### Topics

- [Prerequisites for Microsoft
  Outlook extension](#outlook-prerequisites "#outlook-prerequisites")
- [Configure Microsoft
  Outlook extension access](#configure-outlook-extension "#configure-outlook-extension")

## Prerequisites for Microsoft

Outlook extension

Before configuring access to the Amazon Quick Suite extension to Microsoft
Outlook, administrators must complete the following steps:

1. Have a Microsoft 365 Business subscription and be a Global
   Admin or have administrative permissions (specifically
   `AppCatalog.ReadWrite.All`).
2. Have a Amazon Quick Suite instance.
3. Your Microsoft 365 tenant ID. You can find this by going to
   the Azure portal > **Azure Active
   Directory** > **Properties**, or by using
   PowerShell. For detailed steps, see [How to find your tenant ID - Microsoft Entra](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant "https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant") in
   the Microsoft Learn portal.

###### Note

The Microsoft Outlook extension isn't supported if you're using
IAM Identity Center for end user management in Amazon Quick Suite.

## Configure Microsoft

Outlook extension access

As an administrator, you must allow the Amazon Quick Suite Microsoft
Outlook extension to connect to your Amazon Quick Suite application
environment. You can use the Amazon Quick Suite console to manage extension access
configurations.

### User attribute mapping

When you configure a Microsoft Outlook extension, user identity
is mapped by default using the following attributes:

- **Amazon Quick Suite user attribute** - Email address is
  used to map Amazon Quick Suite users to their corresponding Microsoft
  365 accounts. The system uses the email address to establish
  the connection between user identities.
- **M365 Office add-in user attribute**

* User Principal Name (UPN) is used to match against
  Microsoft 365 user accounts. Users need to use the
  User Principal Name (UPN) to sign in to
  Microsoft 365. Email address that works on both cloud
  and on-premise systems.

These default mappings ensure secure and accurate user identification across
both platforms without requiring additional configuration.

###### Note

The Microsoft Outlook extension isn't supported if you're using
IAM Identity Center for end user management in Amazon Quick Suite.

###### Topics

- [Add Microsoft
  Outlook extension access](#add-outlook-extension-access "#add-outlook-extension-access")
- [Edit Microsoft
  Outlook extension access](#edit-outlook-extension-access "#edit-outlook-extension-access")
- [Delete Microsoft
  Outlook extension access](#delete-outlook-extension-access "#delete-outlook-extension-access")

### Add Microsoft

Outlook extension access

Follow these steps to create a new extension access configuration that will
allow Amazon Quick Suite to integrate with your Microsoft Outlook
environment.

1. Sign in to Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. In the top right, select **New extension
   access**.
6. Select **Microsoft Outlook**. Then,
   **Next**.
7. Configure the following fields:
   - **Name** - A name for your extension is
     pre-filled for you. You can edit this and enter a descriptive
     name for the Outlook extension (maximum 512
     alphanumeric characters, hyphens allowed but no spaces).
   - **Description** (optional) - A description
     for your extension is pre-filled for you. You can edit this and
     enter a new description to provide additional context about this
     extension configuration (maximum 1000 characters).
   - **M365 tenant ID** - Enter your
     Microsoft 365 tenant identifier (must be 36
     characters).

8. Select **Add** to save the new access
   configuration.

A success message will open up on the top right of your screen. 9. From the success message, select **View extensions**
to finish installing your extension.

###### Note

You can also navigate to the installation screen from
**Connections** >
**Extensions** in the Amazon Quick Suite menu.

Once created, this extension access configuration enables authors and other
admin in your organization to create and deploy Amazon Quick Suite extensions within
your Microsoft Outlook environment.

###### Note

For your end users to begin using your Microsoft Outlook
extension, an admin or author must finish deploying a extension after you
configure extension access. Notify your authors that they can view, edit,
and complete installation of this extension under
**Extensions** in the left navigation once it has been
shared. To learn how to do this see [Installing your Microsoft Outlook
extension in the Microsoft Outlook extension author
guide](outlook-extension-author-guide.md#add-extensions-outlook "outlook-extension-author-guide.md#add-extensions-outlook").

### Edit Microsoft

Outlook extension access

Use these steps to modify the configuration settings of an existing
Microsoft Outlook extension access.

1. Sign in to Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. Select the three dot menu icon for the Microsoft
   Outlook extension you need to edit.
6. Select **Edit**.
7. Edit the configuration as required and select
   **Save** to confirm the changes.

Your changes to the Microsoft Outlook extension access
configuration are saved and will take effect immediately.

### Delete Microsoft

Outlook extension access

Follow these steps to permanently remove a Microsoft Outlook
extension access configuration. This action cannot be undone.

1. Sign in to Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. Select the three dot menu icon for the Microsoft
   Outlook Extension you need to delete.
6. Select **Delete**.
7. Enter the word, "confirm", and select
   **DELETE**.

###### Note

Deleting a extension access removes access for all users in your M365
tenant and deletes all extensions created for Outlook. If
delete extension access fails, the admin must switch to the author view and
delete the Outlook extensions that are using the configured
extension access before returning to delete the extension access.

With Microsoft Outlook extension access configured, your team can now
use Amazon Quick Suite to enhance their email workflows with AI-powered assistance for
summarizing, drafting responses, and accessing organizational knowledge directly within
Outlook.
