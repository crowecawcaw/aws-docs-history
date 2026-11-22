

# Databricks integration

Databricks users query the FHIR data in your HealthLake data stores in place from Unity Catalog, with no data copies or ETL pipelines. Access is read-only, and Lake Formation and Unity Catalog control who can read what. The integration uses the [HealthLake OpenSharing server](https://github.com/databricks-industry-solutions/healthlake-opensharing) on the GitHub website, a Databricks solution that runs as a Databricks App in your workspace.

With this integration, you can:
+ Use HealthLake as your transactional FHIR server, and Databricks as your analytics platform.
+ Serve many data stores, across one or more AWS accounts, from one app.
+ Govern access in two layers: Lake Formation for the data Databricks can read, and Unity Catalog for the users who can query it.

**Important**  
After HealthLake data is read into Databricks, you are responsible for governing that data in Databricks, including any protected health information (PHI). For more information, see the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

**Note**  
Databricks, Unity Catalog, Databricks Apps, and the HealthLake OpenSharing solution from Databricks are third-party products that AWS doesn't provide or support. For more information about these components, see the [HealthLake OpenSharing repository](https://github.com/databricks-industry-solutions/healthlake-opensharing) on the GitHub website.

## How it works
<a name="integrating-databricks-how-it-works"></a>

HealthLake keeps an Apache Iceberg table for each FHIR resource type and keeps it current. For more information about how analytics access works, see [How analytics access works](integrating-analytics.md#integrating-analytics-how-it-works). The OpenSharing server reads these tables through Lake Formation credential vending. It gets temporary, read-only credentials for each table, and Databricks compute reads the data files directly from Amazon S3.

![Architecture of the HealthLake integration with Databricks. Databricks users query Unity Catalog. Unity Catalog calls the OpenSharing server, which runs as a Databricks App. The server assumes an IAM role in your AWS account and gets table metadata from the AWS Glue Data Catalog and temporary credentials from AWS Lake Formation. Databricks compute then reads the HealthLake data files directly from Amazon S3.](https://docs.aws.amazon.com/healthlake/latest/devguide/images/healthlake-databricks-architecture.png)


The following steps describe the request flow when a Databricks user runs a query:

1. Unity Catalog checks the user's grants and requests the table from the server as the recipient service principal.

1. The server assumes the IAM role through AWS STS `AssumeRoleWithWebIdentity`.

1. The server calls `GetTable` in the AWS Glue Data Catalog to resolve the current Iceberg snapshot.

1. The server calls `GetTemporaryGlueTableCredentials` in Lake Formation, which checks the role's grants and returns credentials scoped to the table.

1. The server returns presigned URLs, and Databricks compute reads the data files from Amazon S3.

### Access control
<a name="integrating-databricks-access-control"></a>

Every query is authorized twice: Lake Formation sets the maximum data that the server's role can read, and Unity Catalog decides which Databricks users can query it. A user sees data only if both layers allow it.

![Two layers of access control. Lake Formation permissions on the IAM role define the maximum set of HealthLake tables available to Databricks. Unity Catalog grants define which Databricks users and groups can query those tables.](https://docs.aws.amazon.com/healthlake/latest/devguide/images/healthlake-databricks-access-control.png)


There's no automatic mapping between IAM principals and Unity Catalog users or groups, and Unity Catalog keeps the query audit records.

### Security model
<a name="integrating-databricks-security"></a>

The integration secures traffic in two directions:

Inbound (Unity Catalog to the app)  
The Unity Catalog provider authenticates to the app with OAuth client credentials. The Databricks Apps gateway validates the token and checks the `CAN_USE` permission, and the server accepts only the one recipient service principal that you configure. Both checks matter, because the server's responses contain presigned URLs that anyone who holds them can read.

Outbound (the app to AWS)  
IAM trusts the workspace's OIDC identity provider. The role's trust policy allows only this app. No AWS secrets are stored, and the role has no Amazon S3 permissions.

## Limitations and considerations
<a name="integrating-databricks-considerations"></a>

The integration has the following limitations:
+ **Full table scans.** The server doesn't apply predicate pushdown, so every query reads every file of the table. This affects query time and compute cost. To reduce repeated scans, build curated tables, as described in [Building curated tables for repeated queries](#integrating-databricks-querying-pattern).
+ **Unsupported features.** The integration doesn't support time travel, change data feed, or streaming reads.
+ **AWS Regions.** Keep your Databricks workspace and HealthLake data store in the same AWS Region. Cross-Region access can increase latency and data transfer costs.
+ **Environments.** Use a separate IAM role and app configuration for each environment, and match your Databricks and HealthLake environments one to one.
+ **Long-running queries.** The server refreshes the short-lived, table-scoped credentials automatically, so long-running queries complete.

## Querying the tables
<a name="integrating-databricks-querying"></a>

For the table structure, resource versions, and data freshness, see [Understanding the analytics tables](integrating-analytics.md#integrating-analytics-tables). For the Unity Catalog catalog and schema names to use, see [Querying the data](https://github.com/databricks-industry-solutions/healthlake-opensharing#querying-the-data) on the GitHub website.

### Building curated tables for repeated queries
<a name="integrating-databricks-querying-pattern"></a>

Every query against the shared tables performs a full table scan, as described in [Limitations and considerations](#integrating-databricks-considerations). Use the shared tables as a landing zone, and build curated tables (for example, bronze, silver, and gold layers) with scheduled jobs. Analysts and dashboards then query the curated tables instead of the shared tables.

![HealthLake shared tables feed scheduled Databricks jobs that build bronze, silver, and gold curated tables. Analysts and dashboards query the curated tables instead of the shared tables.](https://docs.aws.amazon.com/healthlake/latest/devguide/images/healthlake-databricks-curated-tables.png)


**Topics**
+ [How it works](#integrating-databricks-how-it-works)
+ [Limitations and considerations](#integrating-databricks-considerations)
+ [Querying the tables](#integrating-databricks-querying)
+ [Setting up](integrating-databricks-setting-up.md)
+ [Troubleshooting](integrating-databricks-troubleshooting.md)