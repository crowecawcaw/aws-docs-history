

# [Example] Create a rule to handle Amazon Bedrock state change events
<a name="monitoring-eventbridge-create-rule-ex"></a>

This example shows how to set up notification of Amazon Bedrock state change events. You configure an Amazon Simple Notification Service topic, subscribe to the topic, and create a rule in Amazon EventBridge to notify you of state changes.

**To create a rule to handle Amazon Bedrock state change events**

1. Create an Amazon SNS topic. For instructions, see [Creating an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html) in the Amazon Simple Notification Service Developer Guide.

1. Subscribe to the topic. For instructions, see [Creating a subscription to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html) in the Amazon Simple Notification Service Developer Guide. Alternatively, send a [Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html) request with an [Amazon SNS endpoint](https://docs.aws.amazon.com/general/latest/gr/sns.html) and specify the Amazon Resource Name (ARN) of the topic.

1. Create a rule to notify you when the state of a Amazon Bedrock job changes. Follow the steps at [Creating rules that react to events in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html). Consider the following for this example:
   + Define the rule detail with an event pattern.
   + When you build the event pattern:
     + Select a Amazon Bedrock sample event in the **Sample event** section to see the fields you can use in your pattern. You can also see sample events in [How EventBridge for Amazon Bedrock works](monitoring-eventbridge-how-it-works.md).
     + In the **Creation method** section, choose **Use pattern from**. Then choose Amazon Bedrock as the **AWS service** and the **Event type** to capture. To learn how to define an event pattern, see [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html).
   + For example, use the following event pattern to capture when a batch inference job completes:

     ```
     {
      "source": ["aws.bedrock"],
      "detail-type": ["Batch Inference Job State Change"],
      "detail": {
       "status": ["Completed"]
      }
     }
     ```
   + Select **SNS topic** as the target and choose the topic that you created.

1. After you create the rule, Amazon SNS notifies you when a batch inference job completes.