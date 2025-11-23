# Turning off group lifecycle events

You can turn off group lifecycle events to stop AWS Resource Groups from emitting events to Amazon EventBridge. You can do
this by using either the AWS Management Console or by using a command from the AWS CLI or one of the SDK
APIs.

###### Note

Turning off group lifecycle events deletes the Resource Groups managed EventBridge rule used to scan your resource tags
and CloudFormation stacks for changes. Resource Groups can no longer pass those changes to EventBridge. Any rules
you defined in EventBridge that look for Resource Groups events stop receiving events to process. If you
intend to turn on group lifecycle events again in the future, you can disable your rules. If you don't
intend to use those rules again, you can delete them. For more information, see [Disabling or
deleting an EventBridge rule](../../../eventbridge/latest/userguide/delete-or-disable-rule.md "../../../eventbridge/latest/userguide/delete-or-disable-rule.md") in the _Amazon EventBridge User Guide_.

Turning off group lifecycle events does **_not_** delete the service-linked role. You can [delete the service-linked role manually](security_iam_service-linked-roles.md#delete-service-linked-role "security_iam_service-linked-roles.md#delete-service-linked-role")
if you wish using IAM. If you later need to turn on group lifecycle events again and the
service-linked role doesn't exist, Resource Groups recreates it automatically.

###### Minimum permissions

To turn off group lifecycle events in your current AWS account, you must sign in as an AWS Identity and Access Management
(IAM) principal with the following permissions:

- `resource-groups:UpdateAccountSettings`
- `events:DeleteRule`
- `events:RemoveTargets`
- `events:DescribeRule`
- `events:ListTargetsByRule`

AWS Management Console

###### To turn off group lifecycle event notifications to EventBridge

1. Open the **[Settings](https://console.aws.amazon.com/resource-groups/groups/settings "https://console.aws.amazon.com/resource-groups/groups/settings")** page in the Resource Groups console.
2. In the **Group lifecycle events** section, choose the switch next to
   **Notifications are turned on**.
3. On the confirmation dialog, choose **Turn off
   notifications**.

The feature switch is displayed: **Event notifications are
turned off**.

At this point, Resource Groups no longer sends events to the EventBridge default event bus, and
any rules that you have no longer receive group notification events to process.
You can optionally delete those rules to complete the clean up.

AWS CLI

###### To turn off group lifecycle event notifications to EventBridge

The following example show how to use the AWS CLI to turn off group
lifecycle events in Resource Groups.

```
`$` `aws resource-groups update-account-settings \
 ----group-lifecycle-events-desired-status INACTIVE`
`{
 "AccountSettings": {
 "GroupLifecycleEventsDesiredStatus": "INACTIVE",
 "GroupLifecycleEventsStatus": "INACTIVE"
 }
}`
```

For more information, see the following resources:

- AWS CLI – [aws resource-groups update-account-settings](../../../cli/latest/reference/resource-groups/update-account-settings.md "../../../cli/latest/reference/resource-groups/update-account-settings.md") and
  [aws resource-groups get-account-settings](../../../cli/latest/reference/resource-groups/get-account-settings.md "../../../cli/latest/reference/resource-groups/get-account-settings.md")
- API – [UpdateAccountSettings](../APIReference/API_UpdateAccountSettings.md "../APIReference/API_UpdateAccountSettings.md") and [GetAccountSettings](../APIReference/API_GetAccountSettings.md "../APIReference/API_GetAccountSettings.md")
