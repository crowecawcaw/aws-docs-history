# Backing up and restoring an Amazon RDS Custom for Oracle DB instance

Like Amazon RDS, RDS Custom creates and saves automated backups of your RDS Custom for Oracle DB instance during
the backup window of your DB instance. You can also back up your DB instance manually.

The procedure is identical to taking a snapshot of an Amazon RDS DB instance. The first
snapshot of an RDS Custom DB instance contains the data for the full DB instance. Subsequent
snapshots are incremental.

Restore DB snapshots using either the AWS Management Console or the AWS CLI.

###### Topics

- [Creating an RDS Custom for Oracle snapshot](custom-backup.md "custom-backup.md")
- [Restoring from an RDS Custom for Oracle DB snapshot](custom-backup.md "custom-backup.md")
- [Restoring an RDS Custom for Oracle instance to a point in time](custom-backup.md "custom-backup.md")
- [Deleting an RDS Custom for Oracle snapshot](custom-backup.md "custom-backup.md")
- [Deleting RDS Custom for Oracle automated backups](custom-backup.md "custom-backup.md")
