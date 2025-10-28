**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Step 6: Delete a Vault in Amazon Glacier

A vault is a container for storing archives. To delete an Amazon Glacier vault, you must first
delete all existing archives in the vault as of the last inventory that Amazon Glacier
computed.

You can delete a vault programmatically or by using the Amazon Glacier console. For
information about deleting a vault programmatically, see [Deleting a Vault in Amazon Glacier](deleting-vaults.md "deleting-vaults.md").

###### Important

If you upload an archive to a vault or delete an archive from a vault within the recent 24 hours, you must wait until
the last vault inventory is updated to reflect the latest information. Amazon Glacier prepares an inventory for each vault periodically, every 24 hours.

###### To delete an empty vault

1. Sign in to the AWS Management Console and open the Amazon Glacier console at [https://console.aws.amazon.com/glacier/home](https://console.aws.amazon.com/glacier/home "https://console.aws.amazon.com/glacier/home").
2. From the **Select a Region** menu, choose the AWS Region for the vault
   that you want to delete.

In this getting started exercise, your example vault is in the US West (Oregon)
Region. 3. Select the option button next to the empty vault that you want to delete. If the vault is
not empty, you must delete all archives before deleting the vault. For more
information, see [Deleting an Archive in Amazon Glacier](deleting-an-archive.md "deleting-an-archive.md").

###### Important

Deleting a vault can't be undone. 4. Choose **Delete**. 5. The **Delete vault** dialog box appears. Choose
**Delete**.

###### To delete a nonempty vault

1. If you're deleting a nonempty vault, you must first delete all existing archives before
   deleting the vault. You can do this by writing code to make a delete archive
   request by using either the REST API, the AWS SDK for Java, the AWS SDK for .NET or the
   AWS CLI. For information about deleting archives, see [Step 5: Delete an Archive from a Vault in
   Amazon Glacier](getting-started-delete-archive.md "getting-started-delete-archive.md").
2. After the vault is empty, follow the steps to delete an empty vault in the preceding
   procedure.
