**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Supported Operations in

Amazon Glacier

To work with vaults and archives (see [Amazon Glacier Data Model](amazon-glacier-data-model.md "amazon-glacier-data-model.md")), Amazon Glacier supports a set of operations.
Among all the supported operations, only the following operations are asynchronous:

- Retrieving an archive
- Retrieving a vault inventory (list of archives)
  These operations require you to first initiate a job and then download the job output.
  The following sections summarize the Amazon Glacier operations.

## Vault Operations

Amazon Glacier provides operations to create and delete vaults. You can obtain a vault
description for a specific vault or for all vaults in an AWS Region. The vault
description provides information, such as the creation date, the number of archives
in the vault, the total size in bytes used by all the archives in the vault, and the
date that Amazon Glacier generated the vault inventory. Amazon Glacier also provides
operations to set, retrieve, and delete a notification configuration on the vault.
For more information, see [Working with Vaults in Amazon Glacier](working-with-vaults.md "working-with-vaults.md").

## Archive Operations

Amazon Glacier provides operations for you to upload and delete archives. You cannot
update an existing archive; you must delete the existing archive and upload a new
archive. Each time that you upload an archive, Amazon Glacier generates a new archive ID.
For more information, see [Working with Archives in Amazon Glacier](working-with-archives.md "working-with-archives.md").

## Jobs

You can initiate an Amazon Glacier job to perform a retrieval on an archive or get an
inventory of a vault.

The following are the types of Amazon Glacier jobs:

- `archive-retrieval` – Retrieve an archive.

For more information, see [Downloading an Archive in Amazon Glacier](downloading-an-archive.md "downloading-an-archive.md").

- `inventory-retrieval` – Inventory a vault.

For more information, see [Downloading a Vault Inventory in Amazon Glacier](vault-inventory.md "vault-inventory.md").
