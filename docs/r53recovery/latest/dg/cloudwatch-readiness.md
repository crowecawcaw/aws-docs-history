# Using Amazon CloudWatch with readiness check in ARC

Amazon Application Recovery Controller (ARC) publishes data points to Amazon CloudWatch for your readiness checks.
CloudWatch enables you to retrieve statistics about those data points as an ordered set of
time-series data, known as _metrics_. Think of a metric as a variable
to monitor, and the data points as the values of that variable over time. For example, you
can monitor traffic through an AWS Region over a specified
time period. Each data point has an associated time stamp and an optional unit of measurement.

You can use metrics to verify that your system is performing as expected. For example,
you can create a CloudWatch alarm to monitor a specified metric and initiate an action (such as
sending a notification to an email address) if the metric goes outside what you consider
an acceptable range.

For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Topics

- [ARC metrics](#cloudwatch-metrics-recovery-readiness "#cloudwatch-metrics-recovery-readiness")
- [Statistics for ARC metrics](#cloudwatch-metric-statistics "#cloudwatch-metric-statistics")
- [View CloudWatch metrics in ARC](#view-metric-data "#view-metric-data")

## ARC metrics

The `AWS/Route53RecoveryReadiness` namespace includes the following metrics.

| Metric            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ReadinessChecks` | Represents the number of readiness checks processed by ARC.<br>The metric can be dimensioned by its states, listed below.<br>**Unit**: `Count`.<br>**Reporting criteria**: There is a nonzero value.<br>**Statistics**: The only useful statistic is<br>`Sum`.<br>Dimensions<br>• `READY`<br>• `NOT_READY`<br>• `NOT_AUTHORIZED`<br>• `UNKNOWN`                                                                                                                |
| `Resources`       | Represents the number of resources processed by ARC, which can be dimensioned by<br>their resource identifier, as defined by the API.<br>**Unit**: `Count`.<br>**Reporting criteria**: There is a nonzero value.<br>**Statistics**: The only useful statistic is<br>`Sum`.<br>Dimensions<br>• `ResourceSetType`: These are the resource types, filtered by the<br>number of resources per given type evaluated by ARC<br>For example: `AWS::CloudWatch::Alarm` |

## Statistics for ARC metrics

CloudWatch provides statistics based on the metric data points published by ARC. Statistics
are aggregations of metric data over a specified period of time. When you request
statistics, the returned data stream is identified by the metric name and dimension. A
dimension is a name/value pair that uniquely identifies a metric.

The following are examples of metric/dimension combinations that you might find useful:

- View the number of readiness checks evaluated for readiness by ARC.
- View the total number of resources for a given resource set type evaluated by ARC.

## View CloudWatch metrics in ARC

You can view the CloudWatch metrics for ARC using the CloudWatch console or
the AWS CLI. In the console, metrics are displayed as monitoring
graphs.

You must view CloudWatch metrics for ARC in the US West (Oregon) Region, both in the
console or when using the AWS CLI. When you use the AWS CLI, specify the US West (Oregon) Region
for your command by including the following parameter: `--region us-west-2`.

###### To view metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Select the **Route53RecoveryReadiness** namespace.
4. (Optional) To view a metric across all dimensions, type its name in the search field.

###### To view metrics using the AWS CLI

Use the following [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") command
to list the available metrics:

```
`aws cloudwatch list-metrics --namespace AWS/Route53RecoveryReadiness --region us-west-2`
```

###### To get the statistics for a metric using the AWS CLI

Use the following [get-metric-statistics](../../../cli/latest/reference/cloudwatch/get-metric-statistics.md "../../../cli/latest/reference/cloudwatch/get-metric-statistics.md") command to get statistics for a specified
metric and dimension. Note that CloudWatch treats each unique combination of dimensions as
a separate metric. You can't retrieve statistics using combinations of dimensions
that were not specifically published. You must specify the same dimensions that were used
when the metrics were created.

The following example lists the total readiness checks evaluated, per minute, for an account in ARC.

```
`aws cloudwatch get-metric-statistics --namespace AWS/Route53RecoveryReadiness \
--metric-name ReadinessChecks \
--region us-west-2 \
--statistics Sum --period 60 \
--dimensions Name=State,Value=READY \
--start-time 2021-07-03T01:00:00Z --end-time 2021-07-03T01:20:00Z`
```

The following is example output from the command:

```
{
    "Label": "ReadinessChecks",
    "Datapoints": [
        {
            "Timestamp": "2021-07-08T18:00:00Z",
            "Sum": 1.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2021-07-08T18:04:00Z",
            "Sum": 1.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2021-07-08T18:01:00Z",
            "Sum": 1.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2021-07-08T18:02:00Z",
            "Sum": 1.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2021-07-08T18:03:00Z",
            "Sum": 1.0,
            "Unit": "Count"
        }
    ]
}
```
