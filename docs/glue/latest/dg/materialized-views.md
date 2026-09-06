

# Using materialized views with AWS Glue
<a name="materialized-views"></a>

AWS Glue version 5.1 and later supports creating and managing Apache Iceberg materialized views in the AWS Glue Data Catalog. A materialized view is a managed table that stores the precomputed result of a SQL query in Apache Iceberg format and incrementally updates as the underlying source tables change. You can use materialized views to simplify data transformation pipelines and accelerate query performance for complex analytical workloads.

When you create a materialized view using Spark in AWS Glue, the view definition and metadata are stored in the AWS Glue Data Catalog. The precomputed results are stored as Apache Iceberg tables in Amazon S3 Tables buckets or Amazon S3 general purpose buckets within your account. The AWS Glue Data Catalog automatically monitors source tables and refreshes materialized views using managed compute infrastructure.

**Topics**
+ [How materialized views work with AWS Glue](#materialized-views-how-they-work)
+ [Prerequisites](#materialized-views-prerequisites)
+ [Configuring Spark to use materialized views](#materialized-views-configuring-spark)
+ [Creating materialized views](#materialized-views-creating)
+ [Querying materialized views](#materialized-views-querying)
+ [Refreshing materialized views](#materialized-views-refreshing)
+ [Managing materialized views](#materialized-views-managing)
+ [Permissions for materialized views](#materialized-views-permissions)
+ [Monitoring materialized view operations](#materialized-views-monitoring)
+ [Example: Complete workflow](#materialized-views-complete-workflow)
+ [Considerations and limitations](#materialized-views-considerations-limitations)

## How materialized views work with AWS Glue
<a name="materialized-views-how-they-work"></a>

Materialized views integrate with AWS Glue through Apache Spark's Iceberg support in AWS Glue jobs and AWS Glue Studio notebooks. When you configure your Spark session to use the AWS Glue Data Catalog, you can create materialized views using standard SQL syntax. The Spark optimizer can automatically rewrite queries to use materialized views when they provide better performance, eliminating the need to manually modify application code.

The AWS Glue Data Catalog handles all operational aspects of materialized view maintenance, including:
+ Detecting changes in source tables using Apache Iceberg's metadata layer
+ Scheduling and executing refresh operations using managed Spark compute
+ Determining whether to perform full or incremental refresh based on the data changes
+ Storing precomputed results in Apache Iceberg format for multi-engine access

You can query materialized views from AWS Glue using the same Spark SQL interfaces you use for regular tables. The precomputed data is also accessible from other services including Amazon Athena and Amazon Redshift.

## Prerequisites
<a name="materialized-views-prerequisites"></a>

To use materialized views with AWS Glue, you need:
+ An AWS account
+ AWS Glue version 5.1 or later
+ Source tables in Apache Iceberg format registered in the AWS Glue Data Catalog
+ An S3 Tables bucket or S3 general purpose bucket for storing materialized view data
+ An IAM role with permissions to access AWS Glue Data Catalog and Amazon S3
+ Permissions configured using one of the following models:
  + **IAM policies only** – Your IAM role needs CreateTable permissions on the AWS Glue database and read access to base tables (GetTables on the AWS Glue catalog and read access to underlying S3 locations). No AWS Lake Formation configuration required.
  + **AWS Lake Formation** – If you already use AWS Lake Formation to govern your data lake, configure AWS Lake Formation permissions on source tables and target databases, and register your S3 bucket with AWS Lake Formation.

## Configuring Spark to use materialized views
<a name="materialized-views-configuring-spark"></a>

To create and manage materialized views in AWS Glue, configure your Spark session with the required Iceberg extensions and catalog settings. The configuration method varies depending on whether you're using AWS Glue jobs or AWS Glue Studio notebooks.

### Configuring AWS Glue jobs
<a name="materialized-views-configuring-glue-jobs"></a>

When creating or updating an AWS Glue job, add the following configuration parameters as job parameters:

#### For S3 Tables buckets
<a name="materialized-views-s3-tables-buckets"></a>

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
                  '--conf spark.sql.catalog.glue_catalog.glue.account-id=111122223333 '
                  '--conf spark.sql.catalog.s3t_catalog=org.apache.iceberg.spark.SparkCatalog '
                  '--conf spark.sql.catalog.s3t_catalog.type=glue '
                  '--conf spark.sql.catalog.s3t_catalog.glue.id=111122223333:s3tablescatalog/my-table-bucket '
                  '--conf spark.sql.catalog.s3t_catalog.glue.account-id=111122223333 '
                  '--conf spark.sql.catalog.s3t_catalog.warehouse=s3://amzn-s3-demo-bucket/mv-warehouse '
                  '--conf spark.sql.catalog.s3t_catalog.glue.region=us-east-1 '
                  '--conf spark.sql.defaultCatalog=s3t_catalog '
                  '--conf spark.sql.optimizer.answerQueriesWithMVs.enabled=true '
                  '--conf spark.sql.materializedViews.metadataCache.enabled=true'
    },
    GlueVersion='5.1'
)
```

If you use AWS Lake Formation to govern access to your data lake, add the following setting to each catalog configuration:

```
--conf spark.sql.catalog.glue_catalog.glue.lakeformation-enabled=true
```

#### For S3 general purpose buckets
<a name="materialized-views-s3-general-purpose-buckets"></a>

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
                  '--conf spark.sql.catalog.glue_catalog.glue.account-id=111122223333 '
                  '--conf spark.sql.defaultCatalog=glue_catalog '
                  '--conf spark.sql.optimizer.answerQueriesWithMVs.enabled=true '
                  '--conf spark.sql.materializedViews.metadataCache.enabled=true'
    },
    GlueVersion='5.1'
)
```

If you use AWS Lake Formation to govern access to your data lake, add the following setting to each catalog configuration:

```
--conf spark.sql.catalog.glue_catalog.glue.lakeformation-enabled=true
```

### Configuring AWS Glue Studio notebooks
<a name="materialized-views-configuring-glue-studio-notebooks"></a>

In AWS Glue Studio notebooks, configure your Spark session using the %%configure magic command at the beginning of your notebook:

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
        "spark.sql.defaultCatalog": "glue_catalog",
        "spark.sql.optimizer.answerQueriesWithMVs.enabled": "true",
        "spark.sql.materializedViews.metadataCache.enabled": "true"
    }
}
```

If you use AWS Lake Formation, add the following line to the `conf` block:

```
"spark.sql.catalog.glue_catalog.glue.lakeformation-enabled": "true"
```

### Enabling incremental refresh
<a name="materialized-views-enabling-incremental-refresh"></a>

To enable incremental refresh optimization, add the following configuration properties to your job parameters or notebook configuration:

```
--conf spark.sql.optimizer.incrementalMVRefresh.enabled=true
--conf spark.sql.optimizer.incrementalMVRefresh.deltaThresholdCheckEnabled=false
```

### Configuration parameters
<a name="materialized-views-configuration-parameters"></a>

The following configuration parameters control materialized view behavior:
+ `spark.sql.extensions` – Enables Iceberg Spark session extensions required for materialized view support.
+ `spark.sql.catalog.glue_catalog.glue.lakeformation-enabled` – Optional. Set to `true` only if you use AWS Lake Formation to govern access to your data lake. When omitted or set to `false`, IAM policies are used for authorization.
+ `spark.sql.optimizer.answerQueriesWithMVs.enabled` – Enables automatic query rewrite to use materialized views. Set to true to activate this optimization.
+ `spark.sql.materializedViews.metadataCache.enabled` – Enables caching of materialized view metadata for query optimization. Set to true to improve query rewrite performance.
+ `spark.sql.optimizer.incrementalMVRefresh.enabled` – Enables incremental refresh optimization. Set to true to process only changed data during refresh operations.
+ `spark.sql.optimizer.answerQueriesWithMVs.decimalAggregateCheckEnabled` – Controls validation of decimal aggregate operations in query rewrite. Set to false to disable certain decimal overflow checks.

## Creating materialized views
<a name="materialized-views-creating"></a>

You create materialized views using the CREATE MATERIALIZED VIEW SQL statement in AWS Glue jobs or notebooks. The view definition specifies the transformation logic as a SQL query that references one or more source tables.

### Creating a basic materialized view in AWS Glue jobs
<a name="materialized-views-creating-basic-glue-jobs"></a>

The following example demonstrates creating a materialized view in a AWS Glue job script, use fully qualified table names with three part naming convention in view definition:

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
<a name="materialized-views-creating-automatic-refresh"></a>

To configure automatic refresh, specify a refresh schedule when creating the view, using fully qualified table names with three part naming convention in view definition:

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
<a name="materialized-views-creating-cross-catalog"></a>

When your source tables are in a different catalog than your materialized view, use fully qualified table names with three-part naming convention in both view name and view definition:

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
<a name="materialized-views-creating-glue-studio-notebooks"></a>

In AWS Glue Studio notebooks, you can use the %%sql magic command to create materialized views, using fully qualified table names with three part naming convention in view definition:

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
<a name="materialized-views-querying"></a>

After creating a materialized view, you can query it like any other table using standard SQL SELECT statements in your AWS Glue jobs or notebooks.

### Querying in AWS Glue jobs
<a name="materialized-views-querying-glue-jobs"></a>

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
<a name="materialized-views-querying-glue-studio-notebooks"></a>

```
%%sql
SELECT * FROM customer_orders
```

### Automatic query rewrite
<a name="materialized-views-automatic-query-rewrite"></a>

When automatic query rewrite is enabled, the Spark optimizer analyzes your queries and automatically uses materialized views when they can improve performance. For example, if you execute the following query:

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

The Spark optimizer automatically rewrites this query to use the customer\_orders materialized view instead of processing the base orders table, provided the materialized view is current.

### Verifying automatic query rewrite
<a name="materialized-views-verifying-automatic-query-rewrite"></a>

To verify whether a query uses automatic query rewrite, use the EXPLAIN EXTENDED command:

```
spark.sql("""
    EXPLAIN EXTENDED
    SELECT customer_name, COUNT(*) as order_count, SUM(amount) as total_amount 
    FROM orders
    GROUP BY customer_name
""").show(truncate=False)
```

In the execution plan, look for the materialized view name in the BatchScan operation. If the plan shows BatchScan glue\_catalog.analytics.customer\_orders instead of BatchScan glue\_catalog.sales.orders, the query has been automatically rewritten to use the materialized view.

Note that automatic query rewrite requires time for the Spark metadata cache to populate after creating a materialized view. This process typically completes within 30 seconds.

## Refreshing materialized views
<a name="materialized-views-refreshing"></a>

You can refresh materialized views using two methods: full refresh or incremental refresh. Full refresh recomputes the entire materialized view from all base table data, while incremental refresh processes only the data that has changed since the last refresh.

### Manual full refresh in AWS Glue jobs
<a name="materialized-views-manual-full-refresh-glue-jobs"></a>

To perform a full refresh of a materialized view:

```
spark.sql("REFRESH MATERIALIZED VIEW customer_orders FULL")

# Verify updated results
result = spark.sql("SELECT * FROM customer_orders")
result.show()
```

### Manual incremental refresh in AWS Glue jobs
<a name="materialized-views-manual-incremental-refresh-glue-jobs"></a>

To perform an incremental refresh, ensure incremental refresh is enabled in your Spark session configuration, then execute:

```
spark.sql("REFRESH MATERIALIZED VIEW customer_orders")

# Verify updated results
result = spark.sql("SELECT * FROM customer_orders")
result.show()
```

The AWS Glue Data Catalog automatically determines whether incremental refresh is applicable based on the view definition and the amount of changed data. If incremental refresh is not possible, the operation falls back to full refresh.

### Refreshing in AWS Glue Studio notebooks
<a name="materialized-views-refreshing-glue-studio-notebooks"></a>

In notebooks, use the %%sql magic command:

```
%%sql
REFRESH MATERIALIZED VIEW customer_orders FULL
```

### Verifying incremental refresh execution
<a name="materialized-views-verifying-incremental-refresh"></a>

To confirm that incremental refresh executed successfully, enable debug logging in your AWS Glue job:

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
<a name="materialized-views-managing"></a>

AWS Glue provides SQL commands for managing the lifecycle of materialized views in your jobs and notebooks.

### Describing a materialized view
<a name="materialized-views-describing"></a>

To view metadata about a materialized view, including its definition, refresh status, and last refresh timestamp:

```
spark.sql("DESCRIBE EXTENDED customer_orders").show(truncate=False)
```

### Altering a materialized view
<a name="materialized-views-altering"></a>

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
<a name="materialized-views-dropping"></a>

To delete a materialized view:

```
spark.sql("DROP MATERIALIZED VIEW customer_orders")
```

This command removes the materialized view definition from the AWS Glue Data Catalog and deletes the underlying Iceberg table data from your S3 bucket.

### Listing materialized views
<a name="materialized-views-listing"></a>

To list all materialized views in a database:

```
spark.sql("SHOW VIEWS FROM analytics").show()
```

## Permissions for materialized views
<a name="materialized-views-permissions"></a>

To create and manage materialized views, you must configure permissions for the IAM role that creates the view (the definer role). AWS Glue supports two permission models:
+ **IAM policies only** – If you manage your AWS Glue Data Catalog tables with IAM policies, no AWS Lake Formation configuration is required.
+ **AWS Lake Formation** – If you already use AWS Lake Formation to govern your data lake, you can configure AWS Lake Formation permissions for materialized views.

### Required permissions for the definer role
<a name="materialized-views-required-permissions-definer-role"></a>

**If using IAM policies only:**

The definer role must have the following IAM permissions:
+ On the AWS Glue Data Catalog – GetTable, GetTables, and CreateTable API permissions
+ On the target database – CreateTable permission
+ On source table S3 locations – Read access (s3:GetObject, s3:ListBucket)

When you create a materialized view, the definer role's ARN is stored in the view definition. The AWS Glue Data Catalog assumes this role when executing automatic refresh operations. If the definer role loses access to source tables, refresh operations will fail until permissions are restored.

**If using AWS Lake Formation:**

The definer role must have the following AWS Lake Formation permissions:
+ On source tables – SELECT or ALL permissions without row, column, or cell filters
+ On the target database – CREATE\_TABLE permission
+ On the AWS Glue Data Catalog – GetTable and CreateTable API permissions

When you create a materialized view, the definer role's ARN is stored in the view definition. The AWS Glue Data Catalog assumes this role when executing automatic refresh operations. If the definer role loses access to source tables, refresh operations will fail until permissions are restored.

### IAM permissions for AWS Glue jobs
<a name="materialized-views-iam-permissions-glue-jobs"></a>

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
        }
    ]
}
```

If you use AWS Lake Formation, also add the following permission:

```
{
    "Effect": "Allow",
    "Action": [
        "lakeformation:GetDataAccess"
    ],
    "Resource": "*"
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

To let AWS Glue automatically refresh the materialized view for you, the role must also have the following trust policy that enables the service to assume the role.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
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
<a name="materialized-views-granting-access"></a>

**If using IAM policies only:**

Any IAM identity with GetTable permission on the materialized view can query it. Users can query the materialized view without requiring direct access to the underlying source tables.

**If using AWS Lake Formation:**

To grant other users access to query a materialized view, use AWS Lake Formation to grant SELECT permission on the materialized view table. Users can query the materialized view without requiring direct access to the underlying source tables.

For detailed information about configuring AWS Lake Formation permissions, see Granting and revoking permissions on Data Catalog resources in the AWS Lake Formation Developer Guide.

## Monitoring materialized view operations
<a name="materialized-views-monitoring"></a>

The AWS Glue Data Catalog publishes metrics and logs for materialized view refresh operations to Amazon CloudWatch. You can monitor refresh status, duration, and data volume processed through CloudWatch metrics.

### Viewing job logs
<a name="materialized-views-viewing-job-logs"></a>

To view logs for AWS Glue jobs that create or refresh materialized views:

1. Open the AWS Glue console.

1. Choose Jobs from the navigation pane.

1. Select your job and choose Runs.

1. Select a specific run and choose Logs to view CloudWatch logs.

### Setting up alarms
<a name="materialized-views-setting-up-alarms"></a>

To receive notifications when refresh operations fail or exceed expected duration, create CloudWatch alarms on materialized view metrics. You can also configure Amazon EventBridge rules to trigger automated responses to refresh events.

## Example: Complete workflow
<a name="materialized-views-complete-workflow"></a>

The following example demonstrates a complete workflow for creating and using a materialized view in AWS Glue.

### Example AWS Glue job script
<a name="materialized-views-example-glue-job-script"></a>

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
<a name="materialized-views-example-glue-studio-notebook"></a>

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
<a name="materialized-views-considerations-limitations"></a>

Consider the following when using materialized views with AWS Glue:
+ Materialized views require AWS Glue version 5.1 or later.
+ Source tables must be Apache Iceberg or Apache Hive tables registered in the AWS Glue Data Catalog. Apache Hudi and Linux Foundation Delta Lake tables are not supported at launch.
+ Source tables must reside in the same Region and account as the materialized view.
+ Materialized views cannot reference AWS Glue Data Catalog views, multi-dialect views, or other materialized views as source tables.
+ The view definer role must have full read access on all source tables. For customers using IAM policies, this means GetTables permission on the AWS Glue catalog and read access to underlying S3 locations. For customers using AWS Lake Formation, this means SELECT or ALL permission without row, column, or cell filters applied.
+ Materialized views are eventually consistent with source tables. During the refresh window, queries may return stale data. Execute manual refresh for immediate consistency.
+ The minimum automatic refresh interval is one hour.
+ Incremental refresh supports a restricted subset of SQL operations. The view definition must be a single SELECT-FROM-WHERE-GROUP BY-HAVING block and cannot contain set operations, subqueries, the DISTINCT keyword in SELECT or aggregate functions, window functions, or joins other than INNER JOIN.
+ Incremental refresh does not support user-defined functions or certain built-in functions. Only a subset of Spark SQL built-in functions are supported.
+ Query automatic rewrite only considers materialized views whose definitions belong to a restricted SQL subset similar to incremental refresh restrictions.
+ Identifiers containing special characters other than alphanumeric characters and underscores are not supported in CREATE MATERIALIZED VIEW queries. This applies to all identifier types including catalog/namespace/table names, column and struct field names, CTEs, and aliases.
+ Materialized view columns starting with the \_\_ivm prefix are reserved for system use. Amazon reserves the right to modify or remove these columns in future releases.
+ The SORT BY, LIMIT, OFFSET, CLUSTER BY, and ORDER BY clauses are not supported in materialized view definitions.
+ Cross-Region and cross-account source tables are not supported.
+ Tables referenced in the view query must use three-part naming convention (e.g., glue\_catalog.my\_db.my\_table) because automatic refresh does not use default catalog and database settings.
+ Full refresh operations override the entire table and make previous snapshots unavailable.
+ Non-deterministic functions such as rand() or current\_timestamp() are not supported in materialized view definitions.
+ AWS Lake Formation fine-grained access control (row-level security, column-level security, cell-level security) on materialized views is not currently supported.