# Disabling scale-in

activity

You can prevent the target-tracking scaling policy configuration from scaling
in your cluster by disabling scale-in activity. Disabling scale-in
activity prevents the scaling policy from deleting shards, while still allowing
the scaling policy to create them as needed.

You can specify a Boolean value for `DisableScaleIn` to enable or
disable scale in activity for your cluster. For more information, see [TargetTrackingScalingPolicyConfiguration](../../../autoscaling/application/APIReference/API_TargetTrackingScalingPolicyConfiguration.md "../../../autoscaling/application/APIReference/API_TargetTrackingScalingPolicyConfiguration.md") in the Application Auto
Scaling API Reference.

The following example describes a target-tracking configuration for a scaling
policy. In this configuration, the
`ElastiCachePrimaryEngineCPUUtilization` predefined metric
adjusts an ElastiCache for Valkey and Redis OSS cluster based on an average CPU utilization of 40 percent
across all primary nodes in that cluster. The configuration disables scale-in
activity for the scaling policy.

```
{
    "TargetValue": 40.0,
    "PredefinedMetricSpecification":
    {
        "PredefinedMetricType": "ElastiCachePrimaryEngineCPUUtilization"
    },
    "DisableScaleIn": true
}
```
