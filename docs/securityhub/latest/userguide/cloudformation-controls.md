

# Security Hub CSPM controls for CloudFormation
<a name="cloudformation-controls"></a>

These Security Hub CSPM controls evaluate the AWS CloudFormation service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [CloudFormation.1] CloudFormation stacks should be integrated with Simple Notification Service (SNS)
<a name="cloudformation-1"></a>

**Important**  
Security Hub CSPM retired this control in April 2024. For more information, see [Change log for Security Hub CSPM controls](controls-change-log.md).

**Related requirements:** NIST.800-53.r5 SI-4(12), NIST.800-53.r5 SI-4(5)

**Category:** Detect > Detection services > Application monitoring

**Severity:** Low

**Resource type:** `AWS::CloudFormation::Stack`

**AWS Config rule:** [`cloudformation-stack-notification-check`](https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-notification-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Simple Notification Service notification is integrated with an CloudFormation stack. The control fails for a CloudFormation stack if no SNS notification is associated with it.

Configuring an SNS notification with your CloudFormation stack helps immediately notify stakeholders of any events or changes occurring with the stack.

### Remediation
<a name="cloudformation-1-remediation"></a>

To integrate a CloudFormation stack and an SNS topic, see [Updating stacks directly](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.html) in the *AWS CloudFormation User Guide*.

## [CloudFormation.2] CloudFormation stacks should be tagged
<a name="cloudformation-2"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::CloudFormation::Stack`

**AWS Config rule:** `tagged-cloudformation-stack` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  | No default value  | 

This control checks whether an AWS CloudFormation stack has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the stack doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the stack isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="cloudformation-2-remediation"></a>

To add tags to a CloudFormation stack, see [CreateStack](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html) in the *AWS CloudFormation API Reference*.

## [CloudFormation.3] CloudFormation stacks should have termination protection enabled
<a name="cloudformation-3"></a>

**Category:** Protect > Data Protection > Data deletion protection

**Severity:** Medium

**Resource type:** `AWS::CloudFormation::Stack`

**AWS Config rule:** [cloudformation-termination-protection-check](https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-termination-protection-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS CloudFormation stack has termination protection enabled. The control fails if termination protection is not enabled on a CloudFormation stack.

CloudFormation helps to manage related resources as a single unit called a Stack. You can prevent a stack from being accidentally deleted by enabling termination protection on the stack. If a user attempts to delete a stack with termination protection enabled, the deletion fails and the stack, including its status, remains unchanged. You can set termination protection on a stack with any status except `DELETE_IN_PROGRESS` or `DELETE_COMPLETE`. 

**Note**  
Enabling or disabling termination protection on a stack passes the same choice on to any nested stacks belonging to that stack as well. You can't enable or disable termination protection directly on a nested stack. You can't directly delete a nested stack belonging with a stack that has termination protection enabled. If NESTED is displayed next to the stack name, the stack is a nested stack. You can only change termination protection on the root stack to which the nested stack belongs. 

### Remediation
<a name="cloudformation-3-remediation"></a>

To enable termination protection on a CloudFormation stack, see [Protect CloudFormation stacks from being deleted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html) in the *AWS CloudFormation User Guide*.

## [CloudFormation.4] CloudFormation stacks should have associated service roles
<a name="cloudformation-4"></a>

**Category:** Detect > Secure access management

**Severity:** Medium

**Resource type:** `AWS::CloudFormation::Stack`

**AWS Config rule:** [cloudformation-stack-service-role-check](https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-service-role-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS CloudFormation stack has a service role associated with it. The control fails for a CloudFormation stack if no service role is associated with it.

Service-managed StackSets use execution roles through AWS Organizations trusted access integration. The control also generates a FAILED finding for an AWS CloudFormation stack created by service-managed StackSets because there is no service role associated with it. Due to how service-managed StackSets authenticate, the `roleARN` field cannot be populated for these stacks.

Using service roles with CloudFormation stacks helps implement least privilege access by separating permissions between the user who creates/updates stacks and the permissions needed by CloudFormation to create/update resources. This reduces the risk of privilege escalation and helps maintain security boundaries between different operational roles.

**Note**  
It is not possible to remove a service role attached to a stack after the stack is created. Other users that have permissions to perform operations on this stack are able to use this role, regardless of whether those users have the `iam:PassRole` permission or not. If the role includes permissions that the user shouldn't have, you can unintentionally escalate a user's permissions. Ensure that the role grants least privilege.

### Remediation
<a name="cloudformation-4-remediation"></a>

To associate a service role with a CloudFormation stack, see [CloudFormation service role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html) in the *AWS CloudFormation User Guide*.