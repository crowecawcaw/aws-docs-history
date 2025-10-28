# At-Rest Encryption in ElastiCache

To help keep your data secure, Amazon ElastiCache and Amazon S3 provide different ways to restrict access
to data in your cache. For more information, see [Amazon VPCs and ElastiCache security](VPCs.md "VPCs.md")
and [Identity and Access Management for Amazon ElastiCache](IAM.md "IAM.md").

ElastiCache at-rest encryption is a feature to increase data security by encrypting on-disk data. It is always enabled on a serverless cache. When enabled, it encrypts the following aspects:

- Disk during sync, backup and swap operations
- Backups stored in Amazon S3
  Data stored on SSDs (solid-state drives) in data tiering enabled clusters is always encrypted.

ElastiCache offers default (service managed) encryption at rest, as well as ability to use your own symmetric customer managed AWS KMS keys in [AWS Key Management Service (KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").
When the cache is backed up, under encryption options, choose whether to use the default encryption key or a customer-managed key.
For more information, see [Enabling At-Rest Encryption](#at-rest-encryption-enable "#at-rest-encryption-enable").

###### Important

Enabling At-Rest Encryption on an existing node-based Valkey or Redis OSS cluster involves deleting your existing replication group, **after** running backup and restore on the replication group.

At-rest encryption can be enabled on a cache only when it is created. Because there is
some processing needed to encrypt and decrypt the data, enabling at-rest encryption can
have a performance impact during these operations. You should benchmark your data
with and without at-rest encryption to determine the performance impact for your use
cases.

###### Topics

- [At-Rest Encryption Conditions](#at-rest-encryption-constraints "#at-rest-encryption-constraints")
- [Using customer managed keys from AWS KMS](#using-customer-managed-keys-for-elasticache-security "#using-customer-managed-keys-for-elasticache-security")
- [Enabling At-Rest Encryption](#at-rest-encryption-enable "#at-rest-encryption-enable")
- [See Also](#at-rest-encryption-see-also "#at-rest-encryption-see-also")

## At-Rest Encryption Conditions

The following constraints on ElastiCache at-rest encryption should be kept in mind when you plan
your implementation of ElastiCache encryption at-rest:

- At-rest encryption is supported on replication groups running Valkey 7.2 and later, and Redis OSS versions (3.2.6 scheduled for EOL, see
  [Redis OSS versions end of life schedule](engine-versions.md#deprecated-engine-versions "engine-versions.md#deprecated-engine-versions")),

  4.0.10 or later.

- At-rest encryption is supported only for replication groups running in an Amazon VPC.
- At-rest encryption is only supported for replication groups running the following node types.

      + R7g, R6gd, R6g, R5, R4, R3
      + M7g, M6g, M5, M4, M3
      + T4g, T3, T2
      + C7gn

  For more information, see [Supported node types](CacheNodes.md "CacheNodes.md")

- At-rest encryption is enabled by explicitly setting the parameter `AtRestEncryptionEnabled`
  to `true`.
- You can enable at-rest encryption on a replication group only when creating the replication group.
  You cannot toggle at-rest encryption on and off by modifying a replication group. For
  information on implementing at-rest encryption on an existing replication group, see
  [Enabling At-Rest Encryption](#at-rest-encryption-enable "#at-rest-encryption-enable").
- If a cluster is using a node type from the r6gd family, data stored on SSD is encrypted whether at-rest encryption is enabled or not.
- The option to use customer managed key for encryption at rest is not available in AWS GovCloud (us-gov-east-1 and us-gov-west-1) regions.
- If a cluster is using a node type from the r6gd family, data stored on SSD is encrypted with the chosen customer managed AWS KMS key (or service-managed encryption in AWS GovCloud Regions).

- With Memcached, at-rest encryption is supported only on serverless caches.
- When using Memcached, the option to use customer managed key for encryption at rest is not available in AWS
  GovCloud (us-gov-east-1 and us-gov-west-1) regions.

Implementing at-rest encryption can reduce performance during backup and node sync
operations. Benchmark at-rest encryption compared to no encryption on your own data to
determine its impact on performance for your implementation.

## Using customer managed keys from AWS KMS

ElastiCache supports symmetric customer managed AWS KMS keys (KMS key) for encryption at rest. Customer-managed KMS keys are encryption keys that you create, own and manage in your AWS account. For more information,
see [AWS KMS keys](../../../kms/latest/developerguide/concepts.md#root_keys "../../../kms/latest/developerguide/concepts.md#root_keys") in the _AWS Key Management Service Developer Guide_. The keys must be created in AWS KMS before they can be used
with ElastiCache.

To learn how to create AWS KMS root keys, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

ElastiCache allows you to integrate with AWS KMS. For more information, see [Using Grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md")
in the _AWS Key Management Service Developer Guide_. No customer action is needed to enable Amazon ElastiCache integration with AWS KMS.

The `kms:ViaService` condition key limits use of an AWS KMS key (KMS key) to requests from specified AWS services. To use `kms:ViaService` with ElastiCache, include both ViaService names in the condition key value:
`elasticache.AWS_region.amazonaws.com` and `dax.AWS_region.amazonaws.com`. For more information, see
[kms:ViaService](../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service "../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service").

You can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") to track the requests that Amazon ElastiCache sends to AWS Key Management Service
on your behalf. All API calls to AWS Key Management Service related to customer managed keys have corresponding CloudTrail logs.
You can also see the grants that ElastiCache creates by calling the [ListGrants](../../../kms/latest/APIReference/API_ListGrants.md "../../../kms/latest/APIReference/API_ListGrants.md") KMS API call.

Once a replication group is encrypted using customer managed key, all backups for the replication group are encrypted as follows:

- Automatic daily backups are encrypted using the customer managed key associated with the cluster.
- Final backup created when replication group is deleted, is also encrypted using the customer managed key associated with the replication group.
- Manually created backups are encrypted by default to use the KMS key associated with the replication group. You may override this by choosing another customer managed key.
- Copying a backup defaults to using a customer managed key associated with the source backup. You may override this by choosing another customer managed key.

###### Note

- Customer managed keys cannot be used when exporting backups to your selected Amazon S3 bucket. However, all backups exported to Amazon S3 are encrypted using
  [Server side encryption.](../../../AmazonS3/latest/dev/UsingServerSideEncryption.md "../../../AmazonS3/latest/dev/UsingServerSideEncryption.md") You may choose to copy the backup file to a new S3 object and encrypt using a customer managed
  KMS key, copy the file to another S3 bucket that is set up with default encryption using a KMS key or change an encryption option in the file itself.
- You can also use customer managed keys to encrypt manually-created backups for replication groups that do not use customer managed keys for encryption. With this option, the backup file stored in Amazon S3 is encrypted using
  a KMS key, even though the data is not encrypted on the original replication group.
  Restoring from a backup allows you to choose from available encryption options, similar to encryption choices available when creating a new replication group.

- If you delete the key or [disable](../../../kms/latest/developerguide/enabling-keys.md "../../../kms/latest/developerguide/enabling-keys.md") the key and [revoke grants](../../../kms/latest/APIReference/API_RevokeGrant.md "../../../kms/latest/APIReference/API_RevokeGrant.md") for the key that you used to encrypt a cache,
  the cache becomes irrecoverable. In other words, it cannot be modified or recovered after a hardware failure. AWS KMS deletes root keys only after a waiting period of at least seven days.
  After the key is deleted, you can use a different customer managed key to create a backup for archival purposes.
- Automatic key rotation preserves the properties of your AWS KMS root keys, so the rotation has no effect on your ability to access your ElastiCache data.
  Encrypted Amazon ElastiCache caches don't support manual key rotation, which involves creating a new root key and updating
  any references to the old key. To learn more, see [Rotating AWS KMS keys](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md") in the _AWS Key Management Service Developer Guide_.
- Encrypting an ElastiCache cache using KMS key requires one grant per cache.
  This grant is used throughout the lifespan of the cache. Additionally, one grant per backup is used during backup creation.
  This grant is retired once the backup is created.
- For more information on AWS KMS grants and limits, see [Limits](../../../kms/latest/developerguide/limits.md "../../../kms/latest/developerguide/limits.md") in the _AWS Key Management Service Developer Guide_.

## Enabling At-Rest Encryption

All serverless caches have at-rest encryption enabled.

When creating a node-based cluster, you can enable at-rest encryption by setting the
parameter `AtRestEncryptionEnabled` to `true`. You can't enable
at-rest encryption on existing replication groups.

You can enable at-rest encryption when you create an ElastiCache cache. You can do
so using the AWS Management Console, the AWS CLI, or the ElastiCache API.

When creating a cache, you can pick one of the following options:

- **Default** – This option uses service managed encryption at rest.
- **Customer managed key** – This option allows you to provide the Key ID/ARN from AWS KMS for encryption at rest.

To learn how to create AWS KMS root keys, see [Create Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_

###### Contents

- [Enabling At-Rest Encryption Using the AWS Management Console](at-rest-encryption.md#at-rest-encryption-enable-con "at-rest-encryption.md#at-rest-encryption-enable-con")
- [Enabling At-Rest Encryption Using the AWS CLI](at-rest-encryption.md#at-rest-encryption-enable-cli "at-rest-encryption.md#at-rest-encryption-enable-cli")

You can only enable at-rest encryption when you create a Valkey or Redis OSS replication group. If you
have an existing replication group on which you want to enable at-rest encryption,
do the following.

###### To enable at-rest encryption on an existing replication group

1. Create a manual backup of your existing replication group. For more information, see
   [Taking manual backups](backups-manual.md "backups-manual.md").
2. Create a new replication group by restoring from the backup. On the new replication
   group, enable at-rest encryption. For more information, see [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md").
3. Update the endpoints in your application to point to the new replication group.
4. Delete the old replication group. For more information, see [Deleting a cluster in ElastiCache](Clusters.md "Clusters.md") or [Deleting a replication group](Replication.md "Replication.md").

### Enabling At-Rest Encryption Using the AWS Management Console

All serverless caches have at-rest encryption enabled. By default, an AWS-owned KMS key is used to encrypt data. To choose your own AWS KMS key, make the following selections:

- Expand the **Default settings** section.
- Choose **Customize default settings** under **Default settings** section.
- Choose **Customize your security settings** under **Security** section.
- Choose **Customer managed CMK** under **Encryption key** setting.
- Select a key under **AWS KMS key** setting.

When designing your own cache, 'Dev/Test' and 'Production' configurations with the 'Easy create' method have at-rest encryption enabled using the **Default** key. When choosing configuration yourself, make the
following selections:

- Choose version 3.2.6, 4.0.10 or later as your engine version.
- Click the checkbox next to **Enable** for the **Encryption at rest** option.
- Choose either a **Default key** or **Customer managed CMK**.
  For the step-by-step procedure, see the following:

- [Creating a Valkey (cluster mode disabled) cluster (Console)](SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs "SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs")
- [Creating a Valkey or Redis OSS (cluster mode enabled) cluster (Console)](Clusters.md#Clusters.Create.CON.RedisCluster "Clusters.md#Clusters.Create.CON.RedisCluster")

### Enabling At-Rest Encryption Using the AWS CLI

To enable at-rest encryption when creating a Valkey or Redis OSS cluster using the AWS CLI, use the
_--at-rest-encryption-enabled_ parameter when creating a
replication group.

The following operation creates the Valkey or Redis OSS (cluster mode disabled) replication group `my-classic-rg` with
three nodes (_--num-cache-clusters_), a primary and two read
replicas. At-rest encryption is enabled for this replication group
(_--at-rest-encryption-enabled_).

The following parameters and their values are necessary to enable encryption on this replication group:

###### Key Parameters

- `--engine`—Must be `valkey` or `redis`.
- `--engine-version`—If the engine is Redis OSS, this must be 3.2.6, 4.0.10 or later.
- `--at-rest-encryption-enabled`—Required to enable at-rest encryption.

###### Example 1: Valkey or Redis OSS (Cluster Mode Disabled) Cluster with Replicas

For Linux, macOS, or Unix:

```
aws elasticache create-replication-group \
    --replication-group-id `my-classic-rg` \
    --replication-group-description `"3 node replication group"` \
    --cache-node-type `cache.m4.large` \
    `--engine `redis`` \
    `--at-rest-encryption-enabled` \
    --num-cache-clusters `3`
```

For Windows:

```
aws elasticache create-replication-group ^
    --replication-group-id `my-classic-rg` ^
    --replication-group-description `"3 node replication group"` ^
    --cache-node-type `cache.m4.large` ^
    `--engine `redis`` ^
    `--at-rest-encryption-enabled` ^
    --num-cache-clusters `3` ^
```

For additional information, see the following:

- [Creating a Valkey or Redis OSS (Cluster Mode Disabled) replication group from scratch (AWS CLI)](Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Classic.CLI "Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Classic.CLI")
- [create-replication-group](../../../cli/latest/reference/elasticache/create-replication-group.md "../../../cli/latest/reference/elasticache/create-replication-group.md")

 

The following operation creates the Valkey or Redis OSS (cluster mode enabled) replication group
`my-clustered-rg` with three node groups or shards
(_--num-node-groups_). Each has three nodes, a primary
and two read replicas (_--replicas-per-node-group_). At-rest
encryption is enabled for this replication group
(_--at-rest-encryption-enabled_).

The following parameters and their values are necessary to enable encryption on this
replication group:

###### Key Parameters

- `--engine`—Must be `valkey` or `redis`.
- `--engine-version`—If the engine is Redis OSS, this must be 4.0.10 or later.
- `--at-rest-encryption-enabled`—Required to enable at-rest encryption.
- `--cache-parameter-group`—Must be `default-redis4.0.cluster.on` or one
  derived from it to make this a cluster mode enabled replication group.

###### Example 2: A Valkey or Redis OSS (Cluster Mode Enabled) Cluster

For Linux, macOS, or Unix:

```
aws elasticache create-replication-group \
   --replication-group-id `my-clustered-rg` \
   --replication-group-description `"redis clustered cluster"` \
   --cache-node-type `cache.m3.large` \
   --num-node-groups `3` \
   --replicas-per-node-group `2` \
   `--engine `redis`` \
   `--engine-version `6.2`` \
   `--at-rest-encryption-enabled` \
   `--cache-parameter-group `default.redis6.x.cluster.on``
```

For Windows:

```
aws elasticache create-replication-group ^
   --replication-group-id `my-clustered-rg` ^
   --replication-group-description `"redis clustered cluster"` ^
   --cache-node-type `cache.m3.large` ^
   --num-node-groups `3` ^
   --replicas-per-node-group `2` ^
   `--engine `redis`` ^
   `--engine-version `6.2`` ^
   `--at-rest-encryption-enabled` ^
   `--cache-parameter-group `default.redis6.x.cluster.on``
```

For additional information, see the following:

- [Creating a Valkey or Redis OSS (Cluster Mode Enabled) replication group from scratch (AWS CLI)](Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.CLI "Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.CLI")
- [create-replication-group](../../../cli/latest/reference/elasticache/create-replication-group.md "../../../cli/latest/reference/elasticache/create-replication-group.md")

## See Also

- [Amazon VPCs and ElastiCache security](VPCs.md "VPCs.md")
- [Identity and Access Management for Amazon ElastiCache](IAM.md "IAM.md")
