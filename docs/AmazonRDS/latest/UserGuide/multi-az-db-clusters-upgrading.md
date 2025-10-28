# Upgrading the engine version of a Multi-AZ DB cluster for Amazon RDS

Amazon RDS provides newer versions of each supported database engine so that you can keep your
Multi-AZ DB cluster up to date. This topic explains the process of upgrading a Multi-AZ DB cluster to newer
versions.

Upgrading a Multi-AZ DB cluster involves selecting a new compatible engine version and planning for
potential downtime. The process ensures minimal disruption by utilizing the failover
capabilities of the Multi-AZ architecture. Best
practices include performing upgrades during low-traffic periods, testing in non-production
environments, and verifying application compatibility with the new version.

###### Topics

- [Minor version upgrades](#multi-az-db-clusters-upgrade-minor "#multi-az-db-clusters-upgrade-minor")
- [Major version upgrades](#multi-az-db-clusters-upgrade-major "#multi-az-db-clusters-upgrade-major")
- [Upgrading a Multi-AZ DB cluster](#multi-az-db-clusters-upgrade-process "#multi-az-db-clusters-upgrade-process")
- [Upgrading Multi-AZ DB cluster read
  replicas](#multi-az-db-clusters-upgrade-replicas "#multi-az-db-clusters-upgrade-replicas")
- [Monitoring Multi-AZ DB cluster upgrades with events](#multi-az-db-clusters-upgrade-monitoring "#multi-az-db-clusters-upgrade-monitoring")

## Minor version upgrades

A minor version upgrade includes only changes that are backward-compatible with
existing applications. When you initiate a minor version upgrade, Amazon RDS first upgrades
the reader DB instances one at a time. Then, one of the reader DB instances switches to be the new
writer DB instance. Amazon RDS then upgrades the old writer instance (which is now a reader
instance).

Downtime during the upgrade is limited to the time it takes for one of the reader
DB instances to become the new writer DB instance. This downtime acts like an automatic failover.
For more information, see [Failing over a Multi-AZ DB cluster for Amazon RDS](multi-az-db-clusters-concepts-failover.md "multi-az-db-clusters-concepts-failover.md"). Note
that the replica lag of your Multi-AZ DB cluster might affect the downtime. For more information, see
[Replica lag and Multi-AZ DB clusters](multi-az-db-clusters-concepts.md#multi-az-db-clusters-concepts-replica-lag "multi-az-db-clusters-concepts.md#multi-az-db-clusters-concepts-replica-lag").

For RDS for PostgreSQL Multi-AZ DB cluster read replicas, Amazon RDS upgrades the cluster member instances one
at a time. The reader and writer cluster roles don't switch during the upgrade.
Therefore, your DB cluster might experience downtime while Amazon RDS upgrades the cluster writer
instance.

###### Note

The downtime for a Multi-AZ DB cluster minor version upgrade is typically 35 seconds. When used
with RDS Proxy, you can further reduce downtime to one second or less. For more
information, see [Amazon RDS Proxy](rds-proxy.md "rds-proxy.md"). Alternately, you can use an open
source database proxy such as [ProxySQL](https://aws.amazon.com/blogs/database/achieve-one-second-or-less-of-downtime-with-proxysql-when-upgrading-amazon-rds-multi-az-deployments-with-two-readable-standbys/ "https://aws.amazon.com/blogs/database/achieve-one-second-or-less-of-downtime-with-proxysql-when-upgrading-amazon-rds-multi-az-deployments-with-two-readable-standbys/"), [PgBouncer](https://aws.amazon.com/blogs/database/fast-switchovers-with-pgbouncer-on-amazon-rds-multi-az-deployments-with-two-readable-standbys-for-postgresql/ "https://aws.amazon.com/blogs/database/fast-switchovers-with-pgbouncer-on-amazon-rds-multi-az-deployments-with-two-readable-standbys-for-postgresql/"), or the [AWS Advanced JDBC Wrapper Driver](https://aws.amazon.com/blogs/database/achieve-one-second-or-less-downtime-with-the-advanced-jdbc-wrapper-driver-when-upgrading-amazon-rds-multi-az-db-clusters/ "https://aws.amazon.com/blogs/database/achieve-one-second-or-less-downtime-with-the-advanced-jdbc-wrapper-driver-when-upgrading-amazon-rds-multi-az-db-clusters/").

## Major version upgrades

A major version upgrade can introduce changes that aren't compatible with existing
applications.

When you initiate a major version upgrade of an RDS for PostgreSQL Multi-AZ DB cluster, Amazon RDS
simultaneously upgrades the reader and writer instances. Therefore, your DB cluster might not
be available until the upgrade completes.

When you initiate a major version upgrade of an RDS for MySQL Multi-AZ DB cluster, Amazon RDS upgrades the
cluster member instances one at a time, so replication occurs from a lower engine
version to a higher one. It's important to ensure that your workload is compatible with
both the source and target engine versions during a major version upgrade, as engine
versions might differ in syntax and features.

###### Note

Like minor version upgrades, the downtime for an RDS for MySQL major version upgrade
is typically 35 seconds. When used with RDS Proxy, you can further reduce downtime to
one second or less. For more information, see [Amazon RDS Proxy](rds-proxy.md "rds-proxy.md").

## Upgrading a Multi-AZ DB cluster

The process for upgrading the engine version of a Multi-AZ DB cluster is the same as the process for
upgrading a DB instance engine version. For instructions, see [Upgrading
a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md"). The only difference is that when using
the AWS Command Line Interface (AWS CLI), you use the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") command and specify the
`--db-cluster-identifier` parameter (along with the
`--allow-major-version-upgrade` parameter).

For more information about major and minor version upgrades, see the following
documentation for your DB engine:

- [Upgrades of the RDS for PostgreSQL DB
  engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")
- [Upgrades of the RDS for MySQL DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")

## Upgrading Multi-AZ DB cluster read

replicas

Amazon RDS doesn't automatically upgrade Multi-AZ DB cluster read replicas. For
_minor_ version upgrades, you must first manually upgrade all
read replicas and then upgrade the cluster. Otherwise, the upgrade is blocked. When you
perform a _major_ version upgrade of a cluster, the replication state
of all read replicas changes to **terminated**. You must
delete and recreate the read replicas after the upgrade completes. For more information,
see [Monitoring read replication](USER_ReadRepl.md "USER_ReadRepl.md").

## Monitoring Multi-AZ DB cluster upgrades with events

When you upgrade the engine version of a Multi-AZ DB cluster, Amazon RDS emits a specific event during each phase of the process. To track the progress of an upgrade, you can view or subscribe to these events.

For more information about RDS events, see [Monitoring Amazon RDS events](working-with-events.md "working-with-events.md").

For detailed information about a specific Amazon RDS event that occurs during your engine upgrade, see [Amazon RDS event categories and event messages](USER_Events.md "USER_Events.md").
