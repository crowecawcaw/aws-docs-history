# Applying a

scaling policy

After registering your cluster with ElastiCache for Valkey and Redis OSS auto scaling and defining a scaling
policy, you apply the scaling policy to the registered cluster. To apply a
scaling policy to an ElastiCache for Redis OSS cluster, you can use the AWS CLI or the Application
Auto Scaling API.

## Applying

a scaling policy using the AWS CLI

To apply a scaling policy to your ElastiCache for Valkey and Redis OSS cluster, use the [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") command with the following parameters:

- **--policy-name** – The name
  of the scaling policy.
- **--policy-type** – Set this
  value to `TargetTrackingScaling`.
- **--resource-id** – The
  resource identifier. For this parameter, the resource
  type is `ReplicationGroup` and the unique identifier is
  the name of the cluster, for example
  `replication-group/myscalablecluster`.
- **--service-namespace** – Set
  this value to `elasticache`.
- **--scalable-dimension** – Set
  this value to `elasticache:replication-group:NodeGroups`.
- **--target-tracking-scaling-policy-configuration**
  – The target-tracking scaling policy configuration to use for
  the cluster.

In the following example, you apply a target-tracking scaling policy named
`myscalablepolicy` to an ElastiCache for Valkey and Redis OSS cluster named
`myscalablecluster` with ElastiCache auto scaling. To do so, you
use a policy configuration saved in a file named `config.json`.

For Linux, macOS, or Unix:

```

aws application-autoscaling put-scaling-policy \
    --policy-name myscalablepolicy \
    --policy-type TargetTrackingScaling \
    --resource-id replication-group/myscalablecluster \
    --service-namespace elasticache \
    --scalable-dimension elasticache:replication-group:NodeGroups \
    --target-tracking-scaling-policy-configuration file://config.json
```

For Windows:

```

aws application-autoscaling put-scaling-policy ^
    --policy-name myscalablepolicy ^
    --policy-type TargetTrackingScaling ^
    --resource-id replication-group/myscalablecluster ^
    --service-namespace elasticache ^
    --scalable-dimension elasticache:replication-group:NodeGroups ^
    --target-tracking-scaling-policy-configuration file://config.json
```

## Applying a scaling policy using the API

To apply a scaling policy to your ElastiCache for Valkey and Redis OSS cluster, use the [PutScalingPolicy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") AWS CLI command with the following parameters:

- **--policy-name** – The name of the scaling policy.
- **--resource-id** – The resource identifier. For this parameter, the resource type is `ReplicationGroup`
  and the unique identifier is the name of the cluster, for example `replication-group/myscalablecluster`.
- **--service-namespace** – Set this value to `elasticache`.
- **--scalable-dimension** – Set this value to `elasticache:replication-group:NodeGroups`.
- **--target-tracking-scaling-policy-configuration** – The target-tracking scaling policy configuration to use for the cluster.

In the following example, you apply a target-tracking scaling policy named `myscalablepolicy` to an ElastiCache cluster named `myscalablecluster` with ElastiCache auto scaling.
You use a policy configuration based on the `ElastiCachePrimaryEngineCPUUtilization` predefined metric.

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
    "ScalableDimension": "elasticache:replication-group:NodeGroups",
    "PolicyType": "TargetTrackingScaling",
    "TargetTrackingScalingPolicyConfiguration": {
        "TargetValue": 40.0,
        "PredefinedMetricSpecification":
        {
            "PredefinedMetricType": "ElastiCachePrimaryEngineCPUUtilization"
        }
    }
}
```
