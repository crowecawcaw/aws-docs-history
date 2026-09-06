

# Backup deletion
<a name="deleting-backups"></a>

We recommend you use AWS Backup to automatically delete the backups that you no longer need by configuring your lifecycle when you created your backup plan. For example, if you set your backup plan’s lifecycle to retain your recovery points for one year, AWS Backup will automatically delete on January 1, 2022 the recovery points it created on or within several hours of January 1, 2021. (AWS Backup randomizes its deletions within 8 hours following recovery point expiration to maintain performance.) To learn more about configuring your lifecycle retention policy, see [Creating a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html).

However, you might want to manually delete one or more recovery points. For example:
+ You have `EXPIRED` recovery points. These are recovery points AWS Backup was unable to delete automatically because you deleted or modified the original IAM policy you used to create your backup plan. When AWS Backup attempted to delete them, it lacked permission to do so.

  Expired recovery points might also be created if an AWS managed Amazon EBS or Amazon EC2 recovery point has an Amazon EBS Snapshot Lock applied and AWS Backup is unable to complete the lifecycle process that would normally result in the recovery point being deleted. Note these expired recovery points can be restored from the Amazon EC2 console and [API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-ec2.html) or Amazon EBS console and [API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-ebs.html).
**Warning**  
You will continue to store expired recovery points in your account. This might increase your storage costs.
**Note**  
AWS Backup periodically identifies orphaned AMIs - AMIs created by AWS Backup that are no longer associated with a recovery point - and places them as expired recovery points in the account's Default vault. You can then delete these expired recovery points, which also deletes the associated AMI and snapshots. If the Default vault does not exist in the Region, create one so that orphaned AMIs can be placed there as expired recovery points. You must then delete these recovery points manually.

  After August 6, 2021, AWS Backup will show the target recovery point as **Expired** in its backup vault. You can hover your mouse over the red **Expired** status for a popover status message that explains why it was unable to delete the backup. You can also choose **Refresh** to receive the most recent information.
+ You no longer want a backup plan to operate the way you configured it. Updating the backup plan affects the future recovery points it will create, but does not affect the recovery point it already created. To learn more, see [Updating a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/updating-a-backup-plan.html).
+ You need to clean up after finishing a test or tutorial.

## Deleting backups manually
<a name="deleting-backups-manually"></a>

**To manually delete recovery points**

1. In the AWS Backup console, in the navigation pane, choose **Backup vaults**.

1. On the **Backup vaults** page, choose the backup vault where you stored the backups.

1. Choose recovery points, then choose **Actions**, **Delete**.

1. 

   1. If your list contains a continuous backup, choose one of following options. Each continuous backup has a single recovery point.
      + **Permanently delete my backup data** or **Delete recovery point**. By selecting one of these options, you stop future continuous backups and also delete your existing continuous backup data.
**Note**  
See [Continuous backups and point-in-time recovery (PITR)](point-in-time-recovery.md) for Amazon S3, Amazon RDS, and Aurora continuous backup considerations.
      + **Keep my continuous backup data** or **Disassociate recovery point**. By selecting one of these options, you stop future continuous backups but retain your existing continuous backup data until it expires as defined by your retention period.

        A disassociated Amazon S3 continuous recovery point (backup) will remain in its backup vault, but its state will transition to `STOPPED`.
**Note**  
Calling `DisassociateRecoveryPoint` on an Amazon S3 continuous recovery point that is already in `EXPIRED` status has no effect. The recovery point state and configuration remain unchanged.

   1. To delete all the recovery points selected, type delete, and then choose **Delete recovery points**.

   1. AWS Backup begins to submit your recovery points for deletion and displays a progress bar. Keep your browser tab open and do not navigate away from this page during the submission process.

   1. At the end of the submission process, AWS Backup presents you a status in the banner. The status can be:
      + **Successfully submitted**. You can choose to **View progress** about each recovery point’s deletion status.
      + Failed to submit. You can choose to **View progress** about each recovery point’s deletion status or **Try again** with your submission.
      + A mixed result where some recovery points were successfully submitted while other recovery points failed to submit.

   1. If you choose **View progress**, you can review the **Deletion status** of each backup. If a deletion status is **Failed** or **Expired**, you can click that status to see the reason. You can also choose to **Retry failed deletions**.

## Troubleshooting manual deletions
<a name="deleting-backups-troubleshooting"></a>

In rare situations, AWS Backup might not complete your delete request. AWS Backup uses the service-linked role `[AWSServiceRoleForBackup](https://docs.aws.amazon.com/aws-backup/latest/devguide/using-service-linked-roles.html)` to perform deletions.

If your delete request fails, verify that your IAM role has the permission to create service-linked roles. Specifically, verify your IAM role has the `iam:CreateServiceLinkedRole` action. If it does not, add this permission to the role used to create a backup. Adding this permission allows AWS Backup to perform manual deletions.

If, after you confirm that your IAM role has the `iam:CreateServiceLinkedRole` action, your recovery points are still stuck in the `DELETING` status, we are likely investigating your issue. Complete your manual deletion with the following steps:

1. Set up a reminder to come back in 2-3 days.

1. After 2-3 days, check for recently `EXPIRED` deletion points that are the result of your first manual deletion operation.

1. Manually delete those `EXPIRED` recovery points.

For more information on roles, see [Using service-linked roles](https://docs.aws.amazon.com/aws-backup/latest/devguide/using-service-linked-roles-AWSServiceRoleForBackup.html) and [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).