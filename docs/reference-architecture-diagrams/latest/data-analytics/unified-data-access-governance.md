

# Unified data access governance in a data mesh
<a name="unified-data-access-governance"></a>

Publication date: **February 13, 2023 ([Diagram history](diagram-history.md))**

PrivaceraCloud provides federated computation governance for consistent data access control, governed data sharing, and compliance across AWS services and external on-premises data sources.

## Unified data access governance in a data mesh diagram
<a name="unified-data-access-governance-diagram1"></a>

![PrivaceraCloud governs data access across Amazon S3, AWS Glue, Amazon EMR, Athena, and Amazon Redshift in a data mesh.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/unified-data-access-governance.png)


The following steps describe the architecture:

1. Data flows into AWS through batch processing, real-time data, or change data capture (CDC).

1. The producer domain manages data sources, storing raw data in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) and processing it using [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/), [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/), and [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/).

1. AWS Glue and other services manage metadata, and AWS Glue catalogs data for discovery and governance.

1. The consumer domain uses processed data sets from multiple producer domains based on business needs. Consumers build a data mart using [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) and [Athena](https://docs.aws.amazon.com/athena/latest/ug/).

1. Consumers search and filter data sets recorded in the central data catalog by name, contents, sensitivity, or custom labels.

1. PrivaceraCloud delivers unified data access governance as a fully managed SaaS solution. Built on the attribute-based access control (ABAC) policy model of Apache Ranger, it applies governance to Amazon S3, AWS Glue, Amazon EMR, Amazon RDS, DynamoDB, Athena, and Amazon Redshift.

## Further reading
<a name="unified-data-access-governance-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)