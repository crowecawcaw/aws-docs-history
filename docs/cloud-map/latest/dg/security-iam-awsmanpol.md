# AWS managed policies for AWS Cloud Map

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed 
 to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because 
 they're available for all AWS customers to use. We recommend that you reduce permissions further by defining 
 [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS 
 managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is 
 most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
 existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies") in the 
 *IAM User Guide*.


## AWS managed
 policy: AWSCloudMapDiscoverInstanceAccess


You can attach `AWSCloudMapDiscoverInstanceAccess` to your IAM entities.
 Provides access to AWS Cloud Map Discovery API.


To view the permissions for this policy, see [AWSCloudMapDiscoverInstanceAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudMapDiscoverInstanceAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudMapDiscoverInstanceAccess.html") in the *AWS
 Managed Policy Reference*.


## AWS managed policy:
 AWSCloudMapReadOnlyAccess


You can attach `AWSCloudMapReadOnlyAccess` to your IAM entities. Grants
 read-only access to all AWS Cloud Map actions.


To view the permissions for this policy, see [AWSCloudMapReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudMapReadOnlyAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudMapReadOnlyAccess.html") in the *AWS Managed
 Policy Reference*.


## AWS managed
 policy: AWSCloudMapRegisterInstanceAccess


You can attach `AWSCloudMapRegisterInstanceAccess` to your IAM entities.
 Grants read-only access to namespaces and services and grants permission to register and
 deregister service instances.


To view the permissions for this policy, see [AWSCloudMapRegisterInstanceAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudMapRegisterInstanceAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudMapRegisterInstanceAccess.html") in the *AWS
 Managed Policy Reference*.


## AWS managed policy:
 AWSCloudMapFullAccess


You can attach `AWSCloudMapFullAccess` to your IAM entities. Provides
 full access to all AWS Cloud Map actions


To view the permissions for this policy, see [AWSCloudMapFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudMapFullAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudMapFullAccess.html") in the *AWS Managed Policy
 Reference*.


## AWS Cloud Map updates to AWS managed
 policies


View details about updates to AWS managed policies for AWS Cloud Map since this service
 began tracking these changes. For automatic alerts about changes, subscribe
 to the RSS feed on the AWS Cloud Map document history page.




| Change | Description | Date |
| --- | --- | --- |
| [AWSCloudMapDiscoverInstanceAccess](#security-iam-awsmanpol-AWSCloudMapDiscoverInstanceAccess "#security-iam-awsmanpol-AWSCloudMapDiscoverInstanceAccess"), [AWSCloudMapRegisterInstanceAccess](#security-iam-awsmanpol-AWSCloudMapRegisterInstanceAccess "#security-iam-awsmanpol-AWSCloudMapRegisterInstanceAccess"), [AWSCloudMapReadOnlyAccess](#security-iam-awsmanpol-AWSCloudMapReadOnlyAccess "#security-iam-awsmanpol-AWSCloudMapReadOnlyAccess") – Updates to existing policies. | AWS Cloud Map updated these policies to provide access to the new AWS Cloud Map `DiscoverInstanceRevision` API operations. | August 15, 2023 |
