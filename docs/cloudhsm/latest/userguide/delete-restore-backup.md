# Delete AWS CloudHSM cluster backups

 After you delete an AWS CloudHSM cluster backup, the service holds the backup for seven days,
 during which time you can restore the backup. After the seven-day period, you can no longer
 restore the backup. For more information about managing backups, see [Cluster backups](manage-backups.md "manage-backups.md"). 

The following table describes how to delete a backup.


Console
###### To delete a backup (console)

1. Open the AWS CloudHSM console at
 [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of
 the page.
3. In the navigation pane, choose **Backups**.
4. Choose a backup to delete.
5. To delete the selected backup, choose **Actions,
 Delete**.


The Delete backups dialog box appears.
6. Choose **Delete**.


The state of the backup changes to `PENDING_DELETE`. You can restore
 a backup that is pending deletion for up to 7 days after you request the
 deletion.

###### To list backups (AWS CLI)

* To see a list of all backups in the `PENDING_DELETION` state, run
 the **describe-backups** command and include
 `states=PENDING_DELETION` as a filter. 



```
`$` `aws cloudhsmv2 describe-backups --filters states=PENDING_DELETION``{
 "Backups": [
 {
 "BackupId": "backup-ro5c4er4aac",
 "BackupState": "PENDING_DELETION",
 "ClusterId": "cluster-dygnwhmscg5",
 "CreateTimestamp": 1534461854.64,
 "DeleteTimestamp": 1536339805.522,
 "HsmType": "hsm2m.medium",
 "Mode": "NON_FIPS",
 "NeverExpires": false,
 "TagList": []
 }
}`
```


AWS CLI
Check the status of a backup or find its ID by using the **[describe-backups](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-backups.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-backups.html")** command from the AWS CLI.


###### To delete a backup (AWS CLI)

* At a command prompt, run the **[delete-backup](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/delete-backup.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/delete-backup.html")**
 command, passing the ID of the backup to be deleted. 



```
`$` `aws cloudhsmv2 delete-backup --backup-id `<backup ID>```{
 "Backup": {
 "CreateTimestamp": 1534461854.64,
 "ClusterId": "cluster-dygnwhmscg5",
 "BackupId": "backup-ro5c4er4aac",
 "BackupState": "PENDING_DELETION",
 "DeleteTimestamp": 1536339805.522,
 "HsmType": "hsm1.medium",
 "Mode": "FIPS" 
 }
}`
```


AWS CloudHSM API
Refer to [DeleteBackup](../APIReference/API_DeleteBackup.md "../APIReference/API_DeleteBackup.md") to learn how to delete backups by using the
 API.
