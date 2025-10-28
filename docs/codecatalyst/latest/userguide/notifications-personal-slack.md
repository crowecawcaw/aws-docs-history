Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring Slack direct messages

If a CodeCatalyst project has been configured to [send
notifications to a Slack channel](notifications-projects.md "notifications-projects.md"), those notifications can also be sent as direct
messages (DMs). Having notifications sent to you directly as DMs can help raise awareness of
events happening in the projects where you have a role. To enable DMs, you must add your Slack
member ID to CodeCatalyst.

###### To configure Slack direct messages

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the top menu bar, choose your profile badge, and then choose **My
   settings**. The CodeCatalyst **My settings** page opens.

###### Tip

You can also find your user profile by going to the members page for a project or
space and choosing your name from the members list. 3. In **Personal Slack notifications**, choose **Connect Slack
ID**, and then choose **Connect to Slack workspace**. A
separate window will open.

###### Tip

This option is not configurable unless a user with the
**Space administrator** role has added a Slack workspace for your CodeCatalyst
space. For more information, see [Getting started with Slack notifications](getting-started-notifications.md "getting-started-notifications.md") and [Sending notifications to Slack channels](notifications-projects.md "notifications-projects.md"). 4. In the permissions request window, make sure that the name of the workspace matches
the Slack workspace configured for the CodeCatalyst space. Choose
**Allow** to allow Amazon Q Developer in chat applications access to the workspace. The window will
close, and the Slack workspace will show the **Connnection status** as
**Connected**.

###### Tip

If the connection status does not change, check to see if an error occurred
connecting the Slack workspace. You might have to scroll up to see the error. 5. To stop receiving personal Slack notifications, choose the connected Slack workspace,
and then choose **Disconnect Slack ID**.
