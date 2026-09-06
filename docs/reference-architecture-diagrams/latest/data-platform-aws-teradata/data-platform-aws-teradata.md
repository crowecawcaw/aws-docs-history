

# Modern Data Platform Using AWS and Teradata
<a name="data-platform-aws-teradata"></a>

Publication date: **November 18, 2022 ([Diagram history](#diagram-history))**

Teradata VantageCloud Enterprise is part of the Teradata VantageCloud offering, the complete cloud analytics and data platform that includes Teradata ClearScape Analytics and integration with [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html).

## Modern Data Platform Using AWS and Teradata
<a name="diagram1"></a>

![Architecture diagram showing a modern data platform using AWS and Teradata with Amazon S3, AWS Glue, Amazon EMR, and SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-platform-aws-teradata/images/data-platform-aws-teradata.png)


The following steps describe the architecture:

1. Collect data from multiple sources across the enterprise and SaaS applications. Ingest data using [AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/what-is.html), [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) (AWS DMS), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html), and [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/introduction.html). AWS Data Exchange, AWS DMS, and [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html) use Amazon S3 as a transitional or permanent datastore accessed through Teradata Native Object Store (NOS).

1. The AWS data lake manages data lifecycle and governance. [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) provides highly available storage for permanent and transitional data in the data lake.

1. Process the data using [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html), and store it to Amazon S3 or directly into Teradata using AWS Glue streaming.

1. Teradata Vantage on AWS serves as a highly scalable data warehouse and analytics platform. With Teradata QueryGrid, the analytics platform can query other datastores such as SQL databases and Amazon EMR. Teradata NOS allows Teradata Vantage to access and configure data on Amazon S3 as an external table.

1. SageMaker AI retrieves training data from both Teradata and Amazon S3 using the Teradata SQL kernel or Python library. Deploy trained models to a SageMaker AI endpoint or import them as a bring your own model (BYOM) into Teradata for in-database analytics.

1. External functions within Teradata SQL interface get inference from AWS inference endpoints and third-party AI platform providers.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 18, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.