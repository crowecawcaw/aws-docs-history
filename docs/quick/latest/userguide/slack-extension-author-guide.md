

# Amazon Quick Slack extension author guide
<a name="slack-extension-author-guide"></a>

As an Amazon Quick author, you can deploy Quick Slack extensions after your admin establishes the foundational connection to your organization's Slack workspace. Your capabilities depend on the permission level granted by your administrator.

With **limited permissions** (view, share, delete only), you can manage basic extension operations through the landing page after admin completes all setup. With **full permissions** (deploy, view, share, delete, edit), you can complete the Slack OAuth application deployment, rename extensions, and access all editing features.

Author capabilities for Slack extensions:
+ Deploy extensions to your organization's Slack workspace using OAuth (requires full permissions).
+ Customize extension settings - names, descriptions (requires full permissions).
+ Manage sharing and access permissions (available with limited or full permissions).

**Note**  
Before you deploy a Slack extension as an author, your Quick admin must [configure Amazon Quick access to Slack](https://docs.aws.amazon.com/quicksuite/latest/userguide/slack-extension.html).

**Topics**
+ [Deploy a Slack extension](#add-extensions-slack)
+ [Edit Slack extension](#edit-extensions-slack)
+ [Share Slack extension](#share-extensions-slack)
+ [Delete Slack extension](#delete-extensions-slack)

## Deploy a Slack extension
<a name="add-extensions-slack"></a>

Deploy a new Slack extension instance in the Quick console. This process establishes the foundation for connecting AI-powered assistance to your Slack workspace.

**Note**  
This action requires full author permissions.

1. Sign in to the Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select **Create extension**.

1. Select **Slack**. Then, select **Next**.

1. Configure the following fields:
   + **Name** - A name for your extension is pre-filled for you. You can edit this and enter a descriptive name for the Slack extension.
   + **Description** (optional) - A description for your extension is pre-filled for you. You can edit this and enter a new description to provide additional context about this extension configuration.
   + **Installation** type - Your Slack extension supports OAuth installation by default.

1. Select **Next** to save your configuration.

1. From the **Extension** summary page, navigate to the extension you just configured.

1. Then, from the **Actions** menu, navigate to the extension you just configured.

1. Select **Install**. Then, from the **Complete installation for Slack assistant** dialog box that opens, select **Install**.

   A success message will open up on the top right of your screen.

1. From the success message, select **Install extension** to finish installing your extension.
**Note**  
You can also navigate to the extensions summary page and deploy your extension from the **Actions** menu.

1. The link will open to a Slack login page where after you login (as admin) you will need to find and be asked to install the Amazon Quick app within your Slack workspace.
**Note**  
You may see a "This app is not approved by Slack banner." This message can be ignored.

1. Choose **Allow** to install your Amazon Quick App for Slack.

1. Once the installation is complete, you will see the page confirming that the **Congratulations\! Your Slack App has been successfully installed.**

1. Choose **Open the Amazon Quick App in Slack**.

1. This will open your Slack workspace where all users will be required to sign-in.

Your Slack extension has now been successfully deployed and is available for users.

## Edit Slack extension
<a name="edit-extensions-slack"></a>

**Note**  
This action requires full author permissions.

As an author, you can edit the extensions you deploy to your users. Modify extension settings to update names, descriptions, or configuration options. Changes take effect immediately and apply to all users with access to the extension.

1. Sign in to the Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select the three dot menu icon for the Slack extension you need to edit.

1. Select **Edit**.

1. Edit the configuration as required and select **Save** to confirm the changes.

## Share Slack extension
<a name="share-extensions-slack"></a>

Share ownership and management permissions with specific users and groups, enabling multiple users to manage extensions and assist with installation. You can assign different permission levels and manage access as needed.

1. Sign in to the Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select the three dot menu icon for the Slack extension you need to share.

1. Select **Share**.

1. Enter the users and groups you would like to share the extension with.

1. Select **Share** to send the access email to each group and user.

1. From the drop-down next to each name, you can edit their access levels (**Viewer** or **Owner**).

1. **Optional:** You could select **Remove access** to delete the access for the selected group or user.

## Delete Slack extension
<a name="delete-extensions-slack"></a>

As an author, you can delete the extensions you deploy to your users. Permanently remove a extension from your Quick console and revoke access for all users. This action cannot be undone and requires confirmation.

1. Sign in to Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select the three dot menu icon for the Slack extension you need to delete.

1. Select **Delete**.

1. Enter the word, "confirm", and select **DELETE**.