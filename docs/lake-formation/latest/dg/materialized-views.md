# Materialized views

###### Topics

- [Differentiating materialized
  views from other view types](#materialized-views-differentiating "#materialized-views-differentiating")
- [Use cases](#materialized-views-use-cases "#materialized-views-use-cases")
- [Key concepts](#materialized-views-key-concepts "#materialized-views-key-concepts")
- [Permissions for materialized views](#materialized-views-permissions "#materialized-views-permissions")
- [Creating and managing
  materialized views](#materialized-views-creating-managing "#materialized-views-creating-managing")
- [Storage and data access](#materialized-views-storage-access "#materialized-views-storage-access")
- [Integrating with AWS Lake Formation
  permissions](#materialized-views-lake-formation "#materialized-views-lake-formation")
- [Monitoring and
  debugging](#materialized-views-monitoring-debugging "#materialized-views-monitoring-debugging")
- [Managing refresh
  jobs](#materialized-views-managing-refresh-jobs "#materialized-views-managing-refresh-jobs")
- [Monitoring and
  troubleshooting](#materialized-views-monitoring-troubleshooting "#materialized-views-monitoring-troubleshooting")
- [Considerations and
  limitations](#materialized-views-considerations-limitations "#materialized-views-considerations-limitations")
  In the AWS Glue Data Catalog, a materialized view is a managed table that
  stores the precomputed result of a SQL query in Apache Iceberg format. Unlike standard
  Data Catalog views that execute the query each time they are accessed, materialized
  views physically store the query results and update them as the underlying source tables
  change. You can create materialized views using Apache Spark version 3.5.6+ in
  Amazon Athena, Amazon EMR, or AWS Glue.

Materialized views reference Apache Iceberg tables registered in the
AWS Glue Data Catalog, with precomputed data stored as Apache Iceberg tables
in Amazon S3 Tables buckets or Amazon S3 general purpose buckets, making them accessible
from multiple query engines including Amazon Athena, Amazon Redshift, and third-party
Iceberg-compatible engines.

## Differentiating materialized

views from other view types

Materialized views differ from AWS Glue Data Catalog views, Apache
Spark views, and Amazon Athena views in fundamental ways. While Data Catalog views are
virtual tables that execute the SQL query definition each time they are accessed,
materialized views physically store precomputed query results. This eliminates
redundant computation and significantly improves query performance for frequently
accessed complex transformations.

Materialized views also differ from traditional data transformation pipelines
built with AWS Glue ETL or custom Spark jobs. Instead of writing custom
code to handle change detection, incremental updates, and workflow orchestration,
you define materialized views using standard SQL syntax. The AWS Glue
Data Catalog automatically monitors source tables, detects changes, and refreshes
materialized views using fully managed compute infrastructure.

## Use cases

Following are important use cases for materialized views:

- Accelerate complex analytical queries
  – Create materialized views that precompute expensive joins,
  aggregations, and window functions. Spark engines automatically rewrite
  subsequent queries to use the precomputed results, reducing query latency
  and compute costs.
- Simplify data transformation pipelines
  – Replace complex ETL jobs that handle change detection, incremental
  updates, and workflow orchestration with simple SQL-based materialized view
  definitions. The AWS Glue Data Catalog manages all operational
  complexity automatically.
- Enable self-service analytics with governed data
  access – Create curated materialized views that transform
  raw data into business-ready datasets. Grant users access to materialized
  views without exposing underlying source tables, simplifying security
  management while empowering self-service analytics.
- Optimize feature engineering for machine
  learning – Define materialized views that implement
  feature transformations for ML models. The automatic refresh capability
  ensures feature stores remain current as source data evolves, while
  incremental refresh minimizes compute costs.
- Implement efficient data sharing –
  Create materialized views that filter and transform data for specific
  consumers. Share materialized views across accounts and regions using
  AWS Lake Formation, eliminating the need for data duplication while maintaining
  centralized governance.

## Key concepts

### Automatic refresh

Automatic refresh is a capability that continuously monitors your source
tables and updates materialized views according to a schedule you define. When
you create a materialized view, you can specify a refresh frequency using
time-based scheduling with intervals as frequent as one hour. The
AWS Glue Data Catalog uses managed Spark compute infrastructure to
execute refresh operations in the background, transparently handling all aspects
of change detection and incremental updates.

When source data changes between refresh intervals, the materialized view
becomes temporarily stale. Queries directly accessing the materialized view may
return outdated results until the next scheduled refresh completes. For
scenarios requiring immediate access to the most current data, you can execute a
manual refresh using the `REFRESH MATERIALIZED VIEW` SQL
command.

### Incremental

refresh

Incremental refresh is an optimization technique that processes only the data
that has changed in source tables since the last refresh, rather than
recomputing the entire materialized view. The AWS Glue Data Catalog
leverages Apache Iceberg's metadata layer to efficiently track changes in source
tables and determine which portions of the materialized view require
updates.

This approach significantly reduces compute costs and refresh duration
compared to full refresh operations, particularly for large datasets where only
a small percentage of data changes between refresh cycles. The incremental
refresh mechanism operates automatically; you don't need to write custom logic
to detect or process changed data.

### Automatic query

rewrite

Automatic query rewrite is a query optimization capability available in Spark
engines across Amazon Athena, Amazon EMR, and AWS Glue. When you execute a
query against base tables, the Spark optimizer analyzes your query plan and
automatically determines whether available materialized views can satisfy the
query more efficiently. If a suitable materialized view exists, the optimizer
transparently rewrites the query to use the precomputed results instead of
processing the base tables.

This optimization occurs without requiring any changes to your application
code or query statements. The Spark optimizer ensures that automatic query
rewrite only applies when the materialized view is current and can produce
accurate results. If a materialized view is stale or doesn't fully match the
query requirements, the optimizer executes the original query plan against base
tables, prioritizing correctness over performance.

### View definer role

A materialized view operates based on the permissions of the IAM role that
created it, known as the view definer role. The definer role must have read
access to all base tables referenced in the materialized view definition and
create table permissions on the target database. When the AWS Glue
Data Catalog refreshes a materialized view, it assumes the definer role to
access source tables and write updated results.

This security model enables you to grant users access to materialized views
without granting them direct permissions on the underlying source tables. If the
view definer role loses access to any base table, subsequent refresh operations
will fail until permissions are restored.

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

## Creating and managing

materialized views

You create materialized views using the `CREATE MATERIALIZED VIEW` SQL
statement in Spark engines. The view definition specifies the SQL query that defines
the transformation logic, the target database and table name, and optional refresh
configuration. You can define complex transformations including aggregations, joins
across multiple tables, filters, and window functions.

```
CREATE MATERIALIZED VIEW sales_summary
AS
SELECT
    region,
    product_category,
    SUM(sales_amount) as total_sales,
    COUNT(DISTINCT customer_id) as unique_customers
FROM sales_transactions
WHERE transaction_date >= current_date - interval '90' day
GROUP BY region, product_category;
```

To configure automatic refresh, include the refresh schedule in your view
definition:

```

CREATE MATERIALIZED VIEW sales_summary
SCHEDULE REFRESH EVERY 1 HOUR
AS
SELECT region, product_category, SUM(sales_amount) as total_sales
FROM sales_transactions
GROUP BY region, product_category;

```

You can manually refresh a materialized view at any time using the `REFRESH
 MATERIALIZED VIEW` command:

```
REFRESH MATERIALIZED VIEW sales_summary;
```

To modify an existing materialized view's refresh schedule, use the `ALTER
 MATERIALIZED VIEW` statement:

```
ALTER MATERIALIZED VIEW sales_summary
ADD SCHEDULE REFRESH EVERY 2 HOURS;
```

### Nested materialized views

You can create materialized views that reference other materialized views as
base tables, enabling multi-stage data transformations. When you create nested
materialized views, the AWS Glue Data Catalog tracks dependencies and
automatically propagates updates through the materialized view hierarchy. When a
base materialized view refreshes, all downstream materialized views that depend
on it are updated accordingly.

This capability allows you to decompose complex transformations into logical
stages, improving maintainability and enabling selective refresh of
transformation layers based on your data freshness requirements.

## Storage and data access

Materialized views store precomputed results as Apache Iceberg tables in S3 Tables
buckets or general purpose S3 buckets within your AWS account. The
AWS Glue Data Catalog manages all aspects of Iceberg table maintenance,
including compaction and snapshot retention, through S3 Tables' automated
optimization capabilities.

Because materialized views are stored as Iceberg tables, you can read them
directly from any Iceberg-compatible engine, including Amazon Athena, Amazon Redshift, and
third-party analytics platforms. This multi-engine accessibility ensures your
precomputed data remains accessible across your entire analytics ecosystem without
data duplication or format conversion.

## Integrating with AWS Lake Formation

permissions

You can use AWS Lake Formation to manage fine-grained permissions on materialized views. The
view creator automatically becomes the owner of the materialized view and can grant
other users or roles permissions using AWS Lake Formation's named resource method or
LF-Tags.

When you grant a user `SELECT` permission on a materialized view, they
can query the precomputed results without requiring access to the underlying source
tables. This security model simplifies data access management and enables you to
implement the principle of least privilege, providing users with access to only the
specific data transformations they need.

You can share materialized views across AWS accounts, AWS organizations, and
organizational units using AWS Lake Formation's cross-account sharing capabilities. You can
also access materialized views across AWS Regions using resource links, enabling
centralized data governance with distributed data access.

## Monitoring and

debugging

The AWS Glue Data Catalog publishes all materialized view refresh
operations and associated metrics to Amazon CloudWatch. You can monitor refresh start time,
end time, duration, data volume processed, and refresh status through CloudWatch metrics.
When refresh operations fail, error messages and diagnostic information are captured
in CloudWatch Logs.

You can set up CloudWatch alarms to receive notifications when refresh jobs exceed
expected duration or fail repeatedly. The AWS Glue Data Catalog also
publishes change events to for both successful and failed refresh runs,
enabling you to integrate materialized view operations into broader workflow
automation.

To check the current status of a materialized view, use the `DESCRIBE
 MATERIALIZED VIEW` SQL command, which returns metadata including staleness
status, last refresh timestamp, and refresh schedule configuration.

## Managing refresh

jobs

### Starting a manual

refresh

Trigger an immediate refresh outside the scheduled interval.

Required Permission: The AWS credentials used to make the API call must have
`glue:GetTable` permission for the materialized view.

For S3 Tables Catalog:

```
aws glue start-materialized-view-refresh-task-run \
    --catalog-id <ACCOUNT_ID>:s3tablescatalog/<CATALOG_NAME> \
    --database-name <DATABASE_NAME> \
    --table-name <MV_TABLE_NAME>
```

For Root Catalog:

```
aws glue start-materialized-view-refresh-task-run \
    --catalog-id <ACCOUNT_ID> \
    --database-name <DATABASE_NAME> \
    --table-name <MV_TABLE_NAME>
```

### Checking refresh

status

Get the status of a specific refresh job:

```
aws glue get-materialized-view-refresh-task-run \
    --catalog-id <CATALOG_ID> \
    --materialized-view-refresh-task-run-id <TASK_RUN_ID>
```

### Listing refresh

history

View all refresh jobs for a materialized view:

```
aws glue list-materialized-view-refresh-task-runs \
    --catalog-id <CATALOG_ID> \
    --database-name <DATABASE_NAME> \
    --table-name <MV_TABLE_NAME>
```

###### Note

Use `<ACCOUNT_ID>:s3tablescatalog/<CATALOG_NAME>`
for S3 Tables or `<ACCOUNT_ID>` for root catalog.

### Stopping a running

refresh

Cancel an in-progress refresh job:

```
aws glue stop-materialized-view-refresh-task-run \
    --catalog-id <CATALOG_ID> \
    --database-name <DATABASE_NAME> \
    --table-name <MV_TABLE_NAME>
```

## Monitoring and

troubleshooting

There are three ways to monitor materialized view refresh jobs:

### CloudWatch Metrics

View aggregated metrics for all your materialized view refresh jobs in
CloudWatch:

Available Metrics:

- AWS/Glue namespace with dimensions:
  - CatalogId: Your catalog identifier
  - DatabaseName: Database containing the materialized view
  - TableName: Materialized view name
  - TaskType: Set to "MaterializedViewRefresh"

Viewing in Console:

1. Navigate to CloudWatch Console → Metrics
2. Select AWS/Glue namespace
3. Filter by dimensions: CatalogId, DatabaseName, TableName,
   TaskType
4. View metrics for job success, failure, and duration

Example CloudWatch Metrics Query:

```
{AWS/Glue,CatalogId,DatabaseName,TableName,TaskType} MaterializedViewRefresh
```

Using AWS CLI:

```
aws cloudwatch get-metric-statistics \
    --namespace AWS/Glue \
    --metric-name <MetricName> \
    --dimensions Name=CatalogId,Value=<CATALOG_ID> \
                 Name=DatabaseName,Value=<DATABASE_NAME> \
                 Name=TableName,Value=<TABLE_NAME> \
                 Name=TaskType,Value=MaterializedViewRefresh \
    --start-time <START_TIME> \
    --end-time <END_TIME> \
    --period 3600 \
    --statistics Sum \
    --region <REGION>
```

### CloudWatch Logs

View detailed execution logs for individual refresh task runs:

Log Group:
`/aws-glue/materialized-views/<task_run_id>`

Where `<task_run_id>` is a UUID (e.g.,
abc12345-def6-7890-ghij-klmnopqrstuv).

Viewing Logs:

```
# List log streams for a task run
aws logs describe-log-streams \
    --log-group-name /aws-glue/materialized-views/<TASK_RUN_ID> \
    --region <REGION>

# Get log events
aws logs get-log-events \
    --log-group-name /aws-glue/materialized-views/<TASK_RUN_ID> \
    --log-stream-name <LOG_STREAM_NAME> \
    --region <REGION>
```

In CloudWatch Console:

1. Navigate to CloudWatch → Log groups
2. Search for /aws-glue/materialized-views/
3. Select the log group with your task run ID
4. View detailed execution logs, errors, and Spark job output

### Notifications

Subscribe to events for real-time notifications about refresh job state
changes:

Available Event Types:

- Glue Materialized View Refresh Task Started
- Glue Materialized View Refresh Task Succeeded
- Glue Materialized View Refresh Task Failed
- Glue Materialized View Auto-Refresh Invocation Failure

Creating an Rule:

```
aws events put-rule \
    --name materialized-view-refresh-notifications \
    --event-pattern '{
        "source": ["aws.glue"],
        "detail-type": [
            "Glue Materialized View Refresh Task Started",
            "Glue Materialized View Refresh Task Succeeded",
            "Glue Materialized View Refresh Task Failed",
            "Glue Materialized View Auto-Refresh Invocation Failure"
        ]
    }' \
    --region <REGION>
```

Adding a Target (e.g., SNS Topic):

```
aws events put-targets \
    --rule materialized-view-refresh-notifications \
    --targets "Id"="1","Arn"="arn:aws:sns:<REGION>:<ACCOUNT_ID>:<TOPIC_NAME>" \
    --region <REGION>
```

### Viewing refresh

status

Check the status of your materialized view refresh jobs using the
AWS Glue API:

```
aws glue get-materialized-view-refresh-task-run \
    --catalog-id <CATALOG_ID> \
    --materialized-view-refresh-task-run-id <TASK_RUN_ID> \
    --region <REGION>
```

Or list all recent refresh runs:

```
aws glue list-materialized-view-refresh-task-runs \
    --catalog-id <CATALOG_ID> \
    --database-name <DATABASE_NAME> \
    --table-name <MV_TABLE_NAME> \
    --region <REGION>
```

This shows:

- Last refresh time
- Refresh status (SUCCEEDED, FAILED, RUNNING, STOPPED)
- Task run ID
- Error messages (if failed)

Common Refresh States:

- RUNNING: Refresh job is currently executing
- SUCCEEDED: Refresh completed successfully
- FAILED: Refresh encountered an error
- STOPPED: Refresh was manually cancelled

Troubleshooting Failed Refreshes:

If a refresh fails, check:

1. IAM Permissions: Ensure the definer role has access to all base
   tables and the materialized view location
2. Base Table Availability: Verify all referenced tables exist and are
   accessible
3. Query Validity: Confirm the SQL query is valid for Spark SQL
   dialect
4. Resource Limits: Check if you've reached concurrent refresh limits for
   your account

Use the GetMaterializedViewRefreshTaskRun API to retrieve detailed error
messages.

## Considerations and

limitations

- Materialized views can only reference Apache Iceberg tables registered in
  the AWS Glue Data Catalog as base tables.
- View creation and automatic query rewrite are available only from Spark
  engines in Apache Spark version 3.5.6 and above across Amazon Athena, Amazon EMR,
  and AWS Glue (Version 5.1).
- Materialized views are eventually consistent with base tables. During the
  refresh window, queries directly accessing the materialized view may return
  outdated data. For immediate access to current data, execute a manual
  refresh.
- The minimum automatic refresh interval is one hour. For use cases
  requiring more frequent updates, execute manual refreshes programmatically
  using the `REFRESH MATERIALIZED VIEW` command.
- Query rewrite prioritizes correctness over performance. If a materialized
  view is stale or cannot satisfy query requirements accurately, Spark engines
  execute the original query against base tables.
