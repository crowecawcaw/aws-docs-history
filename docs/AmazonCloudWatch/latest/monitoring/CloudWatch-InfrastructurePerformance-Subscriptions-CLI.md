

# Manage subscriptions using the AWS CLI

Use the AWS CLI or APIs to get Infrastructure Performance metrics and to enable or disable Amazon CloudWatch subscriptions.

Use the following API operations to manage CloudWatch subscriptions:
+ [DescribeAwsNetworkPerformanceMetricSubscriptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAwsNetworkPerformanceMetricSubscriptions.html)
+ [DisableAwsNetworkPerformanceMetricSubscription](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableAwsNetworkPerformanceMetricSubscription.html)
+ [EnableAwsNetworkPerformanceMetricSubscription](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableAwsNetworkPerformanceMetricSubscription.html)

## DescribeAwsNetworkPerformanceMetricSubscriptions
<a name="CloudWatch-InfrastructurePerformance-Subscriptions-CLI-Describe"></a>

Describes your Infrastructure Performance metric subscriptions to Amazon CloudWatch. For more information, see [DescribeAwsNetworkPerformanceMetricSubscriptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAwsNetworkPerformanceMetricSubscriptions.html) in the *Amazon EC2 API Reference*.

The following example filters subscriptions by source Region us-east-1.

```
aws ec2 --region us-east-1 describe-aws-network-performance-metric-subscriptions --filters Name=Source,Values=us-east-1
```

The following is example output.

```json
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

The output contains the following fields:
+ **Source**: The source Region or Availability Zone.
+ **Destination**: The destination Region or Availability Zone.
+ **Metric**: The metric (`aggregate-latency`).
+ **Statistic**: The statistic (`p50`).
+ **Period**: The period (`five-minutes`).

**Note**  
`p50` is the only supported statistic.

## DisableAwsNetworkPerformanceMetricSubscription
<a name="CloudWatch-InfrastructurePerformance-Subscriptions-CLI-Disable"></a>

Disables Amazon CloudWatch subscriptions for Infrastructure Performance. For more information, see [DisableAwsNetworkPerformanceMetricSubscription](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableAwsNetworkPerformanceMetricSubscription.html) in the *Amazon EC2 API Reference*.

The following example disables the subscription between us-east-1 and us-east-2 for the `aggregate-latency` metric and the `p50` statistic.

**Note**  
`p50` is the only supported statistic.

```
aws ec2 --region us-east-1 disable-aws-network-performance-metric-subscription --source us-east-1 --destination us-east-2 --metric aggregate-latency --statistic p50
```

The following is example output.

```json
{
    "Output": true
}
```

## EnableAwsNetworkPerformanceMetricSubscription
<a name="CloudWatch-InfrastructurePerformance-Subscriptions-CLI-Enable"></a>

Enables Amazon CloudWatch subscriptions for Infrastructure Performance. For more information, see [EnableAwsNetworkPerformanceMetricSubscription](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableAwsNetworkPerformanceMetricSubscription.html) in the *Amazon EC2 API Reference*.

The following example enables the subscription between us-east-1 and us-east-2 for the `aggregate-latency` metric and the `p50` statistic.

**Note**  
`p50` is the only supported statistic.

```
aws ec2 --region us-east-1 enable-aws-network-performance-metric-subscription --source us-east-1 --destination us-east-2 --metric aggregate-latency --statistic p50
```

The following is example output.

```json
{
    "Output": true
}
```