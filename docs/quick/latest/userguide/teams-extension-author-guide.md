

# Amazon Quick Microsoft Teams extension author guide
<a name="teams-extension-author-guide"></a>

As an Amazon Quick author, you can deploy Quick Microsoft Teams extensions after your admin establishes the foundational connection to your organization's Microsoft Teams workspace. Your capabilities depend on the permission level granted by your administrator.

With **limited permissions** (view, share, delete only), you can manage basic extension operations through the landing page after admin completes all setup. With **full permissions** (deploy, view, share, delete, edit), you can complete OAuth deployments, download manifests, rename extensions, and access all editing features.

Author capabilities for Microsoft Teams extensions include:
+ Configure extension connections (requires admin privileges).
+ Deploy extensions to your organization's Microsoft Teams workspace (requires full permissions).
+ Manage sharing and access permissions (available with limited or full permissions).
+ Customize extension settings - names, descriptions (requires full permissions).
+ Download manifest files for advanced Microsoft Teams customization (requires full permissions).

**Note**  
Before you deploy a Microsoft Teams extension as an author, your Quick admin must [configure Amazon Quick access to Microsoft Teams](https://docs.aws.amazon.com/quicksuite/latest/userguide/teams-extension.html).

**Topics**
+ [Deploy Microsoft Teams extension](#add-extensions-teams)
+ [Edit Microsoft Teams extension](#edit-extensions-teams)
+ [Share Microsoft Teams extension](#share-extensions-teams)
+ [Delete Microsoft Teams extension](#delete-extensions-teams)

## Deploy Microsoft Teams extension
<a name="add-extensions-teams"></a>

Deploy a new Microsoft Teams extension instance in the Amazon Quick console. This process establishes the foundation for connecting AI-powered assistance to your Microsoft Teams workspace.

**Note**  
This action requires full author permissions.

Use this procedure to create and configure a new Microsoft Teams extension for your organization.

1. Sign in to the Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select **Create extension**.

1. Select **Microsoft Teams**. Then, select **Next**.

1. Configure the following fields:
   + **Name** - A name for your extension is pre-filled for you. You can edit this and enter a descriptive name for the Microsoft Teams extension.
   + **Description** (optional) - A description for your extension is pre-filled for you. You can edit this and enter a new description to provide additional context about this extension configuration.
   + **Installation** type - Your Microsoft Teams extension supports OAuth installation by default.

1. Select **Next** to save your configuration.

1. From the **Extension** summary page, navigate to the extension you just configured.

1. Then, from the **Actions** menu, navigate to the extension you just configured.

1. Select **Install**. Then, from the **Complete installation for Teams assistant** dialog box that opens, select **Install**.

   A success message will open up on the top right of your screen.

1. From the success message, select **Install extension** to finish installing your extension.
**Note**  
You can also navigate to the extensions summary page and deploy your extension from the **Actions** menu.

1. Open the link and login as Global Admin or or someone with administrative permissions can add the Amazon Quick App to the Microsoft Teams admin center for your organization.

1. Choose **Teams apps** in the left navigation.

1. Choose **Amazon Quick** from the list of available apps.

1. Review and grant admin consent by choosing the **Permissions** tab and reviewing the permissions and choose **Grant admin consent**.
**Note**  
If permissions are already granted, proceed to the end of the procedure, there is no further action required.

1. Authenticate and choose **Accept** for Amazon Quick app.

1. Confirm that an app titled Amazon Quick **Permissions** tab now says **Admin consent granted for all required permissions**.

1. All users assigned to the app from the Teams admin center can now find the app in the **Built for your org** section of the **Apps** page of their Teams app.

Your Microsoft Teams extension has now been successfully deployed and is available for users.

## Edit Microsoft Teams extension
<a name="edit-extensions-teams"></a>

**Note**  
This action requires full author permissions.

As an author, you can edit the extensions you deploy to your users. Modify extension settings to update names, descriptions, or configuration options. Changes take effect immediately and apply to all users with access to the extension.

Use this procedure to modify settings and configuration for an existing Microsoft Teams extension.

1. Sign in to the Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select the three dot menu icon for the Microsoft Teams extension you need to edit.

1. Select **Edit**.

1. Edit the configuration as required and select **Save** to confirm the changes.

Your changes are now applied and will be reflected in the extension configuration for all users.

## Share Microsoft Teams extension
<a name="share-extensions-teams"></a>

Share ownership and management permissions with specific users and groups, enabling multiple users to manage extensions and assist with installation. You can assign different permission levels and manage access as needed.

Use this procedure to share your Microsoft Teams extension with other users and manage their access permissions.

1. Sign in to the Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select the three dot menu icon for the Microsoft Teams extension you need to share.

1. Select **Share**.

1. Enter the users and groups you would like to share the extension with.

1. Select **Share** to send the access email to each group and user.

1. From the drop-down next to each name, you can edit their access levels (**Viewer** or **Owner**).

1. **Optional:** You could select **Remove access** to delete the access for the selected group or user.

The specified users and groups now have access to your Microsoft Teams extension with the permissions you assigned.

## Delete Microsoft Teams extension
<a name="delete-extensions-teams"></a>

As an author, you can delete the extensions you deploy to your users. Permanently remove a extension from your Quick console and revoke access for all users. This action cannot be undone and requires confirmation.

Use this procedure to permanently remove a Microsoft Teams extension from your organization.

1. Sign in to Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select the three dot menu icon for the Microsoft Teams extension you need to delete.

1. Select **Delete**.

1. Enter the word, "confirm", and select **DELETE**.

The Microsoft Teams extension has been permanently removed and is no longer accessible to users in your organization.