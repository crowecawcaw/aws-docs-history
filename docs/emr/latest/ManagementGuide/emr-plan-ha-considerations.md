# Considerations and best practices when you create

an Amazon EMR cluster with multiple primary nodes

Consider the following when you create an Amazon EMR cluster with multiple primary nodes:

###### Important

To launch high-availability EMR clusters with multiple primary nodes, we
strongly recommend that you use the latest Amazon EMR release. This ensures that you get
the highest level of resiliency and stability for your high-availability
clusters.

- High availability for _instance fleets_ is supported
  with Amazon EMR releases 5.36.1, 5.36.2, 6.8.1, 6.9.1, 6.10.1, 6.11.1, 6.12.0, and higher.
  For _instance groups_, high availability is supported with
  Amazon EMR releases 5.23.0 and higher. To learn more, see [About Amazon EMR
  Releases](../ReleaseGuide/emr-release-components.md "../ReleaseGuide/emr-release-components.md").
- On high-availability clusters, Amazon EMR only supports the launch of primary nodes
  with On Demand instances. This ensures the highest availability for your
  cluster.
- You can still specify multiple instance types for primary fleet but all the
  primary nodes of high-availability clusters are launched with the same instance
  type, including replacements for unhealthy primary nodes.
- To continue operations, a high-availability cluster with multiple primary
  nodes requires two out of three primary nodes to be healthy. As a result, if any
  two primary nodes fail simultaneously, your EMR cluster will fail.
- All EMR clusters, including high-availability clusters, are launched in a
  single Availability Zone. Therefore, they can't tolerate Availability Zone failures. In the case
  of an Availability Zone outage, you lose access to the cluster.
- If you use If you’re using a custom service role or policy when you launch a cluster inside an
  instance fleet, you can add the `ec2:DescribeInstanceTypeOfferings` permission so
  Amazon EMR can filter out unsupported Availability Zones (AZ). When Amazon EMR filters out the AZs
  that don’t support any instance types of primary nodes, Amazon EMR prevents cluster
  launches from failing because of unsupported primary instance types. For more information,
  see [Instance type not supported](emr-INSTANCE_TYPE_NOT_SUPPORTED-error.md "emr-INSTANCE_TYPE_NOT_SUPPORTED-error.md").
- Amazon EMR doesn't guarantee high availability for open-source applications other
  than the ones that are specified in [Supported applications in an Amazon EMR
  Cluster with multiple primary nodes](emr-plan-ha-applications.md#emr-plan-ha-applications-list "emr-plan-ha-applications.md#emr-plan-ha-applications-list").
- In Amazon EMR releases 5.23.0 through 5.36.2, only two of the three
  primary nodes for an instance group cluster run HDFS
  NameNode.
- In Amazon EMR releases 6.x and higher, all three of the primary nodes for
  an instance group run HDFS NameNode.
  Considerations for configuring subnet:

- An Amazon EMR cluster with multiple primary nodes can reside only in one Availability Zone or subnet.
  Amazon EMR cannot replace a failed primary node if the subnet is fully utilized
  or oversubscribed in the event of a failover. To avoid this scenario, it is
  recommended that you dedicate an entire subnet to an Amazon EMR cluster. In addition,
  make sure that there are enough private IP addresses available in the
  subnet.
  Considerations for configuring core nodes:

- To ensure the core nodes are also highly available, we recommend that you
  launch at least four core nodes. If you decide to launch a smaller cluster with
  three or fewer core nodes, set `dfs.replication parameter` to at
  least `2` for HDFS to have sufficient DFS replication. For more
  information, see [HDFS
  configuration](../ReleaseGuide/emr-hdfs-config.md "../ReleaseGuide/emr-hdfs-config.md").

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
   Considerations for Setting Alarms on Metrics:

- Amazon EMR doesn't provide application-specific metrics about HDFS or YARN. We
  reccommend that you set up alarms to monitor the primary node instance
  count. Configure the alarms using the following Amazon CloudWatch metrics:
  `MultiMasterInstanceGroupNodesRunning`,
  `MultiMasterInstanceGroupNodesRunningPercentage`, or
  `MultiMasterInstanceGroupNodesRequested`. CloudWatch will notify you in
  the case of primary node failure and replacement.

      + If the `MultiMasterInstanceGroupNodesRunningPercentage` is
       lower than 100% and greater than 50%, the cluster may have lost a
       primary node. In this situation, Amazon EMR attempts to replace a
       primary node.
      + If the `MultiMasterInstanceGroupNodesRunningPercentage`
       drops below 50%, two primary nodes may have failed. In this
       situation, the quorum is lost and the cluster can't be recovered. You
       must manually migrate data off of this cluster.

  For more information, see [Setting alarms on metrics](UsingEMR_ViewingMetrics.md#UsingEMR_ViewingMetrics_Alarm "UsingEMR_ViewingMetrics.md#UsingEMR_ViewingMetrics_Alarm").
