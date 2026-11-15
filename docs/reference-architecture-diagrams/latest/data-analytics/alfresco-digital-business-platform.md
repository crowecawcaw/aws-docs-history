

# Alfresco Digital Business Platform on AWS
<a name="alfresco-digital-business-platform"></a>

Publication date: **March 1, 2023 ([Diagram history](diagram-history.md))**

With this architecture, you can deploy a highly available Alfresco Digital Business Platform on AWS. The platform offers Alfresco Content Services for enterprise content management (ECM) and Alfresco Process Services for business process management (BPM). You also get add-on components for search, information governance, rendition, and machine learning (ML).

## Alfresco Digital Business Platform on AWS diagram
<a name="alfresco-diagram"></a>

![Architecture diagram for deploying Alfresco Digital Business Platform on AWS with content, process, and search components.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/alfresco-digital-business-platform-on-aws-ra.png)


The following steps describe the architecture:

1. Users connect to applications through web browsers on a workstation or mobile device.

1. Alfresco Content Connector provides the extended content store in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) or Amazon S3 Glacier. [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/) Intelligent-Tiering is an option.

1. Alfresco Content Services (ACS) provides ECM capabilities with information governance.

1. Business connectors provide integrations with Google Docs, Salesforce, SAP, SAP Cloud, Microsoft Teams, Outlook, and Office.

1. Alfresco Intelligence Services is an add-on module to the Alfresco Transform engine. It integrates with [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/), [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/), and [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/) for metadata extraction and image and text analysis.

1. Alfresco Search and Insight Engine uses Solr on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) and [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/) to provide full-text search across metadata stored in the database. Alfresco Search Enterprise uses [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) as an alternative.

1. Alfresco Process Services is a BPM offering that can create, publish, and use business operations. It supports [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) and [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) (MySQL, Oracle, PostgreSQL, and Microsoft SQL Server).

1. Use the [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/) Alfresco data source connector for intelligent enterprise searches.

## Further reading
<a name="alfresco-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)