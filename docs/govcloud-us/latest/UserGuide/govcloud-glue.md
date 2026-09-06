

# AWS Glue in AWS GovCloud (US)
<a name="govcloud-glue"></a>

AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics. You can create and run an ETL job with a few clicks in the AWS Management Console. You simply point AWS Glue to your data stored on AWS, and AWS Glue discovers your data and stores the associated metadata (e.g. table definition and schema) in the AWS Glue Data Catalog. Once cataloged, your data is immediately searchable, queryable, and available for ETL.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS Glue differs
<a name="w132aac16d174b5"></a>

The following differences apply to AWS Glue:


| Feature |  AWS GovCloud (US-West)  |  AWS GovCloud (US-East)  | 
| --- | --- | --- | 
|  **Version Support**  |  |  | 
|  [AWS Glue Version 3.0](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-30.html)  | Yes | Yes | 
|  [AWS Glue Version 4.0](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-40.html)  | Yes | Yes | 
|  [AWS Glue Version 5.0](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-50.html)  | Yes.<br />However, the following features are not available: Connection v2 support for DB connectors, {smlong} Unified Studio, {smlong} Lakehouse, and Data Lineage | Yes.<br />However, the following features are not available: Connection v2 support for DB connectors, {smlong} Unified Studio, {smlong} Lakehouse, and Data Lineage | 
|  [AWS Glue Version 5.1](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-51.html)  | Yes | Yes | 
|  [AWS Glue Version 6.0](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-60.html)  | Yes | Yes | 
|  **Workers**  |  |  | 
|  [G1/G2 workers](https://docs.aws.amazon.com/glue/latest/dg/add-job.html)  | Yes | Yes | 
|  [G4/G8 workers](https://docs.aws.amazon.com/glue/latest/dg/add-job.html)  | No | No | 
|  ** Data Catalog Features**  |  |  | 
|  [Crawlers](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)  | Yes | Yes | 
|  [Transactional Table Optimization](https://docs.aws.amazon.com/glue/latest/dg/populate-otf.html)  | No | No | 
|  [Statistics for performance optimization](https://docs.aws.amazon.com/glue/latest/dg/column-statistics.html)  | No | No | 
|  ** AWS Glue ETL Features**  |  |  | 
|  [Connectors](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html)  | Yes.<br />However, following connectors are unavailable:<br />Facebook Ads, Google Ads, Google Analytics 4, Google Sheets, Hubspot, Instagram Ads, Intercom, Jira Cloud, Marketo, Oracle NetSuite, Salesforce Marketing Cloud, Salesforce Marketing Cloud Account Engagement, ServiceNow, Slack, Snapchat Ads, Stripe, Zendesk and Zoho CRM | Yes.<br />However, following connectors are unavailable:<br />Facebook Ads, Google Ads, Google Analytics 4, Google Sheets, Hubspot, Instagram Ads, Intercom, Jira Cloud, Marketo, Oracle NetSuite, Salesforce Marketing Cloud, Salesforce Marketing Cloud Account Engagement, ServiceNow, Slack, Snapchat Ads, Stripe, Zendesk and Zoho CRM | 
| Connector Marketplace | No | No | 
|  [Autoscaling](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html)  | Yes | Yes | 
|  [Flex Execution](https://aws.amazon.com/blogs/big-data/introducing-aws-glue-flex-jobs-cost-savings-on-etl-workloads/)  | No | No | 
|  [AWS Glue Streaming](https://docs.aws.amazon.com/glue/latest/dg/streaming-chapter.html)  | Yes | Yes | 
|  [AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/author-job-glue.html)  | Yes.<br />However, does not support SparkUI | Yes.<br />However, does not support Data Preview, AWS Glue data preparation experience, and SparkUI | 
|  [AWS Glue DataBrew](https://docs.aws.amazon.com/databrew/latest/dg/what-is.html)  | Yes | No | 
|  [AWS Glue Studio Notebooks](https://docs.aws.amazon.com/glue/latest/dg/notebooks-chapter.html)  | No | No | 
|  [AWS Glue Interactive Sessions](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-chapter.html)  | Yes | No | 
|  [Amazon Q Integration](https://docs.aws.amazon.com/glue/latest/dg/q.html)  | No | No | 
|  [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html)  | Yes. However, Anomaly detection and Dynamic Rules are not available | Yes. However, Anomaly detection and Dynamic Rules are not available | 
|  [AWS Glue Sensitive Data Detection](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html)  | Yes | Yes | 
|  [AWS Glue Workflows](https://docs.aws.amazon.com/glue/latest/dg/orchestrate-using-workflows.html)  | Yes | No | 
|  [AWS Glue zero-ETL](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html)  | Yes (Amazon DynamoDB, Salesforce, and SAP sources only) | Yes (Amazon DynamoDB, Salesforce, and SAP sources only) | 

## Documentation
<a name="govcloud-glue-docs"></a>
+  [AWS Glue documentation](https://docs.aws.amazon.com/glue) 

## Export-controlled content
<a name="govcloud-glue-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.