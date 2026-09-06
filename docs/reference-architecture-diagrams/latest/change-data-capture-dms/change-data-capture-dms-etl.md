

# Change Data Capture Using AWS DMS: Amazon S3 with ETL for Upsert
<a name="change-data-capture-dms-etl"></a>

This architecture shows how to use AWS Database Migration Service (AWS DMS) to create data pipelines with change data capture to build transactional data lakes.

## Change Data Capture Using AWS DMS: Amazon S3 with ETL for Upsert
<a name="diagram3"></a>

![Architecture diagram showing change data capture using AWS DMS with Amazon S3 and ETL for upsert using AWS Glue and Amazon EMR.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/change-data-capture-dms/images/change-data-capture-dms-3.png)


The following steps describe the architecture:

1. Sources for CDC include Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, Amazon Aurora, Amazon DocumentDB, and Amazon RDS.

1. AWS DMS helps you with one-time data migration of databases and continuous data replication. AWS DMS captures changes on the source database and applies them in a transactionally consistent way to the target.

1. The target for change data capture is [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

1. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) or Amazon EMR for extract, transform, load (ETL) upsert to Amazon S3 and Amazon Redshift.