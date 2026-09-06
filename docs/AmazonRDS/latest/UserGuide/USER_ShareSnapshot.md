

# Sharing a DB snapshot for Amazon RDS
<a name="USER_ShareSnapshot"></a>

Using Amazon RDS, you can share a manual DB snapshot in the following ways:
+ Sharing a manual DB snapshot, whether encrypted or unencrypted, enables authorized AWS accounts to copy the snapshot.
+ Sharing an unencrypted manual DB snapshot enables authorized AWS accounts to directly restore a DB instance from the snapshot instead of taking a copy of it and restoring from that. However, you can't restore a DB instance from a DB snapshot that is both shared and encrypted. Instead, you can make a copy of the DB snapshot and restore the DB instance from the copy.

**Note**  
To share an automated DB snapshot, create a manual DB snapshot by copying the automated snapshot, and then share that copy. This process also applies to AWS Backup–generated resources.

For more information on copying a snapshot, see [Copying a DB snapshot for Amazon RDS](USER_CopySnapshot.md). For more information on restoring a DB instance from a DB snapshot, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md).

You can share a manual snapshot with up to 20 other AWS accounts.

The following limitations apply when you share manual snapshots with other AWS accounts:
+ When you restore a DB instance from a shared snapshot using the AWS Command Line Interface (AWS CLI) or Amazon RDS API, you must specify the Amazon Resource Name (ARN) of the shared snapshot as the snapshot identifier.
+ You can't share a DB snapshot that uses an option group with permanent or persistent options, except for Oracle DB instances that have the `Timezone` or `OLS` option (or both).

  A *permanent option* can't be removed from an option group. Option groups with persistent options can't be removed from a DB instance once the option group has been assigned to the DB instance.

  The following table lists permanent and persistent options and their related DB engines.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html)

  For Oracle DB instances, you can copy shared DB snapshots that have the `Timezone` or `OLS` option (or both). To do so, specify a target option group that includes these options when you copy the DB snapshot. The OLS option is permanent and persistent only for Oracle DB instances running Oracle version 12.2 or higher. For more information about these options, see [Oracle time zone](Appendix.Oracle.Options.Timezone.md) and [Oracle Label Security](Oracle.Options.OLS.md).
+ You can't share a snapshot of a Multi-AZ DB cluster.

See the following topics for information about sharing public snapshots, sharing encrypted snapshots, and stopping snapshot sharing.

**Topics**
+ [Sharing public snapshots for Amazon RDS](USER_ShareSnapshot.Public.md)
+ [Sharing encrypted snapshots for Amazon RDS](share-encrypted-snapshot.md)
+ [Stopping snapshot sharing for Amazon RDS](share-snapshot-stop.md)

## Sharing a snapshot
<a name="USER_ShareSnapshot.Sharing"></a>

You can share a DB snapshot using the AWS Management Console, the AWS CLI, or the RDS API.

### Console
<a name="USER_ShareSnapshot.Console"></a>

Using the Amazon RDS console, you can share a manual DB snapshot with up to 20 AWS accounts. You can also use the console to stop sharing a manual snapshot with one or more accounts.

**To share a manual DB snapshot by using the Amazon RDS console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Snapshots**.

1. Select the manual snapshot that you want to share.

1. For **Actions**, choose **Share snapshot**.

1. Choose one of the following options for **DB snapshot visibility**.
   + If the source is unencrypted, choose **Public** to permit all AWS accounts to restore a DB instance from your manual DB snapshot, or choose **Private** to permit only AWS accounts that you specify to restore a DB instance from your manual DB snapshot.
**Warning**  
If you set **DB snapshot visibility** to **Public**, all AWS accounts can restore a DB instance from your manual DB snapshot and have access to your data. Do not share any manual DB snapshots that contain private information as **Public**.  
For more information, see [Sharing public snapshots for Amazon RDS](USER_ShareSnapshot.Public.md).
   + If the source is encrypted, **DB snapshot visibility** is set as **Private** because encrypted snapshots can't be shared as public.
**Note**  
Snapshots that have been encrypted with the default AWS KMS key can't be shared. For information on how to work around this issue, see [Sharing encrypted snapshots for Amazon RDS](share-encrypted-snapshot.md).

1. For **AWS Account ID**, enter the AWS account identifier for an account that you want to permit to restore a DB instance from your manual snapshot, and then choose **Add**. Repeat to include additional AWS account identifiers, up to 20 AWS accounts.

   If you make an error when adding an AWS account identifier to the list of permitted accounts, you can delete it from the list by choosing **Delete** at the right of the incorrect AWS account identifier.  
![Permit AWS accounts to restore a manual DB snapshot.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/ShareSnapshot_add.png)

1. After you have added identifiers for all of the AWS accounts that you want to permit to restore the manual snapshot, choose **Save** to save your changes.

### AWS CLI
<a name="USER_ShareSnapshot.CLI"></a>

To share a DB snapshot, use the `aws rds modify-db-snapshot-attribute` command. Use the `--values-to-add` parameter to add a list of the IDs for the AWS accounts that are authorized to restore the manual snapshot.

**Example of sharing a snapshot with a single account**  
The following example enables AWS account identifier `123456789012` to restore the DB snapshot named `db7-snapshot`.  
For Linux, macOS, or Unix:  

```
aws rds modify-db-snapshot-attribute \
--db-snapshot-identifier db7-snapshot \
--attribute-name restore \
--values-to-add 123456789012
```
For Windows:  

```
aws rds modify-db-snapshot-attribute ^
--db-snapshot-identifier db7-snapshot ^
--attribute-name restore ^
--values-to-add 123456789012
```

**Example of sharing a snapshot with multiple accounts**  
The following example enables two AWS account identifiers, `111122223333` and `444455556666`, to restore the DB snapshot named `manual-snapshot1`.  
For Linux, macOS, or Unix:  

```
aws rds modify-db-snapshot-attribute \
--db-snapshot-identifier manual-snapshot1 \
--attribute-name restore \
--values-to-add {"111122223333","444455556666"}
```
For Windows:  

```
aws rds modify-db-snapshot-attribute ^
--db-snapshot-identifier manual-snapshot1 ^
--attribute-name restore ^
--values-to-add "[\"111122223333\",\"444455556666\"]"
```
When using the Windows command prompt, you must escape double quotes (") in JSON code by prefixing them with a backslash (\\).

To list the AWS accounts enabled to restore a snapshot, use the [`describe-db-snapshot-attributes`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-snapshot-attributes.html) AWS CLI command.

### RDS API
<a name="USER_ShareSnapshot.API"></a>

You can also share a manual DB snapshot with other AWS accounts by using the Amazon RDS API. To do so, call the [`ModifyDBSnapshotAttribute`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBSnapshotAttribute.html) operation. Specify `restore` for `AttributeName`, and use the `ValuesToAdd` parameter to add a list of the IDs for the AWS accounts that are authorized to restore the manual snapshot. 

To make a manual snapshot public and restorable by all AWS accounts, use the value `all`. However, take care not to add the `all` value for any manual snapshots that contain private information that you don't want to be available to all AWS accounts. Also, don't specify `all` for encrypted snapshots, because making such snapshots public isn't supported.

To list all of the AWS accounts permitted to restore a snapshot, use the [`DescribeDBSnapshotAttributes`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSnapshotAttributes.html) API operation.