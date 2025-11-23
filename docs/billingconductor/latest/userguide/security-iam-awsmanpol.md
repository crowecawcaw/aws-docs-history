# AWS managed policies for AWS Billing Conductor

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: AWSBillingConductorFullAccess

The AWSBillingConductorFullAccess managed policy grants complete access to AWS Billing Conductor console and APIs. Users can list, create, and delete AWS Billing Conductor resources.

To view the permissions for this policy, see [AWSBillingConductorFullAccess](../../../aws-managed-policy/latest/reference/AWSBillingConductorFullAccess.md "../../../aws-managed-policy/latest/reference/AWSBillingConductorFullAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSBillingConductorReadOnlyAccess

The AWSBillingConductorReadOnlyAccess managed policy grants read-only access to AWS Billing Conductor console and APIs. Users can view and list all AWS Billing Conductor resources. Users can't create or delete resources.

To view the permissions for this policy, see [AWSBillingConductorReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSBillingConductorReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSBillingConductorReadOnlyAccess.md") in the _AWS Managed Policy Reference_.

## AWS Billing Conductor updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Billing Conductor since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AWS Billing Conductor Document history page.

| Change                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                     | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSBillingConductorFullAccess](#security-iam-awsmanpol-fullaccess "#security-iam-awsmanpol-fullaccess")<br>• Update to existing policies | We added the `organizations:DescribeResponsibilityTransfer` and `organizations:ListInboundResponsibilityTransfers` actions to the `AWSBillingConductorFullAccess` policy.                                                                                                                                                                                       | November 19, 2025 |
| [AWSBillingConductorFullAccess](#security-iam-awsmanpol-fullaccess "#security-iam-awsmanpol-fullaccess")<br>• Update to existing policies | We added the following actions to the `AWSBillingConductorFullAccess` policy:<br>• `organizations:ListRoots`<br>• `organizations:ListOrganizationalUnitsForParent`<br>• `organizations:ListChildren`<br>• `organizations:DescribeAccount`<br>• `pricing:GetAttributeValues`<br>• `pricing:GetProducts`                                                          | September 9, 2025 |
| [AWSBillingConductorReadOnlyAccess](#security-iam-awsmanpol-readonly "#security-iam-awsmanpol-readonly")<br>• Update to existing policies | We added the following actions to the<br>`AWSBillingConductorReadOnlyAccess` policy:<br>• `billingconductor:GetBillingGroupCostReport`<br>• `organizations:ListRoots`<br>• `organizations:ListOrganizationalUnitsForParent`<br>• `organizations:ListChildren`<br>• `organizations:DescribeAccount`<br>• `pricing:GetAttributeValues`<br>• `pricing:GetProducts` | September 9, 2025 |
| AWSBillingConductorReadOnlyAccess                                                                                                         | Added `GetBillingGroupCostReport` to the `AWSBillingConductorReadOnlyAccess` policy.                                                                                                                                                                                                                                                                            | February 8, 2024  |
| AWSBillingConductorFullAccess                                                                                                             | Created policy                                                                                                                                                                                                                                                                                                                                                  | March 29, 2022    |
| AWSBillingConductorReadOnlyAccess                                                                                                         | Created policy                                                                                                                                                                                                                                                                                                                                                  | March 29, 2022    |
| AWS Billing Conductor change log published                                                                                                | AWS Billing Conductor started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                    | March 29, 2022    |
