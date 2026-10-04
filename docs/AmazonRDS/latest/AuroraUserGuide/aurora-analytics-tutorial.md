

# Tutorial: Querying Amazon S3 data
<a name="aurora-analytics-tutorial"></a>

This tutorial walks you through setting up the analytics feature from scratch and running your first analytical query against Parquet data in Amazon S3. By the end, you will have an Aurora PostgreSQL DB cluster querying Amazon S3 data through standard SQL.

**Topics**
+ [Prerequisites](#aurora-analytics-tutorial-prerequisites)
+ [Step 1: Create the IAM policy and role](#aurora-analytics-tutorial-step-1)
+ [Step 2: Create the Aurora PostgreSQL DB cluster](#aurora-analytics-tutorial-step-2)
+ [Step 3: Attach the IAM role to the DB cluster](#aurora-analytics-tutorial-step-3)
+ [Step 4: Set up the Amazon S3 gateway VPC endpoint](#aurora-analytics-tutorial-step-4)
+ [Step 5: Connect and install the extension](#aurora-analytics-tutorial-step-5)
+ [Step 6: Create a foreign table](#aurora-analytics-tutorial-step-6)
+ [Step 7: Run your first query](#aurora-analytics-tutorial-step-7)
+ [Step 8: Join with a local PostgreSQL table](#aurora-analytics-tutorial-step-8)
+ [Step 9: Materialize results into PostgreSQL](#aurora-analytics-tutorial-step-9)
+ [Step 10: Check cache and performance](#aurora-analytics-tutorial-step-10)
+ [Clean up](#aurora-analytics-tutorial-cleanup)
+ [Next steps](#aurora-analytics-tutorial-next-steps)

## Prerequisites
<a name="aurora-analytics-tutorial-prerequisites"></a>

Before you begin, make sure you have the following:
+ An AWS account with permissions to create IAM roles, Amazon RDS clusters, and VPC endpoints.
+ The AWS CLI installed and configured.
+ A VPC with at least two subnets in different Availability Zones, a DB subnet group, and a security group for Aurora.
+ Parquet data files in an Amazon S3 bucket. If you don't have data yet, you can upload a sample file (this tutorial uses an example orders dataset).

## Step 1: Create the IAM policy and role
<a name="aurora-analytics-tutorial-step-1"></a>

Create an IAM policy that grants the extension read access to your Amazon S3 bucket, then create a role and attach the policy.

To create the IAM policy:

```
aws iam create-policy \
  --policy-name AuroraAnalyticsReadAccess \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "S3Access",
        "Effect": "Allow",
        "Action": ["s3:ListBucket", "s3:GetObject", "s3:GetBucketLocation"],
        "Resource": ["arn:aws:s3:::your-data-bucket", "arn:aws:s3:::your-data-bucket/*"]
      }
    ]
  }'
```

To create the IAM role and attach the policy:

```
aws iam create-role \
  --role-name AuroraAnalyticsRole \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {"Service": "rds.amazonaws.com"},
        "Action": "sts:AssumeRole"
      }
    ]
  }'

aws iam attach-role-policy \
  --role-name AuroraAnalyticsRole \
  --policy-arn arn:aws:iam::<account-id>:policy/AuroraAnalyticsReadAccess
```

## Step 2: Create the Aurora PostgreSQL DB cluster
<a name="aurora-analytics-tutorial-step-2"></a>

Create a DB cluster parameter group, then create the DB cluster and a DB instance.

To create the parameter group with the feature enabled:

```
aws rds create-db-cluster-parameter-group \
  --db-cluster-parameter-group-name my-analytics-params \
  --db-parameter-group-family aurora-postgresql17 \
  --description "Parameter group with aurora_analytics enabled"

aws rds modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name my-analytics-params \
  --parameters "ParameterName=aurora_analytics.enabled,ParameterValue=true,ApplyMethod=immediate"
```

To create the DB cluster:

```
aws rds create-db-cluster \
  --db-cluster-identifier my-analytics-cluster \
  --engine aurora-postgresql \
  --engine-version 17.11 \
  --master-username postgres \
  --master-user-password <password> \
  --db-cluster-parameter-group-name my-analytics-params \
  --db-subnet-group-name <subnet-group> \
  --vpc-security-group-ids <security-group-id>
```

To create a DB instance:

```
aws rds create-db-instance \
  --db-instance-identifier my-analytics-instance-1 \
  --db-cluster-identifier my-analytics-cluster \
  --db-instance-class db.r8gd.xlarge \
  --engine aurora-postgresql
```

Wait for the DB instance to become available:

```
aws rds wait db-instance-available \
  --db-instance-identifier my-analytics-instance-1
```

## Step 3: Attach the IAM role to the DB cluster
<a name="aurora-analytics-tutorial-step-3"></a>

```
aws rds add-role-to-db-cluster \
  --db-cluster-identifier my-analytics-cluster \
  --role-arn arn:aws:iam::<account-id>:role/AuroraAnalyticsRole \
  --feature-name AuroraAnalytics
```

## Step 4: Set up the Amazon S3 gateway VPC endpoint
<a name="aurora-analytics-tutorial-step-4"></a>

If your Aurora DB cluster is in a private subnet, create an Amazon S3 gateway endpoint:

```
aws ec2 create-vpc-endpoint \
  --vpc-id <vpc-id> \
  --service-name com.amazonaws.<region>.s3 \
  --route-table-ids <route-table-id>
```

## Step 5: Connect and install the extension
<a name="aurora-analytics-tutorial-step-5"></a>

Connect to your Aurora PostgreSQL DB cluster using psql:

```
psql --host=my-analytics-cluster.<region>.rds.amazonaws.com \
     --port=5432 --username=postgres --password
```

Install the `aurora_analytics` extension:

```
CREATE EXTENSION aurora_analytics;
```

Verify the installation:

```
SELECT extname, extversion FROM pg_extension WHERE extname = 'aurora_analytics';
```

Expected output:

```
     extname      | extversion
------------------+------------
 aurora_analytics | 1.0
```

Verify the foreign server was created:

```
SELECT srvname FROM pg_foreign_server WHERE srvname = 'aurora_analytics_server';
```

## Step 6: Create a foreign table
<a name="aurora-analytics-tutorial-step-6"></a>

Create a foreign table that points to your Parquet data in Amazon S3. Using empty parentheses () lets Aurora PostgreSQL auto-infer the schema from the Parquet metadata:

```
CREATE FOREIGN TABLE ft_orders ()
SERVER aurora_analytics_server
OPTIONS (
    location 's3://your-data-bucket/data/orders/',
    format 'parquet',
    region 'us-east-1'
);
```

Check the inferred schema:

```
\d ft_orders
```

## Step 7: Run your first query
<a name="aurora-analytics-tutorial-step-7"></a>

```
-- Count all rows
SELECT COUNT(*) FROM ft_orders;

-- Aggregation with filter
SELECT
    status,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_order_value
FROM ft_orders
WHERE order_date >= '2024-01-01'
GROUP BY status
ORDER BY total_revenue DESC;
```

## Step 8: Join with a local PostgreSQL table
<a name="aurora-analytics-tutorial-step-8"></a>

Create a local table and join it with your foreign table:

```
-- Create a local dimension table
CREATE TABLE customer_segments (
    customer_id BIGINT PRIMARY KEY,
    segment TEXT,
    region TEXT
);

INSERT INTO customer_segments VALUES
    (1, 'VIP', 'US-West'),
    (2, 'Premium', 'US-East'),
    (3, 'Regular', 'EU-West');

-- Join local table with S3 data
SELECT
    cs.segment,
    cs.region,
    COUNT(*) AS order_count,
    SUM(o.total_amount) AS total_revenue
FROM ft_orders o
JOIN customer_segments cs ON o.customer_id = cs.customer_id
WHERE o.order_date >= '2024-01-01'
GROUP BY cs.segment, cs.region
ORDER BY total_revenue DESC;
```

## Step 9: Materialize results into PostgreSQL
<a name="aurora-analytics-tutorial-step-9"></a>

Store query results from Amazon S3 as a local PostgreSQL table for fast repeated access:

```
CREATE TABLE monthly_revenue AS
SELECT
    DATE_TRUNC('month', order_date) AS month,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_order_value
FROM ft_orders
WHERE order_date >= '2024-01-01'
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;

-- Query the materialized result (fast, local PostgreSQL)
SELECT * FROM monthly_revenue;
```

## Step 10: Check cache and performance
<a name="aurora-analytics-tutorial-step-10"></a>

After running queries, verify that the cache is working:

```
-- Check cache size (should be non-zero after queries)
SELECT pg_size_pretty(aurora_analytics_cache_size()) AS cache_size;

-- Check per-query statistics
SELECT query,
       pg_size_pretty(analytics_cache_hit_bytes) AS cache_hits,
       pg_size_pretty(analytics_remote_read_bytes) AS s3_reads
FROM aurora_analytics_stat_statements()
WHERE analytics_cache_hit_bytes > 0 OR analytics_remote_read_bytes > 0;
```

Run the same query again and notice the improvement: the second execution reads from cache instead of Amazon S3.

## Clean up
<a name="aurora-analytics-tutorial-cleanup"></a>

To avoid ongoing charges, delete the resources you created:

```
-- Drop the foreign table
DROP FOREIGN TABLE ft_orders;
DROP TABLE customer_segments;
DROP TABLE monthly_revenue;
```

```
aws rds delete-db-instance --db-instance-identifier my-analytics-instance-1 --skip-final-snapshot
aws rds delete-db-cluster --db-cluster-identifier my-analytics-cluster --skip-final-snapshot
aws iam detach-role-policy --role-name AuroraAnalyticsRole --policy-arn arn:aws:iam::<account-id>:policy/AuroraAnalyticsReadAccess
aws iam delete-role --role-name AuroraAnalyticsRole
aws iam delete-policy --policy-arn arn:aws:iam::<account-id>:policy/AuroraAnalyticsReadAccess
```

## Next steps
<a name="aurora-analytics-tutorial-next-steps"></a>

Now that you've completed the tutorial, explore the following topics:
+ [Working with foreign tables](aurora-analytics-foreign-tables.md): Learn about Iceberg tables, time travel with snapshot and timestamp, and schema management.
+ [Configuration parameters](aurora-analytics-configuration-parameters.md): Tune `query_mem` for your workload.
+ [Best practices](aurora-analytics-best-practices.md): Optimize data layout, instance sizing, and concurrency.
+ [Monitoring and troubleshooting](aurora-analytics-monitoring-troubleshooting.md): Metrics, wait events, and diagnosing issues.