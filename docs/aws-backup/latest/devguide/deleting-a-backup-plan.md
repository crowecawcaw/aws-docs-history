# Delete a backup plan

You can delete a backup plan only after all associated selections of resources have been
deleted. These selections are also known as _resource assignments_. If
these have not been deleted prior to deletion of the backup plan, the console will display the
error: "Related backup plan selections must be deleted prior to backup plan deletion." Use the
console or use [`DeleteBackupSelection`](API_DeleteBackupSelection.md "API_DeleteBackupSelection.md").

Deleting a backup plan deletes the current version of the plan. The current and
previous versions, if any, still exist, but they are no longer listed on the console under
**Backup plans**.

###### Note

When a backup plan is deleted, existing backups are not deleted. To remove existing
backups, delete them from the backup vault using the steps in [Deleting backups](deleting-backups.md "deleting-backups.md").

###### To delete a backup plan using the AWS Backup console

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane on the left, choose **Backup plans**.
3. Choose your backup plan in the list.
4. Select any resource assignments that are associated with the backup plan.
5. Choose **Delete**.
