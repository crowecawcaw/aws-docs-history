

# Monitoring Aurora DSQL with Amazon CloudWatch
<a name="cloudwatch-monitoring"></a>

Monitor Aurora DSQL using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. CloudWatch keeps these statistics for 15 months, helping you gain better perspective on your web application or service performance. Set alarms to watch for specific thresholds and send notifications or take actions when met. Review the following Usage and Observability metrics available for Aurora DSQL.

For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/). 

For a deeper understanding of the performance and cost of your clusters, see [Monitoring Aurora DSQL clusters with Aurora DSQL Database Insights](dsql-db-insights.md).

## Observability and performance
<a name="observability-performance"></a>

This table outlines observability metrics for Aurora DSQL. It includes metrics for tracking read-only and total transactions to provide overall workload characterization. Actionable metrics like query timeouts and OCC conflict rate are included to help identify performance issues and concurrency conflicts. Session-related metrics, both active and total, offer insights into the current load on the system.


| CloudWatch Metric Name | Metric | Unit | Description | 
| --- |--- |--- |--- |
| ReadOnlyTransactions | Read-only transactions | none | The number of read-only transactions | 
| TotalTransactions | Total transactions | none | The total number of transactions executed on the system, including read-only transactions. | 
| QueryTimeouts | Query timeouts | none | The number of queries which have timed out due to hitting the maximum transaction time | 
| OccConflicts | OCC conflicts | none | The number of transactions aborted due to key level OCC | 
| CommitLatency | Commit Latency | milliseconds | Time spent by commit phase of query execution (P50) | 
| BytesWritten | Bytes Written | bytes | Bytes written to storage | 
| BytesRead | Bytes Read | bytes | Bytes read from storage | 
| ComputeTime | QP compute time | milliseconds | QP wall clock time | 
| ClusterStorageSize | Cluster Storage Size | bytes | Cluster size | 

Aurora DSQL also publishes the following metrics under the AWS/Usage namespace. Use these metrics to monitor connection attempts and active connection count for your clusters.


| CloudWatch Metric Name | Type | Resource | ResourceId | Service | Unit | Description | 
| --- |--- |--- |--- |--- |--- |--- |
| ResourceCount | Resource | ClusterConnectionCount | cluster/<cluster-id> | AuroraDSQL | None | The number of active connections for a cluster. | 
| CallCount | API | DbConnectAdmin or DbConnect | cluster/<cluster-id> | AuroraDSQL | None | The number of API calls for database connection operations (DbConnectAdmin or DbConnect). | 

## Usage metrics
<a name="usage-metrics"></a>

 Aurora DSQL measures all request-based activity, such as query processing, reads, and writes, using a single normalized billing unit called Distributed Processing Unit (DPU). 


| CloudWatch Metric Name | Metric | Dimension: ResourceId | Unit | Description | 
| --- |--- |--- |--- |--- |
| WriteDPU | Write Units | <cluster-id> | DPU | Approximates the write active-use component of your Aurora DSQL cluster DPU usage. | 
| MultiRegionWriteDPU | Multi-Region Write Units | <cluster-id> | DPU | Applicable for Multi-Region clusters: Approximates the multi-Region write active-use component of your Aurora DSQL cluster DPU usage. | 
| ReadDPU | Read Units | <cluster-id> | DPU | Approximates the read active-use component of your Aurora DSQL cluster DPU usage. | 
| ComputeDPU | Compute Units | <cluster-id> | DPU | Approximates the compute active-use component of your Aurora DSQL cluster DPU usage. | 
| StreamDPU | Stream Units | <cluster-id> | DPU | Applicable for clusters with CDC streams: Approximates the CDC streaming active-use component of your Aurora DSQL cluster DPU usage, summed across all streams on the cluster. | 
| TotalDPU | Total Units | <cluster-id> | DPU | Approximates the total active-use component of your Aurora DSQL cluster DPU usage. This is the sum of the write, multi-Region write, read, compute, and stream components. Use the Sum statistic. | 

## CDC stream metrics
<a name="cdc-stream-metrics"></a>

Aurora DSQL publishes the following metrics for change data capture (CDC) streams. These metrics use the `ClusterId` and `StreamId` dimensions, so you can monitor each CDC stream independently. For more information about CDC streams, see [Change data capture (CDC) streams](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html).


| CloudWatch Metric Name | Metric | Unit | Description | 
| --- |--- |--- |--- |
| IsImpaired | Is impaired | none | Indicates whether the stream is impaired. The value is 1 when the stream is in the IMPAIRED state, and 0 when the stream is healthy. Use this metric to create a CloudWatch alarm that notifies you when a stream becomes impaired. | 
| PublishedBytes | Published bytes | bytes | The total number of bytes that Aurora DSQL wrote to the target Kinesis data stream. | 
| PublishedRecords | Published records | none | The number of CDC records that Aurora DSQL wrote to the target Kinesis data stream. | 
| BehindSourceLag | Behind source lag | milliseconds | The delay, in milliseconds, between when a transaction commits in Aurora DSQL and when the CDC system processes the resulting record. A rising value indicates that the CDC pipeline is falling behind the write workload. If lag grows beyond the failure threshold, the stream transitions to FAILED. | 
| BytesStreamed | Bytes streamed | bytes | The total bytes streamed through the CDC pipeline for billing purposes. This metric reflects the data volume used to calculate streaming charges. | 
| StreamDPU | Stream DPU | DPU | The Distributed Processing Units (DPU) consumed by the CDC stream. This metric reflects the processing cost of streaming change data. Aurora DSQL also publishes StreamDPU with only the ClusterId dimension, summed across all streams on the cluster. | 

## Setting DPU cost alarms
<a name="dpu-cost-alarms"></a>

To get notified when your cluster uses more DPUs than you expect, create a CloudWatch alarm on the `TotalDPU` metric in the `AWS/AuroraDSQL` namespace. Use the `ClusterId` dimension and the `Sum` statistic. Because the alarm evaluates DPU usage over a period, such as one hour, set the threshold as the DPU usage for that period.

To choose an hourly threshold from a monthly DPU budget, use the steps in the following table. Storage has its own charge, so leave it out of your DPU budget.

For example, assume a price of USD $8.00 per 1 million DPUs and a monthly DPU budget of USD $100.00. For the price in your AWS Region, see [Aurora DSQL pricing on the AWS website](https://aws.amazon.com/rds/aurora/dsql/pricing/).


| Step | Calculation | Example | 
| --- |--- |--- |
| 1. Find how many million DPUs your budget covers each month. | Monthly DPU budget ÷ price per 1 million DPUs | 100 ÷ 8 = 12.5 million DPUs | 
| 2. Find the hourly DPUs at 100% of your budget. | Result of step 1 ÷ 730 hours in a month | 12,500,000 ÷ 730 = about 17,123 DPUs | 
| 3. Find the hourly DPUs for an earlier warning, such as at 80% of your budget. | Result of step 2 × 0.8 | 17,123 × 0.8 = about 13,699 DPUs | 

Use the result of step 3 as the hourly threshold for your alarm.

The easiest way to create a DPU cost alarm is to start from the Aurora DSQL console. The console fills in the metric, namespace, and cluster for you.

**To start a DPU cost alarm (Aurora DSQL console)**

1. Open the Aurora DSQL console at [https://console.aws.amazon.com/dsql/](https://console.aws.amazon.com/dsql/).

1. In the list of clusters, select your cluster.

1. On the **Summary** tab, in the **Usage and cost** panel, choose **Create alarm**. CloudWatch opens with the `TotalDPU` metric for your cluster already selected.

You can also start from the CloudWatch console by choosing the metric yourself.

**To choose the metric for a DPU cost alarm (CloudWatch console)**

1. Open the [Alarms page of the Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home#alarmsV2:).

1. Choose **Create alarm**, and then choose **Select metric**.

1. Choose **AuroraDSQL**, then **ClusterId**. Select the `TotalDPU` metric for your cluster, and then choose **Select metric**.

After you start the alarm from either console, configure it.

**To configure the DPU cost alarm (console)**

1. For **Statistic**, choose **Sum**. For **Period**, choose **1 hour**.

1. For **Threshold type**, select **Static**.

1. For **Whenever TotalDPU is**, select **Greater**.

1. For **than**, enter your hourly DPU threshold.

1. Under **Additional configuration**, for **Missing data treatment**, choose **Treat missing data as good (not breaching threshold)**. An idle cluster doesn't publish DPU metrics.

1. Choose **Next**. Choose an Amazon Simple Notification Service (Amazon SNS) topic to notify when the alarm changes state, and then finish creating the alarm.

The following AWS CLI command creates the same alarm. Replace {{your-cluster-id}} with your cluster ID, {{hourly-dpu-threshold}} with your hourly DPU threshold, and {{sns-topic-arn}} with the ARN of your Amazon SNS topic.

```
aws cloudwatch put-metric-alarm \
    --alarm-name "DSQL-Hourly-DPU-Budget-Warning" \
    --alarm-description "Alert when hourly DPU exceeds 80% of budget" \
    --metric-name TotalDPU \
    --namespace AWS/AuroraDSQL \
    --statistic Sum \
    --period 3600 \
    --evaluation-periods 1 \
    --datapoints-to-alarm 1 \
    --threshold {{hourly-dpu-threshold}} \
    --comparison-operator GreaterThanThreshold \
    --dimensions Name=ClusterId,Value={{your-cluster-id}} \
    --alarm-actions {{sns-topic-arn}} \
    --ok-actions {{sns-topic-arn}} \
    --treat-missing-data notBreaching
```

Keep the following in mind when you set DPU cost alarms:
+ The alarm tracks DPU usage for each period, not your total spend for the month. A short spike can trigger the alarm even if your monthly usage stays within budget. To track month-to-date spend, use [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).
+ To reduce alarms from short spikes, require more than one breaching data point, such as two out of three evaluation periods.
+ A multi-Region cluster setup has a separate peered cluster in each Region, and each peered cluster reports its own `TotalDPU`. Create one alarm for each peered cluster, in that cluster's Region.
+ If you use CDC streams, `TotalDPU` already includes `StreamDPU`, so your `TotalDPU` alarm covers stream costs. To track the cost of a single stream, you can also create a separate alarm on `StreamDPU`. Aurora DSQL reports `StreamDPU` for each stream with the `ClusterId` and `StreamId` dimensions.

For more information about finding the statements that drive DPU usage, see [Finding high-load queries with Aurora DSQL Database Insights](billing-metering.md#billing-db-insights).