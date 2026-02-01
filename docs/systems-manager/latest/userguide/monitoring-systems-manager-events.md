• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Configuring EventBridge for Systems Manager

events

You can use Amazon EventBridge to perform a target event when supported AWS Systems Manager status
changes, state changes, or other conditions occur. You can create a rule that runs
whenever there is a state or status transition, or when there is a transition to one or
more states that are of interest.

The following procedure provides general steps for creating an EventBridge rule that engages
when a specified event is emitted by Systems Manager. For a list of procedures in this user guide
that address specific scenarios, see **More info** at the
end of this topic.

###### Note

When a service in your AWS account emits an event, it always goes to your
account’s default event bus. To write a rule that responds to events from
AWS services in your account, associate it with the default event bus. You can
create a rule on a custom event bus that looks for events from AWS services, but
this rule only engages when you receive such an event from another account through
cross-account event delivery. For more information, see [Sending and receiving
Amazon EventBridge events between AWS accounts](../../../eventbridge/latest/userguide/eb-cross-account.md "../../../eventbridge/latest/userguide/eb-cross-account.md") in the
_Amazon EventBridge User Guide_.

###### To configure EventBridge for Systems Manager events

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same AWS Region and
on the same event bus. 5. For **Event bus**, choose the event bus that you want to
associate with this rule. If you want this rule to respond to matching events
that come from your own AWS account, select **default**. When
an AWS service in your account emits an event, it always goes to your
account’s default event bus. 6. For **Rule type**, choose **Rule with an event
pattern**. 7. Choose **Next**. 8. For **Event source**, choose **AWS events or EventBridge
partner events**. 9. In the **Event pattern** section, choose **Event
pattern form**. 10. For **Event source**, choose **AWS
services**. 11. For **AWS service**, choose
**Systems Manager**. 12. For **Event type**, do one of the following:

    * Choose **All Events**.


    If you choose **All Events**, all events emitted by
     Systems Manager will match the rule. Be aware that this option can result in many
     event target actions.
    * Choose the type of Systems Manager event to use for this rule. EventBridge supports
     events from the following AWS Systems Manager tools:




    	+ Automation
    	+ Change Calendar
    	+ Compliance
    	+ Inventory
    	+ Maintenance Windows
    	+ Parameter Store
    	+ Run Command
    	+ State Manager
    ###### Note

    For Systems Manager actions that aren't supported by EventBridge, you can choose an
     AWS API call through CloudTrail to create an event rule that is based on
     an API call, which are recorded by CloudTrail. For an example, see [Monitoring session
     activity using Amazon EventBridge (console)](session-manager-auditing.md#session-manager-auditing-eventbridge-events "session-manager-auditing.md#session-manager-auditing-eventbridge-events").

13. (Optional) To make the rule more specific, add filter values. For example, if
    you chose **State Manager** and want to limit the rule to the state
    of a single managed instance that is targeted by an Association, for
    **Specific type(s)**, choose **EC2 State Manager
    Instance Association State Change**.

For complete details about supported detail types, see [Reference: Amazon EventBridge event patterns and types
for Systems Manager](reference-eventbridge-events.md "reference-eventbridge-events.md").

Some detail types have other supported options such as status. The available
options depend on the tool you selected. 14. Choose **Next**. 15. For **Target types**, choose **AWS
service**. 16. For **Select a target**, choose a target such as
an Amazon SNS topic or AWS Lambda function. The target is triggered when an event is
received that matches the event pattern defined in the rule. 17. For many target types, EventBridge needs permissions to send events to the target. In
these cases, EventBridge can create the AWS Identity and Access Management (IAM) role needed for your rule to
run:

    * To create an IAM role automatically, choose **Create a new
     role for this specific resource**.
    * To use an IAM role that you created earlier, choose **Use
     existing role**.

18. (Optional) Choose **Add another target** to add another
    target for this rule.
19. Choose **Next**.
20. (Optional) Enter one or more tags for the rule. For more information, see
    [Amazon EventBridge tags](../../../eventbridge/latest/userguide/eb-tagging.md "../../../eventbridge/latest/userguide/eb-tagging.md") in
    the _Amazon EventBridge User Guide_.
21. Choose **Next**.
22. Review the details of the rule and choose **Create
    rule**.

**More info**

- [Creating an EventBridge event that uses a
  runbook (console)](running-automations-event-bridge.md#automation-cwe-target-console "running-automations-event-bridge.md#automation-cwe-target-console")
- [Passing data to
  Automation using input transformers](automation-tutorial-eventbridge-input-transformers.md "automation-tutorial-eventbridge-input-transformers.md")
- [Remediating compliance issues using EventBridge](compliance-fixing.md "compliance-fixing.md")
- [Viewing inventory delete actions
  in EventBridge](inventory-custom.md#delete-custom-inventory-cwe "inventory-custom.md#delete-custom-inventory-cwe")
- [Configure EventBridge rules to
  create OpsItems](OpsCenter-automatically-create-OpsItems-2.md "OpsCenter-automatically-create-OpsItems-2.md")
- [Configuring EventBridge rules for parameters
  and parameter policies](sysman-paramstore-cwe.md#cwe-parameter-changes "sysman-paramstore-cwe.md#cwe-parameter-changes")
