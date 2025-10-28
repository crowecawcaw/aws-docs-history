# Backup and tag edits

After you create a backup using AWS Backup, you can change the lifecycle or tags of the backup.
The lifecycle defines when a backup is transitioned to cold storage and when it expires. AWS Backup
transitions and expires backups automatically according to the lifecycle that you
define.

To see the list of resources that you can transition to cold storage, see the "Lifecycle
to cold storage" section of the [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. The cold storage expression is ignored for
other resources.

###### Note

Editing the tags of a backup using the AWS Backup console is only supported for backups of Amazon Elastic File System
(Amazon EFS) file systems and Advanced Amazon DynamoDB.

Tags that were added to the recovery point on creation
for other resources will still appear, but will be greyed out and uneditable.
Even though these tags are not editable in the AWS Backup console, you can edit the tags of these other
services' backups using the service’s console or API.

Backups that are transitioned to cold storage must be stored in cold storage for a minimum
of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to
cold after days” setting. When you update the “transition to cold after days” setting, the
value must be a minimum of the backup’s age plus one day. The “transition to cold after days”
setting cannot be changed after a backup has been transitioned to cold.

The following is an example of how to update the lifecycle of a backup.

###### To edit the lifecycle of a backup

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Backup vaults**.
3. In the **Backups** section, choose a backup.
4. On the backup details page, choose **Edit**.
5. Configure the lifecycle settings, and then choose **Save**.
