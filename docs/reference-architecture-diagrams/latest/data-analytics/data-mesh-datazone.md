

# Data mesh with Amazon DataZone

Publication date: **November 20, 2024 ([Diagram history](diagram-history.md))**

Data mesh is a decentralized architectural and organizational framework that helps organizations accelerate innovation and drive business value. This architecture shows how to use [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/) to build a data mesh-based data solution. In this architecture, a producer account ingests and transforms raw data, then registers it as assets in the Amazon DataZone catalog. A central governance account hosts the Amazon DataZone domain and data portal, where consumers discover assets and request access through subscriptions. After the asset owner approves a subscription request, consumers access the data in the consumer account for analytics and machine learning.

## Data mesh with Amazon DataZone diagram
<a name="data-mesh-datazone-diagram1"></a>

![Architecture diagram showing a data mesh using Amazon DataZone with Amazon S3, AWS Glue, Amazon Redshift, and SageMaker AI.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/data-mesh-datazone.png)


The following steps describe the architecture:

1. Gather data from sources across the enterprise through databases, file shares, edge devices, logs, social networks, SaaS applications, and streaming media.

1. Based on the source system and end user requirements, ingest raw data using [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/), [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/), [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), and [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/).

1. In the producer account, transform raw data using [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/). Store metadata in AWS Glue Data Catalog, measure data quality using AWS Glue Data Quality, and register data in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/), [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), and third-party sources as assets in the Amazon DataZone catalog using data source jobs.

1. The central governance account hosts the Amazon DataZone domain and the related data portal. Associate AWS accounts of data producers and consumers with the Amazon DataZone domain, and create projects under related domain units.

1. End users log in to the Amazon DataZone data portal using [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/) credentials or single sign-on (SSO) through [https://docs.aws.amazon.com/singlesignon/latest/userguide/](https://docs.aws.amazon.com/singlesignon/latest/userguide/). They search, filter, and view asset information including data quality, business metadata, and technical metadata.

1. When end users find assets of interest, they request access using the subscription feature of Amazon DataZone. The asset owner approves or rejects the request based on validity.

1. After the subscription request is granted and fulfilled, access the asset in the consumer account for AI/ML model development using [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/), and for analytics and reporting use [Athena](https://docs.aws.amazon.com/athena/latest/ug/), Amazon Redshift, and [AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/).

## Further reading
<a name="data-mesh-datazone-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)