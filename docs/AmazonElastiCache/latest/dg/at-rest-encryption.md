

# At-Rest Encryption in ElastiCache
<a name="at-rest-encryption"></a>

To help keep your data secure, Amazon ElastiCache and Amazon S3 provide different ways to restrict access to data in your cache. For more information, see [Amazon VPCs and ElastiCache security](VPCs.md) and [Identity and Access Management for Amazon ElastiCache](IAM.md).

ElastiCache at-rest encryption is a feature to increase data security by encrypting on-disk data. It is always enabled on a serverless cache and on clusters with durability enabled. When enabled, it encrypts the following aspects:
+ Disk during sync, backup and swap operations
+ Backups stored in Amazon S3 
+ Multi-AZ transactional durability logs (for clusters with durability enabled)

Data stored on SSDs (solid-state drives) in data tiering enabled clusters is always encrypted.

 ElastiCache offers default (service managed) encryption at rest, as well as ability to use your own symmetric customer managed AWS KMS keys in [AWS Key Management Service (KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html). When the cache is backed up, under encryption options, choose whether to use the default encryption key or a customer-managed key. For more information, see [Enabling At-Rest Encryption](#at-rest-encryption-enable).

**Important**  
Enabling At-Rest Encryption on an existing node-based Valkey or Redis OSS cluster involves deleting your existing replication group, **after** running backup and restore on the replication group.

At-rest encryption can be enabled on a cache only when it is created. Because there is some processing needed to encrypt and decrypt the data, enabling at-rest encryption can have a performance impact during these operations. You should benchmark your data with and without at-rest encryption to determine the performance impact for your use cases. 

**Topics**
+ [At-Rest Encryption Conditions](#at-rest-encryption-constraints)
+ [Using customer managed keys from AWS KMS](#using-customer-managed-keys-for-elasticache-security)
+ [Enabling At-Rest Encryption](#at-rest-encryption-enable)
+ [Viewing at-rest encryption status](#viewing-at-rest-encryption-status)
+ [See Also](#at-rest-encryption-see-also)

## At-Rest Encryption Conditions
<a name="at-rest-encryption-constraints"></a>

The following constraints on ElastiCache at-rest encryption should be kept in mind when you plan your implementation of ElastiCache encryption at-rest:
+ At-rest encryption is supported on replication groups running Valkey 7.2 and later, and Redis OSS version 4.0.10 or later.
+ At-rest encryption is supported only for replication groups running in an Amazon VPC.
+ At-rest encryption is only supported for replication groups running the following node types.
  + R8g, R7g, R6gd, R6g, R5, R4, R3
  + M8g, M7g, M6g, M5, M4, M3
  + T4g, T3, T2
  + C8gn, C7gn

  For more information, see [Supported node types](CacheNodes.SupportedTypes.md)
+ At-rest encryption is enabled by setting the parameter `AtRestEncryptionEnabled` to `true`. For Valkey, this parameter defaults to `true` if not specified.
+ You can enable at-rest encryption on a replication group only when creating the replication group. You cannot toggle at-rest encryption on and off by modifying a replication group. For information on implementing at-rest encryption on an existing replication group, see [Enabling At-Rest Encryption](#at-rest-encryption-enable).
+ If a cluster is using a node type from the r6gd family, data stored on SSD is encrypted whether at-rest encryption is enabled or not.
+ If a cluster is using a node type from the r6gd family, data stored on SSD is encrypted with the chosen customer managed AWS KMS key.
+ With Memcached, at-rest encryption is supported only on serverless caches.

Implementing at-rest encryption can reduce performance during backup and node sync operations. Benchmark at-rest encryption compared to no encryption on your own data to determine its impact on performance for your implementation.

**Note**  
Clusters with durability enabled (sync or async) always have at-rest encryption enabled. You cannot enable durability without also enabling at-rest encryption.

## Using customer managed keys from AWS KMS
<a name="using-customer-managed-keys-for-elasticache-security"></a>

ElastiCache supports symmetric customer managed AWS KMS keys (KMS key) for encryption at rest. Customer-managed KMS keys are encryption keys that you create, own and manage in your AWS account. For more information, see [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#root_keys) in the *AWS Key Management Service Developer Guide*. The keys must be created in AWS KMS before they can be used with ElastiCache.

To learn how to create AWS KMS root keys, see [Creating Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*. 

ElastiCache allows you to integrate with AWS KMS. For more information, see [Using Grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) in the *AWS Key Management Service Developer Guide*. No customer action is needed to enable Amazon ElastiCache integration with AWS KMS. 

The `kms:ViaService` condition key limits use of an AWS KMS key (KMS key) to requests from specified AWS services. To use `kms:ViaService` with ElastiCache, include both ViaService names in the condition key value: `elasticache.AWS_region.amazonaws.com` and `dax.AWS_region.amazonaws.com`. For more information, see [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service).

You can use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) to track the requests that Amazon ElastiCache sends to AWS Key Management Service on your behalf. All API calls to AWS Key Management Service related to customer managed keys have corresponding CloudTrail logs. You can also see the grants that ElastiCache creates by calling the [ListGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListGrants.html) KMS API call. 

Once a replication group is encrypted using customer managed key, all backups for the replication group are encrypted as follows:
+ Automatic daily backups are encrypted using the customer managed key associated with the cluster.
+ Final backup created when replication group is deleted, is also encrypted using the customer managed key associated with the replication group.
+ Manually created backups are encrypted by default to use the KMS key associated with the replication group. You may override this by choosing another customer managed key.
+ Copying a backup defaults to using a customer managed key associated with the source backup. You may override this by choosing another customer managed key.

**Note**  
Customer managed keys cannot be used when exporting backups to your selected Amazon S3 bucket. However, all backups exported to Amazon S3 are encrypted using [Server side encryption.](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html) You may choose to copy the backup file to a new S3 object and encrypt using a customer managed KMS key, copy the file to another S3 bucket that is set up with default encryption using a KMS key or change an encryption option in the file itself.
You can also use customer managed keys to encrypt manually-created backups for replication groups that do not use customer managed keys for encryption. With this option, the backup file stored in Amazon S3 is encrypted using a KMS key, even though the data is not encrypted on the original replication group. 
Restoring from a backup allows you to choose from available encryption options, similar to encryption choices available when creating a new replication group.
+ If you delete the key or [disable](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) the key and [revoke grants](https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html) for the key that you used to encrypt a cache, the cache becomes irrecoverable. In other words, it cannot be modified or recovered after a hardware failure. AWS KMS deletes root keys only after a waiting period of at least seven days. After the key is deleted, you can use a different customer managed key to create a backup for archival purposes. 
+ If you delete the key, disable the key, or revoke grants for the key that you used to encrypt a durability-enabled cluster, the cluster is set to a failed state within 12 hours.
+ Automatic key rotation preserves the properties of your AWS KMS root keys, so the rotation has no effect on your ability to access your ElastiCache data. Encrypted Amazon ElastiCache caches don't support manual key rotation, which involves creating a new root key and updating any references to the old key. To learn more, see [Rotating AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) in the *AWS Key Management Service Developer Guide*. 
+ Encrypting an ElastiCache cache using KMS key requires one grant per cache. This grant is used throughout the lifespan of the cache. Additionally, one grant per backup is used during backup creation. This grant is retired once the backup is created. 
+ For more information on AWS KMS grants and limits, see [Limits](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html) in the *AWS Key Management Service Developer Guide*.

## Enabling At-Rest Encryption
<a name="at-rest-encryption-enable"></a>

All serverless caches have at-rest encryption enabled.

When creating a node-based cluster, you can enable at-rest encryption by setting the parameter `AtRestEncryptionEnabled` to `true`. You can't enable at-rest encryption on existing replication groups.

 You can enable at-rest encryption when you create an ElastiCache cache. You can do so using the AWS Management Console, the AWS CLI, or the ElastiCache API.

When creating a cache, you can pick one of the following options:
+ **Default** – This option uses service managed encryption at rest. 
+ **Customer managed key ** – This option allows you to provide the Key ID/ARN from AWS KMS for encryption at rest. 

To learn how to create AWS KMS root keys, see [Create Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide* 

**Contents**
+ [Enabling At-Rest Encryption Using the AWS Management Console](#at-rest-encryption-enable-con)
+ [Enabling At-Rest Encryption Using the AWS CLI](#at-rest-encryption-enable-cli)

### Enabling At-Rest Encryption on an existing node-based Valkey or Redis OSS Cluster
<a name="at-reset-encryption-enable-existing-cluster"></a>

You can only enable at-rest encryption when you create a Valkey or Redis OSS replication group. If you have an existing replication group on which you want to enable at-rest encryption, do the following.

**To enable at-rest encryption on an existing replication group**

1. Create a manual backup of your existing replication group. For more information, see [Taking manual backups](backups-manual.md).

1. Create a new replication group by restoring from the backup. On the new replication group, enable at-rest encryption. For more information, see [Restoring from a backup into a new cache](backups-restoring.md).

1. Update the endpoints in your application to point to the new replication group.

1. Delete the old replication group. For more information, see [Deleting a cluster in ElastiCache](Clusters.Delete.md) or [Deleting a replication group](Replication.DeletingRepGroup.md).

### Enabling At-Rest Encryption Using the AWS Management Console
<a name="at-rest-encryption-enable-con"></a>

#### Enabling At-Rest Encryption on a Serverless Cache (Console)
<a name="at-rest-encryption-enable-con-serverless"></a>

All serverless caches have at-rest encryption enabled. By default, an AWS-owned KMS key is used to encrypt data. To choose your own AWS KMS key, make the following selections:
+ Expand the **Default settings** section.
+ Choose **Customize default settings** under **Default settings** section.
+ Choose **Customize your security settings** under **Security** section.
+ Choose **Customer managed CMK** under **Encryption key** setting.
+ Select a key under **AWS KMS key** setting.

#### Enabling At-Rest Encryption on a Node-Based Cluster (Console)
<a name="at-rest-encryption-enable-con-self-designed"></a>

When designing your own cache, 'Dev/Test' and 'Production' configurations with the 'Easy create' method have at-rest encryption enabled using the **Default** key. When choosing configuration yourself, make the following selections:
+ Choose version 4.0.10 or later as your engine version.
+ Click the checkbox next to **Enable** for the **Encryption at rest** option.
+ Choose either a **Default key** or **Customer managed CMK**.

For the step-by-step procedure, see the following:
+ [Creating a Valkey (cluster mode disabled) cluster (Console)](SubnetGroups.designing-cluster-pre.valkey.md#Clusters.Create.CON.valkey-gs)
+ [Creating a Valkey or Redis OSS (cluster mode enabled) cluster (Console)](Clusters.Create.md#Clusters.Create.CON.RedisCluster)

### Enabling At-Rest Encryption Using the AWS CLI
<a name="at-rest-encryption-enable-cli"></a>

To enable at-rest encryption when creating a Valkey or Redis OSS cluster using the AWS CLI, use the *--at-rest-encryption-enabled* parameter when creating a replication group.

#### Enabling At-Rest Encryption on a Valkey or Redis OSS (Cluster Mode Disabled) Cluster (CLI)
<a name="at-rest-encryption-enable-cli-redis-classic-rg"></a>

The following operation creates the Valkey or Redis OSS (cluster mode disabled) replication group `my-classic-rg` with three nodes (*--num-cache-clusters*), a primary and two read replicas. At-rest encryption is enabled for this replication group (*--at-rest-encryption-enabled*).

The following parameters and their values are necessary to enable encryption on this replication group:

**Key Parameters**
+ **--engine**—Must be `valkey` or `redis`.
+ **--engine-version**—If the engine is Redis OSS, this must be 4.0.10 or later.
+ **--at-rest-encryption-enabled**—Required to enable at-rest encryption.

**Example 1: Valkey or Redis OSS (Cluster Mode Disabled) Cluster with Replicas**  
For Linux, macOS, or Unix:  

```
aws elasticache create-replication-group \
    --replication-group-id {{my-classic-rg}} \
    --replication-group-description {{"3 node replication group"}} \
    --cache-node-type {{cache.m4.large}} \
    --engine {{redis}} \    
    --at-rest-encryption-enabled \  
    --num-cache-clusters {{3}}
```
For Windows:  

```
aws elasticache create-replication-group ^
    --replication-group-id {{my-classic-rg}} ^
    --replication-group-description {{"3 node replication group"}} ^
    --cache-node-type {{cache.m4.large}} ^
    --engine {{redis}} ^    
    --at-rest-encryption-enabled ^  
    --num-cache-clusters {{3}} ^
```

For additional information, see the following:
+ [Creating a Valkey or Redis OSS (Cluster Mode Disabled) replication group from scratch (AWS CLI)](Replication.CreatingReplGroup.NoExistingCluster.Classic.md#Replication.CreatingReplGroup.NoExistingCluster.Classic.CLI)
+ [create-replication-group](https://docs.aws.amazon.com/cli/latest/reference/elasticache/create-replication-group.html)

 

#### Enabling At-Rest Encryption on a Cluster for Valkey or Redis OSS (Cluster Mode Enabled) (CLI)
<a name="at-rest-encryption-enable-cli-clustered-redis"></a>

The following operation creates the Valkey or Redis OSS (cluster mode enabled) replication group `my-clustered-rg` with three node groups or shards (*--num-node-groups*). Each has three nodes, a primary and two read replicas (*--replicas-per-node-group*). At-rest encryption is enabled for this replication group (*--at-rest-encryption-enabled*).

The following parameters and their values are necessary to enable encryption on this replication group:

**Key Parameters**
+ **--engine**—Must be `valkey` or `redis`.
+ **--engine-version**—If the engine is Redis OSS, this must be 4.0.10 or later.
+ **--at-rest-encryption-enabled**—Required to enable at-rest encryption.
+ **--cache-parameter-group**—Must be `default-redis4.0.cluster.on` or one derived from it to make this a cluster mode enabled replication group.

**Example 2: A Valkey or Redis OSS (Cluster Mode Enabled) Cluster**  
For Linux, macOS, or Unix:  

```
aws elasticache create-replication-group \
   --replication-group-id {{my-clustered-rg}} \
   --replication-group-description {{"redis clustered cluster"}} \
   --cache-node-type {{cache.m5.large}} \
   --num-node-groups {{3}} \
   --replicas-per-node-group {{2}} \
   --engine {{redis}} \
   --engine-version {{6.2}} \
   --at-rest-encryption-enabled \
   --cache-parameter-group {{default.redis6.x.cluster.on}}
```
For Windows:  

```
aws elasticache create-replication-group ^
   --replication-group-id {{my-clustered-rg}} ^
   --replication-group-description {{"redis clustered cluster"}} ^
   --cache-node-type {{cache.m5.large}} ^
   --num-node-groups {{3}} ^
   --replicas-per-node-group {{2}} ^
   --engine {{redis}} ^
   --engine-version {{6.2}} ^
   --at-rest-encryption-enabled ^
   --cache-parameter-group {{default.redis6.x.cluster.on}}
```

For additional information, see the following:
+ [Creating a Valkey or Redis OSS (Cluster Mode Enabled) replication group from scratch (AWS CLI)](Replication.CreatingReplGroup.NoExistingCluster.Cluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.CLI)
+ [create-replication-group](https://docs.aws.amazon.com/cli/latest/reference/elasticache/create-replication-group.html)

## Viewing at-rest encryption status
<a name="viewing-at-rest-encryption-status"></a>

You can check the at-rest encryption status of an existing cluster using the `StorageEncryptionType` field returned by the describe API calls. This field is available on both node-based replication groups and serverless caches.

`StorageEncryptionType` values:


| Value | Meaning | 
| --- | --- | 
| none | At-rest encryption is not enabled | 
| sse-elasticache | Encrypted using a service-managed AWS KMS key | 
| sse-kms | Encrypted using a customer-managed AWS KMS key | 

### Checking status for a node-based replication group (AWS CLI)
<a name="viewing-encryption-replication-group"></a>

```
aws elasticache describe-replication-groups \
    --replication-group-id {{my-replication-group}} \
    --query 'ReplicationGroups[0].StorageEncryptionType'
```

Example output:

```
"sse-elasticache"
```

### Checking status for a serverless cache (AWS CLI)
<a name="viewing-encryption-serverless-cache"></a>

```
aws elasticache describe-serverless-caches \
    --serverless-cache-name {{my-serverless-cache}} \
    --query 'ServerlessCaches[0].StorageEncryptionType'
```

Example output:

```
"sse-elasticache"
```

## See Also
<a name="at-rest-encryption-see-also"></a>
+ [Amazon VPCs and ElastiCache security](VPCs.md)
+ [Identity and Access Management for Amazon ElastiCache](IAM.md)