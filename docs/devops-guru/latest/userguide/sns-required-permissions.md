# Permissions for Amazon SNS topics

Use the information in this topic only if you want to configure Amazon DevOps Guru to deliver
notifications to Amazon SNS topics owned by another AWS account.

For DevOps Guru to deliver notifications to an Amazon SNS topic owned by a different account, you must attach a policy to the Amazon SNS topic
that grants DevOps Guru permissions to send notifications to it. If you configure
DevOps Guru to deliver notifications to Amazon SNS topics owned by the same account you use for DevOps Guru, then DevOps Guru adds a policy to the
topics for you.

After you attach a policy to configure permissions for an Amazon SNS topic in another account, you can add the Amazon SNS topic in DevOps Guru.
You can also update your Amazon SNS policy with a notification channel to make it more secure.

###### Note

DevOps Guru currently only supports cross-account access in the same Region.

###### Topics

- [Configuring permissions for an Amazon SNS topic in another account](#sns-permissions-attach-policy "#sns-permissions-attach-policy")
- [Adding an Amazon SNS topic from another account](#sns-permissions-add-sns-topic "#sns-permissions-add-sns-topic")
- [Updating your Amazon SNS policy with a notification channel (recommended)](#sns-permissions-policy-notification-channel "#sns-permissions-policy-notification-channel")

## Configuring permissions for an Amazon SNS topic in another account

### Adding permissions as an IAM role

To use an Amazon SNS topic from another account after logging in with an IAM role, you must attach a policy to the Amazon SNS topic you want to use.
To attach a policy to an Amazon SNS topic from another account while using an IAM role, you need to have the following permissions for that account resource as part of your IAM role:

- sns:CreateTopic
- sns:GetTopicAttributes
- sns:SetTopicAttributes
- sns:Publish

Attach the following policy to the
Amazon SNS topic you want to use. For the `Resource` key,
`topic-owner-account-id` is the account ID of the topic
owner, `topic-sender-account-id` is the account ID of the user
who set up DevOps Guru, and `devops-guru-role` is the IAM role of the individual user involved. You must substitute appropriate values for
`region-id` (for example, `us-west-2`), and
`my-topic-name`.

### Adding permissions as an IAM user

To use an Amazon SNS topic from another account as an IAM user, attach the following policy to the
Amazon SNS topic you want to use. For the `Resource` key,
`topic-owner-account-id` is the account ID of the topic
owner, `topic-sender-account-id` is the account ID of the user
who set up DevOps Guru, and `devops-guru-user-name` is the individual
IAM user involved. You must substitute appropriate values for
`region-id` (for example, `us-west-2`) and
`my-topic-name`.

###### Note

Where possible, we recommend relying on temporary credentials instead of creating IAM users who have long-term credentials such as passwords and access keys.
For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Adding an Amazon SNS topic from another account

After you configure permissions for an Amazon SNS topic in another account, you can add that Amazon SNS topic to your DevOps Guru notification settings.
You can add the Amazon SNS topic using the AWS CLI or the DevOps Guru console.

- When you use the console, you must select the option
  **Use an SNS topic ARN to specify an existing topic** in order to use a topic from another account.
- When you use the AWS CLI operation [add-notification-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/add-notification-channel.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/add-notification-channel.html"), you must specify the `TopicArn` within the `NotificationChannelConfig` object.

###### Add an Amazon SNS topic from another account using the console

1. Open the Amazon DevOps Guru console at [https://console.aws.amazon.com/devops-guru/](https://console.aws.amazon.com/devops-guru/ "https://console.aws.amazon.com/devops-guru/").
2. Open the navigation pane, and then choose **Settings**.
3. Go to the **Notifications** section and choose **Edit**.
4. Choose **Add SNS topic**.
5. Choose **Use an SNS topic ARN to specify an existing topic**.
6. Enter the ARN of the Amazon SNS topic you want to use. You should have already configured permissions for this topic by attaching a policy to it.
7. (Optional) Choose **Notification configuration** to edit notification frequency settings.
8. Choose **Save**.

After you add the Amazon SNS topic to your notification settings, DevOps Guru uses that topic to notify you of important events, such as when a new insight is created.

## Updating your Amazon SNS policy with a notification channel (recommended)

After you add a topic, we recommend that you make your policy more secure by
specifying permissions for only the DevOps Guru notification channel that contains your
topic.

###### Update your Amazon SNS topic policy with a notification channel (recommended)

1. Run the `list-notification-channels` DevOps Guru AWS CLI command in your account that you want to send notifications from.

```
aws devops-guru list-notification-channels
```

2. In the `list-notification-channels` response, make a note of the
   channel ID that contains your Amazon SNS topic's ARN. The channel ID is a
   guid.

For example, in the following response, the channel ID for the topic with the
ARN `arn:aws:sns:`region-id`:`111122223333`:`topic-name`is
`e89be5f7-989d-4c4c-b1fe-e7145037e531``

```
{
  "Channels": [
    {
      "Id": "`e89be5f7-989d-4c4c-b1fe-e7145037e531`",
      "Config": {
      "Sns": {
          "TopicArn": "arn:aws:sns:`region-id`:`111122223333`:`topic-name`"
        },
      "Filters": {
          "MessageTypes": [`"CLOSED_INSIGHT", "NEW_INSIGHT", "SEVERITY_UPGRADED"`],
          "Severities": [`"HIGH", "MEDIUM"`]
        }
      }
    }
  ]
}

```

3. Go to the policy that you created in another account using the topic owner ID in
   [Configuring permissions for an Amazon SNS topic in another account](#sns-permissions-attach-policy "#sns-permissions-attach-policy"). In the
   `Condition` statement of the policy, add the line that specifies
   the `SourceArn`. The ARN contains your Region ID (for example,
   `us-east-1`), the AWS account number of the topic's sender,
   and the channel ID you made a note of.

Your updated `Condition` statement looks like the following.

```
"Condition" : {
  "StringEquals" : {
    "AWS:SourceArn": "arn:aws:devops-guru:`us-east-1`:`111122223333`:channel/`e89be5f7-989d-4c4c-b1fe-e7145037e531`",
    "AWS:SourceAccount": "`111122223333`"
   }
 }
```

If `AddNotificationChannel` is unable to add your SNS Topic, check that
your IAM policy has the following permissions.
