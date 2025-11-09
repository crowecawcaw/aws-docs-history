# Amazon EventBridge managed rules in AWS User Notifications

AWS User Notifications uses Amazon EventBridge managed rules. A managed rule is a unique type of rule that is directly linked to User Notifications.
These rules match incoming events and send them to targets for processing. Managed rules are predefined by User Notifications and include event patterns that are required by the
service to manage customer notifications, and unless defined otherwise, only the owning service can utilize these managed rules. For more information, see
[Rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in the _Amazon EventBridge User Guide_.

User Notifications managed rules are linked to `notifications.amazonaws.com` service principal. These managed rules are managed through the [AWSUserNotificationsServiceLinkedRolePolicy service-linked role](slr-call-services.md "slr-call-services.md").
To delete these rules, a special confirmation by the customer is required. For more information, see [Deleting managed rules for AWS User Notifications](#delete-rules "#delete-rules").

## Amazon EventBridge managed rules deployed by AWS User Notifications

The followng table displays Amazon EventBridge managed rules:

| Rule name                        | Description                                                                                                       | Definition                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| AWSUserNotificationsManagedRule- | AWS User Notifications rule for source. This can be any Amazon EventBridge source. For example, `aws.cloudwatch`. | Example:<br>`<br>{"source": ["aws.cloudwatch"],"detail-type": ["CloudWatch Alarm State Change"]}<br>` |

###### Note

The managed rule User Notifications creates in EventBridge only contains source and detail-type fields, regardless of whether the User Notifications event rule includes additional filters. User Notifications always filters based on the
User Notifications event rule.

For example, the User Notifications event rule for Amazon Elastic Compute Cloud instance state changed to "terminated", "stopping", "stopped", or "shutting-down" shows:

```
{
 "source": ["aws.ec2"],
 "detail-type": ["EC2 Instance State-change Notification"],
 "detail": {
    "state": ["terminated", "stopping", "stopped", "shutting-down"]
    }
}

```

The corresponding EventBridge managed rule shows:

```
{
 "source": ["aws.ec2"],
 "detail-type": ["EC2 Instance State-change Notification"]
}

```

This rule only generates notifications for Amazon EC2 instance state changed to "terminated", "stopping", "stopped", or "shutting-down". It won't generate notifications for other state changes.

## Creating managed rules for AWS User Notifications

You don’t need to manually create Amazon EventBridge managed rules. Managed rules are automatically created for you based on your specified event rules when you create notification configurations.

User Notifications creates one managed rule per source (for example, EC2, S3). Newly created event rules correspond to existing managed rules if applicable. If no existing managed rules are found, User Notifications creates a new managed rule.

## Editing managed rules for AWS User Notifications

User Notifications doesn't allow you to edit managed rules. The name, description, and event pattern for each managed rule are predefined by User Notifications.

## Deleting managed rules for AWS User Notifications

###### Warning

Don't delete User Notifications managed rules unless you're certain all dependent event rules are removed. Deleting managed rules that are being used by User Notifications may cause some notifications to stop working.
For more information, see [Rules managed by AWS services](../../../eventbridge/latest/userguide/eb-rules.md#eb-rules-managed "../../../eventbridge/latest/userguide/eb-rules.md#eb-rules-managed") in the _Amazon EventBridge User Guide_.

You don’t need to manually delete managed rules. When you delete a notification configuration or specific event rule in a notification configuration, User Notifications cleans up the resources and deletes applicable managed rules owned by User Notifications for you.
