# Creating metadata table configurations

To generate and store Amazon S3 Metadata in fully managed Apache Iceberg metadata tables,
you create a metadata table configuration for your general purpose bucket. Amazon S3 is designed to
continuously update the metadata tables to reflect the latest changes to your data as long as the
configuration is active on the bucket. Additionally, Amazon S3 continuously optimizes your metadata tables to
help reduce storage costs and improve analytics query performance.

For each general purpose bucket, you can create a metadata table configuration that contains two
complementary metadata tables:

- **Journal table** – By default, your metadata table
  configuration contains a _journal table_, which captures events
  that occur for the objects in your bucket. The journal table records changes made to your data in
  near real time, helping you to identify new data uploaded to your bucket, track recently deleted
  objects, monitor lifecycle transitions, and more. The journal table records new objects and updates
  to your objects and their metadata (those updates that require either a `PUT` or a
  `DELETE` operation).

The journal table captures metadata only for change events (such as uploads, updates, and
deletes) that happen after you create your metadata table configuration. Because this table is
queryable, you can audit the changes to your bucket through simple SQL queries.

The journal table is required for each metadata table configuration. (In the initial release of
S3 Metadata, the journal table was referred to as "the metadata table.")

For more information about what data is stored in journal tables, see [S3 Metadata journal tables schema](metadata-tables-schema.md "metadata-tables-schema.md").

To help minimize your storage costs, you can choose to enable journal table record expiration.
For more information, see [Expiring journal table records](metadata-tables-expire-journal-table-records.md "metadata-tables-expire-journal-table-records.md").

- **Live inventory table** – Optionally, you can add a
  _live inventory table_ to your metadata table configuration. The
  live inventory table provides a simple, queryable inventory of all the objects and their versions in
  your bucket so that you can determine the latest state of your data.

You can use the live inventory table to simplify and speed up business workflows and big data
jobs by identifying objects that you want to process for various workloads. For example, you can
query the live inventory table to find all objects stored in a particular storage class, all objects
with certain tags, all objects that aren't encrypted with server-side encryption using AWS Key Management Service
(AWS KMS) keys (SSE-KMS), and more.

When you enable the live inventory table for your metadata table configuration, the table goes
through a process known as _backfilling_, during which Amazon S3 scans
your general purpose bucket to retrieve the initial metadata for all objects that exist in the
bucket. Depending on the number of objects in your bucket, this process can take minutes (minimum 15 minutes) to hours.
When the backfilling process is finished, the status of your live inventory table changes from
**Backfilling** to **Active**. After backfilling is completed,
updates to your objects are typically reflected in the live inventory table within one hour.

You're charged for backfilling your live inventory table. If your general purpose bucket has
more than one billion objects, you're also charged a monthly fee for your live inventory table. For
more information, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

For more information about what data is stored in live inventory tables, see [S3 Metadata live inventory tables schema](metadata-tables-inventory-schema.md "metadata-tables-inventory-schema.md").
Metadata tables have the following Amazon Resource Name (ARN) format, which includes the table ID of
the metadata table:

`arn:aws:s3tables:`region-code`:`account-id`:bucket/aws-s3/table/`table-id``

For example, a metadata table in the US East (N. Virginia) Region would have an ARN like the
following:

`arn:aws:s3tables:us-east-1:111122223333:bucket/aws-s3/table/a12bc345-67d8-912e-3456-7f89123g4h56`

Journal tables have the name `journal`, and live inventory tables have the name
`inventory`.

When you create your metadata table configuration, your metadata tables are stored in an AWS
managed table bucket. All metadata table configurations in your account and in the same Region are
stored in a single AWS managed table bucket. These AWS managed table buckets are named
`aws-s3` and have the following Amazon Resource Name (ARN) format:

`arn:aws:s3tables:`region`:`account_id`:bucket/aws-s3`

For example, if your account ID is 123456789012 and your general purpose bucket is in
US East (N. Virginia) (`us-east-1`), your AWS managed table bucket is also created
in US East (N. Virginia) (`us-east-1`) and has the following ARN:

`arn:aws:s3tables:`us-east-1`:123456789012:bucket/aws-s3`

By default, AWS managed table buckets are encrypted with server-side encryption using Amazon S3 managed
keys (SSE-S3). After you create your first metadata configuration, you can set the default encryption
setting for the AWS managed table bucket to use server-side encryption with AWS Key Management Service (AWS KMS) keys
(SSE-KMS). For more information, see [Encryption for AWS managed table buckets](s3-tables-aws-managed-buckets.md#aws-managed-buckets-encryption "s3-tables-aws-managed-buckets.md#aws-managed-buckets-encryption") and [Specifying server-side encryption with AWS KMS keys (SSE-KMS) in table buckets](s3-tables-kms-specify.md "s3-tables-kms-specify.md").

Within your AWS managed table bucket, the metadata tables for your configuration are typically
stored in a namespace with the following naming format:

`b_`general-purpose-bucket-name``

For more information about metadata table namespaces, see [How metadata tables work](metadata-tables-overview.md#metadata-tables-how-they-work "metadata-tables-overview.md#metadata-tables-how-they-work").

When you create your metadata table configuration, you can choose to encrypt your AWS managed
metadata tables with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS). If you choose to use
SSE-KMS, you must provide a customer managed KMS key in the same Region as your general purpose
bucket. You can set the encryption type for your tables only during table creation. After an AWS
managed table is created, you can't change its encryption setting. To specify SSE-KMS for your metadata
tables, you must have certain permissions. For more information, see [Permissions for SSE-KMS](metadata-tables-permissions.md#metadata-kms-permissions "metadata-tables-permissions.md#metadata-kms-permissions").

The encryption setting for a metadata table takes precedence over the default bucket-level encryption
setting. If you don't specify encryption for a table, it will inherit the default encryption setting
from the bucket.

AWS managed table buckets don't count toward your S3 Tables quotas. For more information about
working with AWS managed table buckets and AWS managed tables, see [Working with AWS managed table
buckets](s3-tables-aws-managed-buckets.md "s3-tables-aws-managed-buckets.md").

You can create a metadata table configuration by using the Amazon S3 console, the AWS Command Line Interface
(AWS CLI), the AWS SDKs, or the Amazon S3 REST API.

###### Note

- If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
  and re-create your configuration so that you can expire journal table records and create an
  inventory table. For more information, see [Enabling inventory tables on metadata configurations created before July 15, 2025](#metadata-tables-migration "#metadata-tables-migration").
- If you've deleted your metadata table configuration and want to re-create a configuration for
  the same general purpose bucket, you must first manually delete the old journal and inventory tables
  from your AWS managed table bucket. Otherwise, creating the new metadata table configuration fails
  because those tables already exist. To delete your metadata tables, see [Delete a metadata table](metadata-tables-delete-table.md#delete-metadata-table-procedure "metadata-tables-delete-table.md#delete-metadata-table-procedure").

Deleting a metadata table configuration deletes only the configuration. The AWS managed table
bucket and your metadata tables still exist, even if you delete the metadata table configuration.

###### Prerequisites

Before you create a metadata table configuration make sure that you've met the following prerequisites:

- Before you create a metadata table configuration make sure that you have the necessary AWS Identity and Access Management
  (IAM) permissions to create and manage metadata tables. For more information, see [Setting up permissions for configuring metadata tables](metadata-tables-permissions.md "metadata-tables-permissions.md").
- If you plan to query your metadata tables with Amazon Athena or another AWS query engine, make
  sure that you integrate your AWS managed table bucket with AWS analytics services. For more
  information, see [Integrating Amazon S3 Tables with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").

If you've already integrated an existing table bucket in this Region, your AWS managed table
bucket is also automatically integrated. To determine the integration status for your table buckets
in this Region, open the Amazon S3 console, and choose **Table buckets** in the left
navigation pane. Under **Integration with AWS analytics services**, check the
Region and whether the integration status says **Enabled**.

## Create a metadata table configuration

###### To create a metadata table configuration

Before you create a metadata table configuration, make sure that you've reviewed
and met the [prerequisites](#metadata-table-config-prereqs "#metadata-table-config-prereqs") and
that you've reviewed [Metadata table limitations and restrictions](metadata-tables-restrictions.md "metadata-tables-restrictions.md").

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose
   buckets**.
3. Choose the general purpose bucket that you want to create a metadata table
   configuration for.

###### Note

Make sure that this general purpose bucket is an AWS Region where table
buckets are available. Table buckets are available only in the US East (N. Virginia),
US East (Ohio), and US West (Oregon) Regions. 4. On the bucket's details page, choose the **Metadata** tab. 5. On the **Metadata** tab, choose **Create metadata
configuration**. 6. On the **Create metadata configuration** page, under **Journal
table**, you can choose whether to encrypt your table with server-side encryption
using AWS Key Management Service (AWS KMS) keys (SSE-KMS). By default, journal tables are encrypted with
server-side encryption using Amazon S3 managed keys (SSE-S3).

If you choose to use SSE-KMS, you must provide a customer managed KMS key in the same
Region as your general purpose bucket.

###### Important

You can set the encryption type for your metadata tables only during table creation.
After an AWS managed table is created, you can't change its encryption setting.

    * To encrypt your journal table with SSE-S3 (the default), choose **Don't
     specify encryption type**.
    * To encrypt your journal table with SSE-KMS, choose **Specify encryption
     type**. Under **Encryption type**, choose
     **Server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS)**.
     Under **AWS KMS key**, either choose from your existing KMS keys, or
     enter your KMS key ARN. If you don't already have a KMS key, choose **Enter
     KMS key ARN**, and then choose **Create a KMS key**.


    Make sure that you've set up the necessary permissions for SSE-KMS. For more
     information, see  [Permissions for
     SSE-KMS](metadata-tables-permissions.md#metadata-kms-permissions "metadata-tables-permissions.md#metadata-kms-permissions").

7. (Optional) By default, the records in your journal table don't expire. To help minimize
   the storage costs for your journal table, choose **Enabled** for
   **Record expiration**.

If you enable journal table record expiration, you can set the number of days to retain
your journal table records. To set the **Days after which records expire**
value, you can specify any whole number between `7` and `2147483647`.
For example, to retain your journal table records for one year, set this value to
`365`.

Records will be expired within 24 to 48 hours after they become eligible for expiration.

###### Important

After journal table records expire, they can't be recovered.

Under **Journal table records will expire after the specified number of
days**, select the checkbox. 8. (Optional) If you want to add an inventory table to your metadata table configuration,
under **Live inventory table**, choose **Enabled** for
**Configuration status**.

You can choose whether to encrypt your table with server-side encryption using AWS Key Management Service
(AWS KMS) keys (SSE-KMS). By default, inventory tables are encrypted with server-side encryption
using Amazon S3 managed keys (SSE-S3).

If you choose to use SSE-KMS, you must provide a customer managed KMS key in the same
Region as your general purpose bucket.

###### Important

You can set the encryption type for your metadata tables only during table creation.
After an AWS managed table is created, you can't change its encryption setting.

    * To encrypt your inventory table with SSE-S3 (the default), choose **Don't
     specify encryption type**.
    * To encrypt your inventory table with SSE-KMS, choose **Specify encryption
     type**. Under **Encryption type**, choose
     **Server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS)**.
     Under **AWS KMS key**, either choose from your existing KMS keys, or
     enter your KMS key ARN. If you don't already have a KMS key, choose **Enter
     KMS key ARN**, and then choose **Create a
     KMS key**.


    Make sure that you've set up the necessary permissions for SSE-KMS. For more
     information, see  [Permissions for
     SSE-KMS](metadata-tables-permissions.md#metadata-kms-permissions "metadata-tables-permissions.md#metadata-kms-permissions").

9. Choose **Create metadata table configuration**.
   If your metadata table configuration was successful, the names and ARNs for your metadata
   tables are displayed on the **Metadata** tab, along with the name of your AWS
   managed table bucket and namespace.

If you chose to enable an inventory table for your metadata table configuration, the table
goes through a process known as _backfilling_, during which Amazon S3
scans your general purpose bucket to retrieve the initial metadata for all objects that exist in
the bucket. Depending on the number of objects in your bucket, this process can take minutes
(minimum 15 minutes) to hours. When the backfilling process is finished, the status of your
inventory table changes from **Backfilling** to **Active**.
After backfilling is completed, updates to your objects are typically reflected in the inventory
table within one hour.

To monitor updates to your metadata table configuration, you can use AWS CloudTrail. For
more information, see [Amazon S3 bucket-level actions that are tracked by CloudTrail logging](cloudtrail-logging-s3-info.md#cloudtrail-bucket-level-tracking "cloudtrail-logging-s3-info.md#cloudtrail-bucket-level-tracking").

To run the following commands, you must have the AWS CLI installed and configured. If
you don’t have the AWS CLI installed, see [Install or update to the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

Alternatively, you can run AWS CLI commands from the console by using AWS CloudShell.
AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from
the AWS Management Console. For more information, see [What is CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") and
[Getting started with AWS CloudShell](../../../cloudshell/latest/userguide/getting-started.md "../../../cloudshell/latest/userguide/getting-started.md") in the
_AWS CloudShell User Guide_.

###### To create a metadata table configuration by using the AWS CLI

Before you create a metadata table configuration, make sure that you've reviewed and met the
[prerequisites](#metadata-table-config-prereqs "#metadata-table-config-prereqs") and that you've reviewed
[Metadata table limitations and restrictions](metadata-tables-restrictions.md "metadata-tables-restrictions.md").

To use the following example commands, replace the `user input
 placeholders` with your own information.

1. Create a JSON file that contains your metadata table configuration, and save it (for
   example, `metadata-config.json`). The following is a sample configuration.

You must specify whether to enable or disable journal table record expiration. If you
choose to enable record expiration, you must also specify the number of days after which your
journal table records will expire. To set the `Days` value, you can specify any
whole number between `7` and `2147483647`. For example, to retain your
journal table records for one year, set this value to `365`.

You can optionally choose to configure an inventory table.

For both journal tables and inventory tables, you can optionally specify an encryption
configuration. By default, metadata tables are encrypted with server-side encryption using
Amazon S3 managed keys (SSE-S3), which you can specify by setting `SseAlgorithm` to
`AES256`.

To encrypt your metadata tables with server-side encryption using AWS Key Management Service (AWS KMS) keys
(SSE-KMS), set `SseAlgorithm` to `aws:kms`. You must also set
`KmsKeyArn` to the ARN of a customer managed KMS key in the same Region where
your general purpose bucket is located.

```
{
  "JournalTableConfiguration": {
     "RecordExpiration": {
       "Expiration": "ENABLED",
      "Days": 10
    },
    "EncryptionConfiguration": {
      "SseAlgorithm": "AES256"
    }
  },
  "InventoryTableConfiguration": {
    "ConfigurationState": "ENABLED",
    "EncryptionConfiguration": {
      "SseAlgorithm": "aws:kms",
      "KmsKeyArn": "arn:aws:kms:`us-east-2`:`account-id`:key/`key-id`"
    }
  }
}
```

2. Use the following command to apply the metadata table configuration to your general
   purpose bucket (for example, `amzn-s3-demo-bucket`):

```
aws s3api create-bucket-metadata-configuration \
--bucket ``amzn-s3-demo-bucket`` \
--metadata-configuration file://./`metadata-config`.json \
--region `us-east-2`
```

3. To verify that the configuration was created, use the following command:

```
aws s3api get-bucket-metadata-configuration \
--bucket ``amzn-s3-demo-bucket`` \
--region `us-east-2`
```

To monitor updates to your metadata table configuration, you can use AWS CloudTrail. For
more information, see [Amazon S3 bucket-level actions that are tracked by CloudTrail logging](cloudtrail-logging-s3-info.md#cloudtrail-bucket-level-tracking "cloudtrail-logging-s3-info.md#cloudtrail-bucket-level-tracking").

You can send REST requests to create a metadata table configuration. For more information, see
[CreateBucketMetadataConfiguration](../API/API_CreateBucketMetadataConfiguration.md "../API/API_CreateBucketMetadataConfiguration.md") in the _Amazon S3
API Reference_.

You can use the AWS SDKs to create a metadata table configuration in Amazon S3. For
information, see the [list of supported SDKs](../API/API_CreateBucketMetadataConfiguration.md#API_CreateBucketMetadataConfiguration_SeeAlso "../API/API_CreateBucketMetadataConfiguration.md#API_CreateBucketMetadataConfiguration_SeeAlso") in the _Amazon S3 API
Reference_.

## Enabling inventory tables on metadata configurations created before July 15, 2025

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete
and re-create your configuration so that you can expire journal table records and create an inventory
table. Any changes to your general purpose bucket that occur between deleting the old configuration
and creating the new one aren't recorded in either of your journal tables.

To migrate from an old metadata configuration to a new configuration, do the following:

1. Delete your existing metadata table configuration. For step-by-step instructions, see [Deleting metadata table configurations](metadata-tables-delete-configuration.md "metadata-tables-delete-configuration.md").
2. Create a new metadata table configuration. For step-by-step instructions, see [Creating metadata table configurations](metadata-tables-create-configuration.md "metadata-tables-create-configuration.md").

If you need assistance with migrating your configuration, contact AWS Support.

After you create your new metadata configuration, you will have two journal tables. If you no
longer need the old journal table, you can delete it. For step-by-step instructions, see [Deleting metadata tables](metadata-tables-delete-table.md "metadata-tables-delete-table.md"). If you've retained your old journal table and want to join
it with your new one, see [Joining custom metadata with S3 metadata tables](metadata-tables-join-custom-metadata.md "metadata-tables-join-custom-metadata.md") for examples of how
to join two tables.

After migration, you can do the following:

1. To view your configuration, you can now use the `GetBucketMetadataConfiguration`
   API operation. To determine whether your configuration is old or new, you can look at the
   following attribute of your `GetBucketMetadataConfiguration` API response. An AWS
   managed bucket type (`"aws"`) indicates a new configuration, and a customer-managed
   bucket type (`"customer"`) indicates an old configuration.

```
"MetadataTableConfigurationResult": {
            "TableBucketType": ["aws" | "customer"]
```

For more information, see [Viewing metadata table configurations](metadata-tables-view-configuration.md "metadata-tables-view-configuration.md").

###### Note

You can use the `GetBucketMetadataConfiguration` and
`DeleteBucketMetadataConfiguration` API operations with old or new metadata table
configurations. However, if you try to use the `GetBucketMetadataTableConfiguration`
and `DeleteBucketMetadataTableConfiguration` API operations with new configurations,
you will receive HTTP `405 Method Not Allowed` errors.

Make sure that you update your processes to use the new API operations
(`CreateBucketMetadataConfiguration`, `GetBucketMetadataConfiguration`,
and `DeleteBucketMetadataConfiguration`) instead of the old API operations. 2. If you plan to query your metadata tables with Amazon Athena or another AWS query engine, make sure
that you integrate your AWS managed table bucket with AWS analytics services. If you've already
integrated an existing table bucket in this Region, your AWS managed table bucket is also
automatically integrated. For more information, see [Integrating Amazon S3 Tables with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").
