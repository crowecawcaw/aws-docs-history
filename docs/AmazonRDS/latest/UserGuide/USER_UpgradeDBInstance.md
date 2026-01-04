# Upgrades of the RDS for PostgreSQL DB

engine

There are two types of upgrades that you can manage for your PostgreSQL
database:

- Operating system updates – Occasionally, Amazon RDS might need to
  update the underlying operating system of your database to apply
  security fixes or OS changes. You can decide when Amazon RDS applies OS
  updates by using the RDS console, AWS Command Line Interface (AWS CLI), or RDS API. For
  more information about OS updates, see [Applying updates to a DB instance](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.OSUpgrades "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.OSUpgrades").
- Database engine upgrades – When Amazon RDS supports a new version
  of a database engine, you can upgrade your databases to the new
  version.
  A _database_ in this context is an RDS for PostgreSQL DB instance or
  Multi-AZ DB cluster.

There are two kinds of engine upgrades for PostgreSQL databases: major version
upgrades and minor version upgrades.

**Major version upgrades**

_Major version upgrades_ can
contain database changes that are not backward-compatible
with existing applications. As a result, you must manually
perform major version upgrades of your databases. You can
initiate a major version upgrade by modifying your DB instance or
Multi-AZ DB cluster. Before you perform a major version upgrade, we
recommend that you follow the steps described in [Choosing a
major version for an RDS for PostgreSQL upgrade](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md").

Amazon RDS handles Multi-AZ major version upgrades in the following
ways:

- **Multi-AZ DB instance
  deployment** – Amazon RDS
  simultaneously upgrades the primary and any
  standby instances. Your database might not be
  available for several minutes while the upgrade
  completes.
- **Multi-AZ DB cluster
  deployment** – Amazon RDS
  simultaneously upgrades the reader and writer
  instances. Your database might not be available
  for several minutes while the upgrade completes.

If you upgrade a DB instance that has in-Region read
replicas, Amazon RDS upgrades the replicas along with the primary
DB instance.

Amazon RDS doesn't upgrade Multi-AZ DB cluster read replicas. If you perform a
major version upgrade of a Multi-AZ DB cluster, then the replication state
of its read replicas changes to
**terminated**. You must manually
delete and recreate the read replicas after the upgrade
completes.

###### Tip

You can minimize the downtime required for a major
version upgrade by using a blue/green deployment.
For more information, see [Using Amazon RDS Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").

**Minor version upgrades**

In contrast, _minor version upgrades_
include only changes that are backward-compatible with
existing applications. You can initiate a minor version
upgrade manually by modifying your database. Or, you can
enable the **Auto minor version upgrade**
option when you create or modify a database. Doing so means
that Amazon RDS automatically upgrades your database after
testing and approving the new version.

Amazon RDS handles Multi-AZ minor version upgrades in the following
ways:

- **Multi-AZ DB instance
  deployment** – Amazon RDS
  simultaneously upgrades the primary and any
  standby instances. Your database might not be
  available for several minutes while the upgrade
  completes.
- **Multi-AZ DB cluster
  deployment** – Amazon RDS upgrades the
  reader DB instances one at a time. Then, one of the
  reader DB instances switches to be the new writer DB instance.
  Amazon RDS then upgrades the old writer instance (which
  is now a reader instance). Multi-AZ DB clusters typically reduce
  the downtime of minor version upgrades to
  approximately 35 seconds. When used with RDS Proxy,
  they can further reduce downtime to one second or
  less. For more information, see [Amazon RDS Proxy](rds-proxy.md "rds-proxy.md"). Alternately, you can use an
  open source database proxy such as [ProxySQL](https://aws.amazon.com/blogs/database/achieve-one-second-or-less-of-downtime-with-proxysql-when-upgrading-amazon-rds-multi-az-deployments-with-two-readable-standbys/ "https://aws.amazon.com/blogs/database/achieve-one-second-or-less-of-downtime-with-proxysql-when-upgrading-amazon-rds-multi-az-deployments-with-two-readable-standbys/"), [PgBouncer](https://aws.amazon.com/blogs/database/fast-switchovers-with-pgbouncer-on-amazon-rds-multi-az-deployments-with-two-readable-standbys-for-postgresql/ "https://aws.amazon.com/blogs/database/fast-switchovers-with-pgbouncer-on-amazon-rds-multi-az-deployments-with-two-readable-standbys-for-postgresql/"), or the [AWS Advanced JDBC Wrapper
  Driver](https://aws.amazon.com/blogs/database/achieve-one-second-or-less-downtime-with-the-advanced-jdbc-wrapper-driver-when-upgrading-amazon-rds-multi-az-db-clusters/ "https://aws.amazon.com/blogs/database/achieve-one-second-or-less-downtime-with-the-advanced-jdbc-wrapper-driver-when-upgrading-amazon-rds-multi-az-db-clusters/").

If your database has read replicas, you must first upgrade all
of the read replicas before you upgrade the source instance
or cluster.

For more information, see [Automatic minor
version upgrades for RDS for PostgreSQL](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md"). For information about manually performing a minor
version upgrade, see [Manually upgrading the engine version](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual").

For more information about database engine versions and the policy for deprecating
database engine versions, see [Database Engine Versions](https://aws.amazon.com/rds/faqs/#Database_Engine_Versions "https://aws.amazon.com/rds/faqs/#Database_Engine_Versions") in
the Amazon RDS FAQs.

###### Topics

- [Considerations for PostgreSQL upgrades](#USER_UpgradeDBInstance.PostgreSQL.Considerations "#USER_UpgradeDBInstance.PostgreSQL.Considerations")
- [Finding
  valid upgrade targets](#USER_UpgradeDBInstance.PostgreSQL.FindingTargets "#USER_UpgradeDBInstance.PostgreSQL.FindingTargets")
- [PostgreSQL
  version numbers](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md")
- [RDS version
  numbers in RDS for PostgreSQL](USER_UpgradeDBInstance.PostgreSQL.rds.md "USER_UpgradeDBInstance.PostgreSQL.rds.md")
- [Choosing a
  major version for an RDS for PostgreSQL upgrade](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md")
- [How
  to perform a major version upgrade for RDS for PostgreSQL](USER_UpgradeDBInstance.PostgreSQL.MajorVersion.md "USER_UpgradeDBInstance.PostgreSQL.MajorVersion.md")
- [Automatic minor
  version upgrades for RDS for PostgreSQL](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md")
- [Upgrading PostgreSQL extensions in RDS for PostgreSQL databases](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md")
- [Monitoring RDS for PostgreSQL engine upgrades with events](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md")

## Considerations for PostgreSQL upgrades

To safely upgrade your databases, Amazon RDS uses the `pg_upgrade`
utility described in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/pgupgrade.html "https://www.postgresql.org/docs/current/pgupgrade.html")

If your backup retention period is greater than 0, Amazon RDS takes two DB
snapshots during the upgrade process. The first DB snapshot is of the
database before any upgrade changes have been made. If the upgrade fails for
your databases, you can restore this snapshot to create a database running
the old version. The second DB snapshot is taken after the upgrade
completes. These DB snapshots are deleted automatically once the backup
retention period expires.

###### Note

Amazon RDS takes DB snapshots during the upgrade process only if you have
set the backup retention period for your database to a number
greater than 0. To change the backup retention period for a DB instance,
see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md"). You can't
configure a custom backup retention period for a Multi-AZ DB cluster.

When you perform a major version upgrade of a DB instance, any
in-Region read replicas are also automatically upgraded.
After the upgrade workflow starts, the read replicas wait for the
`pg_upgrade` to complete successfully on the primary
DB instance. Then the primary DB instance upgrade waits for the read replica upgrades to
complete. You experience an outage until the upgrade is complete. When you
perform a major version upgrade of a Multi-AZ DB cluster, the replication state of its
read replicas changes to **terminated**.

After an upgrade is complete, you can't revert to the previous version of
the DB engine. If you want to return to the previous version, restore the DB
snapshot that was taken before the upgrade to create a new database.

## Finding

valid upgrade targets

When you use the AWS Management Console to upgrade a database, it shows the valid upgrade
targets for the database. You can also use the following AWS CLI command to
identify the valid upgrade targets for a database:

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
  --engine postgres \
  --engine-version `version-number` \
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

For Windows:

```
aws rds describe-db-engine-versions ^
  --engine postgres ^
  --engine-version `version-number` ^
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

For example, to identify the valid upgrade targets for a PostgreSQL version
16.1 database, run the following AWS CLI command:

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
  --engine postgres \
  --engine-version 16.1 \
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

For Windows:

```
aws rds describe-db-engine-versions ^
  --engine postgres ^
  --engine-version 16.1 ^
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```
