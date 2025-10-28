# Disabling snapshot retention optimizer

You can disable the snapshot retention optimizer for a particular Apache Iceberg
table using AWS Glue console or AWS CLI.

Console

###### To disable snapshot retention

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose **Data Catalog** and choose **Tables**.
   From the tables list, choose the Iceberg table that you want to disable the
   optimizer for snapshot retention.
3. On lower section of the **Table details** page, choose **Table optimization** and
   **Disable**, **Snapshot retention** under **Actions**.

You can also choose **Disable** under **Optimization** from the **Actions** menu located on top right corner of the page. 4. Choose **Disable** on the confirmation message. You can
re-enable the snapshot retention optimizer at a later time.

After the you confirm, snapshot retention optimizer is disabled and the
status for snapshot retention turns back to `Not enabled`.

AWS CLI
In the following example, replace the account ID with a valid AWS account ID.
Replace the database name and table name with actual Iceberg table name and the
database name. Replace the `roleArn` with the AWS Resource Name (ARN) of
the IAM role and actual name of the IAM role that has the required permissions to
run the retention optimizer.

```
aws glue update-table-optimizer \
  --catalog-id `123456789012` \
  --database-name `iceberg_db` \
  --table-name `iceberg_table` \
  --table-optimizer-configuration '{"roleArn":"arn:aws:iam::`123456789012`:role/`optimizer_role`", "vpcConfiguration":{"glueConnectionName":`"glue_connection_name"`}, "enabled":'false'}'\
  --type retention
```

AWS API
Call [UpdateTableOptimizer](aws-glue-api-table-optimizers.md#aws-glue-api-table-optimizers-UpdateTableOptimizer "aws-glue-api-table-optimizers.md#aws-glue-api-table-optimizers-UpdateTableOptimizer") operation to disable the snapshot retention optimizer
for a specific table.
