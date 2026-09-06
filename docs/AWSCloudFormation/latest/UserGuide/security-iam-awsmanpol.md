

# AWS managed policies for AWS CloudFormation
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: AWSCloudFormationFullAccess
<a name="security-iam-awsmanpol-AWSCloudFormationFullAccess"></a>

You can attach `AWSCloudFormationFullAccess` to your users, groups, and roles.

This policy grants permissions that allow full access to CloudFormation actions and resources.

**Permissions details**

This policy includes the following permissions.
+ `cloudformation` – Allows principals to perform all CloudFormation actions on all resources.

To view the permissions for this policy, see [AWSCloudFormationFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudFormationFullAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSCloudFormationReadOnlyAccess
<a name="security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess"></a>

You can attach `AWSCloudFormationReadOnlyAccess` to your users, groups, and roles.

This policy grants permissions that allow read-only access to CloudFormation resources and actions.

**Permissions details**

This policy includes the following permissions.
+ `cloudformation` – Allows principals to perform read-only CloudFormation actions such as describing stacks, listing resources, and viewing templates, but does not allow creating, updating, or deleting stacks.

To view the permissions for this policy, see [AWSCloudFormationReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudFormationReadOnlyAccess.html) in the *AWS Managed Policy Reference Guide*.

## CloudFormation updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for CloudFormation since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the CloudFormation Document history page.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSCloudFormationReadOnlyAccess](#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess) – Update to an existing policy | CloudFormation added new permissions to allow `cloudformation:BatchDescribe*` actions for batch describe operations. | January 30, 2026 | 
| [AWSCloudFormationReadOnlyAccess](#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess) – Update to an existing policy | CloudFormation added new permissions to allow `cloudformation:Detect*` actions for stack drift detection capabilities. | November 13, 2019 | 
| [AWSCloudFormationReadOnlyAccess](#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess) – Update to an existing policy | CloudFormation added new permissions to allow `cloudformation:EstimateTemplateCost`, `cloudformation:Get*`, and `cloudformation:ValidateTemplate` actions. | November 2, 2017 | 
| [AWSCloudFormationFullAccess](#security-iam-awsmanpol-AWSCloudFormationFullAccess) – New policy | CloudFormation added a new AWS managed policy that provides full access to CloudFormation actions and resources. | July 26, 2019 | 
| [AWSCloudFormationReadOnlyAccess](#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess) – Update to an existing policy | CloudFormation added new permissions to allow `cloudformation:DetectStackDrift` and `cloudformation:DetectStackResourceDrift` actions for stack drift detection. | February 6, 2019 | 
| [AWSCloudFormationReadOnlyAccess](#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess) – New policy | CloudFormation added a new AWS managed policy that provides read-only access to CloudFormation actions and resources. | February 6, 2015 | 
| CloudFormation started tracking changes | CloudFormation started tracking changes for its AWS managed policies. | February 6, 2015 | 