

# Set up event notifications
<a name="setup-event-notifications"></a>

To receive IAM Identity Center Identity Store event notifications, you create an Amazon EventBridge rule that selects the events that you want and sends them to a target. Then you test the rule.

## Prerequisites
<a name="setup-event-notifications-prerequisites"></a>

Before you create a rule, make sure that you have the following:
+ The AWS account and AWS Region where your IAM Identity Center instance is enabled. You create the rule there.
+ Permissions to create EventBridge rules and targets in that account, such as `events:PutRule` and `events:PutTargets`.
+ A target to receive the events, such as a AWS Lambda function, an Amazon Simple Notification Service (Amazon SNS) topic, or an Amazon SQS queue.

## Step 1: Choose the events that you want
<a name="setup-event-notifications-step-pattern"></a>

An event pattern selects the events that your rule sends to its target. Include both the event source and the event names in your pattern.

AWS CloudTrail also sends Identity Store API calls to EventBridge with the event source `aws.identitystore`. Including the event names makes sure that the rule receives only the events in this section.

The following JSON event pattern matches all event notifications that IAM Identity Center Identity Store sends:

```
{
  "source": ["aws.identitystore"],
  "detail-type": [
    "User Created", "User Updated", "User Deleted",
    "Group Created", "Group Updated", "Group Deleted",
    "GroupMembership Created", "GroupMembership Deleted",
    "IdentityStore Created", "IdentityStore Updated", "IdentityStore Deleted"
  ]
}
```

The following JSON event pattern matches only events for deleted users and for users removed from groups, for example to remove access in downstream applications:

```
{
  "source": ["aws.identitystore"],
  "detail-type": ["User Deleted", "GroupMembership Deleted"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the Amazon EventBridge User Guide.

## Step 2: Create the rule
<a name="setup-event-notifications-step-rule"></a>

Use the following procedure to create the rule and target in the Amazon EventBridge console.

**To create a rule (console)**

1. Sign in to the account where your IAM Identity Center instance is enabled, and open the [Amazon EventBridge console](https://console.aws.amazon.com/events/home#/rules).

1. Choose the AWS Region where your IAM Identity Center instance is enabled.

1. In the navigation pane, choose **Rules**, and then choose **Create rule**.

1. On the rule builder selection page, choose **Advanced Builder**. Enter a **Name** for the rule. For **Event bus**, choose **AWS default event bus**. For **Rule type**, choose **Rule with an event pattern**. Choose **Next**.

1. For **Event source**, choose **AWS events or EventBridge partner events**. For **Creation method**, choose **Custom pattern (JSON editor)**, and then enter the pattern that you chose in Step 1. Choose **Next**.

1. For **Target type**, select **AWS service**. Select a target, such as a AWS Lambda function or an Amazon SNS topic, and provide the requested information. Choose **Next**.

1. (Optional) Add tags, and then choose **Next**. Review the rule, and then choose **Create rule**.

You now have a rule that delivers matching IAM Identity Center events to your target.

For more information, see [Creating rules using the Advanced Builder](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) in the Amazon EventBridge User Guide.

Alternatively, use the following procedure to create the rule and target with the AWS CLI. Before you begin, make sure that the AWS CLI is installed and configured for the account and AWS Region where your IAM Identity Center instance is enabled. In the examples, replace the {{italicized}} values with your own.

**To create a rule (AWS CLI)**

1. Save the pattern that you chose in Step 1 to a file, for example `identity-events.json`.

1. Create the rule on the default event bus. Replace `{{us-east-1}}` with the AWS Region where your IAM Identity Center instance is enabled, and `{{identity-change-events}}` with a name for your rule.

   ```
   aws events put-rule \
     --name {{identity-change-events}} \
     --event-pattern file://identity-events.json \
     --region {{us-east-1}}
   ```

1. Add a target to the rule. The following example sends events to an Amazon SNS topic; replace `{{identity-change-topic}}` with your topic name and `111122223333` with your AWS account ID.

   ```
   aws events put-targets \
     --rule {{identity-change-events}} \
     --targets "Id"="1","Arn"="arn:aws:sns:{{us-east-1}}:111122223333:{{identity-change-topic}}" \
     --region {{us-east-1}}
   ```

When you use the AWS CLI, make sure that EventBridge has permission to send events to the target, for example through the target's resource-based policy. For more information, see [Using resource-based policies for Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-resource-based.html).

You now have a rule that delivers matching IAM Identity Center events to your target.

## Step 3: Test the rule
<a name="setup-event-notifications-step-test"></a>

1. Wait about 1 minute after you create the rule before you test it, because new rules might not match events immediately. Then make a change in IAM Identity Center, such as adding a user to a group.

1. Confirm that your target received a `GroupMembership Created` event. To view events while you test, add an Amazon CloudWatch Logs log group as a second target.

1. If no event arrives, check the following:
   + The rule is on the default event bus, in the AWS account and AWS Region where your IAM Identity Center instance is enabled.
   + The event pattern uses the event source `aws.identitystore`. Each event name in the pattern matches exactly, including capitalization and spaces. For example, the event name is `GroupMembership Created`, not `Group Membership Created` or `groupmembership created`.
   + EventBridge has permission to send events to the target, through either the execution role that you chose when you created the rule or the target's resource-based policy.

When your target receives the test event, your rule is working.

## Example – User Updated event
<a name="setup-event-notifications-example"></a>

The following JSON example shows a `User Updated` event as your target receives it. Other events use the same structure. The `detail-type` field contains the event name, and the `detail` field contains the ID of the user, group, or group membership that changed.

```
{
  "version": "0",
  "id": "c22ba61f-32ac-42f1-a59b-f7f667b428ab",
  "detail-type": "User Updated",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-01-02T11:59:59Z",
  "region": "us-west-2",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890",
    "arn:aws:identitystore:::user/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  ],
  "detail": {
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "user": {
      "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  }
}
```

The event includes the following key fields:
+ `detail-type` – The event name.
+ `source` – The event source, always `aws.identitystore`.
+ `resources` – The ARNs of the identity store and of the user, group, or group membership that changed.
+ `detail` – The IDs of the request and of the resource that changed.