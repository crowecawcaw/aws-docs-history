# Creating a cluster for Valkey or Redis OSS

The following examples show how to create a Valkey or Redis OSS cluster using the AWS Management Console, AWS CLI and ElastiCache API.

ElastiCache supports replication when you use the Valkey or Redis OSS engine. To monitor the latency between
when data is written to a Valkey or Redis OSS read/write primary cluster and when it is propagated
to a read-only secondary cluster, ElastiCache adds to the cluster a special key,
`ElastiCacheMasterReplicationTimestamp`. This key is the current
Universal Universal Time (UTC) time. Because a Valkey or Redis OSS cluster might be added to a
replication group at a later time, this key is included in all Valkey or Redis OSS clusters, even
if initially they are not members of a replication group. For more information on
replication groups, see [High availability using replication groups](Replication.md "Replication.md").

To create a Valkey or Redis OSS (cluster mode disabled) cluster, follow the steps at [Creating a Valkey (cluster mode disabled) cluster (Console)](SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs "SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs").

As soon as your cluster's status is _available_, you can grant Amazon EC2 access to it, connect to it, and begin using it.
For more information, see [Step 3. Authorize access to the cluster](SubnetGroups.designing-cluster-pre.md#GettingStarted.AuthorizeAccess.valkey "SubnetGroups.designing-cluster-pre.md#GettingStarted.AuthorizeAccess.valkey")
and [Step 4. Connect to the cluster's node](SubnetGroups.designing-cluster-pre.md#GettingStarted.ConnectToCacheNode.valkey "SubnetGroups.designing-cluster-pre.md#GettingStarted.ConnectToCacheNode.valkey").

###### Important

As soon as your cluster becomes available,
you're billed for each hour or partial hour that the cluster is active,
even if you're not actively using it.
To stop incurring charges for this cluster, you must delete it. See [Deleting a cluster in ElastiCache](Clusters.md "Clusters.md").

If you are running Redis OSS 3.2.4 or later, you can create a Valkey or Redis OSS (cluster mode enabled) cluster.
Valkey or Redis OSS (cluster mode enabled) clusters support partitioning your data across 1 to 500
shards (API/CLI: node groups) but with some limitations. For a comparison of
Valkey or Redis OSS (cluster mode disabled) and Valkey or Redis OSS (cluster mode enabled), see [Supported engines and versions](VersionManagement.md#supported-engine-versions "VersionManagement.md#supported-engine-versions").

###### To create a Valkey or Redis OSS (cluster mode enabled) cluster using the ElastiCache console

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the list in the upper-right corner, choose the AWS Region that you want to launch
   this cluster in.
3. Choose **Get started** from the navigation pane.
4. Choose **Create VPC** and follow the steps outlined at
   [Creating a Virtual Private Cloud (VPC)](VPCs.md "VPCs.md").
5. On the ElastiCache dashboard page, choose **Create cluster** and then choose **Create Valkey cluster** or **Create Redis OSS cluster**.
6. Under **Cluster settings**, do the following:
   1. Choose **Configure and create a new cluster**.
   2. For **Cluster mode**, choose **Enabled**.
   3. For **Cluster info** enter a value for **Name**.
   4. (Optional) Enter a value for **Description**.

7. Under **Location**:

AWS Cloud

    1. For **AWS Cloud**, we recommend you accept the default settings for **Multi-AZ** and **Auto-failover**. For
     more information, see [Minimizing downtime in ElastiCache for Redis OSS with Multi-AZ](AutoFailover.md "AutoFailover.md").
    2. Under **Cluster settings**


    	1. For **Engine version**, choose an available version.
    	2. For **Port**, use the default port, 6379. If you have a reason to use
    	 a different port, enter the port number.
    	3. For **Parameter group**, choose a parameter group or create a new one.


    	 Parameter groups control the runtime parameters of your cluster.
    	 For more information on parameter groups,
    	 see [Valkey and Redis OSS parameters](ParameterGroups.md#ParameterGroups.Redis "ParameterGroups.md#ParameterGroups.Redis")
    	 and [Creating an ElastiCache parameter group](ParameterGroups.md "ParameterGroups.md").


    	###### Note

    	When
    	 you select a parameter group to set the engine configuration values, that
    	 parameter group is applied to all clusters in the global datastore. On the
    	 **Parameter Groups** page, the yes/no
    	 **Global** attribute indicates whether a parameter group is
    	 part of a global datastore.
    	4. For **Node type**, choose the down arrow (
    	![Downward-pointing triangle icon, typically used to indicate a dropdown menu.](images/ElastiCache-DnArrow.png)
    	). In the **Change node type**
    	 dialog box, choose a value for **Instance family**
    	 for the node type that you want. Then choose the node type that you
    	 want to use for this cluster, and then choose
    	 **Save**.


    	For more information, see [Choosing your node size](CacheNodes.md "CacheNodes.md").


    	If you choose an r6gd node type, data-tiering is automatically enabled. For more information, see [Data tiering in ElastiCache](data-tiering.md "data-tiering.md").
    	5. For **Number of shards**, choose the number of shards (partitions/node
    	 groups) that you want for this Valkey or Redis OSS (cluster mode enabled) cluster.


    	For some versions of Valkey or Redis OSS (cluster mode enabled), you can change the number of shards in your
    	 cluster dynamically:




    		* **Redis OSS 3.2.10 and later** – If your cluster is
    		 running Redis OSS 3.2.10 or later versions, you can change the
    		 number of shards in your cluster dynamically. For more
    		 information, see [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md "scaling-redis-cluster-mode-enabled.md").
    		* **Other Redis OSS versions** – If your cluster is
    		 running a version of Redis OSS before version 3.2.10,
    		 there's another approach. To change the number of
    		 shards in your cluster in this case, create a new cluster
    		 with the new number of shards. For more information, see
    		 [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md").
    	6. For **Replicas per shard**, choose the number of read replica nodes
    	 that you want in each shard.



    	The following restrictions exist for Valkey or Redis OSS (cluster mode enabled).



    		* If you have Multi-AZ enabled, make sure that you have at least one replica per
    		 shard.
    		* The number of replicas is the same for each shard when creating the cluster using the console.
    		* The number of read replicas per shard is fixed and cannot be changed.
    		 If you find you need more or fewer replicas per shard (API/CLI: node group),
    		 you must create a new cluster with the new number of replicas.
    		 For more information, see [Tutorial: Seeding a new node-based cluster with an externally created backup](backups-seeding-redis.md "backups-seeding-redis.md").
    3. Under **Connectivity**


    	1. For **Network type**, choose the IP version(s) this cluster will support.
    	2. For **Subnet groups**, choose the subnet that you want to apply to this
    	 cluster. ElastiCache uses that subnet group to choose a subnet and IP addresses within that subnet to associate with your nodes. ElastiCache clusters require a dual-stack subnet with both IPv4 and IPv6 addresses assigned to them to operate in dual-stack mode and an IPv6-only subnet to operate as IPv6-only.


    	When creating a new subnet group, enter the **VPC ID** to which it belongs.


    	Select a **Discovery IP type**. Only the IP adresses of your chosen protocol are returned.


    	For more information, see:




    		* [Choosing a network type in ElastiCache](network-type.md "network-type.md").
    		* [Create a subnet in your VPC](../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet "../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet").
    	If you are [Using local zones with ElastiCache](Local_zones.md "Local_zones.md"), you must create
    	 or choose a subnet that is in the local zone.


    	For more information, see [Subnets and subnet groups](SubnetGroups.md "SubnetGroups.md").
    4. For **Availability zone placements**, you have two options:




    	* **No preference** – ElastiCache chooses the Availability Zone.
    	* **Specify availability zones** – You specify the Availability Zone for
    	 each cluster.


    	If you chose to specify the Availability Zones, for each cluster in each shard,
    	 choose the Availability Zone from the list.
    For more information, see [Choosing regions and availability zones for ElastiCache](RegionsAndAZs.md "RegionsAndAZs.md").
    5. Choose **Next**
    6. Under **Advanced Valkey settings** or **Advanced Redis OSS settings** or


    	1. For **Security**:


    		1. To encrypt your data, you have the following options:




    			* **Encryption at rest** – Enables encryption of data stored
    			 on disk. For more information, see [Encryption at Rest](at-rest-encryption.md "at-rest-encryption.md").


    			###### Note

    			You have the option to supply a different encryption key by choosing **Customer
    			 Managed AWS KMS key** and choosing
    			 the key. For more information, see [Using customer managed keys from AWS
    			 KMS](at-rest-encryption.md#using-customer-managed-keys-for-elasticache-security "at-rest-encryption.md#using-customer-managed-keys-for-elasticache-security").
    			* **Encryption in-transit** – Enables encryption of data on the wire.
    			 For more information, see [encryption in transit](in-transit-encryption.md "in-transit-encryption.md"). For Valkey 7.2 and above or Redis OSS 6.0 and above, if you enable Encryption in-transit
    			 you will be prompted to specify one of the following **Access Control** options:




    				+ **No Access Control** – This is the default setting. This indicates no restrictions on user access to the cluster.
    				+ **User Group Access Control List** – Select a user group with a defined set of users that can access the cluster.
    				 For more information, see [Managing User Groups with the Console and CLI](Clusters.md#User-Groups "Clusters.md#User-Groups").
    				+ **AUTH Default User** – An authentication
    				 mechanism for a Valkey or Redis OSS server. For more information, see [AUTH](auth.md "auth.md").
    			* **AUTH** – An authentication
    			 mechanism for Valkey or Redis OSS server. For more information, see [AUTH](auth.md "auth.md").
    		###### Note

    		For Redis OSS versions between 3.2.6 onward, excluding version 3.2.10, AUTH is the sole option.
    		2. For **Security groups**, choose the security groups that you want for
    		 this cluster. A *security group*
    		 acts as a firewall to control network access to your cluster. You
    		 can use the default security group for your VPC or create a new
    		 one.


    		For more information on security groups, see [Security groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the
    		 *Amazon VPC User Guide.*
    7. For regularly scheduled automatic backups, select **Enable automatic
     backups** and then enter the number of days that you
     want each automatic backup retained before it is automatically
     deleted. If you don't want regularly scheduled automatic backups,
     clear the **Enable automatic backups** check box.
     In either case, you always have the option to create manual
     backups.


    For more information on backup and restore, see [Snapshot and restore](backups.md "backups.md").
    8. (Optional) Specify a maintenance window. The *maintenance window* is
     the time, generally an hour in length, each week when ElastiCache
     schedules system maintenance for your cluster. You can allow ElastiCache
     to choose the day and time for your maintenance window (*No
     preference*), or you can choose the day, time, and
     duration yourself (*Specify maintenance window*).
     If you choose *Specify maintenance window* from
     the lists, choose the *Start day*,
     *Start time*, and
     *Duration* (in hours) for your maintenance
     window. All times are UCT times.


    For more information, see [Managing ElastiCache cluster maintenance](maintenance-window.md "maintenance-window.md").
    9. (Optional) For **Logs**:




    	* Under **Log format**, choose either **Text** or **JSON**.
    	* Under **Destination Type**, choose either **CloudWatch Logs** or **Kinesis Firehose**.
    	* Under **Log destination**, choose either **Create new** and enter either your CloudWatch Logs log group name or your Firehose stream name, or
    	 choose **Select existing** and then choose either your CloudWatch Logs log group name or your Firehose stream name,
    10. For **Tags**, to help you manage your clusters and other ElastiCache resources, you can assign your own metadata to each
     resource in the form of tags. For mor information, see [Tagging your ElastiCache resources](Tagging-Resources.md "Tagging-Resources.md").
    11. Choose **Next**.
    12. Review all your entries and choices, then make any needed corrections. When you're ready,
     choose **Create**.

On premises

    1. For **On premises**, we recommend you leave **Auto-failover** enabled.
     For more information, see [Minimizing downtime in ElastiCache for Redis OSS with Multi-AZ](AutoFailover.md "AutoFailover.md")
    2. Follow the steps at [Using Outposts](ElastiCache-Outposts.md "ElastiCache-Outposts.md").

To create the equivalent using the ElastiCache API or AWS CLI instead of the ElastiCache console, see the following:

- API: [CreateReplicationGroup](../APIReference/API_CreateReplicationGroup.md "../APIReference/API_CreateReplicationGroup.md")
- CLI: [create-replication-group](../../../cli/latest/reference/elasticache/create-replication-group.md "../../../cli/latest/reference/elasticache/create-replication-group.md")
  As soon as your cluster's status is _available_, you can grant EC2 access to it, connect to it, and begin using it.
  For more information, see [Step 3. Authorize access to the cluster](SubnetGroups.designing-cluster-pre.md#GettingStarted.AuthorizeAccess.valkey "SubnetGroups.designing-cluster-pre.md#GettingStarted.AuthorizeAccess.valkey")
  and [Step 4. Connect to the cluster's node](SubnetGroups.designing-cluster-pre.md#GettingStarted.ConnectToCacheNode.valkey "SubnetGroups.designing-cluster-pre.md#GettingStarted.ConnectToCacheNode.valkey").

###### Important

As soon as your cluster becomes available,
you're billed for each hour or partial hour that the cluster is active,
even if you're not actively using it.
To stop incurring charges for this cluster, you must delete it. See [Deleting a cluster in ElastiCache](Clusters.md "Clusters.md").

To create a cluster using the AWS CLI, use the `create-cache-cluster` command.

###### Important

As soon as your cluster becomes available,
you're billed for each hour or partial hour that the cluster is active,
even if you're not actively using it.
To stop incurring charges for this cluster, you must delete it. See [Deleting a cluster in ElastiCache](Clusters.md "Clusters.md").

### Creating a Valkey or Redis OSS (cluster mode disabled) cluster (CLI)

###### Example – A Valkey or Redis OSS (cluster mode disabled) Cluster with no read replicas

The following CLI code creates a Valkey or Redis OSS (cluster mode disabled) cluster with no replicas.

###### Note

When creating cluster using a node type from the r6gd family, you must pass the `data-tiering-enabled` parameter.

For Linux, macOS, or Unix:

```
aws elasticache create-cache-cluster \
--cache-cluster-id `my-cluster` \
--cache-node-type `cache.r4.large` \
--engine `redis` \
--num-cache-nodes `1` \
--cache-parameter-group `default.redis6.x` \
--snapshot-arns `arn:aws:s3:::amzn-s3-demo-bucket/snapshot.rdb`
```

For Windows:

```
aws elasticache create-cache-cluster ^
--cache-cluster-id `my-cluster` ^
--cache-node-type `cache.r4.large` ^
--engine `redis` ^
--num-cache-nodes `1` ^
--cache-parameter-group `default.redis6.x` ^
--snapshot-arns `arn:aws:s3:::amzn-s3-demo-bucket/snapshot.rdb`
```

### Creating a Valkey or Redis OSS (cluster mode enabled) cluster (AWS CLI)

Valkey or Redis OSS (cluster mode enabled) clusters (API/CLI: replication groups) cannot be created using the
`create-cache-cluster` operation.
To create a Valkey or Redis OSS (cluster mode enabled) cluster (API/CLI: replication group), see [Creating a Valkey or Redis OSS (Cluster Mode Enabled) replication group from scratch (AWS CLI)](Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.CLI "Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.CLI").

For more information, see the AWS CLI for ElastiCache reference topic [`create-replication-group`](../../../cli/latest/reference/elasticache/create-replication-group.md "../../../cli/latest/reference/elasticache/create-replication-group.md").

To create a cluster using the ElastiCache API, use the `CreateCacheCluster` action.

###### Important

As soon as your cluster becomes available,
you're billed for each hour or partial hour that the cluster is active,
even if you're not using it.
To stop incurring charges for this cluster, you must delete it. See [Deleting a cluster in ElastiCache](Clusters.md "Clusters.md").

###### Topics

- [Creating a Valkey or Redis OSS (cluster mode disabled) cluster (ElastiCache API)](#Clusters.Create.API.Redis "#Clusters.Create.API.Redis")
- [Creating a cluster in Valkey or Redis OSS (cluster mode enabled) (ElastiCache API)](#Clusters.Create.API.RedisCluster "#Clusters.Create.API.RedisCluster")

### Creating a Valkey or Redis OSS (cluster mode disabled) cluster (ElastiCache API)

The following code creates a Valkey or Redis OSS (cluster mode disabled) cluster (ElastiCache API).

Line breaks are added for ease of reading.

```
https://elasticache.us-west-2.amazonaws.com/
    ?Action=CreateCacheCluster
    &CacheClusterId=my-cluster
    &CacheNodeType=cache.r4.large
    &CacheParameterGroup=default.redis3.2
    &Engine=redis
    &EngineVersion=3.2.4
    &NumCacheNodes=1
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &SnapshotArns.member.1=arn%3Aaws%3As3%3A%3A%3AmyS3Bucket%2Fdump.rdb
    &Timestamp=20150508T220302Z
    &Version=2015-02-02
    &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
    &X-Amz-Credential=<credential>
    &X-Amz-Date=20150508T220302Z
    &X-Amz-Expires=20150508T220302Z
    &X-Amz-SignedHeaders=Host
    &X-Amz-Signature=<signature>
```

### Creating a cluster in Valkey or Redis OSS (cluster mode enabled) (ElastiCache API)

Valkey or Redis OSS (cluster mode enabled) clusters (API/CLI: replication groups) cannot be created using the
`CreateCacheCluster` operation.
To create a Valkey or Redis OSS (cluster mode enabled) cluster (API/CLI: replication group), see [Creating a replication group in Valkey or Redis OSS (Cluster Mode Enabled) from scratch (ElastiCache API)](Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.API "Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.API").

For more information, see the ElastiCache API reference topic [`CreateReplicationGroup`](../APIReference/API_CreateReplicationGroup.md "../APIReference/API_CreateReplicationGroup.md").
