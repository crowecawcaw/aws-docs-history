# Amazon Neptune Global Cluster execution block

The Amazon Neptune Global Database execution block allows you to perform a _failover_ or
_switchover_ recovery workflow for a Neptune global database.

- Switchover – This operation was previously called _managed planned failover_.
  Use this approach for controlled scenarios, such as operational maintenance and other planned
  operational procedures where all the Amazon Neptune clusters and other services they interact with are
  in a healthy state. Because this feature synchronizes secondary DB clusters with the primary
  before making any other changes, RPO is 0 (no data loss).
- Failover – Use this approach to recover from an unplanned outage. With this
  approach, you perform a cross-Region failover to one of the
  secondary DB clusters in your Amazon Neptune global database. The recovery point objective (RPO) for this approach is typically
  a non-zero value measured in seconds. The amount of data loss
  depends on the Amazon Neptune global database replication lag across the AWS Regions at the time
  of the failure.

## Configuration

To configure a Amazon Neptune Global Database execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place.
For more information, see [Amazon Neptune Global Cluster execution block sample policy](security_iam_region_switch_neptune.md "security_iam_region_switch_neptune.md").

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **Neptune Global Database cluster name:** Enter the identifier for
   the global database.
4. **Cluster ARN for _Region_:** Enter the
   cluster ARN to use in each Region in the plan.
5. **Specify the option for Neptune database:** Choose
   either **Switchover** or **Failover (data loss)**, depending
   on your recovery requirements. Choose switchover for planned operations with zero data loss, or
   failover for unplanned outage recovery where some data loss is acceptable.
6. **Timeout:** Enter a timeout value.

Then, choose **Save step.**

## How it works

By configuring a Amazon Neptune Global Database execution block, you can failover or switchover global
databases as part of your application recovery.

This block supports both graceful and ungraceful execution modes:

- **Graceful** – Region switch performs the operation
  that you specified in the configuration (switchover or failover). If you configured switchover,
  Region switch calls `SwitchoverGlobalCluster`, which synchronizes all secondary clusters
  with the primary before promoting the target cluster (zero data loss). If you configured failover,
  Region switch calls `FailoverGlobalCluster`, which immediately promotes the target cluster
  without waiting for replication to complete (potential data loss).
- **Ungraceful** – If you have configured ungraceful
  settings, Region switch calls `FailoverGlobalCluster` with `AllowDataLoss=true`
  on the target secondary cluster. Amazon Neptune immediately promotes the target cluster to be the new
  primary without waiting for replication to complete. This may result in data loss equal to the
  replication lag at the time of failover.

If an ungraceful execution is requested while a switchover is already in progress, Region switch first
reverses the in-progress switchover (by switching back to the original primary), waits for the cluster
to become available, and then performs the failover to the target cluster.

In both modes, Region switch polls the global cluster status until the target cluster becomes the writer
and the cluster returns to an `available` state, or until the configured timeout is reached.

If the target cluster is already the writer when the block executes, Region switch detects this and
completes the step immediately without making any changes.

For more information about Amazon Neptune Global Database disaster recovery, see
[Using switchover or failover in Amazon Neptune global databases](../../../neptune/latest/userguide/neptune-global-database-failover.md "../../../neptune/latest/userguide/neptune-global-database-failover.md") in the Amazon Neptune User Guide.
