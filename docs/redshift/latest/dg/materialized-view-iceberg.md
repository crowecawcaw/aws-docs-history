

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Materialized views stored as Apache Iceberg tables
<a name="materialized-view-iceberg"></a>

You can create materialized views that store their data as Apache Iceberg tables in Amazon S3 or Amazon S3 Table Buckets. Unlike standard Amazon Redshift materialized views, which store data internally in Redshift Managed Storage (RMS), Iceberg materialized views are stored as standard Iceberg tables and are accessible to any analytics engine that supports the Iceberg format, including Apache Spark, Amazon Athena, and Trino.

Iceberg materialized views combine Amazon Redshift's query optimization and incremental refresh capabilities with Iceberg's open table format. You can create, refresh, and drop Iceberg materialized views using the same SQL commands as standard materialized views, with the addition of the `USING ICEBERG` clause during creation.

Iceberg materialized views are supported on Redshift Serverless and provisioned clusters with RG instance types. RA3 and DC2 instance types are not supported.

For information about SQL commands used to create and manage Iceberg materialized views, see the following command topics:
+ [CREATE MATERIALIZED VIEW](materialized-view-create-sql-command.md)
+ [REFRESH MATERIALIZED VIEW](materialized-view-refresh-sql-command.md)
+ [DROP MATERIALIZED VIEW](materialized-view-drop-sql-command.md)

## How Iceberg materialized views work
<a name="materialized-view-iceberg-how-it-works"></a>

When you create an Iceberg materialized view, Amazon Redshift does the following:

1. Executes the defining query and writes the results as Parquet data files in Amazon S3.

1. Registers the table in the AWS Glue Data Catalog with Iceberg metadata, making it discoverable by other engines.

1. Stores the materialized view definition and refresh state in AWS Glue for cluster-independent management.

When you refresh an Iceberg materialized view, Amazon Redshift compares the current source table Iceberg snapshots against the snapshots recorded at the last refresh. If changes are detected, Amazon Redshift either computes and applies only the changed data (incremental refresh) or performs a full recomputation.

## Source table requirements
<a name="materialized-view-iceberg-source-requirements"></a>

Source tables for Iceberg materialized views must meet the following requirements:
+ Must be in Apache Iceberg format. Non-Iceberg tables (Amazon Redshift native tables, Hive or Parquet external tables) are not supported as source tables.
+ Must be in the same AWS Region and account as the materialized view.
+ Can be referenced using three-part notation (`awsdatacatalog.{{database}}.{{table}}`), Amazon S3 Tables notation (`"{{bucket}}@s3tablescatalog".{{database}}.{{table}}`), or two-part notation via an external schema (`{{external_schema}}.{{table}}`).

## Cross-engine interoperability
<a name="materialized-view-iceberg-interoperability"></a>

Iceberg materialized views created by Amazon Redshift appear as standard Iceberg tables in the AWS Glue Data Catalog. Other analytics engines can read them using standard Iceberg table access patterns without any additional configuration.

The following restrictions apply:
+ Only Amazon Redshift can refresh or drop materialized views that were created by Amazon Redshift.
+ Iceberg materialized views created by other engines (such as Apache Spark) can be queried by Amazon Redshift as read-only tables but cannot be refreshed or dropped by Amazon Redshift.

## Incremental refresh
<a name="materialized-view-iceberg-incremental-refresh"></a>

Amazon Redshift performs incremental refresh when the materialized view definition supports it. Incremental refresh reads only the data that changed in source tables since the last refresh and applies those changes to the materialized view.

Incremental refresh is supported for materialized views that use:
+ `SELECT ... FROM ... WHERE ... GROUP BY` with COUNT and SUM aggregate functions
+ Inner joins between Iceberg source tables
+ UNION ALL

Amazon Redshift automatically falls back to full refresh when:
+ The materialized view uses SQL constructs not supported for incremental refresh. For more information, see the Limitations section that follows and [Refreshing a materialized view](materialized-view-refresh.md).
+ Source table snapshots from the last refresh have expired.
+ The materialized view data was modified outside of a Amazon Redshift refresh operation.

## Concurrent refresh
<a name="materialized-view-iceberg-concurrent-refresh"></a>

Multiple Amazon Redshift clusters or workgroups can attempt to refresh the same Iceberg materialized view concurrently. Amazon Redshift uses optimistic concurrency control (OCC) through the AWS Glue Data Catalog's conditional update mechanism to ensure that only one refresh succeeds. If a concurrent refresh is detected, Amazon Redshift checks whether the materialized view is still stale. If another cluster has already completed the refresh, the operation returns success without redoing work.

## Compaction and table maintenance
<a name="materialized-view-iceberg-compaction"></a>

For Iceberg materialized views stored in Amazon S3 Table Buckets, Amazon S3 Tables automatically manages compaction and data file optimization. No user action is required.

For materialized views stored in general-purpose Amazon S3 buckets (specified via the `LOCATION` parameter), Amazon Redshift doesn't perform compaction. Over time, incremental refresh produces many small data files that can degrade read performance. To maintain read performance, use the following recommended practices:
+ Run compaction regularly using an external tool such as Apache Spark's `rewrite_data_files` procedure.
+ Configure Iceberg snapshot expiration to limit storage growth from historical snapshots.
+ Amazon Redshift recognizes compaction operations as maintenance activities and doesn't fall back to full refresh when compaction has occurred.

For source tables, configure snapshot retention to exceed your expected refresh interval. When source table snapshots expire before the next refresh, Amazon Redshift can no longer compute an incremental delta and falls back to full refresh.

## Security considerations
<a name="materialized-view-iceberg-security"></a>

### Permissions
<a name="materialized-view-iceberg-permissions"></a>

The following permissions are required:
+ **CREATE** – The caller needs CREATE TABLE permission in the target AWS Glue database. The IAM role associated with the external schema (the MV definer role) must have SELECT permission via AWS Lake Formation on all source tables.
+ **REFRESH** – The caller needs ALTER permission on the materialized view. The MV definer role (recorded at create time) must have SELECT permission on all source tables.
+ **DROP** – The caller needs DROP permission on the materialized view.
+ **QUERY** – The caller needs SELECT permission on the materialized view, granted via AWS Lake Formation or AWS Glue resource policies.

For information about creating IAM roles for Amazon Redshift and granting AWS Lake Formation permissions, see [Getting started with Amazon Redshift Spectrum](c-getting-started-using-spectrum.md). To verify that the IAM role has the required permissions on source tables, use the AWS Lake Formation console or the `GetEffectivePermissionsForPath` API. To verify that the target AWS Glue database exists and the role has access, use the `GetDatabase` API.

The following example verifies that the IAM role has SELECT permission on a source table via AWS Lake Formation:

```
aws lakeformation list-permissions \
    --principal DataLakePrincipalIdentifier=arn:aws:iam::123456789012:role/myspectrum_role \
    --resource '{"Table":{"DatabaseName":"mydb","Name":"orders"}}'
```

The following example verifies that the target AWS Glue database exists and is accessible:

```
aws glue get-database --name mydb
```

### Snapshot history visibility
<a name="materialized-view-iceberg-snapshot-visibility"></a>

Iceberg materialized views store data as standard Iceberg tables with full snapshot history. A reader with access to the underlying Iceberg files can compare successive snapshots to observe which rows were added or removed between refreshes.

For aggregated materialized views (those with GROUP BY and aggregate functions), the visible delta is limited to changes in aggregate values, not individual source table rows. For non-aggregated materialized views, the delta corresponds to the specific rows that changed in the materialized view output.

This behavior is inherent to the Iceberg table format. Any Iceberg table that undergoes incremental writes exposes the same property.

To mitigate this behavior:
+ Use AWS Lake Formation permissions or Amazon S3 bucket policies to control who can access the materialized view's underlying Iceberg data files.
+ For materialized views containing sensitive data where change history should not be observable, define the materialized view with SQL constructs that force full refresh (such as DISTINCT). Full refresh replaces all data in each snapshot, making it infeasible to determine which specific rows changed.
+ Configure Iceberg snapshot expiration to limit the window of observable changes. With Amazon S3 Table Buckets, managed maintenance handles snapshot lifecycle automatically.
+ Use Amazon S3 Table Buckets, which provide integrated table-level access control.

## Monitoring
<a name="materialized-view-iceberg-monitoring"></a>

### Refresh history
<a name="materialized-view-iceberg-refresh-history"></a>

Refresh operations performed by the local cluster are logged to [SVL\_MV\_REFRESH\_STATUS](r_SVL_MV_REFRESH_STATUS.md). Query this view to check refresh timing, status, and whether refresh was incremental or full.

```
SELECT mv_name, starttime, endtime, status
FROM svl_mv_refresh_status
WHERE mv_name = 'daily_revenue'
ORDER BY starttime DESC
LIMIT 10;
```

Note that this system view only records refreshes performed by the local cluster. If multiple clusters refresh the same Iceberg materialized view, each cluster's system tables show only its own refresh history.

### Discovering Iceberg materialized views
<a name="materialized-view-iceberg-discovering"></a>

Use [SVV\_EXTERNAL\_TABLES](r_SVV_EXTERNAL_TABLES.md) to find Iceberg materialized views in your external schemas:

```
SELECT schemaname, tablename, location
FROM svv_external_tables
WHERE tabletype = 'MATERIALIZED VIEW';
```

[STV\_MV\_INFO](r_STV_MV_INFO.md) doesn't include Iceberg materialized views.

## Limitations
<a name="materialized-view-iceberg-limitations"></a>

You can't define an Iceberg materialized view that references or includes any of the following:
+ Non-Iceberg source tables (Amazon Redshift native tables, Hive, Parquet, Delta Lake, or Hudi external tables)
+ Source tables using Iceberg format version 3
+ User-defined functions (UDFs) or user-defined aggregates
+ Mutable functions (GETDATE, RANDOM, CURRENT\_TIMESTAMP, and similar functions)
+ ORDER BY, LIMIT, or OFFSET clauses
+ Uppercase identifiers in table names, column names, or aliases
+ Source tables in a different AWS Region or account
+ AWS Lake Formation filtered (fine-grained access control) tables

The following SQL constructs are allowed in the materialized view definition but force full refresh instead of incremental refresh:
+ DISTINCT
+ Outer joins (LEFT, RIGHT, FULL)
+ Window functions
+ Subqueries
+ Set operations other than UNION ALL (INTERSECT, EXCEPT)
+ GROUPING SETS, ROLLUP, CUBE
+ Aggregate functions other than COUNT and SUM
+ COUNT(DISTINCT), SUM(DISTINCT)

Additional limitations:
+ Automatic query rewriting to use materialized views is not supported for Iceberg materialized views.
+ Automated materialized views are not supported for Iceberg materialized views.
+ Iceberg materialized views are supported only on Redshift Serverless and provisioned clusters with RG instance types. RA3 and DC2 instance types are not supported.
+ Fine-grained access control (FGAC) is not supported on Iceberg materialized views.
+ CASCADE refresh is not supported for Iceberg materialized views.
+ Iceberg materialized views cannot be created or refreshed when `enable_case_sensitive_identifier` is set to `true`.