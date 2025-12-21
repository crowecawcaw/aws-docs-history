# Using AWS Glue with AWS Lake Formation for Full Table Access

## Introduction to Full Table Access

AWS Glue 5.0 and above supports Full Table Access (FTA) control in Apache Spark based on your policies defined in AWS Lake Formation.
This feature enables read and write operations from your AWS Glue Spark jobs on AWS Lake Formation registered tables when the job role
has full table access. FTA is ideal for use cases that need to comply with security regulations at the table level and supports Spark capabilities including Resilient Distributed Datasets (RDDs), custom libraries, and User Defined Functions (UDFs) with AWS Lake Formation tables.

When a AWS Glue Spark job is configured for Full Table Access (FTA), AWS Lake Formation credentials are used to read/write Amazon S3 data for AWS Lake Formation registered tables,
while the job's runtime role credentials will be used to read/write tables not registered with AWS Lake Formation. This capability enables Data Manipulation Language (DML) operations including CREATE, ALTER, DELETE, UPDATE, and MERGE INTO statements on Apache Hive and Iceberg tables.

###### Note

Review your requirements and determine if Fine-Grained Access Control (FGAC) or Full Table Access (FTA) suits your needs. Only one AWS Lake Formation permission method can be enabled for a given AWS Glue job. A job cannot simultaneously run Full Table Access (FTA) and Fine-Grained Access Control (FGAC) at the same time.

## How Full-Table Access (FTA) works on AWS Glue

AWS Lake Formation offers two approaches for data access control: Fine-Grained Access Control (FGAC) and Full Table Access (FTA).
FGAC provides enhanced security through column, row, and cell-level filtering, ideal for scenarios requiring granular permissions.
FTA is ideal for straightforward access control scenarios where you need table-
level permissions. It simplifies implementation by eliminating the need to enable
fine-grained access mode, improves performance and reduces cost by avoiding the
system driver and system executors, and supports both read and write operations (
including CREATE, ALTER, DELETE, UPDATE, and MERGE INTO commands).

In AWS Glue 4.0, AWS Lake Formation based data access worked through GlueContext class, the utility class provided by AWS Glue.
In AWS Glue 5.0, AWS Lake Formation based data access is available through native Spark SQL, Spark DataFrames, and continues to be supported
through GlueContext class.

## Implementing Full Table Access

### Step 1: Enable Full Table Access in AWS Lake Formation

To use Full Table Access (FTA) mode, you need to allow third-party query engines to access data without the IAM session tag validation
in AWS Lake Formation. To enable, follow the steps in
[Application integration for full table access](../../../lake-formation/latest/dg/full-table-credential-vending.md "../../../lake-formation/latest/dg/full-table-credential-vending.md") .

### Step 2: Setup IAM permissions for job runtime role

For read or write access to underlying data, in addition to AWS Lake Formation permissions, a job runtime role needs the
`lakeformation:GetDataAccess` IAM permission. With this permission, AWS Lake Formation grants the request for temporary
credentials to access the data.

The following is an example policy of how to provide IAM permissions to access a script in Amazon S3, uploading logs to Amazon S3, AWS Glue API permissions,
and permission to access AWS Lake Formation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ScriptAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/scripts/*"
 ]
 },
 {
 "Sid": "LoggingAccess",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/logs/*"
 ]
 },
 {
 "Sid": "GlueCatalogAccess",
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:GetTable",
 "glue:GetTables",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:CreateTable",
 "glue:UpdateTable"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/default",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/default/*"
 ]
 },
 {
 "Sid": "LakeFormationAccess",
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": "*"
 }
 ]
}`

```

#### Step 2.1 Configure AWS Lake Formation permissions

AWS Glue Spark jobs that read data from Amazon S3 require AWS Lake Formation SELECT permission.

AWS Glue Spark jobs that write/delete data in Amazon S3 require AWS Lake Formation ALL permission.

AWS Glue Spark jobs that interact with AWS Glue Data catalog require DESCRIBE, ALTER, DROP permission as appropriate.

### Step 3: Initialize a Spark session for Full Table Access using AWS Lake Formation

To access tables registered with AWS Lake Formation, the following configurations need to be set during Spark initialization to
configure Spark to use AWS Lake Formation credentials.

To access tables registered with AWS Lake Formation, you need to explicitly
configure your Spark session to use AWS Lake Formation credentials. Add the
following configurations when initializing your Spark session:

```
from pyspark.sql import SparkSession

# Initialize Spark session with Lake Formation configurations
spark = SparkSession.builder \
    .appName("Lake Formation Full Table Access") \
    .config("spark.sql.catalog.glue_catalog", "org.apache.spark.sql.catalog.hive.GlueCatalog") \
    .config("spark.sql.catalog.glue_catalog.glue.lakeformation-enabled", "true") \
    .config("spark.sql.defaultCatalog", "glue_catalog") \
    .getOrCreate()
```

Key configurations:

- `spark.sql.catalog.glue_catalog`: Registers a catalog named "glue_catalog" that uses
  the GlueCatalog implementation
- `spark.sql.catalog.glue_catalog.glue.lakeformation-enabled`: Explicitly enables AWS Lake Formation integration for this catalog
- The catalog name ("glue_catalog" in this example) can be customized, but must be
  consistent in both configuration settings

#### Hive

```

‐‐conf spark.hadoop.fs.s3.credentialsResolverClass=com.amazonaws.AWS Glue.accesscontrol.AWSLakeFormationCredentialResolver
--conf spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject=true
--conf spark.hadoop.fs.s3.folderObject.autoAction.disabled=true
--conf spark.sql.catalog.skipLocationValidationOnCreateTable.enabled=true
--conf spark.sql.catalog.createDirectoryAfterTable.enabled=true
--conf spark.sql.catalog.dropDirectoryBeforeTable.enabled=true

```

#### Iceberg

```

--conf spark.hadoop.fs.s3.credentialsResolverClass=com.amazonaws.AWS Glue.accesscontrol.AWSLakeFormationCredentialResolver
--conf spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject=true
--conf spark.hadoop.fs.s3.folderObject.autoAction.disabled=true
--conf spark.sql.catalog.skipLocationValidationOnCreateTable.enabled=true
--conf spark.sql.catalog.createDirectoryAfterTable.enabled=true
--conf spark.sql.catalog.dropDirectoryBeforeTable.enabled=true
--conf spark.sql.catalog.<catalog>.AWS Glue.lakeformation-enabled=true

```

- `spark.hadoop.fs.s3.credentialsResolverClass=com.amazonaws.AWS Glue.accesscontrol.AWSLakeFormationCredentialResolver`:
  Configure EMR Filesystem (EMRFS) to use AWS Lake Formation S3 credentials for AWS Lake Formation registered tables.
  If the table is not registered, use the job's runtime role credentials.
- `spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject=true` and `spark.hadoop.fs.s3.folderObject.autoAction.disabled=true`:
  Configure EMRFS to use content type header application/x-directory instead of $folder$ suffix when creating S3 folders. This is
  required when reading AWS Lake Formation tables, as AWS Lake Formation credentials do not allow reading table folders
  with $folder$ suffix.
- `spark.sql.catalog.skipLocationValidationOnCreateTable.enabled=true`: Configure Spark to skip validating the table location's
  emptiness before creation. This is necessary for AWS Lake Formation registered tables, as AWS Lake Formation
  credentials to verify the empty location are available only after AWS Glue Data Catalog table creation. Without this configuration, the job's
  runtime role credentials will validate the empty table location.
- `spark.sql.catalog.createDirectoryAfterTable.enabled=true`: Configure Spark to create the Amazon S3 folder after table creation
  in the Hive metastore. This is required for AWS Lake Formation registered tables, as AWS Lake Formation credentials to
  create the Amazon S3 folder are available only after AWS Glue Data Catalog table creation.
- `spark.sql.catalog.dropDirectoryBeforeTable.enabled=true`: Configure Spark to drop the Amazon S3 folder before table deletion in the
  Hive metastore. This is necessary for AWS Lake Formation registered tables, as AWS Lake Formation credentials to drop
  the S3 folder are not available after table deletion from the AWS Glue Data Catalog.
- `spark.sql.catalog.<catalog>.AWS Glue.lakeformation-enabled=true`: Configure Iceberg catalog to use AWS Lake Formation Amazon S3
  credentials for AWS Lake Formation registered tables. If the table is not registered, use default environment credentials.

## Usage Patterns

### Using FTA with DataFrames

For users familiar with Spark, DataFrames can be used with AWS Lake Formation Full Table Access.

AWS Glue 5.0 adds native Spark support for Lake Formation Full Table Access, simplifying how you work with protected tables. This feature enables AWS Glue 5.0 AWS Glue Spark jobs to directly read and write data when full table access is granted, removing limitations that previously restricted certain Extract, Transform, and Load (ETL) operations. You can now leverage advanced Spark capabilities including Resilient Distributed Datasets (RDDs), custom libraries, and User Defined Functions (UDFs) with AWS Lake Formation tables.

#### Native Spark FTA in AWS Glue 5.0

AWS Glue 5.0 supports full-table access (FTA) control in Apache Spark based on your policies defined in AWS Lake Formation. This level of control is ideal for use cases that need to comply with security regulations at the table level.

#### Apache Iceberg Table Example

```
from pyspark.sql import SparkSession

catalog_name = "spark_catalog"
aws_region = "us-east-1"
aws_account_id = "123456789012"
warehouse_path = "s3://amzn-s3-demo-bucket/warehouse/"

spark = SparkSession.builder \
    .config("spark.sql.extensions","org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkSessionCatalog") \
    .config(f"spark.sql.catalog.{catalog_name}.warehouse", f"{warehouse_path}") \
    .config(f"spark.sql.catalog.{catalog_name}.client.region",f"{aws_region}") \
    .config(f"spark.sql.catalog.{catalog_name}.glue.account-id",f"{aws_account_id}") \
    .config(f"spark.sql.catalog.{catalog_name}.glue.lakeformation-enabled","true") \
    .config(f"spark.sql.catalog.dropDirectoryBeforeTable.enabled", "true") \
    .config(f"spark.sql.catalog.{catalog_name}.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog") \
    .config(f"spark.sql.catalog.{catalog_name}.io-impl", "org.apache.iceberg.aws.s3.S3FileIO") \
    .config("spark.sql.defaultCatalog", catalog_name) \  # Add this line
    .getOrCreate()

database_name = "your_database"
table_name = "your_table"

df = spark.sql(f"select * from {database_name}.{table_name}")
df.show()
```

#### Required IAM Permissions

Your AWS Glue job execution role must have:

```
{
    "Action": "lakeformation:GetDataAccess",
    "Resource": "*",
    "Effect": "Allow"
}
```

Plus appropriate S3 access permissions for your data locations.

#### Lake Formation Configuration

Before using native Spark FTA in AWS Glue 5.0:

1. Allow third-party query engines to access data without IAM session tag validation in AWS Lake Formation
2. Grant appropriate table permissions to your AWS Glue job execution role through AWS Lake Formation console
3. Configure your Spark session with the required parameters shown in the example above

### Using FTA with DynamicFrames

AWS Glue's native DynamicFrames can be used with AWS Lake Formation Full Table Access for optimized ETL operations. Full Table Access (FTA)
provides a security model that grants permissions at the table level, allowing for faster data processing compared to Fine-Grained Access Control (FGAC)
since it bypasses the overhead of row and column-level permission checks. This approach is useful when you need to process entire tables
and table-level permissions meet your security requirements.

In AWS Glue 4.0, DynamicFrames with FTA required specific GlueContext configuration. While existing AWS Glue 4.0 DynamicFrame code with FTA will continue to work in AWS Glue 5.0, the newer version also offers native Spark FTA support with greater flexibility. For new development, consider using the native Spark approach described in the DataFrames section, especially if you need additional capabilities such as Resilient Distributed Datasets (RDDs), custom libraries, and User Defined Functions (UDFs) with AWS Lake Formation tables.

#### Required Permissions

The IAM role executing your Glue job must have:

- `lakeformation:GetDataAccess` permission
- Appropriate Lake Formation table permissions granted through the Lake Formation console

#### Example DynamicFrame Implementation in AWS Glue 5.0

```
from awsglue.context import GlueContext
from pyspark.context import SparkContext

# Initialize Glue context
sc = SparkContext()
glueContext = GlueContext(sc)

# Configure catalog for Iceberg tables
catalog_name = "glue_catalog"
aws_region = "us-east-1"
aws_account_id = "123456789012"
warehouse_path = "s3://amzn-s3-demo-bucket/warehouse/"

spark = glueContext.spark_session
spark.conf.set(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkCatalog")
spark.conf.set(f"spark.sql.catalog.{catalog_name}.warehouse", f"{warehouse_path}")
spark.conf.set(f"spark.sql.catalog.{catalog_name}.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog")
spark.conf.set(f"spark.sql.catalog.{catalog_name}.io-impl", "org.apache.iceberg.aws.s3.S3FileIO")
spark.conf.set(f"spark.sql.catalog.{catalog_name}.glue.lakeformation-enabled","true")
spark.conf.set(f"spark.sql.catalog.{catalog_name}.client.region",f"{aws_region}")
spark.conf.set(f"spark.sql.catalog.{catalog_name}.glue.id", f"{aws_account_id}")

# Read Lake Formation-protected table with DynamicFrame
df = glueContext.create_data_frame.from_catalog(
    database="your_database",
    table_name="your_table"
)
```

## Additional Configuration

### Configure full table access mode in AWS Glue Studio notebooks

To access AWS Lake Formation registered tables from interactive Spark sessions in AWS Glue Studio notebooks, you must use compatibility
permission mode. Use the `%%configure` magic command to set up your Spark configuration before starting your interactive session. This configuration must be the first command in your notebook, as it cannot be applied after the session has started. Choose the configuration based on your table
type:

#### For Hive tables

```
%%configure
--conf spark.hadoop.fs.s3.credentialsResolverClass=com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver
--conf spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject=true
--conf spark.hadoop.fs.s3.folderObject.autoAction.disabled=true
--conf spark.sql.catalog.skipLocationValidationOnCreateTable.enabled=true
--conf spark.sql.catalog.createDirectoryAfterTable.enabled=true
--conf spark.sql.catalog.dropDirectoryBeforeTable.enabled=true
```

#### For Iceberg tables

```
%%configure
--conf spark.hadoop.fs.s3.credentialsResolverClass=com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialResolver
--conf spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject=true
--conf spark.hadoop.fs.s3.folderObject.autoAction.disabled=true
--conf spark.sql.catalog.skipLocationValidationOnCreateTable.enabled=true
--conf spark.sql.catalog.createDirectoryAfterTable.enabled=true
--conf spark.sql.catalog.dropDirectoryBeforeTable.enabled=true
--conf spark.sql.catalog.glue_catalog.glue.lakeformation-enabled=true
--conf spark.sql.catalog.glue_catalog.warehouse=s3://example-s3-bucket_DATA_LOCATION
--conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog
--conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO
--conf spark.sql.catalog.glue_catalog.glue.account-id=ACCOUNT_ID
--conf spark.sql.catalog.glue_catalog.glue.region=REGION
```

Replace the placeholders:

- S3_DATA_LOCATION: `s3://amzn-s3-demo-bucket`
- REGION: `AWS Region (e.g., us-east-1)`
- ACCOUNT_ID: `Your AWS Account ID`

###### Note

You must set these configurations before executing any Spark operations in your notebook.

### Supported Operations

These operations will use AWS Lake Formation credentials to access the table data.

###### Note

On enabling AWS Lake Formation:

- For FTA: Enable the Spark configuration `spark.sql.catalog.{catalog_name}.glue.lakeformation-enabled`

- CREATE TABLE
- ALTER TABLE
- INSERT INTO
- INSERT OVERWRITE
- SELECT
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

## Migrating from AWS Glue 4.0 to AWS Glue 5.0 FTA

When migrating from AWS Glue 4.0 GlueContext FTA to AWS Glue 5.0 native Spark FTA:

1. Allow third-party query engines to access data without the IAM session tag validation in AWS Lake Formation.
   Follow [Step 1: Enable Full Table Access in AWS Lake Formation](#security-access-control-fta-step-1 "#security-access-control-fta-step-1").
2. You do not need to change the job runtime role. However, verify that the AWS Glue job execution role has lakeformation:GetDataAccess IAM permission.
3. Modify spark session configurations in the script. Ensure the following spark configurations are present:

```
--conf spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkSessionCatalog
--conf spark.sql.catalog.spark_catalog.warehouse=s3://<bucket-name>/warehouse/
--conf spark.sql.catalog.spark_catalog.client.region=<REGION>
--conf spark.sql.catalog.spark_catalog.glue.account-id=ACCOUNT_ID
--conf spark.sql.catalog.spark_catalog.glue.lakeformation-enabled=true
--conf spark.sql.catalog.dropDirectoryBeforeTable.enabled=true
```

4. Update script such that GlueContext DataFrames are changed to native spark DataFrames.
5. Update your AWS Glue job to use AWS Glue 5.0

## Considerations and Limitations

- If a Hive table is created using a job that doesn't have full table access enabled, and no records are inserted, subsequent reads or writes from a job with full table access will fail. This is because AWS Glue Spark without full table access adds the $folder$ suffix to the table folder name. To resolve this, you can either:
  - Insert at least one row into the table from a job that does not have FTA enabled.
  - Configure the job that does not have FTA enabled to not use $folder$ suffix in folder name in S3. This can be achieved by setting Spark
    configuration `spark.hadoop.fs.s3.useDirectoryHeaderAsFolderObject=true`.
  - Create an Amazon S3 folder at the table location `s3://path/to/table/table_name` using the Amazon S3 console or Amazon S3 CLI.

- Full Table Access works exclusively with EMR Filesystem (EMRFS). S3A filesystem is not compatible.
- Full Table Access is supported for Hive and Iceberg tables. Support for Hudi and Delta tables has not yet been added.
- Jobs referencing tables with AWS Lake Formation Fine-Grained Access Control (FGAC) rules or AWS Glue Data Catalog Views will fail.
  To query a table with an FGAC rules or a AWS Glue Data Catalog View, you need to use the FGAC mode. You can enable FGAC mode by following the
  steps outlined in the AWS documentation: Using AWS Glue with AWS Lake Formation for fine-grained access control.
- Full table access does not support Spark Streaming.
- Cannot be used simultaneously with FGAC.
