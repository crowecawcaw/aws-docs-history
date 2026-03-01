# AWS managed policies for AWS CloudFormation

An AWS managed policy is a standalone policy that is created and administered by AWS.
AWS managed policies are designed to provide permissions for many common use cases so that
you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for
your specific use cases because they're available for all AWS customers to use. We
recommend that you reduce permissions further by defining [customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the
permissions defined in an AWS managed policy, the update affects all principal identities
(users, groups, and roles) that the policy is attached to. AWS is most likely to update an
AWS managed policy when a new AWS service is launched or new API operations become
available for existing services.

For more information, see [AWS
managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

## AWS managed policy: AWSCloudFormationFullAccess

You can attach `AWSCloudFormationFullAccess` to your users, groups, and
roles.

This policy grants permissions that allow full access to CloudFormation actions and
resources.

**Permissions details**

This policy includes the following permissions.

- `cloudformation` – Allows principals to perform all
  CloudFormation actions on all resources.

To view the permissions for this policy, see [AWSCloudFormationFullAccess](../../../aws-managed-policy/latest/reference/AWSCloudFormationFullAccess.md "../../../aws-managed-policy/latest/reference/AWSCloudFormationFullAccess.md") in the _AWS Managed Policy Reference
Guide_.

## AWS managed policy: AWSCloudFormationReadOnlyAccess

You can attach `AWSCloudFormationReadOnlyAccess` to your users, groups, and
roles.

This policy grants permissions that allow read-only access to CloudFormation resources and
actions.

**Permissions details**

This policy includes the following permissions.

- `cloudformation` – Allows principals to perform read-only
  CloudFormation actions such as describing stacks, listing resources, and viewing
  templates, but does not allow creating, updating, or deleting stacks.

To view the permissions for this policy, see [AWSCloudFormationReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSCloudFormationReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSCloudFormationReadOnlyAccess.md") in the _AWS Managed Policy Reference
Guide_.

## CloudFormation updates to AWS managed policies

View details about updates to AWS managed policies for CloudFormation since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the CloudFormation Document history page.

| Change                                                                                                                                                                                 | Description                                                                                                                                                               | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSCloudFormationReadOnlyAccess](#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess "#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess") – Update to an existing<br>policy | CloudFormation added new permissions to allow<br>`cloudformation:BatchDescribe*` actions for batch describe<br>operations.                                                | January 30, 2026  |
| [AWSCloudFormationReadOnlyAccess](#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess "#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess") – Update to an existing<br>policy | CloudFormation added new permissions to allow<br>`cloudformation:Detect*` actions for stack drift detection<br>capabilities.                                              | November 13, 2019 |
| [AWSCloudFormationReadOnlyAccess](#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess "#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess") – Update to an existing<br>policy | CloudFormation added new permissions to allow<br>`cloudformation:EstimateTemplateCost`,<br>`cloudformation:Get*`, and<br>`cloudformation:ValidateTemplate` actions.       | November 2, 2017  |
| [AWSCloudFormationFullAccess](#security-iam-awsmanpol-AWSCloudFormationFullAccess "#security-iam-awsmanpol-AWSCloudFormationFullAccess") – New policy                                  | CloudFormation added a new AWS managed policy that provides full access to<br>CloudFormation actions and resources.                                                       | July 26, 2019     |
| [AWSCloudFormationReadOnlyAccess](#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess "#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess") – Update to an existing<br>policy | CloudFormation added new permissions to allow<br>`cloudformation:DetectStackDrift` and<br>`cloudformation:DetectStackResourceDrift` actions for stack<br>drift detection. | February 6, 2019  |
| [AWSCloudFormationReadOnlyAccess](#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess "#security-iam-awsmanpol-AWSCloudFormationReadOnlyAccess") – New policy                      | CloudFormation added a new AWS managed policy that provides read-only<br>access to CloudFormation actions and resources.                                                  | February 6, 2015  |
| CloudFormation started tracking changes                                                                                                                                                | CloudFormation started tracking changes for its AWS managed policies.                                                                                                     | February 6, 2015  |
