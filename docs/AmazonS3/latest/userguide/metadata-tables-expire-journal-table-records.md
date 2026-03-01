# Expiring journal table records

By default, the records in your journal table don't expire. To help minimize the storage costs for
your journal table, you can enable journal table record expiration.

###### Note

If you created your S3 Metadata configuration before July 15, 2025, you can't enable journal table
record expiration on that configuration. We recommend that you delete and re-create your configuration
so that you can expire journal table records and create an inventory table. For more information, see
[Enabling inventory tables on metadata configurations created before July 15, 2025](metadata-tables-create-configuration.md#metadata-tables-migration "metadata-tables-create-configuration.md#metadata-tables-migration").

If you enable journal table record expiration, you can set the number of days to retain your journal
table records. To set this value, specify any whole number between `7` and
`2147483647`. For example, to retain your journal table records for one year, set this
value to `365`.

###### Important

After journal table records expire, they can't be recovered.

Records are expired within 24 to 48 hours after they become eligible for expiration. Journal records
are removed from the latest snapshot. The data and storage for the deleted records is removed through
table maintenance operations.

If you've enabled journal table record expiration, you can disable it at any time to stop expiring
your journal table records.

You can expire journal table records by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the AWS
SDKs, or the Amazon S3 REST API.

## How to expire journal table records

###### To expire journal table records

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. Choose the general purpose bucket that contains the metadata table configuration with the
   journal table that you want to expire records from.
4. On the bucket's details page, choose the **Metadata** tab.
5. On the **Metadata** tab, choose **Edit**, then choose
   **Edit journal table record expiration**.
6. On the **Edit journal table record expiration** page, choose
   **Enabled** under **Record expiration**.
7. Set the number of days to retain your journal table records. To set the **Days
   after which records expire** value, specify any whole number between `7`
   and `2147483647`. For example, to retain your journal table records for one year,
   set this value to `365`.

###### Important

After journal table records expire, they can't be recovered. 8. Under **Journal table records will expire after the specified number of
days**, select the checkbox. 9. Choose **Save changes**.
If you want to disable journal table record expiration, repeat the preceding steps, but choose
**Disabled** instead of **Enabled** for step 6.

To run the following commands, you must have the AWS CLI installed and configured. If you don't
have the AWS CLI installed, see [Install or update to the latest version
of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

You can also run AWS CLI commands from the console by using AWS CloudShell. AWS CloudShell is a
browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. For more
information, see [What
is CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") and [Getting started with AWS CloudShell](../../../cloudshell/latest/userguide/getting-started.md "../../../cloudshell/latest/userguide/getting-started.md") in
the _AWS CloudShell User Guide_.

###### To expire journal table records by using the AWS CLI

To use the following example commands, replace the `user input
 placeholders` with your own information.

1. Create a JSON file that contains your journal table configuration, and save it (for
   example, `journal-config.json`). The following is a sample configuration.

To set the `Days` value, specify any whole number between `7` and
`2147483647`. For example, to retain your journal table records for one year, set
this value to `365`.

```
{
  "RecordExpiration": {
    "Expiration": "ENABLED",
    "Days": `10`
  }
}
```

To disable journal table record expiration, create the following sample configuration
instead. If `Expiration` is set to `DISABLED`, you must not specify a
`Days` value in the configuration.

```
{
  "RecordExpiration": {
    "Expiration": "DISABLED"
  }
}
```

2. Use the following command to expire records from the journal table in your general purpose
   bucket (for example, `amzn-s3-demo-bucket`):

```
aws s3api update-bucket-metadata-journal-table-configuration \
--bucket `amzn-s3-demo-bucket` \
--journal-table-configuration file://./`journal-config`.json \
--region `us-east-2`
```

You can send REST requests to expire journal table records. For more information, see [UpdateBucketMetadataJournalTableConfiguration](../API/API_UpdateBucketMetadataJournalTableConfiguration.md "../API/API_UpdateBucketMetadataJournalTableConfiguration.md").

You can use the AWS SDKs to expire journal table records in Amazon S3. For information, see the
[list of supported SDKs](../API/API_UpdateBucketMetadataJournalTableConfiguration.md#API_UpdateBucketMetadataJournalTableConfiguration_SeeAlso "../API/API_UpdateBucketMetadataJournalTableConfiguration.md#API_UpdateBucketMetadataJournalTableConfiguration_SeeAlso").
