# Create a notification rule for a

pipeline

You can create notification rules to send notifications about the events on your
pipeline that are important to you. The following steps show you how to set up a
notification rule on a single pipeline event. These steps are written with the
assumption that you have a pipeline configured in your AWS account.

1. Open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
2. Choose a pipeline from the list and open it.
3. Choose **Notify**, and then choose **Create
   notification rule**. You can also choose
   **Settings**, and then choose **Create notification
   rule**.
4. In **Notification name**, enter a name for the rule.
5. In **Detail type**, choose **Basic** if you
   want only the information provided to Amazon EventBridge included in the notification.
   Choose **Full** if you want to include information provided to
   Amazon EventBridge and information that might be supplied by the resource service or the
   notification manager.

For more information, see [Understanding notification contents and
security](security.md#security-notifications "security.md#security-notifications"). 6. In **Events that trigger notifications**, under
**Action execution**, select
**Started**. 7. In **Targets**, choose **Create SNS
topic**.

###### Note

When you create the topic as part of creating the notification rule, the
policy that allows CodePipeline to publish events to the topic is applied for you.
Using a topic created for notification rules helps ensure that you subscribe
only those users you want to receive notifications about this
pipeline.

After the **codestar-notifications-** prefix,enter a name for
the topic, and then choose **Submit**.

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
security](security.md#security-notifications "security.md#security-notifications"). 8. Choose **Submit**, and then review the notification
rule. 9. Subscribe your email address to the Amazon SNS topic you just created. For more
information, see [To subscribe users to an Amazon SNS topic used for
notifications](subscribe-users-sns.md#set-up-sns-subscribe "subscribe-users-sns.md#set-up-sns-subscribe"). 10. Navigate to your pipeline, and then choose **Release
change**. 11. When the action starts, the notification rule sends a notification to all
topic subscribers with information about the event.
