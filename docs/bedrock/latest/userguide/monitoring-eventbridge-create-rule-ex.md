# [Example] Create a rule to handle Amazon Bedrock state change events

This example shows how to set up notification of Amazon Bedrock state change events. You configure an Amazon Simple Notification Service topic, subscribe to the topic, and create a rule in Amazon EventBridge to notify you of state changes.

###### To create a rule to handle Amazon Bedrock state change events

1. Create an Amazon SNS topic. For instructions, see [Creating an Amazon SNS topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") in the Amazon Simple Notification Service Developer Guide.
2. Subscribe to the topic. For instructions, see [Creating a subscription to an Amazon SNS topic](../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md") in the Amazon Simple Notification Service Developer Guide. Alternatively, send a [Subscribe](../../../sns/latest/api/API_Subscribe.md "../../../sns/latest/api/API_Subscribe.md") request with an [Amazon SNS endpoint](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md") and specify the Amazon Resource Name (ARN) of the topic.
3. Create a rule to notify you when the state of a Amazon Bedrock job changes. Follow the steps at [Creating rules that react to events in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md"). Consider the following for this example:

   - Define the rule detail with an event pattern.
   - When you build the event pattern:

     - Select a Amazon Bedrock sample event in the **Sample event** section to see the fields you can use in your pattern. You can also see sample events in [How EventBridge for Amazon Bedrock works](monitoring-eventbridge-how-it-works.md "monitoring-eventbridge-how-it-works.md").
     - In the **Creation method** section, choose **Use pattern from**. Then choose Amazon Bedrock as the **AWS service** and the **Event type** to capture. To learn how to define an event pattern, see [Amazon EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md").

   - For example, use the following event pattern to capture when a batch inference job completes:

   ```
   {
    "source": ["aws.bedrock"],
    "detail-type": ["Batch Inference Job State Change"],
    "detail": {
     "status": ["Completed"]
    }
   }
   ```
   - Select **SNS topic** as the target and choose the topic that you created.

4. After you create the rule, Amazon SNS notifies you when a batch inference job completes.
