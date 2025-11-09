Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Sending Slack and email notifications from CodeCatalyst

You can configure CodeCatalyst to send notifications about events that occur in your project.
CodeCatalyst can send notifications to messaging clients such as Slack channels. Having CodeCatalyst send
messages to Slack channels helps to ensure that your entire team is aware of important events,
such as workflow failures. Optionally, you can choose to have CodeCatalyst @mention you in
the Slack messages it sends out so that you receive a corresponding direct message (DM).

CodeCatalyst can also send notifications directly to you in an email. Email notifications will
be sent about events in any project where you are a member. These emails will be sent to
the email address configured in your AWS Builder ID.

###### Note

The events that can be sent to Slack channels can be different from those sent by email.

###### Topics

- [Configuring email notifications](notifications-personal.md "notifications-personal.md")
- [Sending notifications to Slack channels](notifications-projects.md "notifications-projects.md")
- [Configuring Slack direct messages](notifications-personal-slack.md "notifications-personal-slack.md")
- [Editing notifications for a notification channel](notifications-edit.md "notifications-edit.md")
- [Removing a channel](notifications-remove-channel.md "notifications-remove-channel.md")
