# Using materialized views with

Amazon EMR

Amazon EMR release 7.12.0 and later supports creating and managing Apache Iceberg
materialized views in the AWS Glue Data Catalog. A materialized view is a managed
table that stores the precomputed result of a SQL query in Apache Iceberg format and
incrementally updates as the underlying source tables change. You can use materialized
views to simplify data transformation pipelines and accelerate query performance for
complex analytical workloads.

When you create a materialized view using Spark on Amazon EMR, the view definition and
metadata are stored in the AWS Glue Data Catalog. The precomputed results are stored
as Apache Iceberg tables in Amazon S3 Tables buckets or Amazon S3 general purpose
buckets within your AWS account. The AWS Glue Data Catalog automatically monitors
source tables and refreshes materialized views using managed compute
infrastructure.

###### Topics

- [How materialized views
  work with Amazon EMR](#emr-spark-materialized-views-how-it-works "#emr-spark-materialized-views-how-it-works")
- [Prerequisites](#emr-spark-materialized-views-prerequisites "#emr-spark-materialized-views-prerequisites")
- [Configuring Spark to use
  materialized views](#emr-spark-materialized-views-configure "#emr-spark-materialized-views-configure")
- [Creating materialized
  views](#emr-spark-materialized-views-create "#emr-spark-materialized-views-create")
- [Querying materialized
  views](#emr-spark-materialized-views-query "#emr-spark-materialized-views-query")
- [Refreshing materialized
  views](#emr-spark-materialized-views-refresh "#emr-spark-materialized-views-refresh")
- [Managing materialized
  views](#emr-spark-materialized-views-manage "#emr-spark-materialized-views-manage")
- [Permissions for
  materialized views](#emr-spark-materialized-views-permissions "#emr-spark-materialized-views-permissions")
- [Monitoring materialized
  view operations](#emr-spark-materialized-views-monitoring "#emr-spark-materialized-views-monitoring")
- [Example: Complete
  workflow](#emr-spark-materialized-views-example "#emr-spark-materialized-views-example")
- [Considerations and
  limitations](#emr-spark-materialized-views-limitations "#emr-spark-materialized-views-limitations")

## How materialized views

work with Amazon EMR

Materialized views integrate with Amazon EMR through Apache Spark's Iceberg support.
When you configure your Spark session to use the AWS Glue Data Catalog, you can
create materialized views using standard SQL syntax. The Spark optimizer can
automatically rewrite queries to use materialized views when they provide better
performance, eliminating the need to manually modify application code.

The AWS Glue Data Catalog handles all operational aspects of materialized view
maintenance, including:

- Detecting changes in source tables using Apache Iceberg's metadata
  layer
- Scheduling and executing refresh operations using managed Spark
  compute
- Determining whether to perform full or incremental refresh based on the
  data changes
- Storing precomputed results in Apache Iceberg format for multi-engine
  access

You can query materialized views from Amazon EMR using the same Spark SQL interfaces
you use for regular tables. The precomputed data is also accessible from other
services including Amazon Athena and Amazon Redshift.

## Prerequisites

To use materialized views with Amazon EMR, you need:

- An AWS account
- An Amazon EMR cluster running release 7.12.0 or later
- Source tables in Apache Iceberg format registered in the AWS Glue Data
  Catalog
- AWS Lake Formation permissions configured for source tables and target
  databases
- An S3 Tables bucket or S3 general purpose bucket registered with AWS
  Lake Formation for storing materialized view data

## Configuring Spark to use

materialized views

To create and manage materialized views, configure your Spark session with the
required Iceberg extensions and catalog settings. The configuration varies depending
on whether your source tables and materialized views use S3 Tables buckets or S3
general purpose buckets.

### Configuring

for S3 Tables

When using S3 Tables buckets for materialized views, configure separate
catalog references for your source tables and materialized views:

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

### Configuring

for S3 general purpose buckets

When using S3 general purpose buckets, configure a single catalog
reference:

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

### Enabling

incremental refresh

To enable incremental refresh optimization, add the following configuration
properties to your Spark session:

```
spark-sql \
  --conf spark.sql.optimizer.incrementalMVRefresh.enabled=true \

```

### Configuration parameters

The following configuration parameters control materialized view
behavior:

- `spark.sql.extensions` – Enables Iceberg Spark session
  extensions required for materialized view support.
- `spark.sql.optimizer.answerQueriesWithMVs.enabled` –
  Enables automatic query rewrite to use materialized views. Set to true
  to activate this optimization.
- `spark.sql.optimizer.incrementalMVRefresh.enabled` –
  Enables incremental refresh optimization. Set to true to process only
  changed data during refresh operations.

## Creating materialized

views

You create materialized views using the CREATE MATERIALIZED VIEW SQL statement.
The view definition specifies the transformation logic as a SQL query that
references one or more source tables.

### DLLs

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

###### Note

The view_clauses must appear before the select_statement.

### Creating a basic

materialized view

The following example creates a materialized view that aggregates order data
by customer, use fully qualified table names with three part naming convention
in view definition:

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

### Creating a

materialized view with automatic refresh

To configure automatic refresh, specify a refresh schedule when creating the
view using fully qualified table names with three part naming convention in view
definition:

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

### Creating a

materialized view with cross-catalog references

When your source tables are in a different catalog than your materialized
view, use fully qualified table names with three-part naming convention in both
view name and view definition:

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

## Querying materialized

views

After creating a materialized view, you can query it like any other table using
standard SQL SELECT statements:

```
SELECT * FROM customer_orders;
```

### Automatic query

rewrite

When automatic query rewrite is enabled, the Spark optimizer analyzes your
queries and automatically uses materialized views when they can improve
performance. For example, if you execute the following query:

```
SELECT
    customer_name,
    COUNT(*) as order_count,
    SUM(amount) as total_amount
FROM orders
GROUP BY customer_name;
```

The Spark optimizer automatically rewrites this query to use the
customer_orders materialized view instead of processing the base orders table,
provided the materialized view is current.

### Verifying automatic

query rewrite

To verify whether a query uses automatic query rewrite, use the EXPLAIN
EXTENDED command:

```
EXPLAIN EXTENDED
SELECT customer_name, COUNT(*) as order_count, SUM(amount) as total_amount
FROM orders
GROUP BY customer_name;
```

In the execution plan, look for the materialized view name in the BatchScan
operation. If the plan shows BatchScan glue_catalog.analytics.customer_orders
instead of BatchScan glue_catalog.sales.orders, the query has been automatically
rewritten to use the materialized view.

###### Note

Automatic query rewrite requires time for the Spark metadata cache to
populate after creating a materialized view. This process typically
completes within 30 seconds.

## Refreshing materialized

views

You can refresh materialized views using two methods: full refresh or incremental
refresh. Full refresh recomputes the entire materialized view from all base table
data, while incremental refresh processes only the data that has changed since the
last refresh.

### Manual full

refresh

To perform a full refresh of a materialized view:

```
REFRESH MATERIALIZED VIEW customer_orders FULL;
```

After executing this command, query the materialized view to verify the
updated results:

```
SELECT * FROM customer_orders;
```

### Manual

incremental refresh

To perform an incremental refresh, ensure incremental refresh is enabled in
your Spark session configuration, then execute:

```
REFRESH MATERIALIZED VIEW customer_orders;
```

The AWS Glue Data Catalog automatically determines whether incremental
refresh is applicable based on the view definition and the amount of changed
data. If incremental refresh is not possible, the operation falls back to full
refresh.

### Verifying

incremental refresh execution

To confirm that incremental refresh executed successfully, you can check the
`lastRefreshType` table properties by running the following
commands:

```

SHOW TBLPROPERTIES <mvName>("lastRefreshType")

```

Also, this can also be achieved by enabling debug logging by modifying your
Spark log configuration:

1. Open the Spark log4j configuration file:

```
sudo vim /usr/lib/spark/conf/log4j2.properties
```

2. Add the following logger configurations:

```
logger.spark.name = org.apache.spark.sql
logger.spark.level = debug

logger.inmemcache.name = org.apache.spark.sql.InMemMvMetadataCache
logger.inmemcache.level = off
```

3. After executing a refresh operation, search for the following message
   in the Spark output:

```
DEBUG RefreshMaterializedViewExec: Executed Incremental Refresh
```

## Managing materialized

views

Amazon EMR provides SQL commands for managing the lifecycle of materialized
views.

### Describing a

materialized view

To view metadata about a materialized view, including its definition, refresh
status, and last refresh timestamp:

```
DESCRIBE EXTENDED customer_orders;
```

### Altering a

materialized view

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

### Dropping a

materialized view

To delete a materialized view:

```
DROP MATERIALIZED VIEW customer_orders;
```

This command removes the materialized view definition from the AWS Glue Data
Catalog and deletes the underlying Iceberg table data from your S3
bucket.

## Permissions for

materialized views

To create and manage materialized views, you must configure AWS Lake Formation
permissions. The IAM role creating the materialized view (the definer role) requires
specific permissions on source tables and target databases.

### Required

permissions for the definer role

The definer role must have the following Lake Formation permissions:

- On source tables – SELECT or ALL permissions without row, column, or
  cell filters
- On the target database – CREATE_TABLE permission
- On the AWS Glue Data Catalog – GetTable and CreateTable API
  permissions

When you create a materialized view, the definer role's ARN is stored in the
view definition. The AWS Glue Data Catalog assumes this role when executing
automatic refresh operations. If the definer role loses access to source tables,
refresh operations will fail until permissions are restored.

### Granting

access to materialized views

To grant other users access to query a materialized view, use AWS Lake
Formation to grant SELECT permission on the materialized view table. Users can
query the materialized view without requiring direct access to the underlying
source tables.

For detailed information about configuring Lake Formation permissions, see
Granting and revoking permissions on Data Catalog resources in the AWS Lake
Formation Developer Guide.

## Monitoring materialized

view operations

The AWS Glue Data Catalog publishes metrics and logs for materialized view
refresh operations to Amazon CloudWatch. You can monitor refresh status, duration,
and data volume processed through CloudWatch metrics.

### Viewing

refresh metrics

To view materialized view refresh metrics:

1. Open the CloudWatch console.
2. Choose Metrics from the navigation pane.
3. Select the Glue namespace.
4. Filter metrics by the materialized view name.

### Setting up

alarms

To receive notifications when refresh operations fail or exceed expected
duration, create CloudWatch alarms on materialized view metrics. You can also
configure Amazon EventBridge rules to trigger automated responses to refresh
events.

## Example: Complete

workflow

The following example demonstrates a complete workflow for creating and using a
materialized view on Amazon EMR.

1. Connect to your EMR cluster primary node using SSH.
2. Create a base table with sample data:

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

3. Create a materialized view:

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

4. Query the materialized view:

```
SELECT * FROM customer_summary;
```

5. Insert additional data into the base table:

```
INSERT INTO orders VALUES
    (4, 'Jane Smith', 350.00, DATE('2024-01-18')),
    (5, 'Bob Johnson', 100.25, DATE('2024-01-19'));
```

6. Refresh the materialized view:

```
REFRESH MATERIALIZED VIEW customer_summary FULL;
```

7. Verify the updated results:

```
SELECT * FROM customer_summary;
```

## Considerations and

limitations

Consider the following when using materialized views with Amazon EMR:

- Materialized views require Amazon EMR release 7.12.0 or later.
- Source tables must be Apache Iceberg tables registered in the AWS Glue
  Data Catalog. Apache Hive, Apache Hudi, and Linux Foundation Delta Lake
  tables are not supported at launch.
- Source tables must reside in the same AWS Region and AWS account as
  the materialized view.
- All source tables must be governed by AWS Lake Formation. IAM-only
  permissions and hybrid access are not supported.
- Materialized views cannot reference AWS Glue Data Catalog views,
  multi-dialect views, or other materialized views as source tables.
- The view definer role must have full read access (SELECT or ALL
  permission) on all source tables without row, column, or cell filters
  applied.
- Materialized views are eventually consistent with source tables. During
  the refresh window, queries may return stale data. Execute manual refresh
  for immediate consistency.
- The minimum automatic refresh interval is one hour.
- Incremental refresh supports a restricted subset of SQL operations. The
  view definition must be a single SELECT-FROM-WHERE-GROUP BY-HAVING block and
  cannot contain set operations, subqueries, the DISTINCT keyword in SELECT or
  aggregate functions, window functions, or joins other than INNER
  JOIN.
- Incremental refresh does not support user-defined functions or certain
  built-in functions. Only a subset of Spark SQL built-in functions are
  supported.
- Query automatic rewrite only considers materialized views whose
  definitions belong to a restricted SQL subset similar to incremental refresh
  restrictions.
- Full refresh operations override the entire table and make previous
  snapshots unavailable.
- Identifiers containing special characters other than alphanumeric
  characters and underscores are not supported in CREATE MATERIALIZED VIEW
  queries.
- Materialized view columns starting with the \_\_ivm prefix are reserved for
  system use. AWS reserves the right to modify or remove these columns in
  future releases.
- The SORT BY, LIMIT, OFFSET, CLUSTER BY, and ORDER BY clauses are not
  supported in materialized view definitions.
- Cross-Region and cross-account source tables are not supported.
- Non-deterministic functions such as rand() or current_timestamp() are not
  supported in materialized view definitions.
