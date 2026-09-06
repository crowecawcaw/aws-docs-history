

# Migrating a SQL Server AlwaysOn Database on Primary Replica to Amazon Aurora PostgreSQL
<a name="chap-manageddatabases.sqlserveralwayson2aurorapostgresql"></a>

In this walkthrough we will cover the process of migrating a database from SQL Server AlwaysOn Primary Replica to Amazon Aurora PostgreSQL using AWS Database Migration Service (AWS DMS). We will highlight common migration issues, and methods to overcome them. We will also guide you through the process of our automatic SQL scripts to arrange the tables, prepare the JSON table mappings, and explore methods of distributing tables across multiple DMS tasks for optimal efficiency.

## Why Amazon Aurora PostgreSQL?
<a name="chap-manageddatabases.sqlserveralwayson2aurorapostgresql.whyaurora"></a>

Most organizations use online transaction process (OLTP) database with mixed workloads running on SQL Server AlwaysOn platform. Because of the advanced capabilities and cost-effectiveness of open-source databases, many corporations are moving away from legacy, on-premise SQL Server AlwaysOn environments running high-profile workloads to robust, cloud-based, highly scalable, and resilient solutions.

Organizations prefer to migrate their data to PostgreSQL because it’s an open-source database solution which offers advanced RDBMS capabilities without commercial licensing costs. PostgreSQL is also backed by community base support which isn’t dependent on any specific vendor. Running critical workloads within a robust, secure, and redundant cloud base infrastructure also brings resiliency benefits without high cap-ex costs of maintaining multiple data centers. For more information, see [Working with Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html). For the latest features and key benefits, see [Amazon Aurora PostgreSQL](https://aws.amazon.com/rds/postgresql/?nc=sn&loc=3&dn=3).

## Common database migration challenges
<a name="chap-manageddatabases.sqlserveralwayson2aurorapostgresql.commonchallenges"></a>

Following are some common migration problems that could potentially drain project resources and derail data migration project timelines.
+ Underestimating the complexity of the table structure - A typical application user may not be aware of the specific table fields that hold all the data elements. A manual data migration process often results in incomplete, inaccurate, and outdated information being transferred to the target endpoint.
+ Lack of integrated workflow processes - A database migration typically involves disparate teams using various tools to interact with the data. When you use spreadsheets or other manual methods to document data specifications, human errors can easily occur, resulting in wasted time, and resources or incomplete migration.
+ Inability to validate data transformation specifications - With ongoing data changes on the source endpoint, it’s quite difficult to manually validate all migrated data. Sample-based data validation often results in missed discrepancies which may have negative repercussions post-migration.

## Why AWS DMS?
<a name="chap-manageddatabases.sqlserveralwayson2aurorapostgresql.whydms"></a>

 AWS DMS is a managed-service which provides an out-of-box migration solution that helps you mitigate the aforementioned migration challenges. AWS DMS offers the following key benefits. For complete list of feature benefits, see [AWS Database Migration Service Features](https://aws.amazon.com/dms/features).
+ Cost-effectiveness – you pay only for the compute and log storage resources used during your migration.
+ Ongoing data replication capability that allows you to complete your application cutover without disrupting your DevOps and business processes. You can also enable data validation on a task to ensure that no outdated information is being transferred to the target endpoint.
+ Automatically analyze the source table schema and structure, and retrieve the specific table fields that hold all the data elements, and reduce the need for you to manually gather the data specifications.
+ Ability to integrate with other AWS services such as CloudWatch. With CloudWatch, you can create custom alarms that watch DMS metrics and send notifications when a threshold limit is reached. For more information, see [Monitoring AWS DMS tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html).

## Migration overview
<a name="chap-manageddatabases.sqlserveralwayson2aurorapostgresql.migrationoverview"></a>

The following image shows a high-level architecture of the AWS DMS replication workflow. AWS DMS migration consists of an EC2 replication instance which hosts the DMS software. The replication instance handles the execution of one or more DMS tasks. Each task replicates a specific set of table data from the SQL Server AlwaysOn primary replica source to the Amazon Aurora PostgreSQL target endpoint. For more information, see [Working with an AWS DMS replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html). For a complete migration playbook, see [Microsoft SQL Server to Amazon Aurora PostgreSQL Migration Playbook](https://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/chap-sql-server-aurora-pg.html).

![Migration overview](http://docs.aws.amazon.com/dms/latest/sbs/images/sqlserver2postgresql.png)


In the rest of this document, we’ll migrate a sample financial institution database from SQL Server AlwaysOn to Aurora PostgreSQL. The database includes tables containing large object (LOB) data types with either a primary key or unique key. Tables with these characteristics pose different migration challenges which will also be discussed. The entity relationship diagram of the sample database is shown below.

![Entity relationship diagram](http://docs.aws.amazon.com/dms/latest/sbs/images/sqlserver2postgresql_schema.png)
