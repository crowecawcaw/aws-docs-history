

# Integrating with Amazon S3 Tables
<a name="glue-federation-s3tables"></a>

AWS Glue Data Catalog integration with Amazon S3 Tables allows you to discover, query, and join S3 Tables with data in Amazon S3 data lakes using a single catalog. When you integrate S3 Tables with the Data Catalog, the service creates a federated catalog structure that maps S3 Tables resources to AWS Glue catalog objects:
+ An S3 table bucket becomes a catalog in the Data Catalog
+ An S3 namespace becomes a AWS Glue database
+ An S3 table becomes a AWS Glue table

## Access controls
<a name="s3-tables-access-controls"></a>

The Data Catalog supports two access control modes for S3 Tables integration:
+ **IAM access control** – Uses IAM policies to control access to S3 Tables and the Data Catalog. In this approach, you need IAM permissions on both S3 Tables resources and Data Catalog objects to access resources.
+ **AWS Lake Formation access control** – Uses AWS Lake Formation grants in addition to AWS Glue IAM permissions to control access to S3 Tables through the Data Catalog. In this mode, principals require IAM permissions to interact with the Data Catalog, and AWS Lake Formation grants determine which catalog resources (databases, tables, columns, rows) the principal can access. This mode supports both coarse-grained access control (database-level and table-level grants) and fine-grained access control (column-level and row-level security). When a registered role is configured and credential vending is enabled, S3 Tables IAM permissions are not required for the principal, as AWS Lake Formation vends credentials on behalf of the principal using the registered role. AWS Lake Formation access control also supports credential vending for third-party analytics engines. For more information, see [Creating an S3 Tables catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/create-s3-tables-catalog.html) in the *AWS Lake Formation Developer Guide*.

You can migrate between access control modes as your requirements evolve.

## Catalog hierarchy for auto-mounting
<a name="s3-tables-catalog-hierarchy"></a>

When you integrate S3 Tables with the Data Catalog using the Amazon S3 management console, the console creates a federated catalog called `s3tablescatalog` in the Data Catalog in your account in that AWS Region. This federated catalog serves as the parent catalog for all existing and future S3 table buckets in that account and Region. The integration maps Amazon S3 table bucket resources in the following hierarchy:
+ **Federated catalog** – `s3tablescatalog` (automatically created)
+ **Child catalogs** – Each S3 table bucket becomes a child catalog under `s3tablescatalog`
+ **Databases** – Each S3 namespace within a table bucket becomes a database
+ **Tables** – Each S3 table within a namespace becomes a table

For example, if you have an S3 table bucket named "analytics-bucket" with a namespace "sales" containing a table "transactions", the full path in the Data Catalog would be: `s3tablescatalog/analytics-bucket/sales/transactions`

This four-part hierarchy applies to same-account scenarios where S3 Tables and the Data Catalog are in the same AWS account. For cross-account scenarios, you manually mount individual S3 table buckets in the Data Catalog, which creates a three-part hierarchy.

## Supported Regions
<a name="s3-tables-supported-regions"></a>

S3 Tables integration with the Data Catalog is available in the following AWS Regions:


| Region code | Region name | 
| --- | --- | 
| us-east-1 | US East (N. Virginia) | 
| us-east-2 | US East (Ohio) | 
| us-west-1 | US West (N. California) | 
| us-west-2 | US West (Oregon) | 
| af-south-1 | Africa (Cape Town) | 
| ap-east-1 | Asia Pacific (Hong Kong) | 
| ap-east-2 | Asia Pacific (Taipei) | 
| ap-northeast-1 | Asia Pacific (Tokyo) | 
| ap-northeast-2 | Asia Pacific (Seoul) | 
| ap-northeast-3 | Asia Pacific (Osaka) | 
| ap-south-1 | Asia Pacific (Mumbai) | 
| ap-south-2 | Asia Pacific (Hyderabad) | 
| ap-southeast-1 | Asia Pacific (Singapore) | 
| ap-southeast-2 | Asia Pacific (Sydney) | 
| ap-southeast-3 | Asia Pacific (Jakarta) | 
| ap-southeast-4 | Asia Pacific (Melbourne) | 
| ap-southeast-5 | Asia Pacific (Malaysia) | 
| ap-southeast-6 | Asia Pacific (New Zealand) | 
| ap-southeast-7 | Asia Pacific (Thailand) | 
| ca-central-1 | Canada (Central) | 
| ca-west-1 | Canada West (Calgary) | 
| eu-central-1 | Europe (Frankfurt) | 
| eu-central-2 | Europe (Zurich) | 
| eu-north-1 | Europe (Stockholm) | 
| eu-south-1 | Europe (Milan) | 
| eu-south-2 | Europe (Spain) | 
| eu-west-1 | Europe (Ireland) | 
| eu-west-2 | Europe (London) | 
| eu-west-3 | Europe (Paris) | 
| il-central-1 | Israel (Tel Aviv) | 
| mx-central-1 | Mexico (Central) | 
| sa-east-1 | South America (Sao Paulo) | 
| us-gov-east-1 | AWS GovCloud (US-East) | 
| us-gov-west-1 | AWS GovCloud (US-West) | 
| cn-north-1 | China (Beijing) | 
| cn-northwest-1 | China (Ningxia) | 

**Topics**
+ [Access controls](#s3-tables-access-controls)
+ [Catalog hierarchy for auto-mounting](#s3-tables-catalog-hierarchy)
+ [Supported Regions](#s3-tables-supported-regions)
+ [Prerequisites](s3tables-catalog-prerequisites.md)
+ [Enabling S3 Tables integration with the Data Catalog](enable-s3-tables-catalog-integration.md)
+ [Adding databases and tables to the S3 Tables catalog](create-databases-tables-s3-catalog.md)
+ [Sharing S3 Tables catalog objects](share-s3-tables-catalog.md)
+ [Managing S3 Tables integration](manage-s3-tables-catalog-integration.md)