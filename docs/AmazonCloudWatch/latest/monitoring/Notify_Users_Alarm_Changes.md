# Notifying users on alarm changes

This section explains how you can use AWS User Notifications or Amazon Simple Notification Service to have
users be notified of alarm changes.

## Setting up AWS User Notifications

You can use [AWS User
Notifications](../../../notifications/latest/userguide/what-is-service.md "../../../notifications/latest/userguide/what-is-service.md") to set up delivery channels to get notified about CloudWatch alarm state
change and configuration change events. You receive a notification when an event matches a
rule that you specify. You can receive notifications for events through multiple channels,
including email, [AWS Chatbot](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md") chat notifications, or [AWS Console
Mobile Application push notifications](../../../consolemobileapp/latest/userguide/managing-notifications.md "../../../consolemobileapp/latest/userguide/managing-notifications.md"). You can also see notifications in the at
[Console Notifications Center](https://console.aws.amazon.com/notifications "https://console.aws.amazon.com/notifications"). User
Notifications supports aggregation, which can reduce the number of notifications you
receive during specific events.

The notification configurations you create with AWS User Notifications do not count
towards the limit on the number of actions you can configure per target alarm state. As
AWS User Notifications matches the events emitted to Amazon EventBridge, it sends notifications
for all the alarms in your account and selected Regions, unless you specify an advanced
filter to allowlist or denylist specific alarms or patterns.

The following example of an advanced filter matches an alarm state change from OK to
ALARM on the alarm named `ServerCpuTooHigh`.

```
{
"detail": {
    "alarmName": ["ServerCpuTooHigh"],
    "previousState": { "value": ["OK"] },
    "state": { "value": ["ALARM"] }
  }
}
```

You can use any of the properties published by an alarm in EventBridge events to create a
filter. For more information, see [Alarm events and EventBridge](cloudwatch-and-eventbridge.md "cloudwatch-and-eventbridge.md").

## Setting up Amazon SNS notifications

You can use Amazon Simple Notification Service to send both application-to-application (A2A) messaging and
application-to-person (A2P) messaging, including mobile text messaging (SMS) and email
messages. For more information, see [Amazon SNS event
destinations](../../../sns/latest/dg/sns-event-destinations.md "../../../sns/latest/dg/sns-event-destinations.md").

For every state that an alarm can take, you can configure the alarm to send a message
to an SNS topic. Every Amazon SNS topic you configure for a state on a given alarm counts
towards the limit on the number of actions you can configure for that alarm and state. You
can send messages to the same Amazon SNS topic from any alarms in your account, and use the
same Amazon SNS topic for both application (A2A) and person (A2P) consumers. Because this
configuration is done at the alarm level, only the alarms you have configured send
messages to the selected Amazon SNS topic.

First, create a topic, then subscribe to it. You can optionally publish a test message
to the topic. For an example, see [Setting up an Amazon SNS topic using the AWS Management Console](#set-up-sns-topic-console "#set-up-sns-topic-console"). Or for more information, see [Getting started with
Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md").

Alternatively, if you plan to use the AWS Management Console to create your CloudWatch alarm, you can
skip this procedure because you can create the topic when you create the alarm.

When you create a CloudWatch alarm, you can add actions for any target state the alarm
enters. Add an Amazon SNS notification for the state you want to be notified about, and select
the Amazon SNS topic you created in the previous step to send an email notification when the
alarm enters the selected state.

###### Note

When you create an Amazon SNS topic, you choose to make it a _standard
topic_ or a _FIFO topic_. CloudWatch guarantees the publication
of all alarm notifications to both types of topics. However, even if you use a FIFO
topic, in rare cases CloudWatch sends the notifications to the topic out of order. If you use
a FIFO topic, the alarm sets the message group ID of the alarm notifications to be a
hash of the ARN of the alarm.

###### Topics

- [Preventing confused deputy security issues](#SNS_Confused_Deputy "#SNS_Confused_Deputy")
- [Setting up an Amazon SNS topic using the AWS Management Console](#set-up-sns-topic-console "#set-up-sns-topic-console")
- [Setting up an SNS topic using the AWS CLI](#set-up-sns-topic-cli "#set-up-sns-topic-cli")

### Preventing confused deputy security issues

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the
action. In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_).
The calling service can be manipulated to use its permissions to act on another
customer's resources in a way it should not otherwise have permission to access. To
prevent this, AWS provides tools that help you protect your data for all services with
service principals that have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn"), [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount"), [`aws:SourceOrgID`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgid"), and [`aws:SourceOrgPaths`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgpaths "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgpaths") global condition context keys in resource
policies to limit the permissions that Amazon SNS gives another service to the resource. Use
`aws:SourceArn` to associate only one resource with cross-service access.
Use `aws:SourceAccount` to let any resource in that account be associated
with the cross-service use. Use `aws:SourceOrgID` to allow any resource from
any account within an organization be associated with the cross-service use. Use
`aws:SourceOrgPaths` to associate any resource from accounts within an
AWS Organizations path with the cross-service use. For more information about using and
understanding paths, see [aws:SourceOrgPaths](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgpaths "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgpaths") in the IAM User Guide.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the
resource. If you don't know the full ARN of the resource or if you are specifying
multiple resources, use the `aws:SourceArn` global context condition key with
wildcard characters (`*`) for the unknown portions of the ARN. For example,
`arn:aws:`servicename`:*:`123456789012`:*`.

If the `aws:SourceArn` value does not contain the account ID, such as an
Amazon S3 bucket ARN, you must use both `aws:SourceAccount` and
`aws:SourceArn` to limit permissions.

To protect against the confused deputy problem at scale, use the
`aws:SourceOrgID` or `aws:SourceOrgPaths` global condition
context key with the organization ID or organization path of the resource in your
resource-based policies. Policies that include the `aws:SourceOrgID` or
`aws:SourceOrgPaths` key will automatically include the correct accounts
and you don't have to manually update the policies when you add, remove, or move
accounts in your organization.

The value of `aws:SourceArn` must be the ARN of the alarm that is sending
notifications.

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in CloudWatch to prevent the
confused deputy problem.

```
{
    "Statement": [{
        "Effect": "Allow",
        "Principal": {
            "Service": "cloudwatch.amazonaws.com"
        },
        "Action": "SNS:Publish",
        "Resource": "arn:aws:sns:us-east-2:444455556666:MyTopic",
        "Condition": {
            "ArnLike": {
                "aws:SourceArn": "arn:aws:cloudwatch:us-east-2:111122223333:alarm:*"
            },
            "StringEquals": {
                "aws:SourceAccount": "111122223333"
            }
        }
    }]
}
```

If an alarm ARN includes any non-ASCII characters, use only the
`aws:SourceAccount` global condition key to limit the permissions.

### Setting up an Amazon SNS topic using the AWS Management Console

First, create a topic, then subscribe to it. You can optionally publish a test
message to the topic.

###### To create an SNS topic

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. On the Amazon SNS dashboard, under **Common actions**, choose
   **Create Topic**.
3. In the **Create new topic** dialog box, for **Topic
   name**, enter a name for the topic (for example,
   `my-topic`).
4. Choose **Create topic**.
5. Copy the **Topic ARN** for the next task (for example,
   arn:aws:sns:us-east-1:111122223333:my-topic).

###### To subscribe to an SNS topic

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Subscriptions**,
   **Create subscription**.
3. In the **Create subscription** dialog box, for **Topic
   ARN**, paste the topic ARN that you created in the previous task.
4. For **Protocol**, choose **Email**.
5. For **Endpoint**, enter an email address that you can use to
   receive the notification, and then choose **Create
   subscription**.
6. From your email application, open the message from AWS Notifications and
   confirm your subscription.

Your web browser displays a confirmation response from Amazon SNS.

###### To publish a test message to an SNS topic

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**.
3. On the **Topics** page, select a topic and choose
   **Publish to topic**.
4. In the **Publish a message** page, for
   **Subject**, enter a subject line for your message, and for
   **Message**, enter a brief message.
5. Choose **Publish Message**.
6. Check your email to confirm that you received the message.

### Setting up an SNS topic using the AWS CLI

First, you create an SNS topic, and then you publish a message directly to the topic
to test that you have properly configured it.

###### To set up an SNS topic

1. Create the topic using the [create-topic](../../../cli/latest/reference/sns/create-topic.md "../../../cli/latest/reference/sns/create-topic.md") command as follows.

```
`aws sns create-topic --name `my-topic``
```

Amazon SNS returns a topic ARN with the following format:

```
{
    "TopicArn": "arn:aws:sns:us-east-1:111122223333:my-topic"
}
```

2. Subscribe your email address to the topic using the [subscribe](../../../cli/latest/reference/sns/subscribe.md "../../../cli/latest/reference/sns/subscribe.md") command. If the
   subscription request succeeds, you receive a confirmation email message.

```
`aws sns subscribe --topic-arn arn:aws:sns:`us-east-1`:`111122223333`:`my-topic` --protocol email --notification-endpoint` `my-email-address`
```

Amazon SNS returns the following:

```
{
    "SubscriptionArn": "pending confirmation"
}
```

3. From your email application, open the message from AWS Notifications and
   confirm your subscription.

Your web browser displays a confirmation response from Amazon Simple Notification Service. 4. Check the subscription using the [list-subscriptions-by-topic](../../../cli/latest/reference/sns/list-subscriptions-by-topic.md "../../../cli/latest/reference/sns/list-subscriptions-by-topic.md") command.

```
`aws sns list-subscriptions-by-topic --topic-arn arn:aws:sns:`us-east-1`:`111122223333`:`my-topic``
```

Amazon SNS returns the following:

```
{
  "Subscriptions": [
    {
        "Owner": "111122223333",
        "Endpoint": "me@mycompany.com",
        "Protocol": "email",
        "TopicArn": "arn:aws:sns:us-east-1:111122223333:my-topic",
        "SubscriptionArn": "arn:aws:sns:us-east-1:111122223333:my-topic:64886986-bf10-48fb-a2f1-dab033aa67a3"
    }
  ]
}
```

5. (Optional) Publish a test message to the topic using the [publish](../../../cli/latest/reference/sns/publish.md "../../../cli/latest/reference/sns/publish.md") command.

```
`aws sns publish --message "Verification" --topic arn:aws:sns:`us-east-1`:`111122223333`:`my-topic``
```

Amazon SNS returns the following.

```
{
    "MessageId": "42f189a0-3094-5cf6-8fd7-c2dde61a4d7d"
}
```

6. Check your email to confirm that you received the message.

## Schema of Amazon SNS notifications when alarms change state

This section lists the schemas of the notifications sent to Amazon SNS topics when alarms
change their state.

**Schema when a metric alarm changes state**

```
{
  "AlarmName": "string",
  "AlarmDescription": "string",
  "AWSAccountId": "string",
  "AlarmConfigurationUpdatedTimestamp": "string",
  "NewStateValue": "string",
  "NewStateReason": "string",
  "StateChangeTime": "string",
  "Region": "string",
  "AlarmArn": "string",
  "OldStateValue": "string",
  "OKActions": ["string"],
  "AlarmActions": ["string"],
  "InsufficientDataActions": ["string"],
  "Trigger": {
    "MetricName": "string",
    "Namespace": "string",
    "StatisticType": "string",
    "Statistic": "string",
    "Unit": "string or null",
    "Dimensions": [
      {
        "value": "string",
        "name": "string"
      }
    ],
    "Period": "integer",
    "EvaluationPeriods": "integer",
    "DatapointsToAlarm": "integer",
    "ComparisonOperator": "string",
    "Threshold": "number",
    "TreatMissingData": "string",
    "EvaluateLowSampleCountPercentile": "string or null"
  }
}
```

**Schema when a composite alarm changes state**

```
{
  "AlarmName": "string",
  "AlarmDescription": "string",
  "AWSAccountId": "string",
  "NewStateValue": "string",
  "NewStateReason": "string",
  "StateChangeTime": "string",
  "Region": "string",
  "AlarmArn": "string",
  "OKActions": [String],
  "AlarmActions": [String],
  "InsufficientDataActions": [String],
  "OldStateValue": "string",
  "AlarmRule": "string",
  "TriggeringChildren": [String]
}

```
