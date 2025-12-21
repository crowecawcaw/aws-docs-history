**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Deleting a Vault in Amazon Glacier

Amazon Glacier (Amazon Glacier) deletes a vault only if there are no archives in the vault as of the last
inventory it computed and there have been no writes to the vault since the last inventory.
For information about deleting archives, see [Deleting an Archive in Amazon Glacier](deleting-an-archive.md "deleting-an-archive.md").
For information about downloading a vault inventory, [Downloading a Vault Inventory in Amazon Glacier](vault-inventory.md "vault-inventory.md").

###### Note

Amazon Glacier prepares an inventory for each vault periodically, every 24 hours. Because the
inventory might not reflect the latest information, Amazon Glacier ensures the vault is
indeed empty by checking if there were any write operations since the last vault
inventory.

###### Note

For automated deletion of vault archives, see [Automated deletion of vault archives in Amazon S3 Glacier](https://aws.amazon.com/solutions/guidance/automated-deletion-of-vault-archives-in-amazon-s3-glacier/ "https://aws.amazon.com/solutions/guidance/automated-deletion-of-vault-archives-in-amazon-s3-glacier/").

###### Topics

- [Deleting a Vault in Amazon Glacier Using the AWS SDK for Java](deleting-vaults-sdk-java.md "deleting-vaults-sdk-java.md")
- [Deleting a Vault in Amazon Glacier Using the AWS SDK for .NET](deleting-vaults-sdk-dotnet.md "deleting-vaults-sdk-dotnet.md")
- [Deleting a Vault in Amazon Glacier Using the REST API](deleting-vault-rest-api.md "deleting-vault-rest-api.md")
- [Deleting an Empty Vault by Using the Amazon Glacier
  Console](deleting-vaults-console.md "deleting-vaults-console.md")
- [Deleting a Vault in Amazon Glacier Using the AWS Command Line Interface](deleting-vaults-cli.md "deleting-vaults-cli.md")
