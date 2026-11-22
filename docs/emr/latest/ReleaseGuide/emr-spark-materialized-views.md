

# Using materialized views with Amazon EMR

Amazon EMR release 7.12.0 and later supports creating and managing Apache Iceberg materialized views in the AWS Glue Data Catalog. A materialized view is a managed table that stores the precomputed result of a SQL query in Apache Iceberg format and incrementally updates as the underlying source tables change. You can use materialized views to simplify data transformation pipelines and accelerate query performance for complex analytical workloads.

When you create a materialized view using Spark on Amazon EMR, the view definition and metadata are stored in the AWS Glue Data Catalog. The precomputed results are stored as Apache Iceberg tables in Amazon S3 Tables buckets or Amazon S3 general purpose buckets within your AWS account. The AWS Glue Data Catalog automatically monitors source tables and refreshes materialized views using managed compute infrastructure.

With Amazon EMR release 8.2.0, you can use incremental refresh on materialized views that project, filter, or inner-join data, not only those that aggregate. You can change a materialized view's definition in place with `CREATE OR REPLACE MATERIALIZED VIEW`, without dropping and recreating it. You can also create materialized views on source tables governed by AWS Lake Formation fine-grained access control (FGAC). Finally, you can route Spark Declarative Pipelines to Iceberg materialized views for incremental refresh. The sections that follow describe these capabilities.

**Topics**
+ [How materialized views work with Amazon EMR](#emr-spark-materialized-views-how-it-works)
+ [Prerequisites](#emr-spark-materialized-views-prerequisites)
+ [Configuring Spark to use materialized views](#emr-spark-materialized-views-configure)
+ [Creating materialized views](#emr-spark-materialized-views-create)
+ [Querying materialized views](#emr-spark-materialized-views-query)
+ [Refreshing materialized views](#emr-spark-materialized-views-refresh)
+ [Changing a materialized view definition](#emr-spark-materialized-views-change-definition)
+ [Materialized views on AWS Lake Formation fine-grained access control source tables](#emr-spark-materialized-views-fgac)
+ [Materialized views in Spark Declarative Pipelines](#emr-spark-materialized-views-sdp)
+ [Managing materialized views](#emr-spark-materialized-views-manage)
+ [Permissions for materialized views](#emr-spark-materialized-views-permissions)
+ [Monitoring materialized view operations](#emr-spark-materialized-views-monitoring)
+ [Example: Complete workflow](#emr-spark-materialized-views-example)
+ [System-managed materialized views](#emr-spark-materialized-views-system-managed)
+ [Considerations and limitations](#emr-spark-materialized-views-limitations)

## How materialized views work with Amazon EMR
<a name="emr-spark-materialized-views-how-it-works"></a>

Materialized views integrate with Amazon EMR through Apache Spark's Iceberg support. When you configure your Spark session to use the AWS Glue Data Catalog, you can create materialized views using standard SQL syntax. The Spark optimizer can automatically rewrite queries to use materialized views when they provide better performance, eliminating the need to manually modify application code.

The AWS Glue Data Catalog handles all operational aspects of materialized view maintenance, including:
+ Detecting changes in source tables. For Apache Iceberg source tables, change detection uses Apache Iceberg's metadata layer. For Apache Hive (non-Iceberg) source tables, change detection compares the ETags of the source data files against those recorded at the last refresh.
+ Scheduling and executing refresh operations using managed Spark compute
+ Determining whether to perform full or incremental refresh based on the data changes
+ Storing precomputed results in Apache Iceberg format for multi-engine access

You can query materialized views from Amazon EMR using the same Spark SQL interfaces you use for regular tables. The precomputed data is also accessible from other services including Amazon Athena and Amazon Redshift.

With Amazon EMR release 8.2.0, incremental refresh keeps a materialized view current by merging only the rows that changed since the last refresh. It applies to views that aggregate (`SUM`, `COUNT`) and to views that project, filter, or inner-join data. Non-aggregate views are maintained using Apache Iceberg format version 3 row lineage, which traces every materialized view row back to the source row that produced it and is stable across compaction. When a materialized view or a change doesn't qualify for incremental refresh, Amazon EMR performs a full refresh instead, so the result is always correct.

## Prerequisites
<a name="emr-spark-materialized-views-prerequisites"></a>

To use materialized views with Amazon EMR, you need:
+ An AWS account
+ An Amazon EMR cluster running release 7.12.0 or later. Incremental refresh of non-aggregate materialized views, `CREATE OR REPLACE MATERIALIZED VIEW`, Lake Formation fine-grained access control source tables, and Spark Declarative Pipelines routing require Amazon EMR release 8.2.0 or later.
+ Source tables registered in the AWS Glue Data Catalog. Apache Iceberg source tables are supported on Amazon EMR release 7.12.0 and later. Apache Hive (non-Iceberg) source tables with a PARQUET, ORC, CSV, or JSON provider are supported on Amazon EMR release 7.14.0 and later. Incremental refresh of non-aggregate materialized views requires Apache Iceberg format version 3 source tables.
+ AWS Lake Formation permissions configured for source tables and target databases
+ An S3 Tables bucket or S3 general purpose bucket registered with AWS Lake Formation for storing materialized view data

## Configuring Spark to use materialized views
<a name="emr-spark-materialized-views-configure"></a>

To create and manage materialized views, configure your Spark session with the required Iceberg extensions and catalog settings. The configuration varies depending on whether your source tables and materialized views use S3 Tables buckets or S3 general purpose buckets.

### Configuring for S3 Tables
<a name="emr-spark-materialized-views-configure-s3-tables"></a>

When using S3 Tables buckets for materialized views, configure separate catalog references for your source tables and materialized views:

```
spark-sql \
  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
  --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.glue_catalog.type=glue \
  --conf spark.sql.catalog.glue_catalog.warehouse=s3://amzn-s3-demo-bucket/warehouse \
  --conf spark.sql.catalog.glue_catalog.glue.region=us-east-1 \
  --conf spark.sql.catalog.glue_catalog.glue.id=111122223333 \
  --conf spark.sql.catalog.glue_catalog.glue.account-id=111122223333 \
  --conf spark.sql.catalog.glue_catalog.glue.lakeformation-enabled=true \
  --conf spark.sql.catalog.s3t_catalog=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.s3t_catalog.type=glue \
  --conf spark.sql.catalog.s3t_catalog.glue.id=111122223333:s3tablescatalog/my-table-bucket \
  --conf spark.sql.catalog.s3t_catalog.glue.account-id=111122223333 \
  --conf spark.sql.catalog.s3t_catalog.glue.lakeformation-enabled=true \
  --conf spark.sql.catalog.s3t_catalog.warehouse=s3://amzn-s3-demo-bucket/mv-warehouse \
  --conf spark.sql.catalog.s3t_catalog.glue.region=us-east-1 \
  --conf spark.sql.defaultCatalog=s3t_catalog \
  // turn on automatic query rewrite (optional)
  --conf spark.sql.optimizer.answerQueriesWithMVs.enabled=true
```

### Configuring for S3 general purpose buckets
<a name="emr-spark-materialized-views-configure-s3-general"></a>

When using S3 general purpose buckets, configure a single catalog reference:

```
spark-sql \
  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
  --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.glue_catalog.type=glue \
  --conf spark.sql.catalog.glue_catalog.warehouse=s3://amzn-s3-demo-bucket/warehouse \
  --conf spark.sql.catalog.glue_catalog.glue.region=us-east-1 \
  --conf spark.sql.catalog.glue_catalog.glue.id=111122223333 \
  --conf spark.sql.catalog.s3t_catalog.glue.account-id=111122223333 \
  --conf spark.sql.catalog.s3t_catalog.glue.lakeformation-enabled=true \
  --conf spark.sql.defaultCatalog=glue_catalog \
  // turn on automatic query rewrite (optional)
  --conf spark.sql.optimizer.answerQueriesWithMVs.enabled=true
```

### Enabling incremental refresh
<a name="emr-spark-materialized-views-configure-incremental"></a>

To enable incremental refresh optimization, add the following configuration properties to your Spark session:

```
spark-sql \
  --conf spark.sql.optimizer.incrementalMVRefresh.enabled=true \
```

On Amazon EMR release 8.2.0 and later, incremental refresh covers aggregate and non-aggregate materialized views by default. To restrict incremental refresh to aggregate materialized views only, add `--conf spark.sql.optimizer.incrementalMVRefresh.nonAggregate.enabled=false`.

### Configuration parameters
<a name="emr-spark-materialized-views-configure-parameters"></a>

The following configuration parameters control materialized view behavior:
+ `spark.sql.extensions` – Enables Iceberg Spark session extensions required for materialized view support.
+ `spark.sql.optimizer.answerQueriesWithMVs.enabled` – Enables automatic query rewrite to use materialized views. Set to true to activate this optimization.
+ `spark.sql.optimizer.incrementalMVRefresh.enabled` – Enables incremental refresh optimization. Set to true to process only changed data during refresh operations.
+ `spark.sql.optimizer.incrementalMVRefresh.nonAggregate.enabled` – Default `true`. You can use incremental refresh for materialized views with no aggregation (projection, filter, inner join). Set to `false` to use incremental refresh for aggregate materialized views only. This parameter takes effect only when `spark.sql.optimizer.incrementalMVRefresh.enabled` is `true`. Available on Amazon EMR release 8.2.0 and later.
+ `spark.sql.materializedView.v1SourceTables.enabled` – Allows Apache Hive (non-Iceberg) tables with a PARQUET, ORC, CSV, or JSON provider in the AWS Glue Data Catalog to be used as source tables for a materialized view. Set to true to create materialized views over Hive source tables. Available on Amazon EMR release 7.14.0 and later.
+ `spark.sql.materializedView.v1ETagVersioning.enabled` – Set to true to detect changes in Apache Hive (non-Iceberg) source tables by comparing the ETags of the source data files. This is required to refresh a materialized view that references Hive source tables. Available on Amazon EMR release 7.14.0 and later.

## Creating materialized views
<a name="emr-spark-materialized-views-create"></a>

You create materialized views using the CREATE MATERIALIZED VIEW SQL statement. The view definition specifies the transformation logic as a SQL query that references one or more source tables.

### DLLs
<a name="emr-spark-materialized-views-create-dlls"></a>

**Create View**

```
{ CREATE OR REPLACE MATERIALIZED VIEW | CREATE MATERIALIZED VIEW [ IF NOT EXISTS ] }
   view_identifier
  [ view_clauses ]
  [ schedule_clauses ]
  AS [ select_statement ]

view_clauses =
  { [ LOCATION location ] |
    [ PARTITIONED BY (col [, ...]) ] |
    [ COMMENT view_comment ] |
    [ SCHEDULE [ REFRESH ] schedule_clause ] }

schedule_clause =
  { EVERY number { HOUR | HOURS | DAY | DAYS | WEEK | WEEKS } }
```

**Note**  
The view\_clauses must appear before the select\_statement.

### Creating a basic materialized view
<a name="emr-spark-materialized-views-create-basic"></a>

The following example creates a materialized view that aggregates order data by customer, use fully qualified table names with three part naming convention in view definition:

```
CREATE MATERIALIZED VIEW customer_orders
AS 
SELECT 
    customer_name, 
    COUNT(*) as order_count, 
    SUM(amount) as total_amount 
FROM glue_catalog.sales.orders
GROUP BY customer_name;
```

### Creating a non-aggregate materialized view
<a name="emr-spark-materialized-views-create-non-aggregate"></a>

Starting with Amazon EMR release 8.2.0, incremental refresh covers materialized views that project, filter, and inner-join data, not only those that aggregate. You can build a transformation stage that cleans and conforms raw data into a derived table as a materialized view, so each refresh merges only the rows that changed instead of recomputing the whole table.

Incremental refresh of a non-aggregate materialized view relies on row lineage in the source tables, so the source tables must already use Apache Iceberg format version 3. Setting format version 3 on the materialized view alone isn't enough. The following example creates a non-aggregate materialized view over two Iceberg format version 3 source tables and also creates the materialized view with format version 3. In the example, replace `completed_orders`, `glue_catalog.sales.orders`, and `glue_catalog.sales.customers` with the names of your own materialized view and source tables.

```
CREATE MATERIALIZED VIEW completed_orders
TBLPROPERTIES ('format-version'='3')
AS
SELECT o.order_id, o.customer_name, c.region, o.amount
FROM glue_catalog.sales.orders o
JOIN glue_catalog.sales.customers c ON o.customer_id = c.customer_id
WHERE o.status = 'complete';
```

Incremental refresh of non-aggregate materialized views tracks individual rows using Iceberg format version 3 row lineage. Every materialized view row traces back to the source row that produced it. The lineage is stable across compaction. For an inner join, Amazon EMR tracks lineage from all base tables. Deleting any contributing source row removes the corresponding materialized view row.

Non-aggregate materialized views have the following limitations:
+ Incremental refresh of non-aggregate materialized views requires Apache Iceberg format version 3 source tables for row lineage. On format version 2 source tables, only aggregate materialized views (`SUM` or `COUNT`) refresh incrementally. Non-aggregate materialized views refresh in full.
+ Joins are incremental for inner joins without join hints only, and only when the change lands on one side of the join. If more than one source table changed since the last refresh, the refresh falls back to full.
+ A materialized view that combines a join with an aggregation (a join feeding a `GROUP BY`) refreshes in full. The engine maintains a join alone or an aggregation alone incrementally, but not the two stacked.
+ Outer, cross, semi, and anti joins; `UNION`; subqueries (including `IN (SELECT ...)`); `DISTINCT`; window functions; and `LIMIT` or `ORDER BY` always refresh in full.
+ The `spark.sql.optimizer.incrementalMVRefresh.nonAggregate.enabled` parameter (default `true`) controls incremental refresh for non-aggregate materialized views. This parameter takes effect only when `spark.sql.optimizer.incrementalMVRefresh.enabled` is `true`.

### Creating a materialized view with automatic refresh
<a name="emr-spark-materialized-views-create-auto-refresh"></a>

To configure automatic refresh, specify a refresh schedule when creating the view using fully qualified table names with three part naming convention in view definition:

```
CREATE MATERIALIZED VIEW customer_orders
SCHEDULE REFRESH EVERY 1 HOUR
AS 
SELECT 
    customer_name, 
    COUNT(*) as order_count, 
    SUM(amount) as total_amount 
FROM glue_catalog.sales.orders
GROUP BY customer_name;
```

### Creating a materialized view with cross-catalog references
<a name="emr-spark-materialized-views-create-cross-catalog"></a>

When your source tables are in a different catalog than your materialized view, use fully qualified table names with three-part naming convention in both view name and view definition:

```
CREATE MATERIALIZED VIEW s3t_catalog.analytics.customer_summary
AS
SELECT
    customer_name,
    COUNT(*) as order_count,
    SUM(amount) as total_amount
FROM glue_catalog.sales.orders
GROUP BY customer_name;
```

### Creating a materialized view over Apache Hive source tables
<a name="emr-spark-materialized-views-create-hive-sources"></a>

Starting with Amazon EMR release 7.14.0, you can create a materialized view whose source tables are Apache Hive (non-Iceberg) tables, without first migrating those tables to Apache Iceberg. The materialized view itself is still stored as an Apache Iceberg table; only the source tables can be Hive. A single materialized view can reference a mix of Hive and Iceberg source tables.

Hive source tables are supported when the table's provider is PARQUET, ORC, CSV, or JSON (created with `CREATE TABLE ... USING {{format}}`). A table with a `hive` provider (SerDe-based) is not supported, even if it stores Parquet data underneath. To check a table's provider, use `DESCRIBE EXTENDED {{table_name}}`.

To use Hive source tables, set `spark.sql.materializedView.v1SourceTables.enabled` and `spark.sql.materializedView.v1ETagVersioning.enabled` to `true` in your Spark session. For more information, see [Configuration parameters](#emr-spark-materialized-views-configure-parameters).

The following example creates a materialized view over a Hive source table:

```
CREATE MATERIALIZED VIEW s3t_catalog.analytics.customer_summary
AS
SELECT
    customer_name,
    COUNT(*) as order_count,
    SUM(amount) as total_amount
FROM spark_catalog.sales.orders
GROUP BY customer_name;
```

**Note**  
Hive source tables do not expose row-level change history, so incremental refresh is not available for a materialized view that references any Hive source table. Each refresh recomputes the entire materialized view. For more information, see [Refreshing materialized views](#emr-spark-materialized-views-refresh).

## Querying materialized views
<a name="emr-spark-materialized-views-query"></a>

After creating a materialized view, you can query it like any other table using standard SQL SELECT statements:

```
SELECT * FROM customer_orders;
```

### Automatic query rewrite
<a name="emr-spark-materialized-views-query-rewrite"></a>

When automatic query rewrite is enabled, the Spark optimizer analyzes your queries and automatically uses materialized views when they can improve performance. For example, if you execute the following query:

```
SELECT 
    customer_name, 
    COUNT(*) as order_count, 
    SUM(amount) as total_amount 
FROM orders
GROUP BY customer_name;
```

The Spark optimizer automatically rewrites this query to use the customer\_orders materialized view instead of processing the base orders table, provided the materialized view is current.

Starting with Amazon EMR release 8.1.0, automatic query rewrite can also rewrite queries over Apache Hive (non-Iceberg) source tables to use a matching materialized view. If the materialized view is stale, the optimizer does not rewrite the query and instead reads directly from the source tables, so a stale materialized view is never used to answer a query.

Automatic query rewrite isn't available on clusters that enforce AWS Lake Formation fine-grained access control.

### Verifying automatic query rewrite
<a name="emr-spark-materialized-views-query-verify"></a>

To verify whether a query uses automatic query rewrite, use the EXPLAIN EXTENDED command:

```
EXPLAIN EXTENDED
SELECT customer_name, COUNT(*) as order_count, SUM(amount) as total_amount 
FROM orders
GROUP BY customer_name;
```

In the execution plan, look for the materialized view name in the BatchScan operation. If the plan shows BatchScan glue\_catalog.analytics.customer\_orders instead of BatchScan glue\_catalog.sales.orders, the query has been automatically rewritten to use the materialized view.

**Note**  
Automatic query rewrite requires time for the Spark metadata cache to populate after creating a materialized view. This process typically completes within 30 seconds.

## Refreshing materialized views
<a name="emr-spark-materialized-views-refresh"></a>

You can refresh materialized views using two methods: full refresh or incremental refresh. Full refresh recomputes the entire materialized view from all base table data, while incremental refresh processes only the data that has changed since the last refresh. On Amazon EMR release 8.2.0 and later, incremental refresh covers aggregate materialized views (`SUM`, `COUNT`) and non-aggregate materialized views (projection, filter, inner join).

### Manual full refresh
<a name="emr-spark-materialized-views-refresh-full"></a>

To perform a full refresh of a materialized view:

```
REFRESH MATERIALIZED VIEW customer_orders FULL;
```

After executing this command, query the materialized view to verify the updated results:

```
SELECT * FROM customer_orders;
```

### Manual incremental refresh
<a name="emr-spark-materialized-views-refresh-incremental"></a>

To perform an incremental refresh, ensure incremental refresh is enabled in your Spark session configuration, then execute:

```
REFRESH MATERIALIZED VIEW customer_orders;
```

The AWS Glue Data Catalog automatically determines whether incremental refresh is applicable based on the view definition and the amount of changed data. If incremental refresh is not possible, the operation falls back to full refresh. A refresh that falls back to full records a reason in the Spark event log. Examples include too many rows or data files changed, more than one source table changed, an expired source snapshot, or an explicit full-refresh request. For more information, see [Considerations and limitations](#emr-spark-materialized-views-limitations).

### Verifying incremental refresh execution
<a name="emr-spark-materialized-views-refresh-verify"></a>

To confirm that incremental refresh executed successfully, you can check the `lastRefreshType` table properties by running the following commands:

```
SHOW TBLPROPERTIES <mvName>("lastRefreshType")
```

Also, this can also be achieved by enabling debug logging by modifying your Spark log configuration:

1. Open the Spark log4j configuration file:

   ```
   sudo vim /usr/lib/spark/conf/log4j2.properties
   ```

1. Add the following logger configurations:

   ```
   logger.spark.name = org.apache.spark.sql
   logger.spark.level = debug
   
   logger.inmemcache.name = org.apache.spark.sql.InMemMvMetadataCache
   logger.inmemcache.level = off
   ```

1. After executing a refresh operation, search for the following message in the Spark output:

   ```
   DEBUG RefreshMaterializedViewExec: Executed Incremental Refresh
   ```

## Changing a materialized view definition
<a name="emr-spark-materialized-views-change-definition"></a>

Starting with Amazon EMR release 8.2.0, you can change a materialized view's definition in place with `CREATE OR REPLACE MATERIALIZED VIEW`, without dropping it. This updates the SQL and runs a full refresh that recomputes the data from the new definition. The materialized view keeps its name and grants. Readers continue to see the previous results until the recomputed data is written in a single commit, so there is no gap in analytics while the change takes effect. In the following example, replace `customer_orders` with the name of your materialized view.

```
CREATE OR REPLACE MATERIALIZED VIEW customer_orders
AS
SELECT
    customer_name,
    channel,
    COUNT(*) as order_count,
    SUM(amount) as total_amount
FROM glue_catalog.sales.orders
GROUP BY customer_name, channel;
```

Use `CREATE OR REPLACE MATERIALIZED VIEW` to include a column that a source table added, to add a join or change an aggregation, or to re-expand `SELECT *` after a source widened.

Changing a definition has the following limitations:
+ `CREATE OR REPLACE MATERIALIZED VIEW` runs a full refresh. It isn't an incremental operation.
+ A materialized view defined with an explicit column list keeps working with no action when a source adds a column, but it doesn't include the new column until you restate it with `CREATE OR REPLACE MATERIALIZED VIEW`.
+ A source column rename, a type change, or dropping a column that the view references is a breaking change that requires dropping and recreating the view.
+ `OR REPLACE` can't be combined with `IF NOT EXISTS`.
+ Use `ALTER MATERIALIZED VIEW` only for operational changes such as the refresh schedule, not for definition changes.

## Materialized views on AWS Lake Formation fine-grained access control source tables
<a name="emr-spark-materialized-views-fgac"></a>

Starting with Amazon EMR release 8.2.0, on a cluster that enforces AWS Lake Formation fine-grained access control (FGAC), you can create, read, refresh, and drop materialized views directly on governed source tables. The materialized view contains only the rows and columns that you can see when you run CREATE or REFRESH. AWS Lake Formation applies the same row filters and column masks that it applies to a direct read. On an incremental refresh, AWS Lake Formation applies the same row filters and column masks to the change data read as it does to a full read.

The following table lists the operations that fine-grained access control (FGAC) source tables support.


| Operation | Supported | 
| --- | --- | 
| Create, read, full refresh, drop | Yes | 
| Incremental refresh | Aggregate materialized views only (SUM or COUNT, over Iceberg base tables) | 
| Automatic query rewrite | No | 

Materialized views on FGAC source tables have the following limitations:
+ On a cluster that enforces fine-grained access control, non-aggregate materialized views (projections, filters, joins with no `GROUP BY`) always refresh in full. This is a cluster-level behavior. It applies to every non-aggregate materialized view on the cluster, even over source tables that have no row filters or column masks. If you don't use fine-grained access control, run non-aggregate incremental refresh on a non-FGAC cluster to avoid this fallback.
+ The following conditions fall back to a full refresh on a per-table basis:
  + Materialized views over Hive or Parquet base tables always refresh in full.
  + If the fine-grained access control policy of a base table changed since the last refresh, the next refresh is full, under the current policy.
+ You can't create or refresh Apache Iceberg format version 3 materialized views on an FGAC cluster, for the same reason. Create FGAC materialized views with Iceberg format version 2.
+ Incremental refresh is supported for aggregate materialized views only (`SUM` or `COUNT`, over Iceberg base tables) on an FGAC cluster. If the row filters and column masks can't be applied to the change data read, the refresh fails.
+ A materialized view contains only what you can see when you run CREATE or REFRESH. If you run a full refresh, your access policy determines the contents. If a different user runs the full refresh, that user's policy determines the contents instead, so run refreshes as a consistent principal.
+ Permissions on a materialized view are set separately from permissions on its base tables. Grant access on the materialized view directly.
+ Automatic query rewrite is turned off on FGAC clusters.
+ Scheduled (automatic) refresh isn't supported for a materialized view over fine-grained access control source tables. Refresh these materialized views manually with `REFRESH MATERIALIZED VIEW`.

## Materialized views in Spark Declarative Pipelines
<a name="emr-spark-materialized-views-sdp"></a>

In a Spark Declarative Pipeline (SDP), you declare the datasets you want and the SQL that defines each one, and the pipeline resolves the dependency graph and runs it. By default, a materialized view in an SDP pipeline is a plain Iceberg table that the pipeline rebuilds in full on every run.

Starting with Amazon EMR release 8.2.0, you can route an SDP materialized view to a Glue Iceberg materialized view. The declared view is then backed by a materialized view that records its sources and the snapshot it last read. Each pipeline run skips any materialized view whose sources didn't change, and merges only the delta for the ones that did, using the same pipeline code. Set the routing mode in the pipeline spec. The following table lists the routing modes.


| Mode | When Glue can back the materialized view | When Glue can't | 
| --- | --- | --- | 
| GLUE\_ICEBERG\_MV\_PREFERRED | Glue Iceberg materialized view | Plain Glue Iceberg table, reason logged | 
| GLUE\_ICEBERG\_MV\_ONLY | Glue Iceberg materialized view | Pipeline run fails | 
| NO\_GLUE\_ICEBERG\_MV (default) | Plain Glue Iceberg table | Plain Glue Iceberg table | 

A routed materialized view's sources and the materialized view itself must be Iceberg tables in a Glue catalog in the same Region and account. A routed materialized view is a managed artifact of the pipeline. It refreshes only when the pipeline runs, and it doesn't support standalone REFRESH, scheduled automatic refresh, or automatic query rewrite.

## Managing materialized views
<a name="emr-spark-materialized-views-manage"></a>

Amazon EMR provides SQL commands for managing the lifecycle of materialized views.

### Describing a materialized view
<a name="emr-spark-materialized-views-manage-describe"></a>

To view metadata about a materialized view, including its definition, refresh status, and last refresh timestamp:

```
DESCRIBE EXTENDED customer_orders;
```

### Altering a materialized view
<a name="emr-spark-materialized-views-manage-alter"></a>

To modify the refresh schedule of an existing materialized view:

```
ALTER MATERIALIZED VIEW customer_orders 
ADD SCHEDULE REFRESH EVERY 2 HOURS;
```

To remove automatic refresh:

```
ALTER MATERIALIZED VIEW customer_orders 
DROP SCHEDULE;
```

Use `ALTER MATERIALIZED VIEW` for the refresh schedule. To change the view definition, use `CREATE OR REPLACE MATERIALIZED VIEW`. For more information, see [Changing a materialized view definition](#emr-spark-materialized-views-change-definition).

### Dropping a materialized view
<a name="emr-spark-materialized-views-manage-drop"></a>

To delete a materialized view:

```
DROP MATERIALIZED VIEW customer_orders;
```

This command removes the materialized view definition from the AWS Glue Data Catalog and deletes the underlying Iceberg table data from your S3 bucket.

## Permissions for materialized views
<a name="emr-spark-materialized-views-permissions"></a>

To create and manage materialized views, you must configure permissions for the IAM role that creates the view (the definer role). Amazon EMR supports two permission models:
+ **IAM policies only** – If you manage your data lake with IAM policies, no AWS Lake Formation configuration is required.
+ **AWS Lake Formation** – If you already use AWS Lake Formation to govern your data lake, you can configure AWS Lake Formation permissions for materialized views.

### Required permissions for the definer role
<a name="emr-spark-materialized-views-permissions-definer"></a>

The definer role must have the following Lake Formation permissions:
+ On source tables – SELECT or ALL permissions without row, column, or cell filters (except on fine-grained access control source tables. For more information, see [Materialized views on AWS Lake Formation fine-grained access control source tables](#emr-spark-materialized-views-fgac))
+ On the target database – CREATE\_TABLE permission
+ On the AWS Glue Data Catalog – GetTable and CreateTable API permissions

When you create a materialized view, the definer role's ARN is stored in the view definition. The AWS Glue Data Catalog assumes this role when executing automatic refresh operations. If the definer role loses access to source tables, refresh operations will fail until permissions are restored.

### Granting access to materialized views
<a name="emr-spark-materialized-views-permissions-access"></a>

To grant other users access to query a materialized view, use AWS Lake Formation to grant SELECT permission on the materialized view table. Users can query the materialized view without requiring direct access to the underlying source tables.

For detailed information about configuring Lake Formation permissions, see Granting and revoking permissions on Data Catalog resources in the AWS Lake Formation Developer Guide.

## Monitoring materialized view operations
<a name="emr-spark-materialized-views-monitoring"></a>

The AWS Glue Data Catalog publishes metrics and logs for materialized view refresh operations to Amazon CloudWatch. You can monitor refresh status, duration, and data volume processed through CloudWatch metrics.

### Viewing refresh metrics
<a name="emr-spark-materialized-views-monitoring-metrics"></a>

To view materialized view refresh metrics:

1. Open the CloudWatch console.

1. Choose Metrics from the navigation pane.

1. Select the Glue namespace.

1. Filter metrics by the materialized view name.

### Setting up alarms
<a name="emr-spark-materialized-views-monitoring-alarms"></a>

To receive notifications when refresh operations fail or exceed expected duration, create CloudWatch alarms on materialized view metrics. You can also configure Amazon EventBridge rules to trigger automated responses to refresh events.

## Example: Complete workflow
<a name="emr-spark-materialized-views-example"></a>

The following example demonstrates a complete workflow for creating and using a materialized view on Amazon EMR.

1. Connect to your EMR cluster primary node using SSH.

1. Create a base table with sample data:

   ```
   spark-sql \
     --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
     --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog \
     --conf spark.sql.catalog.glue_catalog.type=glue \
     --conf spark.sql.catalog.glue_catalog.warehouse=s3://amzn-s3-demo-bucket/warehouse \
     --conf spark.sql.catalog.glue_catalog.glue.region=us-east-1 \
     --conf spark.sql.catalog.glue_catalog.glue.id=111122223333 \
     --conf spark.sql.catalog.glue_catalog.glue.account-id=111122223333 \
     --conf spark.sql.catalog.glue_catalog.glue.lakeformation-enabled=true \
     --conf spark.sql.defaultCatalog=glue_catalog \
     --conf spark.sql.optimizer.answerQueriesWithMVs.enabled=true 
   
   
   CREATE DATABASE IF NOT EXISTS sales;
   
   USE sales;
   
   CREATE TABLE orders (
       id INT,
       customer_name STRING,
       amount DECIMAL(10,2),
       order_date DATE
   );
   
   INSERT INTO orders VALUES 
       (1, 'John Doe', 150.00, DATE('2024-01-15')),
       (2, 'Jane Smith', 200.50, DATE('2024-01-16')),
       (3, 'Bob Johnson', 75.25, DATE('2024-01-17'));
   ```

1. Create a materialized view:

   ```
   CREATE MATERIALIZED VIEW customer_summary
   AS 
   SELECT 
       customer_name, 
       COUNT(*) as order_count, 
       SUM(amount) as total_amount 
   FROM glue_catalog.sales.orders
   GROUP BY customer_name;
   ```

1. Query the materialized view:

   ```
   SELECT * FROM customer_summary;
   ```

1. Insert additional data into the base table:

   ```
   INSERT INTO orders VALUES 
       (4, 'Jane Smith', 350.00, DATE('2024-01-18')),
       (5, 'Bob Johnson', 100.25, DATE('2024-01-19'));
   ```

1. Refresh the materialized view:

   ```
   REFRESH MATERIALIZED VIEW customer_summary FULL;
   ```

1. Verify the updated results:

   ```
   SELECT * FROM customer_summary;
   ```

## System-managed materialized views
<a name="emr-spark-materialized-views-system-managed"></a>

With a system-managed materialized view, only AWS Glue can write to the materialized view. AWS Glue writes both its data and its definition, and no other engine or user can modify it. This protects the materialized view from unintended changes, so you can share it as a trusted, consistent dataset. AWS Glue stores the materialized view as a standard Apache Iceberg table in an Amazon S3 Tables bucket within your account.

System-managed materialized views are available with Amazon EMR release 7.14.0 and later, and with Amazon EMR release 8.1.0 and later. They are stored only in Amazon S3 Tables; Amazon S3 general purpose buckets are not supported.

### Enabling system-managed materialized views
<a name="emr-spark-materialized-views-system-managed-enable"></a>

To create system-managed materialized views, set `spark.sql.mv.managed.enabled` to `true` in your Spark session, along with your Amazon S3 Tables catalog configuration:

```
spark-sql \
  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
  --conf spark.sql.catalog.s3t_catalog=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.s3t_catalog.type=glue \
  --conf spark.sql.catalog.s3t_catalog.glue.id=111122223333:s3tablescatalog/amzn-s3-demo-table-bucket \
  --conf spark.sql.catalog.s3t_catalog.warehouse=s3://amzn-s3-demo-bucket/mv-warehouse \
  --conf spark.sql.catalog.s3t_catalog.glue.region=us-east-1 \
  --conf spark.sql.defaultCatalog=s3t_catalog \
  --conf spark.sql.mv.managed.enabled=true
```

### Creating a system-managed materialized view
<a name="emr-spark-materialized-views-system-managed-create"></a>

Create the materialized view with the MANAGED keyword, in a session that has `spark.sql.mv.managed.enabled` set to `true`:

```
CREATE MANAGED MATERIALIZED VIEW s3t_catalog.analytics.customer_summary
AS
SELECT
    customer_name,
    COUNT(*) as order_count,
    SUM(amount) as total_amount
FROM glue_catalog.sales.orders
GROUP BY customer_name;
```

AWS Glue computes and writes the materialized view for you; your Spark session does not write it directly. The CREATE MANAGED MATERIALIZED VIEW statement waits until AWS Glue finishes creating the materialized view before it returns, so it can take longer than creating a regular materialized view.

### Write protection
<a name="emr-spark-materialized-views-system-managed-write-protection"></a>

Only AWS Glue writes the materialized view's data and its metadata, such as its schema and storage location. Any attempt to change these is rejected, whether it comes from another query engine, a direct AWS Glue `UpdateTable` call, or a direct write to the underlying Apache Iceberg table.

You can still perform the following operations on a system-managed materialized view:
+ Refresh the materialized view. AWS Glue runs the refresh and writes the results for you.
+ Change the refresh schedule and table properties.
+ Drop the materialized view, if you have permission to drop it.

Schema evolution is not supported for a system-managed materialized view. To change the materialized view's SQL definition, drop the materialized view and create it again.

## Considerations and limitations
<a name="emr-spark-materialized-views-limitations"></a>

Consider the following when using materialized views with Amazon EMR:
+ Materialized views require Amazon EMR release 7.12.0 or later. Incremental refresh of non-aggregate materialized views, `CREATE OR REPLACE MATERIALIZED VIEW`, Lake Formation fine-grained access control source tables, and Spark Declarative Pipelines routing require Amazon EMR release 8.2.0 or later.
+ Source tables must be registered in the AWS Glue Data Catalog. Apache Iceberg source tables are supported on Amazon EMR release 7.12.0 and later. Apache Hive (non-Iceberg) source tables are supported on Amazon EMR release 7.14.0 and later. Apache Hudi and Linux Foundation Delta Lake source tables are not supported.
+ Source tables must reside in the same AWS Region and AWS account as the materialized view.
+ Materialized views cannot reference AWS Glue Data Catalog views or multi-dialect views as source tables.
+ A materialized view can reference another materialized view as a source table.
+ The view definer role must have full read access (SELECT or ALL permission) on all source tables. Fine-grained access control on source tables is supported as described in [Materialized views on AWS Lake Formation fine-grained access control source tables](#emr-spark-materialized-views-fgac).
+ Materialized views are eventually consistent with source tables. During the refresh window, queries may return stale data. Execute manual refresh for immediate consistency.
+ The minimum automatic refresh interval is one hour on Amazon EMR releases earlier than 7.14.0, and 10 minutes on Amazon EMR release 7.14.0 and later. The maximum interval is 90 days.
+ Incremental refresh of aggregations covers `SUM` and `COUNT`. `AVG`, `MIN`, `MAX`, and `DISTINCT` aggregates refresh in full.
+ Incremental refresh of non-aggregate materialized views (projection, filter, inner join) requires Apache Iceberg format version 3 source tables and is available on Amazon EMR release 8.2.0 and later. On format version 2 source tables, only aggregate materialized views (`SUM` or `COUNT`) refresh incrementally, and non-aggregate materialized views refresh in full. A materialized view that combines a join with an aggregation refreshes in full, and inner joins refresh incrementally only when one source table changed per refresh.
+ An eligible materialized view still falls back to a full refresh in the following cases. Amazon EMR records the reason in the Spark event log.
  + Too many rows or data files changed in a source table.
  + More than one source table changed.
  + A source snapshot expired.
  + The session time zone changed since create.
  + A full refresh is requested.
  + The materialized view's integrity check fails.
+ A materialized view records the Spark version and session time zone it was computed with. Refreshing from a different Spark version is blocked, and query rewrite doesn't use the materialized view. Refreshing from a different time zone runs in full.
+ Incremental refresh does not support user-defined functions or certain built-in functions. Only a subset of Spark SQL built-in functions are supported.
+ Automatic query rewrite only considers materialized views whose definitions belong to a restricted SQL subset similar to the incremental refresh restrictions. It isn't available on AWS Lake Formation fine-grained access control clusters.
+ Full refresh operations override the entire table and make previous snapshots unavailable.
+ Identifiers containing special characters other than alphanumeric characters and underscores are not supported in CREATE MATERIALIZED VIEW queries.
+ Materialized view columns starting with the \_\_ivm prefix are reserved for system use. AWS reserves the right to modify or remove these columns in future releases.
+ The SORT BY, LIMIT, OFFSET, CLUSTER BY, and ORDER BY clauses are not supported in materialized view definitions.
+ Cross-Region and cross-account source tables are not supported.
+ Non-deterministic functions such as rand() or current\_timestamp() are not supported in materialized view definitions.
+ Direct writes to a materialized view table aren't supported. They break the integrity check and force a full refresh or recreation.