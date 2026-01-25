# Restoring from an RDS Custom for Oracle DB snapshot

When you restore an RDS Custom for Oracle DB instance, you provide the name of the DB snapshot and a name for the new instance. You can't restore from a snapshot
to an existing RDS Custom DB instance. A new RDS Custom for Oracle DB instance is created when you restore.

The restore process differs in the following ways from restore in Amazon RDS:

- Before restoring a snapshot, RDS Custom for Oracle backs up existing configuration files. These files are available on the restored
  instance in the directory `/rdsdbdata/config/backup`. RDS Custom for Oracle restores the DB snapshot with default parameters
  and overwrites the previous database configuration files with existing ones. Thus, the restored instance doesn't
  preserve custom parameters and changes to database configuration files.
- The restored database has the same name as in the snapshot. You can't specify a different name. (For RDS Custom for Oracle, the
  default is `ORCL`.)

###### To restore an RDS Custom DB instance from a DB snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Choose the DB snapshot that you want to restore from.
4. For **Actions**, choose **Restore snapshot**.
5. On the **Restore DB instance** page, for **DB instance
   identifier**, enter the name for your restored RDS Custom DB instance.
6. Choose **Restore DB instance**.
   You restore an RDS Custom DB snapshot by using the [restore-db-instance-from-db-snapshot](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md") AWS CLI command.

If the snapshot you are restoring from is for a private DB instance, make sure to specify both the correct
`db-subnet-group-name` and `no-publicly-accessible`. Otherwise, the DB instance defaults to
publicly accessible. The following options are required:

- `db-snapshot-identifier` – Identifies the snapshot from which to restore
- `db-instance-identifier` – Specifies the name of the RDS Custom DB instance to create
  from the DB snapshot
- `custom-iam-instance-profile` – Specifies the instance profile associated with the
  underlying Amazon EC2 instance of an RDS Custom DB instance.
  The following code restores the snapshot named `my-custom-snapshot` for
  `my-custom-instance`.

For Linux, macOS, or Unix:

```
aws rds restore-db-instance-from-db-snapshot \
  --db-snapshot-identifier `my-custom-snapshot` \
  --db-instance-identifier `my-custom-instance` \
  --custom-iam-instance-profile `AWSRDSCustomInstanceProfileForRdsCustomInstance` \
  --no-publicly-accessible
```

For Windows:

```
aws rds restore-db-instance-from-db-snapshot ^
  --db-snapshot-identifier `my-custom-snapshot` ^
  --db-instance-identifier `my-custom-instance` ^
  --custom-iam-instance-profile `AWSRDSCustomInstanceProfileForRdsCustomInstance` ^
  --no-publicly-accessible
```
