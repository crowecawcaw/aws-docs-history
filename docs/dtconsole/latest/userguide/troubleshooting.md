# Troubleshooting

The following information might help you troubleshoot common issues with
notifications.

###### Topics

- [I get a permissions error when I try to
  create a notification rule on a resource](#troubleshooting-permissions-error "#troubleshooting-permissions-error")
- [I cannot view notification rules](#troubleshooting-cannot-view "#troubleshooting-cannot-view")
- [I cannot create notification
  rules](#troubleshooting-cannot-create-rule "#troubleshooting-cannot-create-rule")
- [I am receiving notifications for a
  resource I can't access](#troubleshooting-resource-no-access "#troubleshooting-resource-no-access")
- [I am not receiving Amazon SNS notifications](#troubleshooting-no-SNS "#troubleshooting-no-SNS")
- [I am receiving duplicate
  notifications about events](#troubleshooting-duplicate-notifications "#troubleshooting-duplicate-notifications")
- [I want to understand why a notification
  target status shows as unreachable](#troubleshooting-resource-unavailable "#troubleshooting-resource-unavailable")
- [I want to increase my quotas for
  notifications and resources](#troubleshooting-limit-increase "#troubleshooting-limit-increase")

## I get a permissions error when I try to

create a notification rule on a resource

Make sure that you have sufficient permissions. For more information, see [Identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## I cannot view notification rules

**Problem:** When you are in the Developer Tools console and choose
**Notifications** under **Settings**, you see a
permissions error.

**Possible fixes:** You might not have the permissions
required to view notifications. While most managed policies for AWS Developer Tools services, such as CodeCommit
and CodePipeline, include permissions for notifications, services that do not currently support
notifications do not include permissions to view them. Alternatively, you might have a custom
policy applied to your
IAM user
or role that does not allow you to view notifications. For more information, see [Identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## I cannot create notification

rules

You might not have the permissions required to create a notification rule. For more
information, see [Identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## I am receiving notifications for a

resource I can't access

When you create a notification rule and add a target, the notifications feature does not
validate whether the recipient has access to the resource. It is possible for you to receive
notifications about a resource that you can't access. If you cannot remove yourself, ask to be
removed from the subscription list for the target.

## I am not receiving Amazon SNS notifications

To troubleshoot problems with the Amazon SNS topic, check the following:

- Make sure that the Amazon SNS topic was created in the same AWS Region as the
  notification rule.
- Make sure that your email alias is subscribed to the correct topic and that you have
  confirmed the subscription. For more information, see [Subscribing an
  endpoint to an Amazon SNS topic](../../../sns/latest/dg/sns-tutorial-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-tutorial-create-subscribe-endpoint-to-topic.md").
- Verify that the topic policy has been edited to allow
  AWS CodeStar Notifications
  to push notifications to that topic. The topic policy should include a statement similar
  to the following:

```
{
    "Sid": "AWSCodeStarNotifications_publish",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "codestar-notifications.amazonaws.com"
        ]
    },
    "Action": "SNS:Publish",
    "Resource": "arn:aws:sns:us-east-1:123456789012:MyNotificationTopicName",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "123456789012"
        }
    }
}

```

For more information, see [Configure Amazon SNS topics for notifications](set-up-sns.md "set-up-sns.md").

## I am receiving duplicate

notifications about events

Here are the most common reasons for receiving multiple notifications:

- Multiple notification rules that include the same event type have been configured for
  a resource, and you are subscribed to the Amazon SNS topics that are the targets for those
  rules. To solve this issue, either unsubscribe from one of the topics or edit the
  notification rules to remove duplication.
- One or more notification rule targets are integrated with AWS Chatbot and you are receiving
  notifications in your email inbox and a Slack channel, Microsoft Teams channel, or Amazon Chime chatroom. To solve this
  issue, consider unsubscribing your email address from the Amazon SNS topic that is the target
  for the rule and use the Slack channel, Microsoft Teams channel, or Amazon Chime chatroom to view notifications.

## I want to understand why a notification

target status shows as unreachable

Targets have two possible statuses: **_Active_** and
**_Unreachable_**. **Unreachable**
indicates that notifications were sent to a target, and the delivery was not successful.
Notifications continue to be sent to that target, and if successful, the status resets to
**Active**.

The target for a notification rule might become unavailable for one of the following
reasons:

- The resource (Amazon SNS topic or AWS Chatbot client) has been deleted. Choose another target
  for the notification rule.
- The Amazon SNS topic is encrypted, and either the required policy for encrypted topics is
  missing, or the AWS KMS key has been deleted. For more information, see [Configure Amazon SNS topics for notifications](set-up-sns.md "set-up-sns.md").
- The Amazon SNS topic does not have the required policy for notifications. Notifications
  cannot be sent to an Amazon SNS topic unless it has the policy. For more information, see [Configure Amazon SNS topics for notifications](set-up-sns.md "set-up-sns.md").
- The supporting service for the target (Amazon SNS or AWS Chatbot) might be experiencing
  issues.

## I want to increase my quotas for

notifications and resources

Currently, you cannot change any quotas. See [Quotas for notifications](limits.md "limits.md").
