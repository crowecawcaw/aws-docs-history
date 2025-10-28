**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Working with Vaults in Amazon Glacier

A vault is a container for storing archives. When you create a vault, you specify a vault
name and the AWS Region in which you want to create the vault. For a list of the
AWS Regions supported by Amazon Glacier, see [Amazon Glacier endpoints and quotas](../../../general/latest/gr/glacier-service.md "../../../general/latest/gr/glacier-service.md") in
the _AWS General Reference_.

You can store an unlimited number of archives in a vault.

###### Important

Amazon Glacier does provide a console. However, any archive operation, such as upload, download,
or deletion, requires you to use the AWS Command Line Interface (AWS CLI) or write code. There is no
console support for archive operations. For example, to upload data, such as photos,
videos, and other documents, you must either use the AWS CLI or write code to make
requests, by using either the REST API directly or by using the AWS SDKs.

To install the AWS CLI, see [AWS Command Line Interface](http://aws.amazon.com/cli/ "http://aws.amazon.com/cli/"). For
more information about using Amazon Glacier with the AWS CLI, see the [AWS CLI Reference
for Amazon Glacier](../../../cli/latest/reference/glacier/index.md "../../../cli/latest/reference/glacier/index.md"). For examples of using the AWS CLI to upload archives to
Amazon Glacier, see [Using
Amazon Glacier with the AWS Command Line Interface](../../../cli/latest/userguide/cli-using-glacier.md "../../../cli/latest/userguide/cli-using-glacier.md").

###### Topics

- [Vault Operations in Amazon Glacier](#vault-operations-quick-intro "#vault-operations-quick-intro")
- [Creating a Vault in Amazon Glacier](creating-vaults.md "creating-vaults.md")
- [Retrieving Vault Metadata in Amazon Glacier](retrieving-vault-info.md "retrieving-vault-info.md")
- [Downloading a Vault Inventory in Amazon Glacier](vault-inventory.md "vault-inventory.md")
- [Configuring Vault Notifications in Amazon Glacier](configuring-notifications.md "configuring-notifications.md")
- [Deleting a Vault in Amazon Glacier](deleting-vaults.md "deleting-vaults.md")
- [Tagging Your Amazon Glacier Vaults](tagging-vaults.md "tagging-vaults.md")
- [Amazon Glacier Vault Lock](vault-lock.md "vault-lock.md")

## Vault Operations in Amazon Glacier

Amazon Glacier supports various vault operations. Vault operations are specific to particular
AWS Regions. In other words, when you create a vault, you create it in a specific
AWS Region. When you list vaults, Amazon Glacier returns the vault list from the
AWS Region that you specified in the request.

### Creating and Deleting Vaults

An AWS account can create up to 1,000 vaults per AWS Region. For a list of the
AWS Regions supported by Amazon Glacier, see [Amazon Glacier endpoints and
quotas](../../../general/latest/gr/glacier-service.md "../../../general/latest/gr/glacier-service.md") in the _AWS General Reference_.

You can delete a vault only if there are no archives in the vault as of the last inventory
that Amazon Glacier computed and if there have been no writes to the vault since the last
inventory.

###### Note

Amazon Glacier prepares an inventory for each vault periodically, every 24 hours. Because the
inventory might not reflect the latest information, Amazon Glacier ensures that the
vault is indeed empty by checking if there were any write operations since the
last vault inventory.

For more information, see [Creating a Vault in Amazon Glacier](creating-vaults.md "creating-vaults.md") and [Deleting a Vault in Amazon Glacier](deleting-vaults.md "deleting-vaults.md").

### Retrieving Vault Metadata

You can retrieve vault information such as the vault creation date, number of archives in
the vault, and the total size of all the archives in the vault. Amazon Glacier
provides API calls for you to retrieve this information for a specific vault or all
the vaults in a specific AWS Region in your account. For more information, see [Retrieving Vault Metadata in Amazon Glacier](retrieving-vault-info.md "retrieving-vault-info.md").

### Downloading a Vault Inventory

A _vault inventory_ refers to the list of archives in a
vault. For each archive in the list, the inventory provides archive information,
such as the archive ID, creation date, and size. Amazon Glacier updates the vault
inventory once a day, starting on the day that the first archive is uploaded to the
vault. A vault inventory must exist for you to be able to download it.

Downloading a vault inventory is an asynchronous operation. You must first initiate a job
to download the inventory. After receiving the job request, Amazon Glacier prepares your
inventory for download. After the job is completed, you can download the inventory
data.

Given the asynchronous nature of the job, you can use Amazon Simple Notification Service (Amazon SNS) notifications to
notify you when the job is completed. You can specify an Amazon SNS topic for each
individual job request or configure your vault to send a notification when specific
vault events occur.

Amazon Glacier prepares an inventory for each vault periodically, every 24 hours. If there have
been no archive additions or deletions to the vault since the last inventory, the
inventory date is not updated.

When you initiate a job for a vault inventory, Amazon Glacier returns the last inventory that it
generated, which is a point-in-time snapshot and not real-time data. You might not
find it useful to retrieve vault inventory for each archive upload. However, suppose
that you maintain a database on the client-side that contains metadata associated
with the archives that you upload to Amazon Glacier. In that case, you might find the
vault inventory useful to reconcile information in your database with the actual
vault inventory.

For more information about retrieving a vault inventory, see [Downloading a Vault Inventory in Amazon Glacier](vault-inventory.md "vault-inventory.md").

### Configuring Vault Notifications

Retrieving anything from Amazon Glacier, such as an archive from a vault or a vault inventory,
is a two-step process. First, you initiate a job. After the job is completed, you
download the output. To learn when your job is complete, you can use Amazon Glacier
notifications. Amazon Glacier sends notification messages to an Amazon Simple Notification Service (Amazon SNS) topic
that you provide.

You can configure notifications on a vault and identify vault events and the Amazon SNS
topic to be notified when the event occurs. Anytime the vault event occurs, Amazon Glacier sends a notification to the specified Amazon SNS topic. For more
information, see [Configuring Vault Notifications in Amazon Glacier](configuring-notifications.md "configuring-notifications.md").
