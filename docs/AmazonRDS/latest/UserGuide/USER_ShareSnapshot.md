# Sharing public snapshots for Amazon RDS

You can share an unencrypted manual snapshot as public, which makes the snapshot available to all AWS accounts. Make
sure when sharing a snapshot as public that none of your private information is included in the public snapshot.

When a snapshot is shared publicly, it gives all AWS accounts permission both to copy the snapshot and to create DB
instances from it.

You aren't billed for the backup storage of public snapshots owned by other accounts. You're billed only for
snapshots that you own.

If you copy a public snapshot, you own the copy. You're billed for the backup storage of your snapshot copy. If you
create a DB instance from a public snapshot, you're billed for that DB instance.
For Amazon RDS pricing information, see the [Amazon RDS product
page](https://aws.amazon.com/rds/pricing "https://aws.amazon.com/rds/pricing").

You can delete only the public snapshots that you own. To delete a shared or public snapshot, make sure to log into the
AWS account that owns the snapshot.

## Viewing public snapshots owned by other AWS accounts

You can view public snapshots owned by other accounts in a particular AWS Region on the **Public** tab
of the **Snapshots** page in the Amazon RDS console. Your snapshots (those owned by your account) don't
appear on this tab.

###### To view public snapshots

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Choose the **Public** tab.

The public snapshots appear. You can see which account owns a public snapshot in the **Owner**
column.

###### Note

You might have to modify the page preferences, by selecting the gear icon at the upper right of the
**Public snapshots** list, to see this column.

## Viewing your own public snapshots

You can use the following AWS CLI command (Unix only) to view the public snapshots owned by your AWS account in a
particular AWS Region.

```
aws rds describe-db-snapshots --snapshot-type public --include-public | grep `account_number`
```

The output returned is similar to the following example if you have public snapshots.

```
"DBSnapshotArn": "arn:aws:rds:us-east-1:123456789012:snapshot:mysnapshot1",
"DBSnapshotArn": "arn:aws:rds:us-east-1:123456789012:snapshot:mysnapshot2",
```

###### Note

You might see duplicate entries for `DBSnapshotIdentifier` or
`SourceDBSnapshotIdentifier`.

## Sharing public snapshots from deprecated DB engine versions

Restoring or copying public snapshots from deprecated DB engine versions isn't supported.

The RDS for Oracle and RDS for PostgreSQL DB engines support upgrading DB snapshot engine versions directly. You can upgrade your
snapshots, then re-share them publicly. For more information, see the following:

- [Upgrading an Oracle DB snapshot](USER_UpgradeDBSnapshot.md "USER_UpgradeDBSnapshot.md")
- [Upgrading a PostgreSQL DB snapshot engine version](USER_UpgradeDBSnapshot.md "USER_UpgradeDBSnapshot.md")

For other DB engines, perform the following steps to make your existing unsupported public snapshot available to restore
or copy:

1. Mark the snapshot as private.
2. Restore the snapshot.
3. Upgrade the restored DB instance to a supported engine version.
4. Create a new snapshot.
5. Re-share the snapshot publicly.
