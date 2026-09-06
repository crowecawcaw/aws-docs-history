

# Deleting metadata tables
<a name="metadata-tables-delete-table"></a>

If you want to delete the metadata tables that you created for an Amazon S3 general purpose bucket, you can delete the metadata tables from your AWS managed table bucket. 

**Important**  
Deleting a table is permanent and can't be undone. Before deleting a table, make sure that you have backed up any important data.
Before you delete a metadata table, we recommend that you first delete the associated metadata table configuration on your general purpose bucket. For more information, see [Deleting metadata table configurations](metadata-tables-delete-configuration.md).

To delete your AWS managed table bucket, see [Deleting table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-delete.html) and [DeleteTableBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteTableBucket.html) in the *Amazon S3 API Reference*. Before you delete your AWS managed table bucket, we recommend that you first delete all metadata table configurations that are associated with this bucket. You must also first delete all metadata tables in the bucket. 

You can delete a metadata table by using the AWS Command Line Interface (AWS CLI), the AWS SDKs, or the Amazon S3 REST API.

## Delete a metadata table
<a name="delete-metadata-table-procedure"></a>

### Using the AWS CLI
<a name="delete-metadata-table-cli"></a>

To run the following commands, you must have the AWS CLI installed and configured. If you don't have the AWS CLI installed, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

Alternatively, you can run AWS CLI commands from the console by using AWS CloudShell. AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. For more information, see [What is CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) and [Getting started with AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/getting-started.html) in the *AWS CloudShell User Guide*.

**To delete a metadata table configuration by using the AWS CLI**

To use the following example commands, replace the `{{user input placeholders}}` with your own information. 

1. Use the following command to delete the metadata table from your AWS managed table bucket:

   ```
   aws s3tables delete-table \
   --table-bucket-arn arn:aws:s3tables:{{us-east-2}}:{{111122223333}}:bucket/aws-s3 \
   --namespace b_{{general-purpose-bucket-name}} \
   --name {{journal}} \
   --region {{us-east-2}}
   ```

1. To verify that the table was deleted, use the following command:

   ```
   aws s3tables get-table \
   --table-bucket-arn arn:aws:s3tables:{{us-east-2}}:{{111122223333}}:bucket/aws-s3 \
   --namespace b_{{general-purpose-bucket-name}} \
   --name {{journal}} \
   --region {{us-east-2}}
   ```

### Using the REST API
<a name="delete-metadata-table-rest-api"></a>

You can send REST requests to delete a metadata table configuration. For more information, see [DeleteTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteTable.html) in the *Amazon S3 API Reference*.

### Using the AWS SDKs
<a name="delete-metadata-table-sdk"></a>

You can use the AWS SDKs to delete a metadata table configuration in Amazon S3. For information, see the [list of supported SDKs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteTable.html#API_s3TableBuckets_DeleteTable_SeeAlso) in the *Amazon S3 API Reference*.