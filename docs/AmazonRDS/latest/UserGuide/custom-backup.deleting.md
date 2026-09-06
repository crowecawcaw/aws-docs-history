

# Deleting an RDS Custom for Oracle snapshot
<a name="custom-backup.deleting"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

You can delete DB snapshots managed by RDS Custom for Oracle when you no longer need them. The deletion procedure is the same for both Amazon RDS and RDS Custom DB instances.

The Amazon EBS snapshots for the binary and root volumes remain in your account for a longer time because they might be linked to some instances running in your account or to other RDS Custom for Oracle snapshots. These EBS snapshots are automatically deleted after they're no longer related to any existing RDS Custom for Oracle resources (DB instances or backups).

## Console
<a name="USER_DeleteSnapshot.CON"></a>

**To delete a snapshot of an RDS Custom DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Snapshots**.

1. Choose the DB snapshot that you want to delete.

1. For **Actions**, choose **Delete snapshot**.

1. Choose **Delete** on the confirmation page.

## AWS CLI
<a name="USER_DeleteSnapshot.CLI"></a>

To delete an RDS Custom snapshot, use the AWS CLI command [delete-db-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-db-snapshot.html).

The following option is required:
+ `--db-snapshot-identifier` – The snapshot to be deleted

The following example deletes the `my-custom-snapshot` DB snapshot.

**Example**  
For Linux, macOS, or Unix:  

```
1. aws rds delete-db-snapshot \  
2.   --db-snapshot-identifier {{my-custom-snapshot}}
```
For Windows:  

```
1. aws rds delete-db-snapshot ^
2.   --db-snapshot-identifier {{my-custom-snapshot}}
```