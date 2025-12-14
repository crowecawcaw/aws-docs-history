# Upgrading a MySQL DB snapshot engine

version

With Amazon RDS, you can create a storage volume DB snapshot of your MySQL DB instance. When
you create a DB snapshot, the snapshot is based on the engine version used by your DB
instance. You can
upgrade the engine version for your DB snapshots.

For RDS for MySQL, you can upgrade a version 5.7 snapshot to version 8.0, or a version 8.0
snapshot to version 8.4. You can upgrade encrypted or unencrypted DB snapshots.

To view the available engine versions for your RDS for MySQL DB snapshot, use the following AWS CLI
example.

```
aws rds describe-db-engine-versions --engine mysql --include-all --engine-version `example-engine-version` --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" --output text
```

If you don't see results for your snapshot, your engine version might be deprecated. If
your engine version is deprecated, we recommend that you upgrade to the newest major version
upgrade target or to one of the other available upgrade targets for that version. For more
information, see [Upgrade options for DB snapshots with
unsupported engine versions for RDS for MySQL](mysql-upgrade-snapshot.md "mysql-upgrade-snapshot.md").

After restoring a DB snapshot upgraded to a new engine version, make sure to test that the
upgrade was successful. For more information about a major version upgrade, see [Upgrades of the RDS for MySQL DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md"). To learn how to restore a DB snapshot, see
[Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").

###### Note

You can't upgrade automated DB snapshots that were created during the automated backup
process.

You can upgrade a DB snapshot using the AWS Management Console, AWS CLI, or RDS API.

Console
To upgrade a DB snapshot engine version using the AWS Management Console, use the following procedure.

###### To upgrade a DB snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Choose the snapshot that you want to upgrade.
4. For **Actions**, choose **Upgrade
   snapshot**. The **Upgrade snapshot** page
   appears.
5. Choose the **New engine version** to upgrade to.
6. Choose **Save changes** to upgrade the snapshot.

During the upgrade process, all snapshot actions are disabled for this DB
snapshot. Also, the DB snapshot status changes from
**Available** to **Upgrading**, and
then changes to **Active** upon completion. If the DB
snapshot can't be upgraded because of snapshot corruption issues, the status
changes to **Unavailable**. You can't recover the snapshot
from this state.

###### Note

If the DB snapshot upgrade fails, the snapshot is rolled back to the
original state with the original version.

AWS CLITo upgrade a DB snapshot to a new database engine version, run the AWS CLI [modify-db-snapshot](../../../cli/latest/reference/rds/modify-db-snapshot.md "../../../cli/latest/reference/rds/modify-db-snapshot.md")
command.

###### Options

- `--db-snapshot-identifier` – The identifier of the DB
  snapshot to upgrade. The identifier must be a unique Amazon Resource Name
  (ARN). For more information, see [Amazon Resource Names (ARNs) in Amazon RDS](USER_Tagging.md "USER_Tagging.md").
- `--engine-version` – The engine version to upgrade the
  DB snapshot to.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-snapshot \

    --db-snapshot-identifier `my_db_snapshot` \
    --engine-version `new_version`
```

For Windows:

```
aws rds modify-db-snapshot ^
    --db-snapshot-identifier `my_db_snapshot` ^
    --engine-version `new_version`
```

Amazon RDS APITo upgrade a DB snapshot to a new database engine version, call the RDS API [ModifyDBSnapshot](../APIReference/API_ModifyDBSnapshot.md "../APIReference/API_ModifyDBSnapshot.md") operation.

###### Parameters

- `DBSnapshotIdentifier` – The identifier of the DB
  snapshot to upgrade. The identifier must be a unique Amazon Resource Name
  (ARN). For more information, see [Amazon Resource Names (ARNs) in Amazon RDS](USER_Tagging.md "USER_Tagging.md").
- `EngineVersion` – The engine version to upgrade the DB
  snapshot to.
