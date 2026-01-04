# Oracle minor version upgrades

In RDS for Oracle, a minor version upgrade is an update to a major DB engine version. In RDS, a
minor engine version is either a Release Update (RU) or Spatial Patch Bundle (SPB). For
example, if your DB instance runs major version Oracle Database 21c and minor version
21.0.0.0.ru-2024-10.rur-2024-10.r1, you can upgrade your DB engine to minor version
21.0.0.0.ru-2025-01.rur-2025-01.r1. RDS for Oracle doesn't support minor version
downgrades.

You can upgrade your DB engine to a minor version manually or automatically. To learn how to
upgrade manually, see [Manually upgrading the engine version](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual"). To learn how to configure
automatic upgrades, see [Automatically upgrading the minor engine version](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades"). Whether you
upgrade manually or automatically, a minor version upgrade entails downtime. Consider this
downtime when you plan your upgrades.

Amazon RDS also supports upgrade rollout policy to manage automatic minor version upgrades
across multiple database resources and AWS accounts. For more information,
see [Using AWS Organizations upgrade rollout policy
for automatic minor version upgrades](RDS.Maintenance.AMVU.md "RDS.Maintenance.AMVU.md").

###### Important

Make sure that you thoroughly test any upgrade to verify that your applications work
correctly before applying the upgrade to your production databases. For more
information, see [Testing an Oracle DB upgrade](USER_UpgradeDBInstance.Oracle.md "USER_UpgradeDBInstance.Oracle.md").

###### Topics

- [Release Updates (RUs) and Spatial Patch Bundles
  (SPBs)](#RUs-and-SPBs "#RUs-and-SPBs")
- [Turning on automatic minor
  version upgrades for Oracle](#oracle-minor-version-upgrade-tuning-on "#oracle-minor-version-upgrade-tuning-on")
- [Using AWS Organizations upgrade rollout policy for automatic minor version upgrades](#oracle-minor-version-upgrade-rollout "#oracle-minor-version-upgrade-rollout")
- [Notification of automatic minor
  version upgrades in RDS for Oracle](#oracle-minor-version-upgrade-advance "#oracle-minor-version-upgrade-advance")
- [When RDS schedules automatic
  minor version upgrades in RDS for Oracle](#oracle-minor-version-upgrade-scheduled "#oracle-minor-version-upgrade-scheduled")
- [Managing an automatic minor
  version upgrade in RDS for Oracle](#oracle-minor-version-upgrade-managing "#oracle-minor-version-upgrade-managing")

## Release Updates (RUs) and Spatial Patch Bundles

(SPBs)

In RDS, a release update (RU) is a quarterly minor engine version that includes
security fixes, bug fixes, and new features for Oracle Database. A Spatial Patch Bundle
(SPB) is an RU engine version that includes patches designed for the Oracle Spatial
option. For example, the SPB named 19.0.0.0.ru-2025-01.spb-1.r1 includes all patches in
the corresponding RU 19.0.0.0.ru-2025-01.rur-2025-01.r1 plus patches specific to
Spatial. SPBs are supported only for Oracle Database 19c.

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
19.0.0.0.ru-2025-01.rur-2025-01.r1, then when 19.0.0.0.ru-2025-04.rur-2025-04.r1 is
released, your instance automatically upgrades to this RU. Similarly, if your DB instance runs
19.0.0.0.ru-2025-01.spb-1.r1, then when 19.0.0.0.ru-2025-04.spb-1.r1 is released, your
instance automatically upgrades to this SPB. An instance running
19.0.0.0.ru-2025-01.rur-2025-01.r1, which is an RU, won't automatically upgrade to
19.0.0.0.ru-2025-04.spb-1.r1, which is an SPB on a separate upgrade path.

You can upgrade your DB instance to SPBs even if your instance doesn't use Spatial, but the
Spatial patches apply only to Oracle Spatial. You can upgrade manually from an RU to an
SPB at the same engine version or higher. For example, you can upgrade your instance
from 19.0.0.0.ru-2025-01.rur-2025-01.r1 to either of the following engine
versions:

- 19.0.0.0.ru-2025-01.spb-1.r1
- 19.0.0.0.ru-2025-04.spb-1.r1

You can upgrade your instance from an SPB to an RU only if the RU is a higher
engine version. For example, you can upgrade from SPB version
19.0.0.0.ru-2025-04.spb-1.r1 to a higher RU version 19.0.0.0.ru-2025-07.rur-2025-07.r1
but not to the same RU version 19.0.0.0.ru-2025-04.rur-2025-04.r1.

If your DB instance is configured for automatic minor version upgrades, and you manually
upgrade from an RU to an SPB or from an SPB to an RU, your automatic upgrade path
changes. Suppose that you manually upgrade from RU version
19.0.0.0.ru-2025-01.rur-2025-01.r1 to SPB version 19.0.0.0.ru-2025-01.spb-1.r1. Your
next automatic minor version upgrade will be to SPB version
19.0.0.0.ru-2025-04.spb-1.r1.

Because SPBs function as RUs, the RDS APIs for upgrading your instance to RUs
and SPBs are identical. The following commands demonstrate upgrading to an RU
and to an SPB.

```
aws rds modify-db-instance \
    --db-instance-identifier mydbinstance \
    --engine-version 19.0.0.0.ru-2025-01.rur-2025-01.r1

aws rds modify-db-instance \
    --db-instance-identifier mydbinstance \
    --engine-version 19.0.0.0.ru-2025-01.spb-1.r1
```

For more information about the Oracle Spatial option, see [How Spatial Patch Bundles (SPBs)
work](Oracle.Options.md#Oracle.Options.Spatial.SPBs "Oracle.Options.md#Oracle.Options.Spatial.SPBs").
For supported RUs and SPBs for Oracle Database 19c, see [Amazon RDS for
Oracle Database 19c (19.0.0.0)](../OracleReleaseNotes/oracle-version-19-0.md "../OracleReleaseNotes/oracle-version-19-0.md").

## Turning on automatic minor

version upgrades for Oracle

In an automatic minor version upgrade, RDS applies the latest available minor version
to your Oracle database without manual intervention. An Amazon RDS for Oracle DB instance schedules
your upgrade during the next maintenance window in the following circumstances:

- Your DB instance has the **Auto minor version upgrade** option
  turned on.
- Your DB instance isn't already running the latest minor DB engine version.
- Your DB instance doesn't already have a pending upgrade scheduled.

To learn how to turn on automatic upgrades, see [Automatically upgrading the minor engine version](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades").

## Using AWS Organizations upgrade rollout policy for automatic minor version upgrades

###### Important

For RDS for Oracle, you can use the upgrade rollout policy feature for auto minor version upgrade
to any engine versions released after January 2026. You can't use upgrade rollout policy for
auto minor version upgrade to the October 2025 Release Update.

Amazon RDS for Oracle supports AWS Organizations upgrade rollout policy to manage automatic minor version upgrades
across multiple database resources and AWS accounts. This policy helps you implement a controlled
upgrade strategy for your Oracle DB instances by automatically upgrading databases in a specified
order (for example, development environments before production).

For more information, see [Using AWS Organizations upgrade rollout policy
for automatic minor version upgrades](RDS.Maintenance.AMVU.md "RDS.Maintenance.AMVU.md").

## Notification of automatic minor

version upgrades in RDS for Oracle

RDS publishes an advance notice before it begins scheduling automatic upgrades. You
can find the notification in the **Maintenance & backups** tab of
the database details page. The message has the following format:

```
An automatic minor version upgrade to `engine` `version` will become available on `availability-date` and will be applied during a subsequent maintenance window.
```

The `availability-date` in the advance notice is the date
when RDS starts scheduling upgrades for DB instances in your AWS Region. It is not the date
on which the upgrade of your DB instance is scheduled to occur. For example, if the
`availability-date` is March 1, on this date RDS might
schedule your upgrade for April 14.

You can also get the upgrade availability date by using the
`describe-pending-maintenance-actions` command in the AWS CLI, as shown in
the following example:

```
aws rds describe-pending-maintenance-actions

{
    "PendingMaintenanceActions": [
        {
            "ResourceIdentifier": "arn:aws:rds:us-east-1:123456789012:db:orclinst1",
            "PendingMaintenanceActionDetails": [
                {
                    "Action": "db-upgrade",
                    "Description": "Automatic minor version upgrade to 21.0.0.0.ru-2024-07.rur-2024-07.r1",
                    "CurrentApplyDate": "2024-12-02T08:10:00Z",
                    "OptInStatus": "next-maintenance"
                }
            ]
        }, ...
```

The following table describes your options for each type of pending maintenance action
message.

| Pending maintenance action message                                                                                                                                         | When message appears                                                                                                             | Eligible to be applied at the next maintenance window? | Eligible to be applied immediately? | Eligible to have the opt-in undone? |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------- | ----------------------------------- |
| An automatic minor version upgrade to<br>`engine-version` will become available on<br>`availability-date` and should be applied<br>during a subsequent maintenance window. | 4-6 weeks before automatic upgrades are scheduled.                                                                               | Yes                                                    | Yes                                 | Yes                                 |
| Automatic minor version upgrade to<br>`engine-version`                                                                                                                     | On or after `availability-date`. RDS<br>automatically applies this upgrade in the next maintenance window of the<br>DB instance. | Yes                                                    | Yes                                 | No                                  |

For more information about [describe-pending-maintenance-actions](../../../cli/latest/reference/rds/describe-pending-maintenance-actions.md "../../../cli/latest/reference/rds/describe-pending-maintenance-actions.md"), see the _AWS CLI Command
Reference_.

## When RDS schedules automatic

minor version upgrades in RDS for Oracle

When the availability date for automatic upgrades arrives, RDS begins scheduling
upgrades. For most AWS Regions, RDS schedules your upgrade to the latest quarterly RU
approximately four to six weeks after the availability date. The scheduled date varies
depending on the AWS Region and other factors. For more information about RUs and
RURs, see [_Amazon RDS for Oracle Release Notes_](../OracleReleaseNotes/Welcome.md "../OracleReleaseNotes/Welcome.md").

When RDS schedules the upgrade, the following notification appears in the
**Maintenance & backups** tab of the database details
page:

```
Automatic minor version upgrade to `engine-version`
```

The preceding message indicates that RDS has scheduled the upgrade of your DB engine in
the next maintenance window.

Sometimes a new minor version becomes available before RDS applies a previous minor
version. For example, your instance is running
`minor-version-1` when both
`minor-version-2` and
`minor-version-3` are available as upgrade targets. In this
situation, to avoid unnecessary downtime for your DB instances, RDS schedules the
automatic minor version upgrade to the most recent version, skipping the upgrade to the
previous version. In this example, RDS upgrades your instance from
`minor-version-1` directly to
`minor-version-3`.

To ensure certain frequency of minor version upgrades, you can upgrade your instances
manually instead of using the automatic upgrade mechanism. To schedule an upgrade for
the next maintenance window, specify `--no-apply-immediately` when you
upgrade to a minor version using `modify-db-instance`. To upgrade
immediately, specify `--apply-immediately` instead. For more information, see
[Manually upgrading the engine version](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual").

## Managing an automatic minor

version upgrade in RDS for Oracle

When a new minor version becomes available, you can upgrade your DB instance to this version
manually. The following example upgrades the DB instance named `orclinst1`
immediately:

```
aws rds apply-pending-maintenance-action \
    --resource-identifier arn:aws:rds:us-east-1:123456789012:db:orclinst1 \
    --apply-action db-upgrade \
    --opt-in-type immediate
```

To opt out of an automatic minor version upgrade that hasn't been scheduled yet, set
`--opt-in-type` to `undo-opt-in`, as in the following
example:

```
aws rds apply-pending-maintenance-action \
    --resource-identifier arn:aws:rds:us-east-1:123456789012:db:orclinst1 \
    --apply-action db-upgrade \
    --opt-in-type undo-opt-in
```

If RDS has already scheduled an upgrade for your DB instance, you can't use
`apply-pending-maintenance-action` to cancel it. But you can modify your
DB instance and turn off the automatic minor upgrade feature, which then unschedules the
upgrade.

To learn how to turn off automatic minor version upgrades, see [Automatically upgrading the minor engine version](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades"). For
more information about [apply-pending-maintenance-action](../../../cli/latest/reference/rds/apply-pending-maintenance-action.md "../../../cli/latest/reference/rds/apply-pending-maintenance-action.md"), see the _AWS CLI Command
Reference_.
