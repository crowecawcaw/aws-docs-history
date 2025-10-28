# Troubleshooting AWS User Notifications

In this section, you can find answers to some common questions and concerns.

- **No notifications configured in the account.**

Verify that your notification configurations exist. From the navigation pane, choose
**Notification configurations** to view a list of existing
configurations in your account.

- **Notification configuration error.**

Verify that the status of your notification configuration is
**Active**. From the navigation pane, choose **Notification
configurations** to view a list of existing configurations in your account.
You can check the status of your notification configurations by viewing the list. You
can also choose a notification configuration to navigate to its details page. If the
notification configuration shows an error, choose **Edit** on the
**Notification Configuration** page to fix the issue.

- **Event not matching expected pattern.**

Verify that the created Event Rule matches the emitted AWS event. For more
information, see [Events from
AWS services](../../../eventbridge/latest/userguide/eb-service-event.md "../../../eventbridge/latest/userguide/eb-service-event.md") in the _Amazon EventBridge User Guide_.

- **Permissions error** - Contact your account
  administrator to discuss your permissions.
- **System error** - Try to create the rule
  again.
  Managed rules only contain source and detail-type fields. Your advanced filtering is still applied by User Notifications. For more information, see [Amazon EventBridge managed rules in AWS User Notifications](ev-managed-rules.md "ev-managed-rules.md").

We're working with other AWS services to make sure User Notifications contain all relevant details.
Your feedback helps us prioritize the notifications we should work on next. To send
feedback, choose **Feedback** in the lower left menu of the [User Notifications console](https://console.aws.amazon.com/notifications/ "https://console.aws.amazon.com/notifications/").

The following list includes exceptions that User Notifications can return. It also describes the
HTTP status code associated with each exception.

- ValidationException

HTTP Status Code: 400

- ResourceNotFoundException

HTTP Status Code: 404

- ServiceQuotaExceededException

HTTP Status Code: 402

- AccessDeniedException

HTTP Status Code: 403

- ConflictException

HTTP Status Code: 409

- ThrottlingException

HTTP Status Code: 429

- InternalServerException

HTTP Status Code: 500
