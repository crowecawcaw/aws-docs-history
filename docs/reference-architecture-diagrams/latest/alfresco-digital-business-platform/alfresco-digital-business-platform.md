

# Alfresco Digital Business Platform on AWS
<a name="alfresco-digital-business-platform"></a>

Publication date: **March 1, 2023 ([Diagram history](#alfresco-diagram-history))**

With this architecture, you can deploy a highly available Alfresco Digital Business Platform on AWS. The platform offers Alfresco Content Services for enterprise content management (ECM) and Alfresco Process Services for business process management (BPM). You also get add-on components for search, information governance, rendition, and machine learning (ML).

## Alfresco Digital Business Platform on AWS
<a name="alfresco-diagram"></a>

![Architecture diagram for deploying Alfresco Digital Business Platform on AWS with Amazon S3, Amazon EC2, Amazon Aurora, and Amazon OpenSearch Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/alfresco-digital-business-platform/images/alfresco-digital-business-platform-on-aws-ra.png)


The following steps describe the architecture:

1. Users connect to applications through web browsers on a workstation or mobile device.

1. Alfresco Content Connector provides the extended content store in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) or Amazon S3 Glacier. [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/) Intelligent-Tiering is an option.

1. Alfresco Content Services (ACS) provides ECM capabilities with information governance.

1. Business connectors provide integrations with Google Docs, Salesforce, SAP, SAP Cloud, Microsoft Teams, Outlook, and Office.

1. Alfresco Intelligence Services is an add-on module to the Alfresco Transform engine. It integrates with [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html), [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html), and [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) for metadata extraction and image and text analysis.

1. Alfresco Search and Insight Engine uses Solr on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) and [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) to provide full-text search across metadata stored in the database. Alfresco Search Enterprise uses [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) as an alternative.

1. Alfresco Process Services is a BPM offering that can create, publish, and use business operations. It supports [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) and [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) (MySQL, Oracle, PostgreSQL, and Microsoft SQL Server).

1. Use the [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html) Alfresco data source connector for intelligent enterprise searches.

## Further reading
<a name="alfresco-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="alfresco-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#alfresco-diagram-history) | Reference architecture diagram first published. | March 1, 2023 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.