

# Implementing Travel and Hospitality Data Mesh
<a name="travel-hospitality-data-mesh"></a>

Publication date: **August 3, 2021 ([Diagram history](#travel-hospitality-data-mesh-history))**

The travel and hospitality industries face challenges when generating, accessing, and analyzing data at scale. Use this approach to build a data platform that serves both operational and analytical needs.

This architecture uses domain-owned design, maintained data properties, open data standards, purpose-built databases, and extensible serverless architecture. It helps relieve and eventually replace on-premises data platform load.

## Domain architecture diagram
<a name="travel-hospitality-data-mesh-diagram-1"></a>

![Domain architecture for data mesh using DynamoDB, Amazon Redshift, AWS Glue, and Lake Formation.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/travel-hospitality-data-mesh/images/implementing-travel-and-hospitality-data-mesh-ra-1.png)


The following steps describe the domain architecture:

1. Data flows into AWS through batch processing, real-time data, SFTP, and Internet of Things (IoT) sensors.

1. Data sources are managed by the business domain. Producers use organization-level blueprints for security, governance, and open standards. Producers build the operational data store by using [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) and DynamoDB Accelerator (DAX) for consistent single-digit-millisecond latency.

1. Consumer domains process data sets from multiple producer domains based on business needs. Build data marts in [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) and analytics in [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).

1. Manage metadata through multiple services. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) for data cataloging. Store data lineage in [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/). Store data contracts in DynamoDB.

1. Consumers search and filter data sets in the central data catalog. Filter by name, contents, sensitivity, or custom labels.

1. [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) provides centralized management of security, governance, and auditing with fine-grained permissions. It provides automatic schema discovery and format conversion.

1. Perform machine learning (ML) by using Lake Formation. Use [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for standard AI/ML models. Use [Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/) for actionable insights.

## Service architecture diagram
<a name="travel-hospitality-data-mesh-diagram-2"></a>

![Service architecture for data mesh using Amazon S3, AWS Glue, Amazon Redshift, and Amazon SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/travel-hospitality-data-mesh/images/implementing-travel-and-hospitality-data-mesh-ra-2.png)


The following steps describe the service architecture:

1. Data flows into AWS through batch, real-time, SFTP, and IoT sensors.

1. Stage all batch and real-time data in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. AWS Glue crawler creates table metadata in the data catalog.

1. Use open standards to build the data lake. Use a read-pattern schema for raw and curated data.

1. Use purpose-built databases like DynamoDB and serverless architecture for microservices and events in the operational data store.

1. Build reportable data sets in Amazon S3. Use Amazon Redshift and [Athena](https://docs.aws.amazon.com/athena/latest/ug/) for analytics. For ad hoc requirements, use Athena with standard SQL.

1. Use SageMaker AI for AI/ML models.

1. Use a [multi-account strategy](../account-security-data-platform/account-security-data-platform.html) for resource and security isolation.

## Further reading
<a name="travel-hospitality-data-mesh-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="travel-hospitality-data-mesh-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#travel-hospitality-data-mesh-history) | Reference architecture diagram first published. | August 3, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.