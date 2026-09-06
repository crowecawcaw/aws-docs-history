

# Troubleshooting AWS User Notifications
<a name="user-notifications-troubleshooting"></a>

In this section, you can find answers to some common questions and concerns.

## I can't see any notifications.
<a name="cant-see-notifications"></a>
+ **No notifications configured in the account.**

  Verify that your notification configurations exist. From the navigation pane, choose **Notification configurations** to view a list of existing configurations in your account.
+ **Notification configuration error.**

  Verify that the status of your notification configuration is **Active**. From the navigation pane, choose **Notification configurations** to view a list of existing configurations in your account. You can check the status of your notification configurations by viewing the list. You can also choose a notification configuration to navigate to its details page. If the notification configuration shows an error, choose **Edit** on the **Notification Configuration** page to fix the issue.
+ **Event not matching expected pattern.**

  Verify that the created Event Rule matches the emitted AWS event. For more information, see [Events from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html) in the *Amazon EventBridge User Guide*.

## My Event Rules are taking a long time (more than 5 mins) or failing to create.
<a name="rules-fail"></a>
+ **Permissions error** - Contact your account administrator to discuss your permissions. 
+ **System error** - Try to create the rule again.

## My advanced filters aren't reflected in the managed rule.
<a name="advanced-filter-error"></a>

Managed rules only contain source and detail-type fields. Your advanced filtering is still applied by User Notifications. For more information, see [Amazon EventBridge managed rules in AWS User Notifications](ev-managed-rules.md).

## My notification isn't showing any details.
<a name="no-notification-details"></a>

We're working with other AWS services to make sure User Notifications contain all relevant details. Your feedback helps us prioritize the notifications we should work on next. To send feedback, choose **Feedback** in the lower left menu of the [User Notifications console](https://console.aws.amazon.com/notifications/).

## I received an exception.
<a name="error-codes"></a>

The following list includes exceptions that User Notifications can return. It also describes the HTTP status code associated with each exception.
+ **ValidationException**

  HTTP Status Code: 400
+ **ResourceNotFoundException**

  HTTP Status Code: 404
+ **ServiceQuotaExceededException**

  HTTP Status Code: 402
+ **AccessDeniedException**

  HTTP Status Code: 403 
+ **ConflictException**

  HTTP Status Code: 409
+ **ThrottlingException**

  HTTP Status Code: 429
+ **InternalServerException**

  HTTP Status Code: 500