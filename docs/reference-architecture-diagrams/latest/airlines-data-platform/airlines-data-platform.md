

# Airlines Data Platform
<a name="airlines-data-platform"></a>

Publication date: **August 23, 2022 ([Diagram history](#airlines-data-platform-history))**

This reference architecture provides a data platform for airlines that replaces or augments on-premises data infrastructure. Airlines use this architecture to build domain-owned data products with separated storage and compute. The platform supports flight operations, passenger services, and loyalty program domains.

Airline initiatives to build operations data stores often don't adapt to change. Rigid schemas, long implementation times, siloed operations, and on-premises scaling limitations restrict agility. This data platform architecture relieves or replaces your on-premises data platform load. It increases development agility and cost savings.

This architecture uses the [Implementing Travel and Hospitality Data Mesh](../travel-hospitality-data-mesh/travel-hospitality-data-mesh.html) as its foundation for a domain-owned design approach.

## Airlines data platform diagram
<a name="airlines-data-platform-diagram"></a>

![Architecture for airline data platform using Amazon S3, Amazon Redshift, AWS Glue, and Amazon SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/airlines-data-platform/images/svoc_data_platform_travel_ra.png)


The following steps describe the architecture:

1. Build data products for relevant domains such as flight, passenger, and loyalty. Separate storage from compute to scale each independently.

1. In the operational data store, use managed services and purpose-built databases with microservice and event-driven patterns. This replaces expensive on-premises infrastructure. It eliminates operational databases, service-oriented architecture (SOA) infrastructure, and message-oriented middleware.

1. Use open standards to build a data lake with [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Use a read-pattern schema to make raw and curated data available for all user roles.

1. For known query patterns, build standard enterprise data warehouse schemas in [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/). Build data marts in Amazon Redshift for heavily used analytics. For ad hoc queries, publish the data catalog in [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/). Use [Athena](https://docs.aws.amazon.com/athena/latest/ug/) to query the data lake directly.

1. Use [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for standard AI/ML models. Build customer segmentation and lifetime value models on top of the data lake.

## Further reading
<a name="airlines-data-platform-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="airlines-data-platform-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#airlines-data-platform-history) | Reference architecture diagram first published. | August 23, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.