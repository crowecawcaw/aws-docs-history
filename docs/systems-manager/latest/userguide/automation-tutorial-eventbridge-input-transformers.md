AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Passing data to

Automation using input transformers

This AWS Systems Manager Automation tutorial shows how to use the input transformer feature
of Amazon EventBridge to extract the `instance-id` of an Amazon Elastic Compute Cloud (Amazon EC2) instance
from an instance state change event. Automation is a tool in AWS Systems Manager. We use the
input transformer to pass that data to the `AWS-CreateImage` runbook
target as the `InstanceId` input parameter. The rule is triggered when
any instance changes to the `stopped` state.

For more information about working with input transformers, see [Tutorial: Use Input Transformer to Customize What is Passed to the Event
Target](../../../eventbridge/latest/userguide/eventbridge-input-transformer-tutorial.md "../../../eventbridge/latest/userguide/eventbridge-input-transformer-tutorial.md") in the _Amazon EventBridge User Guide_.

###### Before you begin

Verify that you added the required permissions and trust policy for EventBridge to
your Systems Manager Automation service role. For more information, see [Overview of Managing Access Permissions to Your EventBridge Resources](../../../eventbridge/latest/userguide/iam-access-control-identity-based-eventbridge.md "../../../eventbridge/latest/userguide/iam-access-control-identity-based-eventbridge.md") in
the _Amazon EventBridge User Guide_.

###### To use input transformers with Automation

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same Region and on
the same event bus. 5. For **Event bus**, choose the event bus that you want to
associate with this rule. If you want this rule to respond to matching
events that come from your own AWS account, select
**default**. When an AWS service in your account
emits an event, it always goes to your account’s default event bus. 6. For **Rule type**, choose **Rule with an event
pattern**. 7. Choose **Next**. 8. For **Event source**, choose **AWS events or
EventBridge partner events**. 9. In the **Event pattern** section, choose **Use
pattern form**. 10. For **Event source**, choose **AWS
services**. 11. For **AWS service**, choose
**EC2**. 12. For **Event type**, choose **EC2 Instance
State-change Notification**. 13. For **Event Type Specification 1**, select
**Specific state(s)**, and then choose
**stopped**. 14. For **Event Type Specification 2**, select **Any
instance**, or select **Specific instance
Id(s)** and enter the IDs of the instances to monitor. 15. Choose **Next**. 16. For **Target types**, choose **AWS
service**. 17. For **Select a target**, choose **Systems Manager
Automation**. 18. For **Document**, choose
**AWS-CreateImage**. 19. In the **Configure automation parameter(s)** section,
choose **Input Transformer**. 20. For **Input path**, enter
`{"instance":"$.detail.instance-id"}`. 21. For **Template**, enter
`{"InstanceId":[<instance>]}`. 22. For **Execution role**, choose **Use existing
role** and choose your Automation service role. 23. Choose **Next**. 24. (Optional) Enter one or more tags for the rule. For more information, see
[Tagging Your
Amazon EventBridge Resources](../../../eventbridge/latest/userguide/eventbridge-tagging.md "../../../eventbridge/latest/userguide/eventbridge-tagging.md") in the
_Amazon EventBridge User Guide_. 25. Choose **Next**. 26. Review the details of the rule and choose **Create
rule**.
