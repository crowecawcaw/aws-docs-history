**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Configuring Vault Notifications in Amazon Glacier

Retrieving anything from Amazon Glacier, such as an archive from a vault or a vault inventory, is a
two-step process.

1. Initiate a retrieval job.
2. After the job is completed, download the job output.
   You can set a notification configuration on a vault so that when a job is completed, a
   message is sent to an Amazon Simple Notification Service (Amazon SNS) topic.

###### Topics

- [Configuring Vault Notifications in
  Amazon Glacier: General Concepts](#configuring-notifications.general "#configuring-notifications.general")
- [Configuring Vault Notifications in Amazon Glacier Using the
  AWS SDK for Java](configuring-notifications-sdk-java.md "configuring-notifications-sdk-java.md")
- [Configuring Vault Notifications in Amazon Glacier Using the
  AWS SDK for .NET](configuring-notifications-sdk-dotnet.md "configuring-notifications-sdk-dotnet.md")
- [Configuring Vault Notifications in Amazon Glacier Using the
  REST API](configuring-notifications-rest-api.md "configuring-notifications-rest-api.md")
- [Configuring Vault Notifications by Using the
  Amazon Glacier Console](configuring-notifications-console.md "configuring-notifications-console.md")
- [Configuring Vault Notifications Using the
  AWS Command Line Interface](configuring-notifications-cli.md "configuring-notifications-cli.md")

## Configuring Vault Notifications in

Amazon Glacier: General Concepts

A Amazon Glacier retrieval job request is run asynchronously. You must wait until Amazon Glacier
completes the job before you can get its output. You can periodically poll Amazon Glacier to
determine the job status, but that is not an optimal approach. Amazon Glacier also supports
notifications. When a job is completed, the job can post a message to an Amazon Simple Notification Service
(Amazon SNS) topic. Using this feature requires you to set a notification configuration on
the vault. In the configuration, you identify one or more events and an Amazon SNS topic to
which you want Amazon Glacier to send a message when the event occurs.

Amazon Glacier defines events specifically related to job completion
(`ArchiveRetrievalCompleted`, `InventoryRetrievalCompleted`)
that you can add to the vault's notification configuration. When a specific job is
completed, Amazon Glacier publishes a notification message to the SNS topic.

The notification configuration is a JSON document as shown in the following example.

```
{
   "SNSTopic": "arn:aws:sns:us-west-2:012345678901:mytopic",
   "Events": ["ArchiveRetrievalCompleted", "InventoryRetrievalCompleted"]
}
```

You can configure only one Amazon SNS topic for a vault.

###### Note

Adding a notification configuration to a vault causes Amazon Glacier to send a
notification each time the event specified in the notification configuration occurs.
You can also optionally specify an Amazon SNS topic in each job initiation request. If
you add both the notification configuration on the vault and also specify an Amazon SNS
topic in your initiate job request, Amazon Glacier sends both notifications.

The job completion message Amazon Glacier sends include information such as the type of job
(`InventoryRetrieval`, `ArchiveRetrieval`), job completion
status, SNS topic name, job status code, and the vault ARN. The following is an example
notification Amazon Glacier sent to an SNS topic after an `InventoryRetrieval` job
is completed.

```
{
 "Action": "InventoryRetrieval",
 "ArchiveId": null,
 "ArchiveSizeInBytes": null,
 "Completed": true,
 "CompletionDate": "2012-06-12T22:20:40.790Z",
 "CreationDate": "2012-06-12T22:20:36.814Z",
 "InventorySizeInBytes":11693,
 "JobDescription": "my retrieval job",
 "JobId":"HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID",
 "SHA256TreeHash":null,
 "SNSTopic": "arn:aws:sns:us-west-2:012345678901:mytopic",
 "StatusCode":"Succeeded",
 "StatusMessage": "Succeeded",
 "VaultARN": "arn:aws:glacier:us-west-2:012345678901:vaults/examplevault"
}
```

If the `Completed` field is true, you must also check the
`StatusCode` to check if the job completed successfully or failed.

###### Note

The Amazon SNS topic must allow the vault to publish a notification. By default, only the Amazon SNS
topic owner can publish a message to the topic. However, if the Amazon SNS topic and the
vault are owned by different AWS accounts, then you must configure the Amazon SNS topic
to accept publications from the vault. You can configure the Amazon SNS topic policy in
the Amazon SNS console.

For more information about Amazon SNS, see [Getting
Started with Amazon SNS](../../../sns/latest/gsg/Welcome.md "../../../sns/latest/gsg/Welcome.md").
