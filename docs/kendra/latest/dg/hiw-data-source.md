# Data sources

A data source is a data repository or location that Amazon Kendra connects to and
indexes your documents or content. For example, you can configure Amazon Kendra to
connect to Microsoft SharePoint to crawl and index your documents stored in this source.
You can also index web pages by providing the URLs for Amazon Kendra to crawl. You
can automatically synchronize a data source with an Amazon Kendra index so that
added, updated, or deleted documents in the data source are also added, updated, or
deleted in the index.

Supported data sources are:

- [Adobe
  Experience Manager](data-source-aem.md "data-source-aem.md")
- [Alfresco](data-source-alfresco.md "data-source-alfresco.md")
- [Aurora
  (MySQL)](data-source-aurora-mysql.md "data-source-aurora-mysql.md")
- [Aurora
  (PostgreSQL)](data-source-aurora-postgresql.md "data-source-aurora-postgresql.md")
- [Amazon FSx (Windows)](data-source-fsx.md "data-source-fsx.md")
- [Amazon FSx (NetApp ONTAP)](data-source-fsx-ontap.md "data-source-fsx-ontap.md")
- [Database data sources](data-source-database.md "data-source-database.md")
- [Amazon RDS
  (Microsoft SQL Server)](data-source-rds-ms-sql-server.md "data-source-rds-ms-sql-server.md")
- [Amazon RDS (MySQL)](data-source-rds-mysql.md "data-source-rds-mysql.md")
- [Amazon RDS (Oracle)](data-source-rds-oracle.md "data-source-rds-oracle.md")
- [Amazon RDS
  (PostgreSQL)](data-source-rds-postgresql.md "data-source-rds-postgresql.md")
- [Amazon S3 buckets](data-source-s3.md "data-source-s3.md")
- [Amazon Kendra Web
  Crawler](data-source-web-crawler.md "data-source-web-crawler.md")
- [Box](data-source-box.md "data-source-box.md")
- [Confluence](data-source-confluence.md "data-source-confluence.md")
- [Custom data sources](data-source-custom.md "data-source-custom.md")
- [Dropbox](data-source-dropbox.md "data-source-dropbox.md")
- [Drupal](data-source-drupal.md "data-source-drupal.md")
- [GitHub](data-source-github.md "data-source-github.md")
- [Gmail](data-source-gmail.md "data-source-gmail.md")
- [Google Workspace
  Drives](data-source-google-drive.md "data-source-google-drive.md")
- [IBM DB2](data-source-ibm-db2.md "data-source-ibm-db2.md")
- [Jira](data-source-jira.md "data-source-jira.md")
- [Microsoft Exchange](data-source-exchange.md "data-source-exchange.md")
- [Microsoft OneDrive](data-source-onedrive.md "data-source-onedrive.md")
- [Microsoft SharePoint](data-source-sharepoint.md "data-source-sharepoint.md")
- [Microsoft Teams](data-source-teams.md "data-source-teams.md")
- [Microsoft SQL
  Server](data-source-ms-sql-server.md "data-source-ms-sql-server.md")
- [Microsoft Yammer](data-source-yammer.md "data-source-yammer.md")
- [MySQL](data-source-mysql.md "data-source-mysql.md")
- [Oracle
  Database](data-source-oracle-database.md "data-source-oracle-database.md")
- [PostgreSQL](data-source-postgresql.md "data-source-postgresql.md")
- [Quip](data-source-quip.md "data-source-quip.md")
- [Salesforce](data-source-salesforce.md "data-source-salesforce.md")
- [ServiceNow](data-source-servicenow.md "data-source-servicenow.md")
- [Slack](data-source-slack.md "data-source-slack.md")
- [Zendesk](data-source-zendesk.md "data-source-zendesk.md")
  For a list of document types or formats supported by Amazon Kendra see [Document
  types](index-document-types.md "index-document-types.md"). You must first create an index before creating a data source
  connector to index your documents from your data source.

###### Note

To create an index of documents, you don't need to use a data source. You can add
documents directly to an index with batch upload. For more information, see [Adding
documents directly to an index](in-adding-documents.md "in-adding-documents.md").

For a walkthrough on using the Amazon Kendra console, the AWS
CLI, or SDKs, see [Getting started](getting-started.md "getting-started.md").
