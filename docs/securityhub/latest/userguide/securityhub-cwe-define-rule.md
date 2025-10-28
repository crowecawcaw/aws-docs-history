# Defining a rule in EventBridge

To trigger a custom action in Amazon EventBridge, you must create a corresponding rule in EventBridge. The
rule definition includes the Amazon Resource Name (ARN) of the custom action.

The event pattern for a **Security Hub Findings - Custom
Action** event has the following format:

```
{
  "source": [
    "aws.securityhub"
  ],
  "detail-type": [
    "Security Hub Findings - Custom Action"
  ],
  "resources": [ "`<custom action ARN>`" ]
}
```

The event pattern for a **Security Hub Insight Results**
event has the following format:

```
{
  "source": [
    "aws.securityhub"
  ],
  "detail-type": [
    "Security Hub Insight Results"
  ],
  "resources": [ "`<custom action ARN>`" ]
}
```

In both patterns, `<custom action ARN>`
is the ARN of a custom action. You can configure a rule that applies to more than
one custom action.

The instructions provided here are for the EventBridge console. When you use the console,
EventBridge automatically creates the required resource-based policy that enables EventBridge to
write to CloudWatch Logs.

You can also use the [`PutRule`](../../../eventbridge/latest/APIReference/API_PutRule.md "../../../eventbridge/latest/APIReference/API_PutRule.md") API operation of the EventBridge API. However, if you use
the EventBridge API, then you must create the resource-based policy. For details on the
required policy, see [CloudWatch Logs permissions](../../../eventbridge/latest/userguide/resource-based-policies-eventbridge.md#cloudwatchlogs-permissions "../../../eventbridge/latest/userguide/resource-based-policies-eventbridge.md#cloudwatchlogs-permissions") in the _Amazon EventBridge User Guide_.

###### To define a rule in EventBridge (EventBridge console)

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule.
5. For **Event bus**, choose the event bus that you want to
   associate with this rule. If you want this rule to match events that come
   from your account, select **default**. When an AWS
   service in your account emits an event, it always goes to your account’s
   default event bus.
6. For **Rule type**, choose **Rule with an event
   pattern**.
7. Choose **Next**.
8. For **Event source**, choose **AWS
   events**.
9. For **Event pattern**, choose **Event pattern
   form**.
10. For **Event source**, choose **AWS
    services**.
11. For **AWS service**, choose
    **Security Hub**.
12. For **Event type**, do one of the following:
    - To create a rule to apply when you send findings to a custom
      action, choose **Security Hub Findings - Custom
      Action**.
    - To create a rule to apply when you send insight results to a
      custom action, choose **Security Hub Insight
      Results**.

13. Choose **Specific custom action ARNs**, add a custom
    action ARN.

If the rule applies to multiple custom actions, choose
**Add** to add more custom action ARNs. 14. Choose **Next**. 15. Under **Select targets**, choose and configure the target
to invoke when this rule is matched. 16. Choose **Next**. 17. (Optional) Enter one or more tags for the rule. For more information, see
[Amazon EventBridge tags](../../../eventbridge/latest/userguide/eb-tagging.md "../../../eventbridge/latest/userguide/eb-tagging.md")
in the _Amazon EventBridge User Guide_. 18. Choose **Next**. 19. Review the details of the rule and choose **Create
rule**.

When you perform a custom action on findings or insight results in your
account, events are generated in EventBridge.
