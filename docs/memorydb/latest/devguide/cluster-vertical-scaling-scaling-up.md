# Online scaling up

###### Topics

- [Scaling up MemoryDB clusters (Console)](#cluster-vertical-scaling-console "#cluster-vertical-scaling-console")
- [Scaling up MemoryDB clusters (AWS CLI)](#scaling.scaleUp.cli "#scaling.scaleUp.cli")
- [Scaling up MemoryDB clusters (MemoryDB API)](#verticalscaling.scaleup.api "#verticalscaling.scaleup.api")

## Scaling up MemoryDB clusters (Console)

The following procedure describes how to scale up a MemoryDB cluster using the AWS Management Console. During this process, your MemoryDB cluster will
continue to serve requests with minimal downtime.

###### To scale up a cluster (console)

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. From the list of clusters, choose the cluster.
3. Choose **Actions** and then choose **Modify**.
4. In the **Modify Cluster** dialog:
   1. Choose the node type you want to scale to from the **Node type** list. To scale up, select a node type larger than your existing node.

5. Choose **Save changes**.

The cluster's status changes to _modifying_.
When the status changes to _available_, the modification is complete
and you can begin using the new cluster.

## Scaling up MemoryDB clusters (AWS CLI)

The following procedure describes how to scale up a MemoryDB cluster using the AWS CLI. During this process, your MemoryDB cluster will
continue to serve requests with minimal downtime.

###### To scale up a MemoryDB cluster (AWS CLI)

1. Determine the node types you can scale up to by running the AWS CLI
   `list-allowed-node-type-updates` command with the following parameter.

For Linux, macOS, or Unix:

```
aws memorydb list-allowed-node-type-updates \
	    --cluster-name `my-cluster-name`
```

For Windows:

```
aws memorydb list-allowed-node-type-updates ^
	    --cluster-name `my-cluster-name`
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

For more information, see [list-allowed-node-type-updates](../../../cli/latest/reference/memorydb/list-allowed-node-type-updates.md "../../../cli/latest/reference/memorydb/list-allowed-node-type-updates.md")
in the _AWS CLI Reference_. 2. Modify your cluster to scale up to the new, larger node type, using the AWS CLI `update-cluster` command
and the following parameters.

    * `--cluster-name` –
     The name of the cluster you are scaling up to.
    * `--node-type` –
     The new node type you want to scale the cluster.
     This value must be one of the node types returned by the
     `list-allowed-node-type-updates` command in step 1.

For Linux, macOS, or Unix:

```
aws memorydb update-cluster  \
	--cluster-name `my-cluster` \
	--node-type `db.r6g.2xlarge`
```

For Windows:

```
aws memorydb update-cluster ^
	    --cluster-name `my-cluster` ^
	    --node-type `db.r6g.2xlarge` ^

```

For more information, see [update-cluster](../../../cli/latest/reference/memorydb/update-cluster.md "../../../cli/latest/reference/memorydb/update-cluster.md").

## Scaling up MemoryDB clusters (MemoryDB API)

The following process scales your cluster from its current node type to a new,
larger node type using the MemoryDB API.
During this process, MemoryDB updates the DNS entries so they point to the new nodes. You can scale auto-failover enabled clusters while the cluster continues to stay online and serve incoming requests.

The amount of time it takes to scale up to a larger node type varies,
depending upon your node type and the amount of data in your current cluster.

###### To scale up a MemoryDB cluster (MemoryDB API)

1. Determine which node types you can scale up to using the MemoryDB API
   `ListAllowedNodeTypeUpdates` action with the following parameter.
   - `ClusterName` – the name of the cluster.
     Use this parameter to describe a specific cluster rather than all clusters.

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

For more information, see [ListAllowedNodeTypeUpdates](../APIReference/API_ListAllowedNodeTypeUpdates.md "../APIReference/API_ListAllowedNodeTypeUpdates.md")
in the _MemoryDB API Reference_. 2. Scale your current cluster up to the new node type using the
`UpdateCluster` MemoryDB API
action and with the following parameters.

    * `ClusterName` –
     the name of the cluster.
    * `NodeType` –
     the new, larger node type of the clusters in this cluster.
     This value must be one of the instance types returned by the `ListAllowedNodeTypeUpdates`
     action in step 1.

```
https://memory-db.us-east-1.amazonaws.com/
	   ?Action=UpdateCluster
	   &NodeType=db.r6g.2xlarge
	   &ClusterName=myCluster
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

For more information, see [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md").
