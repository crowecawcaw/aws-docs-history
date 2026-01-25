# Finding connection endpoints in ElastiCache

Your application connects to your ElastiCache cluster using endpoints.
An endpoint is a node or cluster's unique address.

You can also establish a private connection between your VPC and ElastiCache API endpoints by creating an interface VPC endpoint through AWS PrivateLink. For more information, see [ElastiCache API and interface VPC endpoints
(AWS PrivateLink)](elasticache-privatelink.md "elasticache-privatelink.md").

**Which endpoints to use with Valkey or Redis OSS.**

- For a **standalone node**,
  use the node's endpoint for both read and write operations.
- For **Valkey or Valkey or Redis OSS (cluster mode disabled) clusters**,
  use the _Primary Endpoint_ for all write operations. Use the _Reader Endpoint_ to evenly split incoming connections to the endpoint between all read replicas.
  Use the individual _Node Endpoints_ for read operations (In the
  API/CLI these are referred to as Read Endpoints).
- For **Valkey or Redis OSS (cluster mode enabled) clusters**,
  use the cluster's _Configuration Endpoint_ for all operations that support cluster mode enabled commands.
  You must use a client that supports either Valkey Cluster, or Redis OSS Cluster on Redis OSS 3.2 and above.
  You can still read from individual node endpoints (In the API/CLI these are referred
  to as Read Endpoints).
  The following sections guide you through discovering the endpoints you'll need for the engine you're
  running.

**Which endpoints to use with Memcached.**

For **ElastiCache serverless cache for Memcached**,
simply acquire the cluster endpoint DNS and port from the console.

From the AWS CLI, use the `describe-serverless-caches` command to acquire the Endpoint information.

Linux

```
aws elasticache describe-serverless-caches --serverless-cache-name CacheName
```

Windows

```
aws elasticache describe-serverless-caches --serverless-cache-name CacheName
```

The output from the above operation should look something like this (JSON format):

```
{
    "ServerlessCaches": [
        {
            "ServerlessCacheName": "serverless-memcached",
            "Description": "test",
            "CreateTime": 1697659642.136,
            "Status": "available",
            "Engine": "memcached",
            "MajorEngineVersion": "1.6",
            "FullEngineVersion": "21",
            "SecurityGroupIds": [
                "sg-083eda453e1e51310"
            ],
            "Endpoint": {
                "Address": "serverless-memcached-01.amazonaws.com",
                "Port":11211
            },
            "ARN": "<the ARN>",
            "SubnetIds": [
                "subnet-0cf759df15bd4dc65",
                "subnet-09e1307e8f1560d17"
            ],
            "SnapshotRetentionLimit": 0,
            "DailySnapshotTime": "03:00"
        }
    ]
}
```

For an **instance based Memcached cluster**, if you use
Automatic Discovery then you can use the cluster's _configuration endpoint_
to configure your Memcached client.
This means you must use a client that supports Automatic Discovery.

If you don't use Automatic Discovery, you must configure your client to use the individual node endpoints for
reads and writes. You must also keep track of them as you add and remove nodes.

If a Valkey or Valkey or Redis OSS (cluster mode disabled) cluster has only one node, the node's endpoint is used for both reads and writes.

If a Valkey or Valkey or Redis OSS (cluster mode disabled) cluster has multiple nodes, there are three types of endpoints; the _primary endpoint_, the _reader endpoint_ and
the _node endpoints_.

The primary endpoint is a DNS name that always resolves to the primary node in the cluster.
The primary endpoint is immune to changes to your cluster, such as promoting a read replica
to the primary role. For write activity, we recommend that your applications connect to the primary
endpoint.

A reader endpoint will evenly split incoming connections to the endpoint between all read replicas in a ElastiCache for Redis OSS cluster.
Additional factors such as when the application creates the connections or how the application (re)-uses the connections will determine the traffic distribution. Reader endpoints keep up with cluster changes in real-time as replicas are added or removed.
You can place your ElastiCache for Redis OSS cluster’s multiple read replicas in different AWS Availability Zones (AZ) to ensure high availability of reader endpoints.

###### Note

A reader endpoint is not a load balancer. It is a DNS record that will resolve to an IP address of one of the replica nodes in a round robin fashion.

For read activity, applications can also connect to any node in the cluster.
Unlike the primary endpoint, node endpoints resolve to specific endpoints.
If you make a change in your cluster, such as adding or deleting a replica,
you must update the node endpoints in your application.

###### To find a Valkey or Valkey or Redis OSS (cluster mode disabled) cluster's endpoints

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the navigation pane, choose **Valkey clusters** or **Redis OSS clusters**.

The clusters screen will appear with a list of Valkey or Valkey or Redis OSS (cluster mode disabled) and Valkey or Redis OSS (cluster mode enabled) clusters. 3. To find the cluster's Primary and/or Reader endpoints, choose the cluster's name (not the button to its left).

![Image: Primary endpoint for a Valkey or Valkey or Redis OSS (cluster mode disabled) cluster](/images/AmazonElastiCache/latest/dg/images/Reader-Endpoint.png)

_Primary and Reader endpoints for a Valkey or Valkey or Redis OSS (cluster mode disabled) cluster_

If there is only one node in the cluster, there is no primary endpoint and you can continue at the next step. 4. If the Valkey or Valkey or Redis OSS (cluster mode disabled) cluster has replica nodes,
you can find the cluster's replica node endpoints by choosing the cluster's
name and then choosing the **Nodes** tab.

The nodes screen appears with each node in the cluster, primary and replicas,
listed with its endpoint.

![Image: Node endpoints for a Valkey or Valkey or Redis OSS (cluster mode disabled) cluster](/images/AmazonElastiCache/latest/dg/images/ElastiCache-Endpoints-Redis-Node.png)

_Node endpoints for a Valkey or Valkey or Redis OSS (cluster mode disabled) cluster_ 5. To copy an endpoint to your clipboard:

    1. One endpoint at a time, find the endpoint you want to copy.
    2. Choose the copy icon directly in front of the endpoint.The endpoint is now copied to your clipboard. For information on using the endpoint to connect to a node, see

[Connecting to Memcached nodes](nodes-connecting.md#nodes-connecting.mem "nodes-connecting.md#nodes-connecting.mem").
A Valkey or Valkey or Redis OSS (cluster mode disabled) primary endpoint looks something like the following. There is a difference depending upon whether
or not In-Transit encryption is enabled.

**In-transit encryption not enabled**

```
`clusterName.xxxxxx`.`nodeId`.`regionAndAz`.cache.amazonaws.com:`port`

redis-01.7abc2d.0001.usw2.cache.amazonaws.com:6379
```

**In-transit encryption enabled**

```
master.`clusterName`.`xxxxxx`.`regionAndAz`.cache.amazonaws.com:`port`

master.ncit.ameaqx.use1.cache.amazonaws.com:6379
```

A Valkey or Redis OSS (cluster mode enabled) cluster has a single configuration endpoint. By connecting to the configuration endpoint, your application is able to discover the primary and read endpoints for each shard in the cluster.

###### To find a Valkey or Redis OSS (cluster mode enabled) cluster's endpoint

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the navigation pane, choose **Valkey clusters** or **Redis OSS clusters**.

The clusters screen will appear with a list of clusters. Choose the cluster you wish to connect to. 3. To find the cluster's Configuration endpoint, choose the cluster's name (not the radio button). 4. The **Configuration endpoint** is displayed under
**Cluster details**. To copy it, choose the _copy_ icon to the left of the endpoint.
All Memcached endpoints are read/write endpoints.
To connect to nodes in a Memcached cluster your application can use either the endpoints for each node,
or the cluster's configuration endpoint along with Automatic Discovery.
To use Automatic Discovery you must use a client that supports Automatic Discovery.

When using Automatic Discovery, your client application connects to your Memcached cluster using the
configuration endpoint. As you scale your cluster by adding or removing nodes, your application
will automatically "know" all the nodes in the cluster and be able to connect to any of
them. Without Automatic Discovery your application would have to do this, or you'd have to manually
update endpoints in your application each time you added or removed a node.

To copy an endpoint, choose the copy icon directly in front of the endpoint address. For information on using the endpoint to connect to a node,
see [Connecting to Memcached nodes](nodes-connecting.md#nodes-connecting.mem "nodes-connecting.md#nodes-connecting.mem").

Configuration and node endpoints look very similar.
The differences are highlighted with **bold** following.

```
`myclustername.xxxxxx`.**cfg**.usw2.cache.amazonaws.com:`port`   # configuration endpoint contains "cfg"
`myclustername.xxxxxx`.**0001**.usw2.cache.amazonaws.com:`port`  # node endpoint for node 0001
```

###### Important

If you choose to create a CNAME for your Memcached configuration endpoint,
in order for your automatic discovery client to recognize the CNAME as a configuration endpoint,
you must include `.cfg.` in the CNAME.

For Memcached, you can use the AWS CLI for Amazon ElastiCache to discover the endpoints for nodes and clusters.

For Redis OSS, you can use the AWS CLI for Amazon ElastiCache to discover the endpoints for nodes, clusters, and also
replication groups.

###### Topics

- [Finding Endpoints for Nodes and Clusters (AWS CLI)](#Endpoints.Find.CLI.Nodes "#Endpoints.Find.CLI.Nodes")
- [Finding the Endpoints for Valkey or Redis OSS Replication Groups (AWS CLI)](#Endpoints.Find.CLI.ReplGroups "#Endpoints.Find.CLI.ReplGroups")

### Finding Endpoints for Nodes and Clusters (AWS CLI)

You can use the AWS CLI to discover the endpoints for a cluster and its nodes with the
`describe-cache-clusters` command.
For Valkey or Redis OSS clusters, the command returns the cluster endpoint.
For Memcached clusters, the command returns the configuration endpoint.

If you include the optional parameter `--show-cache-node-info`,
the command will also return the endpoints of the individual nodes in the cluster.

The following command retrieves the configuration endpoint (`ConfigurationEndpoint`) and
individual node endpoints (`Endpoint`) for the Memcached cluster _mycluster_.

For Linux, macOS, or Unix:

```
aws elasticache describe-cache-clusters \
    --cache-cluster-id `mycluster` \
    --show-cache-node-info
```

For Windows:

```
aws elasticache describe-cache-clusters ^
    --cache-cluster-id `mycluster` ^
    --show-cache-node-info
```

Output from the above operation should look something like this (JSON format).

```
{
   "CacheClusters": [
   {
       "Engine": "memcached",
       "CacheNodes": [
          {
             "CacheNodeId": "0001",
             "Endpoint": {
                "Port": 11211,
                "Address": "mycluster.amazonaws.com"
             },
                "CacheNodeStatus": "available",
                "ParameterGroupStatus": "in-sync",
                "CacheNodeCreateTime": "2016-09-22T21:30:29.967Z",
                "CustomerAvailabilityZone": "us-west-2b"
          },
          {
             "CacheNodeId": "0002",
             "Endpoint": {
                "Port": 11211,
                "Address": "mycluster.amazonaws.com"
             },
                "CacheNodeStatus": "available",
                "ParameterGroupStatus": "in-sync",
                "CacheNodeCreateTime": "2016-09-22T21:30:29.967Z",
                "CustomerAvailabilityZone": "us-west-2b"
          },
          {
                "CacheNodeId": "0003",
                "Endpoint": {
                   "Port": 11211,
                   "Address": "mycluster.amazonaws.com"
                },
                   "CacheNodeStatus": "available",
                   "ParameterGroupStatus": "in-sync",
                   "CacheNodeCreateTime": "2016-09-22T21:30:29.967Z",
                   "CustomerAvailabilityZone": "us-west-2b"
          }
       ],
       "CacheParameterGroup": {
       "CacheNodeIdsToReboot": [],
       "CacheParameterGroupName": "default.memcached1.4",
       "ParameterApplyStatus": "in-sync"
            },
            "CacheClusterId": "mycluster",
            "PreferredAvailabilityZone": "us-west-2b",
            "ConfigurationEndpoint": {
                "Port": 11211,
                "Address": "mycluster.amazonaws.com"
            },
            "CacheSecurityGroups": [],
            "CacheClusterCreateTime": "2016-09-22T21:30:29.967Z",
            "AutoMinorVersionUpgrade": true,
            "CacheClusterStatus": "available",
            "NumCacheNodes": 3,
            "ClientDownloadLandingPage": "https://console.aws.amazon.com/elasticache/home#client-download:",
            "CacheSubnetGroupName": "default",
            "EngineVersion": "1.4.24",
            "PendingModifiedValues": {},
            "PreferredMaintenanceWindow": "mon:09:00-mon:10:00",
            "CacheNodeType": "cache.m4.large",
             "DataTiering": "disabled"
        }
    ]
}
```

###### Important

If you choose to create a CNAME for your Memcached configuration endpoint,
in order for your auto discovery client to recognize the CNAME as a configuration endpoint,
you must include `.cfg.` in the CNAME. For example, `mycluster`.cfg.`local`
in your php.ini file for the `session.save_path` parameter.

For Valkey and Redis OSS, the following command retrieves the cluster information for the single-node
cluster _mycluster_.

###### Important

The parameter `--cache-cluster-id` can be used with single-node
Valkey or Redis OSS (cluster mode disabled) cluster id or specific node ids in replication groups.
The `--cache-cluster-id` of a replication group is a 4-digit
value such as `0001`.

If `--cache-cluster-id` is the id of a cluster (node) in a replication group, the `replication-group-id` is included in the

output.

For Linux, macOS, or Unix:

```
aws elasticache describe-cache-clusters \
    --cache-cluster-id `redis-cluster` \
    --show-cache-node-info
```

For Windows:

```
aws elasticache describe-cache-clusters ^
    --cache-cluster-id `redis-cluster` ^
    --show-cache-node-info
```

Output from the above operation should look something like this (JSON format).

```
{
    "CacheClusters": [
        {
            "CacheClusterStatus": "available",
            "SecurityGroups": [
                {
                    "SecurityGroupId": "sg-77186e0d",
                    "Status": "active"
                }
            ],
            "CacheNodes": [
                {
                    "CustomerAvailabilityZone": "us-east-1b",
                    "CacheNodeCreateTime": "2018-04-25T18:19:28.241Z",
                    "CacheNodeStatus": "available",
                    "CacheNodeId": "0001",
                    "Endpoint": {
                        "Address": "redis-cluster.amazonaws.com",
                        "Port": 6379
                    },
                    "ParameterGroupStatus": "in-sync"
                }
            ],
            "AtRestEncryptionEnabled": false,
            "CacheClusterId": "redis-cluster",
            "TransitEncryptionEnabled": false,
            "CacheParameterGroup": {
                "ParameterApplyStatus": "in-sync",
                "CacheNodeIdsToReboot": [],
                "CacheParameterGroupName": "default.redis3.2"
            },
            "NumCacheNodes": 1,
            "PreferredAvailabilityZone": "us-east-1b",
            "AutoMinorVersionUpgrade": true,
            "Engine": "redis",
            "AuthTokenEnabled": false,
            "PendingModifiedValues": {},
            "PreferredMaintenanceWindow": "tue:08:30-tue:09:30",
            "CacheSecurityGroups": [],
            "CacheSubnetGroupName": "default",
            "CacheNodeType": "cache.t2.small",
             "DataTiering": "disabled"
            "EngineVersion": "3.2.10",
            "ClientDownloadLandingPage": "https://console.aws.amazon.com/elasticache/home#client-download:",
            "CacheClusterCreateTime": "2018-04-25T18:19:28.241Z"
        }
    ]
}
```

For more information, see the topic [describe-cache-clusters](../../../cli/latest/reference/elasticache/describe-cache-clusters.md "../../../cli/latest/reference/elasticache/describe-cache-clusters.md").

### Finding the Endpoints for Valkey or Redis OSS Replication Groups (AWS CLI)

You can use the AWS CLI to discover the endpoints for a replication group and its clusters with the
`describe-replication-groups` command.
The command returns the replication group's primary endpoint and a list of all the clusters (nodes)
in the replication group with their endpoints, along with the reader endpoint.

The following operation retrieves the primary endpoint and reader endpoint for the
replication group `myreplgroup`.
Use the primary endpoint for all write operations.

```
aws elasticache describe-replication-groups \
    --replication-group-id `myreplgroup`
```

For Windows:

```
aws elasticache describe-replication-groups ^
    --replication-group-id `myreplgroup`
```

Output from this operation should look something like this (JSON format).

```
{
   "ReplicationGroups": [
     {
       "Status": "available",
       "Description": "test",
       "NodeGroups": [
         {
            "Status": "available",
               "NodeGroupMembers": [
                  {
                     "CurrentRole": "primary",
                     "PreferredAvailabilityZone": "us-west-2a",
                     "CacheNodeId": "0001",
                     "ReadEndpoint": {
                        "Port": 6379,
                        "Address": "myreplgroup-001.amazonaws.com"
                     },
                     "CacheClusterId": "myreplgroup-001"
                  },
                  {
                     "CurrentRole": "replica",
                     "PreferredAvailabilityZone": "us-west-2b",
                     "CacheNodeId": "0001",
                     "ReadEndpoint": {
                        "Port": 6379,
                        "Address": "myreplgroup-002.amazonaws.com"
                     },
                     "CacheClusterId": "myreplgroup-002"
                  },
                  {
                     "CurrentRole": "replica",
                     "PreferredAvailabilityZone": "us-west-2c",
                     "CacheNodeId": "0001",
                     "ReadEndpoint": {
                        "Port": 6379,
                        "Address": "myreplgroup-003.amazonaws.com"
                     },
                     "CacheClusterId": "myreplgroup-003"
                  }
               ],
               "NodeGroupId": "0001",
               "PrimaryEndpoint": {
                  "Port": 6379,
                  "Address": "myreplgroup.amazonaws.com"
               },
               "ReaderEndpoint": {
                  "Port": 6379,
                  "Address": "myreplgroup-ro.amazonaws.com"
               }
            }
         ],
         "ReplicationGroupId": "myreplgroup",
         "AutomaticFailover": "enabled",
         "SnapshottingClusterId": "myreplgroup-002",
         "MemberClusters": [
            "myreplgroup-001",
            "myreplgroup-002",
            "myreplgroup-003"
         ],
         "PendingModifiedValues": {}
      }
   ]
}
```

For more information, see [describe-replication-groups](../../../cli/latest/reference/elasticache/describe-replication-groups.md "../../../cli/latest/reference/elasticache/describe-replication-groups.md") in the _AWS CLI Command Reference_.

For Memcached, you can use the Amazon ElastiCache API to discover the endpoints for nodes and clusters.

For Redis OSS, you can use the Amazon ElastiCache API to discover the endpoints for nodes, clusters, and also
replication groups.

###### Topics

- [Finding Endpoints for Nodes and Clusters (ElastiCache API)](#Endpoints.Find.API.Nodes "#Endpoints.Find.API.Nodes")
- [Finding Endpoints for Valkey or Redis OSS Replication Groups (ElastiCache API)](#Endpoints.Find.API.ReplGroups "#Endpoints.Find.API.ReplGroups")

### Finding Endpoints for Nodes and Clusters (ElastiCache API)

You can use the ElastiCache API to discover the endpoints for a cluster and its nodes with the
`DescribeCacheClusters` action.

For Valkey or Redis OSS clusters, the command returns the cluster endpoint.
For Memcached clusters, the command returns the configuration endpoint.

If you include the optional parameter `ShowCacheNodeInfo`,
the action also returns the endpoints of the individual nodes in the cluster.

For Memcached, the following command retrieves the configuration endpoint (`ConfigurationEndpoint`) and
individual node endpoints (`Endpoint`) for the Memcached cluster _mycluster_.

```
https://elasticache.us-west-2.amazonaws.com/
    ?Action=DescribeCacheClusters
    &CacheClusterId=mycluster
    &ShowCacheNodeInfo=true
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20150202T192317Z
    &Version=2015-02-02
    &X-Amz-Credential=<credential>
```

###### Important

If you choose to create a CNAME for your Memcached configuration endpoint,
in order for your auto discovery client to recognize the CNAME as a configuration endpoint,
you must include `.cfg.` in the CNAME. For example, `mycluster`.cfg.`local`
in your php.ini file for the `session.save_path` parameter.

### Finding Endpoints for Valkey or Redis OSS Replication Groups (ElastiCache API)

You can use the ElastiCache API to discover the endpoints for a replication group and its clusters with the
`DescribeReplicationGroups` action.
The action returns the replication group's primary endpoint and a list of all the clusters
in the replication group with their endpoints, along with the reader endpoint.

The following operation retrieves the primary endpoint (PrimaryEndpoint), reader endpoint (ReaderEndpoint) and individual node endpoints (ReadEndpoint) for the
replication group `myreplgroup`.
Use the primary endpoint for all write operations.

```
https://elasticache.us-west-2.amazonaws.com/
    ?Action=DescribeReplicationGroups
    &ReplicationGroupId=myreplgroup
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20150202T192317Z
    &Version=2015-02-02
    &X-Amz-Credential=<credential>
```

For more information, see [DescribeReplicationGroups](../APIReference/API_DescribeReplicationGroups.md "../APIReference/API_DescribeReplicationGroups.md").
