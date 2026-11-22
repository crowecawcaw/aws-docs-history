

# Monitoring SQL statements with Aurora DSQL statement statistics

Aurora DSQL statement statistics provide aggregated statistics for each SQL statement that your cluster runs. For each statement, Aurora DSQL records the number of execution calls, the planning and execution time, the rows, and the distributed processing units (DPUs) that the statement used. Aurora DSQL publishes these statistics as Amazon CloudWatch OpenTelemetry (OTel) metrics. It also writes up to 32 KiB of the normalized SQL text of each statement to Amazon CloudWatch Logs.

Statement statistics are off by default. You turn them on for each cluster that you want to monitor.

**Important**  
Statement statistics incur additional CloudWatch and CloudWatch Logs charges. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

**Topics**
+ [What are statement statistics?](#statement-statistics-what-is)
+ [Turning on statement statistics](#statement-statistics-turn-on)
+ [Accessing statement statistics data](#statement-statistics-access)
+ [Related resources](#statement-statistics-related-resources)

## What are statement statistics?
<a name="statement-statistics-what-is"></a>

Aurora DSQL processes each statement across its query processing and storage layers. Statement statistics combine the work of these layers into one set of metrics for each statement. Aurora DSQL records every successful execution of `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements as it completes, and aggregates the results for each statement. It doesn't count utility statements, such as `BEGIN`, `COMMIT`, and `SET`, or data definition language (DDL) statements. Aurora DSQL counts only top-level statements, which are the statements that your application sends directly.

If a transaction fails at commit, Aurora DSQL still counts the statements that ran in it. If your application retries the transaction, Aurora DSQL counts those statements again.

### Query IDs and normalized SQL text
<a name="statement-statistics-query-ids"></a>

Aurora DSQL groups the runs of a statement by its normalized SQL text. Normalization removes SQL comments, replaces each literal value with a numbered placeholder, such as `$0`, and replaces extra white space with a single space. Aurora DSQL also computes a *query ID*, a short identifier of the normalized statement. Statements that differ only in their literal values share the same normalized SQL text and query ID.


| Statement that your cluster runs | Normalized SQL text | Query ID | 
| --- |--- |--- |
| SELECT name FROM users WHERE id = 1042 | SELECT name FROM users WHERE id = $0 | 6kuw53n1h44do | 
| SELECT name FROM users WHERE id = 7 | SELECT name FROM users WHERE id = $0 | 6kuw53n1h44do | 

### Statement statistics metrics
<a name="statement-statistics-metrics"></a>


| Metric | Unit | Description | 
| --- |--- |--- |
| aws.dsql.query.calls | Count | The number of execution calls of the statement. Each successful execution is one call. | 
| aws.dsql.query.time | Seconds | The planning and execution time of the statement. | 
| aws.dsql.query.rows | Count | The number of rows that the statement returned or changed. | 
| aws.dsql.query.compute\_dpu | DPU | The compute DPUs that the statement used to process data, such as filtering, sorting, and joining. | 
| aws.dsql.query.read\_dpu | DPU | The read DPUs that the statement used to read data from storage. | 
| aws.dsql.query.write\_dpu | DPU | The write DPUs that the statement used to write data to storage, including secondary indexes. | 
| aws.dsql.query.multi\_region\_write\_dpu | DPU | The write DPUs that the statement used in the peered Region of a multi-Region cluster. For a single-Region cluster, the value is 0. | 
| aws.dsql.query.compute.time | Seconds | The time that the statement spent in the query processor, excluding the time spent on storage requests. | 
| aws.dsql.query.storage.time | Seconds | The time that the statement spent on storage servers during read operations. | 
| aws.dsql.query.scanned\_rows | Count | The estimated number of rows that the statement's storage scans visited. | 

The metrics carry the following labels, which you use to group and filter the data.


| Label | Description | 
| --- |--- |
| db.query.id | The fingerprint of the normalized SQL text of the statement. Use it to group by statement and to look up the normalized SQL text. | 
| aws.dsql.session.role.arn | The Amazon Resource Name (ARN) of the IAM identity that the connection authenticated as. | 
| application.name | The application name that you set in connection parameters. Aurora DSQL includes this label only when the connection has an application name. | 
| @resource.aws.dsql.cluster\_id | The cluster identifier. Use it to filter to one cluster. | 

## Turning on statement statistics
<a name="statement-statistics-turn-on"></a>

You turn on statement statistics by adding the `STATEMENT_STATISTICS` metric group to a cluster. `STATEMENT_STATISTICS` is the only metric group available today. This is a Regional, per-cluster setting. For a multi-Region cluster, turn it on for the cluster in each AWS Region.

You can manage this setting with the Aurora DSQL console, the AWS Command Line Interface (AWS CLI), the AWS SDKs, and CloudFormation. In the API and the SDKs, use the `metricGroups` parameter of the `CreateCluster` and `UpdateCluster` operations. In CloudFormation, use the `MetricGroups` property of the `AWS::DSQL::Cluster` resource. To change the setting, you need the `dsql:CreateCluster` or `dsql:UpdateCluster` permission. To read it, you need the `dsql:GetCluster` permission.

------
#### [ Console ]

**Turn on statement statistics when you create a cluster**

1. Open the [Aurora DSQL console](https://console.aws.amazon.com/dsql).

1. Choose **Create cluster**.

1. Choose **Advanced configuration**.

1. In **Advanced monitoring**, select **Enable statement statistics**.

1. Choose **Create cluster**.

**Turn statement statistics on or off for an existing cluster**

1. Open the [Aurora DSQL console](https://console.aws.amazon.com/dsql).

1. In the navigation pane, choose **Clusters**.

1. Choose the ID of the cluster.

1. Choose the **Monitoring** tab.

1. In **Advanced monitoring**, choose **Manage advanced monitoring**.

1. Select or clear **Enable statement statistics**.

1. Choose **Save**.

   The console shows the message **Advanced monitoring updated for {{your\_cluster\_name}}**. The change takes effect in a few minutes. After that, **Statement statistics** shows **On** or **Off** in the **Advanced monitoring** section.

------
#### [ CLI ]

In the following commands, replace {{region}} with the Region of your cluster and {{your\_cluster\_id}} with the ID of your cluster.

**Turn on statement statistics when you create a cluster**  
Run the following AWS CLI command:

```bash
aws dsql create-cluster \
  --metric-groups '[{"metricGroup":"STATEMENT_STATISTICS"}]' \
  --region {{region}}
```

The response includes `metricGroups`. The following example response shows only some of the fields.

```json
{
    "identifier": "abc0def1baz2quux3quuux4abc",
    "arn": "arn:aws:dsql:us-east-1:111122223333:cluster/abc0def1baz2quux3quuux4abc",
    "status": "CREATING",
    "metricGroups": [
        {
            "metricGroup": "STATEMENT_STATISTICS"
        }
    ]
}
```

**Turn on statement statistics for an existing cluster**  
Run the following AWS CLI command:

```bash
aws dsql update-cluster \
  --identifier {{your_cluster_id}} \
  --metric-groups '[{"metricGroup":"STATEMENT_STATISTICS"}]' \
  --region {{region}}
```

**Confirm the setting**  
Run the following AWS CLI command. The output is `STATEMENT_STATISTICS` when statement statistics are on, and empty when they're off.

```bash
aws dsql get-cluster \
  --identifier {{your_cluster_id}} \
  --query 'metricGroups[].metricGroup' --output text \
  --region {{region}}
```

The following example output shows that statement statistics are on.

```text
STATEMENT_STATISTICS
```

**Turn off statement statistics**  
Run the following AWS CLI command with an empty list:

```bash
aws dsql update-cluster \
  --identifier {{your_cluster_id}} \
  --metric-groups '[]' \
  --region {{region}}
```

------

After you turn off statement statistics, statistics from open connections can arrive for a few minutes. Normalized SQL text can arrive for up to a day.

## Accessing statement statistics data
<a name="statement-statistics-access"></a>

You can access statement statistics in the following ways:
+ **Amazon CloudWatch Database Insights** – A curated, no-code user interface (UI) for exploring the normalized SQL text and statement statistics charts of each statement. This is the starting point for most investigations.
+ **Prometheus Query Language (PromQL)** – Query the underlying statement statistics metrics programmatically for integration with monitoring tools, or for interactive exploration in CloudWatch Query Studio.
+ **CloudWatch Log Analytics** – Look up the normalized SQL text of a statement by its query ID.

### How Aurora DSQL aggregates statement statistics data
<a name="statement-statistics-aggregation"></a>

Aurora DSQL sends statement statistics to CloudWatch as one or more data points for each one-minute window. Each data point holds only the work done after the previous data point, not a running total. A time series is a list of data points. Aurora DSQL keeps a separate time series for each combination of cluster, query ID, IAM identity, and application name. For example, if two applications run the same statement, the statement has two time series.

To get the total value of a metric for a time range, sum up the data points in that range. Then add the time series of each statement together. Amazon CloudWatch Database Insights does this aggregation for you.

### Using CloudWatch Database Insights
<a name="statement-statistics-database-insights"></a>

**View statement statistics in Database Insights**

1. Open the CloudWatch console and choose **Database Insights** in the left navigation pane.

1. In **Database resources** of the **Fleet Health** view, choose the **DB Identifier** of your Aurora DSQL cluster.

1. In **Top SQL**, choose a statement to see its query ID, its normalized SQL text, and its statistics charts.

Database Insights shows the following statistics for each statement.


| Statistic | Calculation | What it shows | 
| --- |--- |--- |
| Calls/s | Calls divided by seconds in the chart interval | How often the statement runs. | 
| Rows/s | Rows divided by seconds in the chart interval | How many rows the statement returns or changes per second. | 
| Avg duration | Time divided by calls | The mean planning and execution time of each execution call, in milliseconds. | 
| DPU per call | Total, compute, read, and write DPUs, each divided by calls | Where the cost of each call goes. | 
| Compute time and storage time per call | Compute time divided by calls, and storage time divided by calls | How much of each call goes to storage operations, in milliseconds. | 
| Scanned rows and returned rows per call | Scanned rows divided by calls, and rows divided by calls | Whether the statement scans far more rows than it returns or changes. | 

### Using PromQL
<a name="statement-statistics-promql"></a>

You can query statement statistics with PromQL in CloudWatch Query Studio. In the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/), choose **Query Studio**, and then choose **PromQL**. You need the `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics` permissions.

Every query follows the two steps in [How Aurora DSQL aggregates statement statistics data](#statement-statistics-aggregation). First, `sum_over_time` adds up the data points of each time series. Then, `sum by` adds the time series together by a label, such as `"db.query.id"`. These metrics hold deltas, not running totals, so use `sum_over_time` instead of `rate()` or `increase()`.
+ Because the metric and label names contain periods, use the PromQL quoted-name selector form, such as `{"aws.dsql.query.time"}`.
+ Replace {{your\_cluster\_id}} with your cluster identifier.
+ The `[1h]` range sets the time window. The maximum is 24 hours.
+ For a ranked list, use the table view. For a trend, use the graph view, and set the range equal to the step, for example, `[5m]` with a 5-minute step.
+ A query returns at most 500 time series. Use `topk` or a label filter to stay under this limit.

**Statements that take the most total time**  
The following query ranks the 10 statements with the most total time, in seconds, over the last hour. To rank by another metric, such as calls or DPUs, use its name in place of `aws.dsql.query.time`.

```promql
topk(10,
  sum by ("db.query.id") (
    sum_over_time({
      "aws.dsql.query.time",
      "@resource.aws.dsql.cluster_id"="{{your_cluster_id}}"
    }[1h])
  )
)
```

**Mean planning and execution time per execution call**  
The following query divides the total planning and execution time of each statement by its number of execution calls, and then converts seconds to milliseconds. The `>= 100` filter hides statements with fewer than 100 execution calls. Lower it to see them.

```promql
topk(10,
  sum by ("db.query.id") (
    sum_over_time({
      "aws.dsql.query.time",
      "@resource.aws.dsql.cluster_id"="{{your_cluster_id}}"
    }[1h])
  )
  /
  (sum by ("db.query.id") (
    sum_over_time({
      "aws.dsql.query.calls",
      "@resource.aws.dsql.cluster_id"="{{your_cluster_id}}"
    }[1h])
  ) >= 100)
  * 1000
)
```

**Calls per second, as a trend**  
The following query shows how often each statement runs. Use the graph view with a 5-minute step. The query divides each 5-minute sum by 300 seconds.

```promql
topk(10,
  sum by ("db.query.id") (
    sum_over_time({
      "aws.dsql.query.calls",
      "@resource.aws.dsql.cluster_id"="{{your_cluster_id}}"
    }[5m])
  ) / 300
)
```

**Scanned rows per call**  
The following query shows how many rows each call visits in storage. A statement that scans many rows but returns few might need an index.

```promql
topk(10,
  sum by ("db.query.id") (
    sum_over_time({
      "aws.dsql.query.scanned_rows",
      "@resource.aws.dsql.cluster_id"="{{your_cluster_id}}"
    }[1h])
  )
  /
  (sum by ("db.query.id") (
    sum_over_time({
      "aws.dsql.query.calls",
      "@resource.aws.dsql.cluster_id"="{{your_cluster_id}}"
    }[1h])
  ) > 0)
)
```

For more information about PromQL in CloudWatch, see [Query metrics with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html).

### Using CloudWatch Log Analytics
<a name="statement-statistics-logs"></a>

PromQL results identify each statement by its query ID. To find the normalized SQL text of a query ID, query the `/aws/dsql/normalized-sql-text` log group in your account. All clusters in an AWS account and Region share this log group, and each cluster has its own log stream, named with the cluster identifier.

**Find the normalized SQL text for a query ID**

1. Open the [Log Analytics page](https://console.aws.amazon.com/cloudwatch/home#log-analytics) in the CloudWatch console.

1. Choose the log group `/aws/dsql/normalized-sql-text`.

1. Set the time range to start three hours before the period that you investigate. Aurora DSQL writes the text again at least every three hours as long as the statement runs.

1. In the following query, replace {{your\_query\_id}} with the query ID from your results, and then run the query.

   ```text
   fields @timestamp, queryId, normalizedText
   | filter queryId = "{{your_query_id}}"
   | limit 1
   ```

**Note**  
Aurora DSQL stores up to 32 KiB of normalized SQL text for each statement.
If Aurora DSQL creates the log group, it sets a retention period of 545 days. You can change the retention. If the log group already exists, Aurora DSQL doesn't change it.

## Related resources
<a name="statement-statistics-related-resources"></a>
+ [Query metrics with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html) – overview of PromQL support in CloudWatch.
+ [Running PromQL queries in Query Studio](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL-QueryStudio.html) – the interactive query workbench in the CloudWatch console.
+ [Amazon CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) – the CloudWatch UI for monitoring database load and performance.
+ [Analyzing log data with CloudWatch Log Analytics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) – how to query the normalized SQL text log group of statement statistics.
+ [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) – charges for the metrics and logs that statement statistics publish.