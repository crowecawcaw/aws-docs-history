# Using materialized views with AWS Glue

AWS Glue version 5.1 and later supports creating and managing Apache Iceberg materialized views
in the AWS Glue Data Catalog. A materialized view is a managed table that stores the precomputed
result of a SQL query in Apache Iceberg format and incrementally updates as the underlying
source tables change. You can use materialized views to simplify data transformation pipelines
and accelerate query performance for complex analytical workloads.

When you create a materialized view using Spark in AWS Glue, the view definition and metadata
are stored in the AWS Glue Data Catalog. The precomputed results are stored as Apache Iceberg
tables in Amazon S3 Tables buckets or Amazon S3 general purpose buckets within your account. The
AWS Glue Data Catalog automatically monitors source tables and refreshes materialized views using
managed compute infrastructure.

###### Topics

- [How materialized views work with AWS Glue](#materialized-views-how-they-work "#materialized-views-how-they-work")
- [Prerequisites](#materialized-views-prerequisites "#materialized-views-prerequisites")
- [Configuring Spark to use materialized views](#materialized-views-configuring-spark "#materialized-views-configuring-spark")
- [Creating materialized views](#materialized-views-creating "#materialized-views-creating")
- [Querying materialized views](#materialized-views-querying "#materialized-views-querying")
- [Refreshing materialized views](#materialized-views-refreshing "#materialized-views-refreshing")
- [Managing materialized views](#materialized-views-managing "#materialized-views-managing")
- [Permissions for materialized views](#materialized-views-permissions "#materialized-views-permissions")
- [Monitoring materialized view operations](#materialized-views-monitoring "#materialized-views-monitoring")
- [Example: Complete workflow](#materialized-views-complete-workflow "#materialized-views-complete-workflow")
- [Considerations and limitations](#materialized-views-considerations-limitations "#materialized-views-considerations-limitations")

## How materialized views work with AWS Glue

Materialized views integrate with AWS Glue through Apache Spark's Iceberg support in AWS Glue
jobs and AWS Glue Studio notebooks. When you configure your Spark session to use the AWS Glue Data
Catalog, you can create materialized views using standard SQL syntax. The Spark optimizer can
automatically rewrite queries to use materialized views when they provide better performance,
eliminating the need to manually modify application code.

The AWS Glue Data Catalog handles all operational aspects of materialized view maintenance,
including:

- Detecting changes in source tables using Apache Iceberg's metadata layer
- Scheduling and executing refresh operations using managed Spark compute
- Determining whether to perform full or incremental refresh based on the data
  changes
- Storing precomputed results in Apache Iceberg format for multi-engine access

You can query materialized views from AWS Glue using the same Spark SQL interfaces you use
for regular tables. The precomputed data is also accessible from other services including
Amazon Athena and Amazon Redshift.

## Prerequisites

To use materialized views with AWS Glue, you need:

- An account
- AWS Glue version 5.1 or later
- Source tables in Apache Iceberg format registered in the AWS Glue Data Catalog
- AWS Lake Formation permissions configured for source tables and target databases
- An S3 Tables bucket or S3 general purpose bucket registered with AWS Lake Formation for storing
  materialized view data
- An IAM role with permissions to access AWS Glue Data Catalog and Amazon S3

## Configuring Spark to use materialized views

To create and manage materialized views in AWS Glue, configure your Spark session with the
required Iceberg extensions and catalog settings. The configuration method varies depending on
whether you're using AWS Glue jobs or AWS Glue Studio notebooks.

### Configuring AWS Glue jobs

When creating or updating an AWS Glue job, add the following configuration parameters as
job parameters:

#### For S3 Tables buckets

```

job = glue.create_job(
    Name='materialized-view-job',
    Role='arn:aws:iam::111122223333:role/GlueServiceRole',
    Command={
        'Name': 'glueetl',
        'ScriptLocation': 's3://amzn-s3-demo-bucket/scripts/mv-script.py',
        'PythonVersion': '3'
    },
    DefaultArguments={
        '--enable-glue-datacatalog': 'true',
        '--conf': 'spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions '
        '--conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog '
                  '--conf spark.sql.catalog.glue_catalog.type=glue '
                  '--conf spark.sql.catalog.glue_catalog.warehouse=s3://amzn-s3-demo-bucket/warehouse '
                  '--conf spark.sql.catalog.glue_catalog.glue.region=us-east-1 '
                  '--conf spark.sql.catalog.glue_catalog.glue.id=111122223333 '
                  '--conf spark.sql.catalog.glue_catalog.glue.account-id=111122223333 ',
                  '--conf spark.sql.catalog.glue_catalog.glue.lakeformation-enabled=true ',
                  '--conf spark.sql.catalog.s3t_catalog=org.apache.iceberg.spark.SparkCatalog '
                  '--conf spark.sql.catalog.s3t_catalog.type=glue '
                  '--conf spark.sql.catalog.s3t_catalog.glue.id=111122223333:s3tablescatalog/my-table-bucket ',
                  '--conf spark.sql.catalog.s3t_catalog.glue.account-id=111122223333 ',
                  '--conf spark.sql.catalog.s3t_catalog.glue.lakeformation-enabled=true ',
                  '--conf spark.sql.catalog.s3t_catalog.warehouse=s3://amzn-s3-demo-bucket/mv-warehouse '
                  '--conf spark.sql.catalog.s3t_catalog.glue.region=us-east-1 '
                  '--conf spark.sql.defaultCatalog=s3t_catalog '
                  '--conf spark.sql.optimizer.answerQueriesWithMVs.enabled=true '
                  '--conf spark.sql.materializedViews.metadataCache.enabled=true'
    },
    GlueVersion='5.1'
)

```

#### For S3 general purpose buckets

```

job = glue.create_job(
    Name='materialized-view-job',
    Role='arn:aws:iam::111122223333:role/GlueServiceRole',
    Command={
        'Name': 'glueetl',
        'ScriptLocation': 's3://amzn-s3-demo-bucket/scripts/mv-script.py',
        'PythonVersion': '3'
    },
    DefaultArguments={
        '--enable-glue-datacatalog': 'true',
        '--conf': 'spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions '
                  '--conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog '
                  '--conf spark.sql.catalog.glue_catalog.type=glue '
                  '--conf spark.sql.catalog.glue_catalog.warehouse=s3://amzn-s3-demo-bucket/warehouse '
                  '--conf spark.sql.catalog.glue_catalog.glue.region=us-east-1 '
                  '--conf spark.sql.catalog.glue_catalog.glue.id=111122223333 ',
                  '--conf spark.sql.catalog.glue_catalog.glue.account-id=111122223333 ',
                  '--conf spark.sql.catalog.glue_catalog.glue.lakeformation-enabled=true ',
                  '--conf spark.sql.defaultCatalog=glue_catalog '
                  '--conf spark.sql.optimizer.answerQueriesWithMVs.enabled=true '
                  '--conf spark.sql.materializedViews.metadataCache.enabled=true'
    },
    GlueVersion='5.1'
)

```

### Configuring AWS Glue Studio notebooks

In AWS Glue Studio notebooks, configure your Spark session using the %%configure magic
command at the beginning of your notebook:

```
%%configure
{
    "conf": {
        "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
        "spark.sql.catalog.glue_catalog": "org.apache.iceberg.spark.SparkCatalog",
        "spark.sql.catalog.glue_catalog.type": "glue",
        "spark.sql.catalog.glue_catalog.warehouse": "s3://amzn-s3-demo-bucket/warehouse",
        "spark.sql.catalog.glue_catalog.glue.region": "us-east-1",
        "spark.sql.catalog.glue_catalog.glue.id": "111122223333",
        "spark.sql.catalog.glue_catalog.glue.account-id": "111122223333",
        "spark.sql.catalog.glue_catalog.glue.lakeformation-enabled": "true",
        "spark.sql.defaultCatalog": "glue_catalog",
        "spark.sql.optimizer.answerQueriesWithMVs.enabled": "true",
        "spark.sql.materializedViews.metadataCache.enabled": "true"
    }
}
```

### Enabling incremental refresh

To enable incremental refresh optimization, add the following configuration properties
to your job parameters or notebook configuration:

```
--conf spark.sql.optimizer.incrementalMVRefresh.enabled=true
--conf spark.sql.optimizer.incrementalMVRefresh.deltaThresholdCheckEnabled=false
```

### Configuration parameters

The following configuration parameters control materialized view behavior:

- `spark.sql.extensions` – Enables Iceberg Spark session extensions
  required for materialized view support.
- `spark.sql.optimizer.answerQueriesWithMVs.enabled` – Enables automatic
  query rewrite to use materialized views. Set to true to activate this
  optimization.
- `spark.sql.materializedViews.metadataCache.enabled` – Enables caching of
  materialized view metadata for query optimization. Set to true to improve query rewrite
  performance.
- `spark.sql.optimizer.incrementalMVRefresh.enabled` – Enables incremental
  refresh optimization. Set to true to process only changed data during refresh
  operations.
- `spark.sql.optimizer.answerQueriesWithMVs.decimalAggregateCheckEnabled` –
  Controls validation of decimal aggregate operations in query rewrite. Set to false to
  disable certain decimal overflow checks.

## Creating materialized views

You create materialized views using the CREATE MATERIALIZED VIEW SQL statement in AWS Glue
jobs or notebooks. The view definition specifies the transformation logic as a SQL query that
references one or more source tables.

### Creating a basic materialized view in AWS Glue jobs

The following example demonstrates creating a materialized view in a AWS Glue job
script, use fully qualified table names with three part naming convention in view definition:

```
from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Create materialized view
spark.sql("""
    CREATE MATERIALIZED VIEW customer_orders
    AS
    SELECT
        customer_name,
        COUNT(*) as order_count,
        SUM(amount) as total_amount
    FROM glue_catalog.sales.orders
    GROUP BY customer_name
""")
```

### Creating a materialized view with automatic refresh

To configure automatic refresh, specify a refresh schedule when creating the
view, using fully qualified table names with three part naming convention in view definition:

```
spark.sql("""
    CREATE MATERIALIZED VIEW customer_orders
    SCHEDULE REFRESH EVERY 1 HOUR
    AS
    SELECT
        customer_name,
        COUNT(*) as order_count,
        SUM(amount) as total_amount
    FROM glue_catalog.sales.orders
    GROUP BY customer_name
""")
```

### Creating a materialized view with cross-catalog references

When your source tables are in a different catalog than your materialized view, use
fully qualified table names with three-part naming convention in both view name and view definition:

```
spark.sql("""
    CREATE MATERIALIZED VIEW s3t_catalog.analytics.customer_summary
    AS
    SELECT
        customer_name,
        COUNT(*) as order_count,
        SUM(amount) as total_amount
    FROM glue_catalog.sales.orders
    GROUP BY customer_name
""")
```

### Creating materialized views in AWS Glue Studio notebooks

In AWS Glue Studio notebooks, you can use the %%sql magic command to create materialized
views, using fully qualified table names with three part naming convention in view definition:

```
%%sql
CREATE MATERIALIZED VIEW customer_orders
AS
SELECT
    customer_name,
    COUNT(*) as order_count,
    SUM(amount) as total_amount
FROM glue_catalog.sales.orders
GROUP BY customer_name
```

## Querying materialized views

After creating a materialized view, you can query it like any other table using standard
SQL SELECT statements in your AWS Glue jobs or notebooks.

### Querying in AWS Glue jobs

```
from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Query materialized view
result = spark.sql("SELECT * FROM customer_orders")
result.show()
```

### Querying in AWS Glue Studio notebooks

```
%%sql
SELECT * FROM customer_orders
```

### Automatic query rewrite

When automatic query rewrite is enabled, the Spark optimizer analyzes your queries and
automatically uses materialized views when they can improve performance. For example, if you
execute the following query:

```
result = spark.sql("""
    SELECT
        customer_name,
        COUNT(*) as order_count,
        SUM(amount) as total_amount
    FROM orders
    GROUP BY customer_name
""")
```

The Spark optimizer automatically rewrites this query to use the customer_orders
materialized view instead of processing the base orders table, provided the materialized
view is current.

### Verifying automatic query rewrite

To verify whether a query uses automatic query rewrite, use the EXPLAIN EXTENDED
command:

```
spark.sql("""
    EXPLAIN EXTENDED
    SELECT customer_name, COUNT(*) as order_count, SUM(amount) as total_amount
    FROM orders
    GROUP BY customer_name
""").show(truncate=False)
```

In the execution plan, look for the materialized view name in the BatchScan operation.
If the plan shows BatchScan glue_catalog.analytics.customer_orders instead of BatchScan
glue_catalog.sales.orders, the query has been automatically rewritten to use the
materialized view.

Note that automatic query rewrite requires time for the Spark metadata cache to populate
after creating a materialized view. This process typically completes within 30
seconds.

## Refreshing materialized views

You can refresh materialized views using two methods: full refresh or incremental refresh.
Full refresh recomputes the entire materialized view from all base table data, while
incremental refresh processes only the data that has changed since the last refresh.

### Manual full refresh in AWS Glue jobs

To perform a full refresh of a materialized view:

```
spark.sql("REFRESH MATERIALIZED VIEW customer_orders FULL")

# Verify updated results
result = spark.sql("SELECT * FROM customer_orders")
result.show()
```

### Manual incremental refresh in AWS Glue jobs

To perform an incremental refresh, ensure incremental refresh is enabled in your Spark
session configuration, then execute:

```
spark.sql("REFRESH MATERIALIZED VIEW customer_orders")

# Verify updated results
result = spark.sql("SELECT * FROM customer_orders")
result.show()
```

The AWS Glue Data Catalog automatically determines whether incremental refresh is
applicable based on the view definition and the amount of changed data. If incremental
refresh is not possible, the operation falls back to full refresh.

### Refreshing in AWS Glue Studio notebooks

In notebooks, use the %%sql magic command:

```
%%sql
REFRESH MATERIALIZED VIEW customer_orders FULL
```

### Verifying incremental refresh execution

To confirm that incremental refresh executed successfully, enable debug logging in your
AWS Glue job:

```
from awsglue.context import GlueContext
from pyspark.context import SparkContext
import logging

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Enable debug logging
logger = logging.getLogger('org.apache.spark.sql')
logger.setLevel(logging.DEBUG)

# Execute refresh
spark.sql("REFRESH MATERIALIZED VIEW customer_orders")
```

Search for the following message in the AWS Glue job logs:

```
DEBUG RefreshMaterializedViewExec: Executed Incremental Refresh
```

## Managing materialized views

AWS Glue provides SQL commands for managing the lifecycle of materialized views in your jobs
and notebooks.

### Describing a materialized view

To view metadata about a materialized view, including its definition, refresh status,
and last refresh timestamp:

```
spark.sql("DESCRIBE EXTENDED customer_orders").show(truncate=False)
```

### Altering a materialized view

To modify the refresh schedule of an existing materialized view:

```
spark.sql("""
    ALTER MATERIALIZED VIEW customer_orders
    ADD SCHEDULE REFRESH EVERY 2 HOURS
""")
```

To remove automatic refresh:

```
spark.sql("""
    ALTER MATERIALIZED VIEW customer_orders
    DROP SCHEDULE
""")
```

### Dropping a materialized view

To delete a materialized view:

```
spark.sql("DROP MATERIALIZED VIEW customer_orders")
```

This command removes the materialized view definition from the AWS Glue Data Catalog and
deletes the underlying Iceberg table data from your S3 bucket.

### Listing materialized views

To list all materialized views in a database:

```
spark.sql("SHOW VIEWS FROM analytics").show()
```

## Permissions for materialized views

To create and manage materialized views, you must configure AWS Lake Formation permissions. The IAM
role creating the materialized view (the definer role) requires specific permissions on source
tables and target databases.

### Required permissions for the definer role

The definer role must have the following Lake Formation permissions:

- On source tables – SELECT or ALL permissions without row, column, or cell
  filters
- On the target database – CREATE_TABLE permission
- On the AWS Glue Data Catalog – GetTable and CreateTable API permissions

When you create a materialized view, the definer role's ARN is stored in the view
definition. The AWS Glue Data Catalog assumes this role when executing automatic refresh
operations. If the definer role loses access to source tables, refresh operations will fail
until permissions are restored.

### IAM permissions for AWS Glue jobs

Your AWS Glue job's IAM role requires the following permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "glue:GetCatalog",
                "glue:GetCatalogs",
                "glue:GetTable",
                "glue:GetTables",
                "glue:CreateTable",
                "glue:UpdateTable",
                "glue:DeleteTable",
                "glue:GetDatabase",
                "glue:GetDatabases",
                "cloudwatch:PutMetricData"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:*:*:*:/aws-glue/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "lakeformation:GetDataAccess"
            ],
            "Resource": "*"
        }
    ]
}
```

The role you use for Materialized View auto-refresh must have the iam:PassRole permission on the role.

```

{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:PassRole"
      ],
      "Resource": [
        "arn:aws:iam::111122223333:role/materialized-view-role-name"
      ]
    }
  ]
}

```

To let Glue automatically refresh the materialized view for you, the role must also have the following trust policy that enables the service to assume the role.

```

{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:PassRole"
      ],
      "Resource": [
        "arn:aws:iam::111122223333:role/materialized-view-role-name"
      ]
    }
  ]
}

```

If the Materialized View is stored in S3 Tables Buckets, you also need to add the following permission to the role.

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3tables:PutTableMaintenanceConfiguration"
      ],
      "Resource": "arn:aws:s3tables:*:123456789012:*"
    }
  ]
}

```

### Granting access to materialized views

To grant other users access to query a materialized view, use AWS Lake Formation to grant SELECT
permission on the materialized view table. Users can query the materialized view without
requiring direct access to the underlying source tables.

For detailed information about configuring Lake Formation permissions, see Granting and
revoking permissions on Data Catalog resources in the AWS Lake Formation Developer Guide.

## Monitoring materialized view operations

The AWS Glue Data Catalog publishes metrics and logs for materialized view refresh operations
to Amazon CloudWatch. You can monitor refresh status, duration, and data volume processed
through CloudWatch metrics.

### Viewing job logs

To view logs for AWS Glue jobs that create or refresh materialized views:

1. Open the AWS Glue console.
2. Choose Jobs from the navigation pane.
3. Select your job and choose Runs.
4. Select a specific run and choose Logs to view CloudWatch logs.

### Setting up alarms

To receive notifications when refresh operations fail or exceed expected duration,
create CloudWatch alarms on materialized view metrics. You can also configure Amazon
EventBridge rules to trigger automated responses to refresh events.

## Example: Complete workflow

The following example demonstrates a complete workflow for creating and using a
materialized view in AWS Glue.

### Example AWS Glue job script

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Create database and base table
spark.sql("CREATE DATABASE IF NOT EXISTS sales")
spark.sql("USE sales")

spark.sql("""
    CREATE TABLE IF NOT EXISTS orders (
        id INT,
        customer_name STRING,
        amount DECIMAL(10,2),
        order_date DATE
    )
""")

# Insert sample data
spark.sql("""
    INSERT INTO orders VALUES
        (1, 'John Doe', 150.00, DATE('2024-01-15')),
        (2, 'Jane Smith', 200.50, DATE('2024-01-16')),
        (3, 'Bob Johnson', 75.25, DATE('2024-01-17'))
""")

# Create materialized view
spark.sql("""
    CREATE MATERIALIZED VIEW customer_summary
    AS
    SELECT
        customer_name,
        COUNT(*) as order_count,
        SUM(amount) as total_amount
    FROM glue_catalog.sales.orders
    GROUP BY customer_name
""")

# Query the materialized view
print("Initial materialized view data:")
spark.sql("SELECT * FROM customer_summary").show()

# Insert additional data
spark.sql("""
    INSERT INTO orders VALUES
        (4, 'Jane Smith', 350.00, DATE('2024-01-18')),
        (5, 'Bob Johnson', 100.25, DATE('2024-01-19'))
""")

# Refresh the materialized view
spark.sql("REFRESH MATERIALIZED VIEW customer_summary FULL")

# Query updated results
print("Updated materialized view data:")
spark.sql("SELECT * FROM customer_summary").show()

job.commit()
```

### Example AWS Glue Studio notebook

```
%%configure
{
    "conf": {
        "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
        "spark.sql.catalog.glue_catalog": "org.apache.iceberg.spark.SparkCatalog",
        "spark.sql.catalog.glue_catalog.type": "glue",
        "spark.sql.catalog.glue_catalog.warehouse": "s3://amzn-s3-demo-bucket/warehouse",
        "spark.sql.catalog.glue_catalog.glue.region": "us-east-1",
        "spark.sql.catalog.glue_catalog.glue.id": "111122223333",
        "spark.sql.catalog.glue_catalog.glue.account-id": "111122223333",
        "spark.sql.catalog.glue_catalog.glue.lakeformation-enabled": "true",
        "spark.sql.defaultCatalog": "glue_catalog",
        "spark.sql.optimizer.answerQueriesWithMVs.enabled": "true",
        "spark.sql.materializedViews.metadataCache.enabled": "true"
    }
}
```

```
%%sql
CREATE DATABASE IF NOT EXISTS sales
```

```
%%sql
USE sales
```

```
%%sql
CREATE TABLE IF NOT EXISTS orders (
    id INT,
    customer_name STRING,
    amount DECIMAL(10,2),
    order_date DATE
)
```

```
%%sql
INSERT INTO orders VALUES
    (1, 'John Doe', 150.00, DATE('2024-01-15')),
    (2, 'Jane Smith', 200.50, DATE('2024-01-16')),
    (3, 'Bob Johnson', 75.25, DATE('2024-01-17'))
```

```
%%sql
CREATE MATERIALIZED VIEW customer_summary
AS
SELECT
    customer_name,
    COUNT(*) as order_count,
    SUM(amount) as total_amount
FROM glue_catalog.sales.orders
GROUP BY customer_name
```

```
%%sql
SELECT * FROM customer_summary
```

```
%%sql
INSERT INTO orders VALUES
    (4, 'Jane Smith', 350.00, DATE('2024-01-18')),
    (5, 'Bob Johnson', 100.25, DATE('2024-01-19'))
```

```
%%sql
REFRESH MATERIALIZED VIEW customer_summary FULL
```

```
%%sql
SELECT * FROM customer_summary
```

## Considerations and limitations

Consider the following when using materialized views with AWS Glue:

- Materialized views require AWS Glue version 5.1 or later.
- Source tables must be Apache Iceberg tables registered in the AWS Glue Data Catalog.
  Apache Hive, Apache Hudi, and Linux Foundation Delta Lake tables are not supported at
  launch.
- Source tables must reside in the same Region and account as the materialized
  view.
- All source tables must be governed by AWS Lake Formation. IAM-only permissions and hybrid access
  are not supported.
- Materialized views cannot reference AWS Glue Data Catalog views, multi-dialect views, or
  other materialized views as source tables.
- The view definer role must have full read access (SELECT or ALL permission) on all
  source tables without row, column, or cell filters applied.
- Materialized views are eventually consistent with source tables. During the refresh
  window, queries may return stale data. Execute manual refresh for immediate
  consistency.
- The minimum automatic refresh interval is one hour.
- Incremental refresh supports a restricted subset of SQL operations. The view
  definition must be a single SELECT-FROM-WHERE-GROUP BY-HAVING block and cannot contain set
  operations, subqueries, the DISTINCT keyword in SELECT or aggregate functions, window
  functions, or joins other than INNER JOIN.
- Incremental refresh does not support user-defined functions or certain built-in
  functions. Only a subset of Spark SQL built-in functions are supported.
- Query automatic rewrite only considers materialized views whose definitions belong to
  a restricted SQL subset similar to incremental refresh restrictions.
- Identifiers containing special characters other than alphanumeric characters and
  underscores are not supported in CREATE MATERIALIZED VIEW queries. This applies to all
  identifier types including catalog/namespace/table names, column and struct field names,
  CTEs, and aliases.
- Materialized view columns starting with the \_\_ivm prefix are reserved for system use.
  Amazon reserves the right to modify or remove these columns in future releases.
- The SORT BY, LIMIT, OFFSET, CLUSTER BY, and ORDER BY clauses are not supported in
  materialized view definitions.
- Cross-Region and cross-account source tables are not supported.
- Tables referenced in the view query must use three-part naming convention (e.g.,
  glue_catalog.my_db.my_table) because automatic refresh does not use default catalog and
  database settings.
- Full refresh operations override the entire table and make previous snapshots
  unavailable.
- Non-deterministic functions such as rand() or current_timestamp() are not supported in
  materialized view definitions.
