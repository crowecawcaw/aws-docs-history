Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# How do notifications work?

You can set up your project to provide notifications to your team messaging application,
such as Slack.

## What permissions are necessary for

notifications?

Any project member can configure, view, update, or delete notification settings
for a channel
in
CodeCatalyst. However, only
users with the **Space administrator** role can add or delete Slack workspaces. All
users can configure what project events they want to receive emails about for the projects
they belong to in CodeCatalyst.

## What CodeCatalyst events can I configure

notifications about?

You can configure CodeCatalyst to deliver notifications to one or more Slack channels about
workflow events. Once notifications have been configured between a CodeCatalyst project and Slack,
project users can choose to add their own Slack member ID in order to receive direct messages
in Slack channels about CodeCatalyst events. Users who add their Slack member IDs will receive
direct mentions to their IDs in the Slack channels configured for their projects, helping
raise awareness about events they care about.

You can also choose what events you want to receive emails about. These emails are sent to
the email address configured for your AWS Builder ID.

## How are notifications surfaced?

You can configure CodeCatalyst to deliver notifications to one or more Slack channels. You need
to authorize CodeCatalyst to grant permissions to access your Slack workspace. Once the authorization
is provided, CodeCatalyst can deliver notifications to the Slack channels you
configure. If a project
member chooses to add their Slack member ID, they can receive mentions about CodeCatalyst
events in the Slack channels configured for that project.

## How do I set up notifications?

Email notifications
are configured as part of CodeCatalyst. Project users can choose what events they'd like to receive
emails about in their **My settings** page.

To set up
Slack
notifications for your project resources, you must complete the following
high-level tasks.

###### To set up notifications (high-level tasks)

1. In CodeCatalyst, you **set up a connection** between CodeCatalyst and
   a messaging client, such as Slack. Once a Slack workspace is connected, it will be available
   to all projects in the space.

###### Note

Only users with a Space administrator role can add or delete a Slack workspace. 2. In your project in CodeCatalyst, **add the channel** where you
want your team to receive notifications. 3. In CodeCatalyst, you **turn on notifications** for various
events, such as workflow run failure, and specify the channel where you want them
sent.

For detailed steps, see [Getting started with Slack notifications](getting-started-notifications.md "getting-started-notifications.md").

Once notifications have been configured between a CodeCatalyst space and Slack, users can
choose to add their own Slack member IDs to receive direct messages about CodeCatalyst events in the
Slack channels configured for their projects,
