• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Remediating compliance issues using EventBridge

You can quickly remediate patch and association compliance issues by using Run Command, a
tool in AWS Systems Manager. You can target instance or AWS IoT Greengrass core device IDs or tags and run
the `AWS-RunPatchBaseline` document or the
`AWS-RefreshAssociation` document. If refreshing the association or
re-running the patch baseline fails to resolve the compliance issue, then you need to
investigate your associations, patch baselines, or instance configurations to understand
why the Run Command operations didn't resolve the problem.

For more information about patching, see [AWS Systems Manager Patch Manager](patch-manager.md "patch-manager.md") and [SSM Command document for
patching: AWS-RunPatchBaseline](patch-manager-aws-runpatchbaseline.md "patch-manager-aws-runpatchbaseline.md").

For more information about associations, see [Working with associations in Systems Manager](state-manager-associations.md "state-manager-associations.md").

For more information about running a command, see [AWS Systems Manager Run Command](run-command.md "run-command.md").

###### Specify Compliance as the target of an EventBridge event

You can also configure Amazon EventBridge to perform an action in response to Systems Manager
Compliance events. For example, if one or more managed nodes fail to install
Critical patch updates or run an association that installs anti-virus software, then
you can configure EventBridge to run the `AWS-RunPatchBaseline` document or the
`AWS-RefreshAssocation` document when the Compliance event occurs.

Use the following procedure to configure Compliance as the target of an EventBridge
event.

###### To configure Compliance as the target of a EventBridge event (console)

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
**Systems Manager**. 12. For **Event type**, choose **Configuration
Compliance**. 13. For **Specific detail type(s)**, choose
**Configuration Compliance State Change**. 14. Choose **Next**. 15. For **Target types**, choose **AWS
service**. 16. For **Select a target**, choose **Systems Manager
Run Command**. 17. In the **Document** list, choose a Systems Manager document (SSM
document) to run when your target is invoked. For example, choose
`AWS-RunPatchBaseline` for a non-compliant patch event, or choose
`AWS-RefreshAssociation` for a non-compliant association
event. 18. Specify information for the remaining fields and parameters.

###### Note

Required fields and parameters have an asterisk (\*) next to the name. To
create a target, you must specify a value for each required parameter or
field. If you don't, the system creates the rule, but the rule won't be
run. 19. Choose **Next**. 20. (Optional) Enter one or more tags for the rule. For more information, see
[Tagging Your
Amazon EventBridge Resources](../../../eventbridge/latest/userguide/eventbridge-tagging.md "../../../eventbridge/latest/userguide/eventbridge-tagging.md") in the
_Amazon EventBridge User Guide_. 21. Choose **Next**. 22. Review the details of the rule and choose **Create
rule**.
