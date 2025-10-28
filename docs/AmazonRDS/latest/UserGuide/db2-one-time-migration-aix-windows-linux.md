# Migrating from AIX or Windows to Linux for Amazon RDS for Db2

With this migration approach, you use native Db2 tools to back up your self-managed Db2
database to an Amazon S3 bucket. Native Db2 tools include the `export` utility, the
`db2move` system command, or the `db2look` system command. Your
Db2 database can either be self-managed or in Amazon Elastic Compute Cloud (Amazon EC2). You can move data from your
AIX or Windows system to your Amazon S3 bucket. Then, use a Db2
client to load data directly from the S3 bucket to your Amazon RDS for Db2 database. Downtime
depends on the size of your database. For more information about using Amazon S3, see [Integrating an Amazon RDS for Db2 DB instance with
Amazon S3](db2-s3-integration.md "db2-s3-integration.md").

###### To migrate your Db2 database to RDS for Db2

1. Prepare to back up your database. Configure sufficient storage amount to hold the
   backup on your self-managed Db2 system.
2. Back up your database.
   1. Run the [db2look system command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-db2look-db2-statistics-ddl-extraction-tool "https://www.ibm.com/docs/en/db2/11.5?topic=commands-db2look-db2-statistics-ddl-extraction-tool") to extract the data
      definition language (DDL) file for all objects.
   2. Run either the [Db2 export utility](https://www.ibm.com/docs/en/db2/11.5?topic=utility-exporting-data "https://www.ibm.com/docs/en/db2/11.5?topic=utility-exporting-data"), the [db2move system command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-db2move-database-movement-tool "https://www.ibm.com/docs/en/db2/11.5?topic=commands-db2move-database-movement-tool"), or a [CREATE EXTERNAL TABLE statement](https://www.ibm.com/docs/en/db2/11.5?topic=statements-create-table-external "https://www.ibm.com/docs/en/db2/11.5?topic=statements-create-table-external") to unload
      the Db2 table data to storage on your Db2 system.

3. Move your backup to an Amazon S3 bucket. For more information, see [Integrating an Amazon RDS for Db2 DB instance with
   Amazon S3](db2-s3-integration.md "db2-s3-integration.md").

###### Note

If your database is large and would take a long time to transfer to an S3
bucket, you can order an AWS Snow Family device and ask AWS to perform
the backup. After you copy your files to the device and return it to the
Snow Family team, the team transfers your backed-up images to your S3
bucket. For more information, see the [AWS Snow Family documentation](../../../snowball.md "../../../snowball.md"). 4. Use a Db2 client to load data directly from your S3 bucket to your RDS for Db2
database. For more information, see [Migrating with Amazon S3](db2-migration-load-from-s3.md "db2-migration-load-from-s3.md").
