# Plan and configure primary nodes in your Amazon EMR cluster

When you launch an Amazon EMR cluster, you can choose to have one or three primary nodes
in your cluster. High availability for _instance fleets_ is supported
with Amazon EMR releases 5.36.1, 5.36.2, 6.8.1, 6.9.1, 6.10.1, 6.11.1, 6.12.0, and higher.
For _instance groups_, high availability is supported with
Amazon EMR releases 5.23.0 and higher. To further improve cluster availability, Amazon EMR can use Amazon EC2
placement groups to ensure that primary nodes are placed on distinct underlying
hardware. For more information, see [Amazon EMR integration with EC2 placement
groups](emr-plan-ha-placementgroup.md "emr-plan-ha-placementgroup.md").

An Amazon EMR cluster with multiple primary nodes provides the following benefits:

- The primary node is no longer a single point of failure. If one of the
  primary nodes fails, the cluster uses the other two primary nodes and runs
  without interruption. In the meantime, Amazon EMR automatically replaces the failed
  primary node with a new one that is provisioned with the same configuration and
  bootstrap actions.
- Amazon EMR enables the Hadoop high-availability features of HDFS NameNode and YARN
  ResourceManager and supports high availability for a few other open source
  applications.

For more information about how an Amazon EMR cluster with multiple primary nodes supports open source
applications and other Amazon EMR features, see [Features that support high availability in an Amazon EMR cluster and how they work
with open-source applications](emr-plan-ha-applications.md "emr-plan-ha-applications.md").

###### Note

The cluster can reside only in one Availability Zone or subnet.

This section provides information about supported applications and features of an
Amazon EMR cluster with multiple primary nodes as well as the configuration details, best practices, and considerations
for launching the cluster.

###### Topics

- [Features that support high availability in an Amazon EMR cluster and how they work
  with open-source applications](emr-plan-ha-applications.md "emr-plan-ha-applications.md")
- [Launch an Amazon EMR Cluster with multiple
  primary nodes](emr-plan-ha-launch.md "emr-plan-ha-launch.md")
- [Amazon EMR integration with EC2 placement
  groups](emr-plan-ha-placementgroup.md "emr-plan-ha-placementgroup.md")
- [Considerations and best practices when you create
  an Amazon EMR cluster with multiple primary nodes](emr-plan-ha-considerations.md "emr-plan-ha-considerations.md")
