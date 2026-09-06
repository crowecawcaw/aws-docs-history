

# Creating a cluster for Memcached
<a name="Clusters.Create-mc"></a>

The following examples show how to create a cluster using the AWS Management Console, AWS CLI and ElastiCache API.

## Creating a Memcached cluster (console)
<a name="Clusters.Create.CON.Memcached"></a>

When you use the Memcached engine, Amazon ElastiCache supports horizontally partitioning your data over multiple nodes. Memcached enables auto discovery so you don't need to keep track of the endpoints for each node. Memcached tracks each node's endpoint, updating the endpoint list as nodes are added and removed. All your application needs to interact with the cluster is the configuration endpoint. 

To create a Memcached cluster via the console, follow the steps at [Creating a Valkey (cluster mode disabled) cluster (Console)](Clusters.Create.md#Clusters.Create.CON.RedisCluster). When you reach step five, select **Create Memcached cache**.

As soon as your cluster's status is *available*, you can grant Amazon EC2 access to it, connect to it, and begin using it. For more information, see the similar steps [Step 3. Authorize access to the cluster](SubnetGroups.designing-cluster-pre.valkey.md#GettingStarted.AuthorizeAccess.valkey) and [Step 4. Connect to the cluster's node](SubnetGroups.designing-cluster-pre.valkey.md#GettingStarted.ConnectToCacheNode.valkey).

**Important**  
As soon as your cluster becomes available, you're billed for each hour or partial hour that the cluster is active, even if you're not actively using it. To stop incurring charges for this cluster, you must delete it. See [Deleting a cluster in ElastiCache](Clusters.Delete.md). 

## Creating a cluster (AWS CLI)
<a name="Clusters.Create.CLI.memcached-intro"></a>

To create a cluster using the AWS CLI, use the `create-cache-cluster` command.

**Important**  
As soon as your cluster becomes available, you're billed for each hour or partial hour that the cluster is active, even if you're not actively using it. To stop incurring charges for this cluster, you must delete it. See [Deleting a cluster in ElastiCache](Clusters.Delete.md). 

### Creating a Memcached Cache Cluster (AWS CLI)
<a name="Clusters.Create.CLI.Memcached"></a>

The following CLI code creates a Memcached cluster with 3 nodes.

For Linux, macOS, or Unix:

```
aws elasticache create-cache-cluster \
--cache-cluster-id {{my-cluster}} \
--cache-node-type {{cache.r4.large}} \
--engine {{memcached}} \
--engine-version {{1.4.24}} \
--cache-parameter-group {{default.memcached1.4}} \
--num-cache-nodes {{3}}
```

For Windows:

```
aws elasticache create-cache-cluster ^
--cache-cluster-id {{my-cluster}} ^
--cache-node-type {{cache.r4.large}} ^
--engine {{memcached}} ^
--engine-version {{1.4.24}} ^
--cache-parameter-group {{default.memcached1.4}} ^
--num-cache-nodes {{3}}
```

## Creating a cluster for Memcached (ElastiCache API)
<a name="Clusters.Create.API.mem-heading"></a>

To create a cluster using the ElastiCache API, use the `CreateCacheCluster` action. 

**Important**  
As soon as your cluster becomes available, you're billed for each hour or partial hour that the cluster is active, even if you're not using it. To stop incurring charges for this cluster, you must delete it. See [Deleting a cluster in ElastiCache](Clusters.Delete.md). 

**Topics**
+ [Creating a Memcached cluster (ElastiCache API)](#Clusters.Create.API.Memcached)

### Creating a Memcached cluster (ElastiCache API)
<a name="Clusters.Create.API.Memcached"></a>

The following code creates a Memcached cluster with 3 nodes (ElastiCache API).

Line breaks are added for ease of reading.

```
https://elasticache.us-west-2.amazonaws.com/
    ?Action=CreateCacheCluster
    &CacheClusterId=my-cluster
    &CacheNodeType=cache.r4.large
    &Engine=memcached
    &NumCacheNodes=3
    &SignatureVersion=4       
    &SignatureMethod=HmacSHA256
    &Timestamp=20150508T220302Z
    &Version=2015-02-02
    &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
    &X-Amz-Credential=<credential>
    &X-Amz-Date=20150508T220302Z
    &X-Amz-Expires=20150508T220302Z
    &X-Amz-SignedHeaders=Host
    &X-Amz-Signature=<signature>
```