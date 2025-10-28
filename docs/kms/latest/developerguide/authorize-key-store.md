# Control access to your AWS CloudHSM key store

You use IAM policies to control access to your AWS CloudHSM key store and your AWS CloudHSM cluster. You
can use key policies, IAM policies, and grants to control access to the AWS KMS keys in
your AWS CloudHSM key store. We recommend that you provide users, groups, and roles only the
permissions that they require for the tasks that they are likely to perform.

To support your AWS CloudHSM key stores, AWS KMS needs permission to get information about your AWS CloudHSM
clusters. It also needs permission to create the network infrastructure that connects your AWS CloudHSM
key store to its AWS CloudHSM cluster. To get these permissions, AWS KMS creates the **AWSServiceRoleForKeyManagementServiceCustomKeyStores**
service-linked role in your AWS account. For more information, see [Authorizing AWS KMS to manage AWS CloudHSM and Amazon EC2 resources](authorize-kms.md "authorize-kms.md").

When designing your AWS CloudHSM key store, be sure that the principals who use and manage it have
only the permissions that they require. The following list describes the minimum permissions
required for AWS CloudHSM key store managers and users.

- Principals who create and manage your AWS CloudHSM key store require the following permission
  to use the AWS CloudHSM key store API operations.
  - `cloudhsm:DescribeClusters`
  - `kms:CreateCustomKeyStore`
  - `kms:ConnectCustomKeyStore`
  - `kms:DeleteCustomKeyStore`
  - `kms:DescribeCustomKeyStores`
  - `kms:DisconnectCustomKeyStore`
  - `kms:UpdateCustomKeyStore`
  - `iam:CreateServiceLinkedRole`

- Principals who create and manage the AWS CloudHSM cluster that is associated with your AWS CloudHSM
  key store need permission to create and initialize an AWS CloudHSM cluster. This includes
  permission to create or use an Amazon Virtual Private Cloud (VPC), create subnets, and create an Amazon EC2
  instance. They might also need to create and delete HSMs, and manage backups. For lists of
  the required permissions, see [Identity and access management for AWS CloudHSM](../../../cloudhsm/latest/userguide/identity-access-management.md "../../../cloudhsm/latest/userguide/identity-access-management.md") in the
  _AWS CloudHSM User Guide_.
- Principals who create and manage AWS KMS keys in your AWS CloudHSM key store require [the same permissions](create-keys.md#create-key-permissions "create-keys.md#create-key-permissions") as those who create and
  manage any KMS key in AWS KMS. The [default key
  policy](key-policy-default.md "key-policy-default.md") for a KMS key in an AWS CloudHSM key store is identical to the default key policy
  for KMS keys in AWS KMS. [Attribute-based access control](abac.md "abac.md") (ABAC),
  which uses tags and aliases to control access to KMS keys, is also effective on KMS keys
  in AWS CloudHSM key stores.
- Principals who use the KMS keys in your AWS CloudHSM key store for [cryptographic operations](manage-cmk-keystore.md#use-cmk-keystore "manage-cmk-keystore.md#use-cmk-keystore") need permission to perform the
  cryptographic operation with the KMS key, such as [kms:Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md"). You can provide these permissions
  in a key policy, IAM policy. But, they do not need any additional permissions to use a
  KMS key in an AWS CloudHSM key store.
