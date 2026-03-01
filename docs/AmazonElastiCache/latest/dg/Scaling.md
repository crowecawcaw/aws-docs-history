# Scaling replica nodes for Valkey or Redis OSS (Cluster Mode Disabled)

A Valkey or Redis OSS cluster with replica nodes (called _replication group_ in the
API/CLI) provides high availability via replication that has Multi-AZ with automatic
failover enabled. A cluster with replica nodes is a logical collection of up to six
Valkey or Redis OSS nodes where one node, the Primary, is able to serve both read and write
requests. All the other nodes in the cluster are read-only replicas of the Primary.
Data written to the Primary is asynchronously replicated to all the read replicas in the
cluster. Because Valkey or Redis OSS (cluster mode disabled) does not support partitioning your data across multiple
clusters, each node in a Valkey or Redis OSS (cluster mode disabled) replication group contains the entire cache
dataset. Valkey or Redis OSS (cluster mode enabled) clusters support partitioning your data across up to
500 shards.

To change the data capacity of your cluster you must scale it up to a larger node type,
or down to a smaller node type.

To change the read capacity of your cluster, add more read replicas, up to a
maximum of 5, or remove read replicas.

The ElastiCache scaling up process is designed to make a best effort to retain your existing data and
requires successful Valkey or Redis OSS replication. For Valkey or Redis OSS clusters with replicas,
we recommend that sufficient memory be made available to Valkey or Redis OSS.

###### Topics

- [Scaling up Valkey or Redis OSS clusters with replicas](#Scaling.RedisReplGrps.ScaleUp "#Scaling.RedisReplGrps.ScaleUp")
- [Scaling down Valkey or Redis OSS clusters with replicas](#Scaling.RedisReplGrps.ScaleDown "#Scaling.RedisReplGrps.ScaleDown")
- [Increasing read capacity](#Scaling.RedisReplGrps.ScaleOut "#Scaling.RedisReplGrps.ScaleOut")
- [Decreasing read capacity](#Scaling.RedisReplGrps.ScaleIn "#Scaling.RedisReplGrps.ScaleIn")

###### Related Topics

- [High availability using replication groups](Replication.md "Replication.md")
- [Replication: Valkey and Redis OSS Cluster Mode Disabled vs. Enabled](Replication.md "Replication.md")
- [Minimizing downtime in ElastiCache by using Multi-AZ with Valkey and Redis OSS](AutoFailover.md "AutoFailover.md")
- [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](BestPractices.md "BestPractices.md")

###### Topics

- [Scaling up Valkey or Redis OSS clusters with replicas](#Scaling.RedisReplGrps.ScaleUp "#Scaling.RedisReplGrps.ScaleUp")
- [Scaling down Valkey or Redis OSS clusters with replicas](#Scaling.RedisReplGrps.ScaleDown "#Scaling.RedisReplGrps.ScaleDown")
- [Increasing read capacity](#Scaling.RedisReplGrps.ScaleOut "#Scaling.RedisReplGrps.ScaleOut")
- [Decreasing read capacity](#Scaling.RedisReplGrps.ScaleIn "#Scaling.RedisReplGrps.ScaleIn")

## Scaling up Valkey or Redis OSS clusters with replicas

Amazon ElastiCache provides console, CLI, and API support for scaling your Valkey or Redis OSS (cluster mode disabled) replication group up.

When the scale-up process is initiated, ElastiCache does the following:

1. Launches a replication group using the new node type.
2. Copies all the data from the current primary node to the new primary node.
3. Syncs the new read replicas with the new primary node.
4. Updates the DNS entries so they point to the new nodes. Because of this you don't have to update the endpoints in your application. For Valkey 7.2 and above or Redis OSS 5.0.5 and above, you can scale auto failover enabled clusters while the cluster continues to stay online and serve incoming requests. On Redis OSS version 4.0.10 and below, you may notice a brief interruption of reads and writes on previous versions from the primary node while the DNS entry is updated.
5. Deletes the old nodes (CLI/API: replication group). You will notice a brief interruption (a few seconds) of reads and writes from the old nodes because the connections to the old nodes will be disconnected.

How long this process takes is dependent upon your node type and how much data is in your cluster.

As shown in the following table,
your Valkey or Redis OSS scale-up operation is blocked if you have an engine upgrade scheduled for the
cluster’s next maintenance window.

| Blocked Valkey or Redis OSS operations | Pending Operations       | Blocked Operations |
| -------------------------------------- | ------------------------ | ------------------ |
| Scale up                               | Immediate engine upgrade |
| Engine upgrade                         | Immediate scale up       |
| Scale up and engine upgrade            | Immediate scale up       |
| Immediate engine upgrade               |

If you have a pending operation that is blocking you, you can do one of the following.

- Schedule your Valkey or Redis OSS scale-up operation for the next maintenance window by
  clearing the **Apply immediately** check box
  (CLI use: `--no-apply-immediately`, API use: `ApplyImmediately=false`).
- Wait until your next maintenance window (or after) to perform
  your Valkey or Redis OSS scale-up operation.
- Add the Valkey or Redis OSS engine upgrade to this cluster modification with the
  **Apply Immediately** check box chosen
  (CLI use: `--apply-immediately`, API use: `ApplyImmediately=true`).
  This unblocks your scale-up operation by causing the engine upgrade to be performed immediately.

The following sections describe how to scale your Valkey or Redis OSS cluster with replicas up
using the ElastiCache console, the AWS CLI, and the ElastiCache API.

###### Important

If your parameter group uses `reserved-memory` to set aside memory for Valkey or Redis OSS overhead, before you begin scaling be sure that you have a custom parameter
group that reserves the correct amount of memory for your new node type.
Alternatively, you can modify a custom parameter group so that it uses
`reserved-memory-percent` and use that parameter group for your
new cluster.

If you're using `reserved-memory-percent`, doing this is not necessary.

For more information, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md "redis-memory-management.md").

The amount of time it takes to scale up to a larger node type varies, depending upon the node type and
the amount of data in your current cluster.

The following process scales your cluster with replicas from its current node type to a new, larger node type
using the ElastiCache console.
During this process, there may be a brief interruption of reads and writes for other versions from the primary node while the DNS entry is updated.
you might see less than 1 second downtime for nodes running on 5.0.6 versions and above and a few seconds for older versions.

###### To scale up Valkey or Redis OSS cluster with replicas (console)

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the navigation pane, choose **Valkey clusters** or **Redis OSS clusters**
3. From the list of clusters, choose the cluster you want to scale up.
   This cluster must be running the Valkey or Redis OSS engine and not the clustered Valkey or Redis OSS engine.
4. Choose **Modify**.
5. In the **Modify Cluster** wizard:
   1. Choose the node type you want to scale to from the **Node type** list. Note that not all node types are available to scale down to.
   2. If you're using `reserved-memory` to manage your memory,
      from the **Parameter Group** list, choose the custom parameter
      group that reserves the correct amount of memory for your new node type.

6. If you want to perform the scale-up process right away, choose the **Apply immediately** check box.
   If the **Apply immediately** check box is left not chosen,
   the scale-up process is performed during this cluster's next maintenance window.
7. Choose **Modify**.
8. When the cluster’s status changes from _modifying_ to
   _available_, your cluster has scaled to the new
   node type. There is no need to update the
   endpoints in your application.

The following process scales your replication group from its current node type to a new, larger node type using the AWS CLI.

During this process, ElastiCache updates the DNS entries so they point to the new nodes. Because of this you don't have to update the endpoints in your application. For Valkey 7.2 and above or Redis OSS 5.0.5 and above,
you can scale auto failover enabled clusters while the cluster continues to stay online and serve incoming requests. On version 4.0.10 and below, you may notice a brief interruption of reads and writes on previous versions from the primary node while the DNS entry is updated..

The amount of time it takes to scale up to a larger node type varies,
depending upon your node type and the amount of data in your current cluster.

###### To scale up a Valkey or Redis OSS Replication Group (AWS CLI)

1.  Determine which node types you can scale up to by running the AWS CLI
    `list-allowed-node-type-modifications` command with the following parameter.

        * `--replication-group-id` – the name of the replication group.
         Use this parameter to describe a particular replication group rather than all
         replication groups.

    For Linux, macOS, or Unix:

```
aws elasticache list-allowed-node-type-modifications \
	    --replication-group-id `my-repl-group`
```

For Windows:

```
aws elasticache list-allowed-node-type-modifications ^
	    --replication-group-id `my-repl-group`
```

Output from this operation looks something like this (JSON format).

```
{
	    "ScaleUpModifications": [
	        "cache.m3.2xlarge",
	        "cache.m3.large",
	        "cache.m3.xlarge",
	        "cache.m4.10xlarge",
	        "cache.m4.2xlarge",
	        "cache.m4.4xlarge",
	        "cache.m4.large",
	        "cache.m4.xlarge",
	        "cache.r3.2xlarge",
	        "cache.r3.4xlarge",
	        "cache.r3.8xlarge",
	        "cache.r3.large",
	        "cache.r3.xlarge"
	    ]
	}
```

For more information, see list-allowed-node-type-modifications
in the _AWS CLI Reference_. 2. Scale your current replication group up to the new node type using the AWS CLI
`modify-replication-group` command with the following parameters.

    * `--replication-group-id` –
     the name of the replication group.
    * `--cache-node-type` –
     the new, larger node type of the clusters in this replication group.
     This value must be one of the instance types returned by the `list-allowed-node-type-modifications`
     command in the previous step.
    * `--cache-parameter-group-name` –
     [Optional] Use this parameter if you are using `reserved-memory` to manage your
     cluster's reserved memory.
     Specify a custom cache parameter group that reserves the correct amount of memory for your new
     node type.
     If you are using `reserved-memory-percent` you can omit this parameter.
    * `--apply-immediately` – Causes the scale-up process to be applied
     immediately. To postpone the scale-up operation to the next maintenance window, use
     `--no-apply-immediately`.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
	    --replication-group-id `my-repl-group` \
	    --cache-node-type `cache.m3.xlarge` \
	    --cache-parameter-group-name `redis32-m3-2xl` \
	    --apply-immediately
```

For Windows:

```
aws elasticache modify-replication-group ^
	    --replication-group-id `my-repl-group` ^
	    --cache-node-type `cache.m3.xlarge` ^
	    --cache-parameter-group-name `redis32-m3-2xl` \
	    --apply-immediately
```

Output from this command looks something like this (JSON format).

```

{
	"ReplicationGroup": {
		"Status": "available",
		"Description": "Some description",
		"NodeGroups": [{
			"Status": "available",
			"NodeGroupMembers": [{
					"CurrentRole": "primary",
					"PreferredAvailabilityZone": "us-west-2b",
					"CacheNodeId": "0001",
					"ReadEndpoint": {
						"Port": 6379,
						"Address": "my-repl-group-001.8fdx4s.0001.usw2.cache.amazonaws.com"
					},
					"CacheClusterId": "my-repl-group-001"
				},
				{
					"CurrentRole": "replica",
					"PreferredAvailabilityZone": "us-west-2c",
					"CacheNodeId": "0001",
					"ReadEndpoint": {
						"Port": 6379,
						"Address": "my-repl-group-002.8fdx4s.0001.usw2.cache.amazonaws.com"
					},
					"CacheClusterId": "my-repl-group-002"
				}
			],
			"NodeGroupId": "0001",
			"PrimaryEndpoint": {
				"Port": 6379,
				"Address": "my-repl-group.8fdx4s.ng.0001.usw2.cache.amazonaws.com"
			}
		}],
		"ReplicationGroupId": "my-repl-group",
		"SnapshotRetentionLimit": 1,
		"AutomaticFailover": "disabled",
		"SnapshotWindow": "12:00-13:00",
		"SnapshottingClusterId": "my-repl-group-002",
		"MemberClusters": [
			"my-repl-group-001",
			"my-repl-group-002"
		],
		"PendingModifiedValues": {}
	}
}
```

For more information, see modify-replication-group
in the _AWS CLI Reference_. 3. If you used the `--apply-immediately` parameter,
monitor the status of the replication group using the AWS CLI
`describe-replication-group` command with the following parameter.
While the status is still in _modifying_,
you might see less than 1 second downtime for nodes running on 5.0.6 versions and above and a brief interruption of reads and writes for older versions from the primary node while the DNS entry is updated.

    * `--replication-group-id` – the name of the replication group.
     Use this parameter to describe a particular replication group rather than all replication
     groups.

For Linux, macOS, or Unix:

```
aws elasticache describe-replication-groups \
	    --replication-group-id `my-replication-group`
```

For Windows:

```
aws elasticache describe-replication-groups ^
	    --replication-group-id `my-replication-group`
```

For more information, see [describe-replication-groups](../../../cli/latest/reference/elasticache/describe-replication-groups.md "../../../cli/latest/reference/elasticache/describe-replication-groups.md") in the _AWS CLI Reference_.

The following process scales your replication group from its current node type to a new,
larger node type using the ElastiCache API.

For Valkey 7.2 and above or Redis OSS 5.0.5 and above, you can scale auto failover enabled clusters while the cluster continues to stay online and serve incoming requests. On version Redis OSS 4.0.10 and below, you may notice a brief interruption of reads and writes on previous versions from the primary node while the DNS entry is updated.

The amount of time it takes to scale up to a larger node type varies,
depending upon your node type and the amount of data in your current cluster.

###### To scale up a Valkey or Redis OSS Replication Group (ElastiCache API)

1. Determine which node types you can scale up to using the ElastiCache API
   `ListAllowedNodeTypeModifications` action with the following parameter.
   - `ReplicationGroupId` – the name of the replication group.
     Use this parameter to describe a specific replication group rather than all replication
     groups.

```
https://elasticache.us-west-2.amazonaws.com/
	   ?Action=ListAllowedNodeTypeModifications
	   &ReplicationGroupId=MyReplGroup
	   &Version=2015-02-02
	   &SignatureVersion=4
	   &SignatureMethod=HmacSHA256
	   &Timestamp=20150202T192317Z
	   &X-Amz-Credential=<credential>
```

For more information, see ListAllowedNodeTypeModifications
in the _Amazon ElastiCache API Reference_. 2. Scale your current replication group up to the new node type using the
`ModifyReplicationGroup` ElastiCache API
action and with the following parameters.

    * `ReplicationGroupId` –
     the name of the replication group.
    * `CacheNodeType` –
     the new, larger node type of the clusters in this replication group.
     This value must be one of the instance types returned by the `ListAllowedNodeTypeModifications`
     action in th previous step.
    * `CacheParameterGroupName` –
     [Optional] Use this parameter if you are using `reserved-memory` to manage your
     cluster's reserved memory.
     Specify a custom cache parameter group that reserves the correct amount of memory for your new
     node type.
     If you are using `reserved-memory-percent` you can omit this parameter.
    * `ApplyImmediately` – Set to `true` to causes
     the scale-up process to be applied immediately. To postpone the scale-up process to the next maintenance window, use
     `ApplyImmediately``=false`.

```
https://elasticache.us-west-2.amazonaws.com/
	   ?Action=ModifyReplicationGroup
	   &ApplyImmediately=true
	   &CacheNodeType=cache.m3.2xlarge
	   &CacheParameterGroupName=redis32-m3-2xl
	   &ReplicationGroupId=myReplGroup
	   &SignatureVersion=4
	   &SignatureMethod=HmacSHA256
	   &Timestamp=20141201T220302Z
	   &Version=2014-12-01
	   &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
	   &X-Amz-Date=20141201T220302Z
	   &X-Amz-SignedHeaders=Host
	   &X-Amz-Expires=20141201T220302Z
	   &X-Amz-Credential=<credential>
	   &X-Amz-Signature=<signature>
```

For more information, see ModifyReplicationGroup
in the _Amazon ElastiCache API Reference_. 3. If you used `ApplyImmediately``=true`,
monitor the status of the replication group using the ElastiCache API
`DescribeReplicationGroups` action with the following parameters.
When the status changes from _modifying_
to _available_, you can begin writing to your
new, scaled up replication group.

    * `ReplicationGroupId` – the name of the replication group.
     Use this parameter to describe a particular replication group rather than all
     replication groups.

```
https://elasticache.us-west-2.amazonaws.com/
	   ?Action=DescribeReplicationGroups
	   &ReplicationGroupId=MyReplGroup
	   &Version=2015-02-02
	   &SignatureVersion=4
	   &SignatureMethod=HmacSHA256
	   &Timestamp=20150202T192317Z
	   &X-Amz-Credential=<credential>
```

For more information, see DescribeReplicationGroups
in the _Amazon ElastiCache API Reference_.

## Scaling down Valkey or Redis OSS clusters with replicas

The following sections walk you through how to scale a Valkey or Redis OSS (cluster mode disabled) cluster with
replica nodes down to a smaller node type. Ensuring that the new, smaller node type
is large enough to accommodate all the data and overhead is very important to
success. For more information, see [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](BestPractices.md "BestPractices.md").

###### Note

For clusters running the r6gd node type, you can only scale to node sizes within the r6gd node family.

###### Important

If your parameter group uses `reserved-memory` to set aside memory for Valkey or Redis OSS overhead, before you begin scaling be sure that you have a custom parameter
group that reserves the correct amount of memory for your new node type.
Alternatively, you can modify a custom parameter group so that it uses
`reserved-memory-percent` and use that parameter group for your
new cluster.

If you're using `reserved-memory-percent`, doing this is not necessary.

For more information, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md "redis-memory-management.md").

###### Topics

The following process scales your Valkey or Redis OSS cluster with replica nodes to a smaller node
type using the ElastiCache console.

###### To scale down a Valkey or Redis OSS cluster with replica nodes (console)

1. Ensure that the smaller node type is adequate for your data and overhead needs.
2. If your parameter group uses `reserved-memory` to set aside memory for Valkey or Redis OSS overhead, ensure that you have a custom parameter group to set aside the
   correct amount of memory for your new node type.

Alternatively, you can modify your custom parameter group to use `reserved-memory-percent`.
For more information, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md "redis-memory-management.md"). 3. Sign in to the AWS Management Console and open the ElastiCache console at
[https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/"). 4. From the list of clusters, choose the cluster you want to scale down.
This cluster must be running the Valkey or Redis OSS engine and not the clustered Valkey or Redis OSS engine. 5. Choose **Modify**. 6. In the **Modify Cluster** wizard:

    1. Choose the node type you want to scale down to from the **Node type** list.
    2. If you're using `reserved-memory` to manage your memory,
     from the **Parameter Group** list, choose the custom parameter
     group that reserves the correct amount of memory for your new node type.

7. If you want to perform the scale-down process right away, choose the **Apply immediately** check box.
   If the **Apply immediately** check box is left not chosen,
   the scale-down process is performed during this cluster's next maintenance window.
8. Choose **Modify**.
9. When the cluster’s status changes from _modifying_ to
   _available_, your cluster has scaled to the new
   node type. There is no need to update the
   endpoints in your application.

The following process scales your replication group from its current node type to a new, smaller node type using the AWS CLI.

During this process, ElastiCache updates the DNS entries so they point to the new nodes. Because of this you don't have to update the endpoints in your application. For Valkey 7.2 above or Redis OSS 5.0.5 and above, you can scale auto failover enabled clusters while the cluster continues to stay online and serve incoming requests. On version 4.0.10 and below, you may notice a brief interruption of reads and writes on previous versions from the primary node while the DNS entry is updated..

However, reads from the read replica clusters continue uninterrupted.

The amount of time it takes to scale down to a smaller node type varies,
depending upon your node type and the amount of data in your current cluster.

###### To scale down a Valkey or Redis OSS Replication Group (AWS CLI)

1.  Determine which node types you can scale down to by running the AWS CLI
    `list-allowed-node-type-modifications` command with the following parameter.

        * `--replication-group-id` – the name of the replication group.
         Use this parameter to describe a particular replication group rather than all
         replication groups.

    For Linux, macOS, or Unix:

```
aws elasticache list-allowed-node-type-modifications \
	    --replication-group-id `my-repl-group`
```

For Windows:

```
aws elasticache list-allowed-node-type-modifications ^
	    --replication-group-id `my-repl-group`
```

Output from this operation looks something like this (JSON format).

```
{
	    "ScaleDownModifications": [
	        "cache.m3.2xlarge",
	        "cache.m3.large",
	        "cache.m3.xlarge",
	        "cache.m4.10xlarge",
	        "cache.m4.2xlarge",
	        "cache.m4.4xlarge",
	        "cache.m4.large",
	        "cache.m4.xlarge",
	        "cache.r3.2xlarge",
	        "cache.r3.4xlarge",
	        "cache.r3.8xlarge",
	        "cache.r3.large",
	        "cache.r3.xlarge"
	    ]
	}
```

For more information, see list-allowed-node-type-modifications
in the _AWS CLI Reference_. 2. Scale your current replication group up to the new node type using the AWS CLI
`modify-replication-group` command with the following parameters.

    * `--replication-group-id` –
     the name of the replication group.
    * `--cache-node-type` –
     the new, smaller node type of the clusters in this replication group.
     This value must be one of the instance types returned by the `list-allowed-node-type-modifications`
     command in the previous step.
    * `--cache-parameter-group-name` –
     [Optional] Use this parameter if you are using `reserved-memory` to manage your
     cluster's reserved memory.
     Specify a custom cache parameter group that reserves the correct amount of memory for your new
     node type.
     If you are using `reserved-memory-percent` you can omit this parameter.
    * `--apply-immediately` – Causes the scale-up process to be applied
     immediately. To postpone the scale-up operation to the next maintenance window, use
     `--no-apply-immediately`.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
	    --replication-group-id `my-repl-group` \
	    --cache-node-type `cache.t2.small`  \
	    --cache-parameter-group-name `redis32-m3-2xl` \
	    --apply-immediately
```

For Windows:

```
aws elasticache modify-replication-group ^
	    --replication-group-id `my-repl-group` ^
	    --cache-node-type `cache.t2.small`  ^
	    --cache-parameter-group-name `redis32-m3-2xl` \
	    --apply-immediately
```

Output from this command looks something like this (JSON format).

```

{"ReplicationGroup": {
	        "Status": "available",
	        "Description": "Some description",
	        "NodeGroups": [
	            {
	                "Status": "available",
	                "NodeGroupMembers": [
	                    {
	                        "CurrentRole": "primary",
	                        "PreferredAvailabilityZone": "us-west-2b",
	                        "CacheNodeId": "0001",
	                        "ReadEndpoint": {
	                            "Port": 6379,
	                            "Address": "my-repl-group-001.8fdx4s.0001.usw2.cache.amazonaws.com"
	                        },
	                        "CacheClusterId": "my-repl-group-001"
	                    },
	                    {
	                        "CurrentRole": "replica",
	                        "PreferredAvailabilityZone": "us-west-2c",
	                        "CacheNodeId": "0001",
	                        "ReadEndpoint": {
	                            "Port": 6379,
	                            "Address": "my-repl-group-002.8fdx4s.0001.usw2.cache.amazonaws.com"
	                        },
	                        "CacheClusterId": "my-repl-group-002"
	                    }
	                ],
	                "NodeGroupId": "0001",
	                "PrimaryEndpoint": {
	                    "Port": 6379,
	                    "Address": "my-repl-group.8fdx4s.ng.0001.usw2.cache.amazonaws.com"
	                }
	            }
	        ],
	        "ReplicationGroupId": "my-repl-group",
	        "SnapshotRetentionLimit": 1,
	        "AutomaticFailover": "disabled",
	        "SnapshotWindow": "12:00-13:00",
	        "SnapshottingClusterId": "my-repl-group-002",
	        "MemberClusters": [
	            "my-repl-group-001",
	            "my-repl-group-002",
	        ],
	        "PendingModifiedValues": {}
	    }
	}
```

For more information, see modify-replication-group
in the _AWS CLI Reference_. 3. If you used the `--apply-immediately` parameter,
monitor the status of the replication group using the AWS CLI
`describe-replication-group` command with the following parameter.
When the status changes from _modifying_
to _available_, you can begin writing to your
new, scaled down replication group.

    * `--replication-group-id` – the name of the replication group.
     Use this parameter to describe a particular replication group rather than all replication
     groups.

For Linux, macOS, or Unix:

```
aws elasticache describe-replication-group \
	    --replication-group-id `my-replication-group`
```

For Windows:

```
aws elasticache describe-replication-groups ^
	    --replication-group-id `my-replication-group`
```

For more information, see [describe-replication-groups](../../../cli/latest/reference/elasticache/describe-replication-groups.md "../../../cli/latest/reference/elasticache/describe-replication-groups.md") in the _AWS CLI Reference_.

The following process scales your replication group from its current node type to a new,
smaller node type using the ElastiCache API.

During this process, ElastiCache updates the DNS entries so they point to the new nodes. Because of this you don't have to update the endpoints in your application. For Valkey 7.2 and above or Redis OSS 5.0.5 and above, you can scale auto failover enabled clusters while the cluster continues to stay online and serve incoming requests. On Redis OSS version 4.0.10 and below, you may notice a brief interruption of reads and writes on previous versions from the primary node while the DNS entry is updated..

However, reads from the read replica clusters continue uninterrupted.

The amount of time it takes to scale down to a smaller node type varies,
depending upon your node type and the amount of data in your current cluster.

###### To scale down a Valkey or Redis OSS Replication Group (ElastiCache API)

1. Determine which node types you can scale down to using the ElastiCache API
   `ListAllowedNodeTypeModifications` action with the following parameter.
   - `ReplicationGroupId` – the name of the replication group.
     Use this parameter to describe a specific replication group rather than all replication
     groups.

```
https://elasticache.us-west-2.amazonaws.com/
	   ?Action=ListAllowedNodeTypeModifications
	   &ReplicationGroupId=MyReplGroup
	   &Version=2015-02-02
	   &SignatureVersion=4
	   &SignatureMethod=HmacSHA256
	   &Timestamp=20150202T192317Z
	   &X-Amz-Credential=<credential>
```

For more information, see ListAllowedNodeTypeModifications
in the _Amazon ElastiCache API Reference_. 2. Scale your current replication group up to the new node type using the
`ModifyReplicationGroup` ElastiCache API
action and with the following parameters.

    * `ReplicationGroupId` –
     the name of the replication group.
    * `CacheNodeType` –
     the new, smaller node type of the clusters in this replication group.
     This value must be one of the instance types returned by the `ListAllowedNodeTypeModifications`
     action in the previous step.
    * `CacheParameterGroupName` –
     [Optional] Use this parameter if you are using `reserved-memory` to manage your
     cluster's reserved memory.
     Specify a custom cache parameter group that reserves the correct amount of memory for your new
     node type.
     If you are using `reserved-memory-percent` you can omit this parameter.
    * `ApplyImmediately` – Set to `true` to causes
     the scale-up process to be applied immediately. To postpone the scale-down process to the next maintenance window, use
     `ApplyImmediately``=false`.

```
https://elasticache.us-west-2.amazonaws.com/
	   ?Action=ModifyReplicationGroup
	   &ApplyImmediately=true
	   &CacheNodeType=cache.m3.2xlarge
	   &CacheParameterGroupName=redis32-m3-2xl
	   &ReplicationGroupId=myReplGroup
	   &SignatureVersion=4
	   &SignatureMethod=HmacSHA256
	   &Timestamp=20141201T220302Z
	   &Version=2014-12-01
	   &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
	   &X-Amz-Date=20141201T220302Z
	   &X-Amz-SignedHeaders=Host
	   &X-Amz-Expires=20141201T220302Z
	   &X-Amz-Credential=<credential>
	   &X-Amz-Signature=<signature>
```

For more information, see ModifyReplicationGroup
in the _Amazon ElastiCache API Reference_. 3. If you used `ApplyImmediately``=true`,
monitor the status of the replication group using the ElastiCache API
`DescribeReplicationGroups` action with the following parameters.
When the status changes from _modifying_
to _available_, you can begin writing to your
new, scaled down replication group.

    * `ReplicationGroupId` – the name of the replication group.
     Use this parameter to describe a particular replication group rather than all
     replication groups.

```
https://elasticache.us-west-2.amazonaws.com/
	   ?Action=DescribeReplicationGroups
	   &ReplicationGroupId=MyReplGroup
	   &Version=2015-02-02
	   &SignatureVersion=4
	   &SignatureMethod=HmacSHA256
	   &Timestamp=20150202T192317Z
	   &X-Amz-Credential=<credential>
```

For more information, see DescribeReplicationGroups
in the _Amazon ElastiCache API Reference_.

## Increasing read capacity

To increase read capacity, add read replicas (up to a maximum
of five) to your Valkey or Redis OSS replication group.

You can scale your Valkey or Redis OSS cluster’s read capacity using the ElastiCache console, the AWS CLI, or the ElastiCache API.
For more information, see [Adding a read replica for Valkey or Redis OSS (Cluster Mode Disabled)](Replication.md "Replication.md").

## Decreasing read capacity

To decrease read capacity, delete one or more read replicas from your Valkey or Redis OSS cluster with replicas
(called _replication group_ in the API/CLI).
If the cluster is Multi-AZ with automatic failover enabled, you cannot delete
the last read replica without first disabling Multi-AZ.
For more information, see [Modifying a replication group](Replication.md "Replication.md").

For more information, see [Deleting a read replica for Valkey or Redis OSS (Cluster Mode Disabled)](Replication.md "Replication.md").
