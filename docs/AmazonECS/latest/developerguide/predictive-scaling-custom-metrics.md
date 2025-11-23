# Advanced predictive scaling policy using custom

metrics for Amazon ECS

You can use predefined or custom metrics in a predictive scaling policy. Custom metrics are useful when
the predefined metrics, such as CPU, memory, etc) aren't enough to sufficiently describe your
application load.

When creating a predictive scaling policy with custom metrics, you can specify other CloudWatch metrics
provided by AWS. Alternatively, you can specify metrics that you define and publish yourself. You can
also use metric math to aggregate and transform existing metrics into a new time series that AWS doesn't
automatically track. An example is combining values in your data by calculating new sums or averages called
_aggregating_. The resulting data is called an
_aggregate_.

The following section contains best practices and examples of how to construct the JSON structure for the
policy.

## Prerequisites

To add custom metrics to your predictive scaling policy, you must have
`cloudwatch:GetMetricData` permissions.

To specify your own metrics instead of the metrics that AWS provides, you must first publish your
metrics to CloudWatch. For more information, see [Publishing custom metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md")
in the _Amazon CloudWatch User Guide_.

If you publish your own metrics, make sure to publish the data points at a minimum frequency of five
minutes. Data points are retrieved from CloudWatch based on the length of the period that it needs. For
example, the load metric specification uses hourly metrics to measure the load on your application.
CloudWatch uses your published metric data to provide a single data value for any one-hour period by
aggregating all data points with timestamps that fall within each one-hour period.

## Best

practices

The following best practices can help you use custom metrics more effectively:

- The most useful metric for the load metric specification is a metric that represents the load
  on an Amazon EC2 Auto Scaling group as a whole.
- The most useful metric for the scaling metric specification to scale by is an average
  throughput or utilization per task metric.
- The target utilization must match the type of scaling metric. For a policy configuration that
  uses CPU utilization, this is a target percentage, for example.
- If these recommendations are not followed, the forecasted future values of the time series
  will probably be incorrect. To validate that the data is correct, you can view the forecasted
  values in the console. Alternatively, after you create your predictive scaling policy, inspect
  the `LoadForecast` objects returned by a call to the [GetPredictiveScalingForecast](../../../autoscaling/application/APIReference/API_GetPredictiveScalingForecast.md "../../../autoscaling/application/APIReference/API_GetPredictiveScalingForecast.md") API.
- We strongly recommend that you configure predictive scaling in forecast only mode so that you
  can evaluate the forecast before predictive scaling starts actively scaling.

## Limitations

- You can query data points of up to 10 metrics in one metric specification.
- For the purposes of this limit, one expression counts as one metric.

## Troubleshooting a

predictive scaling policy with custom metrics

If an issue occurs while using custom metrics, we recommend that you do the following:

- If you encounter an issue in a blue/green deployment while using a search expression, make
  sure you created an search expression that's looking for a partial match and not an exact
  match. You should also check that the query is only finding Amazon EC2 Auto Scaling groups running in the specific
  application. For more information about the search expression syntax, see [CloudWatch search expression syntax](../../../AmazonCloudWatch/latest/monitoring/search-expression-syntax.md "../../../AmazonCloudWatch/latest/monitoring/search-expression-syntax.md") in the _Amazon CloudWatch User Guide_.
- The [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md")
  command validates an expression when you create your scaling policy. However, there's a
  possibility that this command might fail to identify the exact cause of the detected errors. To
  fix the issues, troubleshoot the errors that you receive in a response from a request to the
  [get-metric-data](../../../cli/latest/reference/cloudwatch/get-metric-data.md "../../../cli/latest/reference/cloudwatch/get-metric-data.md") command. You can also troubleshoot the expression from the CloudWatch
  console.
- You must specify `false` for `ReturnData` if
  `MetricDataQueries` specifies the SEARCH() function on its own without a math
  function like SUM(). This is because search expressions might return multiple time series, and
  a metric specification based on an expression can return only one time series.
- All metrics involved in a search expression should be of the same resolution.

## Example predictive scaling policy that

combines metrics using metric math (AWS CLI)

Sometimes, instead of specifying the metric directly, you might need to
first process its data in some way. For example, you might have an
application that pulls work from an Amazon SQS queue, and you might want to use
the number of items in the queue as criteria for predictive scaling. The
number of messages in the queue does not solely define the number of
instances that you need. Therefore, more work is needed to create a metric
that can be used to calculate the backlog per instance.

The following is an example predictive scaling policy for this scenario.
It specifies scaling and load metrics that are based on the Amazon SQS
`ApproximateNumberOfMessagesVisible` metric, which is the
number of messages available for retrieval from the queue. It also uses the
Amazon EC2 Auto Scaling `GroupInServiceInstances` metric and a math expression
to calculate the backlog per instance for the scaling metric.

```
aws application-autoscaling put-scaling-policy --policy-name `my-sqs-custom-metrics-policy` \
  --policy-type PredictiveScaling \
  --predictive-scaling-configuration `file://config.json`
  --service-namespace ecs \
  --resource-id service/MyCluster/test \
  "MetricSpecifications": [
    {
      "TargetValue": `100`,
      "CustomizedScalingMetricSpecification": {
        "MetricDataQueries": [
          {
            "Label": "Get the queue size (the number of messages waiting to be processed)",
            "Id": "`queue_size`",
            "MetricStat": {
              "Metric": {
                "MetricName": "`ApproximateNumberOfMessagesVisible`",
                "Namespace": "`AWS/SQS`",
                "Dimensions": [
                  {
                    "Name": "`QueueName`",
                    "Value": "`my-queue`"
                  }
                ]
              },
              "Stat": "`Sum`"
            },
            "ReturnData": false
          },
          {
            "Label": "Get the group size (the number of running instances)",
            "Id": "`running_capacity`",
            "MetricStat": {
              "Metric": {
                "MetricName": "`GroupInServiceInstances`",
                "Namespace": "`AWS/AutoScaling`",
                "Dimensions": [
                  {
                    "Name": "`AutoScalingGroupName`",
                    "Value": "`my-asg`"
                  }
                ]
              },
              "Stat": "`Sum`"
            },
            "ReturnData": false
          },
          {
            "Label": "Calculate the backlog per instance",
            "Id": "`scaling_metric`",
            "Expression": "`queue_size / running_capacity`",
            "ReturnData": true
          }
        ]
      },
      "CustomizedLoadMetricSpecification": {
        "MetricDataQueries": [
          {
            "Id": "`load_metric`",
            "MetricStat": {
              "Metric": {
                "MetricName": "`ApproximateNumberOfMessagesVisible`",
                "Namespace": "`AWS/SQS`",
                "Dimensions": [
                  {
                    "Name": "`QueueName`",
                    "Value": "`my-queue`"
                  }
                ],
              },
              "Stat": "`Sum`"
            },
            "ReturnData": true
          }
        ]
      }
    }
  ]
}
```

The example returns the policy's ARN.

```
{
  "PolicyARN": "arn:aws:autoscaling:region:account-id:scalingPolicy:2f4f5048-d8a8-4d14-b13a-d1905620f345:autoScalingGroupName/my-asg:policyName/my-sqs-custom-metrics-policy",
  "Alarms": []
}
```
