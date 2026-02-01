# Upgrades of the RDS for MySQL DB engine

When Amazon RDS supports a new version of a database engine, you can upgrade your DB instances to the
new version. There are two kinds of upgrades for MySQL databases: major version upgrades and
minor version upgrades.

**Major version upgrades**

_Major version upgrades_ can contain database
changes that are not backward-compatible with existing applications. As a
result, you must manually perform major version upgrades of your DB instances. You can
initiate a major version upgrade by modifying your DB instance. Before you perform a
major version upgrade, we recommend that you follow the instructions in [Major version upgrades for RDS for MySQL](USER_UpgradeDBInstance.MySQL.md "USER_UpgradeDBInstance.MySQL.md").

For major version upgrades of Multi-AZ DB instance deployments, Amazon RDS simultaneously
upgrades the primary and standby replicas. Your DB instance won't be available until
the upgrade completes. For major version upgrades of Multi-AZ DB cluster deployments, Amazon RDS
upgrades the cluster member instances one at a time.

###### Tip

You can minimize the downtime required for a major version upgrade by
using a blue/green deployment. For more information, see [Using Amazon RDS Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").

**Minor version upgrades**

_Minor version upgrades_ include only changes
that are backward-compatible with existing applications. You can initiate a
minor version upgrade manually by modifying your DB instance. Or, you can enable the
**Auto minor version upgrade** option when creating or
modifying a DB instance. Doing so means that Amazon RDS automatically upgrades your DB
instance after testing and approving the new version. For information about
performing an upgrade, see [Upgrading
a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

When you perform a minor version upgrade of a Multi-AZ DB cluster, Amazon RDS upgrades the reader
DB instances one at a time. Then, one of the reader DB instances switches to be the new
writer DB instance. Amazon RDS then upgrades the old writer instance (which is now a reader
instance).

###### Note

The downtime for a minor version upgrade of a Multi-AZ DB
_instance_ deployment can last for several minutes.
Multi-AZ DB clusters typically reduce the downtime of minor version upgrades to
approximately 35 seconds. When used with RDS Proxy, you can further reduce
downtime to one second or less. For more information, see [Amazon RDS Proxy](rds-proxy.md "rds-proxy.md"). Alternately, you can use an open source database
proxy such as [ProxySQL](https://aws.amazon.com/blogs/database/achieve-one-second-or-less-of-downtime-with-proxysql-when-upgrading-amazon-rds-multi-az-deployments-with-two-readable-standbys/ "https://aws.amazon.com/blogs/database/achieve-one-second-or-less-of-downtime-with-proxysql-when-upgrading-amazon-rds-multi-az-deployments-with-two-readable-standbys/"),[PgBouncer](https://aws.amazon.com/blogs/database/fast-switchovers-with-pgbouncer-on-amazon-rds-multi-az-deployments-with-two-readable-standbys-for-postgresql/ "https://aws.amazon.com/blogs/database/fast-switchovers-with-pgbouncer-on-amazon-rds-multi-az-deployments-with-two-readable-standbys-for-postgresql/"), or the [AWS Advanced JDBC Wrapper Driver](https://aws.amazon.com/blogs/database/achieve-one-second-or-less-downtime-with-the-advanced-jdbc-wrapper-driver-when-upgrading-amazon-rds-multi-az-db-clusters/ "https://aws.amazon.com/blogs/database/achieve-one-second-or-less-downtime-with-the-advanced-jdbc-wrapper-driver-when-upgrading-amazon-rds-multi-az-db-clusters/").

Amazon RDS also supports upgrade rollout policy to manage automatic minor version
upgrades across multiple database resources and AWS accounts. For more information,
see [Using AWS Organizations upgrade rollout policy
for automatic minor version upgrades](RDS.Maintenance.AMVU.md "RDS.Maintenance.AMVU.md").

If your MySQL DB instance uses read replicas, then you must upgrade all of the read replicas
before upgrading the source instance.

###### Topics

- [Considerations for MySQL upgrades](#USER_UpgradeDBInstance.MySQL.Considerations "#USER_UpgradeDBInstance.MySQL.Considerations")
- [Finding valid upgrade targets](#USER_UpgradeDBInstance.MySQL.FindingTargets "#USER_UpgradeDBInstance.MySQL.FindingTargets")
- [MySQL version numbers](USER_UpgradeDBInstance.MySQL.md "USER_UpgradeDBInstance.MySQL.md")
- [RDS version numbers in
  RDS for MySQL](USER_UpgradeDBInstance.MySQL.rds.md "USER_UpgradeDBInstance.MySQL.rds.md")
- [Major version upgrades for RDS for MySQL](USER_UpgradeDBInstance.MySQL.md "USER_UpgradeDBInstance.MySQL.md")
- [Testing an RDS for MySQL upgrade](USER_UpgradeDBInstance.MySQL.md "USER_UpgradeDBInstance.MySQL.md")
- [Upgrading a MySQL DB instance](#USER_UpgradeDBInstance.MySQL.Upgrading "#USER_UpgradeDBInstance.MySQL.Upgrading")
- [Automatic minor version upgrades for RDS for MySQL](USER_UpgradeDBInstance.MySQL.md "USER_UpgradeDBInstance.MySQL.md")
- [Using a read replica to reduce downtime when upgrading an RDS for MySQL database](USER_UpgradeDBInstance.MySQL.md "USER_UpgradeDBInstance.MySQL.md")
- [Monitoring RDS for MySQL engine upgrades with events](USER_UpgradeDBInstance.MySQL.md "USER_UpgradeDBInstance.MySQL.md")

## Considerations for MySQL upgrades

Amazon RDS takes two or more DB snapshots during the upgrade process. Amazon RDS takes up to two
snapshots of the DB instance _before_ making any
upgrade changes. If the upgrade doesn't work for your databases, you can restore one of
these snapshots to create a DB instance running the old version. Amazon RDS takes another
snapshot of the DB instance when the upgrade completes. Amazon RDS takes these snapshots
regardless of whether AWS Backup manages the backups for the DB instance.

###### Note

Amazon RDS only takes DB snapshots
if you have set the backup retention period
for your DB instance to a number greater than 0.
To change your backup retention period, see
[Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

After the upgrade is complete, you can't revert to the previous version of the
database engine. If you want to return to the previous version, restore the first DB
snapshot taken to create a new DB instance.

You control when to upgrade your DB instance to a new version supported by Amazon RDS.
This level of control helps you maintain compatibility with specific database versions and test new
versions with your application before deploying in production.
When you are ready, you can perform version upgrades
at the times that best fit your schedule.

If your DB instance uses read replication, then you must upgrade all of the read replicas
before upgrading the source instance.

## Finding valid upgrade targets

When you use the AWS Management Console to upgrade a DB instance, it shows the valid upgrade
targets for the DB instance. You can also run the following AWS CLI command to identify
the valid upgrade targets for a DB instance:

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
  --engine mysql \
  --engine-version `version_number` \
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

For Windows:

```
aws rds describe-db-engine-versions ^
  --engine mysql ^
  --engine-version `version_number` ^
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

For example, to identify the valid upgrade targets for a MySQL version 8.0.28 DB
instance, run the following AWS CLI command:

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
  --engine mysql \
  --engine-version 8.0.28 \
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

For Windows:

```
aws rds describe-db-engine-versions ^
  --engine mysql ^
  --engine-version 8.0.28 ^
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

## Upgrading a MySQL DB instance

For information about manually or automatically upgrading a MySQL DB instance, see
[Upgrading
a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").
