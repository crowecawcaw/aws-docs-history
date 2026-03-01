**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Vault Operations

The following are the vault operations available in Amazon Glacier.

###### Topics

- [Abort Vault Lock (DELETE lock-policy)](api-AbortVaultLock.md "api-AbortVaultLock.md")
- [Add Tags To Vault (POST tags add)](api-AddTagsToVault.md "api-AddTagsToVault.md")
- [Create Vault (PUT vault)](api-vault-put.md "api-vault-put.md")
- [Complete Vault Lock (POST lockId)](api-CompleteVaultLock.md "api-CompleteVaultLock.md")
- [Delete Vault (DELETE vault)](api-vault-delete.md "api-vault-delete.md")
- [Delete Vault Access Policy (DELETE access-policy)](api-DeleteVaultAccessPolicy.md "api-DeleteVaultAccessPolicy.md")
- [Delete Vault Notifications (DELETE notification-configuration)](api-vault-notifications-delete.md "api-vault-notifications-delete.md")
- [Describe Vault (GET vault)](api-vault-get.md "api-vault-get.md")
- [Get Vault Access Policy (GET access-policy)](api-GetVaultAccessPolicy.md "api-GetVaultAccessPolicy.md")
- [Get Vault Lock (GET lock-policy)](api-GetVaultLock.md "api-GetVaultLock.md")
- [Get Vault Notifications (GET notification-configuration)](api-vault-notifications-get.md "api-vault-notifications-get.md")
- [Initiate Vault Lock (POST lock-policy)](api-InitiateVaultLock.md "api-InitiateVaultLock.md")
- [List Tags For Vault (GET tags)](api-ListTagsForVault.md "api-ListTagsForVault.md")
- [List Vaults (GET vaults)](api-vaults-get.md "api-vaults-get.md")
- [Remove Tags From Vault (POST tags remove)](api-RemoveTagsFromVault.md "api-RemoveTagsFromVault.md")
- [Set Vault Access Policy (PUT access-policy)](api-SetVaultAccessPolicy.md "api-SetVaultAccessPolicy.md")
- [Set Vault Notification Configuration (PUT notification-configuration)](api-vault-notifications-put.md "api-vault-notifications-put.md")
