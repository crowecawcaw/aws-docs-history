# Amazon EMR cluster error: HDFS replication factor error

When you remove a core node from a core [instance group](emr-uniform-instance-group.md "emr-uniform-instance-group.md") or
[instance fleet](emr-instance-fleet.md "emr-instance-fleet.md"), Amazon EMR
might run into an HDFS replication error. This error happens when you remove core nodes and the number
core nodes falls below the configured [dfs.replication factor](../ReleaseGuide/emr-hdfs-config.md "../ReleaseGuide/emr-hdfs-config.md")
for the Hadoop Distributed File System (HDFS). As such, Amazon EMR can't safely perform the operation. To determine the
default value of the `dfs.replication` configuration, [HDFS configuration](../ReleaseGuide/emr-hdfs-config.md "../ReleaseGuide/emr-hdfs-config.md").

## Possible causes

See the following for the possible causes of HDFS replication factor error:

- If you [manually resize](emr-manage-resize.md "emr-manage-resize.md") a core instance group or instance fleet below the configured
  `dfs.replication` factor.
- Your policies for [managed scaling](emr-managed-scaling.md "emr-managed-scaling.md") or [autoscaling](emr-automatic-scaling.md "emr-automatic-scaling.md") might allow for scaling to reduce the number of core nodes below the
  threshold of `dfs.replication`.
- This error can also occur if Amazon EMR tries to [replace](emr-plan-node-replacement.md "emr-plan-node-replacement.md") an unhealthy core node
  when a cluster has the minimal number of core nodes defined by
  `dfs.replication`.

## Solutions and best practices

See the following for solutions and best practices:

- When you manually resize an Amazon EMR cluster, don't scale down below the
  `dfs.replication` as Amazon EMR can't safely complete the resize.
- When you use managed scaling or autoscaling, make sure that the minimum capacity of your
  cluster isn't lower than the `dfs.replication` factor.
- The number of core instances should be at least `dfs.replication` plus one.
  This makes sure that Amazon EMR can successfully replace an unhealthy core node
  if you enabled unhealthy core replacement.

###### Important

Failure of a single core node can lead to HDFS data loss if you set
`dfs.replication` to 1. If
your cluster has HDFS storage, we recommend that you configure the cluster with at least four core nodes
for production workloads to avoid data loss and also set the `dfs.replication` factor to at least 2.
