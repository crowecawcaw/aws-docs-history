

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Sending notifications to Slack channels
<a name="notifications-projects"></a>

You can configure CodeCatalyst to send notifications about project events to your team's Slack channels. By doing this, you can help ensure that your entire team is aware of important events, such as when a workflow run fails.

**Note**  
Any member of a project can manage notifications sent to channels for that project. However, only users with the **Space administrator** role can add or delete Slack workspaces. 

Use the following instructions to add a Slack channel to which notifications will be sent.

**To add a Slack channel for notifications**

1. If you're adding your first Slack channel, see instead [Getting started with Slack notifications](getting-started-notifications.md).

   After setting up your first channel, return to this procedure to set up additional channels.

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your project.

1. In the navigation pane, choose **Project settings**.

1. Choose the **Notifications** tab.

1. Choose **Add channel**.

1. Choose **Choose workspace**, and then select the Slack workspace that contains the channel where you want to send notifications.

   If your Slack workspace is not in the list, you can add it by following the instructions in [Getting started with Slack notifications](getting-started-notifications.md).

1. Before entering a **Channel ID**, if the Slack channel you want to add is private, complete these steps:

   1. In your Slack channel’s message box, enter **@aws** and choose **aws app** from the pop-up.

   1. Press Enter.

      A Slackbot message appears, indicating that Amazon Q Developer in chat applications is not in the private channel. 

   1. Choose **Invite Them** to invite Amazon Q Developer in chat applications to the channel.

1. In CodeCatalyst's **Channel ID** field, enter the Slack channel ID. To find the ID, go to Slack, and in the navigation pane, right-click the channel and choose **Open channel details**.

   The channel ID is displayed at the bottom of the dialog box. 

1. In **Channel name**, enter a name. We recommend using the Slack channel name.

1. In **Select notification events**, choose the type of event you want to receive notifications for.

1. Choose **Add**.