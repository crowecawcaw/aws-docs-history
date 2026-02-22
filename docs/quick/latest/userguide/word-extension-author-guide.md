# Amazon Quick Microsoft

Word extension author guide

As an Amazon Quick author, you can deploy Quick Microsoft
Word extensions after your admin establishes the foundational connection
to your organization's Microsoft 365 tenant. Your capabilities depend
on the permission level granted by your administrator.

With **limited permissions** (view, share, delete
only), you can manage basic extension operations through the landing page after
admin completes all setup. With **full permissions**
(deploy, view, share, delete, edit), you can download manifests for deployment in
the M365 admin center, rename extensions, and access all editing
features.

Author capabilities for Microsoft Word extensions include:

- Configure extension connections (requires access to M365
  Admin Center portal).
- Deploy extensions to your organization's Microsoft 365
  tenant (requires full permissions).
- Customize extension settings - names, descriptions (requires full
  permissions).
- Download manifest files for advanced Microsoft 365
  deployment (requires full permissions).
- Manage sharing and access permissions (available with limited or full
  permissions).

###### Note

Before you deploy a Microsoft Word extension as an author, your
Quick admin must [configure Amazon Quick access to Microsoft
Word](../../../quicksuite/latest/userguide/word-extension.md "../../../quicksuite/latest/userguide/word-extension.md").

###### Topics

- [Deploy Microsoft Word
  extension](#add-extensions-word "#add-extensions-word")
- [Edit Microsoft Word
  extension](#edit-extensions-word "#edit-extensions-word")
- [Share Microsoft Word
  extensions](#word-authors-share "#word-authors-share")
- [Delete Microsoft Word
  Extensions](#word-authors-delete "#word-authors-delete")

## Deploy Microsoft Word

extension

Deploy a new Microsoft Word extension instance in the
Amazon Quick console. This process establishes the foundation for connecting
AI-powered assistance to your Microsoft Word environment.

###### Note

This action requires full author permissions.

Use this procedure to create and configure a new Microsoft Word
extension for your organization.

1. Sign in to the Amazon Quick console.
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**.
3. Select **Create extension**.
4. Select **Microsoft Word**. Then,
   select **Next**.
5. Configure the following fields:
   - **Name** - A name for your extension is
     pre-filled for you. You can edit this and enter a descriptive
     name for the Microsoft Word extension.
   - **Description** (optional) - A description
     for your extension is pre-filled for you. You can edit this and
     enter a new description to provide additional context about this
     extension configuration.
   - **Installation** type - Your Microsoft
     Word extension uses manifest-only installation by
     default.

6. Select **Next** to save the details and download the
   manifest file to your computer.

###### Note

You will now continue the remainder of this procedure within the
Microsoft 365 admin center.

1. In the Microsoft 365 admin center, choose
   **Integrated apps** from the left navigation and
   choose **Upload custom apps**. This will open the
   **Deploy New App** page.
2. Choose **Office Add-in** as your App type.
3. Choose **Upload manifest file (.xml) from device**,
   select **Choose from file**, select the downloaded
   manifest xml file and choose **Next**.
4. Choose the users you want to add in the **Add users**
   section.
5. Choose **Accept permissions** in the **Accept
   permissions requests** section and deploy the Add-in. Once
   deployment is completed, your users will be able to install the
   Amazon Quick Add-in in their Microsoft Word.

Your Microsoft Word extension is now created and ready for
deployment to users in your organization.

## Edit Microsoft Word

extension

###### Note

This action requires full author permissions.

As an author, you can edit the extensions you deploy to your users. Modify
existing Microsoft Word extension configurations to update
settings, change descriptions, or adjust deployment parameters as your
organizational needs evolve.

Use this procedure to modify settings and configuration for an existing
Microsoft Word extension.

1. Sign in to the Amazon Quick console.
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**.
3. Select the three dot menu icon for the Microsoft Word
   extension you need to edit.
4. Select **Edit**.
5. Enter your changes and select **Save** to confirm the
   new configuration.

Your changes are now applied and will be reflected in the extension
configuration for all users.

## Share Microsoft Word

extensions

Share ownership and management permissions with specific users and groups,
enabling multiple users to manage extensions and assist with installation. You
can assign different permission levels and manage access as needed.

Use this procedure to share your Microsoft Word extension with
other users and manage their access permissions.

1. Sign in to Amazon Quick console.
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**.
3. Select the three dot menu icon for the Microsoft Word
   extension you need to share.
4. Select **Share**.
5. Enter the users and groups you would like to share the extension
   with.
6. Select **Share** to send the access email to each
   group and user.
7. From the drop-down next to each name, you can edit their access levels
   (**Viewer** or **Owner**).
8. **Optional** You could select,
   **Remove access** to delete the access for the
   selected group or user.

The specified users and groups now have access to your Microsoft
Word extension with the permissions you assigned.

## Delete Microsoft Word

Extensions

As an author, you can delete the extensions you deploy to your users.

Use this procedure to permanently remove a Microsoft Word
extension from your organization.

1. Sign in to Amazon Quick console
2. In the left navigation, under **CONNECTIONS**, select
   **Extensions**
3. Select the three dot menu icon for the Microsoft Word
   extension you need to delete
4. Select **Delete**
5. Enter, confirm and **DELETE** to delete the
   Extension

The Microsoft Word extension has been permanently removed and
is no longer accessible to users in your organization.
