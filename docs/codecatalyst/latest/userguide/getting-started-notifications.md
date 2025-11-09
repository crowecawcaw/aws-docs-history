Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Getting started with Slack notifications

After you create a project, you
can set
up Slack
notifications that help your team to monitor project resources.

These steps walk you through setting up Slack notifications for the first time in CodeCatalyst. If
you have already configured notifications, see [Sending Slack and email notifications from CodeCatalyst](notifications-manage.md "notifications-manage.md").

###### Note

The set of project events that can be sent to notification channels are not the same set
of events that users can choose to be notified about in email. For more information, see [Sending Slack and email notifications from CodeCatalyst](notifications-manage.md "notifications-manage.md").

###### Topics

- [Prerequisites](#getting-started-notifications-prerequisites "#getting-started-notifications-prerequisites")
- [Step 1: Connect CodeCatalyst to your
  Slack workspace](#getting-started-notifications-connect-slack "#getting-started-notifications-connect-slack")
- [Step 2: Add your Slack
  channel to CodeCatalyst](#getting-started-notifications-add-slack-channel "#getting-started-notifications-add-slack-channel")
- [Step
  3: Test notifications from CodeCatalyst to Slack](#getting-started-notifications-next-steps "#getting-started-notifications-next-steps")
- [Step 4: Next steps](#getting-started-notifications-test "#getting-started-notifications-test")

## Prerequisites

Before you begin, you need the following:

- A CodeCatalyst space. For information about creating a CodeCatalyst space and signing in
  for the first time, see [Set up and sign in to CodeCatalyst](setting-up-topnode.md "setting-up-topnode.md").
- A CodeCatalyst project. For more information, see [Creating a project](projects-create.md "projects-create.md").
- A CodeCatalyst account with the **Project administrator** or
  **Space administrator** role. For more information, see [Granting access with user roles](ipa-roles.md "ipa-roles.md").
- A Slack account and Slack workspace that can be accessed by CodeCatalyst.
- A Slack channel where CodeCatalyst will send notifications. The channel can be public or
  private.

## Step 1: Connect CodeCatalyst to your

Slack workspace

Only users with the
**Space administrator** role can add or delete Slack workspaces. Adding or deleting
a Slack workspace affects all projects in the space. To establish the connection between
CodeCatalyst and Slack, CodeCatalyst performs a secure OAuth authentication handshake with your
Slack workspace.

Use the following instructions to connect CodeCatalyst to your Slack workspace.

###### Note

This only needs to be done once for each Slack workspace. You can then set up notifications
by Slack channel.

###### To connect CodeCatalyst to your Slack workspace

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your project.
3. In the navigation pane, choose **Project settings**.
4. Choose the **Notifications** tab.
5. Choose **Configure notifications**.
6. Choose **Connect to Slack workspace**.
7. Read the dialog box contents, and then choose **Connect to
   Slack workspace**.
8. On the **Amazon Q Developer in chat applications** message:
   1. In the upper right, choose the Slack workspace that contains your channel.
   2. Choose **Allow**.You are returned to the CodeCatalyst console.

9. Continue to [Step 2: Add your Slack
   channel to CodeCatalyst](#getting-started-notifications-add-slack-channel "#getting-started-notifications-add-slack-channel").

## Step 2: Add your Slack

channel to CodeCatalyst

You need the Slack channel ID to add your channel to CodeCatalyst.

###### To get your Slack

channel ID

1. Sign in to Slack. For more information, see [Sign in to
   Slack](https://slack.com/help/articles/212681477-Sign-in-to-Slack "https://slack.com/help/articles/212681477-Sign-in-to-Slack").
2. Go to the Slack workspace that contains the channel where you want notifications to go.
   For more information, see [Switch
   between Slack workspaces](https://slack.com/help/articles/1500002200741-Switch-between-workspaces "https://slack.com/help/articles/1500002200741-Switch-between-workspaces") or [Sign in to additional
   Slack workspaces](https://slack.com/help/articles/212681477-Sign-in-to-Slack "https://slack.com/help/articles/212681477-Sign-in-to-Slack").
3. In the navigation pane, open the context (right click) menu for the channel where
   you want notifications to go, and choose **Open channel
   details**.

The channel ID is displayed at the bottom of the dialog box. 4. Copy the **Channel ID** value. You'll need it in the next
step.

Using the channel ID you just copied, you can now connect your Slack channel to
CodeCatalyst.

###### To add your Slack channel to CodeCatalyst

1. Before you begin, if your Slack channel is private, add the Amazon Q Developer in chat applications app to the
   channel as follows:
   1. In your Slack channel’s message box, enter `@aws` and choose
      **aws app** from the dialog box.
   2. Press Enter.

   A Slackbot message appears, indicating that Amazon Q Developer in chat applications is not in the private
   channel. 3. Choose **Invite Them** to invite Amazon Q Developer in chat applications to the
   channel.

2. In the CodeCatalyst console, choose **Next**.
3. In **Channel ID**, paste the Slack channel ID you obtained
   earlier.
4. In **Channel name**, enter a name. We recommend using the Slack
   channel name.
5. Choose **Next**.
6. In **Select notification events**, choose the type of event you want
   to receive notifications for.
7. Choose **Finish**.

## Step

3: Test notifications from CodeCatalyst to Slack

After your project is configured to send notifications for workflow status, you can view
your notifications in Slack.

###### To view your notifications in Slack

1. In your CodeCatalyst project, [start a workflow
   manually](workflows-manually-start.md "workflows-manually-start.md") in order to complete a workflow run and receive a status notification
   when the run finishes.
2. In Slack, view the channel you set up for notifications. Your notifications show the
   latest status from each workflow run, and whether it failed or succeeded.

## Step 4: Next steps

Once a Slack workspace is configured for your CodeCatalyst space, you can add additional
Slack channels existing CodeCatalyst projects, and add them for new projects after you create them.
You can also let project users know that they can configure personal Slack notifications for
their Slack member IDs, and configure the events for which they'll receive emails. For more
information, see [Sending Slack and email notifications from CodeCatalyst](notifications-manage.md "notifications-manage.md").
