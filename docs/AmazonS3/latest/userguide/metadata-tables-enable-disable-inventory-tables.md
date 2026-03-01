# Enabling or disabling live inventory tables

By default, your metadata table configuration contains a _journal
table_, which records the events that occur for the objects in your bucket. The journal
table is required for each metadata table configuration.

Optionally, you can add a _live inventory table_ to your metadata
table configuration. The live inventory table provides a simple, queryable inventory of all the objects
and their versions in your bucket so that you can determine the latest state of your data.

###### Note

If you created your S3 Metadata configuration before July 15, 2025, you can't enable an inventory
table on that configuration. We recommend that you delete and re-create your configuration so that you
can create an inventory table and expire journal table records. For more information, see [Enabling inventory tables on metadata configurations created before July 15, 2025](metadata-tables-create-configuration.md#metadata-tables-migration "metadata-tables-create-configuration.md#metadata-tables-migration").

The inventory table contains the latest metadata for all objects in your bucket. You can use this
table to simplify and speed up business workflows and big data jobs by identifying objects that you want
to process for various workloads. For example, you can query the inventory table to do the following:

- Find all objects stored in the S3 Glacier Deep Archive storage class.
- Create a distribution of object tags or find objects without tags.
- Find all objects that aren't encrypted by using server-side encryption with AWS Key Management Service (AWS KMS)
  keys (SSE-KMS).
- Compare your inventory table at two different points in time to understand the growth in objects
  with specific tags.
  If you chose to enable an inventory table for your metadata table configuration, the table goes
  through a process known as _backfilling_, during which Amazon S3 scans your
  general purpose bucket to retrieve the initial metadata for all objects that exist in the bucket.
  Depending on the number of objects in your bucket, this process can take minutes (minimum 15 minutes) to hours. When the
  backfilling process is finished, the status of your inventory table changes from
  **Backfilling** to **Active**. After backfilling is completed,
  updates to your objects are typically reflected in the inventory table within one hour.

###### Note

- You're charged for backfilling your inventory table. If your general purpose bucket has more
  than one billion objects, you're also charged a monthly fee for your inventory table. For more
  information, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").
- You can't pause updates to your inventory table and then resume them. However, you can disable
  the inventory table configuration. Disabling the inventory table doesn't delete it. The inventory
  table is retained for your records until you decide to delete it.

If you've disabled your inventory table and later want to re-enable it, you must first delete
the old inventory table from your AWS managed table bucket. When you re-enable the inventory
table configuration, Amazon S3 creates a new inventory table, and you're charged again for backfilling
the new inventory table.
You can enable or disable inventory tables by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the
AWS SDKs, or the Amazon S3 REST API.

###### Prerequisites

If you've disabled your inventory table and now want to re-enable it, you must first manually
delete the old inventory table from your AWS managed table bucket. Otherwise, re-enabling the
inventory table fails because an inventory table already exists in the table bucket. To delete your
inventory table, see [Delete a metadata table](metadata-tables-delete-table.md#delete-metadata-table-procedure "metadata-tables-delete-table.md#delete-metadata-table-procedure").

When you re-enable the inventory table configuration, Amazon S3 creates a new inventory table, and you're
charged again for backfilling the new inventory table.

## Enable or disable inventory tables

###### To enable or disable inventory tables

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. Choose the general purpose bucket with the metadata table configuration that you want to
   enable or disable an inventory table for.
4. On the bucket's details page, choose the **Metadata** tab.
5. On the **Metadata** tab, choose **Edit**, then choose
   **Edit inventory table configuration**.
6. On the **Edit inventory table configuration** page, choose
   **Enabled** or **Disabled** under **Inventory
   table**.

###### Note

Before you choose **Enabled**, make sure that you've reviewed and met
the [prerequisites](#inventory-table-config-prereqs "#inventory-table-config-prereqs").

    * If you chose **Enabled**, you can choose whether to encrypt your
     table with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS). By default,
     inventory tables are encrypted with server-side encryption using Amazon S3 managed keys
     (SSE-S3).


    If you choose to use SSE-KMS, you must provide a customer managed KMS key in the
     same Region as your general purpose bucket.


    ###### Important

    You can set the encryption type for your metadata tables only during table creation.
     After an AWS managed table is created, you can't change its encryption setting.




    	+ To encrypt your inventory table with SSE-S3 (the default), choose **Don't
    	 specify encryption type**.
    	+ To encrypt your inventory table with SSE-KMS, choose **Specify encryption
    	 type**. Under **Encryption type**, choose
    	 **Server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS)**.
    	 Under **AWS KMS key**, either choose from your existing KMS keys, or
    	 enter your KMS key ARN. If you don't already have a KMS key, choose
    	 **Enter KMS key ARN**, and then choose **Create a
    	 KMS key**.
    * If you chose **Disabled**, under **After the inventory table
     is disabled, the table will no longer be updated, and updates can't be
     resumed**, select the checkbox.

7. Choose **Save changes**.
   To run the following commands, you must have the AWS CLI installed and configured. If you don’t
   have the AWS CLI installed, see [Install or update to the latest version
   of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

Alternatively, you can run AWS CLI commands from the console by using AWS CloudShell. AWS CloudShell is a
browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. For more
information, see [What
is CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") and [Getting started with AWS CloudShell](../../../cloudshell/latest/userguide/getting-started.md "../../../cloudshell/latest/userguide/getting-started.md") in
the _AWS CloudShell User Guide_.

###### To enable or disable inventory tables by using the AWS CLI

To use the following example commands, replace the `user input
 placeholders` with your own information.

###### Note

Before enabling an inventory configuration, make sure that you've reviewed and met the
[prerequisites](#inventory-table-config-prereqs "#inventory-table-config-prereqs").

1. Create a JSON file that contains your inventory table configuration, and save it (for
   example, `inventory-config.json`). The following is a sample configuration
   to enable a new inventory table.

If you're enabling an inventory table, you can optionally specify an encryption
configuration. By default, metadata tables are encrypted with server-side encryption using
Amazon S3 managed keys (SSE-S3), which you can specify by setting `SseAlgorithm` to
`AES256`.

To encrypt your inventory table with server-side encryption using AWS Key Management Service (AWS KMS) keys
(SSE-KMS), set `SseAlgorithm` to `aws:kms`. You must also set
`KmsKeyArn` to the ARN of a customer managed KMS key in the same Region where
your general purpose bucket is located.

```
{
  "ConfigurationState": "ENABLED",
  "EncryptionConfiguration": {
    "SseAlgorithm": "aws:kms",
    "KmsKeyArn": "arn:aws:kms:`us-east-2`:`account-id`:key/`key-id`"
  }
}
```

If you want to disable an existing inventory table, use the following configuration:

```
{
  "ConfigurationState": "DISABLED"  }
}
```

2. Use the following command to update the inventory table configuration for your general
   purpose bucket (for example, `amzn-s3-demo-bucket`):

```
aws s3api update-bucket-metadata-inventory-table-configuration \
--bucket `amzn-s3-demo-source-bucket` \
--inventory-table-configuration file://./`inventory-config`.json \
--region `us-east-2`
```

You can send REST requests to enable or disable inventory tables. For more information, see
[UpdateBucketMetadataInventoryTableConfiguration](../API/API_UpdateBucketMetadataInventoryTableConfiguration.md "../API/API_UpdateBucketMetadataInventoryTableConfiguration.md").

You can use the AWS SDKs to enable or disable inventory tables in Amazon S3. For information, see
the [list of supported SDKs](../API/API_UpdateBucketMetadataInventoryTableConfiguration.md#API_UpdateBucketMetadataInventoryTableConfiguration_SeeAlso "../API/API_UpdateBucketMetadataInventoryTableConfiguration.md#API_UpdateBucketMetadataInventoryTableConfiguration_SeeAlso").
