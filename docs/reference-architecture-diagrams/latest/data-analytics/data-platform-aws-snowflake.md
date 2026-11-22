

# Modern data platform using AWS and Snowflake

Publication date: **March 11, 2022 ([Diagram history](diagram-history.md))**

This architecture shows how to build an end-to-end modern data analytics platform using AWS and Snowflake. You can ingest data from multiple sources, store it in a data lake, and use Snowflake as a virtual data warehouse for analytics.

## Modern data platform using AWS and Snowflake diagram
<a name="data-platform-aws-snowflake-diagram1"></a>

![Architecture diagram of a modern data platform using AWS and Snowflake with Amazon S3, AWS Glue, and Lake Formation.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/data-platform-aws-snowflake.png)


The following steps describe the architecture:

1. Collect data from multiple data sources across the enterprise, software as a service (SaaS) applications, edge devices, logs, streaming data, and social media networks.

1. Based on the type of data source, use [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/), [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/), [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/), [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/), and [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/) to ingest the data into the data lake.

1. [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) provides fully managed, highly available, and scalable data lake storage.

1. AWS Glue extracts, transforms, and ingests data across multiple data stores. [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) provides the cloud big data platform for processing vast amounts of data using open-source analytics frameworks. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) and [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) provide compute capability for data enrichment.

1. [Amazon Managed Workflows for Apache Airflow (MWAA)](https://docs.aws.amazon.com/mwaa/latest/userguide/) or [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) orchestrates end-to-end data pipelines.

1. [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) makes it easy to build, secure, and manage your data lake. It provides a single place to enforce data classification and manage fine-grained access. [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/) and AWS STS manage access permissions and temporary credentials.

1. Snowflake serves as a virtual data warehouse with the ability to query Amazon S3 using external tables, and automated and continuous data ingestion using Snowpipe.

1. [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) builds, trains, and deploys machine learning (ML) models and adds intelligence to your applications. [AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/) provides ML-powered business intelligence (BI).

## Further reading
<a name="data-platform-aws-snowflake-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)