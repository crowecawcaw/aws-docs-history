

# Online scaling down
<a name="cluster-vertical-scaling-scaling-down"></a>

**Topics**
+ [Scaling down MemoryDB clusters (Console)](#cluster-vertical-scaling-down-console)
+ [Scaling down MemoryDB clusters (AWS CLI)](#scaling.scaledown.cli)
+ [Scaling down MemoryDB clusters (MemoryDB API)](#scaling.vertical.scaledown.api)

## Scaling down MemoryDB clusters (Console)
<a name="cluster-vertical-scaling-down-console"></a>

The following procedure describes how to scale down a MemoryDB cluster using the AWS Management Console. During this process, your MemoryDB cluster will continue to serve requests with minimal downtime.

**To scale down a MemoryDB cluster (console)**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. From the list of clusters, choose your preferred cluster. 

1. Choose **Actions** and then choose **Modify**.

1. In the **Modify Cluster** dialog:

   1. Choose the node type you want to scale to from the **Node type** list. To scale down, select a node type smaller than your existing node. Note that not all node types are available to scale down to.

1. Choose **Save changes**.

   The cluster's status changes to *modifying*. When the status changes to *available*, the modification is complete and you can begin using the new cluster.

## Scaling down MemoryDB clusters (AWS CLI)
<a name="scaling.scaledown.cli"></a>

The following procedure describes how to scale down a MemoryDB cluster using the AWS CLI. During this process, your MemoryDB cluster will continue to serve requests with minimal downtime.

**To scale down a MemoryDB cluster (AWS CLI)**

1. Determine the node types you can scale down to by running the AWS CLI `list-allowed-node-type-updates` command with the following parameter.

   For Linux, macOS, or Unix:

   ```
   aws memorydb list-allowed-node-type-updates \
   	    --cluster-name {{my-cluster-name}}
   ```

   For Windows:

   ```
   aws memorydb list-allowed-node-type-updates ^
   	    --cluster-name {{my-cluster-name}}
   ```

   Output from the above command looks something like this (JSON format).

   ```
   {
   	    "ScaleUpNodeTypes": [
   	        "db.r6g.2xlarge", 
   	        "db.r6g.large"	        
   	    ],
   	    "ScaleDownNodeTypes": [
   	        "db.r6g.large"	        
   	    ], 
   }
   ```

   For more information, see [list-allowed-node-type-updates](https://docs.aws.amazon.com/cli/latest/reference/memorydb/list-allowed-node-type-updates.html).

1. Modify your cluster to scale down to the new, smaller node type, using the `update-cluster` command and the following parameters.
   + `--cluster-name` – The name of the cluster you are scaling down to. 
   + `--node-type` – The new node type you want to scale the cluster. This value must be one of the node types returned by the `list-allowed-node-type-updates` command in step 1.

   For Linux, macOS, or Unix:

   ```
   aws memorydb update-cluster  \
   	    --cluster-name {{my-cluster}} \
   	    --node-type {{db.r6g.large}}
   ```

   For Windows:

   ```
   aws memorydb update-cluster ^
   	    --cluster-name {{my-cluster}} ^
   	    --node-type {{db.r6g.large}}
   ```

   For more information, see [update-cluster](https://docs.aws.amazon.com/cli/latest/reference/memorydb/update-cluster.html).

## Scaling down MemoryDB clusters (MemoryDB API)
<a name="scaling.vertical.scaledown.api"></a>

The following process scales your cluster from its current node type to a new, smaller node type using the MemoryDB API. During this process, your MemoryDB cluster will continue to serve requests with minimal downtime.

The amount of time it takes to scale down to a smaller node type varies, depending upon your node type and the amount of data in your current cluster.

**Scaling down (MemoryDB API)**

1. Determine which node types you can scale down to using the [ListAllowedNodeTypeUpdates](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListAllowedNodeTypeUpdates.html) API with the following parameter:
   + `ClusterName` – the name of the cluster. Use this parameter to describe a specific cluster rather than all clusters.

   ```
   https://memory-db.us-east-1.amazonaws.com/
   	   ?Action=ListAllowedNodeTypeUpdates
   	   &ClusterName=MyCluster
   	   &Version=2021-01-01
   	   &SignatureVersion=4
   	   &SignatureMethod=HmacSHA256
   	   &Timestamp=20210802T192317Z
   	   &X-Amz-Credential=<credential>
   ```

1. Scale your current cluster down to the new node type using the [UpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateCluster.html) API with the following parameters.
   + `ClusterName` – the name of the cluster.
   + `NodeType` – the new, smaller node type of the clusters in this cluster. This value must be one of the instance types returned by the `ListAllowedNodeTypeUpdates` action in step 1.

   ```
   https://memory-db.us-east-1.amazonaws.com/
   	   ?Action=UpdateCluster	   
   	   &NodeType=db.r6g.2xlarge
   	   &ClusterName=myReplGroup
   	   &SignatureVersion=4
   	   &SignatureMethod=HmacSHA256
   	   &Timestamp=20210801T220302Z
   	   &Version=2021-01-01
   	   &X-Amz-Algorithm=Amazon4-HMAC-SHA256
   	   &X-Amz-Date=20210801T220302Z
   	   &X-Amz-SignedHeaders=Host
   	   &X-Amz-Expires=20210801T220302Z
   	   &X-Amz-Credential=<credential>
   	   &X-Amz-Signature=<signature>
   ```