For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Restoring a backup of an Amazon Timestream table

This section describes how to restore a backup of an Amazon Timestream table.

###### Topics

- [Restoring a Timestream for LiveAnalytics table from AWS Backup](#backups-restoring-from "#backups-restoring-from")
- [Restoring a Timestream for LiveAnalytics table to another Region or
  account](#backups-restoring-to "#backups-restoring-to")

## Restoring a Timestream for LiveAnalytics table from AWS Backup

To restore your Timestream for LiveAnalytics table from AWS Backup using Timestream for LiveAnalytics console, follow these steps.

1. Sign in to the [AWS Management
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane on the left side of the console, choose
   **Backups**.
3. To restore a resource, choose the radio button next to the recovery point ID of the
   resource. In the upper-right corner of the pane, choose **Restore**.
4. Enter the table configuration settings, namely **Database name** and
   **Table Name**. Please note, the restored table name should be different
   from the original source table name.
5. Configure the memory and magnetic store retention settings.
6. For **Restore role**, choose the IAM role that AWS Backup will assume for
   this restore.
7. Choose **Restore backup**. A message at the top of the page provides
   information about the restore job.

###### Note

You are charged for restoring the entire backup irrespective of the configured memory and
magnetic store retention periods. However, once the restore is completed, your restored table
will only contain the data within the configured retention periods.

## Restoring a Timestream for LiveAnalytics table to another Region or

account

To restore a Timestream for LiveAnalytics table to another Region or account, you will first need to copy the backup
to that new Region or account. In order to copy to another account, that account must first
grant you permission. After you have copied your Timestream for LiveAnalytics backup to the new Region or account, it can
be restored with the process in the previous section.
