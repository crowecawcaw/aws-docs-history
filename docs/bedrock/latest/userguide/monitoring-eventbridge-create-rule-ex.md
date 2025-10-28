# [Example] Create a rule to handle Amazon Bedrock state change

events

The example in this topic demonstrates how to set up notification of Amazon Bedrock state change events by guiding you through configuring an Amazon Simple Notification Service topic, subscribing to the topic, and creating a rule in Amazon EventBridge to notify you of an Amazon Bedrock state change through the topic. Carry out the following procedure:

1. To create a topic, follow the steps at [Creating an Amazon SNS topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") in the Amazon Simple Notification Service Developer Guide.
2. To subscribe to the topic that you created, follow the steps at [Creating a subscription to an Amazon SNS topic](../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md") in the Amazon Simple Notification Service Developer Guide or send a [Subscribe](../../../sns/latest/api/API_Subscribe.md "../../../sns/latest/api/API_Subscribe.md") request with an [Amazon SNS endpoint](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md") and specify the Amazon Resource Name (ARN) of the topic you created.
3. To create a rule to notify you when the state of a job in Amazon Bedrock has changed, follow the steps at [Creating rules that react to events in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md"), while considering the following specific actions for this example:
   - Choose to define the rule detail with an event pattern.
   - When you build the event pattern, you can do the following:
     - View a sample event in the **Sample event** section by selecting any of the Amazon Bedrock **Sample events** to understand the fields from an Amazon Bedrock event that you can use when defining the pattern. You can also see the sample events in [How EventBridge for Amazon Bedrock works](monitoring-eventbridge-how-it-works.md "monitoring-eventbridge-how-it-works.md").
     - Get started by selecting **Use pattern from** in the **Creation method** section and then choosing Amazon Bedrock as the **AWS service** and the **Event type** that you want to capture. To learn how to define an event pattern, see [Amazon EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md").

   - As an example, you can use the following event pattern to capture when a batch inference job has completed:

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

4. After creating the rule, you will be notified through Amazon SNS when a batch inference job has completed.
