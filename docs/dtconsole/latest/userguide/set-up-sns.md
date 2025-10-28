# Configure Amazon SNS topics for notifications

The easiest way to set up notifications is to create an Amazon SNS topic when you create a
notification rule. You can use an existing Amazon SNS topic if it meets the following
requirements:

- It was created in the same AWS Region as the resource (build project,
  deployment application, repository, or pipeline) for which you want to create
  notification rules.
- It has not been used for sending notifications for CodeCommit before November 5,

2019. If it has, it will contain policy statements that enabled that
      functionality. You can choose to use this topic, but you will need to add the
      additional policy as specified in the procedure. You should not remove the
      existing policy statement if one or more repositories is still configured for
      notifications before November 5, 2019.

- It has a policy that allows AWS CodeStar Notifications to publish notifications to the
  topic.

###### To configure an Amazon SNS topic to use as a

target for AWS CodeStar Notifications notification rules

1. Sign in to the AWS Management Console and open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation bar, choose **Topics**, choose the topic
   you want to configure, and then choose **Edit**.
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
6. If you want to use an AWS KMS-encrypted Amazon SNS topic to send notifications, you
   must also enable compatibility between the event source (AWS CodeStar Notifications) and the
   encrypted topic by adding the following statement to the policy of the
   AWS KMS key. Replace the AWS Region (in this example, us-east-2) with the
   AWS Region where the key was created.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "codestar-notifications.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey*",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "sns.us-east-2.amazonaws.com"
 }
 }
 }
 ]
}`

```

For more information, see [Encryption at rest](../../../kms/latest/developerguide/sns-server-side-encryption.md#sns-what-permissions-for-sse "../../../kms/latest/developerguide/sns-server-side-encryption.md#sns-what-permissions-for-sse") and [Using policy conditions with
AWS KMS](../../../kms/latest/developerguide/policy-conditions.md "../../../kms/latest/developerguide/policy-conditions.md") in the _AWS Key Management Service Developer Guide_.
