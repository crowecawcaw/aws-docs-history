# Auto-scaling the number of replicas in an Amazon Neptune DB cluster

You can use Neptune auto-scaling to automatically adjust the number of Neptune
replicas in a DB cluster to meet your connectivity and workload requirements.
Auto-scaling lets your Neptune DB cluster handle increases in workload,
and then, when the workload decreases, auto-scaling removes unnecessary replicas
so you aren't paying for unused capacity.

You can only use auto-scaling with a Neptune DB cluster that already has one
primary writer instance and at least one read-replica instance (see [Amazon Neptune DB Clusters and Instances](feature-overview-db-clusters.md "feature-overview-db-clusters.md")).
Also, all read-replica instances in the cluster must be in an available state. If
any read-replica is in a state other than available, Neptune autoscaling does
nothing until every read-replica in the cluster is available.

See [Create Neptune cluster](get-started-create-cluster.md "get-started-create-cluster.md")
if you need to create a new cluster.

Using the AWS CLI, you define and apply a [scaling policy](#manage-console-autoscaling-define-policy "#manage-console-autoscaling-define-policy") to
the DB cluster. You can also use the AWS CLI to edit or delete your auto-scaling
policy. The policy specifies the following auto-scaling parameters:

- The minimum and maximum number of replicas to have in the cluster.
- A `ScaleOutCooldown` interval between replica(s)-addition scaling activity,
  and a `ScaleInCooldown` interval between replica(s)-deletion scaling activity.
- The CloudWatch metric and the metric trigger value for scaling up or down.
  The frequency of Neptune auto-scaling actions is damped down in several ways:

- Initially, for auto-scaling to add or delete a reader, the
  `CPUUtilization` high alarm has to be breached for at least 3 minutes or
  the low alarm has to be breached for at least 15 minutes.
- After that first addition or deletion, the frequency of subsequent
  Neptune auto-scaling actions is limited by the `ScaleOutCooldown`
  and `ScaleInCooldown` settings in the autoscaling policy.
  If the CloudWatch metric you're using reaches the high threshold you specified
  in your policy, and if the `ScaleOutCooldown` interval has elapsed
  since the last auto-scaling action, and if your DB cluster doesn't already have the
  maximum number of replicas that you set, Neptune auto-scaling creates a new
  replica using the same instance type as the DB cluster's primary instance.

Similarly, if the metric reaches the low threshold you specified and if
the `ScaleInCooldown` interval has elapsed since the last auto-scaling
action, and if your DB cluster has more than the minimum number of replicas
that you specified, Neptune auto-scaling deletes one of the replicas.

###### Note

Neptune auto-scaling only removes replicas that it created. It does
not remove pre-existing replicas.

Using the [neptune_autoscaling_config](parameters.md#parameters-db-cluster-parameters-neptune_autoscaling_config "parameters.md#parameters-db-cluster-parameters-neptune_autoscaling_config")
DB cluster parameter, you can also specify the instance type of the new read-replicas
that Neptune auto-scaling creates, the maintenance windows for those read-replicas,
and tags to be associated with each of the new read-replicas. You provide these
configuration settings in a JSON string as the value of the `neptune_autoscaling_config`
parameter, like this:

```
"{
  \"tags\": [
    { \"key\" : \"`reader tag-0 key`\", \"value\" : \"`reader tag-0 value`\" },
    { \"key\" : \"`reader tag-1 key`\", \"value\" : \"`reader tag-1 value`\" },
  ],
  \"maintenanceWindow\" : \"`wed:12:03-wed:12:33`\",
  \"dbInstanceClass\" : \"db.r5.xlarge\"
}"
```

Note that the quotation marks in the JSON string must all be escaped with a backslash
character (`\`). All whitespace in the string is optional, as usual.

Any of the three configuration settings not specified in the `neptune_autoscaling_config`
parameter are copied from the configuration of the DB cluster's primary writer instance.

When [auto-scaling](../../../autoscaling/plans/userguide.md "../../../autoscaling/plans/userguide.md") adds a new read-replica instance,
it prefixes the DB instance ID with `autoscaled-reader` (for example,
`autoscaled-reader-7r7t7z3lbd-20210828`). It also adds a tag to every
read-replica that it creates with the key `autoscaled-reader` and a value of
`TRUE`. You can see this tag on the **Tags** tab of the DB
instance detail page in the AWS Management Console.

```
 "key" : "autoscaled-reader",  "value" : "TRUE"
```

The promotion tier of all the read-replica instances created by auto-scaling is the lowest
priority, which is `15` by default. This means that during a failover, any replica
a higher priority, such as one that was created manually, would be promoted first. See
[Fault tolerance for a Neptune DB cluster](backup-restore-overview-fault-tolerance.md "backup-restore-overview-fault-tolerance.md").

Neptune auto-scaling is implemented using Application Auto Scaling with a [target
tracking scaling policy](../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md "../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md") that uses a Neptune [CPUUtilization](cw-metrics.md#cw-metrics-available "cw-metrics.md#cw-metrics-available") CloudWatch metric as a
predefined metric.

## Using auto-scaling in a Neptune serverless DB cluster

Neptune Serverless responds much more rapidly than Neptune auto-scaling when
demand exceeds an instance's capacity, and scales the instance up instead of adding
another instance. Where auto-scaling is designed to match relatively stable increases
or decreases in workload, serverless excels at handling rapid spikes and jitters in
demand.

Understanding their strengths, you can combine auto-scaling and serverless to
create a flexible infrastructure that will handle changes in your workload efficiently
and meet demand while minimizing cost.

To allow auto-scaling to work effectively together with serverless, it's
important to [configure
your serverless cluster's maxNCU](neptune-serverless-capacity-scaling.md#neptune-serverless-capacity-range-max "neptune-serverless-capacity-scaling.md#neptune-serverless-capacity-range-max") setting high enough to
accomodate spikes and brief changes in demand. Otherwise, transient changes
don't trigger serverless scaling, which can cause auto-scaling to spin up
many unnecessary additional instances. If `maxNCU` is set high enough,
serverless scaling can handle those changes faster and less expensively.

## How to enable auto-scaling for Amazon Neptune

Auto-scaling can only be enabled for a Neptune DB cluster using the AWS CLI. You
cannot enable auto-scaling using the AWS Management Console.

Also, autoscaling is not supported in the following Amazon regions:

- Africa (Cape Town): `af-south-1`
- Middle East (UAE): `me-central-1`
- AWS GovCloud (US-East): `us-gov-east-1`
- AWS GovCloud (US-West): `us-gov-west-1`

Enabling auto-scaling for a Neptune DB cluster involves three steps:

### 1. Register your DB cluster with Application Auto Scaling

The first step in enabling auto-scaling for a Neptune DB cluster is to register
the cluster with Application Auto Scaling, using the AWS CLI or one of the Application Auto Scaling SDKs. The cluster
must already have one primary instance and at least one read-replica instance:

For example, to register a cluster to be auto-scaled with from one to eight additional
replicas, you could use the AWS CLI [`register-scalable-target`](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md")
command as follows:

```
aws application-autoscaling register-scalable-target \
  --service-namespace neptune \
  --resource-id cluster:`(your DB cluster name)` \
  --scalable-dimension neptune:cluster:ReadReplicaCount \
  --min-capacity 1 \
  --max-capacity 8
```

This is equivalent to using the the [`RegisterScalableTarget`](../../../ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.md "../../../ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.md")
Application Auto Scaling API operation.

The AWS CLI `register-scalable-target` command takes the following parameters:

- **`service-namespace`**   –  
  Set to `neptune`.

This parameter is equivalent to the `ServiceNamespace` parameter in the
Application Auto Scaling API.

- **`resource-id`**   –  
  Set this to the resource identifier for your Neptune DB cluster. The resource type
  is `cluster`, which is followed by a colon ('`:`'),
  and then the name of your DB cluster.

This parameter is equivalent to the `ResourceID` parameter in the
Application Auto Scaling API.

- **`scalable-dimension`**   –  
  The scalable dimension in this case is the number of replica instances in the DB cluster, so
  you set this parameter to `neptune:cluster:ReadReplicaCount`.

This parameter is equivalent to the `ScalableDimension` parameter in the
Application Auto Scaling API.

- **`min-capacity`**   –  
  The minimum number of reader DB replica instances to be managed by Application Auto Scaling.
  This value should be set in the range from 0 to 15, and must be equal to or less than
  the value specified for the maximum number of Neptune Replicas in
  `max-capacity`. There must be at least one reader in the DB cluster
  for auto-scaling to work.

This parameter is equivalent to the `MinCapacity` parameter in the
Application Auto Scaling API.

- **`max-capacity`**   –  
  The maximum number of reader DB replica instances in the DB cluster, including
  pre-existing instances and new instances managed by Application Auto Scaling.
  This value must be set in the range from 0 to 15, and must be equal to or greater
  than the value specified for the minimum number of Neptune Replicas in
  `min-capacity`.

The `max-capacity` AWS CLI parameter is equivalent to the
`MaxCapacity` parameter in the Application Auto Scaling API.

When you register your DB cluster, Application Auto Scaling creates an `AWSServiceRoleForApplicationAutoScaling_NeptuneCluster`
service-linked role. For more information, see [Service-linked roles for Application auto-scaling](../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md "../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md") in the
_Application Auto Scaling User Guide_.

### 2. Define an autoscaling policy to use with your DB cluster

A target-tracking scaling policy is defined as a JSON text object that can also
be saved in a text file. For Neptune this policy currently can only use the Neptune
[CPUUtilization](cw-metrics.md#cw-metrics-available "cw-metrics.md#cw-metrics-available") CloudWatch metric
as a predefined metric named `NeptuneReaderAverageCPUUtilization`.

Here is an example target tracking scaling configuration policy for Neptune:

```
{
  "PredefinedMetricSpecification": { "PredefinedMetricType": "NeptuneReaderAverageCPUUtilization" },
  "TargetValue": 60.0,
  "ScaleOutCooldown" : 600,
  "ScaleInCooldown" : 600
}
```

The **`TargetValue`** element here
contains the percentage of CPU utilization above which auto-scaling _scales
out_ (that is, adds more replicas) and below which it _scales
in_ (that is, deletes replicas). In this case, the target percentage that
triggers scaling is `60.0`%.

The **`ScaleInCooldown`** element
specifies the amount of time, in seconds, after a scale-in activity completes
before another scale-in can start. The default is 300 seconds. Here, the value
of 600 specifies that at least ten minutes must elapse between the completion of
one replica deletion and the start of another one.

The **`ScaleOutCooldown`** element
specifies the amount of time, in seconds, after a scale-out activity completes
before another scale-out can start. The default is 300 seconds. Here, the value
of 600 specifies that at least ten minutes must elapse between the completion of
one replica addition and the start of another one.

The **`DisableScaleIn`** element
is a Boolean that if present and set to `true` disables scale-in
entirely, meaning that auto-scaling may add replicas but will never remove
any. By default, scale-in is enabled, and `DisableScaleIn` is
`false`.

###

After registering your Neptune DB cluster with Application Auto Scaling and defining a JSON scaling
policy in a text file, next apply the scaling policy to the registered DB cluster. You can
use the AWS CLI [`put-scaling-policy`](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") command to do this, with parameters like
the following:

```
aws application-autoscaling put-scaling-policy \
  --policy-name `(name of the scaling policy)` \
  --policy-type TargetTrackingScaling \
  --resource-id cluster:`(name of your Neptune DB cluster)` \
  --service-namespace neptune \
  --scalable-dimension neptune:cluster:ReadReplicaCount \
  --target-tracking-scaling-policy-configuration file://`(path to the JSON configuration file)`
```

When you have applied the auto-scaling policy, auto-scaling is enabled on
your DB cluster.

You can also use the AWS CLI [`put-scaling-policy`](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") command to update an existing
auto-scaling policy.

See also [PutScalingPolicy](../../../autoscaling/application/APIReference/API_PutScalingPolicy.md "../../../autoscaling/application/APIReference/API_PutScalingPolicy.md")
in the _Application Auto Scaling API Reference_.

## Removing auto-scaling from a Neptune DB cluster

To remove auto-scaling from a Neptune DB cluster, use the AWS CLI [delete-scaling-policy](../../../cli/latest/reference/application-autoscaling/delete-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/delete-scaling-policy.md") and [deregister-scalable-target](../../../cli/latest/reference/application-autoscaling/deregister-scalable-target.md "../../../cli/latest/reference/application-autoscaling/deregister-scalable-target.md")
commands.
