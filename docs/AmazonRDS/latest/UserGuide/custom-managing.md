# Deleting an RDS Custom for Oracle DB instance

###### Warning

Deleting a DB instance is a permanent action. You can't recover a DB instance after deletion unless you have a backup or snapshot.

When you delete an RDS Custom DB instance, AWS automatically deletes the underlying Amazon EC2 instance and EBS volumes. Don't manually terminate the Amazon EC2 instance or delete the EBS volumes before deleting the DB instance through Amazon RDS. Manual deletion of these resources causes DB instance deletion and final snapshot creation to fail, preventing any possibility of recovery.

To delete an RDS Custom DB instance, do the following:

- Provide the name of the DB instance.
- Clear the option to take a final DB snapshot of the DB instance.
- Choose or clear the option to retain automated backups.
  You can delete an RDS Custom DB instance using the console or the CLI. The time required
  to delete the DB instance can vary depending on the backup retention period (that is,
  how many backups to delete) and how much data is deleted.

###### To delete an RDS Custom DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the RDS Custom DB
   instance that you want to delete. RDS Custom DB instances show the role **Instance (RDS Custom)**.
3. For **Actions**, choose **Delete**.
4. To retain automated backups, choose **Retain automated
   backups**.
5. Enter `delete me` in the box.
6. Choose **Delete**.
   You delete an RDS Custom DB instance by using the [delete-db-instance](../../../cli/latest/reference/rds/delete-db-instance.md "../../../cli/latest/reference/rds/delete-db-instance.md") AWS CLI command. Identify the DB instance using the required parameter
   `--db-instance-identifier`. The remaining parameters are the same as for an Amazon RDS DB instance, with the
   following exceptions:

- `--skip-final-snapshot` is required.
- `--no-skip-final-snapshot` isn't supported.
- `--final-db-snapshot-identifier` isn't supported.
  The following example deletes the RDS Custom DB instance named `my-custom-instance`, and retains automated
  backups.

For Linux, macOS, or Unix:

```
aws rds delete-db-instance \
    --db-instance-identifier `my-custom-instance` \
    --skip-final-snapshot \
    --no-delete-automated-backups
```

For Windows:

```
aws rds delete-db-instance ^
    --db-instance-identifier `my-custom-instance` ^
    --skip-final-snapshot ^
    --no-delete-automated-backups
```
