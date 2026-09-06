

# Delete a backup plan
<a name="deleting-a-backup-plan"></a>

You can delete a backup plan only after all associated selections of resources have been deleted. These selections are also known as *resource assignments*. If these have not been deleted prior to deletion of the backup plan, the console will display the error: "Related backup plan selections must be deleted prior to backup plan deletion." Use the console or use [`DeleteBackupSelection`](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupSelection.html).

Deleting a backup plan deletes the current version of the plan. The current and previous versions, if any, still exist, but they are no longer listed on the console under **Backup plans**.

**Note**  
When a backup plan is deleted, existing backups are not deleted. To remove existing backups, delete them from the backup vault using the steps in [Deleting backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html).

**To delete a backup plan using the AWS Backup console**

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the navigation pane on the left, choose **Backup plans**.

1. Choose your backup plan in the list.

1. Select any resource assignments that are associated with the backup plan.

1. Choose **Delete**.