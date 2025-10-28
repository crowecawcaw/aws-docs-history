# Security Hub controls for AWS CloudFormation

These Security Hub controls evaluate the AWS CloudFormation service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [CloudFormation.1] CloudFormation stacks should be integrated with Simple Notification Service (SNS)

###### Important

Security Hub retired this control in April 2024.
For more information, see [Change log for Security Hub CSPM controls](controls-change-log.md "controls-change-log.md").

**Related requirements:** NIST.800-53.r5 SI-4(12), NIST.800-53.r5 SI-4(5)

**Category:** Detect > Detection services > Application monitoring

**Severity:** Low

**Resource type:**
`AWS::CloudFormation::Stack`

**AWS Config rule:**
[`cloudformation-stack-notification-check`](../../../config/latest/developerguide/cloudformation-stack-notification-check.md "../../../config/latest/developerguide/cloudformation-stack-notification-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Simple Notification Service notification is integrated with an AWS CloudFormation
stack. The control fails for a CloudFormation stack if no SNS notification is associated with
it.

Configuring an SNS notification with your CloudFormation stack helps immediately notify stakeholders
of any events or changes occurring with the stack.

### Remediation

To integrate a CloudFormation stack and an SNS topic, see [Updating stacks directly](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.md")
in the _AWS CloudFormation User Guide_.

## [CloudFormation.2] CloudFormation stacks should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::CloudFormation::Stack`

**AWS Config rule:** `tagged-cloudformation-stack` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           | This control checks whether an AWS CloudFormation stack has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the stack doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the stack isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored. A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. ###### Note Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the _AWS General Reference_. ### Remediation To add tags to a CloudFormation stack, see [CreateStack](../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md "../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md") in the _AWS CloudFormation API Reference_. |
