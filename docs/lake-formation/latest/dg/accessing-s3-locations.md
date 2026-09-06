

# Accessing Amazon S3 locations
<a name="accessing-s3-locations"></a>

AWS Lake Formation enables you to read and write the underlying data files in Amazon Simple Storage Service (Amazon S3) for tables registered in the AWS Glue Data Catalog (Data Catalog). This provides you with a single set of permissions for both SQL queries and direct file access using your existing Lake Formation table grants. Lake Formation extends its credential vending functionality to Amazon S3 locations registered in the Data Catalog. When your application requests access to the Amazon S3 files underlying a Data Catalog table, Lake Formation evaluates the caller's existing table-level permissions and, if authorized, returns short-lived, scoped Amazon S3 credentials for that table's registered location.

**Enable direct access to Amazon S3 locations**  
To enable this feature, you must complete the following steps.

**Prerequisites**  
Complete the following prerequisites before enabling the feature flag:
+ **Specify table location** – Specify the path to your data in Amazon S3 using the LOCATION property in the table attributes. For more information about the location format, see [Table location in Amazon S3](https://docs.aws.amazon.com/athena/latest/ug/tables-location-format.html) in the *Amazon Athena User Guide*.
+ **Register Amazon S3 locations** – Catalog your tables in the Data Catalog for your Amazon S3 locations and register them with Lake Formation by providing the Amazon S3 bucket owner account. When you register a location, that Amazon S3 path and all folders under that path are registered. For more information, see [Registering an Amazon S3 location](register-location.md).
+ **Grant Lake Formation permissions** – Grant Lake Formation `SELECT` (or `SUPER`) permissions on tables to your data scientists and applications using the Lake Formation console or APIs. If you already use Lake Formation for table access with services like Athena or Amazon EMR, this is already configured.
+ **Enable Application Integration with Full Table Access** – Enable Application Integration with Full Table Access to allow credential vending to the registered table location. For more information, see [Application integration for full table access](full-table-credential-vending.md).

**Enable the feature flag**  
Enable the `fs.s3a.lakeformation.access.grants.enabled` flag on supported engines:

```
fs.s3a.lakeformation.access.grants.enabled = true
```
+ **Amazon EMR on Amazon EC2** – EMR 7.13 or later
+ **Amazon EMR on EKS** – EMR 7.13 or later
+ **Amazon EMR Serverless** – EMR 7.13 or later

Once configured, you can immediately read or write data files from EMR using standard APIs.

For more information on Amazon EMR integration, see [Lake Formation path-based credential vending](https://docs.aws.amazon.com/emr/latest/ManagementGuide/lake-formation-path-based-credential-vending.html) in the *Amazon EMR Management Guide*.

**How it works**  
Lake Formation-based Amazon S3 location access follows this flow:

1. A principal or role requests access to Amazon S3 data files through a service such as an Amazon EMR Spark job, or data processing pipeline.

1. The AWS SDK plugin integrated with EMR intercepts the Amazon S3 request and calls the Lake Formation [GetTemporaryDataLocationCredentials](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryDataLocationCredentials.html) API.

1. Lake Formation checks if the Amazon S3 path corresponds to a registered location and cataloged table, and evaluates the caller's permissions on the associated AWS Glue table.

1. If the caller has `SELECT` or `SUPER` permissions on the corresponding table with full table access, Lake Formation vends temporary credentials scoped to that Amazon S3 location. `SELECT` grants **READ** credentials; `SUPER` grants **READWRITE** credentials.

1. The plugin uses these credentials to complete the Amazon S3 request, and Amazon S3 provides the data to the application.

1. All credential vending operations are logged to CloudTrail, providing an audit trail for data access.

This process is transparent to you and you will simply use existing Lake Formation permissions with standard file-based APIs.

```
# Read raw data (Lake Formation-based S3 Location access)
raw_df = spark.read.json("s3://finance-datalake/raw/transactions/dt=2024-03-21/")

# Read governed data (Lake Formation-based S3 Location access)
transactions_df = spark.read.parquet("s3://data-lake/transactions/year=2026/")

# Write processed data (Lake Formation-based S3 Location access)
processed_df.write \
    .mode("append") \
    .partitionBy("transaction_date") \
    .parquet("s3://finance-datalake/processed/transactions/")

print("ETL complete. Records written:", processed_df.count())
```

**Permission requirements**  
The feature currently vends credentials only when the caller has **full table access**, meaning `SELECT` on all columns without row or column filters. If a table has row-level or column-level filters applied, callers must continue using trusted engines like Athena, Amazon EMR, AWS Glue, or Amazon Redshift that can enforce those filters. This ensures security boundaries remain consistent.

**Cross-account access**  
Lake Formation simplified access to Amazon S3 locations works with cross-account sharing capabilities. When you share a table with another AWS account through Lake Formation, recipients can access the underlying Amazon S3 data files using their Lake Formation permissions, subject to the same full table access requirements.

The feature supports Lake Formation's resource link mechanism for cross-account access. When a consumer account has permissions on a shared table, Lake Formation vends credentials scoped to the registered account's Amazon S3 location, enabling seamless cross-account data access without requiring separate Amazon S3 bucket policies or cross-account IAM roles.

**Nested Amazon S3 locations**  
When multiple tables point to nested locations in the same bucket, Lake Formation applies the following behavior:
+ When accessing `s3://bucket`, you receive permissions corresponding to the table registered at the bucket level.
+ When accessing `s3://bucket/folder1`, you receive permissions corresponding to the table registered at that specific path.
+ For access to folders without a registered table (for example, `s3://bucket/folder2`), you receive permissions from the nearest parent registered location.
+ If multiple tables are registered at the same location, Lake Formation returns an error due to conflicting permissions.

**Auditing and compliance**  
All credential vending operations are logged to CloudTrail, providing an audit trail for data access. When Lake Formation vends credentials through the `GetTemporaryDataLocationCredentials` API, CloudTrail records:
+ The principal (user or role)
+ Timestamp
+ Amazon S3 location
+ Associated AWS Glue table

Subsequent Amazon S3 API calls made with those credentials are also logged to CloudTrail as Amazon S3 data events, with context linking them back to the Lake Formation permission grant. This provides auditors with complete visibility into who accessed what data, when, and through which permission path—all in a single CloudTrail log stream.

**Supported AWS services**  
Lake Formation simplified access to Amazon S3 locations works with:
+ Amazon EMR on Amazon EC2 (EMR 7.13 or later)
+ Amazon EMR on EKS (EMR 7.13 or later)
+ Amazon EMR Serverless (EMR 7.13 or later)

**Open source plugin for third-party services**  
You can also integrate your Apache Spark or Trino applications using APIs or through an open source plugin provided by AWS. For more information, see [aws-lakeformation-accessgrants-plugin-java-v2](https://github.com/aws/aws-lakeformation-accessgrants-plugin-java-v2) on GitHub.

**Considerations**  
Note the following considerations when using credential vending for Amazon S3 locations:
+ Credential vending for Amazon S3 locations is not supported cross-region.
+ Credential vending is supported for Amazon S3 locations included as the table's primary location.
+ The plugin supports Apache Hive, Apache Hudi, and Delta Lake table formats. Apache Iceberg is not currently supported.
+ The plugin is not currently supported with Amazon EMR Spark Fine-Grained Access Control (FGAC) mode.