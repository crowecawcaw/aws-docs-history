# Viewing metadata table configurations

If you've created a metadata table configuration for a general purpose bucket, you can view
 information about the configuration, such as whether an inventory table has been enabled, or whether
 journal table record expiration has been enabled. You can also view the status of your journal and
 inventory tables. 

You can view your metadata table configuration for a general purpose bucket by using the Amazon S3
 console, the AWS Command Line Interface (AWS CLI), the AWS SDKs, or the Amazon S3 REST API.


## View a metadata table
 configuration


###### To view a metadata table configuration

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. Choose the general purpose bucket that contains the metadata table configuration that you
 want to view.
4. On the bucket's details page, choose the **Metadata** tab.
5. On the **Metadata** tab, scroll down to the **Metadata
 configuration** section. In the **Journal table** and
 **Inventory table** sections, you can view various information for these
 configurations, such as their Amazon Resource Names (ARNs), the status of your tables, and
 whether you've enabled journal table record expiration or an inventory table.
To run the following commands, you must have the AWS CLI installed and configured. If you don’t
 have the AWS CLI installed, see [Install or update to the latest version
 of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html") in the *AWS Command Line Interface User Guide*.

Alternatively, you can run AWS CLI commands from the console by using AWS CloudShell. AWS CloudShell is a
 browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. For more
 information, see [What
 is CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html") and [Getting started with AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/getting-started.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/getting-started.html") in
 the *AWS CloudShell User Guide*.

###### To view a metadata table configuration by using the AWS CLI

To use the following example command, replace the ``user input
 placeholders`` with your own information. 

1. Use the following command to view the metadata table configuration for your general
 purpose bucket (for example, ``amzn-s3-demo-bucket``):



```
aws s3api get-bucket-metadata-configuration \
--bucket `amzn-s3-demo-bucket` \
--region `us-east-2`
```
2. View the output of this command to see the status of your metadata table configuration.
 For example:



```
{
    "GetBucketMetadataConfigurationResult": {
        "MetadataConfigurationResult": {
            "DestinationResult": {
                "TableBucketType": "aws",
                "TableBucketArn": "arn:aws:s3tables:us-east-2:111122223333:bucket/aws-managed-s3-111122223333-us-east-2",
                "TableNamespace": "`b_general-purpose-bucket-name`"
            },
            "JournalTableConfigurationResult": {
                "TableStatus": "ACTIVE",
                "TableName": "journal",
                "TableArn": "arn:aws:s3tables:us-east-2:111122223333:bucket/aws-managed-s3-111122223333-us-east-2/table/0f01234c-fe7a-492f-a4c7-adec3864ea85",
                "EncryptionConfiguration": {
                    "SseAlgorithm": "AES256"
                },
                "RecordExpiration": {
                    "Expiration": "ENABLED",
                    "Days": 10
                }
            },
            "InventoryTableConfigurationResult": {
                "ConfigurationState": "ENABLED",
                "TableStatus": "BACKFILL_COMPLETE",
                "TableName": "inventory",
                "TableArn": "arn:aws:s3tables:us-east-2:111122223333:bucket/aws-managed-s3-111122223333-us-east-2/table/e123456-b876-4e5e-af29-bb055922ee4d",
                "EncryptionConfiguration": {
                    "SseAlgorithm": "AES256"
                }
            }
        }
    }
}
```
You can send REST requests to view a metadata table configuration. For more information, see
 [GetBucketMetadataTableConfiguration](../API/API_GetBucketMetadataTableConfiguration.md "../API/API_GetBucketMetadataTableConfiguration.md").

###### Note

You can use the V2 `GetBucketMetadataConfiguration` API operation with V1 or V2
 metadata table configurations. However, if you try to use the V1
 `GetBucketMetadataTableConfiguration` API operation with V2 configurations, you
 will receive an HTTP `405 Method Not Allowed` error.

You can use the AWS SDKs to view a metadata table configuration in Amazon S3. For information,
 see the [list of supported
 SDKs](../API/API_GetBucketMetadataTableConfiguration.md#API_GetBucketMetadataTableConfiguration_SeeAlso "../API/API_GetBucketMetadataTableConfiguration.md#API_GetBucketMetadataTableConfiguration_SeeAlso").
