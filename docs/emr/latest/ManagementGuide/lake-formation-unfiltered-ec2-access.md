# Lake Formation full table access for Amazon EMR on EC2

With Amazon EMR releases 7.8.0 and higher, you can leverage AWS Lake Formation with Glue Data
Catalog where the job runtime role has full table permissions without the limitations of
fine-grained access control. This capability allows you to read and write to tables that are
protected by Lake Formation from your Amazon EMR on EC2 Spark batch and interactive jobs.
See the following sections to learn more about Lake Formation and how to use it with
Amazon EMR on EC2.

## Using Lake Formation with full table access

You can access AWS Lake Formation protected Glue Data catalog tables from Amazon EMR on EC2 Spark jobs or interactive sessions where
the job's runtime role has full table access. You do not need to enable AWS Lake Formation on the Amazon EMR on EC2
application. When a Spark job is configured for Full Table Access (FTA), AWS Lake Formation credentials are used to read/write S3 data for AWS Lake Formation registered
tables, while the job's runtime role credentials will be used to read/write tables not
registered with AWS Lake Formation.

###### Important

Do not enable AWS Lake Formation for fine-grained access control. A job cannot simultaneously run Full Table Access (FTA)
and Fine-Grained Access Control (FGAC) on the same EMR cluster or application.

### Step 1: Enable Full Table Access in Lake Formation

To use Full Table Access (FTA) mode, you must allow third-party query engines to access data without the IAM session tag
validation in AWS Lake Formation. To enable, follow the steps in [Application integration
for full table access](../../../lake-formation/latest/dg/full-table-credential-vending.md "../../../lake-formation/latest/dg/full-table-credential-vending.md").

###### Note

When accessing cross-account tables, full-table access must be enabled in both producer and consumer accounts. In the same manner, when accessing
cross-region tables, this setting must be enabled in both producer and consumer regions.

### Step 2: Setup IAM permissions for job runtime role

For read or write access to underlying data, in addition to Lake Formation permissions, a job runtime role needs
the `lakeformation:GetDataAccess` IAM permission. With this
permission, Lake Formation grants the request for temporary credentials to access the data.

The following is an example policy of how to provide IAM permissions to access a script in Amazon S3, uploading logs to S3, AWS Glue API permissions, and
permission to access Lake Formation.

#### Step 2.1 Configure Lake Formation permissions

- Spark jobs that read data from S3 require Lake Formation SELECT permission.
- Spark jobs that write/delete data in S3 require Lake Formation ALL (SUPER) permission.
- Spark jobs that interact with Glue Data catalog require DESCRIBE, ALTER, DROP permission as
  appropriate.

For more information, refer to [Granting permissions on Data Catalog resources](../../../lake-formation/latest/dg/granting-catalog-permissions.md "../../../lake-formation/latest/dg/granting-catalog-permissions.md").

### Step 3: Initialize a Spark session for Full Table Access using Lake Formation

#### Prerequisites

AWS Glue Data Catalog must be configured as a metastore to access Lake Formation tables.

Set the following settings to configure Glue catalog as a metastore:

```
--conf spark.sql.catalogImplementation=hive
--conf spark.hive.metastore.client.factory.class=com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory
```

For more information on enabling Data Catalog for Amazon EMR on EC2, refer to [Metastore configuration for Amazon EMR on EC2](metastore-config.md "metastore-config.md").

To access tables registered with AWS Lake Formation, the following configurations need to be set during Spark
initialization to configure Spark to use AWS Lake Formation credentials.

Hive

```
‐‐conf spark.hadoop.fs.s3.credentialsResolverClass=com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver
--conf spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject=true
--conf spark.hadoop.fs.s3.folderObject.autoAction.disabled=true
--conf spark.sql.catalog.skipLocationValidationOnCreateTable.enabled=true
--conf spark.sql.catalog.createDirectoryAfterTable.enabled=true
--conf spark.sql.catalog.dropDirectoryBeforeTable.enabled=true
```

Iceberg

```
--conf spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkSessionCatalog
--conf spark.sql.catalog.spark_catalog.warehouse=`S3_DATA_LOCATION`
--conf spark.sql.catalog.spark_catalog.client.region=`REGION`
--conf spark.sql.catalog.spark_catalog.type=glue
--conf spark.sql.catalog.spark_catalog.glue.account-id=`ACCOUNT_ID`
--conf spark.sql.catalog.spark_catalog.glue.lakeformation-enabled=true
--conf spark.sql.catalog.dropDirectoryBeforeTable.enabled=true
```

Delta Lake

```
‐‐conf spark.hadoop.fs.s3.credentialsResolverClass=com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver
--conf spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject=true
--conf spark.hadoop.fs.s3.folderObject.autoAction.disabled=true
--conf spark.sql.catalog.skipLocationValidationOnCreateTable.enabled=true
--conf spark.sql.catalog.createDirectoryAfterTable.enabled=true
--conf spark.sql.catalog.dropDirectoryBeforeTable.enabled=true
```

Hudi

```
‐‐conf spark.hadoop.fs.s3.credentialsResolverClass=com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver
--conf spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject=true
--conf spark.hadoop.fs.s3.folderObject.autoAction.disabled=true
--conf spark.sql.catalog.skipLocationValidationOnCreateTable.enabled=true
--conf spark.sql.catalog.createDirectoryAfterTable.enabled=true
--conf spark.sql.catalog.dropDirectoryBeforeTable.enabled=true
--conf spark.jars=/usr/lib/hudi/hudi-spark-bundle.jar
--conf spark.sql.extensions=org.apache.spark.sql.hudi.HoodieSparkSessionExtension
--conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.hudi.catalog.HoodieCatalog
--conf spark.serializer=org.apache.spark.serializer.KryoSerializer
```

- `spark.hadoop.fs.s3.credentialsResolverClass=com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver`:

Configure EMR Filesystem (EMRFS) or EMR S3A to use AWS Lake Formation S3 credentials for Lake Formation registered tables. If the table is not
registered, use the job's runtime role credentials.

- `spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject=true` and `spark.hadoop.fs.s3.folderObject.autoAction.disabled=true`: Configure EMRFS to
  use content type header application/x-directory instead of $folder$ suffix when creating S3 folders. This is required when reading Lake Formation tables, as Lake Formation credentials
  do not allow reading table folders with $folder$ suffix.
- `spark.sql.catalog.skipLocationValidationOnCreateTable.enabled=true`: Configure Spark to skip validating the table location's emptiness before
  creation. This is necessary for Lake Formation registered tables, as Lake Formation credentials to verify the empty location are available only after Glue Data Catalog table creation. Without
  this configuration, the job's runtime role credentials will validate the
  empty table location.
- `spark.sql.catalog.createDirectoryAfterTable.enabled=true`: Configure Spark to create the Amazon S3 folder after table creation in the Hive
  metastore. This is required for Lake Formation registered tables, as Lake Formation credentials to create the S3 folder are available only after
  Glue Data Catalog table creation.
- `spark.sql.catalog.dropDirectoryBeforeTable.enabled=true`: Configure Spark to drop the S3 folder before table deletion in the Hive
  metastore. This is necessary for Lake Formation registered tables, as Lake Formation credentials to drop the S3 folder are not available after table deletion from
  the Glue Data Catalog.
- `spark.sql.catalog.<catalog>.glue.lakeformation-enabled=true`: Configure Iceberg catalog to use AWS Lake Formation S3 credentials for Lake Formation registered tables. If
  the table is not registered, use default environment credentials.

#### Configure full table access mode in SageMaker Unified Studio

To access Lake Formation registered tables from interactive Spark sessions in JupyterLab notebooks, use compatibility permission
mode. Use the %%configure magic command to set up your Spark configuration. Choose the configuration based on your table type:

For Hive tables

```
%%configure -f
{
    "conf": {
        "spark.hadoop.fs.s3.credentialsResolverClass": "com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver",
        "spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject": true,
        "spark.hadoop.fs.s3.folderObject.autoAction.disabled": true,
        "spark.sql.catalog.skipLocationValidationOnCreateTable.enabled": true,
        "spark.sql.catalog.createDirectoryAfterTable.enabled": true,
        "spark.sql.catalog.dropDirectoryBeforeTable.enabled": true
    }
}
```

For Iceberg tables

```
%%configure -f
{
    "conf": {
        "spark.sql.catalog.spark_catalog": "org.apache.iceberg.spark.SparkSessionCatalog",
        "spark.sql.catalog.spark_catalog.warehouse": "`S3_DATA_LOCATION`",
        "spark.sql.catalog.spark_catalog.client.region": "`REGION`",
        "spark.sql.catalog.spark_catalog.type": "glue",
        "spark.sql.catalog.spark_catalog.glue.account-id": "`ACCOUNT_ID`",
        "spark.sql.catalog.spark_catalog.glue.lakeformation-enabled": "true",
        "spark.sql.catalog.dropDirectoryBeforeTable.enabled": "true",
    }
}
```

For Delta Lake tables

```
%%configure -f
{
    "conf": {
        "spark.hadoop.fs.s3.credentialsResolverClass": "com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver",
        "spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject": true,
        "spark.hadoop.fs.s3.folderObject.autoAction.disabled": true,
        "spark.sql.catalog.skipLocationValidationOnCreateTable.enabled": true,
        "spark.sql.catalog.createDirectoryAfterTable.enabled": true,
        "spark.sql.catalog.dropDirectoryBeforeTable.enabled": true
    }
}
```

For Hudi tables

```
%%configure -f
{
    "conf": {
        "spark.hadoop.fs.s3.credentialsResolverClass": "com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver",
        "spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject": true,
        "spark.hadoop.fs.s3.folderObject.autoAction.disabled": true,
        "spark.sql.catalog.skipLocationValidationOnCreateTable.enabled": true,
        "spark.sql.catalog.createDirectoryAfterTable.enabled": true,
        "spark.sql.catalog.dropDirectoryBeforeTable.enabled": true,
        "spark.jars": "/usr/lib/hudi/hudi-spark-bundle.jar",
        "spark.sql.extensions": "org.apache.spark.sql.hudi.HoodieSparkSessionExtension",
        "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.hudi.catalog.HoodieCatalog",
        "spark.serializer": "org.apache.spark.serializer.KryoSerializer"
    }
}
```

Replace the placeholders:

- `S3_DATA_LOCATION`: Your S3 bucket path
- `REGION`: AWS region (e.g., us-east-1)
- `ACCOUNT_ID`: Your AWS account ID

###### Note

You must set these configurations before executing any Spark operations in your notebook.

#### Supported Operations

These operations will use AWS Lake Formation credentials to access the table data.

- CREATE TABLE
- ALTER TABLE
- INSERT INTO
- INSERT OVERWRITE
- UPDATE
- MERGE INTO
- DELETE FROM
- ANALYZE TABLE
- REPAIR TABLE
- DROP TABLE
- Spark datasource queries
- Spark datasource writes

###### Note

Operations not listed above will continue to use IAM permissions to access table data.

#### Considerations

- If a Hive table is created using a job that doesn’t have full table access enabled, and no records are inserted, subsequent reads or writes from a job with full table access will
  fail. This is because EMR Spark without full table access adds the `$folder$` suffix to the table folder name. To resolve this, you can either:
  - Insert at least one row into the table from a job that does not have FTA enabled.
  - Configure the job that does not have FTA enabled to not use `$folder$` suffix in folder name in S3. This can be achieved
    by setting Spark configuration `spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject=true`.
  - Create a S3 folder at the table location `s3://path/to/table/table_name` using the AWS S3 console or AWS S3 CLI.

- Full Table Access is supported with the EMR Filesystem (EMRFS) starting in Amazon EMR release 7.8.0, and with the S3A filesystem starting
  in Amazon EMR release 7.10.0.
- Full Table Access is supported for Hive, Iceberg, Delta, and Hudi tables.
- **Hudi FTA Write Support considerations:**
  - Hudi FTA writes require using HoodieCredentialedHadoopStorage for credential vending during job execution. Set the following configuration when running Hudi jobs: `hoodie.storage.class=org.apache.spark.sql.hudi.storage.HoodieCredentialedHadoopStorage`
  - Full Table Access (FTA) write support for Hudi is available starting from Amazon EMR release 7.12.
  - Hudi FTA write support currently works only with the default Hudi configurations. Custom or non-default Hudi settings may not be fully supported and could result in unexpected behavior.
  - Clustering for Hudi Merge-On-Read (MOR) tables is not supported at this point under FTA write mode.

- Jobs referencing tables with Lake Formation Fine-Grained Access Control (FGAC) rules or Glue Data Catalog Views will fail. To query a table
  with an FGAC rules or a Glue Data Catalog View, you must use the FGAC mode. You can enable FGAC mode by following the steps
  outlined in the AWS documentation: [Using Amazon EMR on EC2 with AWS Lake Formation for fine-grained access
  control](emr-serverless-lf-enable.md "emr-serverless-lf-enable.md").
- Full table access does not support Spark Streaming.
- When writing Spark DataFrame to a Lake Formation table, only APPEND mode is
  supported for Hive and Iceberg tables: `df.write.mode("append").saveAsTable(`table_name`)`
- Creating external tables requires IAM permissions.
- Because Lake Formation temporarily caches credentials within a Spark job, a Spark batch job or interactive session that is currently running
  might not reflect permission changes.
- You must use user defined role and not a service-linked
  role:[Lake Formation requirements for roles](../../../lake-formation/latest/dg/registration-role.md "../../../lake-formation/latest/dg/registration-role.md").

#### Hudi FTA Write Support - Supported Operations

The following table shows the supported write operations for Hudi Copy-On-Write (COW) and Merge-On-Read (MOR) tables under Full Table Access mode:

| Hudi FTA Supported Write Operations | Table Type             | Operation                                          | SQL Write Command | Status |
| ----------------------------------- | ---------------------- | -------------------------------------------------- | ----------------- | ------ |
| COW                                 | INSERT                 | INSERT INTO TABLE                                  | Supported         |
| COW                                 | INSERT                 | INSERT INTO TABLE<br>• PARTITION (Static, Dynamic) | Supported         |
| COW                                 | INSERT                 | INSERT OVERWRITE                                   | Supported         |
| COW                                 | INSERT                 | INSERT OVERWRITE<br>• PARTITION (Static, Dynamic)  | Supported         |
| UPDATE                              | UPDATE                 | UPDATE TABLE                                       | Supported         |
| COW                                 | UPDATE                 | UPDATE TABLE<br>• Change Partition                 | Not Supported     |
| DELETE                              | DELETE                 | DELETE FROM TABLE                                  | Supported         |
| ALTER                               | ALTER                  | ALTER TABLE<br>• RENAME TO                         | Not Supported     |
| COW                                 | ALTER                  | ALTER TABLE<br>• SET TBLPROPERTIES                 | Supported         |
| COW                                 | ALTER                  | ALTER TABLE<br>• UNSET TBLPROPERTIES               | Supported         |
| COW                                 | ALTER                  | ALTER TABLE<br>• ALTER COLUMN                      | Supported         |
| COW                                 | ALTER                  | ALTER TABLE<br>• ADD COLUMNS                       | Supported         |
| COW                                 | ALTER                  | ALTER TABLE<br>• ADD PARTITION                     | Supported         |
| COW                                 | ALTER                  | ALTER TABLE<br>• DROP PARTITION                    | Supported         |
| COW                                 | ALTER                  | ALTER TABLE<br>• RECOVER PARTITIONS                | Supported         |
| COW                                 | ALTER                  | REPAIR TABLE SYNC PARTITIONS                       | Supported         |
| DROP                                | DROP                   | DROP TABLE                                         | Supported         |
| COW                                 | DROP                   | DROP TABLE<br>• PURGE                              | Supported         |
| CREATE                              | CREATE                 | CREATE TABLE<br>• Managed                          | Supported         |
| COW                                 | CREATE                 | CREATE TABLE<br>• PARTITION BY                     | Supported         |
| COW                                 | CREATE                 | CREATE TABLE IF NOT EXISTS                         | Supported         |
| COW                                 | CREATE                 | CREATE TABLE LIKE                                  | Supported         |
| COW                                 | CREATE                 | CREATE TABLE AS SELECT                             | Supported         |
| CREATE                              | CREATE                 | CREATE TABLE with LOCATION<br>• External Table     | Not Supported     |
| DATAFRAME(INSERT)                   | DATAFRAME(INSERT)      | saveAsTable.Overwrite                              | Supported         |
| COW                                 | DATAFRAME(INSERT)      | saveAsTable.Append                                 | Not Supported     |
| COW                                 | DATAFRAME(INSERT)      | saveAsTable.Ignore                                 | Supported         |
| COW                                 | DATAFRAME(INSERT)      | saveAsTable.ErrorIfExists                          | Supported         |
| COW                                 | DATAFRAME(INSERT)      | saveAsTable<br>• External table (Path)             | Not Supported     |
| COW                                 | DATAFRAME(INSERT)      | save(path)<br>• DF v1                              | Not Supported     |
| MOR                                 | INSERT                 | INSERT INTO TABLE                                  | Supported         |
| MOR                                 | INSERT                 | INSERT INTO TABLE<br>• PARTITION (Static, Dynamic) | Supported         |
| MOR                                 | INSERT                 | INSERT OVERWRITE                                   | Supported         |
| MOR                                 | INSERT                 | INSERT OVERWRITE<br>• PARTITION (Static, Dynamic)  | Supported         |
| UPDATE                              | UPDATE                 | UPDATE TABLE                                       | Supported         |
| MOR                                 | UPDATE                 | UPDATE TABLE<br>• Change Partition                 | Not Supported     |
| DELETE                              | DELETE                 | DELETE FROM TABLE                                  | Supported         |
| ALTER                               | ALTER                  | ALTER TABLE<br>• RENAME TO                         | Not Supported     |
| MOR                                 | ALTER                  | ALTER TABLE<br>• SET TBLPROPERTIES                 | Supported         |
| MOR                                 | ALTER                  | ALTER TABLE<br>• UNSET TBLPROPERTIES               | Supported         |
| MOR                                 | ALTER                  | ALTER TABLE<br>• ALTER COLUMN                      | Supported         |
| MOR                                 | ALTER                  | ALTER TABLE<br>• ADD COLUMNS                       | Supported         |
| MOR                                 | ALTER                  | ALTER TABLE<br>• ADD PARTITION                     | Supported         |
| MOR                                 | ALTER                  | ALTER TABLE<br>• DROP PARTITION                    | Supported         |
| MOR                                 | ALTER                  | ALTER TABLE<br>• RECOVER PARTITIONS                | Supported         |
| MOR                                 | ALTER                  | REPAIR TABLE SYNC PARTITIONS                       | Supported         |
| DROP                                | DROP                   | DROP TABLE                                         | Supported         |
| MOR                                 | DROP                   | DROP TABLE<br>• PURGE                              | Supported         |
| CREATE                              | CREATE                 | CREATE TABLE<br>• Managed                          | Supported         |
| MOR                                 | CREATE                 | CREATE TABLE<br>• PARTITION BY                     | Supported         |
| MOR                                 | CREATE                 | CREATE TABLE IF NOT EXISTS                         | Supported         |
| MOR                                 | CREATE                 | CREATE TABLE LIKE                                  | Supported         |
| MOR                                 | CREATE                 | CREATE TABLE AS SELECT                             | Supported         |
| CREATE                              | CREATE                 | CREATE TABLE with LOCATION<br>• External Table     | Not Supported     |
| DATAFRAME(UPSERT)                   | DATAFRAME(UPSERT)      | saveAsTable.Overwrite                              | Supported         |
| MOR                                 | DATAFRAME(UPSERT)      | saveAsTable.Append                                 | Not Supported     |
| MOR                                 | DATAFRAME(UPSERT)      | saveAsTable.Ignore                                 | Supported         |
| MOR                                 | DATAFRAME(UPSERT)      | saveAsTable.ErrorIfExists                          | Supported         |
| MOR                                 | DATAFRAME(UPSERT)      | saveAsTable<br>• External table (Path)             | Not Supported     |
| MOR                                 | DATAFRAME(UPSERT)      | save(path)<br>• DF v1                              | Not Supported     |
| DATAFRAME(DELETE)                   | DATAFRAME(DELETE)      | saveAsTable.Append                                 | Not Supported     |
| MOR                                 | DATAFRAME(DELETE)      | saveAsTable<br>• External table (Path)             | Not Supported     |
| MOR                                 | DATAFRAME(DELETE)      | save(path)<br>• DF v1                              | Not Supported     |
| DATAFRAME(BULK_INSERT)              | DATAFRAME(BULK_INSERT) | saveAsTable.Overwrite                              | Supported         |
| MOR                                 | DATAFRAME(BULK_INSERT) | saveAsTable.Append                                 | Not Supported     |
| MOR                                 | DATAFRAME(BULK_INSERT) | saveAsTable.Ignore                                 | Supported         |
| MOR                                 | DATAFRAME(BULK_INSERT) | saveAsTable.ErrorIfExists                          | Supported         |
| MOR                                 | DATAFRAME(BULK_INSERT) | saveAsTable<br>• External table (Path)             | Not Supported     |
| MOR                                 | DATAFRAME(BULK_INSERT) | save(path)<br>• DF v1                              | Not Supported     |
