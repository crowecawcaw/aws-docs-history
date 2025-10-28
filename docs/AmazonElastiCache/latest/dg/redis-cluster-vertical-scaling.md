# Online vertical scaling by modifying node type

By using online vertical scaling with Valkey version 7.2 or newer, or Redis OSS version 3.2.10 or newer, you can scale
your Valkey or Redis OSS clusters dynamically with minimal downtime. This allows your Valkey or Redis OSS cluster
to serve requests even while scaling.

###### Note

Scaling is not supported between a data tiering cluster (for example, a cluster using an r6gd node type) and a cluster that does not use data tiering (for example, a cluster using an r6g node type). For more information, see [Data tiering in ElastiCache](data-tiering.md "data-tiering.md").

You can do the following:

- **Scale up** –
  Increase read and write capacity by adjusting the node type of your Valkey or Redis OSS cluster to use a larger node type.

ElastiCache dynamically resizes your cluster while remaining online and serving requests.

- **Scale down** –
  Reduce read and write capacity by adjusting the node type down to use a smaller node. Again, ElastiCache dynamically resizes your cluster while remaining online and serving requests. In this case,
  you reduce costs by downsizing the node.

###### Note

The scale up and scale down processes rely on creating clusters with newly selected node types and synchronizing the new nodes with the previous ones. To ensure a smooth scale up/down flow,
do the following:

- Ensure you have sufficient ENI (Elastic Network Interface) capacity. If scaling down, ensure the smaller node has sufficient memory to absorb expected traffic.

For best practices on memory management, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md "redis-memory-management.md").

- While the vertical scaling process is designed to remain fully online, it does rely on synchronizing data between the old node and the new node. We recommend that you initiate scale up/down
  during hours when you expect data traffic to be at its minimum.
- Test your application behavior during scaling in a staging environment, if possible.

###### Contents

- [Online scaling up](redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-scaling-up "redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-scaling-up")
  - [Scaling up Valkey or Redis OSS clusters (Console)](redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-console "redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-console")
  - [Scaling up Valkey or Redis OSS clusters (AWS CLI)](redis-cluster-vertical-scaling.md#Scaling.RedisStandalone.ScaleUp.CLI "redis-cluster-vertical-scaling.md#Scaling.RedisStandalone.ScaleUp.CLI")
  - [Scaling up Valkey or Redis OSS clusters (ElastiCache API)](redis-cluster-vertical-scaling.md#VeticalScaling.RedisReplGrps.ScaleUp.API "redis-cluster-vertical-scaling.md#VeticalScaling.RedisReplGrps.ScaleUp.API")

- [Online scaling down](redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-scaling-down "redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-scaling-down")
  - [Scaling down Valkey or Redis OSS clusters (Console)](redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-down-console "redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-down-console")
  - [Scaling down Valkey or Redis OSS clusters (AWS CLI)](redis-cluster-vertical-scaling.md#Scaling.RedisStandalone.ScaleDown.CLI "redis-cluster-vertical-scaling.md#Scaling.RedisStandalone.ScaleDown.CLI")
  - [Scaling down Valkey or Redis OSS clusters (ElastiCache API)](redis-cluster-vertical-scaling.md#Scaling.Vertical.ScaleDown.API "redis-cluster-vertical-scaling.md#Scaling.Vertical.ScaleDown.API")

## Online scaling up

###### Topics

- [Scaling up Valkey or Redis OSS clusters (Console)](#redis-cluster-vertical-scaling-console "#redis-cluster-vertical-scaling-console")
- [Scaling up Valkey or Redis OSS clusters (AWS CLI)](#Scaling.RedisStandalone.ScaleUp.CLI "#Scaling.RedisStandalone.ScaleUp.CLI")
- [Scaling up Valkey or Redis OSS clusters (ElastiCache API)](#VeticalScaling.RedisReplGrps.ScaleUp.API "#VeticalScaling.RedisReplGrps.ScaleUp.API")

### Scaling up Valkey or Redis OSS clusters (Console)

The following procedure describes how to scale up a Valkey or Redis OSS cluster using the ElastiCache Management Console. During this process, your cluster will continue to serve requests with minimal downtime.

###### To scale up a Valkey or Redis OSS cluster (console)

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the navigation pane, choose **Valkey clusters** or **Redis OSS clusters**.
3. From the list of clusters, choose the cluster.
4. Choose **Modify**.
5. In the **Modify Cluster** wizard:
   1. Choose the node type you want to scale to from the **Node type** list. To scale up, select a node type larger than your existing node.

6. If you want to perform the scale-up process right away, choose the **Apply immediately**
   box. If the **Apply immediately** box is not chosen, the scale-up process
   is performed during this cluster's next maintenance window.
7. Choose **Modify**.

If you chose **Apply immediately** in the previous step,
the cluster's status changes to _modifying_.
When the status changes to _available_, the modification is complete
and you can begin using the new cluster.

### Scaling up Valkey or Redis OSS clusters (AWS CLI)

The following procedure describes how to scale up a Valkey or Redis OSS cluster using the AWS CLI. During this process, your cluster will continue to serve requests with minimal downtime.

###### To scale up a Valkey or Redis OSS cluster (AWS CLI)

1. Determine the node types you can scale up to by running the AWS CLI
   `list-allowed-node-type-modifications` command with the following parameter.

For Linux, macOS, or Unix:

```
aws elasticache list-allowed-node-type-modifications \
	    --replication-group-id `my-replication-group-id`
```

For Windows:

```
aws elasticache list-allowed-node-type-modifications ^
	    --replication-group-id `my-replication-group-id`
```

Output from the above command looks something like this (JSON format).

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
	       "ScaleDownModifications": [
	        "cache.t2.micro",
	        "cache.t2.small ",
	        "cache.t2.medium",
	       	"cache.t1.small "
	    ],
}
```

For more information, see list-allowed-node-type-modifications
in the _AWS CLI Reference_. 2. Modify your replication group to scale up to the new, larger node type, using the AWS CLI `modify-replication-group` command
and the following parameters.

    * `--replication-group-id` –
     The name of the replication group you are scaling up to.
    * `--cache-node-type` –
     The new node type you want to scale the cluster.
     This value must be one of the node types returned by the
     `list-allowed-node-type-modifications` command in step 1.
    * `--cache-parameter-group-name` –
     [Optional] Use this parameter if you are using `reserved-memory` to manage your
     cluster's reserved memory.
     Specify a custom cache parameter group that reserves the correct amount of memory for your new
     node type.
     If you are using `reserved-memory-percent` you can omit this parameter.
    * `--apply-immediately` – Causes the scale-up process to be applied
     immediately. To postpone the scale-up process to the cluster's next maintenance window, use the
     `--no-apply-immediately` parameter.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group  \
	    --replication-group-id `my-redis-cluster` \
	    --cache-node-type `cache.m3.xlarge` \
	    --apply-immediately
```

For Windows:

```
aws elasticache modify-replication-group ^
	    --replication-group-id `my-redis-cluster` ^
	    --cache-node-type `cache.m3.xlarge` ^
	    --apply-immediately
```

Output from the above command looks something like this (JSON format).

```

{
		"ReplicationGroup": {
        "Status": "modifying",
        "Description": "my-redis-cluster",
        "NodeGroups": [
            {
                "Status": "modifying",
                "Slots": "0-16383",
                "NodeGroupId": "0001",
                "NodeGroupMembers": [
                    {
                        "PreferredAvailabilityZone": "us-east-1f",
                        "CacheNodeId": "0001",
                        "CacheClusterId": "my-redis-cluster-0001-001"
                    },
                    {
                        "PreferredAvailabilityZone": "us-east-1d",
                        "CacheNodeId": "0001",
                        "CacheClusterId": "my-redis-cluster-0001-002"
                    }
                ]
            }
        ],
        "ConfigurationEndpoint": {
            "Port": 6379,
            "Address": "my-redis-cluster.r7gdfi.clustercfg.use1.cache.amazonaws.com"
        },
        "ClusterEnabled": true,
        "ReplicationGroupId": "my-redis-cluster",
        "SnapshotRetentionLimit": 1,
        "AutomaticFailover": "enabled",
        "SnapshotWindow": "07:30-08:30",
        "MemberClusters": [
            "my-redis-cluster-0001-001",
            "my-redis-cluster-0001-002"
        ],
        "CacheNodeType": "cache.m3.xlarge",
         "DataTiering": "disabled"
        "PendingModifiedValues": {}
    }
}
```

For more information, see modify-replication-group
in the _AWS CLI Reference_. 3. If you used the `--apply-immediately`,
check the status of the cluster using the AWS CLI `describe-cache-clusters` command with the following parameter.
When the status changes to _available_, you can begin using the new, larger cluster node.

### Scaling up Valkey or Redis OSS clusters (ElastiCache API)

The following process scales your cluster from its current node type to a new,
larger node type using the ElastiCache API.

During this process, ElastiCache updates the DNS entries so they point to the new nodes. Because of this you don't have to update the endpoints in your application. For Valkey 7.2 and above Redis OSS 5.0.5 and above, you can scale auto failover enabled clusters while the cluster continues to stay online and serve incoming requests. On version Redis OSS 4.0.10 and below, you may notice a brief interruption of reads and writes on previous versions from the primary node while the DNS entry is updated..

The amount of time it takes to scale up to a larger node type varies,
depending upon your node type and the amount of data in your current cluster.

###### To scale up a Valkey or Redis OSS Cache Cluster (ElastiCache API)

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
     action in the previous step.
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

## Online scaling down

###### Topics

- [Scaling down Valkey or Redis OSS clusters (Console)](#redis-cluster-vertical-scaling-down-console "#redis-cluster-vertical-scaling-down-console")
- [Scaling down Valkey or Redis OSS clusters (AWS CLI)](#Scaling.RedisStandalone.ScaleDown.CLI "#Scaling.RedisStandalone.ScaleDown.CLI")
- [Scaling down Valkey or Redis OSS clusters (ElastiCache API)](#Scaling.Vertical.ScaleDown.API "#Scaling.Vertical.ScaleDown.API")

### Scaling down Valkey or Redis OSS clusters (Console)

The following procedure describes how to scale down a Valkey or Redis OSS cluster using the ElastiCache Management Console. During this process, your Valkey or Redis OSS cluster will
continue to serve requests with minimal downtime.

###### To scale Down a Valkey or Redis OSS cluster (console)

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the navigation pane, choose **Valkey clusters** or **Redis OSS clusters**.
3. From the list of clusters, choose your preferred cluster.
4. Choose **Modify**.
5. In the **Modify Cluster** wizard:
   1. Choose the node type you want to scale to from the **Node type** list.
      To scale down, select a node type smaller than your existing node. Note that not all node types are available to scale down to.

6. If you want to perform the scale down process right away, choose the **Apply immediately**
   box. If the **Apply immediately** box is not chosen, the scale-down process
   is performed during this cluster's next maintenance window.
7. Choose **Modify**.

If you chose **Apply immediately** in the previous step,
the cluster's status changes to _modifying_.
When the status changes to _available_, the modification is complete
and you can begin using the new cluster.

### Scaling down Valkey or Redis OSS clusters (AWS CLI)

The following procedure describes how to scale down a Valkey or Redis OSS cluster using the AWS CLI. During this process, your cluster will
continue to serve requests with minimal downtime.

###### To scale down a Valkey or Redis OSS cluster (AWS CLI)

1. Determine the node types you can scale down to by running the AWS CLI
   `list-allowed-node-type-modifications` command with the following parameter.

For Linux, macOS, or Unix:

```
aws elasticache list-allowed-node-type-modifications \
	    --replication-group-id `my-replication-group-id`
```

For Windows:

```
aws elasticache list-allowed-node-type-modifications ^
	    --replication-group-id `my-replication-group-id`
```

Output from the above command looks something like this (JSON format).

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

	       "ScaleDownModifications": [
	        "cache.t2.micro",
	        "cache.t2.small ",
	        "cache.t2.medium ",
  	      "cache.t1.small"
	    ]
}
```

For more information, see list-allowed-node-type-modifications
in the _AWS CLI Reference_. 2. Modify your replication group to scale down to the new, smaller
node type, using the AWS CLI `modify-replication-group` command
and the following parameters.

    * `--replication-group-id` –
     The name of the replication group you are scaling down to.
    * `--cache-node-type` –
     The new node type you want to scale the cluster.
     This value must be one of the node types returned by the
     `list-allowed-node-type-modifications` command in step 1.
    * `--cache-parameter-group-name` –
     [Optional] Use this parameter if you are using `reserved-memory` to manage your
     cluster's reserved memory.
     Specify a custom cache parameter group that reserves the correct amount of memory for your new
     node type.
     If you are using `reserved-memory-percent` you can omit this parameter.
    * `--apply-immediately` – Causes the scale-up process to be applied
     immediately. To postpone the scale-down process to the cluster's next maintenance window, use the
     `--no-apply-immediately` parameter.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group  \
	    --replication-group-id `my-redis-cluster` \
	    --cache-node-type `cache.t2.micro` \
	    --apply-immediately
```

For Windows:

```
aws elasticache modify-replication-group ^
	    --replication-group-id `my-redis-cluster` ^
	    --cache-node-type `cache.t2.micro` ^
	    --apply-immediately
```

Output from the above command looks something like this (JSON format).

```

{
		"ReplicationGroup": {
        "Status": "modifying",
        "Description": "my-redis-cluster",
        "NodeGroups": [
            {
                "Status": "modifying",
                "Slots": "0-16383",
                "NodeGroupId": "0001",
                "NodeGroupMembers": [
                    {
                        "PreferredAvailabilityZone": "us-east-1f",
                        "CacheNodeId": "0001",
                        "CacheClusterId": "my-redis-cluster-0001-001"
                    },
                    {
                        "PreferredAvailabilityZone": "us-east-1d",
                        "CacheNodeId": "0001",
                        "CacheClusterId": "my-redis-cluster-0001-002"
                    }
                ]
            }
        ],
        "ConfigurationEndpoint": {
            "Port": 6379,
            "Address": "my-redis-cluster.r7gdfi.clustercfg.use1.cache.amazonaws.com"
        },
        "ClusterEnabled": true,
        "ReplicationGroupId": "my-redis-cluster",
        "SnapshotRetentionLimit": 1,
        "AutomaticFailover": "enabled",
        "SnapshotWindow": "07:30-08:30",
        "MemberClusters": [
            "my-redis-cluster-0001-001",
            "my-redis-cluster-0001-002"
        ],
        "CacheNodeType": "cache.t2.micro",
         "DataTiering": "disabled"
        "PendingModifiedValues": {}
    }
}
```

For more information, see modify-replication-group
in the _AWS CLI Reference_. 3. If you used the `--apply-immediately`,
check the status of the cluster using the AWS CLI `describe-cache-clusters` command with the following parameter.
When the status changes to _available_, you can begin using the new, smaller cluster node.

### Scaling down Valkey or Redis OSS clusters (ElastiCache API)

The following process scales your replication group from its current node type to a new,
smaller node type using the ElastiCache API. During this process, your Valkey or Redis OSS cluster will
continue to serve requests with minimal downtime.

The amount of time it takes to scale down to a smaller node type varies,
depending upon your node type and the amount of data in your current cluster.

###### Scaling down (ElastiCache API)

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
in the _Amazon ElastiCache API Reference_. 2. Scale your current replication group down to the new node type using the
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
     the scale-down process to be applied immediately. To postpone the scale-down process to the next maintenance window, use
     `ApplyImmediately``=false`.

```
https://elasticache.us-west-2.amazonaws.com/
	   ?Action=ModifyReplicationGroup
	   &ApplyImmediately=true
	   &CacheNodeType=cache.t2.micro
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
in the _Amazon ElastiCache API Reference_.
