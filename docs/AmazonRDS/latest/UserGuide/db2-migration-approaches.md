# Using AWS services to migrate data from Db2 to Amazon RDS for Db2

In Amazon RDS, there are several ways you can migrate data from a Db2 database to Amazon RDS for Db2.
You can perform a one-time migration of your Db2 database from Linux,
AIX, or Windows environments to Amazon RDS for Db2. To minimize
downtime, you can perform a near-zero downtime migration. You can migrate your data by saving
it to Amazon S3 and loading it one table at a time into your Db2 database. You can also perform a synchronous
migration through replication or use AWS Database Migration Service.

For one-time migrations for Linux-based Db2 databases, Amazon RDS only supports
offline and online backups. Amazon RDS doesn't support incremental and Delta
backups. For near-zero downtime migrations for Linux-based Db2 databases,
Amazon RDS requires online backups. We recommend that you use online backups for near-zero
downtime migrations and offline backups for migrations that can handle downtime.

###### Topics

- [Migrating from Linux to Linux for Amazon RDS for Db2](db2-one-time-migration-linux.md "db2-one-time-migration-linux.md")
- [Migrating from Linux to Linux with near-zero downtime for Amazon RDS for Db2](db2-near-zero-downtime-migration.md "db2-near-zero-downtime-migration.md")
- [Migrating synchronously from Linux to Linux for Amazon RDS for Db2](db2-synchronous-migration-linux.md "db2-synchronous-migration-linux.md")
- [Migrating from AIX or Windows to Linux for Amazon RDS for Db2](db2-one-time-migration-aix-windows-linux.md "db2-one-time-migration-aix-windows-linux.md")
- [Migrating Db2 data through Amazon S3 to Amazon RDS for Db2](db2-migration-load-from-s3.md "db2-migration-load-from-s3.md")
- [Migrating to Amazon RDS for Db2 with AWS Database Migration Service (AWS DMS)](db2-migration-amazon-dms.md "db2-migration-amazon-dms.md")
