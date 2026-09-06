

# Stopping snapshot sharing for Amazon RDS
<a name="share-snapshot-stop"></a>

To stop sharing a DB snapshot, you remove permission from the target AWS account.

## Console
<a name="share-snapshot-stop.CON"></a>

**To stop sharing a manual DB snapshot with an AWS account**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Snapshots**.

1. Select the manual snapshot that you want to stop sharing.

1. Choose **Actions**, and then choose **Share snapshot**.

1. To remove permission for an AWS account, choose **Delete** for the AWS account identifier for that account from the list of authorized accounts.

1. Choose **Save** to save your changes.

## CLI
<a name="share-snapshot-stop.CLI"></a>

To remove an AWS account identifier from the list, use the `--values-to-remove` parameter.

**Example of stopping snapshot sharing**  
The following example prevents AWS account ID 444455556666 from restoring the snapshot.  
For Linux, macOS, or Unix:  

```
aws rds modify-db-snapshot-attribute \
--db-snapshot-identifier manual-snapshot1 \
--attribute-name restore \
--values-to-remove 444455556666
```
For Windows:  

```
aws rds modify-db-snapshot-attribute ^
--db-snapshot-identifier manual-snapshot1 ^
--attribute-name restore ^
--values-to-remove 444455556666
```

## RDS API
<a name="share-snapshot-stop.API"></a>

To remove sharing permission for an AWS account, use the [`ModifyDBSnapshotAttribute`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBClusterSnapshotAttribute.html) operation with `AttributeName` set to `restore` and the `ValuesToRemove` parameter. To mark a manual snapshot as private, remove the value `all` from the values list for the `restore` attribute.