

# Querying S3 Storage Lens data with analytics tools
<a name="storage-lens-s3-tables-querying"></a>

Before you can query S3 Storage Lens data exported to S3 Tables using AWS analytics services like Amazon Athena or Amazon EMR, you must enable analytics integration on the AWS-managed `aws-s3` table bucket and configure AWS Lake Formation permissions.

**Important**  
Enabling analytics integration on the "aws-s3" table bucket is a required step that is often missed. Without this configuration, you will not be able to query your S3 Storage Lens tables using AWS analytics services.

## Prerequisites
<a name="storage-lens-s3-tables-querying-prerequisites"></a>

Before you begin, ensure that you have:
+ An S3 Storage Lens configuration with S3 Tables export enabled. For more information, see [Exporting S3 Storage Lens metrics to S3 Tables](storage-lens-s3-tables-export.md) .
+ Access to Amazon Athena or another analytics service.
+ Waited 24-48 hours after enabling export for the first data to be available.

## Integration overview
<a name="storage-lens-s3-tables-querying-integration-overview"></a>

For detailed information about integrating S3 Tables with AWS analytics services, including prerequisites, IAM role configuration, and step-by-step procedures, see [Integrating Amazon S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html). 

After you enable S3 Tables export and set up analytics integration, you can query your S3 Storage Lens data using AWS analytics services such as Amazon Athena, Amazon Redshift, and Amazon EMR. This enables you to perform custom analysis, create dashboards, and derive insights from your storage data using standard SQL.

## Querying with Amazon Athena
<a name="storage-lens-s3-tables-querying-athena"></a>

Amazon Athena is a serverless interactive query service that makes it easy to analyze data using standard SQL. Use the following steps to query S3 Storage Lens data in Athena.

**Note**  
In all query examples, replace `lens_my-config_exp` with your actual Storage Lens configuration namespace. For more information about namespace naming, see [Table naming for S3 Storage Lens export to S3 Tables](storage-lens-s3-tables-naming.md) .

### Example: Query top storage consumers
<a name="storage-lens-s3-tables-querying-athena-top-consumers"></a>

The following query identifies the top 10 buckets by storage consumption:

```
SELECT 
    bucket_name,
    storage_class,
    SUM(storage_bytes) / POWER(1024, 3) AS storage_gb,
    SUM(object_count) AS objects
FROM "s3tablescatalog/aws-s3"."lens_my-config_exp"."default_storage_metrics"
WHERE report_time = (
    SELECT MAX(report_time) 
    FROM "s3tablescatalog/aws-s3"."lens_my-config_exp"."default_storage_metrics"
)
    AND record_type = 'BUCKET'
    AND bucket_name != ''
GROUP BY bucket_name, storage_class
ORDER BY storage_gb DESC
LIMIT 10
```

### Example: Analyze storage growth over time
<a name="storage-lens-s3-tables-querying-athena-growth"></a>

The following query analyzes storage growth over the last 30 days:

```
SELECT 
    CAST(report_time AS date) AS report_date,
    SUM(storage_bytes) / POWER(1024, 3) AS total_storage_gb
FROM "s3tablescatalog/aws-s3"."lens_my-config_exp"."default_storage_metrics"
WHERE report_time >= current_date - interval '30' day
    AND record_type = 'ACCOUNT'
GROUP BY CAST(report_time AS date)
ORDER BY report_date DESC;
```

### Example: Identify incomplete multipart uploads
<a name="storage-lens-s3-tables-querying-athena-mpu"></a>

The following query finds buckets with incomplete multipart uploads older than 7 days:

```
SELECT 
    bucket_name,
    SUM(incomplete_mpu_storage_older_than_7_days_bytes) / POWER(1024, 3) AS wasted_storage_gb,
    SUM(incomplete_mpu_object_older_than_7_days_count) AS wasted_objects
FROM "s3tablescatalog/aws-s3"."lens_my-config_exp"."default_storage_metrics"
WHERE report_time = (
    SELECT MAX(report_time) 
    FROM "s3tablescatalog/aws-s3"."lens_my-config_exp"."default_storage_metrics"
)
    AND record_type = 'BUCKET'
    AND incomplete_mpu_storage_older_than_7_days_bytes > 0
GROUP BY bucket_name
ORDER BY wasted_storage_gb DESC;
```

### Example: Find cold data candidates
<a name="storage-lens-s3-tables-querying-athena-cold-data"></a>

The following query identifies prefixes with no activity in the last 100 days that are stored in hot storage tiers:

```
WITH recent_activity AS (
    SELECT DISTINCT 
        bucket_name,
        record_value AS prefix_path
    FROM "s3tablescatalog/aws-s3"."lens_my-config_exp"."expanded_prefixes_activity_metrics"
    WHERE report_time >= current_date - interval '100' day
        AND record_type = 'PREFIX'
        AND all_request_count > 0
)
SELECT 
    s.bucket_name,
    s.record_value AS prefix_path,
    s.storage_class,
    SUM(s.storage_bytes) / POWER(1024, 3) AS storage_gb
FROM "s3tablescatalog/aws-s3"."lens_my-config_exp"."expanded_prefixes_storage_metrics" s
LEFT JOIN recent_activity r 
    ON s.bucket_name = r.bucket_name 
    AND s.record_value = r.prefix_path
WHERE s.report_time = (
    SELECT MAX(report_time) 
    FROM "s3tablescatalog/aws-s3"."lens_my-config_exp"."expanded_prefixes_storage_metrics"
)
    AND s.record_type = 'PREFIX'
    AND s.storage_class IN ('STANDARD', 'REDUCED_REDUNDANCY')
    AND s.storage_bytes > 1073741824  -- > 1GB
    AND r.prefix_path IS NULL  -- No recent activity
GROUP BY s.bucket_name, s.record_value, s.storage_class
ORDER BY storage_gb DESC
LIMIT 20;
```

### Example: Analyze request patterns
<a name="storage-lens-s3-tables-querying-athena-requests"></a>

The following query analyzes request patterns to understand access frequency:

```
SELECT 
    bucket_name,
    SUM(all_request_count) AS total_requests,
    SUM(get_request_count) AS get_requests,
    SUM(put_request_count) AS put_requests,
    ROUND(100.0 * SUM(get_request_count) / NULLIF(SUM(all_request_count), 0), 2) AS get_percentage,
    SUM(downloaded_bytes) / POWER(1024, 3) AS downloaded_gb
FROM "s3tablescatalog/aws-s3"."lens_my-config_exp"."default_activity_metrics"
WHERE report_time >= current_date - interval '7' day
    AND record_type = 'BUCKET'
    AND bucket_name != ''
GROUP BY bucket_name
HAVING SUM(all_request_count) > 0
ORDER BY total_requests DESC
LIMIT 10;
```

## Querying with Apache Spark on Amazon EMR
<a name="storage-lens-s3-tables-querying-emr"></a>

Amazon EMR provides a managed Hadoop framework that makes it easy to process vast amounts of data using Apache Spark. You can use the Iceberg connector to read S3 Storage Lens tables directly.

### Read S3 Tables with Spark
<a name="storage-lens-s3-tables-querying-emr-spark"></a>

Use the following Python code to read S3 Storage Lens data with Spark:

```
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("S3StorageLensAnalysis") \
    .config("spark.sql.catalog.s3tablescatalog", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.s3tablescatalog.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog") \
    .getOrCreate()

# Read S3 Storage Lens data
df = spark.read \
    .format("iceberg") \
    .load("s3tablescatalog/aws-s3.lens_my-config_exp.default_storage_metrics")

# Analyze data
df.filter("record_type = 'BUCKET'") \
    .groupBy("bucket_name", "storage_class") \
    .sum("storage_bytes") \
    .orderBy("sum(storage_bytes)", ascending=False) \
    .show(10)
```

## Query optimization best practices
<a name="storage-lens-s3-tables-querying-optimization"></a>

Follow these best practices to optimize query performance and reduce costs:
+  **Filter by report\_time** – Always include date filters to reduce the amount of data scanned. This is especially important for tables with long retention periods.

  ```
  WHERE report_time >= current_date - interval '7' day
  ```
+  **Use record\_type filters** – Specify the appropriate aggregation level (ACCOUNT, BUCKET, PREFIX) to query only the data you need.

  ```
  WHERE record_type = 'BUCKET'
  ```
+  **Include LIMIT clauses** – Use LIMIT for exploratory queries to control result size and reduce query costs.

  ```
  LIMIT 100
  ```
+  **Filter empty records** – Use conditions to exclude empty or zero-value records.

  ```
  WHERE storage_bytes > 0
  ```
+  **Use the latest data** – When analyzing current state, filter for the most recent report\_time to avoid scanning historical data.

  ```
  WHERE report_time = (SELECT MAX(report_time) FROM table_name)
  ```

### Example optimized query pattern
<a name="storage-lens-s3-tables-querying-optimization-example"></a>

The following query demonstrates best practices for optimization:

```
SELECT 
    bucket_name,
    SUM(storage_bytes) / POWER(1024, 3) AS storage_gb
FROM "s3tablescatalog/aws-s3"."lens_my-config_exp"."default_storage_metrics"
WHERE report_time >= current_date - interval '7' day  -- Date filter
    AND record_type = 'BUCKET'                         -- Record type filter
    AND storage_bytes > 0                              -- Non-empty filter
    AND bucket_name != ''                              -- Non-empty filter
GROUP BY bucket_name
ORDER BY storage_gb DESC
LIMIT 100;                                             -- Result limit
```

## Troubleshooting
<a name="storage-lens-s3-tables-querying-troubleshooting"></a>

### Query returns no results
<a name="storage-lens-s3-tables-querying-troubleshooting-no-results"></a>

 **Problem:** Your query completes successfully but returns no results.

 **Solution:** 
+ Verify that data is available by checking the latest report\_time:

  ```
  SELECT MAX(report_time) AS latest_data
  FROM "s3tablescatalog/aws-s3"."lens_my-config_exp"."default_storage_metrics";
  ```
+ Ensure that you're using the correct namespace name. Use `SHOW TABLES IN `lens_my-config_exp`;` to list available tables.
+ Wait 24-48 hours after enabling S3 Tables export for the first data to be available.

### Access denied errors
<a name="storage-lens-s3-tables-querying-troubleshooting-access"></a>

 **Problem:** You receive access denied errors when running queries.

 **Solution:** Verify that AWS Lake Formation permissions are correctly configured. For more information, see [Integrating Amazon S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html). 

## Next steps
<a name="storage-lens-s3-tables-querying-next-steps"></a>
+ Learn about [Using AI assistants with S3 Storage Lens tables](storage-lens-s3-tables-ai-tools.md)
+ Review the [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md) for metric definitions
+ Explore [Amazon S3 Storage Lens metrics use cases](storage-lens-use-cases.md) for more analysis ideas
+ Learn about [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) for serverless querying