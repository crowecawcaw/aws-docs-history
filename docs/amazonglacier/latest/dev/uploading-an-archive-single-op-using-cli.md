**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Uploading an Archive in a Single Operation Using the AWS Command Line Interface

You can upload an archive in Amazon Glacier (Amazon Glacier) using the AWS Command Line Interface (AWS CLI).

###### Topics

- [(Prerequisite) Setting Up the AWS CLI](#Creating-Vaults-CLI-Setup "#Creating-Vaults-CLI-Setup")
- [Example: Upload an Archive Using the AWS CLI](#Uploading-Archives-CLI-Implementation "#Uploading-Archives-CLI-Implementation")

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

## Example: Upload an Archive Using the AWS CLI

In order to upload an archive you must have a vault created. For
more information about creating vaults, see [Creating a Vault in Amazon Glacier](creating-vaults.md "creating-vaults.md").

1. Use the `upload-archive` command to add an archive to an existing
   vault. In the below example replace the `vault name` and `account ID`. For the
   `body` parameter specify a path to the file you wish to upload.

```
aws glacier upload-archive --vault-name `awsexamplevault` --account-id `123456789012` --body `archive.zip`
```

2. Expected output:

```
{
    "archiveId": "kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw",
    "checksum": "969fb39823836d81f0cc028195fcdbcbbe76cdde932d4646fa7de5f21e18aa67",
    "location": "/123456789012/vaults/awsexamplevault/archives/kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw"
}
```

When finished the command will output the archive ID, checksum, and location in Amazon Glacier. For
more information about the upload-archive command, see
[upload-archive](../../../cli/latest/reference/glacier/upload-archive.md "../../../cli/latest/reference/glacier/upload-archive.md") in the _AWS CLI Command Reference_.
