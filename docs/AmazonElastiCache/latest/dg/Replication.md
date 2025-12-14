# Creating a Valkey or Redis OSS replication group

You have the following options for creating a cluster with replica nodes. One applies
when you already have an available Valkey or Redis OSS (cluster mode disabled) cluster not associated with any cluster
that has replicas to use as the primary node. The other applies when you need to create a
primary node with the cluster and read replicas. Currently, a Valkey or Redis OSS (cluster mode enabled) cluster must
be created from scratch.

**Option 1: [Creating a replication group using an existing cluster](Replication.CreatingReplGroup.md "Replication.CreatingReplGroup.md")**

Use this option to leverage an existing single-node Valkey or Redis OSS (cluster mode disabled) cluster. You
specify this existing node as the primary node in the new cluster, and then
individually add 1 to 5 read replicas to the cluster. If
the existing cluster is active, read replicas synchronize with it as they are
created. See [Creating a replication group using an existing cluster](Replication.CreatingReplGroup.md "Replication.CreatingReplGroup.md").

###### Important

You cannot create a Valkey or Redis OSS (cluster mode enabled) cluster using an existing cluster.
To create a Valkey or Redis OSS (cluster mode enabled) cluster (API/CLI: replication group) using the ElastiCache console,
see [Creating a Valkey or Redis OSS (cluster mode enabled) cluster (Console)](Clusters.md#Clusters.Create.CON.RedisCluster "Clusters.md#Clusters.Create.CON.RedisCluster").

**Option 2: [Creating a Valkey or Redis OSS replication group from scratch](Replication.CreatingReplGroup.md "Replication.CreatingReplGroup.md")**

Use this option if you don't already have an available Valkey or Redis OSS (cluster mode disabled) cluster to use
as the cluster's primary node, or if you want to create a Valkey or Redis OSS (cluster mode enabled) cluster.
See [Creating a Valkey or Redis OSS replication group from scratch](Replication.CreatingReplGroup.md "Replication.CreatingReplGroup.md").
