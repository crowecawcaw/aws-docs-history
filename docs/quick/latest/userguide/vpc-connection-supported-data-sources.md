# Supported VPC data sources

With a VPC connection, you can connect Amazon Quick to a data source inside your VPC over
a private network path. Traffic stays off the public internet. Not every data source can use
a VPC connection. VPC connections support the following two categories:

Amazon Quick Sight data sources

Structured data sources, such as databases and data warehouses, that you
connect to when you create datasets and analyses. Most of these support VPC
connections. For more information about supported Amazon Quick Sight data sources, see [Amazon Quick Sight data sources that support VPC connections](#vpc-supported-sight-data-sources "#vpc-supported-sight-data-sources").

Knowledge base data sources

Data sources that you connect to when you create a knowledge base, including
document repositories and content management systems. Amazon Redshift supports VPC
connections in this category. For more information about knowledge base data
sources, see [Knowledge base data sources that support VPC connections](#vpc-supported-knowledge-base-data-sources "#vpc-supported-knowledge-base-data-sources").

Both categories share the same configuration requirements. For more information about
those requirements, see [Requirements for a VPC data source](#vpc-data-source-requirements "#vpc-data-source-requirements").

## Amazon Quick Sight data sources that support VPC connections

The following Amazon Quick Sight data sources support VPC connections. When you create a dataset
from one of these sources, you can route the connection through a VPC connection:

- Amazon OpenSearch Service
- Amazon Redshift
- Amazon Relational Database Service
- Amazon Aurora
- Apache Impala
- Databricks
- Exasol
- MariaDB
- Microsoft SQL Server
- MySQL
- Oracle
- PostgreSQL
- Presto
- Snowflake
- Starburst Enterprise
- Teradata
- Trino

Other Amazon Quick Sight data sources can't use a VPC connection. This group includes Amazon Athena,
Google BigQuery, Apache Spark, and Amazon Timestream. It also
includes the connectors for software as a service (SaaS) applications, such as
Salesforce, ServiceNow, Jira, and
GitHub. If you attach a VPC connection to a data source that doesn't
support one, the request fails with an invalid parameter error.

## Knowledge base data sources that support VPC connections

Amazon Redshift supports VPC connections when you use it as a knowledge base data source.
When you create a knowledge base from an Amazon Redshift data source, you can choose a VPC
connection. Your queries then reach the cluster over a private network path.

The following knowledge base data sources can't use a Quick VPC
connection:

- Amazon Bedrock managed knowledge bases
- Amazon Q Business indexes
- Amazon S3
- Box
- Confluence
- Google Drive
- Microsoft OneDrive
- Microsoft SharePoint

If you attach a VPC connection to one of these data sources, the request fails with an
invalid parameter error.

###### Note

You can still restrict Amazon S3 bucket access to a VPC endpoint. That is a separate
mechanism, and you control it through your bucket policy. For more information about
restricting Amazon S3 bucket access to a VPC endpoint, see [Configure VPC access for the
Amazon S3 connector](s3-admin-setup.md "s3-admin-setup.md").

## Requirements for a VPC data source

Before you can reach a data source in your VPC from Amazon Quick, your configuration
must meet the following requirements:

1. The Domain Name System (DNS) name of the VPC data source must resolve from
   outside your VPC.
2. The connection must return the private IP address of your instance. Databases
   hosted by Amazon Redshift, Amazon RDS, and Aurora automatically meet this
   requirement.
3. A clearly defined network path must connect the data source and
   Amazon Quick.
4. A VPC connection for the VPC must exist in Amazon Quick. You create or select
   one in the Amazon Quick console.
