

# Modern Data Platform Using AWS and Snowflake
<a name="data-platform-aws-snowflake"></a>

Publication date: **March 11, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to build an end-to-end modern data analytics platform using AWS and Snowflake. You can ingest data from multiple sources, store it in a data lake, and use Snowflake as a virtual data warehouse for analytics.

## Modern Data Platform Using AWS and Snowflake
<a name="diagram1"></a>

![Architecture diagram showing a modern data platform using AWS and Snowflake with Amazon S3, AWS Glue, Lake Formation, and Step Functions.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-platform-aws-snowflake/images/data-platform-aws-snowflake.png)


The following steps describe the architecture:

1. Collect data from multiple data sources across the enterprise, software as a service (SaaS) applications, edge devices, logs, streaming data, and social media networks.

1. Based on the type of data source, use [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html), AWS DataSync, [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), Amazon Managed Streaming for Apache Kafka, AWS IoT Core, [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html), and Amazon AppFlow to ingest the data into the data lake.

1. [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) provides fully managed, highly available, and scalable data lake storage.

1. AWS Glue extracts, transforms, and ingests data across multiple data stores. Amazon EMR provides the cloud big data platform for processing vast amounts of data using open-source analytics frameworks. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) and Amazon EC2 provide compute capability for data enrichment.

1. Amazon Managed Workflows for Apache Airflow (MWAA) or [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) orchestrates end-to-end data pipelines.

1. [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) makes it easy to build, secure, and manage your data lake. It provides a single place to enforce data classification and manage fine-grained access. IAM and AWS STS manage access permissions and temporary credentials.

1. Snowflake serves as a virtual data warehouse with the ability to query Amazon S3 using external tables, and automated and continuous data ingestion using SnowPipe.

1. SageMaker AI builds, trains, and deploys machine learning (ML) models and adds intelligence to your applications. [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) provides ML-powered business intelligence (BI).

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 11, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.