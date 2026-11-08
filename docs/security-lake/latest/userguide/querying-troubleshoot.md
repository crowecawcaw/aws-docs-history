

# Troubleshooting querying in Amazon Athena
<a name="querying-troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when using Athena to query objects that are stored in your Security Lake S3 bucket. For more Athena troubleshooting topics, see the [Troubleshooting in Athena](https://docs.aws.amazon.com/athena/latest/ug/troubleshooting-athena.html) section of the *Amazon Athena User Guide*.

## Querying isn't returning new objects in the data lake
<a name="query-not-returning-objects"></a>

Your Athena query may not return new objects in your data lake even when the S3 bucket for Security Lake contains those objects. This may occur if you've disabled Security Lake and then enabled it again. As a result, the AWS Glue partitions may not properly register the new objects.

To resolve the error, follow these steps:

1. Open the AWS Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/).

1. From the navigation bar, on the Regions selector, choose the Region in which Security Lake is enabled but the Athena query isn't returning results.

1. From the navigation pane, choose **Functions**, and select the function from the following list depending on the source version:
   + `Source version 1 (OCSF 1.0.0-rc.2) ` – **SecurityLake\_Glue\_Partition\_Updater\_Lambda\_{{≪region>}}** function.
   + `Source version 2 (OCSF 1.1.0)` – **AmazonSecurityLakeMetastoreManager\_{{≪region>}}** function.

1. On the **Configurations** tab, choose **Triggers**.

1. Select the option next to the function, and choose **Edit**.

1. Select **Activate trigger**, and choose **Save**. This will turn the function state to **Enabled**.

## Unable to access AWS Glue tables
<a name="access-glue-tables"></a>

A query access subscriber may not be able to access AWS Glue tables that contain Security Lake data.

First, ensure that you've followed the steps outlined in [Setting up cross-account table sharing (subscriber step)](create-query-subscriber-procedures.md#grant-query-access-subscriber).

If the subscriber still doesn't have access, follow these steps:

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. From the navigation pane, choose **Data Catalog** and **Catalog settings**.

1. Give permission to the subscriber to access the AWS Glue tables with a resource-based policy. For information about creating resource-based policies, see [Resource-based policy examples for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/security_iam_resource-based-policy-examples.html) in the *AWS Glue Developer Guide*.

## Troubleshooting Amazon S3 throttling for Security Lake queries
<a name="athena-queries-troubleshoot-s3-throttling"></a>

When you query Amazon Security Lake tables with Amazon Athena, a query can fail with an error similar to the following:

```
ICEBERG_CANNOT_OPEN_SPLIT: Error opening Iceberg split s3://{{amzn-s3-demo-bucket}}/aws/CLOUD_TRAIL_MGMT/2.0/region={{region}}/accountId={{accountId}}/eventDay={{eventDay}}/{{file}}.gz.parquet ...
AmazonS3Exception: Please reduce your request rate. (Service: Amazon S3; Status Code: 503; Error Code: SlowDown ...)
```

You might also receive a `HIVE_S3_THROTTLING` error. These errors mean that Amazon S3 throttled the read requests Athena sent to your data lake bucket. The same query can succeed on one run and fail on the next, depending on how many other requests are reading the same data at the same time. This topic explains why throttling happens with Security Lake data and how to reduce it.

### Why throttling happens
<a name="query-s3-throttling-why"></a>

Security Lake delivers data continuously. For each log source, Security Lake writes data in Apache Parquet format to S3 prefixes organized by Region, account, and day:

```
aws/{{source}}/{{version}}/region={{region}}/accountId={{accountId}}/eventDay={{eventDay}}/
```

In a large, multi-petabyte lake, Security Lake produces a new object about every 5 minutes for each source in each account and Region. At that rate, a single-day prefix for one source, account, and Region has 300 objects. A year of data for that source holds more than 100,000 objects.

Athena reads Iceberg tables in parallel. It splits a query into tasks that each read one or more data files. It also decides how many tasks run and how fast they read from S3. As a result, you can't set the read rate yourself. Each Parquet file takes at least one S3 GET request. A query that scans a wide time range across many accounts can send tens of thousands of requests to the same prefixes within seconds.

Amazon S3 supports at least 5,500 GET or HEAD requests (the request types used to read objects) per second for each partitioned prefix in a bucket. It adds partitions automatically as request rates grow, but gradually. Until it catches up, requests above the current limit receive a 503 Slow Down response. For more information about optimizing Amazon S3 performance, see [Best practices design patterns: optimizing Amazon S3 performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html).

The limit applies to all reads from a prefix, not to each query. Concurrent Athena queries from all users and subscribers that read the same data share the limit. Throttling becomes more likely as more users, accounts, or applications query the data lake at the same time.

### Reducing the number of objects each query reads
<a name="query-s3-throttling-reduce-objects"></a>

Limiting what a query scans makes queries faster and, with per-query pricing, cheaper. This is the most effective way to avoid throttling.
+ **Filter on time.** Security Lake tables are partitioned by event time. Always include a filter on `time_dt` that covers only the range you need, so that Athena skips day prefixes outside that range. In the following example SQL query, replace the account ID, Region, and time range with the values you need:

  ```
  SELECT time_dt, api.operation, actor.user.uid
  FROM amazon_security_lake_glue_db_us_east_1.amazon_security_lake_table_us_east_1_cloud_trail_mgmt_2_0
  WHERE time_dt BETWEEN TIMESTAMP '2026-10-01 00:00:00' AND TIMESTAMP '2026-10-07 23:59:59'
    AND accountid = '111122223333'
    AND region = 'us-east-1'
  ```
+ **Filter on account and Region.** If you need data for specific accounts or Regions, filter on `accountid` and `region` as well. Each account and Region combination is a separate prefix.
+ **Split long time ranges.** For investigations that cover months of data, run several queries over shorter ranges one after another instead of one query over the full range.
+ **Reuse results.** Turn on query result reuse for queries that you run repeatedly, so that Athena returns cached results instead of scanning S3 again.

### Reducing concurrent load
<a name="query-s3-throttling-reduce-load"></a>

Because Athena controls how it reads from S3, you can't slow down an individual query. You can reduce how often throttling happens and recover from it when it does.
+ **Retry with exponential backoff.** Throttling errors are temporary. If you run queries from an application, a security information and event management (SIEM) integration, or a scheduled job, retry failed queries with exponential backoff and jitter.
+ **Limit concurrency.** Avoid running many wide queries against the same tables at the same time, especially from automated integrations. Use Athena workgroups to separate workloads. If you use capacity reservations, you can set a maximum number of Data Processing Units (DPUs) for each query. Fewer DPUs mean fewer tasks run in parallel, which can reduce the number of simultaneous reads at the cost of longer run times.
+ **Copy frequently queried data.** If you repeatedly run large queries over the same subset of data, you can use `CREATE TABLE AS SELECT` or `INSERT INTO` to copy that subset into an Iceberg table that you own and manage. Then, query the copy. You can compact and maintain your own table as needed.

### Compacting data
<a name="query-s3-throttling-compaction"></a>

Compaction combines many small files into fewer large ones, which reduces the number of requests that a query needs. Athena and AWS Glue offer different compaction features, and only one of them works with Security Lake tables.
+ **Not supported: AWS Glue table optimizers.** Don't turn on AWS Glue Data Catalog table optimizers for tables that Security Lake creates and manages. AWS Glue compaction isn't compatible with the Parquet files that Security Lake writes, and compaction jobs on these tables fail.
+ **Supported with considerations: Athena OPTIMIZE.** You can run the Athena `OPTIMIZE REWRITE DATA` statement on Security Lake tables. Before you do, consider the following:
  + **Effect on subscribers.** Athena can write the compacted data files to prefixes outside the standard Security Lake prefix layout, and Security Lake doesn't deliver these files to subscribers. Subscribers that rely on new-object notifications might miss the compacted data. They might also process the same records twice if they read both the original and the compacted files. Check how your subscribers consume data before you compact.
  + **Measure first.** Compact a small sample, such as 10 days for one account and Region. Then, compare `EXPLAIN ANALYZE` output for the same query on compacted and uncompacted partitions before you compact at scale.
  + **Statement size.** Limit each statement to a few partitions with a `WHERE` clause, for example, one account, one Region, and a few days. Statements that rewrite large amounts of data can time out.
  + **Concurrent writes.** Security Lake continues to write to the table while `OPTIMIZE` runs. If both commit at the same time, one of the commits fails, and you must retry it.

Compaction reduces the number of files a query reads, but it doesn't raise the per-prefix request limit. As the number of concurrent queries grows, you still need query filters and retries.

### Related topics
<a name="query-s3-throttling-related"></a>
+ [Optimizing Iceberg tables](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-data-optimization.html) in the *Amazon Athena User Guide*