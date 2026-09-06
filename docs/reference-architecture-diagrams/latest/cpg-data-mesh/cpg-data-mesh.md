

# Consumer Packaged Goods Data Mesh
<a name="cpg-data-mesh"></a>

Publication date: **May 11, 2021 ([Diagram history](#cpgmesh-history))**

With this architecture, you can build a data mesh for consumer packaged goods (CPG) companies. Growth in online sales increases the amount of data that business operations generate and maintain. A data mesh follows principles of flexibility and domain-owned design while maintaining data properties throughout the lifecycle. You use [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) for centralized governance and [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) for data cataloging.

For more information about this architecture, see [How to Create a Modern CPG Data Architecture with Data Mesh](https://aws.amazon.com/blogs/industries/how-to-create-a-modern-cpg-data-architecture-with-data-mesh/) on the AWS Blog.

## CPG data mesh diagram
<a name="cpgmesh-diagram"></a>

![Data flowing from batch, streaming, and SFTP sources through domain-owned nodes managed by AWS Lake Formation, with metadata stored in AWS Glue and Amazon Neptune, and analytics through Amazon Athena and Amazon OpenSearch Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/cpg-data-mesh/images/cpg-data-mesh.png)


The following steps describe the architecture:

1. Data flows into AWS through batch processing, real-time streams, and Secure File Transfer Protocol (SFTP).

1. Data sources are managed by the business domain. Consumers and producers use organization-level blueprints that provide core services such as security, governance, IAM roles, and standards.

1. Manage metadata through multiple services. Use AWS Glue for data cataloging. Store data lineage in [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/). Store data contracts in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

1. Consumers search the data by using the contract properties.

1. Lake Formation provides centralized management of fine-grained permissions. It also supports automatic schema discovery and conversion to the required format.

1. Perform ML and analytics by using Lake Formation. This mesh node provides insights and strategy. Use [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/), [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/), and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for analysis.

## Further reading
<a name="cpgmesh-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="cpgmesh-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#cpgmesh-history) | Reference architecture diagram first published. | May 11, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.