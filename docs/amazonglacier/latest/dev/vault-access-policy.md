**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Vault Access Policies

An Amazon Glacier vault access policy is a resource-based policy that you can use to manage
permissions to your vault.

You can create one vault access policy for each vault to manage
_permissions_. You can modify permissions in a vault access policy
at any time. Amazon Glacier also supports a Vault Lock policy on each vault that, after you
lock it, cannot be altered. For more information about working with Vault Lock policies,
see [Vault Lock Policies](vault-lock-policy.md "vault-lock-policy.md").

###### Examples

- [Example 1: Grant Cross-Account Permissions for Specific Amazon Glacier Actions](#vault-access-multiple-accounts "#vault-access-multiple-accounts")
- [Example 2: Grant Cross-Account Permissions for MFA Delete Operations](#vault-access-mfa-authentication "#vault-access-mfa-authentication")

## Example 1: Grant Cross-Account Permissions for Specific Amazon Glacier Actions

The following example policy grants cross-account permissions to two
AWS accounts for a set of Amazon Glacier operations on a vault named
`examplevault`.

###### Note

The account that owns the vault is billed for all costs associated with the
vault. All requests, data transfer, and retrieval costs made by allowed external
accounts are billed to the account that owns the vault.

## Example 2: Grant Cross-Account Permissions for MFA Delete Operations

You can use multi-factor authentication (MFA) to protect your Amazon Glacier resources.
To provide an extra level of security, MFA requires users to prove physical
possession of an MFA device by providing a valid MFA code. For more information about
configuring MFA access, see [Configuring MFA-Protected API Access](../../../IAM/latest/UserGuide/MFAProtectedAPI.md "../../../IAM/latest/UserGuide/MFAProtectedAPI.md") in the
_IAM User Guide_.

The example policy grants an AWS account with temporary credentials permission
to delete archives from a vault named examplevault, provided the request is
authenticated with an MFA device. The policy uses the
`aws:MultiFactorAuthPresent` condition key to specify this additional
requirement. For more information, see [Available Keys
for Conditions](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.
