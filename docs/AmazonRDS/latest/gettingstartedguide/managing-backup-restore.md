

# Backing up and restoring your Amazon RDS DB instance
<a name="managing-backup-restore"></a>

Data backups are important for recovering from accidental deletions, corruption, or unexpected failures. Amazon RDS provides both automated backups and manual snapshots, so you have flexibility in how you protect and restore your data. This section provides an overview of these options and practical guidance for using them.

**Topics**
+ [Automated backups](#automated-backups)
+ [Manual snapshots](#manual-snapshots)

## Automated backups
<a name="automated-backups"></a>

Automated backups in Amazon RDS provide a reliable way to protect your data by creating backups of your database at regular intervals and retaining them for a specified period. Amazon RDS enables this feature by default when you create your DB instance. It ensure that you can recover to almost any point within the retention period without manual intervention.

These sections provide a brief overview of the available backup strategies. For comprehensive documentation on automated backups, see [Managing automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.html) in the *Amazon RDS User Guide*.

### Retention periods
<a name="retention-periods"></a>

The retention period determines how long Amazon RDS retains automated backups before it automatically deletes them. You can configure this period to meet your compliance or operational requirements, with options ranging from 1 to 35 days.

To configure how long Amazon RDS retains automated backups, set the **Backup retention period** setting for the DB instance:

![Backup retention period field set to 7 days, highlighted with a red border.](http://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/images/automated-backups.png)


Consider the following when you configure a retention period:
+ A longer retention period provides more recovery options but might increase storage costs.
+ RDS stores backups in Amazon S3, and AWS calculates the storage cost separately from your DB instance usage.

For more information, see [Retaining automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.Retaining.html) in the *Amazon RDS User Guide*.

### Point-in-time recovery
<a name="pit"></a>

With point-in-time recovery, you can restore your database to any second within your backup retention period. This is especially useful in scenarios such as accidental data deletion or corruption. 

To perform a point-in-time recovery, choose **Automated backups** within the Amazon RDS console and select the DB instance that you want to restore. Then, choose **Actions**, **Restore to point in time**. Specify the exact time to which you want to restore your database. Amazon RDS creates a new instance from the backups and leaves the original instance intact.

![Restore time section with Latest restorable time selected and Custom date and time option.](http://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/images/point-in-time.png)


For more information, see [Restoring a DB instance to a specified time for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html) in the *Amazon RDS User Guide*.

## Manual snapshots
<a name="manual-snapshots"></a>

Manual snapshots provide more control over your backup strategy, and let you capture a complete copy of your database at a specific point in time. Unlike automated backups, manual snapshots are user-initiated and persist until you explicitly delete them. This provides a long-term data retention option.

Manual snapshots have the following main benefits:
+ Ideal for preserving data before significant schema changes or updates.
+ Useful for duplicating a database in a different environment, such as development or testing.
+ Provide an additional layer of redundancy when paired with automated backups.

To take a manual snapshot, select the DB instance that you want to back up and choose **Actions**, **Take snapshot**. RDS stores manual snapshots in Amazon S3. You can share them across AWS accounts or copy them to different AWS Regions for disaster recovery purposes.

![Take DB Snapshot dialog with snapshot type, DB instance, and snapshot name fields.](http://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/images/take-snapshot.png)


Restoring from a manual snapshot involves creating a new DB instance from the stored backup. Choose **Snapshots** within the Amazon RDS console and select the snapshot that you want to restore. Choose **Actions**, **Restore snapshot**. Specify the instance details for the new database.

For more information, see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html) in the *Amazon RDS User Guide*.