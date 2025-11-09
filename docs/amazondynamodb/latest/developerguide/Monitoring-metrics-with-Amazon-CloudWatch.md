# Monitoring metrics in DynamoDB with

Amazon CloudWatch

You can monitor DynamoDB using CloudWatch, which collects and processes raw data from
DynamoDB into readable, near real-time metrics. These statistics are retained for a
period of time, so you can access historical information for a better perspective
on how your web application or service is performing. By default, DynamoDB metric
data is sent to CloudWatch automatically. For more information, see [What is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") and [Metrics retention](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#metrics-retention "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#metrics-retention") in the _Amazon CloudWatch User Guide_.

###### Topics

- [How do I use DynamoDB metrics?](#How-do-I-use-DynamoDB-metrics "#How-do-I-use-DynamoDB-metrics")
- [Viewing metrics in the CloudWatch console](#Viewing-metrics-in-CloudWatch-console "#Viewing-metrics-in-CloudWatch-console")
- [Viewing metrics in the AWS CLI](#Viewing-metrics-in-the-cli "#Viewing-metrics-in-the-cli")
- [DynamoDB Metrics and dimensions](metrics-dimensions.md "metrics-dimensions.md")
- [Creating CloudWatch alarms in DynamoDB](Monitoring-metrics-creating-cloudwatch-alarms.md "Monitoring-metrics-creating-cloudwatch-alarms.md")

## How do I use DynamoDB metrics?

The metrics reported by DynamoDB provide information that you can analyze in
different ways. The following list shows some common uses for the metrics. These are
suggestions to get you started, not a comprehensive list.

| How do I use DynamoDB metrics?                                                             | How can I?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Relevant metrics |
| ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| How can I monitor the rate of TTL deletions on my table?                                   | You can monitor `TimeToLiveDeletedItemCount` over<br>the specified time period, to track the rate of TTL deletions on<br>your table. For an example of a server-less application using<br>the `TimeToLiveDeletedItemCount` metric, see [Automatically archive items to S3 using DynamoDB time to live<br>(TTL) with AWS Lambda and Amazon Data Firehose](https://aws.amazon.com/blogs/database/automatically-archive-items-to-s3-using-dynamodb-time-to-live-with-aws-lambda-and-amazon-kinesis-firehose/ "https://aws.amazon.com/blogs/database/automatically-archive-items-to-s3-using-dynamodb-time-to-live-with-aws-lambda-and-amazon-kinesis-firehose/"). |
| How can I determine how much of my provisioned throughput is being used?                   | You can monitor `ConsumedReadCapacityUnits` or<br>`ConsumedWriteCapacityUnits` over the specified<br>time period, to track how much of your provisioned throughput is<br>being used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| How can I determine which requests exceed the provisioned throughput quotas of a<br>table? | `ThrottledRequests` is incremented by one if any<br>event within a request exceeds a provisioned throughput quota.<br>Then, to gain insight into which event is throttling a request,<br>compare `ThrottledRequests` with the<br>`ReadThrottleEvents` and<br>`WriteThrottleEvents` metrics for the table and<br>its indexes.                                                                                                                                                                                                                                                                                                                                   |
| How can I determine if any system errors occurred?                                         | You can monitor `SystemErrors` to determine if any<br>requests resulted in an HTTP 500 (server error) code. Typically,<br>this metric should be equal to zero. If it isn't, then you might<br>want to investigate.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| How can I monitor the latency value for my table operations?                               | You can monitor `SuccessfulRequestLatency` by tracking the average latency<br>and median latency through percentile metrics (p50). Occasional spikes in latency aren't a<br>cause for concern. However, if average latency or p50 (median) is high, there could be an<br>underlying issue that you must resolve. See [Troubleshooting latency issues in Amazon DynamoDB](TroubleshootingLatency.md "TroubleshootingLatency.md") for more information.                                                                                                                                                                                                          |

## Viewing metrics in the CloudWatch console

Metrics are grouped by the service namespace first and then by the various dimension combinations within
each namespace.

###### To view metrics in the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics, All metrics**.
3. Select the **DynamoDB** namespace. You can also select **Usage** namespace to
   view DynamoDB usage metrics. For more information about usage metrics, see [AWS usage metrics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.md").
4. The **Browse** tab displays all metrics in the namespace.
5. (Optional) To add the metric graph to a CloudWatch dashboard, choose **Actions, Add to
   dashboard**.

## Viewing metrics in the AWS CLI

To obtain metric information using the AWS CLI, use the CloudWatch command `list-metrics`.
In the following example, you list all metrics in the `AWS/DynamoDB` namespace.

```

                `aws cloudwatch list-metrics --namespace "AWS/DynamoDB"`

```

To obtain metric statistics, use the command `get-metric-statistics`. The
following command gets `ConsumedReadCapacityUnits` statistics for the table
`ProductCatalog` over the specific 24-hour period, with a 5-minute
granularity.

```
aws cloudwatch get-metric-statistics —namespace AWS/DynamoDB \
     —metric-name ConsumedReadCapacityUnits \
     —start-time 2023-11-01T00:00:00Z \
     —end-time 2023-11-02T00:00:00Z \
     —period 360 \
     —statistics Average \
     —dimensions Name=TableName,Value=ProductCatalog
```

Sample output appears as follows:

```
{
    "Datapoints": [
        {
            "Timestamp": "2023-11-01T 09:18:00+00:00",
            "Average": 20,
            "Unit": "Count"
        },
        {
            "Timestamp": "2023-11-01T 04:36:00+00:00",
            "Average": 22.5,
            "Unit": "Count"
        },
        {
            "Timestamp": "2023-11-01T 15:12:00+00:00",
            "Average": 20,
            "Unit": "Count"
        }, ...
        {
            "Timestamp": "2023-11-01T 17:30:00+00:00",
            "Average": 25,
            "Unit": "Count"
        }
    ],
    "Label": " ConsumedReadCapacityUnits "
}
```
