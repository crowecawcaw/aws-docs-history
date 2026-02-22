# Amazon Quick Microsoft

Outlook extension author guide

As an Amazon Quick author, you can deploy Quick Microsoft
Outlook extensions after your admin establishes the foundational
connection to your organization's Microsoft 365 tenant. Your
capabilities depend on the permission level granted by your administrator.

With **limited permissions** (view, share, delete
only), you can manage basic extension operations through the landing page after
admin completes all setup. With **full permissions**
(deploy, view, share, delete, edit), you can download manifests for deployment in
the M365 admin center, rename extensions, and access all editing
features.

Author capabilities for Microsoft Outlook extensions
include:

- Configure extension connections (requires access to M365
  Admin Center portal).
- Deploy extensions to your organization's Microsoft 365
  tenant (requires full permissions).
- Manage sharing and access permissions (available with limited or full
  permissions).
- Customize extension settings - names, descriptions (requires full
  permissions).
- Download manifest files for advanced Microsoft 365
  deployment (requires full permissions).

###### Note

Before you deploy a Microsoft Outlook extension as an author,
your Quick admin must [configure Amazon Quick access to Microsoft
Outlook](../../../quicksuite/latest/userguide/outlook-extension.md "../../../quicksuite/latest/userguide/outlook-extension.md").

###### Topics

- [Deploy Microsoft Outlook
  extension](#add-extensions-outlook "#add-extensions-outlook")
- [Edit Microsoft Outlook
  extension](#edit-extensions-outlook "#edit-extensions-outlook")
- [Share Microsoft
  Outlook extension](#share-extensions-outlook "#share-extensions-outlook")
- [Delete Microsoft
  Outlook extension](#delete-extensions-outlook "#delete-extensions-outlook")

## Deploy Microsoft Outlook

extension

Deploy a new Microsoft Outlook extension instance in the
Quick console. This process establishes the foundation for
connecting AI-powered assistance to your Microsoft Outlook
environment.

###### Note

This action requires full author permissions.

1. Sign in to the Amazon Quick console.
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**.
3. Select **Create extension**.
4. Select **Microsoft Outlook**. Then,
   select **Next**.
5. Configure the following fields:
   - **Name** - A name for your extension is
     pre-filled for you. You can edit this and enter a descriptive
     name for the Microsoft Outlook extension.
   - **Description** (optional) - A description
     for your extension is pre-filled for you. You can edit this and
     enter a new description to provide additional context about this
     extension configuration.
   - **Installation** type - Your Microsoft
     Outlook extension uses manifest-only installation by
     default.

6. Select **Next** to save your configuration.
7. From the **Extension** summary page, navigate to the
   extension you just configured.
8. Then, from the **Actions** menu, navigate to the
   extension you just configured.
9. Select **Download manifest**. Then, from the
   **Complete installation for Outlook
   assistant** dialog box that opens, select
   **Download**.

The manifest file will be downloaded to your computer. 10. From the success message, select **Install
extension** to finish downloading the manifest for your
extension.

###### Note

You can also navigate to the extensions summary page and download
the manifest for your extension from the
**Actions** menu. 11. In the screen asking for permissions to allow your Amazon Quick
Outlook extension to access Outlook,
select **Allow**.

###### Note

You will now continue the remainder of this procedure within the
Microsoft 365 admin center. 12. In the Microsoft 365 admin center, choose
**Integrated apps** from the left navigation and
choose **Upload custom apps**. This will open the
**Deploy New App** page. 13. Choose **Office Add-in** as your App type. 14. Paste the manifest URL link you copied in the **Provide link
to manifest file** and choose
**Validate**. 15. Choose the users you want to add in the **Add users**
section. 16. Choose **Accept permissions** in the **Accept
permissions requests** section and deploy the Add-in. Once
deployment is completed, your users will be able to install the
Amazon Quick Add-in in their Microsoft Outlook.

Your Outlook extension has now been successfully deployed and
is available for users.

## Edit Microsoft Outlook

extension

As an author, you can edit the extensions you deploy to your users. Modify
extension settings to update names, descriptions, or configuration options.
Changes take effect immediately and apply to all users with access to the
extension.

1. Sign in to the Amazon Quick console.
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**.
3. Select the three dot menu icon for the Microsoft
   Outlook extension you need to edit.
4. Select **Edit**.
5. Edit the configuration as required and select
   **Save** to confirm the changes.

## Share Microsoft

Outlook extension

Share ownership and management permissions with specific users and groups,
enabling multiple users to manage extensions and assist with installation. You
can assign different permission levels and manage access as needed.

1. Sign in to the Amazon Quick console.
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**.
3. Select the three dot menu icon for the Microsoft
   Outlook extension you need to share.
4. Select **Share**.
5. Enter the users and groups you would like to share the extension
   with.
6. Select **Share** to send the access email to each
   group and user.
7. From the drop-down next to each name, you can edit their access levels
   (Viewer or Owner).
8. **Optional:** You could select
   **Remove access** to delete the access for the
   selected group or user.

## Delete Microsoft

Outlook extension

As an author, you can delete the extensions you deploy to your users.
Permanently remove a extension from your Quick console and revoke
access for all users. This action cannot be undone and requires
confirmation.

1. Sign in to Amazon Quick console.
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**.
3. Select the three dot menu icon for the Microsoft
   Outlook extension you need to delete.
4. Select **Delete**.
5. Enter the word, "confirm", and select
   **DELETE**.
