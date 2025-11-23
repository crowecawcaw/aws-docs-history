# Migrate PostgreSQL database with AWS DMS ongoing replication

After you complete the full load, make sure that you perform ongoing replication using AWS DMS to keep the source and target databases in sync. To configure the ongoing replication task, open the Database Migration Service console. On the **Create database migration task** page, follow these steps to create a migration task.

1. For **Migration type**, choose **Replicate ongoing changes**.
2. Under **CDC start mode for source transactions**, choose **Enable custom CDC start mode**.
3. Under **Custom CDC start point**, paste the native start point you captured when you prepared for ongoing replication. For more information, see [Preparing for Ongoing Replication](chap-manageddatabases.md "chap-manageddatabases.md").

###### Note

PostgreSQL as a source doesn’t support a custom CDC start time. This is because the PostgreSQL database engine doesn’t have a way to map a timestamp to an LSN or SCN as Oracle and SQL Server do.
For more information, see [Creating tasks for ongoing replication](../userguide/CHAP_Task.md "../userguide/CHAP_Task.md") and [Migrate from PostgreSQL to Amazon RDS](https://aws.amazon.com/getting-started/hands-on/move-to-managed/migrate-postgresql-to-amazon-rds/ "https://aws.amazon.com/getting-started/hands-on/move-to-managed/migrate-postgresql-to-amazon-rds/").
