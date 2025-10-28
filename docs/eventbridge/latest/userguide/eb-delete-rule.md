# Disabling or deleting a rule in Amazon EventBridge

To stop a [rule](eb-rules.md "eb-rules.md") from processing [events](eb-events.md "eb-events.md")
or running on a schedule, you can delete or disable
the rule. The following steps walk you through how to delete or disable an EventBridge rule.

###### To delete or disable a rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.

Under **Event bus**, select the event bus that is associated
with the rule. 3. Do one of the following:

    1. To delete a rule, select the button next to the rule and choose
     **Actions**, **Delete**,
     **Delete**.


    If the rule is a managed rule, enter the name of the rule to acknowledge
     that it is a managed rule and that deleting it may stop functionality in the
     service that created the rule. To continue, enter the rule name and choose
     **Force delete**.
    2. To temporarily disable a rule, select the button next to the rule and
     choose **Disable**,
     **Disable**.


    You can't disable a managed rule.
