# Create or configure a notification rule

target

Notification rule targets are Amazon SNS topics or AWS Chatbot clients configured for Slack or Microsoft Teams
channels.

An AWS Chatbot client must be created before you can select a client as a target. When you
choose an AWS Chatbot client as a target for a notification rule, an Amazon SNS topic is
configured for that AWS Chatbot client with all the policies required for notifications to be
sent to the Slack or Microsoft Teams channel. You don't have to configure any existing Amazon SNS topics for the
AWS Chatbot client.

You can create Amazon SNS notification rule targets in the Developer Tools console when you create a
notification rule. The policy that allows notifications to be sent to that topic is
applied for you. This is the easiest way to create a target for a notification rule. For
more information, see [Create a notification rule](notification-rule-create.md "notification-rule-create.md").

If you use an existing Amazon SNS topic, you must configure it with an access policy that
allows the resource to send notifications to that topic. For an example, see [Configure Amazon SNS topics for notifications](set-up-sns.md "set-up-sns.md").

###### Note

If you want to use an existing Amazon SNS topic instead of creating a new one,
in **Targets**, choose its ARN. Make sure the topic has the
appropriate access policy, and that the subscriber list
contains only those users who are allowed to see information about the
resource. If the Amazon SNS topic is a topic that was used for
CodeCommit notifications before November 5, 2019, it will contain a policy that allows
CodeCommit to publish to it that contains different permissions than those required
for AWS CodeStar Notifications. Using these topics is not recommended. If you want to use one created
for that experience, you must add the required policy for AWS CodeStar Notifications in addition to the one
that already exists. For more information, see [Configure Amazon SNS topics for notifications](set-up-sns.md "set-up-sns.md") and [Understanding notification contents and
security](security.md#security-notifications "security.md#security-notifications").

If you want to extend the reach of notifications, you can manually configure
integration between notifications and AWS Chatbot so that notifications are sent to Amazon Chime
chatrooms. For more information, see [Targets](concepts.md#targets "concepts.md#targets")
and [To integrate notifications with AWS Chatbot
and Amazon Chime](notifications-chatbot.md#notifications-chatbot-chime "notifications-chatbot.md#notifications-chatbot-chime").

# To configure an existing Amazon SNS

topic to use as a notification rule target (console)

1. Sign in to the AWS Management Console and open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation bar, choose **Topics**. Choose the topic,
   and then choose **Edit**.
3. Expand **Access policy**, and then choose
   **Advanced**.
4. In the JSON editor, add the following statement to the policy.
   Include the topic ARN, AWS Region, AWS account ID, and topic name.

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
      "Resource": "arn:aws:sns:`us-east-2`:`123456789012`:`codestar-notifications-MyTopicForNotificationRules`"
    }
```

The policy statement should look like the following.

```
{
  "Version": "2008-10-17",
  "Id": "__default_policy_ID",
  "Statement": [
    {
      "Sid": "__default_statement_ID",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "SNS:GetTopicAttributes",
        "SNS:SetTopicAttributes",
        "SNS:AddPermission",
        "SNS:RemovePermission",
        "SNS:DeleteTopic",
        "SNS:Subscribe",
        "SNS:ListSubscriptionsByTopic",
        "SNS:Publish"
      ],
      "Resource": "arn:aws:sns:`us-east-2`:`123456789012`:`codestar-notifications-MyTopicForNotificationRules`",
      "Condition": {
        "StringEquals": {
          "AWS:SourceOwner": "123456789012"
        }
      }
    },
	{
      "Sid": "AWSCodeStarNotifications_publish",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "codestar-notifications.amazonaws.com"
        ]
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:`us-east-2`:`123456789012`:`codestar-notifications-MyTopicForNotificationRules`"
    }
  ]
}
```

5. Choose **Save changes**.
6. In **Subscriptions**, review the list of topic subscribers.
   Add, edit, or delete subscribers as appropriate for this notification rule
   target. Make sure that the subscriber list contains only those users who are
   allowed to see information about the resource. For more information, see [Understanding notification contents and
   security](security.md#security-notifications "security.md#security-notifications").

# To create an AWS Chatbot client with

Slack
to use as a target

1. Follow the instructions in [Setting up
   AWS Chatbot with
   Slack](../../../chatbot/latest/adminguide/slack-setup.md#slack-client-setup "../../../chatbot/latest/adminguide/slack-setup.md#slack-client-setup")
   in the _AWS Chatbot Administrator Guide_. When you do so, consider the
   following choices for optimal integration with notifications:
   - When creating an IAM role, consider choosing a role name that makes it easy to identify the
     purpose of this role (for example,
     `AWSCodeStarNotifications-Chatbot-Slack-Role`). This
     can help you identify the purpose of the role in the future.
   - In **SNS topics**, you don't have to choose a topic or an AWS Region. When
     you choose the AWS Chatbot client as a [target](concepts.md#targets "concepts.md#targets"), an
     Amazon SNS topic with all the required permissions is created and configured for the
     AWS Chatbot client as part of the notification rule creation process.

2. Complete the client creation process. This client is then available for you to choose
   as a target when creating notification rules. For more information, see [Create a notification rule](notification-rule-create.md "notification-rule-create.md").

###### Note

Do not remove the Amazon SNS topic from the AWS Chatbot client after it has been configured
for you. Doing so will prevent notifications from being sent to Slack.

# To create an AWS Chatbot client with

Microsoft Teams to use as a target

1. Follow the instructions in [Setting up
   AWS Chatbot with Microsoft Teams](../../../chatbot/latest/adminguide/teams-setup.md#teams-client-setup "../../../chatbot/latest/adminguide/teams-setup.md#teams-client-setup")
   in the _AWS Chatbot Administrator Guide_. When you do so, consider the
   following choices for optimal integration with notifications:
   - When creating an IAM role, consider choosing a role name that makes it easy to identify the
     purpose of this role (for example,
     `AWSCodeStarNotifications-Chatbot-Microsoft-Teams-Role`). This
     can help you identify the purpose of the role in the future.
   - In **SNS topics**, you don't have to choose a topic or an AWS Region. When
     you choose the AWS Chatbot client as a [target](concepts.md#targets "concepts.md#targets"), an
     Amazon SNS topic with all the required permissions is created and configured for the
     AWS Chatbot client as part of the notification rule creation process.

2. Complete the client creation process. This client is then available for you to choose
   as a target when creating notification rules. For more information, see [Create a notification rule](notification-rule-create.md "notification-rule-create.md").

###### Note

Do not remove the Amazon SNS topic from the AWS Chatbot client after it has been configured
for you. Doing so will prevent notifications from being sent to Microsoft Teams.
