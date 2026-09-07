

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Configure data retention for AWS Wickr
<a name="configure-data-retention"></a>

To configure data retention for your AWS Wickr network, you must deploy the data retention bot Docker image to a container on a host, such as a local computer or an instance in Amazon Elastic Compute Cloud (Amazon EC2). After the bot is deployed, you can configure it to store data locally or in an Amazon Simple Storage Service (Amazon S3) bucket. You can also configure the data retention bot to use other AWS services like AWS Secrets Manager (Secrets Manager), Amazon CloudWatch (CloudWatch), Amazon Simple Notification Service (Amazon SNS), and AWS Key Management Service (AWS KMS). The following topics describe how to configure and run the data retention bot for your Wickr network.

For production deployments of the Wickr Data Retention (DR) Bot, AWS recommends deploying to Amazon EC2/Amazon EBS with messages archived in Amazon S3 and the following minimum instance and storage sizing:
+ Instance type: m8i.large (8GiB RAM, 2vCPUs)
+ Storage: 1 TB Amazon EBS volume
+ Deployment: One DR Bot instance per Amazon EC2 host

For more information on Amazon EBS, see [Amazon EBS snapshot lifecycle](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshot-lifecycle.html) in the *Amazon EBS User Guide*.

**Topics**
+ [Prerequisites to configure data retention for AWS Wickr](#data-retention-prerequisites)
+ [Password for data retention bot in AWS Wickr](data-retention-password.md)
+ [Storage options for AWS Wickr network](data-retention-storage-options.md)
+ [Environment variables to configure data retention bot in AWS Wickr](data-retention-bot-env-variables.md)
+ [Secrets Manager values for AWS Wickr](data-retention-aws-secret-values.md)
+ [IAM policy to use data retention with AWS services](data-retention-aws-services.md)
+ [Start the data retention bot for your Wickr network](starting-data-retention-bot.md)
+ [Stop the data retention bot for your Wickr network](stopping-data-retention-bot.md)

**Note**  
Deactivating the docker bot will reset it. To reactivate, you must re-run the docker bot installation process using the bot password you configured during initial setup.

## Prerequisites to configure data retention for AWS Wickr
<a name="data-retention-prerequisites"></a>

This assumes you have an Amazon EC2 instance running already with the minimum storage requirements listed above and your VPC is able to reach the Wickr messaging endpoint:

 `com.amazonaws.{{region}}.wickr-messaging` — the bot receives messages from the Wickr messaging service.

Before you get started, complete the following procedure to enable data retention in the console.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **Network polices**.

1. On the **Network polices** page, in the **Data Retention** section, select **Edit**.

1. On the **Edit data retention** page, follow Steps 1 and 2.

1. Start your data retention bot. For more information, see [ Start the data retention bot for your Wickr network](https://docs.aws.amazon.com/wickr/latest/adminguide/starting-data-retention-bot.html).

1. In the **Configure your data retention server** section, copy the **Username** and **Initial Password**. Configure your data retention bot with the username and initial password by following, [ Password for data retention bot in AWS Wickr](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention-password.html).

1. Select the **Enable data retention** checkbox, then choose **Save changes**.

**Note**  
The DR Bot is validated for sustained processing at approximately 11,000 messages per hour (\~3 messages/second). For workloads that consistently exceed this throughput or are expected to surpass 1.5 million messages in a single processing run, additional scaling strategies should be evaluated.

For Disaster Recovery, we recommend Snapshot Lifecycles on the Amazon EBS volume(s) and Amazon S3 Cross-Region Replication. To configure how often messages are sent to Amazon S3, you can set the environment variable WICKRIO\_COMP\_FILESIZE or `WICKRIO_COMP_TIMEROTATE` to rotate on size or time. Message logs and file attachments will get delivered into the same prefix in the same bucket. For more information, see [Environment variables to configure data retention bot in AWS Wickr](data-retention-bot-env-variables.md).