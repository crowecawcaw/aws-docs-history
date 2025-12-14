# Security Hub CSPM controls for Step Functions

These AWS Security Hub CSPM controls evaluate the AWS Step Functions service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [StepFunctions.1] Step Functions state machines should have

logging turned on

**Related requirements:** PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::StepFunctions::StateMachine`

**AWS Config rule:**
[`step-functions-state-machine-logging-enabled`](../../../config/latest/developerguide/step-functions-state-machine-logging-enabled.md "../../../config/latest/developerguide/step-functions-state-machine-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter  | Description           | Type | Allowed custom values | Security Hub CSPM default value |
| ---------- | --------------------- | ---- | --------------------- | ------------------------------- |
| `logLevel` | Minimum logging level | Enum | `ALL, ERROR, FATAL`   | No default value                |

This controls checks whether an AWS Step Functions state machine has logging turned on. The control fails if a state machine
doesn't have logging turned on. If you provide a custom value for the `logLevel` parameter, the control passes
only if the state machine has the specified logging level turned on.

Monitoring helps you maintain the reliability, availability, and performance of Step Functions.
You should collect as much monitoring data from the AWS services that you use so you
can more easily debug multi-point failures. Having a logging configuration defined for
your Step Functions state machines allows for you to track execution history and results in
Amazon CloudWatch Logs. Optionally, you can track only errors or fatal events.

### Remediation

To turn on logging for a Step Functions state machine, see [Configure logging](../../../step-functions/latest/dg/cw-logs.md#monitoring-logging-configure "../../../step-functions/latest/dg/cw-logs.md#monitoring-logging-configure") in the _AWS Step Functions Developer Guide_.

## [StepFunctions.2] Step Functions activities should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::StepFunctions::Activity`

**AWS Config rule:**`tagged-stepfunctions-activity` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an AWS Step Functions activity has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the activity doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the activity isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to an Step Functions activity, see [Tagging in Step Functions](../../../step-functions/latest/dg/concepts-tagging.md "../../../step-functions/latest/dg/concepts-tagging.md") in the _AWS Step Functions Developer Guide_.
