

# Change Data Capture Using AWS DMS: Streaming
<a name="change-data-capture-dms-streaming"></a>

This architecture shows how to use AWS Database Migration Service (AWS DMS) to ingest real-time changes from source databases through streaming services.

## Change Data Capture Using AWS DMS: Streaming
<a name="diagram2"></a>

![Architecture diagram showing change data capture using AWS DMS to stream data through Amazon Kinesis and Amazon Managed Streaming for Apache Kafka.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/change-data-capture-dms/images/change-data-capture-dms-2.png)


The following steps describe the architecture:

1. Sources for CDC include Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, Amazon Aurora, Amazon DocumentDB, and Amazon RDS.

1. AWS DMS helps you with one-time data migration of databases and continuous data replication. AWS DMS captures changes on the source database and applies them in a transactionally consistent way to the target.

1. Use AWS DMS to stream data to an [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) data stream and Amazon Managed Streaming for Apache Kafka (Amazon MSK) to collect and process large streams of data.

1. Use purpose-built services for analytics in your data lake or data warehouse.

1. Visualize and consume data using [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) and SageMaker AI Notebooks.