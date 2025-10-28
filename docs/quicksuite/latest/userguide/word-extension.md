# Amazon Quick Suite Microsoft Word

extension

The Quick Suite extension for Microsoft Word integrates
AI-powered assistance directly into your document creation and editing workflows. Users
can access Quick Suite capabilities within Word to enhance their
document productivity and content quality without switching between applications.

The Word extension enables users to:

- Review, draft, and revise documents with AI assistance.
- Summarize documents and get insights.
- Simplify and improve writing quality.
- Use actions from action connectors configured in Amazon Quick Suite.
- Access any company knowledge sources added to your Amazon Quick Suite instance from
  within Microsoft Word.

###### Important

- The Amazon Quick Suite customer integrating Microsoft Word must
  have a paid Word organization with an
  _M365 subscription for their
  organization_.
- Amazon Quick Suite does not use user data for service improvement or for
  training its underlying large language models (LLMs).

###### Topics

- [Prerequisites for Microsoft Word
  extension](#word-prerequisites "#word-prerequisites")
- [Configure Microsoft Word
  extension access](#configure-word-extension "#configure-word-extension")

## Prerequisites for Microsoft Word

extension

Before adding the Amazon Quick Suite extension to Microsoft Word,
administrators must complete the following steps:

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

The Microsoft Word extension isn't supported if you're using
IAM Identity Center for end user management in Amazon Quick Suite.

## Configure Microsoft Word

extension access

As an administrator, you must allow the Amazon Quick Suite Microsoft Word
Extension to connect to your Amazon Quick Suite application environment and web
experience. You can use the Amazon Quick Suite console to manage extension access
configurations.

### User attribute mapping

When you configure a Microsoft Word extension, user identity is
mapped by default using the following attributes:

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

###### Topics

- [Add Microsoft Word
  extension access](#add-word-extension-access "#add-word-extension-access")
- [Edit Microsoft Word
  extension access](#edit-word-extension-access "#edit-word-extension-access")
- [Delete Microsoft
  Word extension access](#delete-word-extension-access "#delete-word-extension-access")

### Add Microsoft Word

extension access

Follow these steps to create a new extension access configuration that will
allow Amazon Quick Suite to integrate with your Microsoft Word
environment.

1. Sign in to Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. In the top right, select **New extension
   access**.
6. Select **Microsoft Word**. Then, select
   **Next**.
7. Configure the following fields:
   - **Name** - A name for your extension is
     pre-filled for you. You can edit this and enter a descriptive
     name for the Word extension (maximum 512
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
your Microsoft Word environment.

###### Note

For your end users to begin using your Microsoft Word
extension, an admin or author must finish deploying a extension after you
configure extension access. Notify your authors that they can view, edit,
and complete installation of this extension under
**Extensions** in the left navigation once it has been
shared. To learn how to do this see [Installing your Microsoft Word
extension in the Microsoft Word extension author
guide](word-extension-author-guide.md#add-extensions-word "word-extension-author-guide.md#add-extensions-word").

### Edit Microsoft Word

extension access

Use these steps to modify the configuration settings of an existing
Microsoft Word extension access.

1. Sign in to Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. Select the three dot menu icon for the **Microsoft
   Word** extension you need to edit.
6. Select **Edit**.
7. Edit the configuration as required and select
   **Save** to confirm the changes.

Your changes to the Microsoft Word extension access
configuration are saved and will take effect immediately.

### Delete Microsoft

Word extension access

Follow these steps to permanently remove a Microsoft Word
extension access configuration. This action cannot be undone.

###### Note

Deleting a extension access removes access for all users in your M365
tenant and deletes all extensions created for Word.

1. Sign in to Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. Select the three dot menu icon for the Microsoft Word
   Extension you need to delete.
6. Select **Delete**.
7. Enter the word, "confirm", and select
   **DELETE**.

###### Note

If the process to delete extension access fails, the admin must switch to
the author view and delete the Word extensions that are using
the configured extension access before returning to delete the extension
access.

With Microsoft Word extension access configured, your team can now use
Amazon Quick Suite to enhance their document creation workflows with AI assistance for
reviewing, drafting, revising, and accessing organizational knowledge directly within
Word.
