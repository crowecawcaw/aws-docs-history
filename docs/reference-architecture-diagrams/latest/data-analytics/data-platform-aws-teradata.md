

# Modern data platform using AWS and Teradata

Publication date: **November 18, 2022 ([Diagram history](diagram-history.md))**

Teradata VantageCloud Enterprise is part of the Teradata VantageCloud offering, the complete cloud analytics and data platform that includes Teradata ClearScape Analytics and integration with [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/).

## Modern data platform using AWS and Teradata diagram
<a name="data-platform-aws-teradata-diagram1"></a>

![Architecture diagram showing a data platform using AWS and Teradata with Amazon S3, AWS Glue, Amazon EMR, and SageMaker AI.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/data-platform-aws-teradata.png)


The following steps describe the architecture:

1. Collect data from multiple sources across the enterprise and SaaS applications. Ingest data using [AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/), [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) (AWS DMS), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), and [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/). AWS Data Exchange, AWS DMS, and [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/) use [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) as a transitional or permanent datastore accessed through Teradata Native Object Store (NOS).

1. The AWS data lake manages data lifecycle and governance. Amazon S3 provides highly available storage for permanent and transitional data in the data lake.

1. Process the data using [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/), and store it to Amazon S3 or directly into Teradata using AWS Glue streaming.

1. Teradata Vantage on AWS serves as a highly scalable data warehouse and analytics platform. With Teradata QueryGrid, the analytics platform can query other datastores such as SQL databases and Amazon EMR. Teradata NOS allows Teradata Vantage to access and configure data on Amazon S3 as an external table.

1. SageMaker AI retrieves training data from both Teradata and Amazon S3 using the Teradata SQL kernel or Python library. Deploy trained models to a SageMaker AI endpoint or import them as a bring your own model (BYOM) into Teradata for in-database analytics.

1. External functions within Teradata SQL interface get inference from AWS inference endpoints and third-party AI platform providers.

## Further reading
<a name="data-platform-aws-teradata-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)