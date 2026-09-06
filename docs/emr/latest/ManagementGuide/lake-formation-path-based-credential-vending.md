

# S3 path-based access using Lake Formation for Amazon EMR Spark
<a name="lake-formation-path-based-credential-vending"></a>

With Amazon EMR releases 7.13.0 and higher, you can use the AWS Lake Formation Access Grants Plugin to obtain temporary credentials for S3 paths registered with Lake Formation. This enables Spark queries that directly reference S3 paths to use Lake Formation-vended credentials, in addition to the existing table-name based credential vending provided by Full Table Access (FTA). For more details, see [Accessing Amazon S3 locations](https://docs.aws.amazon.com/lake-formation/latest/dg/accessing-s3-locations.html).

The Lake Formation Access Grants Plugin integrates with the S3A filesystem in Spark. When enabled, S3A uses the plugin to call the Lake Formation [GetTemporaryDataLocationCredentials](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryDataLocationCredentials.html) API to obtain temporary credentials for S3 paths that belong to Lake Formation-registered tables.

This plugin is useful when your Spark jobs read or write data by referencing S3 paths directly (for example, `spark.read.parquet("s3a://my-bucket/my-table/")`) rather than using table names. The plugin also supports optional fallback to S3 Access Grants or IAM role credentials when Lake Formation access is denied.

## Relationship to Full Table Access (FTA)
<a name="lake-formation-path-based-relationship-fta"></a>

The existing Full Table Access feature uses the [GetTemporaryGlueTableCredentials](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryGlueTableCredentials.html) API, which vends credentials based on table names. The Lake Formation Access Grants Plugin uses the [GetTemporaryDataLocationCredentials](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryDataLocationCredentials.html) API, which vends credentials based on S3 paths.

You can use both features together. When both are enabled, FTA credentials take precedence for table-name queries, while the plugin handles direct S3 path queries.

## Prerequisites
<a name="lake-formation-path-based-prerequisites"></a>

Before you use the Lake Formation Access Grants Plugin, complete the following steps:
+ Set up Full Table Access (FTA) for your Amazon EMR environment. For instructions, see [Configuring Lake Formation full table access](https://docs.aws.amazon.com/emr/latest/ManagementGuide/lake-formation-unfiltered-ec2-access.html).
+ In the Lake Formation console, register the S3 path with the owner account:

  1. Navigate to **Data lake locations**.

  1. Select the location and enable **Register S3 path with Owner Account**.
+ Grant the runtime role the appropriate Lake Formation permissions on the table:
  + To read table data, grant the runtime role full `SELECT` permission on the table.
  + To modify table data, grant the runtime role `SUPER` permission on the table.

## Enable the Lake Formation Access Grants Plugin
<a name="lake-formation-path-based-enable"></a>

To enable the plugin, set the following S3A configuration properties in your Spark session:


**Lake Formation Access Grants Plugin configuration properties**  

| Property | Default | Description | 
| --- | --- | --- | 
| fs.s3a.lakeformation.access.grants.enabled | FALSE | Enables the Lake Formation Access Grants Plugin. | 
| fs.s3a.lakeformation.access.grants.fallback.to.iam | FALSE | Enables fallback to S3 Access Grants or IAM role credentials if Lake Formation denies access. | 

## Fallback behavior
<a name="lake-formation-path-based-fallback"></a>

When `fs.s3a.lakeformation.access.grants.fallback.to.iam` is set to `true`, the plugin uses a fallback chain if Lake Formation denies access. This is useful in scenarios where some S3 paths are registered with Lake Formation and others are managed through S3 Access Grants or IAM policies.

When fallback is enabled, the plugin attempts to obtain credentials in the following order:

1. **Lake Formation** – The plugin calls [GetTemporaryDataLocationCredentials](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryDataLocationCredentials.html). If Lake Formation grants access, the plugin returns those credentials.

1. **S3 Access Grants** – If Lake Formation denies access, the plugin checks whether S3 Access Grants can provide credentials for the requested path. If an S3 Access Grants instance covers the path and the caller has a matching grant, the plugin uses those credentials.

1. **IAM role** – If both Lake Formation and S3 Access Grants deny access, the plugin falls back to the IAM role credentials attached to the job.

## Considerations and limitations
<a name="lake-formation-path-based-considerations"></a>
+ The plugin supports Apache Hive, Apache Hudi, and Delta Lake table formats. Apache Iceberg is not currently supported.
+ The plugin is not currently supported with Amazon EMR Spark Fine-Grained Access Control (FGAC) mode.
+ Path-based credential vending requires a 1:1 mapping between a table and its S3 location in the AWS Glue Data Catalog.