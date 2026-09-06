

# Loading data into Aurora DSQL
<a name="loading-data"></a>

Whether you are migrating from an existing database, importing files from Amazon Simple Storage Service, or loading data from your local system, Aurora DSQL provides multiple approaches for getting your data in. This section covers the recommended tools and techniques for data loads of all sizes, from gigabytes to hundreds of terabytes.

## Choosing a loading approach
<a name="loading-data-options"></a>

Aurora DSQL supports standard PostgreSQL data loading commands, but loading data efficiently at scale requires handling parallelization, connection management, and error recovery. The following table summarizes your options:


| Approach | Best for | Considerations | 
| --- | --- | --- | 
| Aurora DSQL Loader - Open source utility that makes it easy to parallelize inserts when using Aurora DSQL | Most data loading scenarios, especially migrations and bulk imports | Handles parallelization, connection pooling, conflict resolution, and IAM authentication automatically. Available as source code or binary. | 
| PostgreSQL \\copy - Client-side psql meta-command | Simple loads when you are already connected via psql | Reads files on the client and streams data over the connection; you manage parallelization yourself | 
| INSERT transactions - Standard SQL DML | Small datasets or application-driven inserts | Simplest approach but slowest for bulk data | 

For most data loading tasks, use the Aurora DSQL Loader. It handles the operational complexity of loading data into a distributed database, including parallel execution across multiple connections and automatic retry of failed operations.

## Aurora DSQL Loader
<a name="aurora-dsql-loader"></a>

The [Aurora DSQL Loader](https://github.com/aws-samples/aurora-dsql-loader) is an open-source command-line utility designed to efficiently load data into Aurora DSQL clusters. It manages connection pooling, parallelizes data transfer across multiple workers, and handles conflicts and retries automatically.

### Key features
<a name="aurora-dsql-loader-features"></a>

The Aurora DSQL Loader provides the following capabilities:

**Parallel loading**  
Configurable worker threads enable concurrent data loading across multiple connections for improved performance.

**Connection pooling**  
Manages a pool of connections to your Aurora DSQL cluster, handling IAM authentication and connection lifecycle automatically.

**Multiple file format support**  
Supports CSV (comma-separated values), TSV (tab-separated values), and Apache Parquet columnar format. The loader automatically detects the file format based on the source URI extension.

**Automatic schema inference**  
When used with the `--if-not-exists` flag, the loader can automatically create tables with appropriate column types based on the data.

**Conflict handling**  
When your target table has unique constraints, configure how the loader handles conflicts using the `--on-conflict` option: skip duplicates, upsert records, or return an error.

**Fault tolerance**  
Automatic retries and job resumption capabilities ensure that interrupted loads can continue from their stopping point rather than restarting entirely.

**Local and S3 sources**  
Load data from local file system paths or directly from Amazon S3 buckets using S3 URIs.

### Prerequisites
<a name="aurora-dsql-loader-prerequisites"></a>

Before using the Aurora DSQL Loader, ensure you have the following:
+ An active Aurora DSQL cluster with a valid endpoint.
+ AWS credentials configured through the AWS CLI (**aws configure**), AWS Single Sign-On (**aws sso login**), or IAM roles.
+ IAM permissions: `dsql:DbConnectAdmin` or `dsql:DbConnect` on your Aurora DSQL cluster.
+ For S3 sources, appropriate permissions to read from the source bucket.

### Installation
<a name="aurora-dsql-loader-installation"></a>

Download the latest release from the [GitHub releases page](https://github.com/aws-samples/aurora-dsql-loader/releases/latest). Pre-built binaries are available for common platforms. For instructions on building from source, see the [Aurora DSQL Loader repository](https://github.com/aws-samples/aurora-dsql-loader).

### Usage examples
<a name="aurora-dsql-loader-usage"></a>

The following examples demonstrate common use cases for the Aurora DSQL Loader.

**Example Loading a local CSV file**  <a name="aurora-dsql-loader-example-basic"></a>
This example loads a CSV file from your local file system into an existing table:  

```
aurora-dsql-loader load \
  --endpoint {{cluster-id}}.dsql.{{region}}.on.aws \
  --source-uri {{data.csv}} \
  --table {{my_table}}
```

**Example Loading data from Amazon S3**  <a name="aurora-dsql-loader-example-s3"></a>
This example loads a Parquet file from an Amazon S3 bucket:  

```
aurora-dsql-loader load \
  --endpoint {{cluster-id}}.dsql.{{region}}.on.aws \
  --source-uri s3://{{my-bucket}}/{{data.parquet}} \
  --table {{my_table}}
```

**Example Automatic table creation**  <a name="aurora-dsql-loader-example-create-table"></a>
This example creates a new table automatically based on the data schema:  

```
aurora-dsql-loader load \
  --endpoint {{cluster-id}}.dsql.{{region}}.on.aws \
  --source-uri {{data.csv}} \
  --table {{my_table}} \
  --if-not-exists
```

**Example Validating before loading**  <a name="aurora-dsql-loader-example-dry-run"></a>
This example validates your configuration without actually loading data:  

```
aurora-dsql-loader load \
  --endpoint {{cluster-id}}.dsql.{{region}}.on.aws \
  --source-uri {{data.csv}} \
  --table {{my_table}} \
  --dry-run
```

**Example Resuming an interrupted load**  <a name="aurora-dsql-loader-example-resume"></a>
If a load operation is interrupted, you can resume it using the job ID from the previous run:  

```
aurora-dsql-loader load \
  --endpoint {{cluster-id}}.dsql.{{region}}.on.aws \
  --source-uri {{data.csv}} \
  --table {{my_table}} \
  --resume-job-id {{job-id}} \
  --manifest-dir {{./loader-state}}
```
When resuming, the loader skips most already-completed work but may retry some records. If your target table has unique constraints, use the `--on-conflict` option to handle duplicates—for example, `DO NOTHING` to skip them or `DO UPDATE` to upsert.

### Command-line options
<a name="aurora-dsql-loader-options"></a>

The Aurora DSQL Loader supports the following command-line options:

`--endpoint`  
(Required) The Aurora DSQL cluster endpoint. Example: `{{cluster-id}}.dsql.{{region}}.on.aws`

`--source-uri`  
(Required) The path to the data file. Can be a local file path or an S3 URI (for example, `s3://{{bucket-name}}/{{file.parquet}}`).

`--table`  
(Required) The name of the target table in your Aurora DSQL database.

`--if-not-exists`  
(Optional) Automatically create the target table if it does not exist. The loader infers the schema from the data.

`--dry-run`  
(Optional) Validate the configuration and data without actually loading it into the database.

`--resume-job-id`  
(Optional) Resume a previously interrupted load operation using the specified job ID.

`--manifest-dir`  
(Optional) Directory for storing job state and manifests, used for job resumption.

`--on-conflict`  
(Optional) Specifies how to handle conflicts when inserting rows that violate unique constraints on the target table. Valid values are `error` (return an error), `do-nothing` (skip duplicate rows), or `do-update` (update existing rows with new values).

For a complete list of options and additional configuration parameters, run:

```
aurora-dsql-loader load --help
```

### Best practices
<a name="aurora-dsql-loader-best-practices"></a>
+ **Use dry-run for validation** – Always test your load configuration with `--dry-run` before loading data into production tables.
+ **Define unique constraints for resumption** – If you need to resume interrupted loads, define unique constraints on your target tables and use the `--on-conflict` option to handle already-loaded records.
+ **Use Parquet for large datasets** – Parquet's columnar format typically provides better compression and faster loading for large datasets compared to CSV or TSV.
+ **Preserve manifest directories** – Keep the manifest directory for load jobs until you confirm the load completed successfully, enabling resumption if needed.
+ **Pre-create tables when possible** – Define the target table with explicit column data types and primary keys before loading data. Pre-created schemas give you control over type precision and indexing, which typically results in better query performance compared to auto-inferred schemas.

### Troubleshooting
<a name="aurora-dsql-loader-troubleshooting"></a>

Authentication errors  
Verify your AWS credentials are configured correctly and that your IAM identity has the required `dsql:DbConnect` or `dsql:DbConnectAdmin` permissions on the target cluster.

S3 access errors  
Ensure your IAM identity has appropriate S3 read permissions for the source bucket and objects.

Schema inference errors  
When using `--if-not-exists`, ensure your data file has consistent column types. Mixed types in a column may cause schema inference to fail.

Duplicate key errors on resume  
If you encounter duplicate key errors when resuming a load, add unique constraints to your target table so the loader can use `ON CONFLICT DO NOTHING` to skip already-loaded records.

For additional troubleshooting information, see the [Aurora DSQL Loader GitHub repository](https://github.com/aws-samples/aurora-dsql-loader).

## Migration pathways
<a name="loading-data-migrations"></a>

The following sections describe how to migrate data from common source systems into Aurora DSQL.

### Migrating from PostgreSQL
<a name="loading-data-from-postgresql"></a>

To migrate data from an existing PostgreSQL database to Aurora DSQL:

1. Export your data from PostgreSQL to CSV or Parquet format. You can use the PostgreSQL `COPY` command to export each table:

   ```
   COPY {{my_table}} TO '{{/path/to/my_table.csv}}' WITH (FORMAT csv, HEADER true);
   ```

1. Create the target table in Aurora DSQL. You can either create the schema manually or use the loader's `--if-not-exists` flag to infer the schema from your data.

1. Load the exported data using the Aurora DSQL Loader:

   ```
   aurora-dsql-loader load \
     --endpoint {{cluster-id}}.dsql.{{region}}.on.aws \
     --source-uri {{/path/to/my_table.csv}} \
     --table {{my_table}}
   ```

**Tip**  
For large migrations, consider exporting to Parquet format for better compression and faster loading. Tools like DuckDB can convert CSV files to Parquet efficiently.

### Migrating from MySQL
<a name="loading-data-from-mysql"></a>

To migrate data from MySQL to Aurora DSQL:

1. Export your data from MySQL to CSV format using `SELECT INTO OUTFILE` or a tool like **mysqldump** with the `--tab` option:

   ```
   SELECT * FROM {{my_table}}
   INTO OUTFILE '{{/path/to/my_table.csv}}'
   FIELDS TERMINATED BY ','
   ENCLOSED BY '"'
   LINES TERMINATED BY '\n';
   ```

1. Create the target table in Aurora DSQL with appropriate PostgreSQL-compatible data types.

1. Load the exported data using the Aurora DSQL Loader:

   ```
   aurora-dsql-loader load \
     --endpoint {{cluster-id}}.dsql.{{region}}.on.aws \
     --source-uri {{/path/to/my_table.csv}} \
     --table {{my_table}}
   ```

**Note**  
MySQL and PostgreSQL have different data type systems. Review your schema and adjust data types as needed when creating tables in Aurora DSQL.

### Loading from Amazon S3
<a name="loading-data-from-s3"></a>

If your data is already in Amazon S3, you can load it directly without downloading to your local system. The Aurora DSQL Loader supports S3 URIs natively:

```
aurora-dsql-loader load \
  --endpoint {{cluster-id}}.dsql.{{region}}.on.aws \
  --source-uri s3://{{my-bucket}}/{{path/to/data.parquet}} \
  --table {{my_table}}
```

Ensure your IAM identity has `s3:GetObject` permission on the source objects.

## Using PostgreSQL \\copy
<a name="loading-data-copy"></a>

If you are already connected to Aurora DSQL through a `psql` session that handles IAM authentication, you can use the client-side `\copy` meta-command to load data from your local file system. Unlike the server-side `COPY` statement, `\copy` reads the file on the client machine and streams the data over the existing connection, so no server-side file access is required. This approach works well for simple, single-threaded loads.

**Example Loading a CSV file with \\copy**  

```
\copy {{my_table}} FROM '{{/path/to/data.csv}}' WITH (FORMAT csv, HEADER true);
```

When using `\copy` directly, you are responsible for:
+ Managing parallelization if loading multiple files or large datasets
+ Handling connection management and authentication token refresh
+ Implementing retry logic for failed operations

### Best practices for INSERT transactions
<a name="aurora-dsql-insert-best-practices"></a>

When using `INSERT` statements to load data into Aurora DSQL, follow these practices to improve throughput and reliability:
+ **Batch rows into multi-row INSERTs** – Group multiple rows into a single `INSERT` statement to reduce round trips. For example, `INSERT INTO my_table VALUES (1, 'a'), (2, 'b'), (3, 'c')` is more efficient than three separate statements.
+ **Use parameterized queries** – Use prepared statements with parameter binding instead of string concatenation. This avoids SQL injection risks and allows the database to reuse query plans.
+ **Keep transactions small** – Aurora DSQL uses optimistic concurrency control, so large transactions that touch many rows are more likely to encounter conflicts. Aim for transactions of a few hundred rows rather than thousands.
+ **Implement retry logic** – Transient errors such as optimistic concurrency control (OCC) conflicts are expected in a distributed system. Implement exponential backoff with retry for failed transactions.
+ **Parallelize across connections** – Open multiple connections and distribute inserts across them. Each connection can process a different subset of data concurrently.

For most use cases, the Aurora DSQL Loader provides a simpler and more robust approach to data loading.

## Additional resources
<a name="loading-data-more-info"></a>
+ [Aurora DSQL Loader on GitHub](https://github.com/aws-samples/aurora-dsql-loader) – Source code, documentation, and issue tracking
+ [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md) – Learn about IAM authentication tokens for Aurora DSQL
+ [Accessing Aurora DSQL with PostgreSQL-compatible clients ](accessing.md) – Connect to Aurora DSQL using various clients and tools