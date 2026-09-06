

# AWS managed policies for AWS Billing and Cost Management
<a name="security-iam-awsmanpol"></a>

Creating [IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) with only the permissions your team needs requires time and expertise. To get started quickly, you can use AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

## AWSUserAttributeCostAllocationPolicy
<a name="security-iam-awsmanpol-AWSUserAttributeCostAllocationPolicy"></a>

This policy provides permissions for the user attributes for cost allocation service-linked role to fetch role information for internal service operations.

This policy is attached to the `AWSServiceRoleForUserAttributeCostAllocation` service-linked role.

## AWS Billing and Cost Management updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Billing and Cost Management since this service began tracking these changes.


| Policy | Version | Change | 
| --- | --- | --- | 
| AWSUserAttributeCostAllocationPolicy | 1 | **December 15, 2025:** Initial policy creation. This policy provides permissions for the user attributes for cost allocation service-linked role to fetch role information for internal service operations. | 