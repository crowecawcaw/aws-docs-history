

# Scaling for Valkey or Redis OSS (Cluster Mode Disabled) clusters
<a name="scaling-redis-classic"></a>

Valkey or Redis OSS (cluster mode disabled) clusters can be a single-node cluster with 0 shards or multi-node clusters with 1 shard. Single-node clusters use the one node for both reads and writes. Multi-node clusters always have 1 node as the read/write primary node with 0 to 5 read-only replica nodes.

**Topics**
+ [Scaling for Valkey or Redis OSS (Cluster Mode Disabled) clusters](#Scaling.RedisStandalone)


**Scaling Valkey or Redis OSS clusters**  

| Action | Valkey or Redis OSS (cluster mode disabled) | Valkey or Redis OSS (cluster mode enabled) | 
| --- | --- | --- | 
| Scaling in | [Removing nodes from an ElastiCache cluster](Clusters.DeleteNode.md) | [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md) | 
| Scaling out | [Adding nodes to a cluster](Clusters.html#AddNode) | [Online resharding for Valkey or Redis OSS (cluster mode enabled)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online) | 
| Changing node types |  +  [Scaling up single-node Valkey or Redis OSS clusters](#Scaling.RedisStandalone.ScaleUp)<br />+  [Scaling up Valkey or Redis OSS clusters with replicas](Scaling.RedisReplGrps.md#Scaling.RedisReplGrps.ScaleUp) +  [Scaling down single-node Valkey or Redis OSS clusters](#Scaling.RedisStandalone.ScaleDown)<br />+  [Scaling down Valkey or Redis OSS clusters with replicas](Scaling.RedisReplGrps.md#Scaling.RedisReplGrps.ScaleDown)  | [Online vertical scaling by modifying node type](redis-cluster-vertical-scaling.md) | 
| Changing the number of node groups | Not supported for Valkey or Redis OSS (cluster mode disabled) clusters | [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md) | 

**Contents**
+ [Scaling for Valkey or Redis OSS (Cluster Mode Disabled) clusters](#Scaling.RedisStandalone)
  + [Scaling up single-node Valkey or Redis OSS clusters](#Scaling.RedisStandalone.ScaleUp)
    + [Scaling up single-node Valkey or Redis OSS (Cluster Mode Disabled) (Console) clusters](#Scaling.RedisStandalone.ScaleUp.CON)
    + [Scaling up single-node Valkey or Redis OSS clusters (AWS CLI)](#Scaling.RedisStandalone.ScaleUp.CLI)
    + [Scaling up single-node Valkey or Redis OSS clusters (ElastiCache API)](#Scaling.RedisStandalone.ScaleUp.API)
  + [Scaling down single-node Valkey or Redis OSS clusters](#Scaling.RedisStandalone.ScaleDown)
    + [Scaling down a single-node Valkey or Redis OSS cluster (Console)](#Scaling.RedisStandalone.ScaleDown.CON)
    + [Scaling down single-node Valkey or Redis OSS clusters (AWS CLI)](#Scaling.RedisStandalone.ScaleUpDown-Modify.CLI)
    + [Scaling down single-node Valkey or Redis OSS clusters (ElastiCache API)](#Scaling.RedisStandalone.ScaleDown.API)

## Scaling for Valkey or Redis OSS (Cluster Mode Disabled) clusters
<a name="Scaling.RedisStandalone"></a>

Valkey or Redis OSS (cluster mode disabled) nodes must be large enough to contain all the cache's data plus the Valkey or Redis OSS overhead. To change the data capacity of your Valkey or Redis OSS (cluster mode disabled) cluster, you must scale vertically; scaling up to a larger node type to increase data capacity, or scaling down to a smaller node type to reduce data capacity.

The ElastiCache scaling up process is designed to make a best effort to retain your existing data and requires successful Valkey or Redis OSS replication. For Valkey or Redis OSS (cluster mode disabled) clusters, we recommend that sufficient memory be made available to Valkey or Redis OSS. 

You cannot partition your data across multiple Valkey or Redis OSS (cluster mode disabled) clusters. However, if you only need to increase or decrease your cluster's read capacity, you can create a Valkey or Redis OSS (cluster mode disabled) cluster with replica nodes and add or remove read replicas. To create a Valkey or Redis OSS (cluster mode disabled) cluster with replica nodes using your single-node Valkey or Redis OSS cluster as the primary cluster, see [Creating a Valkey (cluster mode disabled) cluster (Console)](SubnetGroups.designing-cluster-pre.valkey.md#Clusters.Create.CON.valkey-gs).

After you create the cluster with replicas, you can increase read capacity by adding read replicas. Later, if you need to, you can reduce read capacity by removing read replicas. For more information, see [Increasing read capacity](Scaling.RedisReplGrps.md#Scaling.RedisReplGrps.ScaleOut) or [Decreasing read capacity](Scaling.RedisReplGrps.md#Scaling.RedisReplGrps.ScaleIn).

In addition to being able to scale read capacity, Valkey or Redis OSS (cluster mode disabled) clusters with replicas provide other business advantages. For more information, see [High availability using replication groups](Replication.md).

**Important**  
If your parameter group uses `reserved-memory` to set aside memory for Valkey or Redis OSS overhead, before you begin scaling be sure that you have a custom parameter group that reserves the correct amount of memory for your new node type. Alternatively, you can modify a custom parameter group so that it uses `reserved-memory-percent` and use that parameter group for your new cluster.  
If you're using `reserved-memory-percent`, doing this is not necessary.   
For more information, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md).

**Topics**
+ [Scaling up single-node Valkey or Redis OSS clusters](#Scaling.RedisStandalone.ScaleUp)
+ [Scaling down single-node Valkey or Redis OSS clusters](#Scaling.RedisStandalone.ScaleDown)

### Scaling up single-node Valkey or Redis OSS clusters
<a name="Scaling.RedisStandalone.ScaleUp"></a>

When you scale up a single-node Valkey or Redis OSS cluster, ElastiCache performs the following process, whether you use the ElastiCache console, the AWS CLI, or the ElastiCache API.

1. A new cluster with the new node type is spun up in the same Availability Zone as the existing cluster.

1. The cache data in the existing cluster is copied to the new cluster. How long this process takes depends upon your node type and how much data is in the cluster.

1. Reads and writes are now served using the new cluster. Because the new cluster's endpoints are the same as they were for the old cluster, you do not need to update the endpoints in your application. You will notice a brief interruption (a few seconds) of reads and writes from the primary node while the DNS entry is updated.

1. ElastiCache deletes the old cluster. You will notice a brief interruption (a few seconds) of reads and writes from the old node because the connections to the old node will be disconnected. 

**Note**  
For clusters running the r6gd node type, you can only scale to node sizes within the r6gd node family.

As shown in the following table, your Valkey or Redis OSS scale-up operation is blocked if you have an engine upgrade scheduled for the next maintenance window. For more information on Maintenance Windows, see [Managing ElastiCache cluster maintenance](maintenance-window.md).


**Blocked Valkey or Redis OSS operations**  


- **Scale up**
  - Immediate engine upgrade

- **Engine upgrade**
  - Immediate scale up

- **Scale up and engine upgrade**
  - Immediate scale up
  - Immediate engine upgrade



If you have a pending operation that is blocking you, you can do one of the following.
+ Schedule your Valkey or Redis OSS scale-up operation for the next maintenance window by clearing the **Apply immediately** check box (CLI use: `--no-apply-immediately`, API use: `ApplyImmediately=false`).
+ Wait until your next maintenance window (or after) to perform your Valkey or Redis OSS scale up operation.
+ Add the Valkey or Redis OSS engine upgrade to this cluster modification with the **Apply Immediately** check box chosen (CLI use: `--apply-immediately`, API use: `ApplyImmediately=true`). This unblocks your scale up operation by causing the engine upgrade to be performed immediately.

You can scale up a single-node Valkey or Redis OSS (cluster mode disabled) cluster using the ElastiCache console, the AWS CLI, or ElastiCache API.

**Important**  
If your parameter group uses `reserved-memory` to set aside memory for Valkey or Redis OSS overhead, before you begin scaling be sure that you have a custom parameter group that reserves the correct amount of memory for your new node type. Alternatively, you can modify a custom parameter group so that it uses `reserved-memory-percent` and use that parameter group for your new cluster.  
If you're using `reserved-memory-percent`, doing this is not necessary.   
For more information, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md).

#### Scaling up single-node Valkey or Redis OSS (Cluster Mode Disabled) (Console) clusters
<a name="Scaling.RedisStandalone.ScaleUp.CON"></a>

The following procedure describes how to scale up a single-node Valkey or Redis OSS cluster using the ElastiCache Management Console. During this process, your Valkey or Redis OSS cluster will continue to serve requests with minimal downtime.

**To scale up a single-node Valkey or Redis OSS cluster (console)**

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. From the navigation pane, choose **Valkey or Redis OSS clusters**.

1. From the list of clusters, choose the cluster you want to scale up (it must be running the Valkey or Redis OSS engine, not the clustered Valkey or Redis OSS engine). 

1. Choose **Modify**.

1. In the **Modify Cluster** wizard:

   1. Choose the node type you want to scale to from the **Node type** list.

   1. If you're using `reserved-memory` to manage your memory, from the **Parameter Group** list, choose the custom parameter group that reserves the correct amount of memory for your new node type.

1. If you want to perform the scale up process right away, choose the **Apply immediately** box. If the **Apply immediately** box is not chosen, the scale-up process is performed during this cluster's next maintenance window.

1. Choose **Modify**.

   If you chose **Apply immediately** in the previous step, the cluster's status changes to *modifying*. When the status changes to *available*, the modification is complete and you can begin using the new cluster.

#### Scaling up single-node Valkey or Redis OSS clusters (AWS CLI)
<a name="Scaling.RedisStandalone.ScaleUp.CLI"></a>

The following procedure describes how to scale up a single-node Valkey or Redis OSS cluster using the AWS CLI. During this process, your Valkey or Redis OSS cluster will continue to serve requests with minimal downtime.

**To scale up a single-node Valkey or Redis OSS cluster (AWS CLI)**

1. Determine the node types you can scale up to by running the AWS CLI `list-allowed-node-type-modifications` command with the following parameter.
   + `--cache-cluster-id`

   For Linux, macOS, or Unix:

   ```
   aws elasticache list-allowed-node-type-modifications \
   	    --cache-cluster-id {{my-cache-cluster-id}}
   ```

   For Windows:

   ```
   aws elasticache list-allowed-node-type-modifications ^
   	    --cache-cluster-id {{my-cache-cluster-id}}
   ```

   Output from the above command looks something like this (JSON format).

   ```
   {
   	    "ScaleUpModifications": [
   	        "cache.m5.2xlarge", 
   	        "cache.m5.large", 
   	        "cache.m5.xlarge", 
   	        "cache.m4.10xlarge", 
   	        "cache.m4.2xlarge", 
   	        "cache.m4.4xlarge", 
   	        "cache.m4.large", 
   	        "cache.m4.xlarge", 
   	        "cache.r5.2xlarge", 
   	        "cache.r5.4xlarge", 
   	        "cache.r5.12xlarge", 
   	        "cache.r5.large", 
   	        "cache.r5.xlarge"
   	    ]
   	       "ScaleDownModifications": [
   	        "cache.t2.micro", 
   	        "cache.t2.small ", 
   	        "cache.t2.medium "
   	    ], 
   
   	}
   ```

   For more information, see [list-allowed-node-type-modifications](https://docs.aws.amazon.com/cli/latest/reference/elasticache/list-allowed-node-type-modifications.html) in the *AWS CLI Reference*.

1. Modify your existing cluster specifying the cluster to scale up and the new, larger node type, using the AWS CLI `modify-cache-cluster` command and the following parameters.
   + `--cache-cluster-id` – The name of the cluster you are scaling up. 
   + `--cache-node-type` – The new node type you want to scale the cluster. This value must be one of the node types returned by the `list-allowed-node-type-modifications` command in step 1.
   + `--cache-parameter-group-name` – [Optional] Use this parameter if you are using `reserved-memory` to manage your cluster's reserved memory. Specify a custom cache parameter group that reserves the correct amount of memory for your new node type. If you are using `reserved-memory-percent` you can omit this parameter.
   + `--apply-immediately` – Causes the scale-up process to be applied immediately. To postpone the scale-up process to the cluster's next maintenance window, use the `--no-apply-immediately` parameter.

   For Linux, macOS, or Unix:

   ```
   aws elasticache modify-cache-cluster \
   	    --cache-cluster-id {{my-redis-cache-cluster}} \
   	    --cache-node-type {{cache.m5.xlarge}} \
   	    --cache-parameter-group-name {{redis7-cluster}} \
   	    --apply-immediately
   ```

   For Windows:

   ```
   aws elasticache modify-cache-cluster ^
   	    --cache-cluster-id {{my-redis-cache-cluster}} ^
   	    --cache-node-type {{cache.m5.xlarge}} ^
   	    --cache-parameter-group-name {{redis7-cluster}} ^
   	    --apply-immediately
   ```

   Output from the above command looks something like this (JSON format).

   ```
   {
   	    "CacheCluster": {
   	        "Engine": "redis", 
   	        "CacheParameterGroup": {
   	            "CacheNodeIdsToReboot": [], 
   	            "CacheParameterGroupName": "default.redis6.x", 
   	            "ParameterApplyStatus": "in-sync"
   	        }, 
   	        "SnapshotRetentionLimit": 1, 
   	        "CacheClusterId": "my-redis-cache-cluster", 
   	        "CacheSecurityGroups": [], 
   	        "NumCacheNodes": 1, 
   	        "SnapshotWindow": "00:00-01:00", 
   	        "CacheClusterCreateTime": "2017-02-21T22:34:09.645Z", 
   	        "AutoMinorVersionUpgrade": true, 
   	        "CacheClusterStatus": "modifying", 
   	        "PreferredAvailabilityZone": "us-west-2a", 
   	        "ClientDownloadLandingPage": "https://console.aws.amazon.com/elasticache/home#client-download:", 
   	        "CacheSubnetGroupName": "default", 
   	        "EngineVersion": "6.0", 
   	        "PendingModifiedValues": {
   	            "CacheNodeType": "cache.m5.2xlarge"
   	        }, 
   	        "PreferredMaintenanceWindow": "tue:11:30-tue:12:30", 
   	        "CacheNodeType": "cache.m5.large",
   	         "DataTiering": "disabled"
   	    }
   	}
   ```

   For more information, see [modify-cache-cluster](https://docs.aws.amazon.com/cli/latest/reference/elasticache/modify-cache-cluster.html) in the *AWS CLI Reference*.

1. If you used the `--apply-immediately`, check the status of the new cluster using the AWS CLI `describe-cache-clusters` command with the following parameter. When the status changes to *available*, you can begin using the new, larger cluster.
   + `--cache-cluster-id` – The name of your single-node Valkey or Redis OSS cluster. Use this parameter to describe a particular cluster rather than all clusters.

   ```
   aws elasticache describe-cache-clusters --cache-cluster-id {{my-redis-cache-cluster}}
   ```

   For more information, see [describe-cache-clusters](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-clusters.html) in the *AWS CLI Reference*.

#### Scaling up single-node Valkey or Redis OSS clusters (ElastiCache API)
<a name="Scaling.RedisStandalone.ScaleUp.API"></a>

The following procedure describes how to scale up a single-node Valkey or Redis OSS cluster using the ElastiCache API. During this process, your Valkey or Redis OSS cluster will continue to serve requests with minimal downtime.

**To scale up a single-node Valkey or Redis OSS cluster (ElastiCache API)**

1. Determine the node types you can scale up to by running the ElastiCache API `ListAllowedNodeTypeModifications` action with the following parameter.
   + `CacheClusterId` – The name of the single-node Valkey or Redis OSS cluster you want to scale up.

   ```
   https://elasticache.us-west-2.amazonaws.com/
   	   ?Action=ListAllowedNodeTypeModifications
   	   &CacheClusterId=MyRedisCacheCluster
   	   &Version=2015-02-02
   	   &SignatureVersion=4
   	   &SignatureMethod=HmacSHA256
   	   &Timestamp=20150202T192317Z
   	   &X-Amz-Credential=<credential>
   ```

   For more information, see [ListAllowedNodeTypeModifications](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ListAllowedNodeTypeModifications.html) in the *Amazon ElastiCache API Reference*.

1. Modify your existing cluster specifying the cluster to scale up and the new, larger node type, using the `ModifyCacheCluster` ElastiCache API action and the following parameters.
   + `CacheClusterId` – The name of the cluster you are scaling up.
   + `CacheNodeType` – The new, larger node type you want to scale the cluster up to. This value must be one of the node types returned by the `ListAllowedNodeTypeModifications` action in the previous step.
   + `CacheParameterGroupName` – [Optional] Use this parameter if you are using `reserved-memory` to manage your cluster's reserved memory. Specify a custom cache parameter group that reserves the correct amount of memory for your new node type. If you are using `reserved-memory-percent` you can omit this parameter.
   + `ApplyImmediately` – Set to `true` to cause the scale-up process to be performed immediately. To postpone the scale-up process to the cluster's next maintenance window, use `ApplyImmediately``=false`.

   ```
   https://elasticache.us-west-2.amazonaws.com/
   	   ?Action=ModifyCacheCluster
   	   &ApplyImmediately=true
   	   &CacheClusterId=MyRedisCacheCluster
   	   &CacheNodeType=cache.m5.xlarge
   	   &CacheParameterGroupName redis7-cluster
   	   &Version=2015-02-02
   	   &SignatureVersion=4
   	   &SignatureMethod=HmacSHA256
   	   &Timestamp=20150202T192317Z
   	   &X-Amz-Credential=<credential>
   ```

   For more information, see [ModifyCacheCluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html) in the *Amazon ElastiCache API Reference*.

1. If you used `ApplyImmediately``=true`, check the status of the new cluster using the ElastiCache API `DescribeCacheClusters` action with the following parameter. When the status changes to *available*, you can begin using the new, larger cluster.
   + `CacheClusterId` – The name of your single-node Valkey or Redis OSS cluster. Use this parameter to describe a particular cluster rather than all clusters.

   ```
   https://elasticache.us-west-2.amazonaws.com/
   	   ?Action=DescribeCacheClusters
   	   &CacheClusterId=MyRedisCacheCluster
   	   &Version=2015-02-02
   	   &SignatureVersion=4
   	   &SignatureMethod=HmacSHA256
   	   &Timestamp=20150202T192317Z
   	   &X-Amz-Credential=<credential>
   ```

   For more information, see [DescribeCacheClusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheClusters.html) in the *Amazon ElastiCache API Reference*.

### Scaling down single-node Valkey or Redis OSS clusters
<a name="Scaling.RedisStandalone.ScaleDown"></a>

The following sections walk you through how to scale a single-node Valkey or Redis OSS cluster down to a smaller node type. Ensuring that the new, smaller node type is large enough to accommodate all the data and Valkey or Redis OSS overhead is important to the long-term success of your new Valkey or Redis OSS cluster. For more information, see [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](BestPractices.BGSAVE.md).

**Note**  
For clusters running the r6gd node type, you can only scale to node sizes within the r6gd node family.

**Topics**
+ [Scaling down a single-node Valkey or Redis OSS cluster (Console)](#Scaling.RedisStandalone.ScaleDown.CON)
+ [Scaling down single-node Valkey or Redis OSS clusters (AWS CLI)](#Scaling.RedisStandalone.ScaleUpDown-Modify.CLI)
+ [Scaling down single-node Valkey or Redis OSS clusters (ElastiCache API)](#Scaling.RedisStandalone.ScaleDown.API)

#### Scaling down a single-node Valkey or Redis OSS cluster (Console)
<a name="Scaling.RedisStandalone.ScaleDown.CON"></a>

The following procedure walks you through scaling your single-node Valkey or Redis OSS cluster down to a smaller node type using the ElastiCache console.

**Important**  
If your parameter group uses `reserved-memory` to set aside memory for Valkey or Redis OSS overhead, before you begin scaling be sure that you have a custom parameter group that reserves the correct amount of memory for your new node type. Alternatively, you can modify a custom parameter group so that it uses `reserved-memory-percent` and use that parameter group for your new cluster.  
If you're using `reserved-memory-percent`, doing this is not necessary.   
For more information, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md).

**To scale down your single-node Valkey or Redis OSS cluster (console)**

1. Ensure that the smaller node type is adequate for your data and overhead needs. 

1. If your parameter group uses `reserved-memory` to set aside memory for Valkey or Redis OSS overhead, ensure that you have a custom parameter group to set aside the correct amount of memory for your new node type.

   Alternatively, you can modify your custom parameter group to use `reserved-memory-percent`. For more information, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md).

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. From the list of clusters, choose the cluster you want to scale down. This cluster must be running the Valkey or Redis OSS engine and not the clustered Valkey or Redis OSS engine.

1. Choose **Modify**.

1. In the **Modify Cluster** wizard:

   1. Choose the node type you want to scale down to from the **Node type** list.

   1. If you're using `reserved-memory` to manage your memory, from the **Parameter Group** list, choose the custom parameter group that reserves the correct amount of memory for your new node type.

1. If you want to perform the scale-down process right away, choose the **Apply immediately** check box. If the **Apply immediately** check box is left not chosen, the scale-down process is performed during this cluster's next maintenance window.

1. Choose **Modify**.

1. When the cluster’s status changes from *modifying* to *available*, your cluster has scaled to the new node type. There is no need to update the endpoints in your application.

#### Scaling down single-node Valkey or Redis OSS clusters (AWS CLI)
<a name="Scaling.RedisStandalone.ScaleUpDown-Modify.CLI"></a>

The following procedure describes how to scale down a single-node Valkey or Redis OSS cluster using the AWS CLI. 

**To scale down a single-node Valkey or Redis OSS cluster (AWS CLI)**

1. Determine the node types you can scale down to by running the AWS CLI `list-allowed-node-type-modifications` command with the following parameter.
   + `--cache-cluster-id`

   For Linux, macOS, or Unix:

   ```
   aws elasticache list-allowed-node-type-modifications \
   	    --cache-cluster-id {{my-cache-cluster-id}}
   ```

   For Windows:

   ```
   aws elasticache list-allowed-node-type-modifications ^
   	    --cache-cluster-id {{my-cache-cluster-id}}
   ```

   Output from the above command looks something like this (JSON format).

   ```
   {
   	    "ScaleUpModifications": [
   	        "cache.m5.2xlarge", 
   	        "cache.m5.large", 
   	        "cache.m5.xlarge", 
   	        "cache.m4.10xlarge", 
   	        "cache.m4.2xlarge", 
   	        "cache.m4.4xlarge", 
   	        "cache.m4.large", 
   	        "cache.m4.xlarge", 
   	        "cache.r5.2xlarge", 
   	        "cache.r5.4xlarge", 
   	        "cache.r5.12xlarge", 
   	        "cache.r5.large", 
   	        "cache.r5.xlarge"
   	    ]
   	       "ScaleDownModifications": [
   	        "cache.t2.micro", 
   	        "cache.t2.small ", 
   	        "cache.t2.medium "
   	    ], 
   
   	}
   ```

   For more information, see [list-allowed-node-type-modifications](https://docs.aws.amazon.com/cli/latest/reference/elasticache/list-allowed-node-type-modifications.html) in the *AWS CLI Reference*.

1. Modify your existing cluster specifying the cluster to scale down and the new, smaller node type, using the AWS CLI `modify-cache-cluster` command and the following parameters.
   + `--cache-cluster-id` – The name of the cluster you are scaling down. 
   + `--cache-node-type` – The new node type you want to scale the cluster. This value must be one of the node types returned by the `list-allowed-node-type-modifications` command in step 1.
   + `--cache-parameter-group-name` – [Optional] Use this parameter if you are using `reserved-memory` to manage your cluster's reserved memory. Specify a custom cache parameter group that reserves the correct amount of memory for your new node type. If you are using `reserved-memory-percent` you can omit this parameter.
   + `--apply-immediately` – Causes the scale-down process to be applied immediately. To postpone the scale-up process to the cluster's next maintenance window, use the `--no-apply-immediately` parameter.

   For Linux, macOS, or Unix:

   ```
   aws elasticache modify-cache-cluster \
   	    --cache-cluster-id {{my-redis-cache-cluster}} \
   	    --cache-node-type {{cache.m5.xlarge}} \
   	    --cache-parameter-group-name {{redis7-cluster}} \
   	    --apply-immediately
   ```

   For Windows:

   ```
   aws elasticache modify-cache-cluster ^
   	    --cache-cluster-id {{my-redis-cache-cluster}} ^
   	    --cache-node-type {{cache.m5.xlarge}} ^
   	    --cache-parameter-group-name {{redis7-cluster}} ^
   	    --apply-immediately
   ```

   Output from the above command looks something like this (JSON format).

   ```
   {
   	    "CacheCluster": {
   	        "Engine": "redis", 
   	        "CacheParameterGroup": {
   	            "CacheNodeIdsToReboot": [], 
   	            "CacheParameterGroupName": "default.redis6,x", 
   	            "ParameterApplyStatus": "in-sync"
   	        }, 
   	        "SnapshotRetentionLimit": 1, 
   	        "CacheClusterId": "my-redis-cache-cluster", 
   	        "CacheSecurityGroups": [], 
   	        "NumCacheNodes": 1, 
   	        "SnapshotWindow": "00:00-01:00", 
   	        "CacheClusterCreateTime": "2017-02-21T22:34:09.645Z", 
   	        "AutoMinorVersionUpgrade": true, 
   	        "CacheClusterStatus": "modifying", 
   	        "PreferredAvailabilityZone": "us-west-2a", 
   	        "ClientDownloadLandingPage": "https://console.aws.amazon.com/elasticache/home#client-download:", 
   	        "CacheSubnetGroupName": "default", 
   	        "EngineVersion": "6.0", 
   	        "PendingModifiedValues": {
   	            "CacheNodeType": "cache.m5.2xlarge"
   	        }, 
   	        "PreferredMaintenanceWindow": "tue:11:30-tue:12:30", 
   	        "CacheNodeType": "cache.m5.large",
   	         "DataTiering": "disabled"
   	    }
   	}
   ```

   For more information, see [modify-cache-cluster](https://docs.aws.amazon.com/cli/latest/reference/elasticache/modify-cache-cluster.html) in the *AWS CLI Reference*.

1. If you used the `--apply-immediately`, check the status of the new cluster using the AWS CLI `describe-cache-clusters` command with the following parameter. When the status changes to *available*, you can begin using the new, smaller cluster.
   + `--cache-cluster-id` – The name of your single-node Valkey or Redis OSS cluster. Use this parameter to describe a particular cluster rather than all clusters.

   ```
   aws elasticache describe-cache-clusters --cache-cluster-id {{my-redis-cache-cluster}}
   ```

   For more information, see [describe-cache-clusters](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-clusters.html) in the *AWS CLI Reference*.

#### Scaling down single-node Valkey or Redis OSS clusters (ElastiCache API)
<a name="Scaling.RedisStandalone.ScaleDown.API"></a>

The following procedure describes how to scale updown a single-node Valkey or Redis OSS cluster using the ElastiCache API. 

**To scale down a single-node Valkey or Redis OSS cluster (ElastiCache API)**

1. Determine the node types you can scale down to by running the ElastiCache API `ListAllowedNodeTypeModifications` action with the following parameter.
   + `CacheClusterId` – The name of the single-node Valkey or Redis OSS cluster you want to scale down.

   ```
   https://elasticache.us-west-2.amazonaws.com/
   	   ?Action=ListAllowedNodeTypeModifications
   	   &CacheClusterId=MyRedisCacheCluster
   	   &Version=2015-02-02
   	   &SignatureVersion=4
   	   &SignatureMethod=HmacSHA256
   	   &Timestamp=20150202T192317Z
   	   &X-Amz-Credential=<credential>
   ```

   For more information, see [ListAllowedNodeTypeModifications](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ListAllowedNodeTypeModifications.html) in the *Amazon ElastiCache API Reference*.

1. Modify your existing cluster specifying the cluster to scale up and the new, larger node type, using the `ModifyCacheCluster` ElastiCache API action and the following parameters.
   + `CacheClusterId` – The name of the cluster you are scaling down.
   + `CacheNodeType` – The new, smaller node type you want to scale the cluster down to. This value must be one of the node types returned by the `ListAllowedNodeTypeModifications` action in previous step.
   + `CacheParameterGroupName` – [Optional] Use this parameter if you are using `reserved-memory` to manage your cluster's reserved memory. Specify a custom cache parameter group that reserves the correct amount of memory for your new node type. If you are using `reserved-memory-percent` you can omit this parameter.
   + `ApplyImmediately` – Set to `true` to cause the scale-down process to be performed immediately. To postpone the scale-up process to the cluster's next maintenance window, use `ApplyImmediately``=false`.

   ```
   https://elasticache.us-west-2.amazonaws.com/
   	   ?Action=ModifyCacheCluster
   	   &ApplyImmediately=true
   	   &CacheClusterId=MyRedisCacheCluster
   	   &CacheNodeType=cache.m5.xlarge
   	   &CacheParameterGroupName redis7-cluster
   	   &Version=2015-02-02
   	   &SignatureVersion=4
   	   &SignatureMethod=HmacSHA256
   	   &Timestamp=20150202T192317Z
   	   &X-Amz-Credential=<credential>
   ```

   For more information, see [ModifyCacheCluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html) in the *Amazon ElastiCache API Reference*.

1. If you used `ApplyImmediately``=true`, check the status of the new cluster using the ElastiCache API `DescribeCacheClusters` action with the following parameter. When the status changes to *available*, you can begin using the new, smaller cluster.
   + `CacheClusterId` – The name of your single-node Valkey or Redis OSS cluster. Use this parameter to describe a particular cluster rather than all clusters.

   ```
   https://elasticache.us-west-2.amazonaws.com/
   	   ?Action=DescribeCacheClusters
   	   &CacheClusterId=MyRedisCacheCluster
   	   &Version=2015-02-02
   	   &SignatureVersion=4
   	   &SignatureMethod=HmacSHA256
   	   &Timestamp=20150202T192317Z
   	   &X-Amz-Credential=<credential>
   ```

   For more information, see [DescribeCacheClusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheClusters.html) in the *Amazon ElastiCache API Reference*.