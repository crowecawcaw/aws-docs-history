**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Configuring Vault Notifications Using the

AWS Command Line Interface

This section describes how to configure vault notifications using the AWS Command Line Interface. When you
configure notifications, you specify job completion events that trigger notification to an
Amazon Simple Notification Service (Amazon SNS) topic. In addition to configuring notifications for the vault, you can
also specify a topic to publish notification to when you initiate a job. If your vault is
configured to notify for a specific event and you specify notification in the job initiation
request, then two notifications are sent.

Follow these steps to configure vault notification using the AWS CLI.

###### Topics

- [(Prerequisite) Setting Up the AWS CLI](#Creating-Vaults-CLI-Setup "#Creating-Vaults-CLI-Setup")
- [Example: Configure
  Vault Notifications Using the AWS CLI](#Configure-Vault-Notifications-CLI-Implementation "#Configure-Vault-Notifications-CLI-Implementation")

## (Prerequisite) Setting Up the AWS CLI

1. Download and configure the AWS CLI. For instructions, see the following topics in the
   _AWS Command Line Interface User Guide_:

[Installing the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md")

[Configuring the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") 2. Verify your AWS CLI setup by entering the following commands at the command prompt. These
commands don't provide credentials explicitly, so the credentials of the default
profile are used.

    * Try using the help command.



    ```
    aws help
    ```
    * To get a list of Amazon Glacier vaults on the configured account, use the `list-vaults` command. Replace `123456789012` with your AWS account ID.



    ```
    aws glacier list-vaults --account-id `123456789012`
    ```
    * To see the current configuration data for the AWS CLI, use the `aws
     configure list` command.



    ```
    aws configure list
    ```

## Example: Configure

Vault Notifications Using the AWS CLI

1. Use the `set-vault-notifications` command to configure
   notifications that will be sent when specific events happen to a vault. By
   default, you don't get any notifications.

```
aws glacier set-vault-notifications --vault-name `examplevault` --account-id `111122223333` --vault-notification-config file://notificationconfig.json
```

2. The notification configuration is a JSON document as shown in the following
   example.

```
{
   "SNSTopic": "arn:aws:sns:us-west-2:012345678901:mytopic",
   "Events": ["ArchiveRetrievalCompleted", "InventoryRetrievalCompleted"]
}
```

For more information about using Amazon SNS topics for Amazon Glacier see, [Configuring Vault Notifications in Amazon Glacier: General
Concepts](configuring-notifications.md#configuring-notifications.general "configuring-notifications.md#configuring-notifications.general")

For more information about Amazon SNS, see [Getting Started with Amazon SNS](../../../sns/latest/gsg/Welcome.md "../../../sns/latest/gsg/Welcome.md").
