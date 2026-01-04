# Backing up and restoring an Amazon RDS Custom for SQL Server DB instance

Like Amazon RDS, RDS Custom creates and saves automated backups of your RDS Custom for SQL Server DB instance when backup retention is enabled.
You can also back up your DB instance manually. The automated backups are comprised of snapshot backups and transaction log backups.
Snapshot backups are taken for the entire storage volume of DB instance during your specified backup window.
Transaction log backups are taken for the PITR-eligible databases on a regular interval period.
RDS Custom saves the automated backups of your DB instance according to your specified backup retention period.
You can use automated backups to recover your DB instance to a point in time within the backup retention period.

You can also take snapshot backups manually. You can create a new DB instance from these snapshot backups at any time.
For more information about manually creating a DB snapshot, see [Creating an RDS Custom for SQL Server snapshot](custom-backup-sqlserver.md "custom-backup-sqlserver.md").

Although snapshot backups serve operationally as full backups, you are billed only for incremental storage use.
The first snapshot of an RDS Custom DB instance contains the data for the full DB instance. Subsequent snapshots of the same
database are incremental, which means that only the data that has changed after your most recent snapshot is saved.

###### Topics

- [Creating an RDS Custom for SQL Server snapshot](custom-backup-sqlserver.md "custom-backup-sqlserver.md")
- [Restoring from an RDS Custom for SQL Server DB snapshot](custom-backup-sqlserver.md "custom-backup-sqlserver.md")
- [Restoring an RDS Custom for SQL Server instance to a point in time](custom-backup.md "custom-backup.md")
- [Deleting an RDS Custom for SQL Server snapshot](custom-backup-sqlserver.md "custom-backup-sqlserver.md")
- [Deleting RDS Custom for SQL Server automated backups](custom-backup-sqlserver.md "custom-backup-sqlserver.md")
