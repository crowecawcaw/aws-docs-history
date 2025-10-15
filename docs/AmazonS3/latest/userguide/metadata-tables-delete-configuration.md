# Deleting metadata table
 configurations

If you want to stop updating the metadata table configuration for an Amazon S3 general purpose bucket,
 you can delete the metadata table configuration that's attached to your bucket. Deleting a metadata
 table configuration deletes only the configuration. The AWS managed table bucket and your metadata
 tables still exist, even if you delete the metadata table configuration. However, the metadata tables
 will no longer be updated.

###### Note

If you delete your metadata table configuration and want to re-create a configuration for the same
 general purpose bucket, you must first manually delete the old journal and inventory tables from your
 AWS managed table bucket. Otherwise, creating the new metadata table configuration fails because
 those tables already exist. To delete your metadata tables, see [Deleting metadata tables](metadata-tables-delete-table.md "metadata-tables-delete-table.md"). 

To delete your metadata tables, see [Delete a metadata table](metadata-tables-delete-table.md#delete-metadata-table-procedure "metadata-tables-delete-table.md#delete-metadata-table-procedure"). To delete
 your table bucket, see [Deleting table buckets](s3-tables-buckets-delete.md "s3-tables-buckets-delete.md") and
 [DeleteTableBucket](../API/API_s3TableBuckets_DeleteTableBucket.md "../API/API_s3TableBuckets_DeleteTableBucket.md") in the *Amazon S3 API
 Reference*. 

You can delete a metadata table configuration by using the Amazon S3 console, the AWS Command Line Interface
 (AWS CLI), the AWS SDKs, or the Amazon S3 REST API.


## Delete a metadata table
 configuration


###### To delete a metadata table configuration

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose
 buckets**.
3. Choose the general purpose bucket that you want to remove a metadata table
 configuration from.
4. On the bucket's details page, choose the **Metadata** tab.
5. On the **Metadata** tab, choose
 **Delete**.
6. In the **Delete metadata configuration** dialog box, enter
 `confirm` to confirm that you want to delete the
 configuration. Then choose **Delete**.
To run the following commands, you must have the AWS CLI installed and configured. If
 you don’t have the AWS CLI installed, see [Install or update to the
 latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html") in the *AWS Command Line Interface User Guide*.

Alternatively, you can run AWS CLI commands from the console by using AWS CloudShell.
 AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from
 the AWS Management Console. For more information, see [What is CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html") and
 [Getting started with AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/getting-started.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/getting-started.html") in the
 *AWS CloudShell User Guide*.

###### To delete a metadata table configuration by using the AWS CLI

To use the following example commands, replace the ``user input
 placeholders`` with your own information. 

1. Use the following command to delete the metadata table configuration from your general
 purpose bucket (for example, ``amzn-s3-demo-bucket``):



```
aws s3api delete-bucket-metadata-configuration \
--bucket `amzn-s3-demo-bucket` \
--region `us-east-2`
```
2. To verify that the configuration was deleted, use the following command:



```
aws s3api get-bucket-metadata-configuration \
--bucket `amzn-s3-demo-bucket` \
--region `us-east-2`
```
You can send REST requests to delete a metadata table configuration. For more information, see
 [DeleteBucketMetadataConfiguration](../API/API_DeleteBucketMetadataConfiguration.md "../API/API_DeleteBucketMetadataConfiguration.md").

###### Note

You can use the V2 `DeleteBucketMetadataConfiguration` API operation with V1 or
 V2 metadata table configurations. However, if you try to use the V1
 `DeleteBucketMetadataTableConfiguration` API operation with V2 configurations, you
 will receive an HTTP `405 Method Not Allowed` error.

You can use the AWS SDKs to delete a metadata table configuration in Amazon S3. For
 information, see the [list of supported SDKs](../API/API_DeleteBucketMetadataConfiguration.md#API_DeleteBucketMetadataConfiguration_SeeAlso "../API/API_DeleteBucketMetadataConfiguration.md#API_DeleteBucketMetadataConfiguration_SeeAlso").
