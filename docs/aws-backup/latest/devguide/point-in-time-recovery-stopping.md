# Stopping or deleting continuous

backups

You can stop the creation of continuous backups or you can delete specific backups
(point-in-time-recovery or PITR points).

If you want to stop continuous backups, you must delete the continuous backup rule from
your backup plan. If you wish to stop continuous backups for one or more resources but not
for all resources, create a new backup plan with the continuous backup rule for those
resources you still want to be continuously backed up. If instead you only delete a
continuous backup recovery point from your backup vault, your backup plan will still
continue to execute the continuous backup rule, creating a new recovery point.

However, even after you delete your continuous backup rule, AWS Backup remembers the
retention period from your now-deleted backup rule. It will automatically delete your
continuous backup recovery point from your backup vault based on your specified retention
period.

When deleting Amazon RDS recovery points, consider:

- A multi AZ (availability zone) database instance set to `Always On`
  should not have a backup retention set to zero. If errors occur, use AWS CLI command
  `disassociate-recovery-point` instead of
  `delete-recovery-point`, then change the retention setting to 1 in your Amazon RDS
  settings.
- When a point-in-time recovery point (a backup created by continuous backup) for
  Amazon RDS is deleted, a database reboot is triggered and the binary logs are disabled. For
  further detail see [Backup retention period](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md#USER_WorkingWithAutomatedBackups.BackupRetention "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md#USER_WorkingWithAutomatedBackups.BackupRetention") in the _Amazon RDS User Guide_.
  When deleting Aurora recovery points, consider:

If this is selected for an Amazon Aurora recovery point, AWS Backup sets the retention period to
1 day. Aurora backups cannot be completely deleted until the source cluster has also been
deleted.
