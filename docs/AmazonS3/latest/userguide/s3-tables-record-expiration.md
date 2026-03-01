# Record expiration for tables

By default, records in your S3 tables don't expire. To help minimize storage costs for your
tables, you can enable and configure record expiration for the tables. With this option, Amazon S3
automatically removes records from a table when the records expire.

If you enable record expiration for a table, you specify the number of days to retain
records in the table before the records expire. This can be any number of days ranging from 1
day through 2,147,483,647 days. For example, to retain table records for one year, specify
`365` days. The records then persist for 365 days. After 365 days, the records
expire and Amazon S3 automatically removes them.

You can enable and configure record expiration for AWS managed tables that store specific
data sets from certain AWS services, currently Amazon S3 Storage Lens and Amazon SageMaker Catalog. Record expiration
options aren't currently available for other AWS managed tables. The exception is Amazon S3
metadata journal tables. Journal tables use distinct record expiration settings that you specify
at the service level. For information about configuring record expiration for this type of
table, see [Expiring journal table records](metadata-tables-expire-journal-table-records.md "metadata-tables-expire-journal-table-records.md"). Note that record expiration
options aren't available for S3 tables that you create.

After you enable record expiration for a table, you can disable it at any time. Amazon S3 then
stops expiring and removing records from the table.

###### Topics

- [How it
  works](#s3-tables-record-expiration-how-it-works "#s3-tables-record-expiration-how-it-works")
- [Configuring record
  expiration](#s3-tables-record-expiration-configure "#s3-tables-record-expiration-configure")
- [Monitoring record
  expiration](#s3-tables-record-expiration-monitor "#s3-tables-record-expiration-monitor")
- [Considerations](#s3-tables-expiration-considerations "#s3-tables-expiration-considerations")

## How record expiration works

Record expiration automatically removes records from an S3 table when the records are
older than the number of days that you specify in the record expiration settings for the
table. To determine when records expire, Amazon S3 uses specific timestamps in the records. The
choice of timestamp column derives directly from the table schema for a table. You don't need
to specify which timestamp column to use. The tables are managed by AWS and Amazon S3
automatically chooses the appropriate column to use when you enable record expiration for a
table.

You can enable and configure record expiration settings for AWS managed tables that
store specific Amazon S3 Storage Lens metrics or specific Amazon SageMaker Catalog metadata. Record expiration
options are available for the following AWS managed tables for those services:

- S3 Storage Lens – `bucket_property_metrics`,
  `default_activity_metrics`, `default_storage_metrics`,
  `expanded_prefixes_activity_metrics`, and
  `expanded_prefixes_storage_metrics`. To determine when records in these
  tables expire, Amazon S3 uses the `report_time` field in the records.
- Amazon SageMaker Catalog – `ASSET`. To determine when records in this table
  expire, Amazon S3 uses the `snapshot_time` field in the records.

After you enable record expiration for a table, Amazon S3 starts running record expiration jobs
that perform the following operations for the table:

1. Identify records that are older than the specified expiration setting.
2. Create a new snapshot that excludes references to the expired records.

Removal is also based on snapshot expiration and unreferenced file removal settings in the
maintenance configuration settings for the table. To learn more about these settings, see
[Maintenance for tables](s3-tables-maintenance.md "s3-tables-maintenance.md").

###### Warning

Amazon S3 expires and removes records within 24 to 48 hours after the records become eligible
for expiration. Table records are removed from the latest snapshot. Data and storage for the
records are removed through table maintenance operations. Table records can't be recovered
after they expire.

## Configuring record expiration for a table

You can enable, configure, and otherwise manage the record expiration settings for an S3
table by using the Amazon S3 console, Amazon S3 REST API, AWS Command Line Interface (AWS CLI), or AWS SDKs.

Before you try to perform these tasks for a table, make sure that you have the following
AWS Identity and Access Management (IAM) permissions:

- `s3tables:GetTableRecordExpirationConfiguration` – This action
  allows you to access current record expiration settings for tables.
- `s3tables:PutTableRecordExpirationConfiguration` – This action
  allows you to enable, configure, and disable record expiration settings for tables.
- `s3tables:GetTableRecordExpirationJobStatus` – This action allows
  you to monitor the status of record expiration operations (jobs) for tables and access
  metrics for the operations.

The following sections explain how to enable, configure, and disable record expiration
settings for a table by using the Amazon S3 console and the AWS CLI. To perform these tasks with the
Amazon S3 REST API or an AWS SDK, use the [PutTableRecordExpirationConfiguration](../API/API_s3Buckets_PutTableRecordExpirationConfiguration.md "../API/API_s3Buckets_PutTableRecordExpirationConfiguration.md") operation. For more information, see [Developing with
Amazon S3](../API/developing-s3.md "../API/developing-s3.md") in the _Amazon Simple Storage Service API Reference_.

To enable and configure record expiration settings for an S3 table by using the
console, follow these steps.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. On the **Table buckets** page, choose the bucket that stores the
   table.
4. On the **Tables** tab, choose the table.
5. On the **Maintenance** tab, in the **Record
   expiration** section, choose **Edit**.
6. Under **Record expiration**, choose
   **Enable**.
7. For **Days after which records expire**, enter the number of days
   to retain records in the table. This can be any whole number ranging from 1 through
   2,147,483,647. For example, to retain records for one year, enter
   `365`.

###### Warning

As you determine the appropriate retention period for records in the table, note
that records can't be recovered after they expire. 8. Choose **Save changes**.
To subsequently change the retention period, repeat the preceding steps.

To subsequently disable record expiration, repeat steps 1 through 5. Then, for step 6,
choose **Disable**. When you finish, choose **Save
changes**.

To configure and manage record expiration settings for an S3 table by using the AWS CLI,
run the [put-table-record-expiration-configuration](../../../cli/latest/reference/s3tables/put-table-record-expiration-configuration.md "../../../cli/latest/reference/s3tables/put-table-record-expiration-configuration.md") command.

You can start by creating a JSON file that contains the record expiration settings to
apply to the table. The following example shows the contents of a JSON file that enables
record expiration for a table. It also specifies a retention period of 30 days for records
in the table. In other words, it specifies that table records should expire after 30
days.

```
{
    "status": "`enabled`",
        "settings": {
            "days": `30`
        {
}
```

To use the preceding example, replace the `user input
 placeholders` with your own information.

###### Warning

As you determine the appropriate retention period for records in the table, note
that records can't be recovered after they expire.

To disable record expiration for a table, specify `disabled` for the
`status` field and omit the `settings` object from the file. For
example:

```
{
    "status": "`disabled`"
}
```

After you create a JSON file with the settings to apply, run the
`put-table-record-expiration-configuration` command. For the
`table-arn` parameter, specify the Amazon Resource Name (ARN) of the table.
For the `value` parameter, specify the name of the file that stores the
settings.

For example, the following command updates the record expiration settings for a table.
The settings are specified in a file named
`record-expiration-config.json`.

```
aws s3tables put-table-record-expiration-configuration \
    --table-arn arn:aws:s3tables:`us-east-1`:`123456789012`:bucket/`amzn-s3-demo-table-bucket`/table/`amzn-s3-demo-table` \
    --value `file://./record-expiration-config.json`
```

To use the preceding example, replace the `user input
 placeholders` with your own information.

## Monitoring record expiration for a table

To monitor the status and results of record expiration operations for your S3 tables, use
the [GetTableRecordExpirationJobStatus](../API/API_s3Buckets_GetTableRecordExpirationJobStatus.md "../API/API_s3Buckets_GetTableRecordExpirationJobStatus.md") operation or, if you're using the AWS CLI, run the
[get-table-record-expiration-job-status](../../../cli/latest/reference/s3tables/get-table-record-expiration-job-status.md "../../../cli/latest/reference/s3tables/get-table-record-expiration-job-status.md") command. In your request, specify the Amazon
Resource Name (ARN) of the table.

For example, the following AWS CLI command retrieves the status of record expiration
operations for a specific table in a table bucket. To use this example, replace the
`user input placeholders` with your own
information.

```
aws s3tables get-table-record-expiration-job-status \
    --table-arn arn:aws:s3tables:`us-east-1`:`123456789012`:bucket/`amzn-s3-demo-table-bucket`/table/`amzn-s3-demo-table`
```

If your request succeeds, you receive a response that provides details such as when Amazon S3
most recently ran record expiration operations for the table and the status of that run. If
the most recent run succeeded, the response also includes processing metrics—for
example, the number of data files and records that were removed, and the total size of the
data that was removed. If errors occurred during the most recent run, the response includes a
failure message that describes why the run failed.

## Considerations

As you configure and manage record expiration settings for your AWS managed S3 tables,
keep the following in mind:

- Record expiration is available only for certain AWS managed tables created by
  supported AWS services, Amazon S3 Storage Lens and Amazon SageMaker Catalog. In addition, record expiration is
  available only for individual tables, not entire table buckets.
- To determine when records expire, Amazon S3 uses specific timestamps in the tables. These
  timestamps represent when the data was created, not when Amazon S3 ingested the records in a
  table. The timestamp column that's used depends on the service that publishes the table:
  for S3 Storage Lens metrics, the `report_time` field; and, for Amazon SageMaker Catalog metadata,
  the `snapshot_time` field. You cannot specify which field to use because the
  tables are managed by AWS.
- If there are delays when data is exported to a table, records might become eligible
  for expiration sooner than you expect. For this reason, we recommend that you account for
  potential ingestion delays by adding buffer to the retention period in the expiration
  settings for your tables.
- Records expire and are removed within 24 to 48 hours after they become eligible for
  expiration. Amazon S3 doesn't expire and remove records immediately after they become eligible
  for expiration.
- Records cannot be recovered after they expire and are removed.
