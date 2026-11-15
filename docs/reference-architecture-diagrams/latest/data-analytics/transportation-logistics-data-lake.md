

# Transportation and logistics data lake
<a name="transportation-logistics-data-lake"></a>

Publication date: **March 15, 2020 ([Diagram history](diagram-history.md))**

This architecture shows how to break data silos and create a single repository for transportation and logistics data from multiple sources. You can use a fully managed, pay-per-use, and scalable architecture to remove the complexity and costs of managing on-premises databases.

## Transportation and logistics data lake diagram
<a name="transportation-logistics-data-lake-diagram1"></a>

![Data from sources lands in an Amazon S3 data lake governed by Lake Formation, cataloged by AWS Glue, analyzed with Athena.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/transportation-logistics-data-lake.png)


The following steps describe the architecture:

1. Ingest data from multiple sources: historical and large databases with AWS Snowball, real-time data with [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/), ERP data synchronization with [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/), and mobile app data with [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/).

1. Automatically extract, transform, and load raw data with [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/). Discover schemas and create a data catalog for further data exploration.

1. Create an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) data lake where you can store, organize, and access business-critical data securely. Use [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) for fine-grained control over extraction, transformation, and loading (ETL) jobs. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) to manage your data catalog.

1. Turn raw data into actionable knowledge with [Athena](https://docs.aws.amazon.com/athena/latest/ug/) and [AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/). Disseminate key business intelligence insights across your organization. Use [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) to deliver ML-based predictive and prescriptive analytics.

1. Use AWS fully managed databases to deliver specific capabilities: [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/) graph database for network optimization, [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) for fast relational queries, and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for interactive mobile and web apps with real-time updates. Avoid data latency with live data stream ingestion from Kinesis Data Streams.

## Further reading
<a name="transportation-logistics-data-lake-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)