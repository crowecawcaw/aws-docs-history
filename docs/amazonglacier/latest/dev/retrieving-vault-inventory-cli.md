**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Downloading a Vault Inventory in Amazon Glacier

Using the AWS Command Line Interface

Follow these steps to download a vault inventory in Amazon Glacier (Amazon Glacier) using the
AWS Command Line Interface (AWS CLI).

###### Topics

- [(Prerequisite) Setting Up the AWS CLI](#Creating-Vaults-CLI-Setup "#Creating-Vaults-CLI-Setup")
- [Example: Downloading a
  Vault Inventory Using the AWS CLI](#Retrieving-Vault-Inventory-CLI-Implementation "#Retrieving-Vault-Inventory-CLI-Implementation")

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

## Example: Downloading a

Vault Inventory Using the AWS CLI

1. Use the `initiate-job` command to start an inventory retrieval
   job.

```
aws glacier initiate-job --vault-name `awsexamplevault` --account-id `111122223333` --job-parameters='{"Type": "inventory-retrieval"}'
```

Expected output:

```

{
    "location": "/`111122223333`/vaults/`awsexamplevault`/jobs/`*** jobid ***`",
    "jobId": "`*** jobid ***`"
}

```

2. Use the `describe-job` command to check status of the previous
   retrieval job.

```
aws glacier describe-job --vault-name `awsexamplevault` --account-id `111122223333` --job-id `*** jobid ***`
```

Expected output:

```

{
    "InventoryRetrievalParameters": {
        "Format": "JSON"
    },
    "VaultARN": "`*** vault arn ***`",
    "Completed": false,
    "JobId": "`*** jobid ***`",
    "Action": "InventoryRetrieval",
    "CreationDate": "`*** job creation date ***`",
    "StatusCode": "InProgress"
}

```

3. Wait for the job to complete.

You must wait until the job output is ready for you to download. The job ID
does not expire for at least 24 hours after Amazon Glacier completes the job. If you
have either set a notification configuration on the vault, or specified an
Amazon Simple Notification Service (Amazon SNS) topic when you initiated the job, Amazon Glacier sends a message to
the topic after it completes the job.

You can set the notification configuration for specific events on the vault. For more
information, see [Configuring Vault Notifications in Amazon Glacier](configuring-notifications.md "configuring-notifications.md"). Amazon Glacier sends a message to
the specified SNS topic anytime the specific events occur. 4. When it's complete, use the `get-job-output` command to download the retrieval
job to the file `output.json`.

```
aws glacier get-job-output --vault-name `awsexamplevault` --account-id `111122223333` --job-id `*** jobid ***` output.json
```

This command produces a file with the following fields.

```

{
"VaultARN":"arn:aws:glacier:`region`:`111122223333`:vaults/`awsexamplevault`",
"InventoryDate":"`*** job completion date ***`",
"ArchiveList":[
{"ArchiveId":"`*** archiveid ***`",
"ArchiveDescription":"`*** archive description (if set) ***`",
"CreationDate":"`*** archive creation date ***`",
"Size":"`*** archive size (in bytes) ***`",
"SHA256TreeHash":"`*** archive hash ***`"
}
{"ArchiveId":
...
]}

```
