

# Limitations

The following limitations apply to foreign tables. For supported engine versions, instance classes, and Regions, see [Querying Apache Iceberg and Parquet data directly in Aurora PostgreSQL](query-iceberg-and-parquet-data.md).

**Topics**
+ [Data modification](#aurora-analytics-limitations-data-modification)
+ [Data format and schema](#aurora-analytics-limitations-data-format)
+ [Query execution](#aurora-analytics-limitations-query-execution)
+ [Lake Formation access control](#aurora-analytics-limitations-access-control)
+ [Infrastructure](#aurora-analytics-limitations-infrastructure)

## Data modification
<a name="aurora-analytics-limitations-data-modification"></a>
+ **Read-only access**: These foreign tables are read-only. `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, and `COPY FROM` operations on foreign tables are not supported. To modify your data, update the source files in Amazon S3 (for Parquet) or update your Iceberg table through AWS Glue or other tools.
+ **Row locking has no effect**: You can include the `FOR UPDATE`, `FOR NO KEY UPDATE`, `FOR SHARE`, and `FOR KEY SHARE` locking clauses in a query, and the query runs and returns rows. This is standard PostgreSQL foreign data wrapper behavior, not specific to this feature.

## Data format and schema
<a name="aurora-analytics-limitations-data-format"></a>
+ **Amazon S3 Multi-Region Access Points not supported**: A foreign table location can be an `s3://` URI, an AWS Glue Data Catalog ARN, or an Amazon S3 Tables ARN. Amazon S3 Multi-Region Access Point (MRAP) ARNs and hostnames are not supported as a foreign table location.
+ **Amazon Redshift federated catalogs not supported**: Foreign tables cannot read Amazon Redshift-native tables exposed through an Amazon Redshift federated catalog in the AWS Glue Data Catalog. This applies even when "Access this catalog from Apache Iceberg compatible engines" is enabled. These tables are not stored as Iceberg or Parquet files in Amazon S3, so foreign tables cannot read them. AWS Glue Data Catalog federation is supported only for Iceberg REST Catalog (IRC)-compatible catalogs whose underlying data is Iceberg data in Amazon S3. To query Amazon Redshift data from Aurora PostgreSQL, expose it as an Amazon S3-backed Iceberg or Parquet dataset.
+ **Data type limitations**: Some PostgreSQL data types do not have a supported mapping. `JSONB`, `SERIAL`, array types, network types, range types, geometric types, and `XML` are not supported. For more information, see [Data formats and type mapping](aurora-analytics-type-mapping.md).
+ **Column name length limit**: Column names inferred from Parquet or Iceberg metadata cannot exceed 63 characters (the PostgreSQL `NAMEDATALEN` limit).
+ **Case-insensitive column name collisions**: A foreign table cannot contain two columns whose names differ only in ASCII letter case (for example, `"Foo"` and `"foo"`). If the underlying data contains such columns, rename them in the source data.
+ **Collation restrictions**: Only `C` and `ICU` collations are supported on foreign table column definitions. libc collations (such as `en_US`) and custom collations are not supported on foreign table columns. You can use libc collations at the expression level in queries, but this might reduce pushdown optimization.

## Query execution
<a name="aurora-analytics-limitations-query-execution"></a>
+ **Single-Region data access per query**: You cannot access data from multiple AWS Regions within a single query. All Amazon S3 data accessed in a query must reside in the same Region.
+ **System columns not accessible**: Aurora PostgreSQL does not support PostgreSQL system columns (`ctid`, `xmin`, `xmax`, `cmin`, `cmax`, and `tableoid`) on foreign tables. Referencing one returns the error `[Aurora Analytics] system column is not supported`.
+ **`security_barrier` views not supported**: The `security_barrier` option of `CREATE VIEW` has no effect on queries on foreign tables. A view over a foreign table still limits which columns and rows a database role can query when you grant `SELECT` on the view instead of the foreign table.

## Lake Formation access control
<a name="aurora-analytics-limitations-access-control"></a>
+ **Lake Formation fine-grained access control not supported**: You can't use AWS Lake Formation fine-grained access control with Aurora PostgreSQL foreign tables. If the AWS Identity and Access Management (IAM) role that Aurora PostgreSQL uses to read your data has a Lake Formation permission that limits it to some columns or rows of a table, Aurora PostgreSQL can't read that table. This includes column-level, row-level, and cell-level security (Lake Formation data filters), whether the permission names specific columns, excludes columns, or uses a row filter expression. A Lake Formation `SELECT` permission on the whole table, with all columns and no data filter, is supported.

  This applies to foreign tables whose `location` is an AWS Glue Data Catalog ARN. For `s3://` and Amazon S3 Tables ARN locations, Lake Formation permissions aren't checked. Access is governed by the IAM role's Amazon S3 or Amazon S3 Tables permissions.

  For a table with a data filter, queries on the foreign table return the following error. `IMPORT FOREIGN SCHEMA`, and `CREATE FOREIGN TABLE` when it reads the table definition from the Data Catalog (that is, when you omit `format` or the column list), return the same error.

  ```
  ERROR:  [Aurora Analytics] Access to table "arn:aws:glue:us-east-1:111122223333:table/{{my_database}}/{{my_table}}" is restricted by a Lake Formation data filter, which is currently not supported with Aurora Analytics.
  ```

  Aurora PostgreSQL checks the role's Lake Formation permission each time it reads the table. If you add a data filter to the role's permission after you create a foreign table, queries on that foreign table return the same error.

  Because `IMPORT FOREIGN SCHEMA` runs in a single transaction, it imports no tables if any table in the source database has a data filter for the role. To import the other tables, exclude the filtered tables with `EXCEPT`, or list the tables to import with `LIMIT TO`. For more information, see [Bulk table creation (IMPORT FOREIGN SCHEMA)](aurora-analytics-foreign-tables.md#aurora-analytics-foreign-tables-import).

  To restrict which columns or rows users can see, use one of the following approaches:
  + Create a separate Iceberg table that contains only the permitted columns and rows, grant the role Lake Formation `SELECT` on that whole table, and create the foreign table on it.
  + Grant the role access to the whole table, and restrict access in Aurora PostgreSQL with PostgreSQL privileges. For more information, see [Restricting access to columns and rows](aurora-analytics-foreign-tables.md#aurora-analytics-foreign-tables-permissions-restrict).
+ **IAM role needs Amazon S3 access to the data**: Aurora PostgreSQL currently reads data in Amazon S3 with the permissions of the IAM role associated with your DB cluster, including for Lake Formation-governed tables. Lake Formation doesn't provide temporary credentials to Aurora PostgreSQL. Grant the role `s3:GetObject` on the data location. Without it, queries on a Lake Formation-governed table fail with an Amazon S3 `AccessDenied` error, even when the role has Lake Formation `SELECT` on the table.

## Infrastructure
<a name="aurora-analytics-limitations-infrastructure"></a>
+ **Cache not persistent across restarts**: The on-disk read cache is cleared when a DB instance restarts or fails over. Subsequent queries re-fetch data from Amazon S3.
+ **Serverless scaling considerations**: With Aurora Serverless v2 deployments, running multiple resource-intensive analytical queries concurrently might exceed the rate at which the DB instance can scale up.