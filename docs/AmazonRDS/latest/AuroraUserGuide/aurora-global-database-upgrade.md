# Upgrading an Amazon Aurora global database

Upgrading an Aurora global database follows the same procedures as upgrading Aurora DB
clusters. However, following are some important differences to take note of before you start
the process.

We recommend that you upgrade the primary and secondary DB clusters to the same version. You can only perform a managed cross-Region database failover
on an Aurora global database if the primary and secondary DB clusters have the same major, minor, and patch level engine versions. However, the patch levels can be different,
depending on the minor engine version. For more information, see [Patch level
compatibility for managed cross-Region switchovers and failovers](#aurora-global-database-upgrade.minor.incompatibility "#aurora-global-database-upgrade.minor.incompatibility").

## Major version upgrades

When you perform a major version upgrade of an Amazon Aurora global database, you upgrade
the global database cluster instead the individual clusters that it contains.

To learn how to upgrade an Aurora PostgreSQL global database to a higher major version, see [Major upgrades for
global databases](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.GlobalDB "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.GlobalDB").

###### Note

With an Aurora global database based on Aurora PostgreSQL, you can't perform a major version upgrade of the Aurora DB
engine if the recovery point objective (RPO) feature is turned on. For information about the RPO feature, see [Managing RPOs for Aurora PostgreSQL–based global databases](aurora-global-database-disaster-recovery.md#aurora-global-database-manage-recovery "aurora-global-database-disaster-recovery.md#aurora-global-database-manage-recovery").

To learn how to upgrade an Aurora MySQL global database to a higher major version, see [In-place major upgrades for global databases](AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.GlobalDB "AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.GlobalDB").

###### Note

With an Aurora global database based on Aurora MySQL, you can perform an in-place upgrade from Aurora MySQL version
2 to version 3 only if you set the `lower_case_table_names` parameter to default and you reboot your global database.

To perform a major version upgrade to Aurora MySQL version 3 when using `lower_case_table_names`, use the
following process:

1. Remove all secondary Regions from the global cluster. Follow the steps in [Removing a cluster from an Amazon Aurora global database](aurora-global-database-detaching.md "aurora-global-database-detaching.md").
2. Upgrade the engine version of the primary Region to
   Aurora MySQL version 3. Follow the steps in [How to perform an in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md").
3. Add secondary Regions to the global cluster. Follow the steps in [Adding an AWS Region to an Amazon Aurora global database](aurora-global-database-attaching.md "aurora-global-database-attaching.md").
   You can also use the snapshot restore method instead. For more information, see [Restoring from a DB cluster snapshot](aurora-restore-snapshot.md "aurora-restore-snapshot.md").

## Minor version upgrades

You can upgrade your Aurora global database to a newer minor engine version across all regions with a single managed operation and minimal downtime, eliminating the need to manually upgrade each cluster individually and reducing operational overhead for global cluster management.

### Understanding global database minor version upgrades

You can upgrade the minor version of your global database through the RDS API, AWS CLI, or AWS Management Console. This single operation orchestrates the upgrade across your primary cluster and all secondary (mirror) clusters. If issues occur during the upgrade, the service automatically rolls back to the existing version.

###### Note

This managed capability is currently supported only for Aurora PostgreSQL-compatible engines.

When you initiate a global database minor version upgrade using the `modify-global-cluster` command, you specify the target engine version, and the service coordinates the upgrade across all clusters. This upgrade is applied immediately.

For Linux, macOS, or Unix:

```
aws rds modify-global-cluster \
    --global-cluster-identifier `global_cluster_identifier` \
    --engine-version `target_engine_version`
```

For Windows:

```
aws rds modify-global-cluster ^
    --global-cluster-identifier `global_cluster_identifier` ^
    --engine-version `target_engine_version`
```

### Considerations for minor version upgrades

When planning a minor version upgrade for your global database, consider the following:

- The managed capability applies only to minor version upgrades. Patch version upgrades continue to use existing system-update maintenance actions.
- The managed capability is supported only for Aurora PostgreSQL global clusters.

You can upgrade each cluster in your global cluster topology individually. If you choose this approach, upgrade all secondary clusters before upgrading the primary cluster. When upgrading, ensure your primary and secondary DB clusters are upgraded to the same minor version and patch level. To update the patch level, apply all pending maintenance actions on the secondary cluster. To learn how to upgrade an Aurora PostgreSQL global database to a higher minor version, see
[How to perform minor
version upgrades and apply patches](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor").

### Minor version upgrades for Aurora MySQL global database

To learn how to upgrade an Aurora MySQL global database to a higher minor version, see [Upgrading Aurora MySQL by modifying the engine version](AuroraMySQL.Updates.Patching.md "AuroraMySQL.Updates.Patching.md").

Before you perform the upgrade, review the following considerations:

- Upgrading the minor version of a secondary cluster doesn't affect availability or usage of the primary cluster in any way.
- A secondary cluster must have at least one DB instance to perform a minor upgrade.
- If you upgrade an Aurora MySQL global database to version 2.11.\*, you must upgrade your primary and secondary DB clusters to exactly the same version, including the patch level.
- To support managed cross-Region switchovers or failovers, you might need to upgrade your primary and secondary DB clusters to the exact same version, including the patch level. This requirement applies to Aurora MySQL and some Aurora PostgreSQL versions. For a list of versions that allow switchovers and failovers between clusters running different patch levels, see [Patch level
  compatibility for managed cross-Region switchovers and failovers](#aurora-global-database-upgrade.minor.incompatibility "#aurora-global-database-upgrade.minor.incompatibility").

### Patch level

compatibility for managed cross-Region switchovers and failovers

If your Aurora Global Database is running one of the following minor engine
versions, you can perform managed cross-Region switchovers or failovers
even if the patch levels of your primary and secondary DB clusters don't match. For minor
engine versions lower than the ones on this list, your primary and
secondary DB clusters must be running the same major, minor, and patch levels to perform managed
cross-Region switchovers or failovers. Make sure to review the version
information and the notes in the following table when planning upgrades for your primary cluster,
secondary clusters, or both.

###### Note

For manual cross-Region failovers, you can perform the failover process as
long as the target secondary DB cluster is running the same major and minor engine
version as the primary DB cluster. In this case, the patch levels don't need to match.

If your engine versions require identical patch levels, you can perform the failover manually by following the steps in
[Performing manual failovers for Aurora global databases](aurora-global-database-disaster-recovery.md#aurora-global-database-failover.manual-unplanned "aurora-global-database-disaster-recovery.md#aurora-global-database-failover.manual-unplanned").

| Database engine   | Minor engine versions                                                                                                                                                                                               | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Aurora MySQL      | No minor versions                                                                                                                                                                                                   | None of the Aurora MySQL minor versions allow managed cross-Region switchovers or<br>failovers with differing patch levels between the primary and secondary DB clusters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Aurora PostgreSQL | • Version 15 or higher major versions<br>• Version 14.5 or higher minor versions<br>• Version 13.8 or higher minor versions<br>• Version 12.12 or higher minor versions<br>• Version 11.17 or higher minor versions | With the engine versions listed in the previous column, you can perform managed<br>cross-Region switchovers or failovers from a primary DB cluster<br>with one patch level to a secondary DB cluster with a different patch level.<br>With minor versions lower than these, you can perform managed<br>cross-Region switchovers or failovers only if the patch levels<br>of the primary and secondary DB clusters match.<br>WarningWhen you update a cluster in your global database to any of the following patch versions,<br>you won't be able to perform cross-Region switchovers or failovers until all of the<br>clusters in your global database are running one of these patch versions or a newer one.<br>• Patch versions 16.1.6, 16.2.4, 16.3.2, and 16.4.2<br>• Patch versions 15.3.8, 15.4.9, 15.5.6, 15.6.4, 15.7.2, and 15.8.2<br>• Patch versions 14.8.8, 14.9.9, 14.10.6, 14.11.4, 14.12.2, and 14.13.2 |
