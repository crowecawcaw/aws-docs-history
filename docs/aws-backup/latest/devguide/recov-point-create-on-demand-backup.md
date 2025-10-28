# Creating an on-demand backup using AWS Backup

On the AWS Backup console, the **Protected resources** page lists resources
that have been backed up by AWS Backup at least once. If you’re using AWS Backup for the first time,
there aren’t any resources (such as Amazon EBS volumes or Amazon RDS databases) listed on this page.
This is true even if a resource was assigned to a backup plan and that backup plan has not
run a scheduled backup job at least once.

Note: An on-demand backup begins to back up your resource immediately. You can choose
an on-demand backup if you wish to create a backup at a time other than the scheduled time
defined in a backup plan. An on-demand backup can be used, for example, to test backup and
functionality at any time.

On-demand backups cannot be used with
point-in-time recovery (PITR), because an on-demand backup preserves resources
in the state they are in when the backup is taken, but PITR uses
[continuous backups](point-in-time-recovery.md#point-in-time-recovery-working-with "point-in-time-recovery.md#point-in-time-recovery-working-with"), which record changes over a period of time.

###### Considerations

- If the AWS Backup default role is not present in your account, one is created for
  you with the correct permissions.
- When backups expire and are marked for deletion as part of your lifecycle policy,
  AWS Backup deletes the backups at a randomly chosen point over the following 8 hours. This
  window helps ensure consistent performance.
- For Amazon EC2 resources, AWS Backup automatically copies existing group and individual
  resource tags, in addition to any tags that you add in this step.
- AWS Backup takes EC2 backups with "no reboot" as the default behavior. AWS Backup currently
  supports resources running on Amazon EC2, and certain instance types are not supported. For
  more information, see [Create Windows VSS backups](windows-backups.md "windows-backups.md").

###### To create an on-demand backup

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. On the dashboard, choose **Create an on-demand backup**. Or, in the
   navigation pane, choose **Protected resources** and then choose
   **Create an on-demand backup**.
3. For **Resource type** page, choose the resource type
   that you want to back up. For example, choose **DynamoDB** for Amazon DynamoDB
   tables.
4. Choose the name or ID of the resource to protect. For example,
   choose the name of the DynamoDB table for Amazon DynamoDB.
5. Ensure that **Create backup now** is selected.
6. If the resource type supports transition to cold storage, **Cold storage**
   is present. For more information, see the **Lifecycle to cold storage**
   column in table [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource").

To specify when this backup goes to cold storage, choose **Move backups from
warm to cold storage** and then specify the time in warm storage. 7. For **Total retention period**, specify the number of days. If you
specified time in cold storage, the retention period is divided between warm and cold
storage. 8. Choose an existing **Backup vault** or create a new one. Choosing
**Create new Backup vault** opens a new page to create a vault and
then returns you to the **Create on-demand backup** page when you are
finished. 9. For **IAM role**, choose the default role or a role that you
created. 10. To assign a tag to your on-demand backup, expand **Tags added to recovery
points**, choose **Add new tag**, and enter a tag key and
tag value. 11. **Advanced backup settings** options vary by resource type:

    * For **EC2** resources: To take application-consistent snapshots using Windows Volume Shadow Copy
     Service (VSS), choose **Windows VSS**.
    * For **Amazon S3** resources: You can choose to exclude Access Control Lists (ACLs)
     from your backup by leaving **Backup Access Control Lists (ACLs)** unselected.

12. Choose **Create on-demand backup**. This opens the
    **Jobs** page, where you can see a list of jobs and view
    job status.
