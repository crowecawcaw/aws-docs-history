

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Data sources
<a name="hiw-data-source"></a>

A data source is a data repository or location that Amazon Kendra connects to and indexes your documents or content. For example, you can configure Amazon Kendra to connect to Microsoft SharePoint to crawl and index your documents stored in this source. You can also index web pages by providing the URLs for Amazon Kendra to crawl. You can automatically synchronize a data source with an Amazon Kendra index so that added, updated, or deleted documents in the data source are also added, updated, or deleted in the index.

Supported data sources are:
+ [Adobe Experience Manager](https://docs.aws.amazon.com/kendra/latest/dg/data-source-aem.html)
+ [Alfresco](https://docs.aws.amazon.com/kendra/latest/dg/data-source-alfresco.html)
+ [Aurora (MySQL)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-aurora-mysql.html)
+ [Aurora (PostgreSQL)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-aurora-postgresql.html)
+ [Amazon FSx (Windows)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-fsx.html)
+ [Amazon FSx (NetApp ONTAP)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-fsx-ontap.html) 
+  [Database data sources](https://docs.aws.amazon.com/kendra/latest/dg/data-source-database.html)
+ [Amazon RDS (Microsoft SQL Server)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-rds-ms-sql-server.html)
+ [Amazon RDS (MySQL)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-rds-mysql.html)
+ [Amazon RDS (Oracle)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-rds-oracle.html)
+ [Amazon RDS (PostgreSQL)](https://docs.aws.amazon.com/kendra/latest/dg/data-source-rds-postgresql.html)
+ [Amazon S3 buckets](https://docs.aws.amazon.com/kendra/latest/dg/data-source-s3.html)
+ [Amazon Kendra Web Crawler](https://docs.aws.amazon.com/kendra/latest/dg/data-source-web-crawler.html)
+ [Box](https://docs.aws.amazon.com/kendra/latest/dg/data-source-box.html)
+ [Confluence](https://docs.aws.amazon.com/kendra/latest/dg/data-source-confluence.html)
+ [Custom data sources](https://docs.aws.amazon.com/kendra/latest/dg/data-source-custom.html)
+ [Dropbox](https://docs.aws.amazon.com/kendra/latest/dg/data-source-dropbox.html)
+ [Drupal](https://docs.aws.amazon.com/kendra/latest/dg/data-source-drupal.html)
+ [GitHub](https://docs.aws.amazon.com/kendra/latest/dg/data-source-github.html)
+ [Gmail](https://docs.aws.amazon.com/kendra/latest/dg/data-source-gmail.html)
+ [Google Workspace Drives](https://docs.aws.amazon.com/kendra/latest/dg/data-source-google-drive.html)
+ [IBM DB2](https://docs.aws.amazon.com/kendra/latest/dg/data-source-ibm-db2.html)
+ [Jira](https://docs.aws.amazon.com/kendra/latest/dg/data-source-jira.html)
+ [Microsoft Exchange](https://docs.aws.amazon.com/kendra/latest/dg/data-source-exchange.html)
+ [Microsoft OneDrive](https://docs.aws.amazon.com/kendra/latest/dg/data-source-onedrive.html)
+ [Microsoft SharePoint](https://docs.aws.amazon.com/kendra/latest/dg/data-source-sharepoint.html)
+ [Microsoft Teams](https://docs.aws.amazon.com/kendra/latest/dg/data-source-teams.html)
+ [Microsoft SQL Server](https://docs.aws.amazon.com/kendra/latest/dg/data-source-ms-sql-server.html)
+ [Microsoft Yammer](https://docs.aws.amazon.com/kendra/latest/dg/data-source-yammer.html)
+ [MySQL](https://docs.aws.amazon.com/kendra/latest/dg/data-source-mysql.html)
+ [Oracle Database](https://docs.aws.amazon.com/kendra/latest/dg/data-source-oracle-database.html)
+ [PostgreSQL](https://docs.aws.amazon.com/kendra/latest/dg/data-source-postgresql.html)
+ [Quip](https://docs.aws.amazon.com/kendra/latest/dg/data-source-quip.html)
+ [Salesforce](https://docs.aws.amazon.com/kendra/latest/dg/data-source-salesforce.html)
+ [ServiceNow](https://docs.aws.amazon.com/kendra/latest/dg/data-source-servicenow.html)
+ [Slack](https://docs.aws.amazon.com/kendra/latest/dg/data-source-slack.html)
+ [Zendesk](https://docs.aws.amazon.com/kendra/latest/dg/data-source-zendesk.html)

For a list of document types or formats supported by Amazon Kendra see [Document types](https://docs.aws.amazon.com/kendra/latest/dg/index-document-types.html). You must first create an index before creating a data source connector to index your documents from your data source.

**Note**  
To create an index of documents, you don't need to use a data source. You can add documents directly to an index with batch upload. For more information, see [Adding documents directly to an index](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-documents.html).

 For a walkthrough on using the Amazon Kendra console, the AWS CLI, or SDKs, see [Getting started](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html).