# Restore AWS CloudHSM backups

AWS CloudHSM holds deleted backups for seven days, during which time you can restore the backup.
After the seven-day period, you can no longer restore the backup. For more information about
managing backups, see [Cluster backups](manage-backups.md "manage-backups.md").

The following table describes how to delete a backup.

Console

###### To restore a backup (console)

1. Open the AWS CloudHSM console at
   [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of
   the page.
3. In the navigation pane, choose **Backups**.
4. Choose a backup in the `PENDING_DELETE` state to restore.
5. To restore the selected backup, choose **Actions,
   Restore**.

AWS CLI

###### To restore a backup (AWS CLI)

- To restore a backup, issue the **[restore-backup](../../../cli/latest/reference/cloudhsmv2/restore-backup.md "../../../cli/latest/reference/cloudhsmv2/restore-backup.md")** command, passing the ID of a backup that is in
  the `PENDING_DELETION` state.

````
`$` `aws cloudhsmv2 restore-backup --backup-id `<backup ID>```{
 "Backup": {
 "ClusterId": "cluster-dygnwhmscg5",
 "CreateTimestamp": 1534461854.64,
 "BackupState": "READY",
 "BackupId": "backup-ro5c4er4aac"
 }
}`
````

AWS CloudHSM API
Refer to [RestoreBackup](../APIReference/API_RestoreBackup.md "../APIReference/API_RestoreBackup.md") to
learn how to restore backups by using the API.
