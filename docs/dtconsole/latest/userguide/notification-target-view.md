# View notification rule targets

You can use Developer Tools console, not the Amazon SNS console to view all of the notification rule
targets for all resources in an AWS Region. You can also view the details of a
notification rule target.

# To view notification rule targets

(console)

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/ "https://console.aws.amazon.com/codesuite/settings/notifications/").
2. In the navigation bar, expand **Settings**, and then choose
   **Notification rules**.
3. In **Notification rule targets**, review the list of targets
   used by notification rules in in your AWS account in the AWS Region where
   you are currently signed in. Use the selector to change the AWS Region. If
   the target status shows as **Unreachable**, you might need to
   investigate. For more information, see [Troubleshooting](troubleshooting.md "troubleshooting.md") .

# To view a list of notification

rule targets (AWS CLI)

1. At a terminal or command prompt, run the **list-targets**
   command to view a list of all notification rule targets for the specified AWS
   Region:

```
aws codestar-notifications list-targets --region `us-east-2`
```

2. If successful, this command returns the ID and ARN for each notification rule
   in the AWS Region, similar to the following:

```
{
    "Targets": [
        {
            "TargetAddress": "arn:aws:sns:us-east-2:`123456789012`:`MySNSTopicForNotificationRules`",
            "TargetType": "SNS",
            "TargetStatus": "ACTIVE"
        },
        {
            "TargetAddress": "arn:aws:chatbot::`123456789012`:chat-configuration/slack-channel/`MySlackChannelClientForMyDevTeam`",
            "TargetStatus": "ACTIVE",
            "TargetType": "AWSChatbotSlack"
        },
        {
            "TargetAddress": "arn:aws:sns:us-east-2:`123456789012`:`MySNSTopicForNotificationsAboutMyDemoRepo`",
            "TargetType": "SNS",
            "TargetStatus": "ACTIVE"
        }
    ]
}
```
