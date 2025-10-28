# Update a backup plan

After creating a backup plan, you can edit the plan—for example, you can add tags,
or you can add, edit, or delete backup rules. Any changes that you make to a backup plan have
no effect on existing backups created by the backup plan. The changes apply only to backups
that are created in the future.

For example, when you update the retention period in a backup rule, the retention period
of backups created before you made the update remain the same. Any backups that are created by
that rule going forward reflect the updated retention period.

You can't change the name of a plan after it is created.

###### To edit a backup plan using the AWS Backup console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Backup plans**.
3. Under the second pane, **Backup plans**, existing back plans are
   displayed. Select the underlined link in the column **Backup plan name**
   to see details of the chosen backup plan.
4. You can edit a backup rule, view resource assignments, view backup jobs, manage tags,
   or change Windows VSS settings.
5. To update a backup rule, select the name of the backup rule.

Select **Manage tags** to add or delete tags.

Select **Edit** next to **Advanced backup settings**
to turn Windows VSS on or off. 6. Change the setting(s) you prefer, and then select
**Save**.
