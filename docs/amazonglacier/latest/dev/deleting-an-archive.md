**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Deleting an Archive in Amazon Glacier

You cannot delete an archive using the Amazon Glacier (Amazon Glacier) management console. To delete
an archive you must use the AWS Command Line Interface (CLI) or write code to make a delete request using
either the REST API directly or the AWS SDK for Java and .NET wrapper libraries. The following
topics explain how to use the AWS SDK for Java and .NET wrapper libraries, the REST
API, and the AWS CLI.

###### Topics

- [Deleting an Archive in Amazon Glacier Using the AWS SDK for Java](deleting-an-archive-using-java.md "deleting-an-archive-using-java.md")
- [Deleting an Archive in Amazon Glacier Using the AWS SDK for .NET](deleting-an-archive-using-dot-net.md "deleting-an-archive-using-dot-net.md")
- [Deleting an Amazon Glacier Archive Using the
  REST API](deleting-an-archive-using-rest.md "deleting-an-archive-using-rest.md")
- [Deleting an Archive in Amazon Glacier Using the
  AWS Command Line Interface](deleting-an-archive-using-cli.md "deleting-an-archive-using-cli.md")
  You can delete one archive at a time from a vault. To delete the archive you must provide
  its archive ID in your delete request. You can get the archive ID by downloading the vault
  inventory for the vault that contains the archive. For more information about downloading
  the vault inventory, see [Downloading a Vault Inventory in Amazon Glacier](vault-inventory.md "vault-inventory.md").

After you delete an archive, you might still be able to make a successful request to
initiate a job to retrieve the deleted archive, but the archive retrieval job will fail.

Archive retrievals that are in progress for an archive ID when you delete the archive
might or might not succeed according to the following scenarios:

- If the archive retrieval job is actively preparing the data for download when
  Amazon Glacier receives the delete archive request, then the archival retrieval operation
  might fail.
- If the archive retrieval job has successfully prepared the archive for download
  when Amazon Glacier receives the delete archive request, then you will be able to
  download the output.
  For more information about archive retrieval, see [Downloading an Archive in Amazon Glacier](downloading-an-archive.md "downloading-an-archive.md").

This operation is idempotent. Deleting an already-deleted archive does not result in an
error.

After you delete an archive, if you immediately download the vault inventory, it might
include the deleted archive in the list because Amazon Glacier prepares vault inventory only
about once a day.

###### Note

For automated deletion of vault archives, see [Automated deletion of vault archives in Amazon S3 Glacier](https://aws.amazon.com/solutions/guidance/automated-deletion-of-vault-archives-in-amazon-s3-glacier/ "https://aws.amazon.com/solutions/guidance/automated-deletion-of-vault-archives-in-amazon-s3-glacier/").
