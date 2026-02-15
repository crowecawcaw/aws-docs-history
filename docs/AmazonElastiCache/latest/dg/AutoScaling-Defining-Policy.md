# Defining a scaling policy

A target-tracking scaling policy configuration is represented by a JSON block that
the metrics and target values are defined in. You can save a scaling policy
configuration as a JSON block in a text file. You use that text file when invoking
the AWS CLI or the Application Auto Scaling API. For more information about policy
configuration syntax, see [TargetTrackingScalingPolicyConfiguration](../../../ApplicationAutoScaling/latest/APIReference/API_TargetTrackingScalingPolicyConfiguration.md "../../../ApplicationAutoScaling/latest/APIReference/API_TargetTrackingScalingPolicyConfiguration.md") in the _Application
Auto Scaling API Reference_.

The following options are available for defining a target-tracking scaling policy
configuration:

###### Topics

- [Using a predefined
  metric](#AutoScaling-Predefined-Metric "#AutoScaling-Predefined-Metric")
- [Editing a scaling policy](AutoScaling-Editing-Policy.md "AutoScaling-Editing-Policy.md")
- [Deleting a scaling policy](AutoScaling-Deleting-Policy.md "AutoScaling-Deleting-Policy.md")
- [Use CloudFormation for Auto Scaling
  policies](AutoScaling-with-Cloudformation.md "AutoScaling-with-Cloudformation.md")
- [Scheduled scaling](AutoScaling-with-Scheduled-Scaling-Replicas.md "AutoScaling-with-Scheduled-Scaling-Replicas.md")

## Using a predefined

metric

A target-tracking scaling policy configuration is represented by a JSON block that the metrics and target values are defined in.
You can save a scaling policy configuration as a JSON block in a text file. You use that text file when invoking the AWS CLI or the Application Auto Scaling API.
For more information about policy configuration syntax, see [TargetTrackingScalingPolicyConfiguration](../../../ApplicationAutoScaling/latest/APIReference/API_TargetTrackingScalingPolicyConfiguration.md "../../../ApplicationAutoScaling/latest/APIReference/API_TargetTrackingScalingPolicyConfiguration.md")
in the _Application Auto Scaling API Reference_.

The following options are available for defining a target-tracking scaling policy configuration:

###### Topics

- [Using a predefined metric](#AutoScaling-Predefined-Metric "#AutoScaling-Predefined-Metric")
- [Using a custom metric](#AutoScaling-Custom-Metric "#AutoScaling-Custom-Metric")
- [Using cooldown periods](#AutoScaling-Using-Cooldowns "#AutoScaling-Using-Cooldowns")
- [Disabling scale-in
  activity](#AutoScaling-Disabling-Scalein "#AutoScaling-Disabling-Scalein")
- [Applying a scaling
  policy to an ElastiCache for Valkey and Redis OSS cluster](#AutoScaling-Applying-Policy "#AutoScaling-Applying-Policy")

### Using a predefined metric

By using predefined metrics, you can quickly define a target-tracking scaling policy for an ElastiCache for Valkey and Redis OSS cluster that works with target tracking in ElastiCache Auto Scaling.
Currently, ElastiCache supports the following predefined metric in ElastiCache Replicas Auto Scaling:

`ElastiCacheReplicaEngineCPUUtilization` – The average value of the EngineCPUUtilization metric in CloudWatch across all replicas in the cluster. You can find the aggregated metric value in CloudWatch under ElastiCache `ReplicationGroupId, Role` for required ReplicationGroupId and Role Replica.

To use a predefined metric in your scaling policy, you create a target tracking configuration for your scaling policy. This configuration must include a `PredefinedMetricSpecification` for the predefined metric and a `TargetValue` for the target value of that metric.

### Using a custom metric

By using custom metrics, you can define a target-tracking scaling policy that meets your custom requirements.
You can define a custom metric based on any ElastiCache for Valkey and Redis OSS metric that changes in proportion to scaling.
Not all ElastiCache metrics work for target tracking. The metric must be a valid utilization metric and describe how busy an instance is.
The value of the metric must increase or decrease in proportion to the number of replicas in the cluster.
This proportional increase or decrease is necessary to use the metric data to proportionally increase or decrease the number of replicas.

###### Example

The following example describes a target-tracking configuration for a scaling policy. In this configuration, a custom metric adjusts
a cluster based on an average CPU utilization of 50 percent across all replicas in an cluster named `my-db-cluster`.

```
{"TargetValue": 50,
    "CustomizedMetricSpecification":
    {"MetricName": "EngineCPUUtilization",
        "Namespace": "AWS/ElastiCache",
        "Dimensions": [
            {"Name": "ReplicationGroup","Value": "my-db-cluster"},
            {"Name": "Role","Value": "REPLICA"}
        ],
        "Statistic": "Average",
        "Unit": "Percent"
    }
}

```

### Using cooldown periods

You can specify a value, in seconds, for `ScaleOutCooldown` to add
a cooldown period for scaling out your cluster. Similarly, you can add a value,
in seconds, for `ScaleInCooldown` to add a cooldown period for
scaling in your cluster. For more information about `ScaleInCooldown`
and `ScaleOutCooldown`, see [TargetTrackingScalingPolicyConfiguration](../../../ApplicationAutoScaling/latest/APIReference/API_TargetTrackingScalingPolicyConfiguration.md "../../../ApplicationAutoScaling/latest/APIReference/API_TargetTrackingScalingPolicyConfiguration.md") in the
_Application Auto Scaling API Reference_. The following
example describes a target-tracking configuration for a scaling policy. In this
configuration, the `ElastiCacheReplicaEngineCPUUtilization`predefined
metric is used to adjust a cluster based on an average CPU utilization
of 40 percent across all replicas in that cluster. The configuration provides a
scale-in cooldown period of 10 minutes and a scale-out cooldown period of 5
minutes.

```
{"TargetValue": 40.0,
    "PredefinedMetricSpecification":
    {"PredefinedMetricType": "ElastiCacheReplicaEngineCPUUtilization"
    },
    "ScaleInCooldown": 600,
    "ScaleOutCooldown": 300
}

```

### Disabling scale-in

activity

You can prevent the target-tracking scaling policy configuration from scaling
in your ElastiCache for Valkey and Redis OSS cluster by disabling scale-in activity. Disabling scale-in
activity prevents the scaling policy from deleting replicas, while still
allowing the scaling policy to add them as needed.

You can specify a Boolean value for `DisableScaleIn` to enable or
disable scale in activity for your cluster. For more information about
`DisableScaleIn`, see [TargetTrackingScalingPolicyConfiguration](../../../ApplicationAutoScaling/latest/APIReference/API_TargetTrackingScalingPolicyConfiguration.md "../../../ApplicationAutoScaling/latest/APIReference/API_TargetTrackingScalingPolicyConfiguration.md") in the
_Application Auto Scaling API Reference_.

###### Example

The following example describes a target-tracking configuration for a
scaling policy. In this configuration, the
`ElastiCacheReplicaEngineCPUUtilization` predefined metric
adjusts a cluster based on an average CPU utilization of 40 percent
across all replicas in that cluster. The configuration disables scale-in
activity for the scaling policy.

```
{"TargetValue": 40.0,
    "PredefinedMetricSpecification":
    {"PredefinedMetricType": "ElastiCacheReplicaEngineCPUUtilization"
    },
    "DisableScaleIn": true
}

```

### Applying a scaling

policy to an ElastiCache for Valkey and Redis OSS cluster

After registering your cluster with ElastiCache for Valkey and Redis OSS auto scaling and defining a scaling
policy, you apply the scaling policy to the registered cluster. To apply a
scaling policy to an ElastiCache for Valkey and Redis OSS cluster, you can use the AWS CLI or the Application
Auto Scaling API.

**Using the AWS CLI**

To apply a scaling policy to your ElastiCache for Valkey and Redis OSS cluster, use the [put-scaling-policy](../../../cli/latest/reference/autoscaling/put-scaling-policy.md "../../../cli/latest/reference/autoscaling/put-scaling-policy.md") command with the following parameters:

- --policy-name – The name of the scaling policy.
- --policy-type – Set this value to `TargetTrackingScaling`.
- --resource-id – The resource identifier for the cluster. For
  this parameter, the resource type is ReplicationGroup and the unique
  identifier is the name of the cluster, for example
  `replication-group/myscalablecluster`.
- --service-namespace – Set this value to elasticache.
- --scalable-dimension – Set this value to
  `elasticache:replication-group:Replicas`.
- --target-tracking-scaling-policy-configuration – The target-tracking
  scaling policy configuration to use for the cluster.

###### Example

In the following example, you apply a target-tracking scaling policy named
`myscalablepolicy` to a cluster named
`myscalablecluster` with ElastiCache auto scaling. To do so, you
use a policy configuration saved in a file named `config.json`.

For Linux, macOS, or Unix:

```

aws application-autoscaling put-scaling-policy \
    --policy-name myscalablepolicy \
    --policy-type TargetTrackingScaling \
    --resource-id replication-group/myscalablecluster \
    --service-namespace elasticache \
    --scalable-dimension elasticache:replication-group:Replicas \
    --target-tracking-scaling-policy-configuration file://config.json
```

```
{"TargetValue": 40.0,
    "PredefinedMetricSpecification":
    {"PredefinedMetricType": "ElastiCacheReplicaEngineCPUUtilization"
    },
    "DisableScaleIn": true
}

```

For Windows:

```

aws application-autoscaling put-scaling-policy ^
    --policy-name myscalablepolicy ^
    --policy-type TargetTrackingScaling ^
    --resource-id replication-group/myscalablecluster ^
    --service-namespace elasticache ^
    --scalable-dimension elasticache:replication-group:Replicas ^
    --target-tracking-scaling-policy-configuration file://config.json
```

**Using the API**

To apply a scaling policy to your ElastiCache cluster with the Application Auto
Scaling API, use the [PutScalingPolicy](../../../autoscaling/application/APIReference/API_PutScalingPolicy.md "../../../autoscaling/application/APIReference/API_PutScalingPolicy.md") Application Auto Scaling API operation with the
following parameters:

- PolicyName – The name of the scaling policy.
- PolicyType – Set this value to `TargetTrackingScaling`.
- ResourceID – The resource identifier for the cluster. For this
  parameter, the resource type is ReplicationGroup and the unique
  identifier is the name of the ElastiCache for Redis OSS cluster, for example
  `replication-group/myscalablecluster`.
- ServiceNamespace – Set this value to elasticache.
- ScalableDimension – Set this value to
  `elasticache:replication-group:Replicas`.
- TargetTrackingScalingPolicyConfiguration – The target-tracking scaling
  policy configuration to use for the cluster.

###### Example

In the following example, you apply a target-tracking scaling policy named
`scalablepolicy` to an cluster named
`myscalablecluster` with ElastiCache auto scaling. You use a
policy configuration based on the
`ElastiCacheReplicaEngineCPUUtilization` predefined metric.

```

POST / HTTP/1.1
Host: autoscaling.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 219
X-Amz-Target: AnyScaleFrontendService.PutScalingPolicy
X-Amz-Date: 20160506T182145Z
User-Agent: aws-cli/1.10.23 Python/2.7.11 Darwin/15.4.0 botocore/1.4.8
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS
{
    "PolicyName": "myscalablepolicy",
    "ServiceNamespace": "elasticache",
    "ResourceId": "replication-group/myscalablecluster",
    "ScalableDimension": "elasticache:replication-group:Replicas",
    "PolicyType": "TargetTrackingScaling",
    "TargetTrackingScalingPolicyConfiguration": {
        "TargetValue": 40.0,
        "PredefinedMetricSpecification":
        {
            "PredefinedMetricType": "ElastiCacheReplicaEngineCPUUtilization"
        }
    }
}
```
