# Troubleshooting S3 Metadata

Use the following information to help you diagnose and fix common issues that you might encounter when
working with Amazon S3 Metadata.

## I'm unable to delete my AWS managed table bucket and metadata tables

Before you can delete a metadata table, you must first delete the associated metadata table
configuration on your general purpose bucket. For more information, see [Deleting metadata table configurations](metadata-tables-delete-configuration.md "metadata-tables-delete-configuration.md").

Before you can delete your AWS managed table bucket, you must delete all metadata table
configurations that are associated with this bucket and all metadata tables in the bucket. For more
information, see [Deleting metadata table configurations](metadata-tables-delete-configuration.md "metadata-tables-delete-configuration.md") and [Deleting metadata tables](metadata-tables-delete-table.md "metadata-tables-delete-table.md").

## I'm unable to set or change the encryption settings for my AWS managed metadata table

When you create your metadata table configuration, you can choose to encrypt your AWS managed
metadata tables with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS). If you choose to use
SSE-KMS, you must provide a customer managed KMS key in the same Region as your general purpose
bucket. You can set the encryption type for your tables only during table creation. After an AWS
managed table is created, you can't change its encryption setting. To specify SSE-KMS for your metadata
tables, you must have certain permissions. For more information, see [Permissions for SSE-KMS](metadata-tables-permissions.md#metadata-kms-permissions "metadata-tables-permissions.md#metadata-kms-permissions").

The encryption setting for a metadata table takes precedence over the default bucket-level
encryption setting. If you don't specify encryption for a table, it will inherit the default encryption
setting from the bucket.

By default, AWS managed table buckets are encrypted with server-side encryption using Amazon S3 managed
keys (SSE-S3). After you create your first metadata configuration, you can set the default encryption
setting for the AWS managed table bucket to use server-side encryption with AWS Key Management Service (AWS KMS) keys
(SSE-KMS). For more information, see [Encryption for AWS managed table buckets](s3-tables-aws-managed-buckets.md#aws-managed-buckets-encryption "s3-tables-aws-managed-buckets.md#aws-managed-buckets-encryption") and [Specifying server-side encryption with AWS KMS keys (SSE-KMS) in table buckets](s3-tables-kms-specify.md "s3-tables-kms-specify.md").

## When I try to re-create my metadata table configuration, I get an error

Deleting a metadata table configuration deletes only the configuration. The AWS managed table
bucket and your metadata tables still exist, even if you delete the metadata table configuration.

If you delete your metadata table configuration and want to re-create a configuration for the same
general purpose bucket, you must first manually delete the old journal and inventory tables from your
AWS managed table bucket. Otherwise, creating the new metadata table configuration fails because those
tables already exist.

To delete your metadata tables, see [Deleting metadata tables](metadata-tables-delete-table.md "metadata-tables-delete-table.md").

## I can't enable an inventory table on my configuration

If you created your S3 Metadata configuration before July 15, 2025, you can't enable an inventory
table on that configuration. We recommend that you delete and re-create your configuration so that you
can create an inventory table and expire journal table records. For more information, see [Enabling inventory tables on metadata configurations created before July 15, 2025](metadata-tables-create-configuration.md#metadata-tables-migration "metadata-tables-create-configuration.md#metadata-tables-migration").

## I can't enable journal table record expiration on my configuration

If you created your S3 Metadata configuration before July 15, 2025, you can't enable journal table
record expiration on that configuration. We recommend that you delete and re-create your configuration
so that you can expire journal table records and create an inventory table. For more information, see
[Enabling inventory tables on metadata configurations created before July 15, 2025](metadata-tables-create-configuration.md#metadata-tables-migration "metadata-tables-create-configuration.md#metadata-tables-migration").

## I can't query my metadata tables

If you're unable to query your metadata tables, check the following:

- When you're using Amazon Athena or Amazon Redshift to query your metadata tables, you must surround your
  metadata table namespace names in quotation marks (`"`) or backticks (```),
  otherwise the query might not work.
- When using Apache Spark on Amazon EMR or other third-party engines to query your
  metadata tables, we recommend that you use the Amazon S3 Tables Iceberg REST endpoint.
  Your query might not run successfully if you don't use this endpoint. For more information, see
  [Accessing tables using the Amazon S3 Tables Iceberg REST endpoint](s3-tables-integrating-open-source.md "s3-tables-integrating-open-source.md").
- Make sure that you have the appropriate AWS Identity and Access Management (IAM) permissions to query metadata tables.
  For more information, see [Permissions for querying metadata tables](metadata-tables-bucket-query-permissions.md "metadata-tables-bucket-query-permissions.md").
- If you're using Amazon Athena and receive errors when you try to run your queries, do the
  following:
  - If you receive the error **`"Insufficient permissions to execute the query. Principal
does not have any privilege on specified resource"`** when you try to run a query in
    Athena, you must be granted the necessary Lake Formation permissions on the table. For more information, see
    [Granting Lake Formation permission on a table or database](grant-permissions-tables.md#grant-lf-table "grant-permissions-tables.md#grant-lf-table").
  - If you receive the error **`"Iceberg cannot access the requested resource"`**
    when you try to run the query, go to the AWS Lake Formation console and make sure that you've granted yourself
    permissions on the table bucket catalog and database (namespace) that you created. Don't specify a
    table when granting these permissions. For more information, see [Granting Lake Formation permission on a table or database](grant-permissions-tables.md#grant-lf-table "grant-permissions-tables.md#grant-lf-table").

## I'm receiving 405 errors when I try to use certain S3 Metadata AWS CLI commands and API operations

Calling the V1 `GetBucketMetadataTableConfiguration` API operation or using the
`get-bucket-metadata-table-configuration` AWS Command Line Interface (AWS CLI) command against a V2 metadata
table configuration results in an HTTP `405 Method Not Allowed` error. Likewise, calling the
V1 `DeleteBucketMetadataTableConfiguration` API operation or using the
`delete-bucket-metadata-table-configuration` AWS CLI command also causes a 405 error.

You can use the V2 `GetBucketMetadataConfiguration` API operation or the
`get-bucket-metadata-configuration` AWS CLI command against a V1 or V2 metadata table
configuration. Likewise, you can use the V2 `DeleteBucketMetadataConfiguration` API
operation or the `delete-bucket-metadata-configuration` AWS CLI command against a V1 or V2
metadata table configuration.

We recommend updating your processes to use the new V2 API operations
(`CreateBucketMetadataConfiguration`, `GetBucketMetadataConfiguraion`, and
`DeleteBucketMetadataConfiguration`) instead of the V1 API operations. For more information
about migrating from V1 of S3 Metadata to V2, see [Enabling inventory tables on metadata configurations created before July 15, 2025](metadata-tables-create-configuration.md#metadata-tables-migration "metadata-tables-create-configuration.md#metadata-tables-migration").

To determine whether your configuration is V1 or V2, you can look at the following attribute of your
`GetBucketMetadataConfiguration` API response. An AWS managed bucket type
(`"aws"`) indicates a V2 configuration, and a customer-managed bucket type
(`"customer"`) indicates a V1 configuration.

```
"MetadataTableConfigurationResult": {
            "TableBucketType": ["aws" | "customer"]
```

For more information, see [Viewing metadata table configurations](metadata-tables-view-configuration.md "metadata-tables-view-configuration.md").
