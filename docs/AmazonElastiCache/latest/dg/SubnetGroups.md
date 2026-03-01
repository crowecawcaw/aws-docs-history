# Assigning a subnet group to a cache

After you have created a subnet group, you can launch a cache in an Amazon VPC.
For more information, see the following.

- **Memcached cluster** –
  To launch a Memcached cluster, see [Creating a Memcached cluster (console)](Clusters.md#Clusters.Create.CON.Memcached "Clusters.md#Clusters.Create.CON.Memcached").
  In step 7.a (**Advanced Memcached Settings**), choose a VPC subnet group.
- **Standalone Valkey or Redis OSS cluster** –
  To launch a single-node Valkey or Redis OSS cluster, see [Creating a Valkey (cluster mode disabled) cluster (Console)](SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs "SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs").
  In step 7.a (**Advanced Redis OSS Settings**), choose a VPC subnet group.
- **Valkey or Redis OSS (cluster mode disabled) replication group** –
  To launch a Valkey or Redis OSS (cluster mode disabled) replication group in a VPC, see [Creating a Valkey or Redis OSS (Cluster Mode Disabled) replication group from scratch](Replication.CreatingReplGroup.NoExistingCluster.md "Replication.CreatingReplGroup.NoExistingCluster.md").

In step 7.b (**Advanced Redis OSS Settings**), choose a VPC subnet group.

- **Valkey or Redis OSS (cluster mode enabled) replication group** –
  [Creating a Valkey or Redis OSS (Cluster Mode Enabled) cluster (Console)](Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.CON "Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.CON").
  In step 6.i (**Advanced Redis OSS Settings**), choose a VPC subnet group.
