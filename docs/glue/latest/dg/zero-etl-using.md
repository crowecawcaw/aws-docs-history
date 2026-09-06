

# Zero-ETL integrations
<a name="zero-etl-using"></a>

[Zero-ETL](https://aws.amazon.com/what-is/zero-etl/) is a set of fully managed integrations by AWS that minimizes the need to build ETL data pipelines for common ingestion and replication use cases. It makes data available in Lakehouse architecture of Amazon SageMaker and Amazon Redshift from multiple operational, transactional, and application sources. Currently AWS Glue Zero-ETL supports DynamoDB, Oracle Database@AWS and SaaS sources like Salesforce, SAP, Zendesk as sources. With zero-ETL integration, you have fresher data for analytics, AI/ML, and reporting. You get more accurate and timely insights for use cases like business dashboards, optimized gaming experience, data quality monitoring, and customer behavior analysis. You can make data-driven predictions with more confidence, improve customer experiences, and promote data-driven insights across the business.

Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to efficiently analyze all your data using your existing business intelligence tools.

Lakehouse architecture of Amazon SageMaker unifies all your data across Amazon Simple Storage Service (Amazon S3) data lakes and Amazon Redshift data warehouses, helping you build powerful analytics and AI/ML applications on a single copy of data. Lakehouse architecture of Amazon SageMaker gives you the flexibility to access and query your data in-place with all Apache Iceberg compatible tools and engines. Additionally, you can secure your data with integrated, fine-grained access controls, that are enforced across all your data in all analytic tools and engines. Define permissions once and confidently share data across your organization.

## Zero-ETL capabilities in AWS Glue
<a name="zero-etl-capabilities"></a>

Zero-ETL integrations in AWS Glue simplify data ingestion and replication from AWS data services and third-party applications to AWS destinations.

AWS services supported as zero-ETL sources in AWS Glue include:
+ Amazon DynamoDB
+ Oracle at AWS, ODB

Third-party applications supported as zero-ETL sources in AWS Glue include:
+ Facebook Ads
+ Instagram Ads
+ Salesforce
+ Salesforce Marketing Cloud Account Engagement
+ SAP OData
+ ServiceNow
+ Zendesk
+ Zoho CRM

Self-managed databases supported as zero-ETL sources in AWS Glue include:
+ Oracle
+ SQL Server
+ MySQL
+ PostgreSQL

For more information about zero-ETL integrations from self-managed sources, see [AWS zero-ETL integration for self-managed database sources](https://docs.aws.amazon.com/dms/latest/userguide/zero-etl.html).

AWS services supported by Zero-ETL targets in AWS Glue include:
+ General purpose Amazon S3 bucket via Lakehouse architecture of Amazon SageMaker
+ Amazon S3 Tables via Lakehouse architecture of Amazon SageMaker
+ Redshift Managed Storage via Lakehouse architecture of Amazon SageMaker
+ Amazon Redshift Datawarehouse

**Note**  
For self-managed database sources, you can replicate data only to an Amazon Redshift data warehouse. Other targets are not supported.