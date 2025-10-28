# Tutorial: Register the event rule

In this section, you create an EventBridge event rule that captures job events that are coming
from your AWS Batch resources. This rule captures all events coming from AWS Batch within the
account where it's defined. The job messages themselves contain information about the event
source, including the job queue where it was submitted. You can use this information to filter
and sort events programmatically.

###### Note

If you use the AWS Management Console to create an event rule, the console automatically adds the IAM permissions for
EventBridge to call your Lambda function. However, if you're creating an event rule using the AWS CLI, you must grant
permissions explicitly. For more information, see [Events and Event Patterns](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") in the _Amazon EventBridge User
Guide_.

###### To create your EventBridge rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same Region and on the same event bus. 5. For **Event bus**, choose the event bus that you want to associate with this rule. If you
want this rule to match events that come from your account, select **AWS default event bus**.
When an AWS service in your account emits an event, it always goes to your account's default event bus. 6. For **Rule type**, choose **Rule with an event
pattern**. 7. Choose **Next**. 8. For **Event source**, choose **Other**. 9. For **Event pattern**, select **Custom patterns (JSON
editor)**. 10. Paste the following event pattern into the text area.

```
{
  "source": [
    "aws.batch"
  ]
}
```

This rule applies across all of your AWS Batch groups and to every AWS Batch event. Alternatively, you can create
a more specific rule to filter out some results. 11. Choose **Next**. 12. For **Target types**, choose **AWS service**. 13. For **Select a target**, choose **Lambda function**,
and select your Lambda function. 14. (Optional) For **Additional settings**, do the following:

    1. For **Maximum age of event**, enter a value between one minute (00:01)
     and 24 hours (24:00).
    2. For **Retry attempts**, enter a number between 0 and 185.
    3. For **Dead-letter queue**, choose whether to use a standard Amazon SQS
     queue as a dead-letter queue. EventBridge sends events that match this rule to the dead-letter
     queue if they are not successfully delivered to the target. Do one of the following:


    	* Choose **None** to not use a dead-letter queue.
    	* Choose **Select an Amazon SQS queue in the current AWS account to use as the
    	 dead-letter queue** and then select the queue to use from the dropdown.
    	* Choose **Select an Amazon SQS queue in an other AWS account as a dead-letter
    	 queue** and then enter the ARN of the queue to use. You must attach a
    	 resource-based policy to the queue that grants EventBridge permission to send messages to it. For
    	 more information, see [Granting permissions to
    	 the dead-letter queue](../../../eventbridge/latest/userguide/eb-rule-dlq.md#eb-dlq-perms "../../../eventbridge/latest/userguide/eb-rule-dlq.md#eb-dlq-perms") in the *Amazon EventBridge User Guide*.

15. Choose **Next**.
16. (Optional) Enter one or more tags for the rule. For more information, see [Amazon EventBridge tags](../../../eventbridge/latest/userguide/eb-tagging.md "../../../eventbridge/latest/userguide/eb-tagging.md")
    in the _Amazon EventBridge User Guide_.
17. Choose **Next**.
18. Review the details of the rule and choose **Create rule**.
