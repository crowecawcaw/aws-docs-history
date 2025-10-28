# Zero-ETL integrations

[Zero-ETL](https://aws.amazon.com/what-is/zero-etl/ "https://aws.amazon.com/what-is/zero-etl/") is a set of fully managed integrations by AWS that minimizes the need to build ETL data pipelines for common ingestion and replication use cases. It makes data available in Amazon SageMaker Lakehouse and Amazon Redshift from multiple operational, transactional, and application sources. With zero-ETL integration, you have fresher data for analytics, AI/ML, and reporting. You get more accurate and timely insights for use cases like business dashboards, optimized gaming experience, data quality monitoring, and customer behavior analysis. You can make data-driven predictions with more confidence, improve customer experiences, and promote data-driven insights across the business.

Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to efficiently analyze all your data using your existing business intelligence tools.

Amazon SageMaker Lakehouse unifies all your data across Amazon Simple Storage Service (S3) data lakes and Amazon Redshift data warehouses, helping you build powerful analytics and AI/ML applications on a single copy of data. SageMaker Lakehouse gives you the flexibility to access and query your data in-place with all Apache Iceberg compatible tools and engines. With SageMaker Lakehouse, you also have the ﬂexibility to access and query your data in-place with Apache Iceberg compatible tools and engines. Additionally, you can secure your data with integrated, fine-grained access controls, that are enforced across all your data in all analytic tools and engines. Define permissions once and confidently share data across your organization.

## Zero-ETL capabilities in AWS Glue

Zero-ETL integrations in AWS Glue simplify data ingestion and replication from AWS data services and third-party applications to AWS destinations.

AWS services supported by zero-ETL sources in AWS Glue include:

- Amazon DynamoDB

Third-party application supported by zero-ETL include:

- Facebook Ads
- Instagram Ads
- Salesforce
- Salesforce Marketing Cloud Account Engagement
- SAP OData
- ServiceNow
- Zendesk
- Zoho CRM

AWS services supported by zero-ETL targets in AWS Glue include:

- Amazon Redshift
- Amazon SageMaker Lakehouse

###### Note

When creating a zero-ETL integration with an Amazon DynamoDB source in AWS Glue, the target is supported by Amazon SageMaker Lakehouse.
