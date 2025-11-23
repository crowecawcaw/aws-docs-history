# Using Lake Formation with Athena Spark workgroups

With the release version Apache Spark version 3.5, you can leverage AWS Lake Formation with AWS Glue Data Catalog where the session execution role has full table permissions. This capability allows you to read and write to tables that are protected by Lake Formation from your Athena Spark interactive sessions. See the following sections to learn more about Lake Formation and how to use it with Athena Spark.

## Step 1: Enable Full Table Access in Lake Formation

To use Full Table Access (FTA) mode, you must allow Athena Spark to access data without the IAM session tag validation in AWS Lake Formation. To enable, follow the steps in [Application integration for full table access](../../../lake-formation/latest/dg/fta-app-integration.md "../../../lake-formation/latest/dg/fta-app-integration.md").

### Step 1.1: Register data locations in Lake Formation using user defined role

You must use a user-defined role to register data locations in AWS Lake Formation. See [Requirements for roles used to register locations](../../../lake-formation/latest/dg/registration-role.md "../../../lake-formation/latest/dg/registration-role.md") for details.

## Step 2: Setup IAM permissions for the execution role for the session

For read or write access to underlying data, in addition to Lake Formation permissions, the execution role needs the `lakeformation:GetDataAccess` IAM permission. With this permission, Lake Formation grants the request for temporary credentials to access the data.

The following is an example policy of how to provide IAM permissions to access a script in Amazon S3, uploading logs to S3, AWS Glue API permissions, and permission to access Lake Formation.

### Step 2.1: Configure Lake Formation permissions

- Spark jobs that read data from S3 require Lake Formation `SELECT` permission.
- Spark jobs that write/delete data in S3 require Lake Formation `ALL (SUPER)` permission.
- Spark jobs that interact with AWS Glue Data catalog require `DESCRIBE`, `ALTER`, `DROP` permission as appropriate.

## Step 3: Initialize a Spark session for Full Table Access using Lake Formation

### Prerequisites

AWS Glue Data Catalog must be configured as a metastore to access Lake Formation tables.

Set the following settings to configure AWS Glue catalog as a metastore:

```
{
  "spark.hadoop.glue.catalogid": "ACCOUNT_ID",
  "spark.hadoop.hive.metastore.client.factory.class": "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory",
  "spark.hadoop.hive.metastore.glue.catalogid": "ACCOUNT_ID",
  "spark.sql.catalogImplementation": "hive"
}
```

To access tables registered with AWS Lake Formation, the following configurations need to be set during Spark initialization to configure Spark to use AWS Lake Formation credentials.

### Hive

```
{
  "spark.hadoop.fs.s3.credentialsResolverClass": "com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver",
  "spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject": "true",
  "spark.hadoop.fs.s3.folderObject.autoAction.disabled": "true",
  "spark.sql.catalog.skipLocationValidationOnCreateTable.enabled": "true",
  "spark.sql.catalog.createDirectoryAfterTable.enabled": "true",
  "spark.sql.catalog.dropDirectoryBeforeTable.enabled": "true"
}
```

### Apache Iceberg

```
{
  "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
  "spark.sql.catalog.spark_catalog": "org.apache.iceberg.spark.SparkSessionCatalog",
  "spark.sql.catalog.spark_catalog.warehouse": "s3://your-bucket/warehouse/",
  "spark.sql.catalog.spark_catalog.client.region": "REGION",
  "spark.sql.catalog.spark_catalog.catalog-impl": "org.apache.iceberg.aws.glue.GlueCatalog",
  "spark.sql.catalog.spark_catalog.glue.account-id": "ACCOUNT_ID",
  "spark.sql.catalog.spark_catalog.glue.lakeformation-enabled": "true"
}
```

### Amazon S3 Tables

```
{
  "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
  "spark.sql.catalog.{catalogName}": "org.apache.iceberg.spark.SparkCatalog",
  "spark.sql.catalog.{catalogName}.warehouse": "arn:aws:s3tables:{region}:{accountId}:bucket/{bucketName}",
  "spark.sql.catalog.{catalogName}.catalog-impl": "org.apache.iceberg.aws.glue.GlueCatalog",
  "spark.sql.catalog.{catalogName}.glue.id": "{accountId}:s3tablescatalog/{bucketName}",
  "spark.sql.catalog.{catalogName}.glue.lakeformation-enabled": "true",
  "spark.sql.catalog.{catalogName}.client.region": "REGION",
  "spark.sql.catalog.{catalogName}.glue.account-id": "ACCOUNT_ID"
}
```

### Delta Lake

```
{
  "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
  "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
  "spark.hadoop.fs.s3.credentialsResolverClass": "com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver",
  "spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject": "true",
  "spark.hadoop.fs.s3.folderObject.autoAction.disabled": "true",
  "spark.sql.catalog.skipLocationValidationOnCreateTable.enabled": "true",
  "spark.sql.catalog.createDirectoryAfterTable.enabled": "true",
  "spark.sql.catalog.dropDirectoryBeforeTable.enabled": "true"
}
```

## Considerations and Limitations

- Full Table Access is supported for Hive, Iceberg, Amazon S3 Tables and Delta tables. Hudi tables do not support full table access.
- To add new catalogs to an active session use `spark.conf.set` with new catalog configs.
- Catalog configs are immutable. If you want to update a catalog config create new catalog using `spark.conf.set`.
- Add only catalogs you need to the spark session.
- To change default catalog: `spark.catalog.setCurrentCatalog("s3tablesbucket")`
- If you have special characters in your catalog name like `-` then escape it in your query like:

```
SELECT sales_amount as nums FROM `my-s3-tables-bucket`.`s3namespace`.`daily_sales` LIMIT 100
```
