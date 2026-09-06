

# Stopping or deleting continuous backups
<a name="point-in-time-recovery-stopping"></a>

You can stop the creation of continuous backups or you can delete specific backups (point-in-time-recovery or PITR points).

If you want to stop continuous backups, you must delete the continuous backup rule from your backup plan. If you wish to stop continuous backups for one or more resources but not for all resources, create a new backup plan with the continuous backup rule for those resources you still want to be continuously backed up. If instead you only delete a continuous backup recovery point from your backup vault, your backup plan will still continue to execute the continuous backup rule, creating a new recovery point.

However, even after you delete your continuous backup rule, AWS Backup remembers the retention period from your now-deleted backup rule. It will automatically delete your continuous backup recovery point from your backup vault based on your specified retention period.

When deleting Amazon RDS recovery points, consider:
+ A multi AZ (availability zone) database instance set to `Always On` should not have a backup retention set to zero. If errors occur, use AWS CLI command `disassociate-recovery-point` instead of `delete-recovery-point`, then change the retention setting to 1 in your Amazon RDS settings.
+ When point-in-time recovery (PITR) is disabled, the change is scheduled for your maintenance window. You may continue to incur backup storage costs until the maintenance window applies the change. This process may take up to 7 days depending on your maintenance window schedule.

When deleting Aurora recovery points, consider:

If this is selected for an Amazon Aurora recovery point, AWS Backup sets the retention period to 1 day. Aurora backups cannot be completely deleted until the source cluster has also been deleted.

## Transitioning continuous backups between backup plans
<a name="pitr-transitioning-between-plans"></a>

If you transition a resource's continuous backup protection from one backup plan to another, be aware of the following behavior:
+ **Amazon RDS:** After the existing continuous recovery point's retention period elapses and the recovery point is removed from the vault, the next execution of the new backup plan configures continuous backups. There is no gap in point-in-time restore coverage during this transition. For more information, see [How do I stop continuous backups for Amazon RDS in AWS Backup?](https://repost.aws/knowledge-center/backup-stop-rds-continuous-backup)
+ **Amazon S3:** A disassociated Amazon S3 continuous recovery point transitions to a `STOPPED` state and remains in its backup vault. For more information, see [Backup deletion](deleting-backups.md).
**Note**  
Calling `DisassociateRecoveryPoint` on an Amazon S3 continuous recovery point that is already in `EXPIRED` status has no effect. The recovery point state and configuration remain unchanged.

In all cases, when you remove a continuous backup rule from a backup plan, AWS Backup remembers the retention period from the deleted rule and automatically deletes the continuous backup recovery point when the retention period elapses. For more information, see [Removing the only continuous backup rule from a backup plan](point-in-time-recovery-removing_rule.md).