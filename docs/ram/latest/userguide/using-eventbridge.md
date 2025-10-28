# Monitoring AWS RAM using EventBridge

Using Amazon EventBridge, you can set up automatic notifications for specific events in AWS RAM.
Events from AWS RAM are delivered to EventBridge in near-real time. You can configure EventBridge to
monitor events and invoke targets in response to events that indicate changes to your resource shares.
Changes to a resource share trigger events for both the owner of the resource share and the
principals that were granted access to the resource share.

When you create an event pattern, the source is `aws.ram`.

###### Note

Take care writing code that depends on these events. These events are not guaranteed,
but are emitted on a best effort basis. If an error occurs when AWS RAM attempts to emit
an event, the service tries several more times. However, it can time out and result in
the loss of that specific event.

For more information, see the Amazon EventBridge User Guide.

## Example: Alerting on resource

share failures

Consider the scenario where you want to share Amazon EC2 capacity reservations with other
accounts in your organization. Doing this is a good way to reduce your costs.

However, if you don't meet all of the [prerequisites for sharing a capacity reservation](../../../AWSEC2/latest/UserGuide/capacity-reservation-sharing.md#sharing-cr-prereq "../../../AWSEC2/latest/UserGuide/capacity-reservation-sharing.md#sharing-cr-prereq"), then it can silently fail
performing the asynchronous tasks involved in sharing resources. If the share operation
fails, and your users in other accounts attempt to launch instances with one of those
capacity reservations, then Amazon EC2 acts as if the capacity reservation was full and
launches the instance as an on-demand instance instead. This can result in higher than
expected costs.

To monitor for resource share failures, set up an Amazon EventBridge rule that alerts you
whenever an AWS RAM resource share fails. The following tutorial procedure uses an
Amazon Simple Notification Service (SNS) topic to notify all topic subscribers whenever EventBridge discovers a resource
sharing failure. For more information about Amazon SNS, see the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").

###### To create a rule that notifies you when resource sharing fails

1. Open the [Amazon EventBridge console](https://console.aws.amazon.com/events "https://console.aws.amazon.com/events").
2. In the navigation pane, choose **Rules**, and then in the
   **Rules** list, choose **Create
   rule**.
3. Enter a name and optional description for your rule, then choose
   **Next**.
4. Scroll down to the **Event pattern** box, and choose
   **Custom patterns (JSON editor)**.
5. Copy and paste the following event pattern:

```
{
  "source": ["aws.ram"],
  "detail-type": ["Resource Sharing State Change"],
  "detail": {
    "event": ["Resource Share Association"],
    "status": ["failed"]
  }
}
```

6. Choose **Next**.
7. For **Target 1**, under **Target type**,
   choose **AWS service**.
8. Under **Select a target**, choose **SNS
   topic**.
9. For **Topic**, choose the SNS topic to which you want to
   publish the notification. This topic must already exist.
10. Choose **Next**, and then choose **Next**
    again to see to review your configuration.
11. When you're satisfied with your options, choose **Create
    rule**.
12. Back on the **Rules** page, ensure that your new rule is
    marked **Enabled**. If necessary, choose the radio button next
    to your rule name, and then choose **Enable**.

As long as that rule is enabled, any AWS RAM resource share that fails generates an SNS
alert to the recipients of the topic you published to.

You can also confirm that shared capacity reservations are accessible to the accounts
you shared them with by attempting to [view them in the Amazon EC2 console from those accounts](../../../AWSEC2/latest/UserGuide/capacity-reservation-sharing.md#identifying-shared-cr "../../../AWSEC2/latest/UserGuide/capacity-reservation-sharing.md#identifying-shared-cr").
