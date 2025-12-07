# Deleting a read replica for

Valkey or Redis OSS (Cluster Mode Disabled)

Information in the following topic applies to Valkey or Redis OSS (cluster mode disabled) replication groups
only.

As read traffic on your Valkey or Redis OSS replication group changes, you might want to add or
remove read replicas. Removing a node from a replication group is the
same as just deleting a cluster, though there are restrictions:

- You cannot remove the primary from a replication group. If you want to delete
  the primary, do the following:
  1.  Promote a read replica to primary.
      For more information on promoting a read replica to primary,
      see [Promoting a read replica to primary, for Valkey or Redis OSS (cluster mode disabled) replication groups](Replication.md "Replication.md").
  2.  Delete the old primary. For a restriction on this method, see the next
      point.

- If Multi-AZ is enabled on a replication group, you can't remove the last
  read replica from the replication group. In this case, do the following:

      1. Modify the replication group by disabling Multi-AZ.
       For more information,
       see [Modifying a replication group](Replication.md "Replication.md").
      2. Delete the read replica.

  You can remove a read replica from a Valkey or Redis OSS (cluster mode disabled) replication group using the ElastiCache console, the AWS CLI for ElastiCache, or the ElastiCache API.

For directions on deleting a cluster from a Valkey or Redis OSS replication group, see the following:

- [Using the AWS Management Console](Clusters.md#Clusters.Delete.CON "Clusters.md#Clusters.Delete.CON")
- [Using the AWS CLI to delete an ElastiCache cluster](Clusters.md#Clusters.Delete.CLI "Clusters.md#Clusters.Delete.CLI")
- [Using the ElastiCache API](Clusters.md#Clusters.Delete.API "Clusters.md#Clusters.Delete.API")
- [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md "scaling-redis-cluster-mode-enabled.md")
- [Decreasing the number of replicas in a shard](decrease-replica-count.md "decrease-replica-count.md")
