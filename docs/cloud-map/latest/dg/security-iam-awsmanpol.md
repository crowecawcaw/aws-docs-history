# AWS managed policies for AWS Cloud Map

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed

policy: AWSCloudMapDiscoverInstanceAccess

You can attach `AWSCloudMapDiscoverInstanceAccess` to your IAM entities.
Provides access to AWS Cloud Map Discovery API.

To view the permissions for this policy, see [AWSCloudMapDiscoverInstanceAccess](../../../aws-managed-policy/latest/reference/AWSCloudMapDiscoverInstanceAccess.md "../../../aws-managed-policy/latest/reference/AWSCloudMapDiscoverInstanceAccess.md") in the _AWS
Managed Policy Reference_.

## AWS managed policy:

AWSCloudMapReadOnlyAccess

You can attach `AWSCloudMapReadOnlyAccess` to your IAM entities. Grants
read-only access to all AWS Cloud Map actions.

To view the permissions for this policy, see [AWSCloudMapReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSCloudMapReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSCloudMapReadOnlyAccess.md") in the _AWS Managed
Policy Reference_.

## AWS managed

policy: AWSCloudMapRegisterInstanceAccess

You can attach `AWSCloudMapRegisterInstanceAccess` to your IAM entities.
Grants read-only access to namespaces and services and grants permission to register and
deregister service instances.

To view the permissions for this policy, see [AWSCloudMapRegisterInstanceAccess](../../../aws-managed-policy/latest/reference/AWSCloudMapRegisterInstanceAccess.md "../../../aws-managed-policy/latest/reference/AWSCloudMapRegisterInstanceAccess.md") in the _AWS
Managed Policy Reference_.

## AWS managed policy:

AWSCloudMapFullAccess

You can attach `AWSCloudMapFullAccess` to your IAM entities. Provides
full access to all AWS Cloud Map actions

To view the permissions for this policy, see [AWSCloudMapFullAccess](../../../aws-managed-policy/latest/reference/AWSCloudMapFullAccess.md "../../../aws-managed-policy/latest/reference/AWSCloudMapFullAccess.md") in the _AWS Managed Policy
Reference_.

## AWS Cloud Map updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Cloud Map since this service
began tracking these changes. For automatic alerts about changes, subscribe
to the RSS feed on the AWS Cloud Map document history page.

| Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                | Date            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [AWSCloudMapDiscoverInstanceAccess](#security-iam-awsmanpol-AWSCloudMapDiscoverInstanceAccess "#security-iam-awsmanpol-AWSCloudMapDiscoverInstanceAccess"), [AWSCloudMapRegisterInstanceAccess](#security-iam-awsmanpol-AWSCloudMapRegisterInstanceAccess "#security-iam-awsmanpol-AWSCloudMapRegisterInstanceAccess"), [AWSCloudMapReadOnlyAccess](#security-iam-awsmanpol-AWSCloudMapReadOnlyAccess "#security-iam-awsmanpol-AWSCloudMapReadOnlyAccess") – Updates to existing policies. | AWS Cloud Map updated these policies to provide access to the new AWS Cloud Map `DiscoverInstanceRevision` API operations. | August 15, 2023 |
