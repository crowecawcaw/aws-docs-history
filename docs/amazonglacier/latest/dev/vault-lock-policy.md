**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Vault Lock Policies

An Amazon Glacier (Amazon Glacier) vault can have one resource-based vault access policy and one
Vault Lock policy attached to it. A _Vault Lock policy_ is a vault
access policy that you can lock. Using a Vault Lock policy can help you enforce
regulatory and compliance requirements. Amazon Glacier provides a set of API operations for
you to manage the Vault Lock policies, see [Locking a Vault by Using the Amazon Glacier API](vault-lock-how-to-api.md "vault-lock-how-to-api.md").

As an example of a Vault Lock policy, suppose that you are required to retain
archives for one year before you can delete them. To implement this requirement, you can
create a Vault Lock policy that denies users permissions to delete an archive until the
archive has existed for one year. You can test this policy before locking it down. After
you lock the policy, the policy becomes immutable. For more information about the
locking process, see Vault Lock Policies. If you want to manage other user permissions that can be changed, you can use the
vault access policy (see [Vault Access Policies](vault-access-policy.md "vault-access-policy.md")).

You can use the Amazon Glacier API, Amazon SDKs, AWS CLI, or the Amazon Glacier console to create
and manage Vault Lock policies. For a list of Amazon Glacier actions allowed for vault
resource-based policies, see [API Permissions Reference](glacier-api-permissions-ref.md "glacier-api-permissions-ref.md").

###### Examples

- [Example 1: Deny Deletion Permissions for
  Archives Less Than 365 Days Old](#vault-lock-archive-age "#vault-lock-archive-age")
- [Example 2: Deny Deletion Permissions
  Based on a Tag](#vault-lock-legal-hold-tag "#vault-lock-legal-hold-tag")

## Example 1: Deny Deletion Permissions for

Archives Less Than 365 Days Old

Suppose that you have a regulatory requirement to retain archives for up to one
year before you can delete them. You can enforce that requirement by implementing the
following Vault Lock policy. The policy denies the `glacier:DeleteArchive`
action on the examplevault vault if the archive being deleted is less than one year
old. The policy uses the Amazon Glacier-specific condition key
`ArchiveAgeInDays` to enforce the one-year retention requirement.

## Example 2: Deny Deletion Permissions

Based on a Tag

Suppose that you have a time-based retention rule that an archive can be deleted
if it is less than a year old. At the same time, suppose that you need to place a
legal hold on your archives to prevent deletion or modification for an indefinite
duration during a legal investigation. In this case, the legal hold takes precedence
over the time-based retention rule specified in the Vault Lock policy.

To put these two rules in place, the following example policy has two
statements:

- The first statement denies deletion permissions for everyone, locking the
  vault. This lock is performed by using the `LegalHold` tag.
- The second statement grants deletion permissions when the archive is less
  than 365 days old. But even when archives are less than 365 days old, no one
  can delete them when the condition in the first statement is met.
