**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Deleting an Empty Vault by Using the Amazon Glacier

Console

###### Note

Before deleting a vault, you must delete all existing archives within the vault. You can do
this by writing code to make a delete archive request by using either the REST API, the
AWS SDK for Java, the AWS SDK for .NET, or by using the AWS Command Line Interface (AWS CLI). For information about
deleting archives, see [Step 5: Delete an Archive from a Vault in
Amazon Glacier](getting-started-delete-archive.md "getting-started-delete-archive.md").

After your vault is empty, you can delete it by using the following steps.

###### To delete an empty vault by using the Amazon Glacier console

1. Sign into the AWS Management Console and open the Amazon Glacier console at [Amazon Glacier
   Console](https://console.aws.amazon.com/glacier/home "https://console.aws.amazon.com/glacier/home").
2. Under **Select a Region**, choose the AWS Region where the vault
   exists.
3. In the left navigation pane, choose **Vaults**.
4. In the **Vaults** list, select the option button next to the name of the
   vault that you want to delete, and then choose **Delete** at the
   top of the page.
5. In the **Delete vault** dialog box, confirm that you want to delete the
   vault by choosing **Delete**.

###### Important

Deleting a vault can't be undone. 6. To verify that you've deleted the vault, open the **Vaults** list and
enter the name of the vault that you deleted. If the vault can't be found, your deletion
was successful.
