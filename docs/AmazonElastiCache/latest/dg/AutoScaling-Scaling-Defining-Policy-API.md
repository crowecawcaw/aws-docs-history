# Defining a scaling

policy

A target-tracking scaling policy configuration is represented by a JSON block that
the metrics and target values are defined in. You can save a scaling policy
configuration as a JSON block in a text file. You use that text file when invoking
the AWS CLI or the Application Auto Scaling API. For more information about policy
configuration syntax, see [TargetTrackingScalingPolicyConfiguration](../../../autoscaling/application/APIReference/API_TargetTrackingScalingPolicyConfiguration.md "../../../autoscaling/application/APIReference/API_TargetTrackingScalingPolicyConfiguration.md") in the Application Auto
Scaling API Reference.

The following options are available for defining a target-tracking scaling policy
configuration:

###### Topics

- [Using a predefined
  metric](#AutoScaling-Scaling-Predefined-Metric "#AutoScaling-Scaling-Predefined-Metric")
- [Using a custom
  metric](#AutoScaling-Scaling-Custom-Metric "#AutoScaling-Scaling-Custom-Metric")
- [Using cooldown
  periods](#AutoScaling-Scaling-Cooldown-periods "#AutoScaling-Scaling-Cooldown-periods")

## Using a predefined

metric

By using predefined metrics, you can quickly define a target-tracking scaling
policy for an ElastiCache for Valkey and Redis OSS cluster that works with target tracking in ElastiCache Auto
Scaling.

Currently, ElastiCache supports the following predefined metrics in NodeGroup Auto Scaling:

- **ElastiCachePrimaryEngineCPUUtilization** – The
  average value of the `EngineCPUUtilization` metric in CloudWatch
  across all primary nodes in the cluster.
- **ElastiCacheDatabaseMemoryUsageCountedForEvictPercentage**
  – The average value of the
  `DatabaseMemoryUsageCountedForEvictPercentage` metric in
  CloudWatch across all primary nodes in the cluster.
- **ElastiCacheDatabaseCapacityUsageCountedForEvictPercentage**
  – The average value of the
  `ElastiCacheDatabaseCapacityUsageCountedForEvictPercentage`
  metric in CloudWatch across all primary nodes in the cluster.

For more information about the `EngineCPUUtilization`,
`DatabaseMemoryUsageCountedForEvictPercentage` and
`DatabaseCapacityUsageCountedForEvictPercentage` metrics, see
[Monitoring use with CloudWatch Metrics](CacheMetrics.md "CacheMetrics.md"). To use a
predefined metric in your scaling policy, you create a target tracking
configuration for your scaling policy. This configuration must include a
`PredefinedMetricSpecification` for the predefined metric and a
TargetValue for the target value of that metric.

The following example describes a typical policy configuration for
target-tracking scaling for an ElastiCache for Valkey and Redis OSS cluster. In this configuration, the
`ElastiCachePrimaryEngineCPUUtilization` predefined metric is
used to adjust the cluster based on an average CPU utilization of 40
percent across all primary nodes in the cluster.

```
{
    "TargetValue": 40.0,
    "PredefinedMetricSpecification":
    {
        "PredefinedMetricType": "ElastiCachePrimaryEngineCPUUtilization"
    }
}
```

## Using a custom

metric

By using custom metrics, you can define a target-tracking scaling policy that
meets your custom requirements. You can define a custom metric based on any
ElastiCache metric that changes in proportion to scaling. Not all ElastiCache metrics
work for target tracking. The metric must be a valid utilization metric and
describe how busy an instance is. The value of the metric must increase or
decrease in proportion to the number of Shards in the cluster. This proportional
increase or decrease is necessary to use the metric data to proportionally scale
out or in the number of shards.

The following example describes a target-tracking configuration for a
scaling policy. In this configuration, a custom metric adjusts an ElastiCache for Redis OSS
cluster based on an average CPU utilization of 50 percent across all shards
in an cluster named `my-db-cluster`.

```
{
    "TargetValue": 50,
    "CustomizedMetricSpecification":
    {
        "MetricName": "EngineCPUUtilization",
        "Namespace": "AWS/ElastiCache",
        "Dimensions": [
            {
                "Name": "ReplicationGroup","Value": "my-db-cluster"
            },
            {
                "Name": "Role","Value": "PRIMARY"
            }
        ],
        "Statistic": "Average",
        "Unit": "Percent"
    }
}
```

## Using cooldown

periods

You can specify a value, in seconds, for `ScaleOutCooldown` to add
a cooldown period for scaling out your cluster. Similarly, you can add a value,
in seconds, for `ScaleInCooldown` to add a cooldown period for
scaling in your cluster. For more information, see [TargetTrackingScalingPolicyConfiguration](../../../autoscaling/application/APIReference/API_TargetTrackingScalingPolicyConfiguration.md "../../../autoscaling/application/APIReference/API_TargetTrackingScalingPolicyConfiguration.md") in the Application Auto
Scaling API Reference.

The following example describes a target-tracking configuration for a scaling
policy. In this configuration, the
`ElastiCachePrimaryEngineCPUUtilization` predefined metric is
used to adjust an ElastiCache for Redis OSS cluster based on an average CPU utilization of 40
percent across all primary nodes in that cluster. The configuration provides a
scale-in cooldown period of 10 minutes and a scale-out cooldown period of 5
minutes.

```
{
    "TargetValue": 40.0,
    "PredefinedMetricSpecification":
    {
        "PredefinedMetricType": "ElastiCachePrimaryEngineCPUUtilization"
    },
    "ScaleInCooldown": 600,
    "ScaleOutCooldown": 300
}
```
