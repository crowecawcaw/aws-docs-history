**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Step 2: Create a Vault in Amazon Glacier

A vault is a container for storing archives. Your first step is to create a vault in one of
the supported AWS Regions. For a list of the AWS Regions that are supported by
Amazon Glacier, see [Amazon Glacier endpoints and quotas](../../../general/latest/gr/glacier-service.md "../../../general/latest/gr/glacier-service.md") in the _AWS General
Reference_.

You can create vaults programmatically or by using the Amazon Glacier console. This section uses
the console to create a vault.

###### To create a vault

1. Sign in to the AWS Management Console and open the Amazon Glacier console at [https://console.aws.amazon.com/glacier/home](https://console.aws.amazon.com/glacier/home "https://console.aws.amazon.com/glacier/home").
2. In the left navigation pane, choose **Vaults**.
3. Choose **Create vault**.

The **Create vault** page opens. 4. Under **Select a Region**, select an AWS Region from the Region
selector. Your vault will be located in the Region that you select. 5. For **Vault name**, enter a name for your vault.

The following are the vault-naming requirements:

    * A vault name must be unique within an AWS account and the AWS Region in which the
     vault is created.
    * A vault name must be between 1 and 255 characters long.
    * A vault name can contain only the following characters: **a–z**, **A–Z**,
     **0–9**, **\_** (underscore), **-**
     (hyphen), and **.** (period).

6. Under **Event notifications**, to turn on or off notifications on a vault
   for when a job is completed, choose one of the following settings:
   - **Turn off notifications** – Notifications are turned off, and
     notifications are not sent to an Amazon Simple Notification Service (Amazon SNS) topic when a
     specified job is completed.

   - **Turn on notifications** – Notifications are turned on, and
     notifications are sent to the provided Amazon SNS topic when a specified job
     is completed.

   If you chose **Turn on notifications**, see [Configuring Vault Notifications by Using the Amazon Glacier
   Console](configuring-notifications-console.md "configuring-notifications-console.md").

7. If the AWS Region and vault name are correct, then choose **Create
   vault**.
   Your new vault is now listed on the **Vaults** page in the Amazon Glacier
   console.
