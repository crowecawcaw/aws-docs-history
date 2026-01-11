# Managing an Amazon RDS Custom for SQL Server DB instance

Amazon RDS Custom for SQL Server supports a subset of the usual management tasks for Amazon RDS DB instances.
Following, you can find instructions for the supported RDS Custom for SQL Server management tasks using the
AWS Management Console and the AWS CLI.

###### Topics

- [Pausing and resuming RDS Custom automation](custom-managing-sqlserver.md "custom-managing-sqlserver.md")
- [Modifying an RDS Custom for SQL Server DB instance](custom-managing.md "custom-managing.md")
- [Modifying the storage for an RDS Custom for SQL Server DB instance](custom-managing-sqlserver.md "custom-managing-sqlserver.md")
- [Tagging RDS Custom for SQL Server resources](custom-managing-sqlserver.md "custom-managing-sqlserver.md")
- [Deleting an RDS Custom for SQL Server DB instance](#custom-managing-sqlserver.deleting "#custom-managing-sqlserver.deleting")
- [Starting and stopping an RDS Custom for SQL Server DB instance](custom-managing-sqlserver.md "custom-managing-sqlserver.md")

## Deleting an RDS Custom for SQL Server DB instance

To delete an RDS Custom for SQL Server DB instance, do the following:

- Provide the name of the DB instance.
- Choose or clear the option to take a final DB snapshot of the DB instance.
- Choose or clear the option to retain automated backups.

You can delete an RDS Custom for SQL Server DB instance using the console or the CLI. The time required
to delete the DB instance can vary depending on the backup retention period (that is,
how many backups to delete), how much data is deleted, and whether a final snapshot is taken.

###### Warning

Deleting a RDS Custom for SQL Server DB instance will permanently delete the EC2 instance and the associated Amazon EBS volumes.
You shouldn’t terminate or delete these resources at any time, otherwise, the deletion and the final snapshot creation may fail.

###### Note

You can't create a final DB snapshot of your DB instance if it has a status of `creating`, `failed`,
`incompatible-create`, `incompatible-restore`, or `incompatible-network`.
For more information, see [Viewing Amazon RDS DB instance status](accessing-monitoring.md#Overview.DBInstance.Status "accessing-monitoring.md#Overview.DBInstance.Status").

###### Important

When you choose to take a final snapshot, we recommend that you avoid writing data to
your DB instance while the DB instance deletion is in progress. Once the DB instance deletion is initiated,
data changes are not guaranteed to be captured by the final snapshot.

###### To delete an RDS Custom DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the RDS Custom for SQL Server DB
   instance that you want to delete. RDS Custom for SQL Server DB instances show the role **Instance (RDS Custom for SQL Server)**.
3. For **Actions**, choose **Delete**.
4. To take a final snapshot, choose **Create final snapshot**, and provide a name for the **Final snapshot name**.
5. To retain automated backups, choose **Retain automated
   backups**.
6. Enter `delete me` in the box.
7. Choose **Delete**.
   You delete an RDS Custom for SQL Server DB instance by using the [delete-db-instance](../../../cli/latest/reference/rds/delete-db-instance.md "../../../cli/latest/reference/rds/delete-db-instance.md") AWS CLI command. Identify the DB instance using the required parameter
   `--db-instance-identifier`. The remaining parameters are the same as for an Amazon RDS DB instance.

The following example deletes the RDS Custom for SQL Server DB instance named `my-custom-instance`, takes a final snapshot,
and retains automated backups.

For Linux, macOS, or Unix:

```
aws rds delete-db-instance \
    --db-instance-identifier `my-custom-instance` \
    --no-skip-final-snapshot \
    --final-db-snapshot-identifier `my-custom-instance-final-snapshot` \
    --no-delete-automated-backups
```

For Windows:

```
aws rds delete-db-instance ^
    --db-instance-identifier `my-custom-instance` ^
    --no-skip-final-snapshot ^
    --final-db-snapshot-identifier `my-custom-instance-final-snapshot` ^
    --no-delete-automated-backups
```

To take a final snapshot, the `--final-db-snapshot-identifier` option is required and must be specified.

To skip the final snapshot, specify the `--skip-final-snapshot` option instead of the `--no-skip-final-snapshot` and `--final-db-snapshot-identifier` options in the command.

To delete automated backups, specify the `--delete-automated-backups` option instead of the `--no-delete-automated-backups` option in the command.
