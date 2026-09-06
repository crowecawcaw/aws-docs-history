

# Lodging Data Platform
<a name="lodging-data-platform"></a>

Publication date: **October 7, 2022 ([Diagram history](#ldp-history))**

With this architecture, you can build a data platform that serves both operational and analytics needs for lodging companies. Use open data standards and separate storage from compute. You use [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for the data lake, [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for operational data, and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for artificial intelligence (AI) and machine learning (ML) models.

## Lodging data platform diagram
<a name="ldp-diagram"></a>

![How to build a lodging data platform by using Amazon Simple Storage Service, Amazon DynamoDB, and Amazon SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/lodging-data-platform/images/lodging-data-platform.png)


The following steps describe the architecture:

1. Build basic data as a service with the most important domains: properties, reservations, stays, and loyalty. Separate storage from compute as a key design tenet.

1. Use purpose-built databases and serverless architecture to deliver microservices and events for the operational data store. Use DynamoDB, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) to scale based on adoption. Replace expensive on-premises operational databases and service-oriented architecture (SOA) infrastructure.

1. Use open standards to build the data lake with the same data as the operational platform. Use a read pattern schema to make raw and curated data available for all user roles. Process data by using [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/).

1. Build standard enterprise data warehouse schemas and data marts in [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/) for known usage patterns. For one-time requirements, publish the data catalog and use [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) for analysis directly from the data lake.

1. Use SageMaker AI to provide standard AI and ML models for customer segmentation and lifetime value. Build custom models on top of the data.

## Further reading
<a name="ldp-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ldp-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#ldp-history) | Reference architecture diagram first published. | October 7, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.