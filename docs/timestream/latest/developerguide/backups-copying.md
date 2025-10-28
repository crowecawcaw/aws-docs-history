For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Copying a backup of a Amazon Timestream table

You can make a copy of a current backup. You can copy backups to multiple AWS accounts or
AWS Regions on demand or automatically as part of a scheduled backup plan. Cross-Region
replication is especially valuable if you have business continuity or compliance requirements to
store backups a minimum distance away from your production data.

Cross-account backups are useful for securely copying your backups to one or more AWS
accounts in your organization for operational or security reasons. If your original backup is
inadvertently deleted, you can copy the backup from its destination account to its source
account, and then start the restore. Before you can do this, you must have two accounts that
belong to the same organization in the Organizations service and required permissions for the
accounts. When you copy an incremental backup into another account or Region, the associated full
backup is also copied.

Copies inherit the source backup's configuration unless you specify otherwise. There is one
exception. If you specify your new copy to "Never" expire. With this setting, the new copy still
inherits its source expiration date. If you want your new backup copy to be permanent, either set
your source backups to never expire, or specify your new copy to expire 100 years after its
creation.

To copy a backup from Timestream console, follow these steps.

1. Sign in to the [AWS Management
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane on the left side of the console, choose
   **Backups**.
3. Choose the radio button next to the recovery point ID of the resource. In the upper-right
   corner of the pane, select **Actions** and choose
   **Copy**.
4. Select **Continue to AWS Backup** and follow the steps for [Cross account backup](../../../aws-backup/latest/devguide/cross-region-backup.md "../../../aws-backup/latest/devguide/cross-region-backup.md").
   Copying on-demand and scheduled backups across accounts and Regions is not natively
   supported in the Timestream for LiveAnalytics console currently and you have to navigate to AWS Backup to perform the
   operation.
