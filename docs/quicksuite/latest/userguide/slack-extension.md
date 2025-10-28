# Amazon Quick Suite Slack extension

The Quick Suite extension for Slack integrates AI-powered
assistance directly into your team communication workflows. Users can access
Quick Suite knowledge and capabilities within Slack channels and
direct messages without switching between applications.

The Slack extension enables users to:

- Add Amazon Quick Suite as a collaborator using **@Amazon Quick Suite**
  mentions.
- Get conversation summaries and insights.
- Access organizational knowledge bases and documents directly from
  Slack channels.
- Generate notes and action items from discussions in Slack
  threads.
- Get help with data analysis and report generation using uploaded files.

###### Important

- When Amazon Quick Suite is used in public Slack channels,
  responses are based on the invoking user's permissions. This may include
  content that other channel members aren't authorized to access. Carefully
  evaluate using Amazon Quick Suite in public channels to prevent unintended
  exposure of sensitive information.
- Amazon Quick Suite does not use your user data for service improvement or for
  training its underlying large language models (LLMs).

###### Topics

- [Prerequisites for Slack
  extension](#slack-prerequisites "#slack-prerequisites")
- [Configure Slack extension
  access](#configure-slack-extension "#configure-slack-extension")

## Prerequisites for Slack

extension

Before adding the Amazon Quick Suite Slack Extension, administrators must
complete the following requirements:

- Have a paid Slack workspace.
- Have admin access to your Slack workspace.
- Get started with Amazon Quick Suite.
- Your Slack workspace ID (must start with 'T' and be
  alphanumeric). One way to find your Slack workspace ID is by
  navigating to your Slack workspace and starting a chat with
  the Slack Developer Tools app running the `/sdt
whoami` command. For more information, see [Locate your Slack URL or ID](https://slack.com/help/articles/221769328-Locate-your-Slack-URL-or-ID "https://slack.com/help/articles/221769328-Locate-your-Slack-URL-or-ID") in the Slack help
  center.

## Configure Slack extension

access

As an administrator, you must allow your Amazon Quick Suite Slack
extension to connect to your Amazon Quick Suite application environment. You can use the
Amazon Quick Suite console to manage extension access configurations.

### User attribute mapping

When you configure a Slack extension, user identity is mapped
by default using the following attributes:

- **Amazon Quick Suite user attribute** - Email address is
  used to map Amazon Quick Suite users to their corresponding
  Slack accounts. The system uses the email address to
  establish the connection between user identities.
- **Slack user attribute** - User
  Profile Email is used to match against Slack
  user accounts. This maps to the email address associated with the user's
  Slack profile.

These default mappings ensure secure and accurate user identification across
both platforms without requiring additional configuration.

###### Topics

- [Add Slack extension
  access](#add-slack-extension-access "#add-slack-extension-access")
- [Edit Slack
  extension access](#edit-slack-extension-access "#edit-slack-extension-access")
- [Delete Slack
  extension access](#delete-slack-extension-access "#delete-slack-extension-access")

### Add Slack extension

access

Follow these steps to create a new extension access configuration that will
allow Amazon Quick Suite to integrate with your Slack
environment.

1. Sign in to Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. In the top right, select **New extension
   access**.
6. Select Slack, then, **Next**.
7. Configure the following fields:
   - **Name** - A name for your extension is
     pre-filled for you. You can edit this and enter a descriptive
     name for the Slack extension (maximum 512
     alphanumeric characters, hyphens allowed but no spaces).
   - **Description** (optional) - A description
     for your extension is pre-filled for you. You can edit this and
     enter a new description to provide additional context about this
     extension configuration (maximum 1000 characters).
   - **Slack Workspace ID** - Enter your
     Slack workspace identifier. Workspace ID must
     start with T and be between 1 and 256 alphanumeric characters
     long.

8. Select **Add** to save the new access
   configuration.

A success message will open up on the top right of your screen. 9. From the success message, select **View extensions**
to finish installing your extension.

###### Note

You can also navigate to the installation screen from
**Connections** >
**Extensions** in the Amazon Quick Suite menu.

Once created, this extension access configuration enables authors and other
admins in your organization to deploy Amazon Quick Suite Slack
extensions in their workspace.

###### Note

For your end users to begin using your Slack extension, an
admin or author must finish deploying a extension after you configure
extension access. Notify your authors that they can view, edit, and complete
installation of this extension under **Extensions** in the
left navigation once it has been shared. To learn how to do this see [Installing your Slack extension in
the Slack extension author guide](slack-extension-author-guide.md#add-extensions-slack "slack-extension-author-guide.md#add-extensions-slack").

### Edit Slack

extension access

Use these steps to modify the configuration settings of an existing
Slack extension access.

1. Sign in to Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. Select the three dot menu icon for the Slack Extension
   you need to edit.
6. Select **Edit**.
7. Edit the configuration as required and select
   **Save** to confirm the changes.

Your changes to the Slack extension access configuration are
saved and will take effect immediately.

### Delete Slack

extension access

Follow these steps to permanently remove a Slack extension
access configuration. This action cannot be undone.

1. Sign in to Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. Select the three dot menu icon for the Slack Extension
   you need to delete.
6. Select **Delete**.
7. Enter the word, "confirm", and select
   **DELETE**.

###### Note

Deleting a extension access removes access for all users in your
Slack workspace and deletes all extensions created for
Slack. If delete extension access fails, the admin must
switch to the author view and delete the Slack extensions
that are using the configured extension access before returning to delete
the extension access.

With Slack extension access configured, your team can now use
**@Amazon Quick Suite** mentions in channels and direct messages to
access AI assistance and organizational knowledge directly within their
Slack workspace.
