# Manage CloudWatch subscriptions using the AWS CLI

Use the AWS CLI or APIs to get Infrastructure Performance metrics in AWS Network Manager and to enable or disable
Amazon CloudWatch subscriptions.

###### CloudWatch subscription APIs

- [DescribeAwsNetworkPerformanceMetricSubscriptions](#nmip-cli-DescribeAggregatedAwsNetworkPerformanceMetricSubscriptions "#nmip-cli-DescribeAggregatedAwsNetworkPerformanceMetricSubscriptions")
- [DisableAwsNetworkPerformanceMetricSubscription](#nmip-cli-DisableAggregatedAwsNetworkPerformanceMetricSubscription "#nmip-cli-DisableAggregatedAwsNetworkPerformanceMetricSubscription")
- [EnableAwsNetworkPerformanceMetricSubscription](#nmip-cli-EnableNetworkPerformanceMetricSubscription "#nmip-cli-EnableNetworkPerformanceMetricSubscription")

## DescribeAwsNetworkPerformanceMetricSubscriptions

This provides details about any Infrastructure Performance metric subscriptions for
Amazon CloudWatch. For more information, see [DescribeAwsNetworkPerformanceMetricSubscriptions](../../../AWSEC2/latest/APIReference/API_DescribeAwsNetworkPerformanceMetricSubscriptions.md "../../../AWSEC2/latest/APIReference/API_DescribeAwsNetworkPerformanceMetricSubscriptions.md").

In this example, a `filter` is used where:

- The filter `Name` is `Source`.
- The `Value` of the filter `Name` is `us-east-1`.

In this example, CloudWatch subscriptions are being described for the Region
`us-east-1`.

```
aws ec2  --region us-east-1 describe-aws-network-performance-metric-subscriptions --filters Name=Source,Values=us-east-1
```

The results describe the `us-east-1` subscriptions, including the
following:

- `Source` is the originating location of the subscription. In this example, the
  `Source` is the Region `us-east-1`.
- `Destination` is the target location of the subscription. In this example, the
  `Destination` is the Region `us-east-2`.
- `Metric` indicates what type of metric is being requested. In this example,
  `aggregate-latency`, indicates that the performance metrics are aggregated and
  returned for latency.
- `Statistic` is the median value of the metric. In this example, `p50` is
  the statistic of all the data points gathered within those five minutes.

###### Note

`p50` is the only supported statistic.

- `Period` indicates the interval at which performance the `metric`
  is returned. In this example, `aggregated-latency` metrics are returned for every
  `five-minutes`.

```
{
    "Subscriptions": [
        {
            "Source": "us-east-1",
            "Destination": "us-east-2",
            "Metric": "aggregate-latency",
            "Statistic": "p50",
            "Period": "five-minutes"
        }
    ]
}
```

## DisableAwsNetworkPerformanceMetricSubscription

This disables Amazon CloudWatch subscriptions for Infrastructure Performance. For more information,
see [DisableAwsNetworkPerformanceMetricSubscription](../../../AWSEC2/latest/APIReference/API_DisableAwsNetworkPerformanceMetricSubscription.md "../../../AWSEC2/latest/APIReference/API_DisableAwsNetworkPerformanceMetricSubscription.md").

The following example disables subscriptions between a source Region,
`us-east-1`, and a destination Region, `us-east-2`. In
addition to the `source` and `destination` parameters, the request uses
the following parameters:

- `metric` indicates what type of metric is being requested. In this example,
  `aggregate-latency`, indicates that the performance metrics are aggregated and
  returned for latency.
- `statistic` is the median value of the metric. In this example, `p50` is
  the statistic of all the data points gathered within those five minutes.

###### Note

`p50` is the only supported statistic.

```
aws ec2 --region us-east-1 disable-aws-network-performance-metric-subscription --source us-east-1 --destination us-east-2 --metric aggregate-latency --statistic p50
```

The results return the following Boolean, `true`, indicating that the Amazon CloudWatch
subscription between the two Regions was disabled. CloudWatch will no longer receive
these metrics.

```
{
"Output": true
}
```

## EnableAwsNetworkPerformanceMetricSubscription

This enables Amazon CloudWatch subscriptions for Infrastructure Performance. For more information,
see [EnableAwsNetworkPerformanceMetricSubscription](../../../AWSEC2/latest/APIReference/API_EnableAwsNetworkPerformanceMetricSubscription.md "../../../AWSEC2/latest/APIReference/API_EnableAwsNetworkPerformanceMetricSubscription.md").

In the following example, subscriptions are enabled between a source
Region, `us-east-1`, and a destination Region,
`us-east-2`. In addition to the `source` and `destination`
parameters, the request also uses the following parameters:

- `metric` indicates what type of metric is being requested. In this example,
  `aggregate-latency`, indicates that the performance metrics are aggregated and
  returned for latency.
- `statistic` is the median value of the metric. In this example, `p50` is
  the statistic of all the data points gathered within those five minutes.

###### Note

`p50` is the only supported statistic.

```
aws ec2 --region us-east-1 enable-aws-network-performance-metric-subscription --source us-east-1 --destination us-east-2 --metric aggregate-latency --statistic p50
```

The results return the following Boolean, `true`, indicating that an Amazon CloudWatch subscription as been enabled between the two Regions. CloudWatch will begin receiving
metrics.

```
{
"Output": true
}
```
