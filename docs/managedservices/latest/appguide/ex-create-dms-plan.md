# AWS Database Migration Service (AWS DMS), before you begin

When planning a database migration using the AMS AWS DMS, consider the following:

- Source and target endpoints: You need to know what information and tables in the source database need to be migrated to the
  target database. AMS AWS DMS supports basic schema migration, including the creation of tables and primary keys.
  However, AMS AWS DMS doesn't automatically create secondary indexes, foreign keys, accounts, and so on in the target database. See
  [Sources for Data Migration](../../../dms/latest/userguide/CHAP_Source.md "../../../dms/latest/userguide/CHAP_Source.md") and
  [Targets for Data Migration](../../../dms/latest/userguide/CHAP_Target.md "../../../dms/latest/userguide/CHAP_Target.md") for more information.
- Schema/Code Migration: AMS AWS DMS doesn't perform schema or code conversion. You can use tools such as Oracle SQL Developer,
  MySQL Workbench, or pgAdmin III to convert your schema. If you want to convert an existing schema to a different database engine, you can use the
  [AWS Schema Conversion Tool](../../../SchemaConversionTool/latest/userguide/CHAP_SchemaConversionTool.md "../../../SchemaConversionTool/latest/userguide/CHAP_SchemaConversionTool.md").
  It can create a target schema and also can generate and create an entire schema: tables, indexes,
  views, and so on. You can also use the tool to convert PL/SQL or TSQL to PgSQL and other formats.
- Unsupported data types: Some source data types need to be converted into the equivalent data types for the target database.
  **AWS DMS scenarios to consider**

The following, documented, scenarios might help you craft your own database migration path.

- Migrate data from an on-prem MySQL server to Amazon RDS MySQL: See AWS blog post
  [Migrate On-Premises MySQL Data to Amazon RDS (and back)](https://aws.amazon.com/blogs/aws/migrate-mysql-data-to-amazon-rds-and-back/ "https://aws.amazon.com/blogs/aws/migrate-mysql-data-to-amazon-rds-and-back/")
- Migrate data from an Oracle database to Amazon RDS Aurora PostgreSQL database: See AWS blog post
  [A quick introduction to migrating from an Oracle database to an Amazon Aurora PostgreSQL database](https://aws.amazon.com/blogs/database/a-quick-introduction-to-migrating-from-an-oracle-database-to-an-amazon-aurora-postgresql-database/ "https://aws.amazon.com/blogs/database/a-quick-introduction-to-migrating-from-an-oracle-database-to-an-amazon-aurora-postgresql-database/")
- Migrate data from RDS MySQL to S3: See AWS blog post
  [How to archive data from relational
  databases to Amazon Glacier using AWS DMS](https://aws.amazon.com/blogs/database/archiving-data-from-relational-databases-to-amazon-glacier-via-aws-dms/ "https://aws.amazon.com/blogs/database/archiving-data-from-relational-databases-to-amazon-glacier-via-aws-dms/")
  For a database migration, you must do the following:

- Plan your database migration, this includes setting up a replication subnet group.
- Allocate a replication instance that performs all the processes for the migration.
- Specify a source and a target database endpoint.
- Create a task or set of tasks to define what tables and replication processes you want to use.
- Create the AWS DMS IAM `dms-cloudwatch-logs-role` and `dms-vpc-role` roles. If you use Amazon Redshift as a
  target database, you must also create and add the IAM role `dms-access-for-endpoint` to your AWS account. For more information, see
  [Creating the IAM roles to use with the AWS CLI and AWS DMS API](../../../dms/latest/userguide/CHAP_Security.md#CHAP_Security.APIRole "../../../dms/latest/userguide/CHAP_Security.md#CHAP_Security.APIRole").
  These walkthroughs provide an example of using the AMS console or AMS CLI to create an AWS Database Migration Service (AWS DMS).
  CLI commands for creating the AWS DMS replication instance, subnet group, and task as well as an AWS DMS source endpoint and target endpoint are provided.

To learn more about AMS AWS DMS, see [AWS Database Migration Service](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/") for general
information and [AWS Database Migration Service FAQs](https://aws.amazon.com/dms/faqs/ "https://aws.amazon.com/dms/faqs/") for answers to common questions.
