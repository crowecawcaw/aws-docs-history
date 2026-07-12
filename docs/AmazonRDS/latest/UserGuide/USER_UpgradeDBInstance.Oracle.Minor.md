# Oracle minor version upgrades

In RDS for Oracle, a minor version upgrade is an update to a major DB engine version. In RDS, a
minor engine version is a Release Update (RU), a Supplemental Patch Bundle (SPB), or, for
Oracle Database 26ai, an RU paired with a Monthly Recommended Patch (MRP). For example, if your DB instance
runs major version Oracle Database 19c and minor version
19.0.0.0.ru-2025-10.rur-2025-10.r1, you can upgrade your DB engine to minor version
19.0.0.0.ru-2026-01.rur-2026-01.r1. RDS for Oracle doesn't support minor version
downgrades.

You can upgrade your DB engine to a minor version manually or automatically. To learn how to
upgrade manually, see [Manually upgrading the engine version](USER_UpgradeDBInstance.Upgrading.md#USER_UpgradeDBInstance.Upgrading.Manual "USER_UpgradeDBInstance.Upgrading.md#USER_UpgradeDBInstance.Upgrading.Manual"). To learn how to configure
automatic upgrades, see [Automatically upgrading the minor engine version](USER_UpgradeDBInstance.Upgrading.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades "USER_UpgradeDBInstance.Upgrading.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades"). Whether you
upgrade manually or automatically, a minor version upgrade entails downtime. Consider this
downtime when you plan your upgrades.

Amazon RDS also supports upgrade rollout policy to manage automatic minor version upgrades
across multiple database resources and AWS accounts. For more information,
see [Using AWS Organizations upgrade rollout policy for automatic minor version upgrades](RDS.Maintenance.AMVU.UpgradeRollout.md "RDS.Maintenance.AMVU.UpgradeRollout.md").

###### Important

Make sure that you thoroughly test any upgrade to verify that your applications work
correctly before applying the upgrade to your production databases. For more
information, see [Testing an Oracle DB upgrade](USER_UpgradeDBInstance.Oracle.UpgradeTesting.md "USER_UpgradeDBInstance.Oracle.UpgradeTesting.md").

###### Topics

- [Release Updates (RUs) and Supplemental Patch Bundles (SPBs)](#RUs-and-SPBs "#RUs-and-SPBs")
- [Release updates and monthly recommended patches](#RUs-and-MRPs "#RUs-and-MRPs")
- [Turning on automatic minor version upgrades for Oracle](#oracle-minor-version-upgrade-tuning-on "#oracle-minor-version-upgrade-tuning-on")
- [Using AWS Organizations upgrade rollout policy for automatic minor version upgrades](#oracle-minor-version-upgrade-rollout "#oracle-minor-version-upgrade-rollout")
- [Notification of automatic minor version upgrades in RDS for Oracle](#oracle-minor-version-upgrade-advance "#oracle-minor-version-upgrade-advance")
- [How Amazon RDS schedules automatic minor version upgrades](#oracle-minor-version-upgrade-scheduled "#oracle-minor-version-upgrade-scheduled")
- [Managing an automatic minor version upgrade in RDS for Oracle](#oracle-minor-version-upgrade-managing "#oracle-minor-version-upgrade-managing")

## Release Updates (RUs) and Supplemental Patch Bundles (SPBs)

In RDS, a release update (RU) is a quarterly minor engine version that includes
security fixes, bug fixes, and new features for Oracle Database. A Supplemental Patch
Bundle (SPB) is an RU engine version that includes additional database patches
recommended by Oracle for specific use cases, such as Oracle Spatial, Oracle Data Pump,
and Oracle GoldenGate. For example, the SPB named
19.0.0.0.ru-2026-04.spb-1.r1 includes all patches in the corresponding RU
19.0.0.0.ru-2026-04.rur-2026-04.r1 plus supplemental patches. SPBs are supported only
for Oracle Database 19c.

When your instance is configured for automatic minor version upgrades, RUs and SPBs
are on separate upgrade paths. Typically, an SPB is released 2–3 weeks after its
corresponding RU. The following table shows sample minor versions for Oracle Database
19c.

| Standard RU upgrade path           | SPB upgrade path             |
| ---------------------------------- | ---------------------------- |
| 19.0.0.0.ru-2025-01.rur-2025-01.r1 | 19.0.0.0.ru-2025-01.spb-1.r1 |
| 19.0.0.0.ru-2025-04.rur-2025-04.r1 | 19.0.0.0.ru-2025-04.spb-1.r1 |
| 19.0.0.0.ru-2025-07.rur-2025-07.r1 | 19.0.0.0.ru-2025-07.spb-1.r1 |
| 19.0.0.0.ru-2025-10.rur-2025-10.r1 | 19.0.0.0.ru-2025-10.spb-1.r1 |

If your DB instance is configured for automatic upgrades, your instance is on the upgrade
path corresponding to your current version. For example, if your DB instance runs version
19.0.0.0.ru-2026-04.rur-2026-04.r1, then when 19.0.0.0.ru-2026-07.rur-2026-07.r1 is
released, your instance automatically upgrades to this RU. Similarly, if your DB instance runs
19.0.0.0.ru-2026-04.spb-1.r1, then when 19.0.0.0.ru-2026-07.spb-1.r1 is released, your
instance automatically upgrades to this SPB. An instance running
19.0.0.0.ru-2026-04.rur-2026-04.r1, which is an RU, won't automatically upgrade to
19.0.0.0.ru-2026-07.spb-1.r1, which is an SPB on a separate upgrade path.

You can upgrade your DB instance to SPBs even if your instance doesn't currently have use
cases such as Oracle Spatial, Oracle Data Pump, and Oracle GoldenGate. You can upgrade
manually from an RU to an SPB at the same engine version or higher. For example, you
can upgrade your instance from 19.0.0.0.ru-2026-04.rur-2026-04.r1 to either of the
following engine versions:

- 19.0.0.0.ru-2026-04.spb-1.r1
- 19.0.0.0.ru-2026-07.spb-1.r1

You can upgrade your instance from an SPB to an RU only if the RU is a higher
engine version. For example, you can upgrade from SPB version
19.0.0.0.ru-2026-04.spb-1.r1 to a higher RU version 19.0.0.0.ru-2026-07.rur-2026-07.r1
but not to the same RU version 19.0.0.0.ru-2026-04.rur-2026-04.r1.

If your DB instance is configured for automatic minor version upgrades, and you manually
upgrade from an RU to an SPB or from an SPB to an RU, your automatic upgrade path
changes. Suppose that you manually upgrade from RU version
19.0.0.0.ru-2026-04.rur-2026-04.r1 to SPB version 19.0.0.0.ru-2026-04.spb-1.r1. Your
next automatic minor version upgrade will be to SPB version
19.0.0.0.ru-2026-07.spb-1.r1.

Because SPBs function as RUs, the RDS APIs for upgrading your instance to RUs
and SPBs are identical. The following commands demonstrate upgrading to an RU
and to an SPB.

```
aws rds modify-db-instance \
    --db-instance-identifier mydbinstance \
    --engine-version 19.0.0.0.ru-2026-04.rur-2026-04.r1

aws rds modify-db-instance \
    --db-instance-identifier mydbinstance \
    --engine-version 19.0.0.0.ru-2026-04.spb-1.r1
```

For more information about how SPBs work with Oracle Spatial, see [How Supplemental Patch Bundles (SPBs) work](Oracle.Options.Spatial.md#Oracle.Options.Spatial.SPBs "Oracle.Options.Spatial.md#Oracle.Options.Spatial.SPBs").
For supported RUs and SPBs for Oracle Database 19c, see [Amazon RDS for
Oracle Database 19c (19.0.0.0)](../OracleReleaseNotes/oracle-version-19-0.md "../OracleReleaseNotes/oracle-version-19-0.md"). For supported RUs, MRPs, and SPBs for Oracle Database 26ai, see
[Amazon RDS
for Oracle Database 26ai (26.0.0.0)](../OracleReleaseNotes/oracle-version-26-0.md "../OracleReleaseNotes/oracle-version-26-0.md").

###### Note

Spatial Patch Bundle has been renamed to Supplemental Patch Bundle (SPB). SPBs
now include additional bundle patches beyond Oracle Spatial such as Data Pump and
GoldenGate. The abbreviation "SPB" remains unchanged. All existing SPB engine
versions continue to work as before.

## Release updates and monthly recommended patches

RDS for Oracle releases new minor engine versions of Oracle Database 26ai (26.0.0.0) quarterly. Each
Oracle Database 26ai engine version includes an RU component and an MRP component. An RU includes
the patches that Oracle releases for the specified quarter. An MRP includes a Critical
Security Patch Update and other fixes that Oracle recommends.

An Oracle Database 26ai engine version uses the following format:
``release`.ru-`ru-date`.mrp-`mrp-date`.r`rnumber``.
The format includes the following components:

`release`

The major release number.

`ru-date`

The RU date.

`mrp-date`

The MRP date.

`rnumber`

The revision number.

For example, the January 2026 quarterly RU is named
`26.0.0.0.ru-2026-01.mrp-2026-01.r1`.

Oracle can release an MRP in the months between quarterly RUs. A new MRP advances
the MRP component of the engine version, while the RU component stays the same. For
example, `26.0.0.0.ru-2026-01.mrp-2026-03.r1` includes the January 2026 RU
plus the March 2026 MRP.

Oracle doesn't release an MRP for every month. If a month has no new recommended
fixes or Critical Security Patch Update for the RU, Oracle doesn't release an MRP for
that month.

RDS for Oracle supports MRPs only for the latest RU. To get the latest security fixes for
an earlier RU, upgrade your DB instance to the latest RU.

You can upgrade to any higher Oracle Database 26ai engine version. The upgrade can be a new
quarterly RU, a new MRP, or both. RDS for Oracle doesn't support minor version downgrades.
For more information about supported RUs and MRPs for Oracle Database 26ai, see [Amazon RDS for
Oracle Database 26ai (26.0.0.0)](../OracleReleaseNotes/oracle-version-26-0.md "../OracleReleaseNotes/oracle-version-26-0.md").

## Turning on automatic minor version upgrades for Oracle

###### Manual upgrades for MRPs

For Oracle Database 26ai, automatic minor version upgrades apply new quarterly RUs but don't
apply MRPs. To upgrade a DB instance to a new MRP, apply the upgrade
manually.

In an automatic minor version upgrade, RDS applies the latest available minor version
to your Oracle database without manual intervention. An Amazon RDS for Oracle DB instance schedules
your upgrade during the next maintenance window in the following circumstances:

- Your DB instance has the **Auto minor version upgrade** option
  turned on.
- Your DB instance isn't already running the latest minor DB engine version.

To learn how to turn on automatic upgrades, see [Automatically upgrading the minor engine version](USER_UpgradeDBInstance.Upgrading.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades "USER_UpgradeDBInstance.Upgrading.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades").

## Using AWS Organizations upgrade rollout policy for automatic minor version upgrades

Amazon RDS for Oracle supports AWS Organizations upgrade rollout policy to manage automatic minor version upgrades
across multiple database resources and AWS accounts. This policy eliminates the operational overhead
of coordinating automatic minor version upgrades either manually or through custom tools, while ensuring
upgrades are first applied in non-production environments before being rolled out to production.
When a new minor engine version becomes available, Amazon RDS upgrades your DB instances based on their
configured upgrade rollout order:

| Upgrade Rollout Order | Typical Use Case                                 | When Upgrade Begins                             |
| --------------------- | ------------------------------------------------ | ----------------------------------------------- |
| First                 | Development and Test Environments                | Earliest<br>• ideal for validating new versions |
| Second                | Staging and Non-critical Production Environments | After "First" phase completes                   |
| Last                  | Critical Production Environments                 | After "Second" phase completes                  |

###### Important

If you do not configure an upgrade rollout order for your DB instance, it defaults to second.

For detailed information about phase timing and duration, see [How Amazon RDS schedules automatic minor version upgrades](#oracle-minor-version-upgrade-scheduled "#oracle-minor-version-upgrade-scheduled"). For information about configuring upgrade rollout policies
in AWS Organizations, see [Using AWS Organizations upgrade rollout policy for automatic minor version upgrades](RDS.Maintenance.AMVU.UpgradeRollout.md "RDS.Maintenance.AMVU.UpgradeRollout.md").

## Notification of automatic minor version upgrades in RDS for Oracle

If automatic minor version upgrade is enabled on your DB instance, RDS for Oracle
creates pending maintenance actions to notify you before applying upgrades. You can view these
pending maintenance actions on the **Maintenance & backups** tab of your
database details page in the Amazon RDS console.

When a new minor version becomes available, RDS for Oracle publishes an early
notification (pending maintenance action). The early notification has the following format:

```
An automatic minor version upgrade to `engine-version` will be applied during your maintenance window on `apply-date` based on the upgrade rollout order `rollout-order`. You can change the upgrade rollout order or apply this upgrade manually at any time before the scheduled date through the AWS console or AWS CLI.
```

`apply-date` in the early notification is the date when Amazon RDS
will upgrade your DB instance. `rollout-order` is your upgrade rollout order
(first, second, or last). If you have not configured an upgrade rollout policy, this value is second
by default. For more information, see [Using AWS Organizations upgrade rollout policy for automatic minor version upgrades](RDS.Maintenance.AMVU.UpgradeRollout.md "RDS.Maintenance.AMVU.UpgradeRollout.md").

When the upgrade rollout phase begins, the pending maintenance action message changes to the following format:

```
Automatic minor version upgrade to `engine-version`
```

This message indicates that the upgrade has been scheduled and will be applied during your maintenance window
on the scheduled apply date. You can check the scheduled apply date on the **Maintenance & backups** tab of your database
details page in the Amazon RDS console or in the `CurrentApplyDate` field of the
`describe-pending-maintenance-actions` API response.

The following example shows you can get the details about pending maintenance actions by using the
`describe-pending-maintenance-actions` command in the AWS CLI:

```
aws rds describe-pending-maintenance-actions

    "PendingMaintenanceActions": [
        {
            "ResourceIdentifier": "arn:aws:rds:us-east-1:123456789012:db:orclinst1",
            "PendingMaintenanceActionDetails": [
                {
                    "Action": "db-upgrade",
                    "Description": "Automatic minor version upgrade to 21.0.0.0.ru-2024-07.rur-2024-07.r1",
                    "CurrentApplyDate": "2024-12-02T08:10:00Z"
                }
            ]
        }, ...
```

For more information about [describe-pending-maintenance-actions](../../../cli/latest/reference/rds/describe-pending-maintenance-actions.md "../../../cli/latest/reference/rds/describe-pending-maintenance-actions.md"), see the _AWS CLI Command
Reference_.

## How Amazon RDS schedules automatic minor version upgrades

When you use AWS Organizations upgrade rollout policy, Amazon RDS upgrades DB instances in phases based on their configured
rollout order. This section describes the timing and duration of each phase.

**Phase 0: Early Notification**

When RDS for Oracle releases a new minor version (typically 3 to 4 weeks after Oracle's quarterly RU release), all DB
instances with auto minor version upgrade enabled receive an early notification. This notification appears on the **Maintenance & backups**
tab of the database details page in the Amazon RDS console and in the `describe-pending-maintenance-actions` API response. The early
notification phase lasts 2 weeks. During this phase, no automatic upgrades occur.

**Phase 1: Upgrade Rollout Order First**

At the end of the early notification phase, RDS for Oracle begins upgrading DB instances with the upgrade rollout order first.
This phase lasts 2 to 3 weeks for the January, April, July quarterly minor versions, and 7 to 8 weeks for the October quarterly minor version.
The extended period for the October minor version provides sufficient time to test the new minor version during the year-end holiday season.
New DB instances created during this phase with the upgrade rollout order first will be upgraded automatically.

**Phase 2: Upgrade Rollout Order Second**

At the end of phase 1, RDS for Oracle begins upgrading DB instances with upgrade rollout order second. This phase lasts 2 weeks
for all quarterly minor versions. New DB instances created with upgrade rollout order first or second during this phase will be upgraded automatically.

**Phase 3: Upgrade Rollout Order Last**

At the end of Phase 2, RDS for Oracle begins upgrading DB instances with upgrade rollout order last. This phase lasts until the next quarterly
minor version release. New DB instances created with upgrade rollout order first, second, or last during this phase will be upgraded automatically.

| Phase                                 | When it starts                                   | Duration                                                                                   | Pending maintenance action message                                                                                                                                                                                                                                                                                          |
| ------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Phase 0: Early Notification           | When RDS for Oracle releases a new minor version | 2 weeks                                                                                    | An automatic minor version upgrade to `engine-version` will be applied during your maintenance window on `apply-date` based on the upgrade rollout order `rollout-order`. You can change the upgrade rollout order or apply this upgrade manually at any time before the scheduled date through the AWS console or AWS CLI. |
| Phase 1: Upgrade Rollout Order First  | End of early notification phase                  | 2 to 4 weeks for January/April/July minor versions, 7 to 9 weeks for October minor version | Automatic minor version upgrade to `engine-version`                                                                                                                                                                                                                                                                         |
| Phase 2: Upgrade Rollout Order Second | End of Phase 1                                   | 2 weeks                                                                                    | Automatic minor version upgrade to `engine-version`                                                                                                                                                                                                                                                                         |
| Phase 3: Upgrade Rollout Order Last   | End of Phase 2                                   | Until the next quarterly minor version release                                             | Automatic minor version upgrade to `engine-version`                                                                                                                                                                                                                                                                         |

## Managing an automatic minor version upgrade in RDS for Oracle

When auto minor version upgrade is enabled on your DB instance, Amazon RDS automatically upgrades your DB instance to the
latest minor version during your maintenance window. However, you can choose to apply the upgrade manually before the scheduled
date using the AWS CLI or on the **Maintenance & backups** tab of the database details page.

To upgrade your DB instance immediately instead of waiting for the scheduled maintenance window:

```
aws rds apply-pending-maintenance-action \
    --resource-identifier arn:aws:rds:us-east-1:123456789012:db:orclinst1 \
    --apply-action db-upgrade \
    --opt-in-type immediate
```

To apply the upgrade during your next maintenance window instead of the scheduled apply date:

```
aws rds apply-pending-maintenance-action \
    --resource-identifier arn:aws:rds:us-east-1:123456789012:db:orclinst1 \
    --apply-action db-upgrade \
    --opt-in-type next-maintenance
```

To opt out of an automatic minor version upgrade, modify your DB instance and turn off the automatic minor version upgrade option.
This unschedules any pending automatic upgrade.

To learn more about how to turn off automatic minor version upgrade, see [Automatically upgrading the minor engine version](USER_UpgradeDBInstance.Upgrading.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades "USER_UpgradeDBInstance.Upgrading.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades"). If you need assistance with turning off automatic minor
version upgrade, please reach out to the AWS Support.

Sometimes a new minor version becomes available before RDS applies a previous minor version. For example, your instance is
running on `21.0.0.0.ru-2025-07.rur-2025-07.r1` when `both 21.0.0.0.ru-2025-10.rur-2025-10.r1` and `21.0.0.0.ru-2026-01.rur-2026-01.r1`
are available as upgrade targets. In this situation, to avoid unnecessary downtime for your DB instances, RDS schedules the automatic
minor version upgrade to the most recent version, skipping the upgrade to the previous version. In this example, RDS upgrades your instance
from `21.0.0.0.ru-2025-07.rur-2025-07.r1` directly to `21.0.0.0.ru-2026-01.rur-2026-01.r1`.
