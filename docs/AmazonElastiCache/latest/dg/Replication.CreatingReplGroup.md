# Creating a replication group using an existing cluster

The following procedure adds a replication group to your Valkey or Redis OSS (cluster mode disabled) single-node cluster, which is necessary in order to upgrade your cluster to the latest version of Valkey. This is an in-place procedure that involves zero downtime and zero data loss. When you create a replication group for your single-node cluster, the cluster's node becomes the primary node in the new cluster.
If you do not have a Valkey or Redis OSS (cluster mode disabled) cluster that you can use as the new cluster's primary,
see [Creating a Valkey or Redis OSS replication group from scratch](Replication.CreatingReplGroup.md "Replication.CreatingReplGroup.md").

An available cluster is an existing single-node Valkey or Redis OSS cluster.
Currently, Valkey or Redis OSS (cluster mode enabled) does not support creating a cluster with replicas
using an available single-node cluster.
If you want to create a Valkey or Redis OSS (cluster mode enabled) cluster, see [Creating a Valkey or Redis OSS (Cluster Mode Enabled) cluster (Console)](Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.CON "Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.CON").

## Creating a replication group using an existing cluster (Console)

See the topic [Using the ElastiCache AWS Management Console](Clusters.md#Clusters.AddNode.CON "Clusters.md#Clusters.AddNode.CON").

## Creating a replication group using an available Valkey or Redis OSS cluster (AWS CLI)

There are two steps to creating a replication group with read replicas
when using an available Valkey or Redis OSS Cache Cluster for the primary when using the AWS CLI.

When using the AWS CLI you create a replication group specifying the available standalone node as the cluster's primary node,
`--primary-cluster-id` and the number of nodes you want in the cluster using the CLI command,
`create-replication-group`.
Include the following parameters.

**--replication-group-id**
The name of the replication group you are creating.
The value of this parameter is used as the basis for the names of the added nodes with a
sequential 3-digit number added to the end of the `--replication-group-id`.
For example, `sample-repl-group-001`.

Valkey or Redis OSS (cluster mode disabled) replication group naming constraints are as follows:

- Must contain 1–40 alphanumeric characters or hyphens.
- Must begin with a letter.
- Can't contain two consecutive hyphens.
- Can't end with a hyphen.

**--replication-group-description**
Description of the replication group.

**--num-node-groups**
The number of nodes you want in this cluster. This value includes the primary node. This
parameter has a maximum value of six.

**--primary-cluster-id**
The name of the available Valkey or Redis OSS (cluster mode disabled) cluster's node that you want to be the primary node
in this replication group.

The following command creates the replication group `sample-repl-group` using the available Valkey or Redis OSS (cluster mode disabled)
cluster `redis01` as the replication group's primary node.
It creates 2 new nodes which are read replicas.
The settings of `redis01` (that is, parameter group, security group, node type, engine version, and so on.) will
be applied to all nodes in the replication group.

For Linux, macOS, or Unix:

```
aws elasticache create-replication-group \
   --replication-group-id `sample-repl-group` \
   --replication-group-description `"demo cluster with replicas"` \
   --num-cache-clusters `3` \
   --primary-cluster-id `redis01`
```

For Windows:

```
aws elasticache create-replication-group ^
   --replication-group-id `sample-repl-group` ^
   --replication-group-description `"demo cluster with replicas"` ^
   --num-cache-clusters `3` ^
   --primary-cluster-id `redis01`
```

For additional information and parameters you might want to use,
see the AWS CLI topic create-replication-group.

###### Next, add read replicas to the replication group

After the replication group is created, add one to five read replicas to it using the
`create-cache-cluster` command, being sure to include the following parameters.

**--cache-cluster-id**
The name of the cluster you are adding to the replication group.

Cluster naming constraints are as follows:

- Must contain 1–40 alphanumeric characters or hyphens.
- Must begin with a letter.
- Can't contain two consecutive hyphens.
- Can't end with a hyphen.

**--replication-group-id**
The name of the replication group to which you are adding this cluster.

Repeat this command for each read replica you want to add to the replication group,
changing only the value of the `--cache-cluster-id` parameter.

###### Note

Remember, a replication group cannot have more than five read replicas.
Attempting to add a read replica to a replication group that already has five read replicas
causes the operation to fail.

The following code adds the read replica `my-replica01` to the replication group
`sample-repl-group`.
The settings of the primary cluster–parameter group, security group, node type, and so on.–will
be applied to nodes as they are added to the replication group.

For Linux, macOS, or Unix:

```
aws elasticache create-cache-cluster \
   --cache-cluster-id `my-replica01` \
   --replication-group-id `sample-repl-group`
```

For Windows:

```
aws elasticache create-cache-cluster ^
   --cache-cluster-id `my-replica01` ^
   --replication-group-id `sample-repl-group`
```

Output from this command will look something like this.

```
{
    "ReplicationGroup": {
        "Status": "creating",
        "Description": "demo cluster with replicas",
        "ClusterEnabled": false,
        "ReplicationGroupId": "sample-repl-group",
        "SnapshotRetentionLimit": 1,
        "AutomaticFailover": "disabled",
        "SnapshotWindow": "00:00-01:00",
        "SnapshottingClusterId": "redis01",
        "MemberClusters": [
            "sample-repl-group-001",
            "sample-repl-group-002",
            "redis01"
        ],
        "CacheNodeType": "cache.m4.large",
        "DataTiering": "disabled",
        "PendingModifiedValues": {}
    }
}
```

For additional information, see the AWS CLI topics:

- [create-replication-group](../../../cli/latest/reference/elasticache/create-replication-group.md "../../../cli/latest/reference/elasticache/create-replication-group.md")
- [modify-replication-group](../../../cli/latest/reference/elasticache/modify-replication-group.md "../../../cli/latest/reference/elasticache/modify-replication-group.md")

## Adding replicas to a standalone Valkey or Redis OSS (Cluster Mode Disabled) cluster (ElastiCache API)

When using the ElastiCache API, you create a replication group specifying the available
standalone node as the cluster's primary node, `PrimaryClusterId` and the
number of nodes you want in the cluster using the CLI command,
`CreateReplicationGroup`. Include the following parameters.

**ReplicationGroupId**
The name of the replication group you are creating.
The value of this parameter is used as the basis for the names of the added nodes with a
sequential 3-digit number added to the end of the `ReplicationGroupId`.
For example, `sample-repl-group-001`.

Valkey or Redis OSS (cluster mode disabled) replication group naming constraints are as follows:

- Must contain 1–40 alphanumeric characters or hyphens.
- Must begin with a letter.
- Can't contain two consecutive hyphens.
- Can't end with a hyphen.

**ReplicationGroupDescription**
Description of the cluster with replicas.

**NumCacheClusters**
The number of nodes you want in this cluster. This value includes the primary node.
This parameter has a maximum value of six.

**PrimaryClusterId**
The name of the available Valkey or Redis OSS (cluster mode disabled) cluster that you want to be the primary node
in this cluster.

The following command creates the cluster with replicas `sample-repl-group` using the available Valkey or Redis OSS (cluster mode disabled)
cluster `redis01` as the replication group's primary node.
It creates 2 new nodes which are read replicas.
The settings of `redis01` (that is, parameter group, security group, node type, engine version, and so on.) will
be applied to all nodes in the replication group.

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=CreateReplicationGroup
   &Engine=redis
   &EngineVersion=6.0
   &ReplicationGroupDescription=Demo%20cluster%20with%20replicas
   &ReplicationGroupId=sample-repl-group
   &PrimaryClusterId=redis01
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

For additional information, see the ElastiCache APL topics:

- [CreateReplicationGroup](../APIReference/API_CreateReplicationGroup.md "../APIReference/API_CreateReplicationGroup.md")
- [ModifyReplicationGroup](../APIReference/API_ModifyReplicationGroup.md "../APIReference/API_ModifyReplicationGroup.md")

###### Next, add read replicas to the replication group

After the replication group is created, add one to five read replicas to it using the
`CreateCacheCluster` operation, being sure to include the following parameters.

**CacheClusterId**
The name of the cluster you are adding to the replication group.

Cluster naming constraints are as follows:

- Must contain 1–40 alphanumeric characters or hyphens.
- Must begin with a letter.
- Can't contain two consecutive hyphens.
- Can't end with a hyphen.

**ReplicationGroupId**
The name of the replication group to which you are adding this cluster.

Repeat this operation for each read replica you want to add to the replication group,
changing only the value of the `CacheClusterId` parameter.

The following code adds the read replica `myReplica01` to the replication group
`myReplGroup`
The settings of the primary cluster–parameter group, security group, node type, and so on.–will
be applied to nodes as they are added to the replication group.

```
https://elasticache.us-west-2.amazonaws.com/
	?Action=CreateCacheCluster
	&CacheClusterId=myReplica01
	&ReplicationGroupId=myReplGroup
	&SignatureMethod=HmacSHA256
	&SignatureVersion=4
	&Version=2015-02-02
	&X-Amz-Algorithm=&AWS;4-HMAC-SHA256
	&X-Amz-Credential=[your-access-key-id]/20150202/us-west-2/elasticache/aws4_request
	&X-Amz-Date=20150202T170651Z
	&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
	&X-Amz-Signature=[signature-value]
```

For additional information and parameters you might want to use,
see the ElastiCache API topic CreateCacheCluster.
