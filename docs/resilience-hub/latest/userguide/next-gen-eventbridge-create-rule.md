# Creating an EventBridge rule for events from the next generation of Resilience Hub

With EventBridge, you can create rules that define actions to take when the next generation of Resilience Hub emits
events for your services.

Next generation Resilience Hub emits all events with the source `aws.resiliencehub`.
Your event pattern must include this source to match events from the next generation of Resilience Hub. You can further
filter by `detail-type` to match specific event types.

To enter or paste an event pattern into the EventBridge console, choose the
**Enter my own** option. To help you determine event patterns
that might be useful, this topic includes
[Example event patterns and events](next-gen-eventbridge-examples.md "next-gen-eventbridge-examples.md").

###### To create a rule for an event from the next generation of Resilience Hub

1. Open the EventBridge console at
   [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. For the AWS Region, choose the Region where your service in the next generation of Resilience Hub is
   deployed.
3. Choose **Create rule**.
4. Enter a **Name** for the rule, and, optionally, a
   description.
5. For **Event bus**, leave the default value,
   **default**.
6. Choose **Next**.
7. For **Event source**, leave the default value,
   **AWS events**.
8. Under **Event pattern**, choose
   **Enter my own**.
9. Enter or paste an event pattern that includes
   `"source": ["aws.resiliencehub"]` and the
   `detail-type` you want to match. For examples, see
   [Example event patterns and events](next-gen-eventbridge-examples.md "next-gen-eventbridge-examples.md").
10. Choose **Next** and configure your target (for example,
    an Amazon SNS topic, Lambda function, or CloudWatch log group).
11. Complete the rule creation workflow by choosing
    **Create rule**.
