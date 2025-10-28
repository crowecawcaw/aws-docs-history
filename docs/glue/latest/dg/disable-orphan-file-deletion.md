# Disabling orphan file deletion

You can disable orphan file deletion optimizer for a particular Apache Iceberg table using AWS Glue console or AWS CLI.

Console

###### To disable orphan file deletion

1. Choose **Data Catalog** and choose **Tables**.
   From the tables list, choose the Iceberg table that you want to disable the
   optimizer for orphan file deletion.
2. On lower section of the **Table details** page, choose
   **Table optimization** tab.
3. Choose **Actions**, and then choose **Disable** , **Orphan file deletion**.

You can also choose **Disable** under
**Optimization** from the **Actions**
menu. 4. Choose **Disable** on the confirmation message. You can
re-enable the orphan file deletion optimizer at a later time.

After the you confirm, orphan file deletion optimizer is disabled and the
status for orphan file deletion turns back to `Not enabled`.

AWS CLI
In the following example, replace the account ID with a valid AWS account ID.
Replace the database name and table name with actual Iceberg table name and the database name. Replace the `roleArn` with the AWS Resource Name (ARN) of the IAM role and actual name of the IAM role
that has the required permissions to disable the optimizer.

```
aws glue update-table-optimizer \
  --catalog-id `123456789012` \
  --database-name `iceberg_db` \
  --table-name `iceberg_table` \
  --table-optimizer-configuration '{"roleArn":"arn:aws:iam::`123456789012`:role/`optimizer_role`", "enabled":'false'}'\
  --type orphan_file_deletion
```

API
Call the [UpdateTableOptimizer](aws-glue-api-table-optimizers.md#aws-glue-api-table-optimizers-UpdateTableOptimizer "aws-glue-api-table-optimizers.md#aws-glue-api-table-optimizers-UpdateTableOptimizer") operation to disable the snapshot retention optimizer
for a specific table.
