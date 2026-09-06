

# Transportation and Logistics Data Lake
<a name="transportation-logistics-data-lake"></a>

Publication date: **March 15, 2020 ([Diagram history](#diagram-history))**

This architecture shows how to break data silos and create a single repository for transportation and logistics data from multiple sources. You can use a fully managed, pay-per-use, and scalable architecture to remove the complexity and costs of managing on-premises databases.

## Transportation and Logistics Data Lake
<a name="diagram1"></a>

![Architecture diagram showing a transportation and logistics data lake with Amazon S3, Lake Formation, AWS Glue, and Athena.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/transportation-logistics-data-lake/images/transportation-logistics-data-lake.png)


The following steps describe the architecture:

1. Ingest data from multiple sources: historical and large databases with AWS Snowball, real-time data with [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), ERP data synchronization with AWS DataSync, and mobile app data with [Amazon AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html).

1. Automatically extract, transform, and load raw data with [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html). Discover schemas and create a data catalog for further data exploration.

1. Create an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) data lake where you can store, organize, and access business-critical data securely. Use Amazon EMR for fine-grained control over extraction, transformation, and loading (ETL) jobs. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) to manage your data catalog.

1. Turn raw data into actionable knowledge with [Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) and [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html). Disseminate key business intelligence insights across your organization. Use SageMaker AI to deliver ML-based predictive and prescriptive analytics.

1. Use AWS fully managed databases to deliver specific capabilities: Amazon Neptune graph database for network optimization, Amazon Aurora for fast relational queries, and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) for interactive mobile and web apps with real-time updates. Avoid data latency with live data stream ingestion from Amazon Kinesis.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 15, 2020 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.