

# Tutorial: Register an event rule
<a name="service_sns_reg_rule"></a>

 Next, register an event rule that captures only `Membership Updated` events. 

**To register your EventBridge rule**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the navigation pane, choose **Rules**.

1. Choose **Create rule**.

1. Enter a name and description for the rule.
**Note**  
A rule can't have the same name as another rule in the same Region and on the same event bus.

1. For **Event bus**, choose the event bus that you want to associate with this rule. If you want this rule to match events that come from your account, select **AWS default event bus**. When an AWS service in your account emits an event, it always goes to your account's default event bus.
**Note**  
This should be setup in your AWS Organizations or delegated administrator account you created the AWS Security Incident Response membership in.

1. For **Rule type**, choose **Rule with an event pattern**.

1. Choose **Next**.

1. For **Event source**, choose **Other**.

1. For **Event pattern**, select **Custom patterns (JSON editor)**.

1. Paste the following event pattern into the text area.

   ```
                     {
                       "source": ["aws.security-ir"],
                       "detail-type": ["Membership Updated"]
                     }
   ```

   This code defines an EventBridge rule that matches any event where your service membership is updated or modified. For more information about event patterns, see [Events and Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html) in the *Amazon EventBridge User Guide*.

1. Choose **Next**.

1. For **Target types**, choose **AWS service**.

1. For **Select a target**, choose **SNS topic**, and for **Topic**, choose **MembershipUpdated**.

1. (Optional) For **Additional settings**, do the following:

   1. For **Maximum age of event**, enter a value between one minute (00:01) and 24 hours (24:00).

   1. For **Retry attempts**, enter a number between 0 and 185.

   1. For **Dead-letter queue**, choose whether to use a standard Amazon SQS queue as a dead-letter queue. EventBridge sends events that match this rule to the dead-letter queue if they are not successfully delivered to the target. Do one of the following:
      + Choose **None** to not use a dead-letter queue.
      + Choose **Select an Amazon SQS queue in the current AWS account to use as the dead-letter queue** and then select the queue to use from the dropdown.
      + Choose **Select an Amazon SQS queue in an other AWS account as a dead-letter queue** and then enter the ARN of the queue to use. You must attach a resource-based policy to the queue that grants EventBridge permission to send messages to it. For more information, see [Granting permissions to the dead-letter queue](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-dlq.html#eb-dlq-perms) in the *Amazon EventBridge User Guide*.

1. Choose **Next**.

1. (Optional) Enter one or more tags for the rule. For more information, see [Amazon EventBridge tags](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tagging.html) in the *Amazon EventBridge User Guide*.

1. Choose **Next**.

1. Review the details of the rule and choose **Create rule**.