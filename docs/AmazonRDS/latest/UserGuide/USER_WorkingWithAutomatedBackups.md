# Introduction to backups

Amazon RDS creates and saves automated backups of your DB instance or Multi-AZ DB cluster
during the backup window of your DB instance. RDS creates a storage volume snapshot of your
DB instance, backing up the entire DB instance and not just individual databases. RDS saves
the automated backups of your DB instance according to the backup retention period that you
specify. If necessary, you can recover your DB instance to any point in time during the
backup retention period.

Automated backups follow these rules:

- Your DB instance must be in the `available` state for automated backups
  to occur. Automated backups don't occur while your DB instance is in a state
  other than `available`, for example, `storage_full`.
- Automated backups don't occur while a DB snapshot copy is running in the same
  AWS Region for the same database.
  You can also back up your DB instance manually by creating a DB snapshot. For more
  information about manually creating a DB snapshot, see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md").

Snapshot and backup functionality supports multi-volume configurations. All backup
operations include both the primary volume and any additional storage volumes. Snapshots
capture the entire database storage configuration. Point-in-time recovery (PITR) works
across all storage volumes.

The first snapshot of a DB instance contains the data for the full database. Subsequent
snapshots of the same database are incremental, which means that only the data that has
changed after your most recent snapshot is saved.

You can copy both automatic and manual DB snapshots, and share manual DB snapshots. For
more information about copying a DB snapshot, see [Copying a DB snapshot for Amazon RDS](USER_CopySnapshot.md "USER_CopySnapshot.md"). For more information about sharing a DB snapshot,
see [Sharing a DB snapshot for Amazon RDS](USER_ShareSnapshot.md "USER_ShareSnapshot.md").

## Backup storage

Your Amazon RDS backup storage for each AWS Region is composed of the automated backups
and manual DB snapshots for that Region. Total backup storage space
equals the sum of the storage for all backups in that Region. Moving a
DB snapshot to another Region increases the backup storage in the
destination Region. Backups are stored in Amazon S3.

For more information about backup storage costs, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/").

If you choose to retain automated backups when you delete a DB instance, the automated
backups are saved for the full retention period. If you don't choose
**Retain automated backups** when you delete a DB instance, all
automated backups are deleted with the DB instance. After they are deleted, the
automated backups can't be recovered. If you choose to have Amazon RDS create a final DB
snapshot before it deletes your DB instance, you can use that to recover your DB
instance. Optionally, you can use a previously created manual snapshot. Manual snapshots
are not deleted. You can have up to 100 manual snapshots per
Region.
