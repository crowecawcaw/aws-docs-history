For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Creating backups of Amazon Timestream tables

This section describes how to enable AWS Backup and create on-demand and scheduled backups for
Amazon Timestream.

###### Topics

- [Enabling AWS Backup to protect Timestream for LiveAnalytics data](#backups-enabling "#backups-enabling")
- [Creating on-demand backups](#backups-on-demand "#backups-on-demand")
- [Scheduled backups](#backups-scheduled "#backups-scheduled")

## Enabling AWS Backup to protect Timestream for LiveAnalytics data

You must enable AWS Backup to use it with Timestream for LiveAnalytics.

To enable AWS Backup in the Timestream for LiveAnalytics console, perform the following steps.

1. Sign in to the [AWS Management
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. A pop-up banner appears at the top of your Timestream for LiveAnalytics dashboard page to enable AWS Backup to support
   Timestream for LiveAnalytics data. Otherwise, from the navigation pane, choose **Backups**.
3. In the **Backup** window, you will see the banner to enable AWS Backup.
   Choose **Enable**.

Data Protection through AWS Backup is now available for your Timestream for LiveAnalytics tables.

To enable through AWS Backup, refer to AWS Backup documentation to enable via console and
programmatically.

If you choose to disable AWS Backup from protection your Timestream for LiveAnalytics data after those have been enabled,
log in through AWS Backup console and move the toggle to the left.

If you can’t enable or disable the AWS Backup features, your AWS admin may need to perform
those actions.

## Creating on-demand backups

To create an on-demand backup of a Timestream for LiveAnalytics table, follow these steps.

1. Sign in to the [AWS Management
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane on the left side of the console, choose
   **Backups**.
3. Choose **Create on-demand backup**.
4. Continue to select the settings in the backup window.
5. You can either create a backup now, initiates a backup immediately, or select a backup
   window to start the backup.
6. Select the lifecycle management policy of your backup. You can transition your backup
   data into cold storage where you have to retain the backup for a minimum of 90 days. You can
   set the required retention period for your backup You can either select an existing vault or
   or select **create new backup vault** to navigate to AWS Backup console and create
   a new backup vault <documentation link on creating a new backup vault here>
7. Select the appropriate IAM role.
8. If you want to assign one or more tags to your on-demand backup, enter a
   **key** and optional **value**, and choose **Add
   tag**.
9. Choose to create an on-demand backup. This takes you to the **Backup**
   page, where you will see a list of jobs.
10. Choose the **Backup job ID** for the resource that you chose to back up
    to see the details of that job.

## Scheduled backups

To schedule a backup, refer to [Create a scheduled
backup](../../../aws-backup/latest/devguide/create-a-scheduled-backup.md "../../../aws-backup/latest/devguide/create-a-scheduled-backup.md").
