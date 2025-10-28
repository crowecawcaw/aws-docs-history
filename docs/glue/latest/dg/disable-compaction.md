# Disabling compaction optimizer

You can disable automatic compaction for a particular Apache Iceberg table using AWS Glue console or AWS CLI.

Console

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. On the left navigation, under **Data Catalog**, choose
   **Tables**.
3. From the tables list, choose the Iceberg table that you want to disable
   compaction.
4. Choose the **Table optimization** tab on the lower section of
   the **Tables details** page.
5. From **Actions**, choose **Disable**, and
   then choose **Compaction**.
6. Choose **Disable compaction** on the confirmation message. You can re-enable compaction at a later time.

After the you confirm, compaction is disabled and the compaction status for the table turns back to `Disabled`.

AWS CLI
In the following example, replace the account ID with a valid AWS account ID.
Replace the database name and table name with actual Iceberg table name and the database name. Replace the `roleArn` with the AWS Resource Name (ARN) of the IAM role and actual name of the IAM role
that has the required permissions to run compaction.

```
aws glue update-table-optimizer \
  --catalog-id `123456789012` \
  --database-name `iceberg_db` \
  --table-name `iceberg_table` \
  --table-optimizer-configuration '{"roleArn":"arn:aws:iam::`123456789012`:role/`optimizer_role`", "enabled":'false', "vpcConfiguration":{"glueConnectionName":`"glue_connection_name"`}}'\
  --type compaction
```

AWS API
Call [UpdateTableOptimizer](aws-glue-api-table-optimizers.md#aws-glue-api-table-optimizers-UpdateTableOptimizer "aws-glue-api-table-optimizers.md#aws-glue-api-table-optimizers-UpdateTableOptimizer") operation to disable compaction for a specific
table.
