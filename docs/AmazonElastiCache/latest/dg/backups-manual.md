

# Taking manual backups
<a name="backups-manual"></a>

In addition to automatic backups, you can create a *manual* backup at any time. Unlike automatic backups, which are automatically deleted after a specified retention period, manual backups do not have a retention period after which they are automatically deleted. Even if you delete the cache, any manual backups from that cache are retained. If you no longer want to keep a manual backup, you must explicitly delete it yourself.

In addition to directly creating a manual backup, you can create a manual backup in one of the following ways:
+ [Copying backups](backups-copying.md). It does not matter whether the source backup was created automatically or manually.
+ [Creating a final backup](backups-final.md). Create a backup immediately before deleting a cluster or node.

You can create a manual backup of a cache using the AWS Management Console, the AWS CLI, or the ElastiCache API.

You can generate manual backups from replicas that are cluster mode enabled, and cluster mode disabled.



## Creating a manual backup (Console)
<a name="backups-manual-CON"></a>

**To create a backup of a cache (console)**

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. From the navigation pane, choose **Valkey caches**, **Redis OSS caches**, or **Memcached caches**, depending on your preference.

1. Choose the box to the left of the name of the cache you want to back up.

1. Choose **Backup**.

1. In the **Create Backup** dialog, type in a name for your backup in the **Backup Name** box. We recommend that the name indicate which cluster was backed up and the date and time the backup was made.

   Cluster naming constraints are as follows:
   + Must contain 1–40 alphanumeric characters or hyphens.
   + Must begin with a letter.
   + Can't contain two consecutive hyphens.
   + Can't end with a hyphen.

1. Choose **Create Backup**.

   The status of the cluster changes to *snapshotting*.

## Creating a manual backup (AWS CLI)
<a name="backups-manual-CLI"></a>

**Manual backup of a serverless cache with the AWS CLI**

To create a manual backup of a cache using the AWS CLI, use the `create-serverless-cache-snapshot` AWS CLI operation with the following parameters:
+ `--serverless-cache-name` – The name of the serverless cache that you are backing up.
+ `--serverless-cache-snapshot-name` – Name of the snapshot to be created.

For Linux, macOS, or Unix:
+ 

  ```
  aws elasticache create-serverless-cache-snapshot \
                          --serverless-cache-name CacheName \
                          --serverless-cache-snapshot-name bkup-20231127
  ```

For Windows:
+ 

  ```
  aws elasticache create-serverless-cache-snapshot ^
      --serverless-cache-name CacheName ^
      --serverless-cache-snapshot-name bkup-20231127
  ```

**Manual backup of a node-based cluster with the AWS CLI**

To create a manual backup of a node-based cluster using the AWS CLI, use the `create-snapshot` AWS CLI operation with the following parameters:
+ `--cache-cluster-id`
  + If the cluster you're backing up has no replica nodes, `--cache-cluster-id` is the name of the cluster you are backing up, for example {{mycluster}}.
  + If the cluster you're backing up has one or more replica nodes, `--cache-cluster-id` is the name of the node in the cluster that you want to use for the backup. For example, the name might be {{mycluster-002}}.

  Use this parameter only when backing up a Valkey or Redis OSS (cluster mode disabled) cluster.

   
+ `--replication-group-id` – Name of the Valkey or Redis OSS (cluster mode enabled) cluster (CLI/API: a replication group) to use as the source for the backup. Use this parameter when backing up a Valkey or Redis OSS (cluster mode enabled) cluster.

   
+ `--snapshot-name` – Name of the snapshot to be created.

  Cluster naming constraints are as follows:
  + Must contain 1–40 alphanumeric characters or hyphens.
  + Must begin with a letter.
  + Can't contain two consecutive hyphens.
  + Can't end with a hyphen.

### Example 1: Backing up a Valkey or Redis OSS (Cluster Mode Disabled) cluster that has no replica nodes
<a name="backups-manual-CLI-example1"></a>

The following AWS CLI operation creates the backup `bkup-20150515` from the Valkey or Redis OSS (cluster mode disabled) cluster `myNonClusteredRedis` that has no read replicas.

For Linux, macOS, or Unix:

```
aws elasticache create-snapshot \
    --cache-cluster-id {{myNonClusteredRedis}} \
    --snapshot-name {{bkup-20150515}}
```

For Windows:

```
aws elasticache create-snapshot ^
    --cache-cluster-id {{myNonClusteredRedis}} ^
    --snapshot-name {{bkup-20150515}}
```

### Example 2: Backing up a Valkey or Redis OSS (Cluster Mode Disabled) cluster with replica nodes
<a name="backups-manual-CLI-example2"></a>

The following AWS CLI operation creates the backup `bkup-20150515` from the Valkey or Redis OSS (cluster mode disabled) cluster `myNonClusteredRedis`. This backup has one or more read replicas.

For Linux, macOS, or Unix:

```
aws elasticache create-snapshot \
    --cache-cluster-id {{myNonClusteredRedis-001}} \
    --snapshot-name {{bkup-20150515}}
```

For Windows:

```
aws elasticache create-snapshot ^
    --cache-cluster-id {{myNonClusteredRedis-001}} ^
    --snapshot-name {{bkup-20150515}}
```

**Example Output: Backing Up a Valkey or Redis OSS (Cluster Mode Disabled) Cluster with Replica Nodes**

Output from the operation looks something like the following.

```
{
    "Snapshot": {
        "Engine": "redis", 
        "CacheParameterGroupName": "default.redis6.x", 
        "VpcId": "vpc-91280df6", 
        "CacheClusterId": "myNonClusteredRedis-001", 
        "SnapshotRetentionLimit": 0, 
        "NumCacheNodes": 1, 
        "SnapshotName": "bkup-20150515", 
        "CacheClusterCreateTime": "2017-01-12T18:59:48.048Z", 
        "AutoMinorVersionUpgrade": true, 
        "PreferredAvailabilityZone": "us-east-1c", 
        "SnapshotStatus": "creating", 
        "SnapshotSource": "manual", 
        "SnapshotWindow": "08:30-09:30", 
        "EngineVersion": "6.0", 
        "NodeSnapshots": [
            {
                "CacheSize": "", 
                "CacheNodeId": "0001", 
                "CacheNodeCreateTime": "2017-01-12T18:59:48.048Z"
            }
        ], 
        "CacheSubnetGroupName": "default", 
        "Port": 6379, 
        "PreferredMaintenanceWindow": "wed:07:30-wed:08:30", 
        "CacheNodeType": "cache.m5.2xlarge",
        "DataTiering": "disabled"
    }
}
```

### Example 3: Backing up a cluster for Valkey or Redis OSS (Cluster Mode Enabled)
<a name="backups-manual-CLI-example3"></a>

The following AWS CLI operation creates the backup `bkup-20150515` from the Valkey or Redis OSS (cluster mode enabled) cluster `myClusteredRedis`. Note the use of `--replication-group-id` instead of `--cache-cluster-id` to identify the source. Also note that ElastiCache takes the backup using the replica node when present, and will default to the primary node if a replica node is unavailable.

For Linux, macOS, or Unix:

```
aws elasticache create-snapshot \
    --replication-group-id {{myClusteredRedis}} \
    --snapshot-name {{bkup-20150515}}
```

For Windows:

```
aws elasticache create-snapshot ^
    --replication-group-id {{myClusteredRedis}} ^
    --snapshot-name {{bkup-20150515}}
```

**Example Output: Backing Up a Valkey or Redis OSS (Cluster Mode Enabled) Cluster**

Output from this operation looks something like the following.

```
{
    "Snapshot": {
        "Engine": "redis", 
        "CacheParameterGroupName": "default.redis6.x.cluster.on", 
        "VpcId": "vpc-91280df6", 
        "NodeSnapshots": [
            {
                "CacheSize": "", 
                "NodeGroupId": "0001"
            }, 
            {
                "CacheSize": "", 
                "NodeGroupId": "0002"
            }
        ], 
        "NumNodeGroups": 2, 
        "SnapshotName": "bkup-20150515", 
        "ReplicationGroupId": "myClusteredRedis", 
        "AutoMinorVersionUpgrade": true, 
        "SnapshotRetentionLimit": 1, 
        "AutomaticFailover": "enabled", 
        "SnapshotStatus": "creating", 
        "SnapshotSource": "manual", 
        "SnapshotWindow": "10:00-11:00", 
        "EngineVersion": "6.0", 
        "CacheSubnetGroupName": "default", 
        "ReplicationGroupDescription": "2 shards 2 nodes each", 
        "Port": 6379, 
        "PreferredMaintenanceWindow": "sat:03:30-sat:04:30", 
        "CacheNodeType": "cache.r5.large",
        "DataTiering": "disabled"
    }
}
```

### Related topics
<a name="backups-manual-CLI-see-also"></a>

For more information, see [create-snapshot](https://docs.aws.amazon.com/cli/latest/reference/elasticache/create-snapshot.html) in the *AWS CLI Command Reference*.

## Creating a backup using CloudFormation
<a name="backups-CFN"></a>

You can use CloudFormation to create a backup of your ElastiCache Redis OSS or Valkey cache, using the `AWS::ElastiCache::ServerlessCache` or `AWS::ElastiCache::ReplicationGroup` properties.

**Using the `AWS::ElastiCache::ServerlessCache` resource **

Use this to create a backup using the AWS::ElastiCache::ServerlessCache resource:

```
Resources:
                    iotCatalog:
                        Type: AWS::ElastiCache::ServerlessCache
                            Properties:
                            ...
                            ServerlessCacheName: "your-cache-name"
                            Engine: "redis"
                            CacheUsageLimits
```

**Using the AWS::ElastiCache::ReplicationGroup resource **

Use the `AWS::ElastiCache::ReplicationGroup` resource:

```
Resources:
                    iotCatalog:
                        Type: AWS::ElastiCache::ReplicationGroup 
                            Properties:
                            ...
                            ReplicationGroupDescription: "Description of your replication group"
                            Engine: "redis"
                            CacheNodeType
                            NumCacheClusters
                            AutomaticFailoverEnabled
                            AtRestEncryptionEnabled
```