

# Data Mesh Reference Architecture with Amazon DataZone
<a name="data-mesh-datazone"></a>

Publication date: **November 20, 2024 ([Diagram history](#diagram-history))**

Data mesh is a decentralized architectural and organizational framework that helps organizations accelerate innovation and drive business value. This architecture shows how to use [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/what-is-datazone.html) to build a data mesh-based data solution.

## Data Mesh Reference Architecture with Amazon DataZone
<a name="diagram1"></a>

![Architecture diagram showing a data mesh using Amazon DataZone with Amazon S3, AWS Glue, Amazon Redshift, and SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-mesh-datazone/images/data-mesh-datazone.png)


The following steps describe the architecture:

1. Gather data from sources across the enterprise through databases, file shares, edge devices, logs, social networks, SaaS applications, and streaming media.

1. Based on the source system and end user requirements, ingest raw data using [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html), [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html), [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html), and Amazon Managed Streaming for Apache Kafka.

1. In the producer account, transform raw data using [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html). Store metadata in AWS Glue Data Catalog, measure data quality using AWS Glue Data Quality, and register data in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html), [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html), and third-party sources as assets in the Amazon DataZone catalog using data source jobs.

1. The central governance account hosts the Amazon DataZone domain and the related data portal. Associate AWS accounts of data producers and consumers with the Amazon DataZone domain, and create projects under related domain units.

1. End users log into the Amazon DataZone data portal using IAM credentials or single sign-on (SSO) through [https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html). They search, filter, and view asset information including data quality, business metadata, and technical metadata.

1. When end users find assets of interest, they request access using the subscription feature of Amazon DataZone. The asset owner approves or rejects the request based on validity.

1. After the subscription request is granted and fulfilled, access the asset in the consumer account for AI/ML model development using [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), and for analytics and reporting use [Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html), Amazon Redshift, and [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 20, 2024 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.