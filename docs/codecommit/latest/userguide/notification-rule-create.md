# Create a notification rule

You can use notification rules to notify users of important changes, such as when a pull
request is created in a repository. Notification rules specify both the events and the Amazon SNS topic
that is used to send notifications. For more information, see [What are notifications?](../../../codestar-notifications/latest/userguide/welcome.md "../../../codestar-notifications/latest/userguide/welcome.md")

###### Note

This feature is not available in the Europe (Milan) Region. To learn how to configure
notifications in the experience available in that Region, see [Configure Repository Notifications](https://github.com/awsdocs/aws-codecommit-user-guide/blob/master/doc_source/how-to-repository-email-create.2.md "https://github.com/awsdocs/aws-codecommit-user-guide/blob/master/doc_source/how-to-repository-email-create.2.md").

You can use the console or the AWS CLI to create notification rules for AWS CodeCommit.

# To create a notification rule

(console)

1. Sign in to the AWS Management Console and open the CodeCommit console at
   [https://console.aws.amazon.com/codecommit/](https://console.aws.amazon.com/codecommit/ "https://console.aws.amazon.com/codecommit/").
2. Choose **Repositories**, and then choose a repository where you want to
   add notification rules.
3. On the repository page, choose **Notify**, and then choose
   **Create notification rule**. You can also go to the
   **Settings** page for the repository and choose **Create notification
   rule**.
4. In **Notification name**, enter a name for the rule.
5. In **Detail type**, choose **Basic** if you want only the
   information provided to Amazon EventBridge included in the notification. Choose **Full**
   if you want to include information provided to Amazon EventBridge and information that might be supplied
   by the CodeCommit or the notification manager.

For more information, see [Understanding Notification Contents and Security](../../../codestar-notifications/latest/userguide/security.md#security-notifications "../../../codestar-notifications/latest/userguide/security.md#security-notifications"). 6. In **Events that trigger notifications**, select the events for which you
want to send notifications. For more information, see [Events for
Notification Rules on Repositories](../../../codestar-notifications/latest/userguide/concepts.md#events-ref-repositories "../../../codestar-notifications/latest/userguide/concepts.md#events-ref-repositories"). 7. In **Targets**, do one of the following:

    * If you have already configured a resource to use with notifications, in **Choose
     target type**, choose either **Amazon Q Developer in chat applications (Slack)** or **SNS
     topic**. In **Choose target**, choose the name of the client (for a
     Slack client configured in Amazon Q Developer in chat applications) or the Amazon Resource Name (ARN) of the Amazon SNS topic (for
     Amazon SNS topics already configured with the policy required for notifications).
    * If you have not configured a resource to use with notifications, choose **Create
     target**, and then choose **SNS topic**. Provide a name for the
     topic after **codestar-notifications-**, and then choose
     **Create**.

###### Note

    * If you create the Amazon SNS topic as part of creating the notification rule, the policy that
     allows the notifications feature to publish events to the topic is applied for you. Using a
     topic created for notification rules helps ensure that you subscribe only those users that
     you want to receive notifications about this resource.
    * You cannot create an Amazon Q Developer in chat applications client as part of creating a notification rule. If you
     choose Amazon Q Developer in chat applications (Slack), you will see a button directing you to configure a client in Amazon Q Developer in chat applications.
     Choosing that option opens the Amazon Q Developer in chat applications console. For more information, see  [Configure
     Integrations Between Notifications and Amazon Q Developer in chat applications](../../../codestar-notifications/latest/userguide/notifications-chatbot.md "../../../codestar-notifications/latest/userguide/notifications-chatbot.md").
    * If you want to use an existing Amazon SNS topic as a target, you must add the required policy
     for AWS CodeStar Notifications in addition to any other policies that might exist for that topic. For more
     information, see [Configure Amazon SNS Topics
     for Notifications](../../../codestar-notifications/latest/userguide/set-up-sns.md "../../../codestar-notifications/latest/userguide/set-up-sns.md")  and [Understanding Notification Contents and Security](../../../codestar-notifications/latest/userguide/security.md#security-notifications "../../../codestar-notifications/latest/userguide/security.md#security-notifications").

8. To finish creating the rule, choose **Submit**.
9. You must subscribe users to the Amazon SNS topic for the rule before they can receive
   notifications. For more information, see [Subscribe Users to Amazon SNS Topics That Are Targets](../../../codestar-notifications/latest/userguide/subscribe-users-sns.md "../../../codestar-notifications/latest/userguide/subscribe-users-sns.md"). You can also set up integration
   between notifications and Amazon Q Developer in chat applications to send notifications to Amazon Chime chatrooms. For more information,
   see [Configure Integration Between
   Notifications and Amazon Q Developer in chat applications](../../../codestar-notifications/latest/userguide/notifications-chatbot.md "../../../codestar-notifications/latest/userguide/notifications-chatbot.md").

# To create a notification rule (AWS CLI)

1. At a terminal or command prompt, run the **create-notification rule**
   command to generate the JSON skeleton:

```
aws codestar-notifications create-notification-rule --generate-cli-skeleton > `rule.json`
```

You can name the file anything you want. In this example, the file is named
`rule.json`. 2. Open the JSON file in a plain-text editor and edit it to include the resource, event types,
and target you want for the rule. The following example shows a notification rule named
`MyNotificationRule` for a repository named
`MyDemoRepo` in an AWS acccount with the ID
`123456789012`. Notifications with the full detail type are
sent to an Amazon SNS topic named `MyNotificationTopic` when branches and
tags are created:

```
{
    "Name": "`MyNotificationRule`",
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

Save the file. 3. Using the file you just edited, at the terminal or command line, run the
**create-notification-rule** command again to create the notification
rule:

```
aws codestar-notifications create-notification-rule --cli-input-json  file://`rule.json`
```

4. If successful, the command returns the ARN of the notification rule, similar to the
   following:

```
{
    "Arn": "arn:aws:codestar-notifications:`us-east-1`:`123456789012`:notificationrule/dc82df7a-EXAMPLE"
}
```
