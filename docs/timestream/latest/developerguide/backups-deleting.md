For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Deleting backups

This section describes how to delete a backup of a Timestream for LiveAnalytics table.

To delete a backup from Timestream console, follow these steps.

1. Sign in to the [AWS Management
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane on the left side of the console, choose
   **Backups**.
3. Choose the radio button next to the recovery point ID of the resource. In the upper-right
   corner of the pane, select **Actions** and choose
   **Delete**.
4. Select **Continue to AWS Backup** and follow the steps for deleting
   backups at [Deleting backups](../../../aws-backup/latest/devguide/deleting-backups.md "../../../aws-backup/latest/devguide/deleting-backups.md").

###### Note

When you delete a backup that is incremental, only the incremental backup is deleted and the
underlying full backup is not deleted.
