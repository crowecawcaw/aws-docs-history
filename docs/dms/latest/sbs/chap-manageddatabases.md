# Full load SQL Server database migration

The full load migration phase populates the target database with a copy of the source data. In each section, you can find detailed information about the full load method and their results to help you choose the one that fits your use case. For all three methods, we use the [`dms_sample`](https://github.com/aws-samples/aws-database-migration-samples/blob/master/sqlserver/sampledb/v1/README.md "https://github.com/aws-samples/aws-database-migration-samples/blob/master/sqlserver/sampledb/v1/README.md") database as an example. The `dms_sample` database includes tables, views, indexes, stored procedures, and other database objects.

###### Topics

- [SQL Server database backup and restore using Amazon S3](chap-manageddatabases.md "chap-manageddatabases.md")
- [SQL Server import and export wizard](chap-manageddatabases.md "chap-manageddatabases.md")
- [Generate and Publish Scripts wizard and Bulk Copy Program Utility](chap-manageddatabases.md "chap-manageddatabases.md")
