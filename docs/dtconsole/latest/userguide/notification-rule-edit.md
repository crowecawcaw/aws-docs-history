# Edit a notification rule

You can edit a notification rule to change its name, the events for which it sends
notifications, the detail type, or the target or targets to which it sends
notifications. You can use the Developer Tools console or the AWS CLI to edit a notification
rule.

# To edit a notification rule

(console)

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/ "https://console.aws.amazon.com/codesuite/settings/notifications/").
2. In the navigation bar, expand **Settings**, and then choose
   **Notification rules**.
3. In **Notification rules**, review the rules configured for
   resources in your AWS account in the AWS Region where you are currently
   signed in. Use the selector to change the AWS Region.
4. Choose the rule from the list, and then choose **Edit**. Make
   your changes, and then choose **Submit**.

# To edit a notification rule

(AWS CLI)

1. At a terminal or command prompt, run the [describe-notification-rule
   command](notification-rule-view.md#notification-rule-view-details-cli "notification-rule-view.md#notification-rule-view-details-cli") to view the structure of the notification rule.
2. Run the **update-notification rule** command to generate the
   JSON skeleton and then save it to a file.

```
aws codestar-notifications update-notification-rule --generate-cli-skeleton > `update.json`
```

You can name the file anything you want. In this example, the file is
`update.json`. 3. Open the JSON file in a plaintext editor and make changes to the rule.

The following example shows a notification rule named
`MyNotificationRule` for a repository named
`MyDemoRepo` in an AWS account with the ID
`123456789012`. Notifications are sent to
an Amazon SNS topic named `MyNotificationTopic` when
branches and tags are created. The rule name is changed to
`MyNewNotificationRule`.

```
{
    "Name": "`MyNewNotificationRule`",
    "EventTypeIds": [
        "codecommit-repository-branches-and-tags-created"
    ],
    "Resource": "arn:aws:codecommit:`us-east-1`:`123456789012`:`MyDemoRepo`",
    "Targets": [
        {
            "TargetType": "SNS",
            "TargetAddress": "arn:aws:sns:`us-east-1`:`123456789012`:`MyNotificationTopic`"
        }
    ],
    "Status": "ENABLED",
    "DetailType": "FULL"
}
```

Save the file. 4. Using the file you just edited, at the terminal or command line, run the
**update-notification-rule** command again to update the
notification rule.

```
aws codestar-notifications update-notification-rule --cli-input-json  file://`update`.json
```

5. If successful, the command returns the Amazon Resource Name (ARN) of the
   notification rule, similar to the following.

```
{
    "Arn": "arn:aws:codestar-notifications:`us-east-1`:`123456789012`:notificationrule/dc82df7a-EXAMPLE"
}
```

# To remove a tag from a

notification rule (AWS CLI)

1. At a terminal or command prompt, run the **untag-resource**
   command. For example, the following command removes a tag with the name of
   `Team`.

```
aws codestar-notifications untag-resource --arn arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/fe1efd35-EXAMPLE --tag-keys Team
```

2. If successful, this command returns nothing.

## See also

- [Add or remove a target for a
  notification rule](notification-target-change-rule.md "notification-target-change-rule.md")
- [Enable or disable notifications for a notification rule](notification-rule-enable-disable.md "notification-rule-enable-disable.md")
- [Events](concepts.md#events "concepts.md#events")
