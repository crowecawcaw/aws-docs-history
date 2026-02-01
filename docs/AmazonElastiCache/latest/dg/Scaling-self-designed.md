# On-demand scaling for Memcached clusters

ElastiCache for Memcached offers a fully managed, in-memory caching service that deploys, operates, and vertically scales Memcached in the AWS cloud.

**On-demand vertical scaling**

With vertical scaling, ElastiCache for Memcached provides a high-performance, distributed memory caching system widely used to speed up dynamic applications by alleviating database load. It stores data and objects in RAM, reducing the need to read from external data sources.

You can apply vertical scaling to existing node-based clusters as well as new ones. This can provide flexibility in resource allocation, allowing users to efficiently adapt to changing workloads without altering cluster architecture. This ability to scale improves performance by increasing cache capacity during high demand periods, and scaling down to optimize costs during low-demand periods. This simplifies operations, eliminates the need to create new clusters for shifting resource requirements, and enables quick responses to traffic fluctuations. Overall, vertical scaling for Memcached node-based clusters can help enhance cost efficiency, improve resource utilization, and even let users change their Memcached instance type. All making it easier for users to align their caching infrastructure with actual application needs.

###### Note

- Node type modifications are only available for node-based Memcached clusters with engine versions 1.5 or later.
- Auto Discovery must be enabled in order to make use of vertical scaling.

## Setting up on-demand vertical scaling for node-based Memcached clusters

You can configure on-demand vertical scaling for Memcached with `scale-config`, which contains two parameters:

1. **ScaleIntervalMinutes:** Time (in minutes) between scaling batches during the Memcached upgrade process
2. **ScalePercentage:** Percentage of nodes to scale concurrently during the Memcached upgrade process

**Converting an existing Memcached node type to a cache that can vertically scale via the CLI**

To convert an existing Memcached node-based cluster to a cache that can vertically scale, you can use `elasticache modify-cache-cluster` via the CLI.

```
aws elasticache modify-cache-cluster \
    --cache-cluster-id <your-cluster-id> \
    --cache-node-type <new-node-type> \
    --scale-config <scale-config> \
    --apply-immediately
```

**Setting up vertical scaling with the CLI**

To set up vertical scaling for a node-based Memcached cluster via the CLI, use `elasticache modify-cache-cluster` with `scale-config` and its parameters `ScalePercentage` and `ScaleIntervalMinutes`.

- **scale-interval-minutes:**This defines the time (in minutes) between scaling batches. This setting can range from 2-30 minutes. If no value is specified, the default value of 5 minutes is applied.
- **scale-percentage:**This specifies the percentage of nodes to scale concurrently in each batch. This setting can range from 10-100. The setting is rounded up when dividing, so for example if the result would be 49.5 a setting of 50 is applied. If no value is specified, the default value of 20 is applied.

These configuration options will enable you to fine-tune the scaling process according to your specific needs, balancing between minimizing cluster disruption and optimizing scaling speed. The scale-config parameter will only be applicable for Memcached engine types and will be ignored for other cache engines, ensuring backward compatibility with existing API usage for other clusters.

**API call**

```
aws elasticache modify-cache-cluster \
    --cache-cluster-id <your-cluster-id> \
    --cache-node-type <new-node-type> \
    --scale-config '{
            "ScalePercentage": 30,
            "ScaleIntervalMinutes": 2
          }'
    --apply-immediately
```

**Result:**

Returns the cluster ID and the pending change.

```
{
    "CacheCluster": {
        "CacheNodeType": "old_insance_type",
         ...
         ...
         "PendingModifiedValues": {
            "CacheNodeType": "new_instance_type"
         },
    }
}
```

**List your Memcached cache vertical scaling setting**

You can retrieve scaling options for your Memcached caches, and see what their current options are for vertical scaling.

**API call**

```
aws elasticache list-allowed-node-type-modifications --cache-cluster-id <your-cluster-id>

```

**Result:**

```
{
  "ScaleUpModifications": [
      "cache.x.xxxx",
      "cache.x.xxxx"
   	  ],
   "ScaleDownModifications": [
      "cache.x.xxxx",
      "cache.x.xxxx",
      "cache.x.xxxx"
      ]
}
```

**Vertical scaling for Memcached with the AWS Management Console**

Follow these steps to use the AWS Management Console to convert a node-based Memcached cluster to a vertically scalable cluster.

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. Select the Memcached cluster to convert.
3. Select the **Modify** tab.
4. Go to the **Cache settings** section, and select the desired **Node type**.
5. Select **Preview changes**, and review the changes.
6. Select **Modify**.

## Automated horizontal scaling for Memcached

ElastiCache now integrates with the AWS Application Auto Scaling (AAS) service to include automated horizontal scaling for Memcached clusters. You can define scaling policies through the AWS Application Auto Scaling service, and automatically adjust the number of nodes in Memcached clusters as needed, based on predefined metrics or schedules.

###### Note

Automated horizontal scaling is not currently available in the Beijing and Ningxia Regions.

These are the available methods for automatically horizontally scaling your node-based clusters.

- **Scheduled Scaling:**
  Scaling based on a schedule allows you to set your own scaling schedule for predictable load changes. For example, every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. You can configure Auto Scaling to increase capacity on Wednesday and decrease capacity on Friday.
- **Target Tracking:** With target tracking scaling policies, you choose a scaling metric and set a target value. Application Auto Scaling creates and manages the CloudWatch alarms that trigger the scaling policy and calculates the scaling adjustment based on the metric and the target value. The scaling policy adds or removes capacity as required to keep the metric at, or close to, the specified target value.

**How to set up horizontal scaling for a node-based Memcached cluster via the CLI**

When horizontal scaling a node-based Memcached cluster, you can use a target tracking policy, a scheduled policy, or both.

1. **Register a resource as scalable target**

Call the `RegisterScalableTarget` API in AWS Application Auto Scaling to register the target for the scalable dimension `elasticache:cache-cluster:Nodes`.

**API: ApplicationAutoScaling.RegisterScalableTarget**

Input:

```
{
	"ScalableDimension": "elasticache:cache-cluster:Nodes",
	"ResourceId": "cache-cluster/test-cluster-1",
	"ServiceNamespace": "elasticache",
	"MinCapacity": 20,
	"MaxCapacity": 50
}
```

2. **Create a Target tracking scaling policy**

Next, you can create a target tracking scaling policy for the resource by calling put scaling policy API. 3. **Predefined Metric**

Following is a policy that scales along the dimension of Cache Node, using the predefined metric `ElastiCacheCPUUtilization`, set at 50 for cluster test-cluster-1. When deleting nodes for scale-in, the last n nodes will be removed.

API: ApplicationAutoScaling.PutScalingPolicy

Input:

```
{
	"PolicyName": "cpu50-target-tracking-scaling-policy",
	"PolicyType": "TargetTrackingScaling",
	"TargetTrackingScalingPolicyConfiguration": {
		"TargetValue": 50,
		"PredefinedMetricSpecification": {
			"PredefinedMetricType": "ElastiCacheCPUUtilization"
			},
		"ScaleOutCooldown": 600,
		"ScaleInCooldown": 600
			},
	"ServiceNamespace": "elasticache",
	"ScalableDimension": "elasticache:cache-cluster:Nodes",
	"ResourceId": "cache-cluster/test-cluster-1"
}
```

Output:

```
{
	"PolicyARN": "arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/elasticache/cache-cluster/test-cluster-1:policyName/cpu50-target-tracking-scaling-policy",
	"Alarms": [
		{
		"AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:TargetTracking-elasticache/cache-cluster/test-cluster-1-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca",
		"AlarmName": "TargetTracking-elasticache/cache-cluster/test-cluster-1-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca"
		},
		{
		"AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:TargetTracking-elasticache/cache-cluster/test-cluster-1-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d",
		"AlarmName": "TargetTracking-elasticache/cache-cluster/test-cluster-1-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d"
		}
	]
}
```

4. **Custom Metric**

You can also set scaling policy on dimension by using a custom percentage that's based on the Cloudwatch metric.

Input:

```
{
	"PolicyName": "cpu50-target-tracking-scaling-policy",
	"PolicyType": "TargetTrackingScaling",
	"TargetTrackingScalingPolicyConfiguration": {
		"CustomizedMetricSpecification": {
			"Dimensions": [
				{
				"Name": "MyMetricDimension",
				"Value": "DimensionValue"
				}
				],
			"MetricName": "MyCustomMetric",
			"Namespace": "MyNamespace",
			"Statistic": "Average",
			"Unit": "Percent"
			},
		"TargetValue": 40,
		"ScaleOutCooldown": 600,
		"ScaleInCooldown": 600
		},
	"ServiceNamespace": "elasticache",
	"ScalableDimension": "elasticache:cache-cluster:Nodes",
	"ResourceId": "cache-cluster/test-cluster-1"
}
```

5. **Scheduled Actions**

When you need to scale out for a particular event and then scale in after the event, you can create two scheduled actions by calling the `PutScheduledAction` API.

**Policy 1: Scaling out**

The `at` command in `--schedule` schedules the action to be run once at a specified date and time in the future. The schedule field also supports rate (minute, hour, day etc) and cron (for cron expression).

At the date and time specified, Application Auto Scaling updates the `MinCapacity` and `MaxCapacity` values. Application Auto Scaling scales out to MinCapacity to put the cache nodes to 70.

**API: ApplicationAutoScaling.PutScheduledAction**

Input:

```
{
	"ResourceId": "elasticache:ache-cluster:test-cluster-1",
	"ScalableDimension": "elasticache:cache-cluster:Nodes",
		"ScalableTargetAction": {
			"MaxCapacity": 100,
			"MinCapacity": 70
			},
	"Schedule": "at(2020-05-20T17:05:00)",
	"ScheduledActionName": "ScalingOutScheduledAction",
	"ServiceNamespace": "elasticache",
}
```

**Policy 2: Scaling in**

At the date and time specified, Application Auto Scaling updates the table's `MinCapacity` and `MaxCapacity`, and scales in to `MaxCapacity` to return the cache nodes to 60.

**API: ApplicationAutoScaling.PutScheduledAction**

Input:

```
{
	"ResourceId": "elasticache:cache-cluster:test-cluster-1",
	"ScalableDimension": "elasticache:cache-cluster:Nodes",
	"ScalableTargetAction": {
		"MaxCapacity": 60,
		"MinCapacity": 40
		},
	"Schedule": "at(2020-05-21T17:05:00)",
	"ScheduledActionName": "ScalingInScheduledAction",
	"ServiceNamespace": "elasticache",
}
```

6. **View the Scaling Activities**

You can view the scaling activities using the `DescribeScalingActivities` API.

**API: ApplicationAutoScaling.DescribeScalingActivities**

Output:

```
{
	"ScalingActivities": [
		{
		"ScalableDimension": "elasticache:elasticache:DesiredCount",
		"Description": "Setting desired count to 30.",
		"ResourceId": "elasticache/cache-cluster/test-cluster-1",
		"ActivityId": "4d759079-a31f-4d0c-8468-504c56e2eecf",
		"StartTime": 1462574194.658,
		"elasticacheNamespace": "elasticache",
		"EndTime": 1462574276.686,
		"Cause": "monitor alarm TargetTracking-elasticache/cache-cluster/test-cluster-1-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca in state ALARM triggered policy cpu50-target-tracking-scaling-policy",
		"StatusMessage": "Failed to set desired count to 30",
		"StatusCode": "Failed"
		},
		{
		"ScalableDimension": "elasticache:elasticache:DesiredCount",
		"Description": "Setting desired count to 25.",
		"ResourceId": "elasticache/cache-cluster/test-cluster-1",
		"ActivityId": "90aff0eb-dd6a-443c-889b-b809e78061c1",
		"StartTime": 1462574254.223,
		"elasticacheNamespace": "elasticache",
		"EndTime": 1462574333.492,
		"Cause": "monitor alarm TargetTracking-elasticache/cache-cluster/test-cluster-1-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca in state ALARM triggered policy cpu50-target-tracking-scaling-policy",
		"StatusMessage": "Successfully set desired count to 25. Change successfully fulfilled by elasticache.",
		"StatusCode": "Successful"
		}
	]
}
```

7. **Edit/Delete Scaling Policy**

You can edit or delete policies by calling `PutScalingPolicy` API again, or by calling `DeleteScalingPolicy` or `DeleteScheduled` Action. 8. **De-register scalable targets**

You can de-register the scalable target through the `DeregisterScalableTarget` API. Deregistering a scalable target deletes the scaling policies and the scheduled actions that are associated with it.

**API: ApplicationAutoScaling.DeregisterScalableTarget**

Input:

```
{
	"ResourceId": "elasticache/cache-cluster/test-cluster-1",
	"ServiceNamespace": "elasticache",
	"ScalableDimension": "elasticache:cache-cluster:Nodes"
}
```

9. **Scaling Policy Cleanup**
10. **Multiple Scaling Policies**

You can create multiple scaling policies. Following are key callouts on behavior from [Auto scaling target tracking](../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md "../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md").

    * You can have multiple target tracking scaling policies for a scalable target, provided that each of them uses a different metric.
    * The intention of Application Auto Scaling is to always prioritize availability, so its behavior differs depending on whether the target tracking policies are ready for scale out or scale in. It will scale out the scalable target if any of the target tracking policies are ready for scale out, but will scale in only if all of the target tracking policies (with the scale-in portion enabled) are ready to scale in.
    * If multiple policies instruct the scalable target to scale out or in at the same time, Application Auto Scaling scales based on the policy that provides the largest capacity for both scale in and scale out. This provides greater flexibility to cover multiple scenarios and ensures that there is always enough capacity to process your application workloads.

###### Note

AWS Application Auto Scaling does not queue scaling policies. Application Auto Scaling will wait for the first scaling to complete, then cooldown, and then repeat the above algorithm.

**Automatically horizontally scale a node-based Memcached cluster via the AWS Management Console**

Follow these steps to use the AWS Management Console to convert an existing node-based Memcached cluster to a horizontally scalable cluster.

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. Select the Memcached cache to convert.
3. Go to the **Autoscaling** tab.
4. Select the scaling policy to apply, by selecting either **Add dynamic scaling** or **Add scheduled scaling**.
5. Fill in the details for the selected policy as needed.
6. Click **Create**.
