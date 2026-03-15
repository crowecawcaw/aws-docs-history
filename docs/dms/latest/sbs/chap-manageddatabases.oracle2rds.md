# Migrate Oracle database with AWS DMS ongoing replication

After you complete the full load, make sure that you perform ongoing replication using AWS DMS to keep the source and target databases in sync. To configure the ongoing replication task, sign in to the AWS Management Console and follow these steps.

1. Choose **Database Migration Service**, and then choose **Database migration tasks**.
2. Choose **Create task**.
3. For **Migration type**, choose **Replicate data changes only**.
4. For **CDC start mode for source transactions**, choose **Enable custom CDC start mode**.
5. For **Custom CDC start point**, choose **Specify a log sequence number** and enter the SCN that you captured before starting the full load.
   For more information, see [Continuous replication tasks](../userguide/CHAP_Task.md "../userguide/CHAP_Task.md") and [Migrate from Oracle to Amazon RDS](https://aws.amazon.com/getting-started/hands-on/move-to-managed/migrate-oracle-to-amazon-rds/ "https://aws.amazon.com/getting-started/hands-on/move-to-managed/migrate-oracle-to-amazon-rds/").
