# Create a notification rule

You can use notification rules to notify users of important changes, such as when a pipeline
starts execution. Notification rules specify both the events and the Amazon SNS topic that is used to
send notifications. For more information, see [What are
notifications?](../../../codestar-notifications/latest/userguide/welcome.md "../../../codestar-notifications/latest/userguide/welcome.md")

You can use the console or the AWS CLI to create notification rules for AWS CodePipeline.

# To create a notification rule

(console)

1. Sign in to the AWS Management Console and open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
2. Choose **Pipelines**, and then choose a pipeline where you want to add
   notifications.
3. On the pipeline page, choose **Notify**, and then choose **Create
   notification rule**. You can also go to the **Settings** page for the
   pipeline and choose **Create notification rule**.
4. In **Notification name**, enter a name for the rule.
5. In **Detail type**, choose **Basic** if you want only the
   information provided to Amazon EventBridge included in the notification. Choose **Full**
   if you want to include information provided to Amazon EventBridge and information that might be supplied
   by the CodePipeline or the notification manager.

For more information, see [Understanding Notification Contents and Security](../../../codestar-notifications/latest/userguide/security.md#security-notifications "../../../codestar-notifications/latest/userguide/security.md#security-notifications"). 6. In **Events that trigger notifications**, select the events for which you
want to send notifications. For more information, see [Events for
Notification Rules on Pipelines](../../../codestar-notifications/latest/userguide/concepts.md#events-ref-pipeline "../../../codestar-notifications/latest/userguide/concepts.md#events-ref-pipeline"). 7. In **Targets**, do one of the following:

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
   between notifications and Amazon Q Developer in chat applications to send notifications to Amazon Chime chatrooms or Slack channels. For
   more information, see [Configure Integration
   Between Notifications and Amazon Q Developer in chat applications](../../../codestar-notifications/latest/userguide/notifications-chatbot.md "../../../codestar-notifications/latest/userguide/notifications-chatbot.md").

# To create a notification rule (AWS CLI)

1. At a terminal or command prompt, run the **create-notification rule**
   command to generate the JSON skeleton:

```
aws codestar-notifications create-notification-rule --generate-cli-skeleton > `rule.json`
```

You can name the file anything you want. In this example, the file is named
`rule.json`. 2. Open the JSON file in a plain-text editor and edit it to include the resource, event types,
and target you want for the rule. The following example shows a notification rule named
`MyNotificationRule` for a pipeline named
`MyDemoPipeline` in an AWS acccount with the ID
`123456789012`. Notifications are sent with the full detail
type to an Amazon SNS topic named
`codestar-notifications-MyNotificationTopic` when pipeline executions
start:

```
{
    "Name": "`MyNotificationRule`",
    "EventTypeIds": [
        "codepipeline-pipeline-pipeline-execution-started"
    ],
    "Resource": "arn:aws:codebuild:`us-east-2`:`123456789012`:`MyDemoPipeline`",
    "Targets": [
        {
            "TargetType": "SNS",
            "TargetAddress": "arn:aws:sns:`us-east-2`:`123456789012`:`codestar-notifications-MyNotificationTopic`"
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
