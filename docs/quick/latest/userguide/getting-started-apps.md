

# Getting started with apps in Quick
<a name="getting-started-apps"></a>

You can create your first app in apps in Amazon Quick in minutes. This section walks you through each step.

## Prerequisites
<a name="apps-prerequisites"></a>

Before you begin, confirm the following:
+ You have an active Amazon Quick account.
+ Your subscription includes Author, Professional, Author Pro, Enterprise, or Admin Pro access.

## Open the apps in Quick landing page
<a name="apps-open-landing"></a>

To open the apps in Quick landing page:

1. Sign in to Amazon Quick.

1. In the navigation pane, choose **Apps**.

The apps in Quick landing page provides a prompt area where you describe the app you want to build. Rotating example prompts suggest ideas you can use or customize.

Below the prompt area, you can browse your existing apps in two views: **Library** (all apps you have access to, including apps shared with you) and **My apps** (apps you created). You can search for apps by name or owner and sort results by last visited, last updated, or name.

## Create an app
<a name="apps-create"></a>

To create an app:

1. In the prompt area, enter a description of the app you want to build. Alternatively, choose one of the example prompts to start with a pre-written description, then edit it before proceeding.

1. Choose **Generate**.

1. Review the live preview in the apps in Quick editor as the agent builds your app. Use the chat panel to provide follow-up instructions.

Write your description as if you were explaining the app to a colleague. Include the purpose, the audience, and the data it needs. A detailed description produces a better first version and reduces iteration.

## Edit an app
<a name="apps-edit"></a>

The apps in Quick editor is a two-panel workspace. The preview panel shows a live, interactive rendering of your app. The chat panel is where you converse with the apps in Quick agent to build, modify, and debug the app.

To edit an app:

1. Enter an instruction in the chat panel.

1. Wait for the agent to update the preview with your changes.

1. Interact with the preview to test buttons, forms, navigation, and other features.

The chat conversation persists across sessions. If you close the editor and return later, your previous messages are still there. Choose **Load older messages** to see the full history.

## Manage versions
<a name="apps-versions"></a>

Apps in Quick automatically creates a new version each time the agent changes your app. You do not need to save manually. A version selector in the editor lets you browse all previous versions and preview any of them.

To restore a previous version:

1. Select the version you want to review from the version selector.

1. Confirm the preview shows the state you want.

1. Choose **Restore to this version**.

Restoring a version does not affect the published version. You must publish again for end users to see the change. For more information about recovering from a broken app, see [Recovering from a broken app](apps-troubleshooting.md#apps-ts-broken-page).

## Review app settings
<a name="apps-settings"></a>

The app settings panel provides two views:
+ **Overview** — Shows the app name (editable), a unique app ID, creation date, last published date, the published URL, the public URL (if published publicly), and an editable description. You can also delete the app from this view.
+ **Assets** — Lists all integrations and services registered on the app. Each asset shows its name, type (Action or AI), and permission level (Read or Write).

## Publish an app
<a name="apps-publish"></a>

To publish an app:

1. When your app is ready for others to use, choose **Publish**.

1. Copy the shareable URL from the confirmation dialog.

You can continue editing after publishing. Changes do not affect the published version until you publish again.

## Share an app
<a name="apps-share"></a>

To share an app:

1. Choose **Share** to open the sharing controls.

1. Search for users by name, alias, or email.

1. Assign each person a role and choose **Share**.

Each shared user has a role that you can change at any time:
+ **Co-owner** — Can edit, publish, and share the app.
+ **Viewer** — Can view and interact with the published app.

Apps in Quick supports three access levels:


| Access level | Description | 
| --- | --- | 
| Limited | Only users you explicitly share the app with can access it. | 
| Account | Everyone in your Amazon Quick account can access the app. | 
| Public | Anyone on the internet can access the app without signing in. Available on Free and Plus accounts only. | 

You can also toggle **Share with all** to make the app accessible to everyone in your Amazon Quick account, or choose **Copy link** to copy the published URL.

### Publish an app to the public internet
<a name="apps-publish-public"></a>

To publish an app publicly (Free and Plus accounts):

1. Choose **Share** to open the sharing controls.

1. Set the access level to **Public**.

1. Choose **Publish**.

After publishing, the app receives a public URL that you can share with anyone. Anonymous viewers can use the app without creating an account.

**Important**  
Public apps cannot use connectors, embedded visuals, embedded chat experiences, or Amazon Quick spaces. If your app uses any of these integrations, remove them before publishing publicly.

## Manage public app usage
<a name="apps-manage-public-usage"></a>

When your app is published publicly, AI inference usage counts against your subscription quota. Monitor your usage in the Amazon Quick account settings.

To manage or revoke public access:

1. Choose **Share** to open the sharing controls.

1. Change the access level from **Public** to **Limited** or **Account**.

Revoking public access takes effect immediately. The public URL stops working and anonymous viewers can no longer access the app.