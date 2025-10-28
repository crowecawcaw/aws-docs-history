# Updating your notifications in DevOps Guru

Set up Amazon Simple Notification Service topics that are used to notify you about important Amazon DevOps Guru events.
You can choose from a list of topic names that already exist in your AWS account,
enter the name for a new topic that DevOps Guru creates in your account, or enter the Amazon
Resource Name (ARN) of an existing topic in any AWS account in your Region. If you
specify the ARN of a topic that is not in your account, you must grant permission for
DevOps Guru to access that topic by adding an IAM policy to it. For more information, see
[Permissions for Amazon SNS topics](sns-required-permissions.md "sns-required-permissions.md").
You can specify up to two topics.

DevOps Guru sends notifications for the following updates:

- A new insight is created.
- A new anomaly is added to an insight.
- The severity of an insight is upgraded from `Low` or `Medium` to `High`.
- The status of an insight changes from ongoing to resolved.
- A recommendation for an insight is identified.
  DevOps Guru also sends notifications if a selected AWS CloudFormation stack or tag key is invalid when you are attempting to add resources to your DevOps Guru account.

You can choose to receive Amazon SNS notifications for all kinds of updates to an issue or to receive Amazon SNS notifications only when the
issue is opened, closed, or has a change in severity. By default, you receive notifications for
all updates.

To update your notifications, first navigate to the notifications page and then choose whether to add, remove, or update configurations for Amazon SNS notification topics.

###### Topics

- [Navigate to notification settings in the DevOps Guru console](#navigate-to-notification-settings "#navigate-to-notification-settings")
- [Adding Amazon SNS notification topics in the DevOps Guru console](#add-notification-topics "#add-notification-topics")
- [Removing Amazon SNS notification topics in the DevOps Guru console](#remove-notification-topics "#remove-notification-topics")
- [Updating Amazon SNS notification configurations](#update-notification-configurations "#update-notification-configurations")
- [Permissions added to
  your Amazon SNS topic](#permissions-added-to-sns-topic-on-update "#permissions-added-to-sns-topic-on-update")

## Navigate to notification settings in the DevOps Guru console

To update notifications, you must first navigate to the notification settings section.

###### To navigate to the notification settings section

1. Open the Amazon DevOps Guru console at [https://console.aws.amazon.com/devops-guru/](https://console.aws.amazon.com/devops-guru/ "https://console.aws.amazon.com/devops-guru/").
2. Choose **Settings** in the navigation pane.

The Settings page includes the **Notifications** section, with information about configured Amazon SNS topics.

## Adding Amazon SNS notification topics in the DevOps Guru console

###### To add an Amazon SNS notification topic in the DevOps Guru console

1. [Navigate to notification settings in the DevOps Guru console](#navigate-to-notification-settings "#navigate-to-notification-settings").
2. Choose **Add notification**.
3. To add an Amazon SNS topic, do one of the following.
   - Choose **Generate a new SNS topic using email**. Then, from **Specify the email address**,
     enter the email address you want to receive notifications. To enter in additional email addresses, choose **Add new email**.
   - Choose **Use an existing SNS topic**. Then, from **Choose a topic in
     your AWS account**, choose the topic you want to use.
   - Choose **Use an existing SNS topic ARN to specify an existing topic from another account**. Then, in **Enter an ARN for a topic**,
     enter the topic ARN. The ARN is the topic's Amazon Resource Name. You can specify a topic in a different account. If you use
     a topic in another account, you must add a resource policy to the topic. For more information,
     see [Permissions for Amazon SNS topics](sns-required-permissions.md "sns-required-permissions.md").

4. Choose **Save**.

## Removing Amazon SNS notification topics in the DevOps Guru console

###### To remove Amazon SNS topics in the DevOps Guru console

1. [Navigate to notification settings in the DevOps Guru console](#navigate-to-notification-settings "#navigate-to-notification-settings").
2. Choose **Select existing topic**.
3. From the drop-down menu, select the topic you want to remove.
4. Choose **Remove**.
5. Choose **Save**.

## Updating Amazon SNS notification configurations

There are two types of notification configurations for Amazon SNS notification topics in DevOps Guru.
You can choose to receive notifications of all severity levels
or only notifications with **High** and **Medium** severity levels.
You can also choose to receive notifications for all kinds of updates or only some kinds of updates.

When you choose to receive Amazon SNS notifications for all kinds of updates to the issue, DevOps Guru sends notifications for the following updates:

- A new insight is created.
- A new anomaly is added to an insight.
- The severity of an insight is upgraded from `Low` or `Medium` to `High`.
- The status of an insight changes from ongoing to resolved.
- A recommendation for an insight is identified.

By default, you receive only **High** and **Medium** severity level notifications, and you receive notifications for all kinds of updates.

###### To update notification configurations for Amazon SNS notification topics

1. [Navigate to notification settings in the DevOps Guru console](#navigate-to-notification-settings "#navigate-to-notification-settings").
2. Choose **Select existing topic**.
3. From the drop-down menu, select the topic you want to make updates to.
4. Choose **All severity levels** to receive notifications with High, Medium, and Low severity levels,
   or choose **Only High and Medium** to receive notifications with High and Medium severity levels.
5. Choose **Notify me on all updates to the insight**, or choose **Notify me when an insight is opened or closed, or the severity level changes from Low or Medium to High**.
6. Choose **Save**.

## Permissions added to

your Amazon SNS topic

An Amazon SNS topic is a resource that contains
an AWS Identity and Access Management (IAM) resource policy. When you specify a topic here, DevOps Guru appends the following permissions
to its resource policy.

```
{
    "Sid": "DevOpsGuru-added-SNS-topic-permissions",
    "Effect": "Allow",
    "Principal": {
        "Service": "region-id.devops-guru.amazonaws.com"
    },
    "Action": "sns:Publish",
    "Resource": "arn:aws:sns:`region-id`:`topic-owner-account-id`:`my-topic-name`",
    "Condition" : {
      "StringEquals" : {
        "AWS:SourceArn": "arn:aws:devops-guru:`region-id`:`topic-owner-account-id`:channel/`devops-guru-channel-id`",
        "AWS:SourceAccount": "`topic-owner-account-id`"
    }
  }
}
```

These permissions are required for DevOps Guru to publish notifications using a topic. If you prefer to not have
these permissions on the topic, you can safely remove them and the topic will continue to work as it did
before you chose it. However, if these appended permissions are removed, DevOps Guru cannot use the topic to
generate notifications.
