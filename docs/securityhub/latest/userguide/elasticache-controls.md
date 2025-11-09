# Security Hub controls for ElastiCache

These AWS Security Hub controls evaluate the Amazon ElastiCache service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [ElastiCache.1] ElastiCache (Redis OSS) clusters should have

automatic backups enabled

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6, NIST.800-53.r5 CP-6(1), NIST.800-53.r5 CP-6(2), NIST.800-53.r5 CP-9, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-12, NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > Backups enabled

**Severity:** High

**Resource type:**
`AWS::ElastiCache::CacheCluster`, `AWS:ElastiCache:ReplicationGroup`

**AWS Config rule:**
[elasticache-redis-cluster-automatic-backup-check](../../../config/latest/developerguide/elasticache-redis-cluster-automatic-backup-check.md "../../../config/latest/developerguide/elasticache-redis-cluster-automatic-backup-check.md")

**Schedule type:** Periodic

**Parameters:**

| Parameter                 | Description                               | Type    | Allowed custom values | Security Hub default value |
| ------------------------- | ----------------------------------------- | ------- | --------------------- | -------------------------- |
| `snapshotRetentionPeriod` | Minimum snapshot retention period in days | Integer | `1` to `35`           | `1`                        |

This control evaluates whether an Amazon ElastiCache (Redis OSS) cluster has automatic backups
enabled. The control fails if the `SnapshotRetentionLimit` for the Redis OSS
cluster is less than the specified time period. Unless you provide a custom parameter
value for the snapshot retention period, Security Hub uses a default value of 1 day.

ElastiCache (Redis OSS) clusters can back up their data. You can use the backup to restore a
cluster or seed a new cluster. The backup consists of the cluster's metadata, along with
all the data in the cluster. All backups are written to Amazon S3, which provides durable
storage. You can restore your data by creating a new ElastiCache cluster and populating it
with data from a backup. You can manage backups using the AWS Management Console, the AWS CLI, and the
ElastiCache API.

###### Note

This control also evaluates ElastiCache (Redis OSS and Valkey) replication
groups.

### Remediation

For information about scheduling automatic backups for an ElastiCache cluster, see [Scheduling
automatic backups](../../../AmazonElastiCache/latest/red-ug/backups-automatic.md "../../../AmazonElastiCache/latest/red-ug/backups-automatic.md") in the _Amazon ElastiCache User Guide_.

## [ElastiCache.2] ElastiCache clusters should have automatic minor

version upgrades enabled

**Related requirements:** NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-2(2), NIST.800-53.r5 SI-2(4), NIST.800-53.r5 SI-2(5) PCI DSS v4.0.1/6.3.3

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** High

**Resource type:**
`AWS::ElastiCache::CacheCluster`

**AWS Config rule:**
[elasticache-auto-minor-version-upgrade-check](../../../config/latest/developerguide/elasticache-auto-minor-version-upgrade-check.md "../../../config/latest/developerguide/elasticache-auto-minor-version-upgrade-check.md")

**Schedule type:** Periodic

**Parameters:** None

This control evaluates whether Amazon ElastiCache automatically applies minor version upgrades to a cache cluster.
The control fails if the cache cluster doesn't have minor version upgrades automatically applied.

###### Note

This control doesn't apply to ElastiCache Memcached clusters.

Automatic minor version upgrade is a feature that you can enable in Amazon ElastiCache to automatically upgrade your
cache clusters when a new minor cache engine version is available. These upgrades might include security patches
and bug fixes. Staying up-to-date with patch installation is an important step in securing systems.

### Remediation

To automatically apply minor version upgrades to an existing ElastiCache cache cluster, see [Version management for ElastiCache](../../../AmazonElastiCache/latest/red-ug/VersionManagement.md "../../../AmazonElastiCache/latest/red-ug/VersionManagement.md") in the _Amazon ElastiCache User Guide_.

## [ElastiCache.3] ElastiCache replication groups should have

automatic failover enabled

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::ElastiCache::ReplicationGroup`

**AWS Config rule:**
[elasticache-repl-grp-auto-failover-enabled](../../../config/latest/developerguide/elasticache-repl-grp-auto-failover-enabled.md "../../../config/latest/developerguide/elasticache-repl-grp-auto-failover-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an ElastiCache replication groups has automatic failover enabled. The control fails if automatic
failover isn't enabled for a replication group.

When automatic failover is enabled for a replication group, the role of primary node will automatically fail over to one
of the read replicas. This failover and replica promotion ensure that you can resume writing to the new primary after
promotion is complete, which reduces overall downtime in case of failure.

### Remediation

To enable automatic failover for an existing ElastiCache replication group,, see [Modifying an ElastiCache cluster](../../../AmazonElastiCache/latest/red-ug/Clusters.md#Clusters.Modify.CON "../../../AmazonElastiCache/latest/red-ug/Clusters.md#Clusters.Modify.CON") in the _Amazon ElastiCache User Guide_.
If you use the ElastiCache console, set **Auto failover** to enabled.

## [ElastiCache.4] ElastiCache replication groups should be encrypted

at rest

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::ElastiCache::ReplicationGroup`

**AWS Config rule:**
[elasticache-repl-grp-encrypted-at-rest](../../../config/latest/developerguide/elasticache-repl-grp-encrypted-at-rest.md "../../../config/latest/developerguide/elasticache-repl-grp-encrypted-at-rest.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an ElastiCache replication group is encrypted at rest. The control fails if the replication
group isn't encrypted at rest.

Encrypting data at rest reduces the risk that an unauthenticated user gets access to data that is stored on disk.
ElastiCache (Redis OSS) replication groups should be encrypted at rest for an added layer of security.

### Remediation

To configure at-rest encryption on an ElastiCache replication group, see [Enabling at-rest encryption](../../../AmazonElastiCache/latest/red-ug/at-rest-encryption.md#at-rest-encryption-enable "../../../AmazonElastiCache/latest/red-ug/at-rest-encryption.md#at-rest-encryption-enable") in the _Amazon ElastiCache User Guide_.

## [ElastiCache.5] ElastiCache replication groups should be encrypted

in transit

**Related requirements:** NIST.800-53.r5 AC-17(2), NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5 SI-7(6), PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::ElastiCache::ReplicationGroup`

**AWS Config rule:**
[elasticache-repl-grp-encrypted-in-transit](../../../config/latest/developerguide/elasticache-repl-grp-encrypted-in-transit.md "../../../config/latest/developerguide/elasticache-repl-grp-encrypted-in-transit.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an ElastiCache replication group is encrypted in transit. The control fails if the
replication group isn't encrypted in transit.

Encrypting data in transit reduces the risk that an unauthorized user can eavesdrop on network traffic.
Enabling encryption in transit on an ElastiCache replication group encrypts your data whenever it's moving from one place
to another, such as between nodes in your cluster or between your cluster and your application.

### Remediation

To configure in-transit encryption on an ElastiCache replication group, see [Enabling in-transit encryption](../../../AmazonElastiCache/latest/red-ug/in-transit-encryption.md "../../../AmazonElastiCache/latest/red-ug/in-transit-encryption.md") in the _Amazon ElastiCache User Guide_.

## [ElastiCache.6] ElastiCache (Redis OSS) replication groups of earlier versions

should have Redis OSS AUTH enabled

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6, PCI DSS v4.0.1/8.3.1

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**
`AWS::ElastiCache::ReplicationGroup`

**AWS Config rule:**
[elasticache-repl-grp-redis-auth-enabled](../../../config/latest/developerguide/elasticache-repl-grp-redis-auth-enabled.md "../../../config/latest/developerguide/elasticache-repl-grp-redis-auth-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an ElastiCache (Redis OSS) replication group has Redis OSS AUTH enabled. The control fails if the Redis OSS
version of the replication group nodes is below 6.0 and `AuthToken` isn't in use.

When you use Redis authentication tokens, or passwords, Redis requires a password before allowing clients to run
commands, which improves data security. For Redis 6.0 and later versions, we recommend using Role-Based Access Control
(RBAC). Since RBAC is not supported for Redis versions earlier than 6.0, this control only evaluates versions which can't
use the RBAC feature.

### Remediation

To use Redis AUTH on an ElastiCache (Redis OSS) replication group, see [Modifying the AUTH token on an existing ElastiCache (Redis OSS) cluster](../../../AmazonElastiCache/latest/red-ug/auth.md#auth-modifyng-token "../../../AmazonElastiCache/latest/red-ug/auth.md#auth-modifyng-token") in the _Amazon ElastiCache User Guide_.

## [ElastiCache.7] ElastiCache clusters should not use the default

subnet group

**Related requirements:** NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(5)

**Category:** Protect > Secure network configuration

**Severity:** High

**Resource type:**
`AWS::ElastiCache::CacheCluster`

**AWS Config rule:**
[elasticache-subnet-group-check](../../../config/latest/developerguide/elasticache-subnet-group-check.md "../../../config/latest/developerguide/elasticache-subnet-group-check.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an ElastiCache cluster is configured with a custom subnet group. The control fails if
`CacheSubnetGroupName` for an ElastiCache cluster has the value `default`.

When launching an ElastiCache cluster, a default subnet group is created if one doesn't exist already. The default
group uses subnets from the default Virtual Private Cloud (VPC). We recommend using custom subnet groups that are
more restrictive of the subnets that the cluster resides in, and the networking that the cluster inherits from the subnets.

### Remediation

To create a new subnet group for an ElastiCache cluster, see [Creating a subnet group](../../../AmazonElastiCache/latest/red-ug/SubnetGroups.md "../../../AmazonElastiCache/latest/red-ug/SubnetGroups.md") in the _Amazon ElastiCache User Guide_.
