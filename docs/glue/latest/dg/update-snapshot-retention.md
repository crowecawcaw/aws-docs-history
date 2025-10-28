# Updating snapshot retention optimizer

You can update the existing configuration of an snapshot retention optimizer for a
particular Apache Iceberg table using the AWS Glue console, AWS CLI, or the UpdateTableOptimizer
API.

Console

###### To update snapshot retention configuration

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose **Data Catalog** and choose **Tables**. From the tables list, choose the Iceberg table you want to
   update the snapshot retention optimizer configuration.
3. On the lower section of the **Tables details** page,
   select the **Table optimization** tab, and then choose
   **Edit**. You can also choose **Edit** under
   **Optimization** from the **Actions** menu
   located on the top right corner of the page.
4. On the **Edit optimization** page, make the desired changes.
5. Choose **Save**.

AWS CLI

To update a snapshot retention optimizer using the AWS CLI, you can use the following command:

```
aws glue update-table-optimizer \
 --catalog-id `123456789012` \
 --database-name `iceberg_db` \
 --table-name `iceberg_table` \
 --table-optimizer-configuration '{"roleArn":"arn:aws:iam::`123456789012`:role/`optimizer_role`"","enabled":'true', "vpcConfiguration":{"glueConnectionName":`"glue_connection_name"`},"retentionConfiguration":{"icebergConfiguration":{"snapshotRetentionPeriodInDays":`7`,"numberOfSnapshotsToRetain":`3`,"cleanExpiredFiles":`'true'`}}}' \
 --type retention
```

This command updates the retention configuration for the specified table in
the given catalog, database, and Region. The key parameters are:

- snapshotRetentionPeriodInDays –The number of days to retain snapshots
  before expiring them. The default value is `1`.
- numberOfSnapshotsToRetain – The minimum number of snapshots to keep, even
  if they are older than the retention period. The default value is `5`.
- cleanExpiredFiles – A boolean indicating whether to delete expired data files
  after expiring snapshots. The default value is `true`.

When set to true, older snapshots are removed from table metadata, and their underlying files are deleted."
If this parameter is set to false, older snapshots are removed from table metadata but their underlying files remain in the storage as orphan files.

API
To update a table optimizer, you can use the `UpdateTableOptimizer` API.
This API allows you to update the configuration of an existing table optimizer for compaction,
retention, or orphan file removal.
The request parameters include:

- catalogId (required): The ID of the catalog containing the table
- databaseName (optional): The name of the database containing the table
- tableName (optional): The name of the table
- type (required): The type of table optimizer (compaction, retention, or
  orphan_file_deletion)
- retentionConfiguration (required): The updated configuration for the table optimizer,
  including role ARN, enabled status, retention configuration, and orphan file
  removal configuration.
