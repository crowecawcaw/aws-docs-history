

# Change data capture using AWS Database Migration Service
<a name="change-data-capture-dms"></a>

Publication date: **August 2, 2021 ([Diagram history](diagram-history.md))**

This architecture shows how to use [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) (AWS DMS) for change data capture (CDC) to migrate databases using ongoing replication.

## Migrate and replicate
<a name="change-data-capture-dms-migrate"></a>

![Architecture diagram showing change data capture using AWS DMS to migrate and replicate databases.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/change-data-capture-dms-1.png)


The following steps describe the architecture:

1. Sources for CDC include [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/), [Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/devguide/), [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), MongoDB, MySQL, Oracle, PostgreSQL, and SQL Server.

1. [AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/) makes heterogeneous database migrations predictable by automatically converting the source database schema and a majority of code objects to a format compatible with the target database.

1. AWS DMS helps you with one-time data migration of databases and continuous data replication. AWS DMS captures changes on the source database and applies them in a transactionally consistent way to the target.

1. Targets for CDC include Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, Amazon Aurora, Amazon DocumentDB, Amazon RDS, and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

## Streaming
<a name="change-data-capture-dms-streaming"></a>

This architecture shows how to use AWS Database Migration Service (AWS DMS) to ingest real-time changes from source databases through streaming services.

![Architecture diagram showing change data capture using AWS DMS to stream data through Amazon Kinesis and Amazon MSK.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/change-data-capture-dms-2.png)


The following steps describe the architecture:

1. Sources for CDC include Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, Amazon Aurora, Amazon DocumentDB, and Amazon RDS.

1. AWS DMS helps you with one-time data migration of databases and continuous data replication. AWS DMS captures changes on the source database and applies them in a transactionally consistent way to the target.

1. Use AWS DMS to stream data to an [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/) data stream and [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/) (Amazon MSK) to collect and process large streams of data.

1. Use purpose-built services for analytics in your data lake or data warehouse.

1. Visualize and consume data using [AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/) and [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) Notebooks.

## Amazon S3 with ETL for upsert
<a name="change-data-capture-dms-etl"></a>

This architecture shows how to use AWS Database Migration Service (AWS DMS) to create data pipelines with change data capture to build transactional data lakes.

![Architecture diagram showing change data capture using AWS DMS with Amazon S3 and ETL upsert using AWS Glue and Amazon EMR.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/change-data-capture-dms-3.png)


The following steps describe the architecture:

1. Sources for CDC include Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, Amazon Aurora, Amazon DocumentDB, and Amazon RDS.

1. AWS DMS helps you with one-time data migration of databases and continuous data replication. AWS DMS captures changes on the source database and applies them in a transactionally consistent way to the target.

1. The target for change data capture is Amazon S3.

1. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) or [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) for extract, transform, load (ETL) upsert to Amazon S3 and [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/).

## Further reading
<a name="change-data-capture-dms-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)