# Upgrading an Oracle DB snapshot

Upgrading your Oracle DB snapshots in Amazon RDS ensures that your database remains secure,
compatible, and fully supported. As older Oracle versions reach the end of patch support,
you can upgrade any manual DB snapshots tied to these versions to avoid potential
vulnerabilities or service limitations. For more information, see [Oracle engine version management](USER_UpgradeDBInstance.Oracle.md#Oracle.Concepts.Patching "USER_UpgradeDBInstance.Oracle.md#Oracle.Concepts.Patching").

Amazon RDS supports upgrading snapshots in all AWS Regions.

###### To upgrade an Oracle DB snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**, and
   then select the DB snapshot that you want to upgrade.
3. For **Actions**, choose **Upgrade
   snapshot**. The **Upgrade snapshot** page
   appears.
4. Choose the **New engine version** to upgrade the
   snapshot to.
5. (Optional) For **Option group**, choose the option
   group for the upgraded DB snapshot. The same option group considerations
   apply when upgrading a DB snapshot as when upgrading a DB instance. For
   more information, see [Option group considerations](USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG "USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG").
6. Choose **Save changes** to save your changes.

During the upgrade process, all snapshot actions are disabled for this
DB snapshot. Also, the DB snapshot status changes from
**available** to **upgrading**,
and then changes to **active** upon completion. If the
DB snapshot can't be upgraded because of snapshot corruption issues, the
status changes to **unavailable**. You can't recover
the snapshot from this state.

###### Note

If the DB snapshot upgrade fails, the snapshot is rolled back to
the original state with the original version.
To upgrade an Oracle DB snapshot by using the AWS CLI, call the [modify-db-snapshot](../../../cli/latest/reference/rds/modify-db-snapshot.md "../../../cli/latest/reference/rds/modify-db-snapshot.md")
command with the following parameters:

- `--db-snapshot-identifier` – The name of the DB
  snapshot.
- `--engine-version` – The version to upgrade the
  snapshot to.
  You might also need to include the following parameter. The same option group
  considerations apply when upgrading a DB snapshot as when upgrading a DB
  instance. For more information, see [Option group considerations](USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG "USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG").

- `--option-group-name` – The option group for the
  upgraded DB snapshot.

###### Example

The following example upgrades a DB snapshot.

For Linux, macOS, or Unix:

```
aws rds modify-db-snapshot \
    --db-snapshot-identifier `mydbsnapshot` \
    --engine-version `19.0.0.0.ru-2020-10.rur-2020-10.r1` \
    --option-group-name `default:oracle-se2-19`
```

For Windows:

```
aws rds modify-db-snapshot ^
    --db-snapshot-identifier `mydbsnapshot` ^
    --engine-version `19.0.0.0.ru-2020-10.rur-2020-10.r1` ^
    --option-group-name `default:oracle-se2-19`
```

To upgrade an Oracle DB snapshot by using the Amazon RDS API, call the [ModifyDBSnapshot](../APIReference/API_ModifyDBSnapshot.md "../APIReference/API_ModifyDBSnapshot.md")
operation with the following parameters:

- `DBSnapshotIdentifier` – The name of the DB
  snapshot.
- `EngineVersion` – The version to upgrade the
  snapshot to.
  You might also need to include the `OptionGroupName` parameter. The
  same option group considerations apply when upgrading a DB snapshot as when
  upgrading a DB instance. For more information, see [Option group considerations](USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG "USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG").
