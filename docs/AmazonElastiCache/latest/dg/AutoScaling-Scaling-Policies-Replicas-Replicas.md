# Target tracking scaling

policies

With target tracking scaling policies, you select a metric and set a target value.
ElastiCache for Valkey and Redis OSS AutoScaling creates and manages the CloudWatch alarms that trigger the scaling
policy and calculates the scaling adjustment based on the metric and the target
value. The scaling policy adds or removes replicas uniformly across all shards as
required to keep the metric at, or close to, the specified target value. In addition
to keeping the metric close to the target value, a target tracking scaling policy
also adjusts to the fluctuations in the metric due to a fluctuating load pattern and
minimizes rapid fluctuations in the capacity of the fleet.

## Auto Scaling criteria

for replicas

Your Auto Scaling policy defines the following predefined metric for your
cluster:

`ElastiCacheReplicaEngineCPUUtilization`: The AVG EngineCPU
utilization threshold aggregated across all replicas that ElastiCache uses to trigger
an auto-scaling operation. You can set the utilization target between 35 percent
and 70 percent.

When the service detects that your
`ElastiCacheReplicaEngineCPUUtilization` metric is equal to or
greater than the Target setting, it will increase replicas across your shards
automatically. ElastiCache scales out your cluster replicas by a count equal to the
larger of two numbers: Percent variation from Target and one replica. For
scale-in, ElastiCache won't auto scale-in unless the overall metric value is
below 75 percent of your defined Target.

For a scale-out example, if you have 5 shards and 1 replica each:

If your Target breaches by 30 percent, ElastiCache for Valkey and Redis OSS scales out by 1 replica
(max(0.3, default 1)) across all shards. which results in 5 shards with 2
replicas each,

For a scale-in example, if you have selected Target value of 60 percent,
ElastiCache for Valkey and Redis OSS won't auto scale-in until the metric is less than or equal to 45
percent (25 percent below the Target 60 percent).

### Auto Scaling

considerations

Keep the following considerations in mind:

- A target tracking scaling policy assumes that it should perform
  scale out when the specified metric is above the target value. You
  cannot use a target tracking scaling policy to scale out when the
  specified metric is below the target value. ElastiCache for Valkey and Redis OSS scales out
  replicas by maximum of (% deviation rounded off from Target, default

1.  of existing replicas across all shards in the cluster.

- A target tracking scaling policy does not perform scaling when the
  specified metric has insufficient data. It does not perform scale in
  because it does not interpret insufficient data as low utilization.
- You may see gaps between the target value and the actual metric
  data points. This is because ElastiCache Auto Scaling always acts
  conservatively by rounding up or down when it determines how much
  capacity to add or remove. This prevents it from adding insufficient
  capacity or removing too much capacity.
- To ensure application availability, the service scales out
  proportionally to the metric as fast as it can, but scales in more
  gradually with max scale in of 1 replica across the shards in the
  cluster.
- You can have multiple target tracking scaling policies for an
  ElastiCache for Valkey and Redis OSS cluster, provided that each of them uses a different metric.
  The intention of Auto Scaling is to always prioritize
  availability, so its behavior differs depending on whether the
  target tracking policies are ready for scale out or scale in. It
  will scale out the service if any of the target tracking policies
  are ready for scale out, but will scale in only if all of the target
  tracking policies (with the scale-in portion enabled) are ready to
  scale in.
- Do not edit or delete the CloudWatch alarms that ElastiCache Auto Scaling
  manages for a target tracking scaling policy. Auto Scaling
  deletes the alarms automatically when you delete the scaling policy
  or deleting the cluster.
- ElastiCache Auto Scaling doesn't prevent you from manually modifying
  replicas across shards. These manual adjustments don't affect
  any existing CloudWatch alarms that are attached to the scaling policy but
  can impact metrics that may trigger these CloudWatch alarms.
- These CloudWatch alarms managed by Auto Scaling are defined over the AVG
  metric across all the shards in the cluster. So, having hot shards
  can result in either scenario of:
  - scaling when not required due to load on a few hot shards
    triggering a CloudWatch alarm
  - not scaling when required due to aggregated AVG across all
    shards affecting alarm not to breach.

- ElastiCache default limits on nodes per cluster still applies. So, when
  opting for Auto Scaling and if you expect maximum nodes to be more
  than default limit, request a limit increase at [AWS Service Limits](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") and choose the limit type
  **Nodes per cluster per instance type**.
- Ensure that you have enough ENIs (Elastic Network Interfaces)
  available in your VPC, which are required during scale-out. For more
  information, see [Elastic network interfaces](../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md "../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md").
- If there is not enough capacity available from EC2, ElastiCache Auto
  Scaling will not scale out until either the capacity is available, or if
  you manually modify the cluster to the instance types that have
  enough capacity.
- ElastiCache Auto Scaling doesn't support scaling of replicas with
  a cluster having `ReservedMemoryPercent` less than 25
  percent. For more information, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md "redis-memory-management.md").
