# Cluster scale-down options for Amazon EMR clusters

###### Note

Scale-down behavior options are no longer supported since Amazon EMR release 5.10.0.
Because of the introduction of per-second billing in Amazon EC2, the default scale-down
behavior for Amazon EMR clusters is now terminate at task completion.

With Amazon EMR releases 5.1.0 through 5.9.1, there are two options for scale-down
behavior: terminate at the instance-hour boundary for Amazon EC2 billing, or terminate at
task completion. Starting with Amazon EMR release 5.10.0, the setting for termination at
instance-hour boundary is deprecated because of the introduction of per-second billing
in Amazon EC2. We do not recommend specifying termination at the instance-hour boundary in
versions where the option is available.

###### Warning

If you use the AWS CLI to issue a `modify-instance-groups` with
`EC2InstanceIdsToTerminate`, these instances are terminated
immediately, without consideration for these settings, and regardless of the status
of applications running on them. Terminating an instance in this way risks data loss
and unpredictable cluster behavior.

When terminate at task completion is specified, Amazon EMR deny lists and drains tasks from
nodes before terminating the Amazon EC2 instances. With either behavior specified, Amazon EMR does
not terminate Amazon EC2 instances in core instance groups if it could lead to HDFS
corruption.

## Terminate at task completion

Amazon EMR allows you to scale down your cluster without affecting your workload. Amazon EMR attempts to gracefully decommission YARN, HDFS, and other daemons
on core and task nodes during a resize down operation without losing data or interrupting jobs. Amazon EMR only reduces
instance group size if the work assigned to the groups has completed and they are
idle. For YARN NodeManager Graceful Decommission, you can manually adjust the time a
node waits for decommissioning.

###### Note

When graceful decommissioning occurs, there can be data loss. Be sure to back up your data.

###### Important

It is possible that HDFS data can be permanently lost during the graceful replacement of an unhealthy core
instance. We recommend that you always back up your data.

This time is set using a property in the `YARN-site` configuration
classification. Using Amazon EMR release 5.12.0 and higher, specify the
`YARN.resourcemanager.nodemanager-graceful-decommission-timeout-secs`
property. Using earlier Amazon EMR releases, specify the
`YARN.resourcemanager.decommissioning.timeout` property.

If there are still running containers or YARN applications when the
decommissioning timeout passes, the node is forced to be decommissioned and YARN
reschedules affected containers on other nodes. The default value is 3600s (one
hour). You can set this timeout to be an arbitrarily high value to force graceful
reduction to wait longer. For more information, see [Graceful Decommission of YARN nodes](http://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/GracefulDecommission.html "http://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/GracefulDecommission.html") in the Apache Hadoop
documentation.

### Task node groups

Amazon EMR intelligently selects instances that do not have tasks that are running
against any step or application, and removes those instances from a cluster
first. If all instances in the cluster are in use, Amazon EMR waits for tasks to
complete on an instance before removing it from the cluster. The default wait
time is 1 hour. This value can be changed with the
`YARN.resourcemanager.decommissioning.timeout` setting. Amazon EMR
dynamically uses the new setting. You can set this to an arbitrarily large
number to ensure that Amazon EMR doesn't terminate any tasks while reducing the
cluster size.

### Core node groups

On core nodes, both YARN NodeManager and HDFS DataNode daemons must be
decommissioned for the instance group to reduce. For YARN, graceful reduction
ensures that a node marked for decommissioning is only transitioned to the
`DECOMMISSIONED` state if there are no pending or incomplete
containers or applications. The decommissioning finishes immediately if there
are no running containers on the node at the beginning of decommissioning.

For HDFS, graceful reduction ensures that the target capacity of HDFS is large
enough to fit all existing blocks. If the target capacity is not large enough,
only a partial amount of core instances are decommissioned such that the
remaining nodes can handle the current data residing in HDFS. You should ensure
additional HDFS capacity to allow further decommissioning. You should also try
to minimize write I/O before attempting to reduce instance groups. Excessive
write I/O might delay completion of the resize operation.

Another limit is the default replication factor, `dfs.replication`
inside `/etc/hadoop/conf/hdfs-site`. When it creates a
cluster, Amazon EMR configures the value based on the number of instances in the
cluster: `1` with 1-3 instances, `2` for clusters with 4-9
instances, and `3` for clusters with 10+ instances.

###### Warning

1. Setting `dfs.replication` to 1 on clusters with fewer than
   four nodes can lead to HDFS data loss if a single node goes down. We
   recommend you use a cluster with at least four core nodes for production
   workloads.
2. Amazon EMR will not allow clusters to scale core nodes below
   `dfs.replication`. For example, if `dfs.replication
= 2`, the minimum number of core nodes is 2.
3. When you use Managed Scaling, Auto-scaling, or choose to manually resize
   your cluster, we recommend that you to set `dfs.replication` to 2 or
   higher.

Graceful reduction doesn't let you reduce core nodes below the HDFS
replication factor. This is to allow HDFS to close files due insufficient
replicas. To circumvent this limit, lower the replication factor and restart the
NameNode daemon.
