# Updating orphan file deletion optimizer

You can modify the configuration for the orphan file deletion optimizer, such as changing the retention period for orphan files or the IAM role used by the optimizer
using AWS Glue console, AWS CLI, or the `UpdateTableOptimizer` operation.

AWS Management Console

###### To update the orphan file deletion optimizer

1. Choose **Data Catalog** and choose **Tables**. From the tables list, choose the table you want to
   update the orphan file deletion optimizer configuration.
2. On the lower section of the **Tables details** page,
   choose **Table optimization** , and then choose
   **Edit**.
3. On the **Edit optimization** page, make the desired changes.
4. Choose **Save**.

AWS CLI
You can use the `update-table-optimizer` call to update the orphan
file deletion optimizer in AWS Glue, you can use call. This allows you to modify the
`OrphanFileDeletionConfiguration` in the
`icebergConfiguration` field where you can specify the updated
`OrphanFileRetentionPeriodInDays` to set the number of days to retain
orphan files, to specify the Iceberg table location to delete orphan files from.

```
aws glue update-table-optimizer \
 --catalog-id `123456789012` \
 --database-name `iceberg_db` \
 --table-name `Iceberg_table` \
 --table-optimizer-configuration '{"roleArn":"arn:aws:iam::`123456789012`:role/`optimizer_role`","enabled":true, "vpcConfiguration":{"glueConnectionName":`"glue_connection_name"`},"orphanFileDeletionConfiguration":{"icebergConfiguration":{"orphanFileRetentionPeriodInDays":`5`}}}' \
 --type orphan_file_deletion
```

APICall the [UpdateTableOptimizer](aws-glue-api-table-optimizers.md#aws-glue-api-table-optimizers-UpdateTableOptimizer "aws-glue-api-table-optimizers.md#aws-glue-api-table-optimizers-UpdateTableOptimizer") operation to update the orphan file deletion optimizer for a table.
