

# Adding nodes to an ElastiCache cluster
<a name="Clusters.AddNode"></a>

Adding nodes to a Memcached cluster increases the number of your cluster's partitions. When you change the number of partitions in a cluster some of your key spaces need to be remapped so that they are mapped to the right node. Remapping key spaces temporarily increases the number of cache misses on the cluster. For more information, see [Configuring your ElastiCache client for efficient load balancing (Memcached)](BestPractices.LoadBalancing.md).

To reconfigure your Valkey or Redis OSS (cluster mode enabled) cluster, see [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md)

You can use the ElastiCache Management Console, the AWS CLI or ElastiCache API to add nodes to your cluster.

## Using the ElastiCache AWS Management Console
<a name="Clusters.AddNode.CON"></a>

If you want to add a node to a single-node Valkey or Redis OSS (cluster mode disabled) cluster (one without replication enabled), it's a two-step process: first add replication, and then add a replica node.

**Topics**
+ [To add replication to a Valkey or Redis OSS cluster with no shards](#AddReplication.CON)
+ [To add nodes to an ElastiCache cluster (console)](#AddNode.CON)

The following procedure adds replication to a single-node Valkey or Redis OSS that does not have replication enabled. When you add replication, the existing node becomes the primary node in the replication-enabled cluster. After replication is added, you can add up to 5 replica nodes to the cluster.<a name="AddReplication.CON"></a>

**To add replication to a Valkey or Redis OSS cluster with no shards**

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. From the navigation pane, choose **Valkey clusters** or **Redis OSS clusters**.

   A list of clusters running that engine is displayed.

1. Choose the name of a cluster, not the box to the left of the cluster's name, that you want to add nodes to.

   The following is true of a Redis OSS cluster that does not have replication enabled:
   + It is running Redis OSS, not Clustered Redis OSS.
   + It has zero shards.

     If the cluster has any shards, replication is already enabled on it and you can continue at [To add nodes to an ElastiCache cluster (console)](#AddNode.CON).

1. Choose **Add replication**.

1. In **Add Replication**, enter a description for this replication-enabled cluster.

1. Choose **Add**.

   As soon as the cluster's status returns to *available* you can continue at the next procedure and add replicas to the cluster.<a name="AddNode.CON"></a>

**To add nodes to an ElastiCache cluster (console)**

The following procedure can be used to add nodes to a cluster.

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. In the navigation pane, choose the engine running on the cluster that you want to add nodes to.

   A list of clusters running the chosen engine appears.

1. From the list of clusters, for the cluster that you want to add a node to, choose its name.

   If your cluster is a Valkey or Redis OSS (cluster mode enabled) cluster, see [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md).

   If your cluster is a Valkey or Redis OSS (cluster mode disabled) cluster with zero shards, first complete the steps at [To add replication to a Valkey or Redis OSS cluster with no shards](#AddReplication.CON).

1. Choose **Add node**.

1. Complete the information requested in the **Add Node** dialog box.

1. Choose the **Apply Immediately - Yes** button to add this node immediately, or choose **No** to add this node during the cluster's next maintenance window.  
**Impact of New Add and Remove Requests on Pending Requests**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.AddNode.html)

   To determine what operations are pending, choose the **Description** tab and check to see how many pending creations or deletions are shown. You cannot have both pending creations and pending deletions. 

1. Choose the **Add** button.

    After a few moments, the new nodes should appear in the nodes list with a status of **creating**. If they don't appear, refresh your browser page. When the node's status changes to *available* the new node is able to be used.

## Using the AWS CLI with ElastiCache
<a name="Clusters.AddNode.CLI"></a>

To add nodes to a cluster using the AWS CLI, use the AWS CLI operation `modify-cache-cluster` with the following parameters:
+ `--cache-cluster-id` The ID of the cluster that you want to add nodes to.
+ `--num-cache-nodes` The `--num-cache-nodes` parameter specifies the number of nodes that you want in this cluster after the modification is applied. To add nodes to this cluster, `--num-cache-nodes` must be greater than the current number of nodes in this cluster. If this value is less than the current number of nodes, ElastiCache expects the parameter `cache-node-ids-to-remove` and a list of nodes to remove from the cluster. For more information, see [Using the AWS CLI with ElastiCache](Clusters.DeleteNode.md#Clusters.DeleteNode.CLI).
+ `--apply-immediately` or `--no-apply-immediately` which specifies whether to add these nodes immediately or at the next maintenance window.

For Linux, macOS, or Unix:

```
aws elasticache modify-cache-cluster \
    --cache-cluster-id {{my-cluster}} \
    --num-cache-nodes {{5}} \
    --apply-immediately
```

For Windows:

```
aws elasticache modify-cache-cluster ^
    --cache-cluster-id {{my-cluster}} ^
    --num-cache-nodes {{5}} ^
    --apply-immediately
```

This operation produces output similar to the following (JSON format):

```
{
    "CacheCluster": {
        "Engine": "memcached", 
        "CacheParameterGroup": {
            "CacheNodeIdsToReboot": [], 
            "CacheParameterGroupName": "default.memcached1.4", 
            "ParameterApplyStatus": "in-sync"
        }, 
        "CacheClusterId": "my-cluster", 
        "PreferredAvailabilityZone": "us-west-2b", 
        "ConfigurationEndpoint": {
            "Port": 11211, 
            "Address": "rlh-mem000.7alc7bf-example.cfg.usw2.cache.amazonaws.com"
        }, 
        "CacheSecurityGroups": [], 
        "CacheClusterCreateTime": "2016-09-21T16:28:28.973Z", 
        "AutoMinorVersionUpgrade": true, 
        "CacheClusterStatus": "modifying", 
        "NumCacheNodes": 2, 
        "ClientDownloadLandingPage": "https://console.aws.amazon.com/elasticache/home#client-download:", 
        "SecurityGroups": [
            {
                "Status": "active", 
                "SecurityGroupId": "sg-dbe93fa2"
            }
        ], 
        "CacheSubnetGroupName": "default", 
        "EngineVersion": "1.4.24", 
        "PendingModifiedValues": {
            "NumCacheNodes": 5
        }, 
        "PreferredMaintenanceWindow": "sat:09:00-sat:10:00", 
        "CacheNodeType": "cache.m5.large",
         "DataTiering": "disabled",
    }
}
```

For more information, see the AWS CLI topic [`modify-cache-cluster`](https://docs.aws.amazon.com/cli/latest/reference/elasticache/modify-cache-cluster.html).

## Using the AWS CLI with ElastiCache
<a name="Clusters.AddNode.CLI"></a>

If you want to add nodes to an existing Valkey or Redis OSS (cluster mode disabled) cluster that does not have replication enabled, you must first create the replication group specifying the existing cluster as the primary. For more information, see [Creating a replication group using an available Valkey or Redis OSS cluster (AWS CLI)](Replication.CreatingReplGroup.ExistingCluster.md#Replication.CreatingReplGroup.ExistingCluster.CLI). After the replication group is *available*, you can continue with the following process.

To add nodes to a cluster using the AWS CLI, use the AWS CLI operation `increase-replica-count` with the following parameters:
+ `--replication-group-id` The ID of the replicationn group that you want to add nodes to.
+ `--new-replica-count` specifies the number of nodes that you want in this replication group after the modification is applied. To add nodes to this cluster, `--new-replica-count` must be greater than the current number of nodes in this cluster.
+ `--apply-immediately` or `--no-apply-immediately` which specifies whether to add these nodes immediately or at the next maintenance window.

For Linux, macOS, or Unix:

```
aws elasticache increase-replica-count \
    --replication-group-id {{my-replication-group}} \
    --new-replica-count {{4}} \
    --apply-immediately
```

For Windows:

```
aws elasticache increase-replica-count ^
    --replication-group-id {{my-replication-group}} ^
    --new-replica-count {{4}} ^
    --apply-immediately
```

This operation produces output similar to the following (JSON format):

```
{
    "ReplicationGroup": {
        "ReplicationGroupId": "node-test",
        "Description": "node-test",       
        "Status": "modifying",
        "PendingModifiedValues": {},
        "MemberClusters": [
            "node-test-001",
            "node-test-002",
            "node-test-003",
            "node-test-004",
            "node-test-005"
        ],
        "NodeGroups": [
            {
                "NodeGroupId": "0001",
                "Status": "modifying",
                "PrimaryEndpoint": {
                    "Address": "node-test.zzzzzz.ng.0001.usw2.cache.amazonaws.com",
                    "Port": 6379
                },
                "ReaderEndpoint": {
                    "Address": "node-test.zzzzzz.ng.0001.usw2.cache.amazonaws.com",
                    "Port": 6379
                },
                "NodeGroupMembers": [
                    {
                        "CacheClusterId": "node-test-001",
                        "CacheNodeId": "0001",
                        "ReadEndpoint": {
                            "Address": "node-test-001.zzzzzz.0001.usw2.cache.amazonaws.com",
                            "Port": 6379
                        },
                        "PreferredAvailabilityZone": "us-west-2a",
                        "CurrentRole": "primary"
                    },
                    {
                        "CacheClusterId": "node-test-002",
                        "CacheNodeId": "0001",
                        "ReadEndpoint": {
                            "Address": "node-test-002.zzzzzz.0001.usw2.cache.amazonaws.com",
                            "Port": 6379
                        },
                        "PreferredAvailabilityZone": "us-west-2c",
                        "CurrentRole": "replica"
                    },
                    {
                        "CacheClusterId": "node-test-003",
                        "CacheNodeId": "0001",
                        "ReadEndpoint": {
                            "Address": "node-test-003.zzzzzz.0001.usw2.cache.amazonaws.com",
                            "Port": 6379
                        },
                        "PreferredAvailabilityZone": "us-west-2b",
                        "CurrentRole": "replica"
                    }
                ]
            }
        ],
        "SnapshottingClusterId": "node-test-002",
        "AutomaticFailover": "enabled",
        "MultiAZ": "enabled",
        "SnapshotRetentionLimit": 1,
        "SnapshotWindow": "07:30-08:30",
        "ClusterEnabled": false,
        "CacheNodeType": "cache.r5.large",
         "DataTiering": "disabled",
        "TransitEncryptionEnabled": false,
        "AtRestEncryptionEnabled": false,
        "ARN": "arn:aws:elasticache:us-west-2:123456789012:replicationgroup:node-test"
    }
}
```

For more information, see the AWS CLI topic [`increase-replica-count`](https://docs.aws.amazon.com/cli/latest/reference/elasticache/increase-replica-count.html).

## Using the ElastiCache API
<a name="Clusters.AddNode.API"></a>

If you want to add nodes to an existing Valkey or Redis OSS (cluster mode disabled) cluster that does not have replication enabled, you must first create the replication group specifying the existing cluster as the Primary. For more information, see [Adding replicas to a standalone Valkey or Redis OSS (Cluster Mode Disabled) cluster (ElastiCache API)](Replication.CreatingReplGroup.ExistingCluster.md#Replication.CreatingReplGroup.ExistingCluster.API). After the replication group is *available*, you can continue with the following process.

**To add nodes to a cluster (ElastiCache API)**
+ Call the `IncreaseReplicaCount` API operation with the following parameters:
  + `ReplicationGroupId` The ID of the cluster that you want to add nodes to.
  + `NewReplicaCount` The `NewReplicaCount` parameter specifies the number of nodes that you want in this cluster after the modification is applied. To add nodes to this cluster, `NewReplicaCount` must be greater than the current number of nodes in this cluster. If this value is less than the current number of nodes, use the `DecreaseReplicaCount` API with the number of nodes to remove from the cluster.
  + `ApplyImmediately` Specifies whether to add these nodes immediately or at the next maintenance window.
  + `Region` Specifies the AWS Region of the cluster that you want to add nodes to.

  The following example shows a call to add nodes to a cluster.  
**Example**  

  ```
  https://elasticache.us-west-2.amazonaws.com/
      ?Action=IncreaseReplicaCount
      &ApplyImmediately=true
      &NumCacheNodes=4
      &ReplicationGroupId=my-replication-group
      &Region=us-east-2
      &Version=2014-12-01
      &SignatureVersion=4
      &SignatureMethod=HmacSHA256
      &Timestamp=20141201T220302Z
      &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
      &X-Amz-Date=20141201T220302Z
      &X-Amz-SignedHeaders=Host
      &X-Amz-Expires=20141201T220302Z
      &X-Amz-Credential=<credential>
      &X-Amz-Signature=<signature>
  ```

For more information, see ElastiCache API topic [`IncreaseReplicaCount`](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_IncreaseReplicaCount.html).

## Using the ElastiCache API
<a name="Clusters.AddNode.API"></a>

**To add nodes to a cluster (ElastiCache API)**
+ Call the `ModifyCacheCluster` API operation with the following parameters:
  + `CacheClusterId` The ID of the cluster that you want to add nodes to.
  + `NumCacheNodes` The `NumCachNodes` parameter specifies the number of nodes that you want in this cluster after the modification is applied. To add nodes to this cluster, `NumCacheNodes` must be greater than the current number of nodes in this cluster. If this value is less than the current number of nodes, ElastiCache expects the parameter `CacheNodeIdsToRemove` with a list of nodes to remove from the cluster (see [Using the ElastiCache API with Memcached](Clusters.DeleteNode.md#Clusters.DeleteNode.API)).
  + `ApplyImmediately` Specifies whether to add these nodes immediately or at the next maintenance window.
  + `Region` Specifies the AWS Region of the cluster that you want to add nodes to.

  The following example shows a call to add nodes to a cluster.  
**Example**  

  ```
  https://elasticache.us-west-2.amazonaws.com/
      ?Action=ModifyCacheCluster
      &ApplyImmediately=true
      &NumCacheNodes=5
  	&CacheClusterId=my-cluster
  	&Region=us-east-2
      &Version=2014-12-01
      &SignatureVersion=4
      &SignatureMethod=HmacSHA256
      &Timestamp=20141201T220302Z
      &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
      &X-Amz-Date=20141201T220302Z
      &X-Amz-SignedHeaders=Host
      &X-Amz-Expires=20141201T220302Z
      &X-Amz-Credential=<credential>
      &X-Amz-Signature=<signature>
  ```

For more information, see ElastiCache API topic [`ModifyCacheCluster`](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html).