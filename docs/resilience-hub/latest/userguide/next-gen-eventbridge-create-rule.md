

# Creating an EventBridge rule for events from the next generation of Resilience Hub
<a name="next-gen-eventbridge-create-rule"></a>

With EventBridge, you can create rules that define actions to take when the next generation of Resilience Hub emits events for your services.

Next generation Resilience Hub emits all events with the source `aws.resiliencehub`. Your event pattern must include this source to match events from the next generation of Resilience Hub. You can further filter by `detail-type` to match specific event types.

To enter or paste an event pattern into the EventBridge console, choose the **Enter my own** option. To help you determine event patterns that might be useful, this topic includes [Example event patterns and events](next-gen-eventbridge-examples.md).

**To create a rule for an event from the next generation of Resilience Hub**

1. Open the EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. For the AWS Region, choose the Region where your service in the next generation of Resilience Hub is deployed.

1. Choose **Create rule**.

1. Enter a **Name** for the rule, and, optionally, a description.

1. For **Event bus**, leave the default value, **default**.

1. Choose **Next**.

1. For **Event source**, leave the default value, **AWS events**.

1. Under **Event pattern**, choose **Enter my own**.

1. Enter or paste an event pattern that includes `"source": ["aws.resiliencehub"]` and the `detail-type` you want to match. For examples, see [Example event patterns and events](next-gen-eventbridge-examples.md).

1. Choose **Next** and configure your target (for example, an Amazon SNS topic, Lambda function, or CloudWatch log group).

1. Complete the rule creation workflow by choosing **Create rule**.