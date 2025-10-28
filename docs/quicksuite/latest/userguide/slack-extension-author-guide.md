# Amazon Quick Suite Slack

extension author guide

As an Amazon Quick Suite author, you can deploy Quick Suite Slack
extensions after your admin establishes the foundational connection to your
organization's Slack workspace. Your capabilities depend on the
permission level granted by your administrator.

With **limited permissions** (view, share, delete
only), you can manage basic extension operations through the landing page after
admin completes all setup. With **full permissions**
(deploy, view, share, delete, edit), you can complete the Slack OAuth
application deployment, rename extensions, and access all editing features.

Author capabilities for Slack extensions:

- Deploy extensions to your organization's Slack workspace
  using OAuth (requires full permissions).
- Customize extension settings - names, descriptions (requires full
  permissions).
- Manage sharing and access permissions (available with limited or full
  permissions).

###### Note

Before you deploy a Slack extension as an author, your
Quick Suite admin must [configure Amazon Quick Suite access to Slack](slack-extension.md "slack-extension.md").

###### Topics

- [Deploy a Slack
  extension](#add-extensions-slack "#add-extensions-slack")
- [Edit Slack
  extension](#edit-extensions-slack "#edit-extensions-slack")
- [Share Slack
  extension](#share-extensions-slack "#share-extensions-slack")
- [Delete Slack
  extension](#delete-extensions-slack "#delete-extensions-slack")

## Deploy a Slack

extension

Deploy a new Slack extension instance in the Quick Suite
console. This process establishes the foundation for connecting AI-powered
assistance to your Slack workspace.

###### Note

This action requires full author permissions.

1. Sign in to the Amazon Quick Suite console.
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**.
3. Select **Create extension**.
4. Select **Slack**. Then, select
   **Next**.
5. Configure the following fields:
   - **Name** - A name for your extension is
     pre-filled for you. You can edit this and enter a descriptive
     name for the Slack extension.
   - **Description** (optional) - A description
     for your extension is pre-filled for you. You can edit this and
     enter a new description to provide additional context about this
     extension configuration.
   - **Installation** type - Your
     Slack extension supports OAuth installation
     by default.

6. Select **Next** to save your configuration.
7. From the **Extension** summary page, navigate to the
   extension you just configured.
8. Then, from the **Actions** menu, navigate to the
   extension you just configured.
9. Select **Install**. Then, from the **Complete
   installation for Slack assistant** dialog
   box that opens, select **Install**.

A success message will open up on the top right of your screen. 10. From the success message, select **Install
extension** to finish installing your extension.

###### Note

You can also navigate to the extensions summary page and deploy
your extension from the **Actions** menu. 11. The link will open to a Slack login page where after
you login (as admin) you will need to find and be asked to install the
Amazon Quick Suite app within your Slack workspace.

###### Note

You may see a "This app is not approved by Slack
banner." This message can be ignored. 12. Choose **Allow** to install your Amazon Quick Suite App for
Slack. 13. Once the installation is complete, you will see the page confirming
that the **Congratulations! Your Slack App has
been successfully installed.** 14. Choose **Open the Amazon Quick Suite App in
Slack**. 15. This will open your Slack workspace where all users
will be required to sign-in.

Your Slack extension has now been successfully deployed and is
available for users.

## Edit Slack

extension

###### Note

This action requires full author permissions.

As an author, you can edit the extensions you deploy to your users. Modify
extension settings to update names, descriptions, or configuration options.
Changes take effect immediately and apply to all users with access to the
extension.

1. Sign in to the Amazon Quick Suite console.
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**.
3. Select the three dot menu icon for the Slack extension
   you need to edit.
4. Select **Edit**.
5. Edit the configuration as required and select
   **Save** to confirm the changes.

## Share Slack

extension

Share ownership and management permissions with specific users and groups,
enabling multiple users to manage extensions and assist with installation. You
can assign different permission levels and manage access as needed.

1. Sign in to the Amazon Quick Suite console.
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**.
3. Select the three dot menu icon for the Slack extension
   you need to share.
4. Select **Share**.
5. Enter the users and groups you would like to share the extension
   with.
6. Select **Share** to send the access email to each
   group and user.
7. From the drop-down next to each name, you can edit their access levels
   (**Viewer** or **Owner**).
8. **Optional:** You could select
   **Remove access** to delete the access for the
   selected group or user.

## Delete Slack

extension

As an author, you can delete the extensions you deploy to your users.
Permanently remove a extension from your Quick Suite console and revoke
access for all users. This action cannot be undone and requires
confirmation.

1. Sign in to Amazon Quick Suite console.
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**.
3. Select the three dot menu icon for the Slack extension
   you need to delete.
4. Select **Delete**.
5. Enter the word, "confirm", and select
   **DELETE**.
