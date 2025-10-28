# Constructing the JSON for predictive

scaling custom metrics with Amazon ECS

The following section contains examples for how to configure predictive scaling to query data from
CloudWatch. There are two different methods to configure this option, and the method that you choose affects
which format you use to construct the JSON for your predictive scaling policy. When you use metric
math, the format of the JSON varies further based on the metric math being performed.

1. To create a policy that gets data directly from other CloudWatch metrics provided by AWS or
   metrics that you publish to CloudWatch, see [Example predictive scaling policy with
   custom load and scaling metrics using the AWS CLI](#predictive-scaling-custom-metrics-example1 "#predictive-scaling-custom-metrics-example1").

## Example predictive scaling policy with

custom load and scaling metrics using the AWS CLI

To create a predictive scaling policy with custom load and scaling metrics with the AWS CLI, store
the arguments for `--predictive-scaling-configuration` in a JSON file named
`config.json`.

You start adding custom metrics by replacing the replaceable values in the following example with
those of your metrics and your target utilization.

```
{
  "MetricSpecifications": [
    {
      "TargetValue": `50`,
      "CustomizedScalingMetricSpecification": {
        "MetricDataQueries": [
          {
            "Id": "`scaling_metric`",
            "MetricStat": {
              "Metric": {
                "MetricName": "`MyUtilizationMetric`",
                "Namespace": "`MyNameSpace`",
                "Dimensions": [
                  {
                    "Name": "`MyOptionalMetricDimensionName`",
                    "Value": "`MyOptionalMetricDimensionValue`"
                  }
                ]
              },
              "Stat": "`Average`"
            }
          }
        ]
      },
      "CustomizedLoadMetricSpecification": {
        "MetricDataQueries": [
          {
            "Id": "`load_metric`",
            "MetricStat": {
              "Metric": {
                "MetricName": "`MyLoadMetric`",
                "Namespace": "`MyNameSpace`",
                "Dimensions": [
                  {
                    "Name": "`MyOptionalMetricDimensionName`",
                    "Value": "`MyOptionalMetricDimensionValue`"
                  }
                ]
              },
              "Stat": "`Sum`"
            }
          }
        ]
      }
    }
  ]
}
```

For more information, see [MetricDataQuery](../../../autoscaling/ec2/APIReference/API_MetricDataQuery.md "../../../autoscaling/ec2/APIReference/API_MetricDataQuery.md") in the
_Amazon EC2 Auto Scaling API Reference_.

###### Note

Following are some additional resources that can help you find metric names, namespaces,
dimensions, and statistics for CloudWatch metrics:

- For information about the available metrics for AWS services, see [AWS
  services that publish CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.md "../../../AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.md") in the
  _Amazon CloudWatch User Guide_.
- To get the exact metric name, namespace, and dimensions (if applicable) for a CloudWatch
  metric with the AWS CLI, see [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md").

To create this policy, run the [put-scaling-policy](../../../cli/latest/reference/autoscaling/put-scaling-policy.md "../../../cli/latest/reference/autoscaling/put-scaling-policy.md") command using the JSON file as input, as demonstrated in the
following example.

```
aws application-autoscaling put-scaling-policy --policy-name `my-predictive-scaling-policy` \
  --auto-scaling-group-name `my-asg` --policy-type PredictiveScaling \
  --predictive-scaling-configuration `file://config.json`
```

If successful, this command returns the policy's Amazon Resource Name (ARN).

```
{
  "PolicyARN": "arn:aws:autoscaling:region:account-id:scalingPolicy:2f4f5048-d8a8-4d14-b13a-d1905620f345:autoScalingGroupName/my-asg:policyName/my-predictive-scaling-policy",
  "Alarms": []
}
```
