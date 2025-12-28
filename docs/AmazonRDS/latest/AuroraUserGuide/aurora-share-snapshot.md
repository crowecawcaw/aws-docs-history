# Sharing a DB cluster snapshot

Using Amazon RDS, you can share a manual DB cluster snapshot in the following ways:

- Sharing a manual DB cluster snapshot, whether encrypted or unencrypted, enables authorized AWS
  accounts to copy the snapshot.
- Sharing a manual DB cluster snapshot, whether encrypted or unencrypted, enables authorized AWS
  accounts to directly restore a DB cluster from the snapshot instead of taking a copy
  of it and restoring from that.

###### Note

To share an automated DB cluster snapshot, create a manual DB cluster snapshot by copying the
automated snapshot, and then share that copy. This process also applies to AWS
Backup–generated resources.

For more information on copying a snapshot, see
[DB cluster snapshot copying](aurora-copy-snapshot.md "aurora-copy-snapshot.md"). For more
information on restoring a DB instance from a DB cluster snapshot, see
[Restoring from a DB cluster snapshot](aurora-restore-snapshot.md "aurora-restore-snapshot.md").

For more information on restoring a DB
cluster from a DB cluster snapshot, see [Overview of backing up and restoring an Aurora DB
cluster](Aurora.Managing.md "Aurora.Managing.md").

You can share a manual snapshot with up to 20 other AWS accounts.

The following limitation applies when sharing manual snapshots with other AWS accounts:

- When you restore a DB cluster from a shared snapshot using the AWS Command Line Interface (AWS CLI) or Amazon RDS API,
  you must specify the Amazon Resource Name (ARN) of the shared snapshot as the snapshot identifier.
  Learn to share snapshots, public snapshots, and encrypted snapshots in the following sections. You can also learn how to stop sharing snapshots.

###### Topics

- [Sharing a snapshot](#aurora-share-snapshot.Sharing "#aurora-share-snapshot.Sharing")
- [Sharing public snapshots](aurora-share-snapshot.md "aurora-share-snapshot.md")
- [Sharing encrypted snapshots](share-encrypted-snapshot.md "share-encrypted-snapshot.md")
- [Stopping snapshot sharing](share-snapshot-stop.md "share-snapshot-stop.md")

## Sharing a snapshot

You can share a DB cluster snapshot using the AWS Management Console, the AWS CLI, or the RDS API.

Using the Amazon RDS console, you can share a manual DB cluster snapshot with up
to 20 AWS accounts. You can also use the console to stop sharing a manual snapshot with
one or more accounts.

###### To share a manual DB cluster snapshot by using the Amazon RDS console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Select the manual snapshot that you want to share.
4. For **Actions**, choose **Share snapshot**.
5. Choose one of the following options for **DB snapshot
   visibility**.
   - If the source is unencrypted, choose **Public** to permit all AWS accounts to restore a DB cluster from your manual
     DB cluster snapshot, or choose **Private** to permit only AWS accounts that you
     specify to restore a DB cluster from your manual DB cluster snapshot.

   ###### Warning

   If you set **DB snapshot visibility** to **Public**,
   all AWS accounts can restore a DB cluster from your manual DB cluster snapshot and have
   access to your data. Do not share any manual DB cluster snapshots that contain private
   information as **Public**.

   For more information, see [Sharing public snapshots](aurora-share-snapshot.md "aurora-share-snapshot.md").
   - If the source is encrypted, **DB snapshot visibility** is set as
     **Private** because encrypted snapshots can't be
     shared as public.

   ###### Note

   Snapshots that have been encrypted with the default AWS KMS key can't be shared. For
   information on how to work around this issue, see [Sharing encrypted snapshots](share-encrypted-snapshot.md "share-encrypted-snapshot.md").

6. For **AWS Account ID**, enter the AWS account identifier for an account that you want to permit to restore a
   DB cluster from your manual snapshot, and then choose **Add**. Repeat to include additional
   AWS account identifiers, up to 20 AWS accounts.

If you make an error when adding an AWS account identifier to the list of permitted
accounts, you can delete it from the list by choosing **Delete** at
the right of the incorrect AWS account identifier.

![Permit AWS accounts to restore a manual DB cluster snapshot](images/ShareSnapshot_add.png) 7. After you have added identifiers for all of the AWS accounts that you want to permit to restore the manual snapshot, choose
**Save** to save your changes.
To share a DB cluster snapshot, use the `aws rds modify-db-cluster-snapshot-attribute`
command. Use the `--values-to-add` parameter to add a list of the IDs for the AWS accounts
that are authorized to restore the manual snapshot.

###### Example of sharing a snapshot with a single account

The following example enables AWS account identifier `123456789012` to restore the DB cluster snapshot
named `cluster-3-snapshot`.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-snapshot-attribute \
--db-cluster-snapshot-identifier cluster-3-snapshot \
--attribute-name restore \
--values-to-add 123456789012
```

For Windows:

```
aws rds modify-db-cluster-snapshot-attribute ^
--db-cluster-snapshot-identifier cluster-3-snapshot ^
--attribute-name restore ^
--values-to-add 123456789012
```

###### Example of sharing a snapshot with multiple accounts

The following example enables two AWS account identifiers, `111122223333` and
`444455556666`, to restore the DB cluster snapshot named
`manual-cluster-snapshot1`.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-snapshot-attribute \
--db-cluster-snapshot-identifier manual-cluster-snapshot1 \
--attribute-name restore \
--values-to-add {"111122223333","444455556666"}
```

For Windows:

```
aws rds modify-db-cluster-snapshot-attribute ^
--db-cluster-snapshot-identifier manual-cluster-snapshot1 ^
--attribute-name restore ^
--values-to-add "[\"111122223333\",\"444455556666\"]"
```

###### Note

When using the Windows command prompt, you must escape double quotes (") in JSON code by
prefixing them with a backslash (\).

To list the AWS accounts enabled to restore a snapshot, use the
[`describe-db-cluster-snapshot-attributes`](../../../cli/latest/reference/rds/describe-db-cluster-snapshot-attributes.md "../../../cli/latest/reference/rds/describe-db-cluster-snapshot-attributes.md")
AWS CLI command.

You can also share a manual DB cluster snapshot with other AWS accounts by
using the Amazon RDS API. To do so, call the
[`ModifyDBClusterSnapshotAttribute`](../APIReference/API_ModifyDBClusterSnapshotAttribute.md "../APIReference/API_ModifyDBClusterSnapshotAttribute.md")
operation. Specify `restore` for `AttributeName`, and
use the `ValuesToAdd` parameter to add a list of the IDs for the AWS accounts
that are authorized to restore the manual snapshot.

To make a manual snapshot public and restorable by all AWS accounts, use the value
`all`. However, take care not to add the `all` value for any
manual snapshots that contain private information that you don't want to be available to
all AWS accounts. Also, don't specify `all` for encrypted snapshots, because
making such snapshots public isn't supported.

To list all of the AWS accounts permitted to restore a snapshot, use the
[`DescribeDBClusterSnapshotAttributes`](../APIReference/API_DescribeDBClusterSnapshotAttributes.md "../APIReference/API_DescribeDBClusterSnapshotAttributes.md")
API operation.
