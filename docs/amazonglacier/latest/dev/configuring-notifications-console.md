

 **This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/).

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/).

# Configuring Vault Notifications by Using the Amazon Glacier Console
<a name="configuring-notifications-console"></a>

This section describes how to configure vault notifications by using the Amazon Glacier console. When you configure notifications, you specify job-completion events that send a notification to an Amazon Simple Notification Service (Amazon SNS) topic. In addition to configuring notifications for the vault, you can also specify a topic to publish notifications to when you initiate a job. If your vault is configured to send a notification for a specific event and you also configure notifications in the job-initiation request, then two notifications are sent. 

**To configure a vault notification**

1. Sign in to the AWS Management Console and open the Amazon Glacier console at [https://console.aws.amazon.com/glacier/home](https://console.aws.amazon.com/glacier/home).

1. In the left navigation pane, choose **Vaults**.

1. In the **Vaults** list, choose a vault.

1. In the **Notifications** section, choose **Edit**.

1. On the **Event notifications** page, choose **Turn on notifications**.

1. In the **Notifications** section, choose one of the following Amazon Simple Notification Service (Amazon SNS) options, and then follow the corresponding steps:


<table>
<thead>
  <tr><th>Amazon SNS options</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><b>Create new SNS topic</b></td><td> <ol><li> Choose <b>Create new SNS topic</b>. </li><li> For <b>Topic name</b>, enter the name of the new topic. <br />Topic names can be up to 256 characters. Alphanumeric characters, hyphens (-), and underscores (_) are allowed. Topic names must be unique within the account and AWS Region. </li><li> (Optional) If you want to subscribe to the topic by using SMS messages, enter a name for <b>Display name</b>. <br />A display name can have up to 100 characters. </li></ol> </td></tr>
  <tr><td><b>Choose an existing SNS topic</b></td><td> <ol><li> Choose <b>Choose an existing SNS topic</b>. </li><li> Under <b>Specify SNS topic</b>, choose one of the following options: <ul><li> <b>Choose from your SNS topics</b> <br />An <b>SNS topic</b> dropdown list appears. <br /> Choose an existing topic from the dropdown list. </li><li> <b>Enter SNS topic ARN</b> <br />An <b>Amazon SNS topic ARN</b> text box appears.  <br />Enter the Amazon Resource Name (ARN) for your SNS topic. An SNS topic ARN has the following format: <br /> <code>arn:aws:sns:region:account-id:topic-name</code> <br />You can find the SNS topic ARN in the Amazon SNS console.  </li></ul> </li></ol> </td></tr>
</tbody>
</table>


1. Under **Events**, select one or both events that you want to send notifications:
   + To send a notification only when archive retrieval jobs are complete, select **Archive Retrieval Job Complete**. 
   + To send a notification only when vault inventory jobs are complete, select **Vault Inventory Retrieval Job Complete**. 