**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Configuring Vault Notifications by Using the

Amazon Glacier Console

This section describes how to configure vault notifications by using the Amazon Glacier console.
When you configure notifications, you specify job-completion events that send a notification
to an Amazon Simple Notification Service (Amazon SNS) topic. In addition to configuring notifications for the vault, you
can also specify a topic to publish notifications to when you initiate a job. If your vault
is configured to send a notification for a specific event and you also configure
notifications in the job-initiation request, then two notifications are sent.

###### To configure a vault notification

1. Sign in to the AWS Management Console and open the Amazon Glacier console at [https://console.aws.amazon.com/glacier/home](https://console.aws.amazon.com/glacier/home "https://console.aws.amazon.com/glacier/home").
2. In the left navigation pane, choose **Vaults**.
3. In the **Vaults** list, choose a vault.
4. In the **Notifications** section, choose **Edit**.
5. On the **Event notifications** page, choose **Turn on
   notifications**.
6. In the **Notifications** section, choose one of the following Amazon Simple Notification Service
   (Amazon SNS) options, and then follow the corresponding steps:

| Amazon SNS options               | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Create new SNS topic**         | 1. Choose **Create new SNS topic**.<br>2. For **Topic name**, enter the name of the new topic.<br>Topic names can be up to 256 characters. Alphanumeric characters, hyphens (-), and<br>underscores (\_) are allowed. Topic names must be unique<br>within the account and AWS Region.<br>3. (Optional) If you want to subscribe to the topic by using SMS messages, enter a name<br>for **Display name**.<br>A display name can have up to 100 characters.                                                                                                                                  |
| **Choose an existing SNS topic** | 1. Choose **Choose an existing SNS<br>topic**.<br>2. Under **Specify SNS topic**, choose one of the<br>following options:<br>• **Choose from your SNS topics**<br>An **SNS topic\*<br>• dropdown<br>list appears.<br>Choose an existing topic from the dropdown<br>list.<br>• **Enter SNS topic ARN**<br>An **Amazon SNS topic ARN\*\*<br>text box appears.<br>Enter the Amazon Resource Name (ARN) for your<br>SNS topic. An SNS topic ARN has the following<br>format:<br>`arn:aws:sns:`region`:`account-id`:`topic-name``<br>You can find the SNS topic ARN in the Amazon SNS<br>console. |

7. Under **Events**, select one or both events that you want to send
   notifications:
   - To send a notification only when archive retrieval jobs are complete, select
     **Archive Retrieval Job Complete**.
   - To send a notification only when vault inventory jobs are complete, select **Vault
     Inventory Retrieval Job Complete**.
