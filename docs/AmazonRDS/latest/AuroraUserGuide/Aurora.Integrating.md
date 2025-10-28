# Amazon Aurora Auto Scaling with Aurora Replicas

To meet your connectivity and workload requirements, Aurora Auto Scaling dynamically adjusts the number of Aurora Replicas (reader
DB instances) provisioned for an Aurora DB cluster. Aurora Auto Scaling is available for both Aurora MySQL and Aurora PostgreSQL. Aurora Auto
Scaling enables your Aurora DB cluster to handle sudden increases in connectivity or workload. When the connectivity or workload
decreases, Aurora Auto Scaling removes unnecessary Aurora Replicas so that you don't pay for unused provisioned DB instances.

You define and apply a scaling policy to an Aurora DB cluster. The _scaling
policy_ defines the minimum and maximum number of Aurora Replicas that Aurora
Auto Scaling can manage. Based on the policy, Aurora Auto Scaling adjusts the number of Aurora
Replicas up or down in response to actual workloads, determined by using Amazon CloudWatch metrics
and target values.

###### Note

Aurora Auto Scaling doesn't apply to the workload on the writer DB instance. Aurora Auto Scaling helps with the workload only on the reader
instances.

You can use the AWS Management Console to apply a scaling policy based on a predefined metric.
Alternatively, you can use either the AWS CLI or Aurora Auto Scaling API to apply a scaling
policy based on a predefined or custom metric.

###### Topics

- [Before you begin](#Aurora.Integrating.AutoScaling.BYB "#Aurora.Integrating.AutoScaling.BYB")
- [Aurora Auto Scaling policies](#Aurora.Integrating.AutoScaling.Concepts "#Aurora.Integrating.AutoScaling.Concepts")
- [DB instance IDs and tagging](#Aurora.Integrating.AutoScaling.Concepts.Tagging "#Aurora.Integrating.AutoScaling.Concepts.Tagging")
- [Aurora Auto Scaling and Performance Insights](#aurora-auto-scaling-pi "#aurora-auto-scaling-pi")

## Before you begin

Before you can use Aurora Auto Scaling with an Aurora DB cluster, you must first create an Aurora DB cluster with a primary
(writer) DB instance. For more information about creating an Aurora DB cluster, see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

Aurora Auto Scaling only scales a DB cluster if the DB cluster is in the available state.

When Aurora Auto Scaling adds a new Aurora Replica, the new Aurora Replica is the same DB
instance class as the one used by the primary instance. For more information about DB
instance classes, see [Amazon Aurora DB instance classes](Concepts.md "Concepts.md"). Also, the promotion tier for new Aurora
Replicas is set to the last priority, which is 15 by default. This means that during a
failover, a replica with a better priority, such as one created manually, would be
promoted first. For more information, see [Fault tolerance for an Aurora DB
cluster](Concepts.md#Aurora.Managing.FaultTolerance "Concepts.md#Aurora.Managing.FaultTolerance").

Aurora Auto Scaling only removes Aurora Replicas that it created.

To benefit from Aurora Auto Scaling, your applications must support connections to new
Aurora Replicas. To do so, we recommend using the Aurora reader endpoint. You can use a
driver such as the AWS JDBC Driver. For more information, see [Connecting to an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

###### Note

Aurora global databases currently don't support Aurora Auto Scaling for secondary DB clusters.

## Aurora Auto Scaling policies

Aurora Auto Scaling uses a scaling policy to adjust the number of Aurora Replicas in an Aurora DB
cluster. Aurora Auto Scaling has the following components:

- A service-linked role
- A target metric
- Minimum and maximum capacity
- A cooldown period

###### Topics

- [Service linked role](#Aurora.Integrating.AutoScaling.Concepts.SLR "#Aurora.Integrating.AutoScaling.Concepts.SLR")
- [Target metric](#Aurora.Integrating.AutoScaling.Concepts.TargetMetric "#Aurora.Integrating.AutoScaling.Concepts.TargetMetric")
- [Minimum and maximum capacity](#Aurora.Integrating.AutoScaling.Concepts.Capacity "#Aurora.Integrating.AutoScaling.Concepts.Capacity")
- [Cooldown period](#Aurora.Integrating.AutoScaling.Concepts.Cooldown "#Aurora.Integrating.AutoScaling.Concepts.Cooldown")
- [Enable or disable scale-in activities](#Aurora.Integrating.AutoScaling.Concepts.ScaleIn "#Aurora.Integrating.AutoScaling.Concepts.ScaleIn")
- [Add, edit, or delete auto scaling policies](#Aurora.Integrating.AutoScaling.Concepts.AddEditDelete "#Aurora.Integrating.AutoScaling.Concepts.AddEditDelete")

### Service linked role

Aurora Auto Scaling uses the
`AWSServiceRoleForApplicationAutoScaling_RDSCluster` service-linked
role. For more information, see [Service-linked roles for Application Auto Scaling](../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md "../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md") in the
_Application Auto Scaling User Guide_.

### Target metric

In this type of policy, a predefined or custom metric and a target value for the metric is specified in a target-tracking
scaling policy configuration. Aurora Auto Scaling creates and manages CloudWatch alarms that trigger the scaling policy and
calculates the scaling adjustment based on the metric and target value. The scaling policy adds or removes Aurora Replicas as
required to keep the metric at, or close to, the specified target value. In addition to keeping the metric close to the
target value, a target-tracking scaling policy also adjusts to fluctuations in the metric due to a changing workload. Such a
policy also minimizes rapid fluctuations in the number of available Aurora Replicas for your DB cluster.

For example, take a scaling policy that uses the predefined average CPU utilization metric. Such a policy can keep CPU
utilization at, or close to, a specified percentage of utilization, such as 40 percent.

###### Note

For each Aurora DB cluster, you can create only one Auto Scaling policy for each target metric.

When you configure Aurora Auto Scaling, the target metric value is calculated as
the average of all reader instances in the cluster. This calculation is performed as
follows:

- Includes all reader instances in the Aurora cluster, regardless of whether
  they’re managed by Auto Scaling or added manually.
- Includes instances associated with custom endpoints. Custom endpoints
  don’t influence the calculation of target metrics.
- Does not include the cluster’s writer instance.

The metrics are derived from CloudWatch using the following dimensions:

- `DBClusterIdentifier`
- `Role=READER`

For example, consider an Aurora MySQL cluster with the following setup:

- **Manual instances (not controlled by Auto
  Scaling)**:
  - Writer with 50% CPU utilization
  - Reader 1 (custom endpoint: `custom-reader-1`) with 90%
    CPU utilization
  - Reader 2 (custom endpoint: `custom-reader-2`) with 90%
    CPU utilization

- **Auto Scaling instance**:
  - Reader 3 (added using Auto Scaling) with 10% CPU
    utilization

In this scenario, the target metric for the Auto Scaling policy is calculated as
follows:

```
Target metric = (CPU utilization of reader 1 + reader 2 + reader 3) / total number of readers

Target metric = (90 + 90 + 10) / 3 = 63.33%
```

The Auto Scaling policy uses this value to evaluate whether to scale in or scale
out based on the defined threshold.

Consider the following:

- Although custom endpoints determine how traffic is routed to specific
  readers, they don’t exclude readers from the metric calculation.
- Manual instances are always included in the target metric
  calculations.
- To avoid unexpected scaling behavior, make sure that the Auto Scaling
  configuration accounts for all reader instances in the cluster.
- If a cluster has no readers, the metric is not calculated, and the Auto
  Scaling policy alarms remain inactive. For the Auto Scaling policy to
  function effectively, at least one reader must be present at all
  times.

### Minimum and maximum capacity

You can specify the maximum number of Aurora Replicas to be managed by
Application Auto Scaling. This value must be set to 0–15, and must be equal to or greater
than the value specified for the minimum number of Aurora Replicas.

You can also specify the minimum number of Aurora Replicas to be managed by
Application Auto Scaling. This value must be set to 0–15, and must be equal to or less than
the value specified for the maximum number of Aurora Replicas.

There must be at least one reader DB instance for Aurora Auto Scaling to work. If the DB cluster has no reader instance, and you set the minimum capacity
to 0, then Aurora Auto Scaling won't work.

###### Note

The minimum and maximum capacity are set for an Aurora DB cluster. The specified values apply to all of the policies associated with that Aurora DB
cluster.

### Cooldown period

You can tune the responsiveness of a target-tracking scaling policy by adding cooldown periods that affect scaling your
Aurora DB cluster in and out. A cooldown period blocks subsequent scale-in or scale-out requests until the period expires.
These blocks slow the deletions of Aurora Replicas in your Aurora DB cluster for scale-in requests, and the creation of Aurora
Replicas for scale-out requests.

You can specify the following cooldown periods:

- A scale-in activity reduces the number of Aurora Replicas in your Aurora DB cluster. A scale-in cooldown period
  specifies the amount of time, in seconds, after a scale-in activity completes before another scale-in activity can
  start.
- A scale-out activity increases the number of Aurora Replicas in your Aurora DB cluster. A scale-out cooldown period
  specifies the amount of time, in seconds, after a scale-out activity completes before another scale-out activity can
  start.

###### Note

A scale-out cooldown period is ignored if a subsequent scale-out request is for a larger number of Aurora
Replicas than the first request.

If you don't set the scale-in or scale-out cooldown period, the default for each is 300 seconds.

### Enable or disable scale-in activities

You can enable or disable scale-in activities for a policy. Enabling scale-in activities allows the scaling policy to
delete Aurora Replicas. When scale-in activities are enabled, the scale-in cooldown period in the scaling policy applies to
scale-in activities. Disabling scale-in activities prevents the scaling policy from deleting Aurora Replicas.

###### Note

Scale-out activities are always enabled so that the scaling policy can create Aurora Replicas as needed.

### Add, edit, or delete auto scaling policies

You can add, edit, or delete auto scaling policies using the AWS Management Console, AWS CLI, or Application Auto Scaling API. For more information about adding, editing, or deleting auto scaling policies, see the following sections.

- [Adding an auto scaling policy to an Amazon Aurora DB cluster](Aurora.Integrating.AutoScaling.md "Aurora.Integrating.AutoScaling.md")
- [Editing an auto scaling policy for an Amazon Aurora DB cluster](Aurora.Integrating.AutoScaling.md "Aurora.Integrating.AutoScaling.md")
- [Deleting an auto scaling policy from your Amazon Aurora DB cluster](Aurora.Integrating.AutoScaling.md "Aurora.Integrating.AutoScaling.md")

## DB instance IDs and tagging

When a replica is added by Aurora Auto Scaling, its DB instance ID is prefixed by `application-autoscaling-`, for
example, `application-autoscaling-61aabbcc-4e2f-4c65-b620-ab7421abc123`.

The following tag is automatically added to the DB instance. You can view it on the **Tags** tab of the DB
instance detail page.

| Tag                                | Value                        |
| ---------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| application-autoscaling:resourceId | cluster:mynewcluster-cluster | For more information on Amazon RDS resource tags, see [Tagging Amazon Aurora and Amazon RDS resources](USER_Tagging.md "USER_Tagging.md"). ## Aurora Auto Scaling and Performance Insights You can use Performance Insights to monitor replicas that have been added by Aurora Auto Scaling, the same as with any Aurora reader DB instance. For more information on using Performance Insights to monitor Aurora DB clusters, see [Monitoring DB load with Performance Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md"). |
