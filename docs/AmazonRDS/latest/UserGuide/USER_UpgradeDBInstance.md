# Upgrades of the MariaDB DB engine

When Amazon RDS supports a new version of a database engine, you can upgrade your DB instances
to the new version. There are two kinds of upgrades for MariaDB DB instances: major
version upgrades and minor version upgrades.

_Major version upgrades_ can contain database changes
that are not backward-compatible with existing applications. As a result, you must manually
perform major version upgrades of your DB instances. You can initiate a major version
upgrade by modifying your DB instance. However, before you perform a major version upgrade,
we recommend that you follow the instructions in [Major version upgrades for RDS for MariaDB](USER_UpgradeDBInstance.MariaDB.md "USER_UpgradeDBInstance.MariaDB.md").

In contrast, _minor version upgrades_ include only changes that are
backward-compatible with existing applications. You can initiate a minor version upgrade
manually by modifying your DB instance. Or you can enable the **Auto minor version
upgrade** option when creating or modifying a DB instance. Doing so means that
your DB instance is automatically upgraded after Amazon RDS tests and approves the new version.
For information about performing an upgrade, see [Upgrading
a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

If your MariaDB DB instance is using read replicas, you must upgrade all of the read
replicas before upgrading the source instance. If your DB instance is in a Multi-AZ
deployment, both the writer and standby replicas are upgraded. Your DB instance might not be
available until the upgrade is complete.

For more information about MariaDB supported versions and version management, see
[MariaDB on Amazon RDS versions](MariaDB.Concepts.md "MariaDB.Concepts.md").

Database engine upgrades require downtime. The duration of the downtime varies based
on the size of your DB instance.

Amazon RDS also supports upgrade rollout policy to manage automatic minor version upgrades
across multiple database resources and AWS accounts. For more information,
see [Using AWS Organizations upgrade rollout policy
for automatic minor version upgrades](RDS.Maintenance.AMVU.md "RDS.Maintenance.AMVU.md").

###### Tip

You can minimize the downtime required for DB instance upgrade by using a blue/green deployment. For more information,
see [Using Amazon RDS Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").

###### Topics

- [Considerations for MariaDB upgrades](#USER_UpgradeDBInstance.MariaDB.Considerations "#USER_UpgradeDBInstance.MariaDB.Considerations")
- [Finding valid upgrade targets](#USER_UpgradeDBInstance.MariaDB.FindingTargets "#USER_UpgradeDBInstance.MariaDB.FindingTargets")
- [MariaDB version
  numbers](USER_UpgradeDBInstance.MariaDB.md "USER_UpgradeDBInstance.MariaDB.md")
- [RDS version numbers in RDS for MariaDB](USER_UpgradeDBInstance.MariaDB.rds.md "USER_UpgradeDBInstance.MariaDB.rds.md")
- [Major version upgrades for RDS for MariaDB](USER_UpgradeDBInstance.MariaDB.md "USER_UpgradeDBInstance.MariaDB.md")
- [Upgrading a MariaDB DB instance](#USER_UpgradeDBInstance.MariaDB.Upgrading "#USER_UpgradeDBInstance.MariaDB.Upgrading")
- [Automatic minor version upgrades for RDS for MariaDB](USER_UpgradeDBInstance.MariaDB.md "USER_UpgradeDBInstance.MariaDB.md")
- [Using a read replica to reduce downtime when upgrading an RDS for MariaDB database](USER_UpgradeDBInstance.MariaDB.md "USER_UpgradeDBInstance.MariaDB.md")
- [Monitoring RDS for MariaDB DB engine upgrades with events](USER_UpgradeDBInstance.MariaDB.md "USER_UpgradeDBInstance.MariaDB.md")

## Considerations for MariaDB upgrades

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

After the upgrade is complete,
you can't revert to the previous version of the database engine.
If you want to return to the previous version,
restore the first DB snapshot taken to create a new DB instance.

You control when to upgrade your DB instance to a new version supported by Amazon RDS.
This level of control helps you maintain compatibility with specific database versions and test new
versions with your application before deploying in production.
When you are ready, you can perform version upgrades
at the times that best fit your schedule.

If your DB instance is using read replication, you must upgrade all of the Read
Replicas before upgrading the source instance.

If your DB instance is in a Multi-AZ deployment,
both the primary and standby DB instances are upgraded.
The primary and standby DB instances are upgraded
at the same time and you will experience
an outage until the upgrade is complete.
The time for the outage varies based on your database engine,
engine version, and the size of your DB instance.

## Finding valid upgrade targets

When you use the AWS Management Console to upgrade a DB instance, it shows the valid upgrade targets for the
DB instance. You can also run the following AWS CLI command to identify the valid upgrade targets for a DB instance:

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
  --engine mariadb \
  --engine-version `version_number` \
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

For Windows:

```
aws rds describe-db-engine-versions ^
  --engine mariadb ^
  --engine-version `version_number` ^
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

For example, to identify the valid upgrade targets for a MariaDB version 10.5.17 DB
instance, run the following AWS CLI command:

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
  --engine mariadb \
  --engine-version 10.5.17 \
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

For Windows:

```
aws rds describe-db-engine-versions ^
  --engine mariadb ^
  --engine-version 10.5.17 ^
  --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

## Upgrading a MariaDB DB instance

For information about manually or automatically upgrading a MariaDB DB instance, see
[Upgrading
a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").
