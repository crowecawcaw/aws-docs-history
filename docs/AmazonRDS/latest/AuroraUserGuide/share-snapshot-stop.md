# Stopping snapshot sharing

To stop sharing a DB cluster snapshot, you remove permission from the target AWS account.

###### To stop sharing a manual DB cluster snapshot with an AWS account

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Select the manual snapshot that you want to stop sharing.
4. Choose **Actions**, and then choose **Share snapshot**.
5. To remove permission for an AWS account, choose **Delete** for the AWS account identifier
   for that account from the list of authorized accounts.
6. Choose **Save** to save your changes.
   To remove an AWS account identifier from the list, use the `--values-to-remove` parameter.

###### Example of stopping snapshot sharing

The following example prevents AWS account ID 444455556666 from restoring the snapshot.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-snapshot-attribute \
--db-cluster-snapshot-identifier manual-cluster-snapshot1 \
--attribute-name restore \
--values-to-remove 444455556666
```

For Windows:

```
aws rds modify-db-cluster-snapshot-attribute ^
--db-cluster-snapshot-identifier manual-cluster-snapshot1 ^
--attribute-name restore ^
--values-to-remove 444455556666
```

To remove sharing permission for an AWS account, use the [`ModifyDBClusterSnapshotAttribute`](../APIReference/API_ModifyDBClusterSnapshotAttribute.md "../APIReference/API_ModifyDBClusterSnapshotAttribute.md")
operation with `AttributeName` set to `restore` and the `ValuesToRemove` parameter. To
mark a manual snapshot as private, remove the value `all` from the values list for the `restore`
attribute.
