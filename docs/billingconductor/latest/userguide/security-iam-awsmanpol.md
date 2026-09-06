

# AWS managed policies for AWS Billing Conductor
<a name="security-iam-awsmanpol"></a>





To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AWSBillingConductorFullAccess
<a name="security-iam-awsmanpol-fullaccess"></a>

The AWSBillingConductorFullAccess managed policy grants complete access to AWS Billing Conductor console and APIs. Users can list, create, and delete AWS Billing Conductor resources.

To view the permissions for this policy, see [AWSBillingConductorFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBillingConductorFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSBillingConductorReadOnlyAccess
<a name="security-iam-awsmanpol-readonly"></a>

The AWSBillingConductorReadOnlyAccess managed policy grants read-only access to AWS Billing Conductor console and APIs. Users can view and list all AWS Billing Conductor resources. Users can't create or delete resources.

To view the permissions for this policy, see [AWSBillingConductorReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBillingConductorReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## AWS Billing Conductor updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for AWS Billing Conductor since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS Billing Conductor Document history page.




| Change | Description | Date | 
| --- | --- | --- | 
| [AWSBillingConductorFullAccess](#security-iam-awsmanpol-fullaccess) - Update to existing policies | We added the `organizations:DescribeResponsibilityTransfer` and `organizations:ListInboundResponsibilityTransfers` actions to the `AWSBillingConductorFullAccess` policy. | November 19, 2025 | 
| [AWSBillingConductorFullAccess](#security-iam-awsmanpol-fullaccess) - Update to existing policies | We added the following actions to the `AWSBillingConductorFullAccess` policy:+  `organizations:ListRoots` <br />+  `organizations:ListOrganizationalUnitsForParent` <br />+  `organizations:ListChildren` <br />+  `organizations:DescribeAccount` <br />+  `pricing:GetAttributeValues` <br />+  `pricing:GetProducts`  | September 9, 2025 | 
| [AWSBillingConductorReadOnlyAccess](#security-iam-awsmanpol-readonly) - Update to existing policies | We added the following actions to the `AWSBillingConductorReadOnlyAccess` policy:+  `billingconductor:GetBillingGroupCostReport` <br />+  `organizations:ListRoots` <br />+  `organizations:ListOrganizationalUnitsForParent` <br />+  `organizations:ListChildren` <br />+  `organizations:DescribeAccount` <br />+  `pricing:GetAttributeValues` <br />+  `pricing:GetProducts`  | September 9, 2025 | 
| AWSBillingConductorReadOnlyAccess | Added `GetBillingGroupCostReport` to the `AWSBillingConductorReadOnlyAccess` policy. | February 8, 2024 | 
| AWSBillingConductorFullAccess | Created policy | March 29, 2022 | 
| AWSBillingConductorReadOnlyAccess | Created policy | March 29, 2022 | 
| AWS Billing Conductor change log published | AWS Billing Conductor started tracking changes for its AWS managed policies. | March 29, 2022 | 