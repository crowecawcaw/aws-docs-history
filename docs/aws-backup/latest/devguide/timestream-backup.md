# Amazon Timestream backups

Amazon Timestream is a scalable time series database that allows storage and analysis of up
to trillions of time series data points daily. Timestream is optimized for cost and time
savings by keeping recent data in memory and by storing historical data in a cost-optimized
storage tier in accordance with your policies.

A Timestream database has tables. These tables contain records, and each record is a single
data point in a time series. A time series is a sequence of records recorded over a time
interval, such as a stock price, usage level of memory of an Amazon EC2 instance, or a temperature
reading. AWS Backup can centrally backup and restore Timestream tables. You can copy these table
backups to other accounts and several other AWS Regions within the same organization.

Timestream does not currently offer native backup and restore services, so using AWS Backup to
create secure copies of your Timestream tables can add an extra layer of security and resilience
to your resources.

## Back up Timestream tables

You can backup Timestream tables either through the AWS Backup console or using the AWS CLI.

There are two ways to use the AWS Backup console to backup a Timestream table: on demand or as part of a backup plan.

#### Create on-demand Timestream backups

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Using the navigation pane, choose **Protected resources**,
   and then **Create on-demand backup**.
3. On the **Create on-demand backup** page, choose
   Amazon Timestream.
4. Choose **Resource type** Timestream, and then choose the
   table name you want to back up.
5. In Backup window, ensure that **Create backup now** is selected.
   This initiates a backup immediately and enables you to see your cluster sooner on
   the **Protected resources** page.
6. In the drop down menu **Transition to cold storage**,
   you can set your transition settings.
7. In **Retention Period**, you can choose how long to retain
   your backup.
8. Choose an existing backup vault or create a new backup vault. Choosing
   **Create new backup vault** opens a new page to create a vault and then
   returns you to the **Create on-demand backup page** when you are finished.
9. Under **IAM role**, choose **Default role**
   (if the AWS Backup default role is not present in your account, it will be created for you
   with the correct permissions).
10. _Optionally,_ tags can be added to your recovery point.
    If you want to assign one or more tags to your on-demand backup, enter a **key**
    and optional **value**, and choose **Add tag**.
11. Choose **Create on-demand backup**. This takes you to the **Jobs**
    page, where you will see a list of jobs.
12. Choose the **Backup job ID** for the cluster to see the details of
    that job. It will display a status of `Completed`, `In Progress`, or
    `Failed`. You can click the refresh button to update the displayed status.

#### Create scheduled Timestream backups in a backup plan

Your scheduled backups can include Timestream tables if they are a protected resource. To opt into
protecting Amazon Timestream tables:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Using the navigation pane, choose **Protected resources**.
3. Toggle Amazon Timestream to **On**.
4. See
   [Assigning resources to the console](assigning-resources.md#assigning-resources-console "assigning-resources.md#assigning-resources-console") to include Timestream tables in an existing or
   new plan.

Under **Manage Backup plans**, you can choose to
[create a backup plan](creating-a-backup-plan.md "creating-a-backup-plan.md")
and include Timestream tables, or you can
[update an existing one](updating-a-backup-plan.md "updating-a-backup-plan.md")
to include Timestream tables. When adding the resource type _Timestream_, you can
choose to add **All Timestream tables**, or check the boxes next to the tables you
wish to add under **Select specific resource types**.

The first backup made of Timestream tables will be a full backup. Subsequent backups will be
incremental backups.

After you’ve created or modified your backup plan, navigate to Backup plans in the left navigation.
The backup plan you specified should display your clusters under **Resource Assignments**.

### Backing up programmatically

You can use the operation name `start-backup-job`.
Include the following parameters:

```
aws backup start-backup-job \
--backup-vault-name `backup-vault-name` \
--resource-arn arn:aws:timestream:`region`:`account`:database/`database-name`/table/`table-name` \
--iam-role-arn arn:aws:iam::`account`:role/`role-name` \
--region `AWS Region` \
--endpoint-url `URL`
```

## View Timestream table backups

To view and modify your Timestream table backups within the console:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Choose **Backup vaults**. Then, click on the backup vault name that contains your
   Timestream tables.
3. The backup vault will display a summary and a list of backups.
   1. You can click on the link in the column **Recovery point ID**, or
   2. You can check the box to the left of the recovery point ID and click **Actions**
      to delete the recovery points that are no longer needed.

## Restore a Timestream table

See how to
[restore a Timestream table](timestream-restore.md "timestream-restore.md")
