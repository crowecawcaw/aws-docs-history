# Deleting metadata tables

If you want to delete the metadata tables that you created for an Amazon S3 general purpose bucket, you
can delete the metadata tables from your AWS managed table bucket.

###### Important

- Deleting a table is permanent and can't be undone. Before deleting a table, make sure that you
  have backed up any important data.
- Before you delete a metadata table, we recommend that you first delete the associated metadata
  table configuration on your general purpose bucket. For more information, see [Deleting metadata table
  configurations](metadata-tables-delete-configuration.md "metadata-tables-delete-configuration.md").
  To delete your AWS managed table bucket, see [Deleting table buckets](s3-tables-buckets-delete.md "s3-tables-buckets-delete.md") and
  [DeleteTableBucket](../API/API_s3TableBuckets_DeleteTableBucket.md "../API/API_s3TableBuckets_DeleteTableBucket.md") in the _Amazon S3 API
  Reference_. Before you delete your AWS managed table bucket, we recommend that you first
  delete all metadata table configurations that are associated with this bucket. You must also first
  delete all metadata tables in the bucket.

You can delete a metadata table by using the AWS Command Line Interface (AWS CLI), the AWS SDKs, or the
Amazon S3 REST API.

## Delete a metadata table

To run the following commands, you must have the AWS CLI installed and configured. If
you don’t have the AWS CLI installed, see [Install or update to the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

Alternatively, you can run AWS CLI commands from the console by using AWS CloudShell.
AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from
the AWS Management Console. For more information, see [What is CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") and
[Getting started with AWS CloudShell](../../../cloudshell/latest/userguide/getting-started.md "../../../cloudshell/latest/userguide/getting-started.md") in the
_AWS CloudShell User Guide_.

###### To delete a metadata table configuration by using the AWS CLI

To use the following example commands, replace the `user input
 placeholders` with your own information.

1. Use the following command to delete the metadata table from your AWS managed table
   bucket:

```
aws s3tables delete-table \
--table-bucket-arn arn:aws:s3tables:`us-east-2`:`111122223333`:bucket/aws-s3 \
--namespace b_`general-purpose-bucket-name` \
--name `journal` \
--region `us-east-2`
```

2. To verify that the table was deleted, use the following command:

```
aws s3tables get-table \
--table-bucket-arn arn:aws:s3tables:`us-east-2`:`111122223333`:bucket/aws-s3 \
--namespace b_`general-purpose-bucket-name` \
--name `journal` \
--region `us-east-2`
```

You can send REST requests to delete a metadata table configuration. For more
information, see [DeleteTable](../API/API_s3TableBuckets_DeleteTable.md "../API/API_s3TableBuckets_DeleteTable.md") in the _Amazon S3 API
Reference_.

You can use the AWS SDKs to delete a metadata table configuration in Amazon S3. For
information, see the [list of supported SDKs](../API/API_s3TableBuckets_DeleteTable.md#API_s3TableBuckets_DeleteTable_SeeAlso "../API/API_s3TableBuckets_DeleteTable.md#API_s3TableBuckets_DeleteTable_SeeAlso") in the _Amazon S3 API
Reference_.
