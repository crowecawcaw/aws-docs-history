

# Unified Data Access Governance in a Data Mesh
<a name="unified-data-access-governance"></a>

Publication date: **February 13, 2023 ([Diagram history](#diagram-history))**

PrivaceraCloud provides federated computation governance for consistent data access control, governed data sharing, and compliance across AWS services and external on-premises data sources.

## Unified Data Access Governance in a Data Mesh Using PrivaceraCloud on AWS
<a name="diagram1"></a>

![Architecture diagram showing unified data access governance in a data mesh using PrivaceraCloud with Amazon S3, AWS Glue, Amazon Redshift, and Athena.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/unified-data-access-governance/images/unified-data-access-governance.png)


The following steps describe the architecture:

1. Data flows into AWS through batch processing, real-time data, or change data capture (CDC).

1. The producer domain manages data sources. Raw data is stored in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) and processed using [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html), [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), and [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).

1. Metadata is managed through multiple services. AWS Glue provides data cataloging for discovery and governance.

1. The consumer domain uses processed data sets from multiple producer domains based on business needs. Consumers build a data mart using [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html) and [Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html).

1. Consumers search and filter data sets recorded in the central data catalog by name, contents, sensitivity, or custom labels.

1. PrivaceraCloud delivers unified data access governance as a fully managed SaaS solution. Built on the attribute-based access control (ABAC) policy model of Apache Ranger, it applies governance to Amazon S3, AWS Glue, Amazon EMR, Amazon RDS, DynamoDB, Athena, and Amazon Redshift.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | February 13, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.