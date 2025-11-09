# AWS managed policies for AWS Key Management Service

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

policy: AWSKeyManagementServicePowerUser

You can attach the `AWSKeyManagementServicePowerUser` policy to your IAM
identities.

You can use the `AWSKeyManagementServicePowerUser` managed policy to give
IAM principals in your account the permissions of a power user. Power users can create
KMS keys, use and manage the KMS keys they create, and view all KMS keys and IAM
identities. Principals who have the `AWSKeyManagementServicePowerUser`
managed policy can also get permissions from other sources, including key policies,
other IAM policies, and grants.

`AWSKeyManagementServicePowerUser` is an AWS managed IAM policy. For
more information about AWS managed policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

###### Note

Permissions in this policy that are specific to a KMS key, such as
`kms:TagResource` and `kms:GetKeyRotationStatus`, are
effective only when the key policy for that KMS key [explicitly allows the
AWS account to use IAM policies](key-policy-default.md#key-policy-default-allow-root-enable-iam "key-policy-default.md#key-policy-default-allow-root-enable-iam") to control access to the key. To
determine whether a permission is specific to a KMS key, see [AWS KMS permissions](kms-api-permissions-reference.md "kms-api-permissions-reference.md") and look for a value of
**KMS key** in the **Resources** column.

This policy gives a power user permissions on any KMS key with a key policy that
permits the operation. For cross-account permissions, such as
`kms:DescribeKey` and `kms:ListGrants`, this might include
KMS keys in untrusted AWS accounts. For details, see [Best practices for IAM policies](iam-policies-best-practices.md "iam-policies-best-practices.md") and [Allowing users in other accounts to
use a KMS key](key-policy-modifying-external-accounts.md "key-policy-modifying-external-accounts.md"). To determine whether a
permission is valid on KMS keys in other accounts, see [AWS KMS permissions](kms-api-permissions-reference.md "kms-api-permissions-reference.md") and look for a value of
**Yes** in the **Cross-account use** column.

To allow principals to view the AWS KMS console without errors, the principal needs
the [tag:GetResources](../../../resourcegroupstagging/latest/APIReference/API_GetResources.md "../../../resourcegroupstagging/latest/APIReference/API_GetResources.md") permission, which is not included in the
`AWSKeyManagementServicePowerUser` policy. You can allow this
permission in a separate IAM policy.

The [AWSKeyManagementServicePowerUser](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSKeyManagementServicePowerUser "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSKeyManagementServicePowerUser") managed IAM policy includes the
following permissions.

- Allows principals to create KMS keys. Because this process includes setting
  the key policy, power users can give themselves and others permission to use and
  manage the KMS keys they create.
- Allows principals to create and delete [aliases](kms-alias.md "kms-alias.md") and [tags](tagging-keys.md "tagging-keys.md") on all
  KMS keys. Changing a tag or alias can allow or deny permission to use and
  manage the KMS key. For details, see [ABAC for AWS KMS](abac.md "abac.md").
- Allows principals to get detailed information about all KMS keys, including
  their key ARN, cryptographic configuration, key policy, aliases, tags, and [rotation status](rotate-keys.md "rotate-keys.md").
- Allows principals to list IAM users, groups, and roles.
- This policy does not allow principals to use or manage KMS keys that they
  didn't create. However, they can change aliases and tags on all KMS keys,
  which might allow or deny them permission to use or manage a KMS key.

To view the permissions for this policy, see [AWSKeyManagementServicePowerUser](../../../aws-managed-policy/latest/reference/AWSKeyManagementServicePowerUser.md "../../../aws-managed-policy/latest/reference/AWSKeyManagementServicePowerUser.md") in the AWS Managed Policy Reference.

## AWS managed policy: AWSServiceRoleForKeyManagementServiceCustomKeyStores

You can't attach `AWSServiceRoleForKeyManagementServiceCustomKeyStores` to
your IAM entities. This policy is attached to a service-linked role that gives AWS KMS
permission to view the AWS CloudHSM clusters associated with your AWS CloudHSM key store and create
the network to support a connection between your custom key store and its AWS CloudHSM cluster.
For more information, see [Authorizing AWS KMS to manage AWS CloudHSM and Amazon EC2 resources](authorize-kms.md "authorize-kms.md").

## AWS managed policy: AWSServiceRoleForKeyManagementServiceMultiRegionKeys

You can't attach `AWSServiceRoleForKeyManagementServiceMultiRegionKeys` to
your IAM entities. This policy is attached to a service-linked role that gives AWS KMS
permission to synchronize any changes to the key material of a multi-Region primary key
to its replica keys. For more information, see [Authorizing AWS KMS to synchronize multi-Region
keys](multi-region-auth-slr.md "multi-region-auth-slr.md").

## AWS KMS updates to AWS managed

policies

View details about updates to AWS managed policies for AWS KMS since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the AWS KMS [Document history](dochistory.md "dochistory.md")
page.

| Change                                                                                                                                        | Description                                                                                                                                                                                                                                                                     | Date              |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy](multi-region-auth-slr.md "multi-region-auth-slr.md")<br>– Update to existing policy | AWS KMS added a statement ID (`Sid`) field to the managed<br>policy in policy version v2.                                                                                                                                                                                       | November 21, 2024 |
| [AWSKeyManagementServiceCustomKeyStoresServiceRolePolicy](authorize-kms.md "authorize-kms.md")<br>– Update to existing policy                 | AWS KMS added the `ec2:DescribeVpcs`,<br>`ec2:DescribeNetworkAcls`, and<br>`ec2:DescribeNetworkInterfaces` permissions to<br>monitor changes in the VPC that contains your AWS CloudHSM cluster so that<br>AWS KMS can provide clear error messages in the case of<br>failures. | November 10, 2023 |
| AWS KMS started tracking changes                                                                                                              | AWS KMS started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                               | November 10, 2023 |
