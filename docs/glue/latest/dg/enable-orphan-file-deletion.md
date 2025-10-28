# Enabling orphan file deletion

You can use AWS Glue console, AWS CLI, or AWS API to enable orphan file deletion for your Apache Iceberg tables in the Data Catalog.
For new tables, you can choose Apache Iceberg as table format and enable orphan file deletion optimizer when you create the table.
Snapshot retention is disabled by default for new tables.

Console

###### To enable orphan file deletion

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/") and sign in as a data lake administrator, the table creator, or a user who has been granted
   the `glue:UpdateTable` and `lakeformation:GetDataAccess` permissions on the table.
2. In the navigation pane, under **Data Catalog**, choose **Tables**.
3. On the **Tables** page, choose an Iceberg table in that you want to
   enable orphan file deletion.

Choose the **Table
optimization** tab on the lower section of the page, and choose
**Enable**, **Orphan file deletion** from **Actions**.

You can also choose **Enable** under **Optimization** from the **Actions** menu located on the top right corner of the page.. 4. On the **Enable optimization** page, choose
**Orphan file deletion** under **Optimization
options**. 5. If you choose to use **Default settings**, all orphan files will be deleted after 3 days.
If you want to keep the orphan files for a specific number of days, choose **Customize settings**. 6. Next, choose an IAM role with the required permissions to delete orphan
files. 7. If you have security policy configurations where the Iceberg table
optimizer needs to access Amazon S3 buckets from a specific Virtual Private
Cloud (VPC), create an AWS Glue network connection or use an existing
one.

If you don't have an AWS Glue VPC Connection set up already,
create a new one by following the steps in the [Creating connections for connectors](creating-connections.md "creating-connections.md") section using the AWS Glue console or the AWS CLI/SDK. 8. If you choose **Customize settings**, enter the number
of days to retain the files before deletion under **Orphan file deletion
configuration**. You can also specify the interval between two
consecutive optimizer runs. The default value is 24 hours. 9. Choose **Enable optimization**.

AWS CLI
To enable orphan file deletion for an Iceberg table in AWS Glue, you need to create
a table optimizer of type `orphan_file_deletion` and set the
`enabled` field to true. To create an orphan file deletion optimizer for
an Iceberg table using the AWS CLI, you can use the following command:

```
aws glue create-table-optimizer \
 --catalog-id `123456789012` \
 --database-name `iceberg_db` \
 --table-name `iceberg_table` \
 --table-optimizer-configuration '{"roleArn":"arn:aws:iam::`123456789012`:role/`optimizer_role`","enabled":true, "vpcConfiguration":{
"glueConnectionName":`"glue_connection_name"`}, "orphanFileDeletionConfiguration":{"icebergConfiguration":{"orphanFileRetentionPeriodInDays":`3`, "location":'`S3 location`'}}}'\
 --type orphan_file_deletion
```

This command creates an orphan file deletion optimizer for the specified Iceberg
table. The key parameters are:

- roleArn – the ARN of the IAM role with permissions to access the S3
  bucket and Glue resources.
- enabled – Set to true to enable the optimizer.
- orphanFileRetentionPeriodInDays – The number of days to retain orphan
  files before deleting them (minimum 1 day).
- type – Set to orphan_file_deletion to create an orphan file deletion
  optimizer.

After creating the table optimizer, it will run orphan file deletion periodically
(once per day if left enabled). You can check the runs using the
`list-table-optimizer-runs` API. The orphan file deletion job will
identify and delete files that are not tracked in the Iceberg metadata for the
table.

API
Call [CreateTableOptimizer](aws-glue-api-table-optimizers.md#aws-glue-api-table-optimizers-CreateTableOptimizer "aws-glue-api-table-optimizers.md#aws-glue-api-table-optimizers-CreateTableOptimizer") operation to create the orphan file
deletion optimizer for a specific table.
