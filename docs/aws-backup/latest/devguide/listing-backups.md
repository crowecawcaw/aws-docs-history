

# View existing backups
<a name="listing-backups"></a>

You can view a list of your backups using the [AWS Backup console](https://console.aws.amazon.com/backup) or programmatically.

**Topics**
+ [Listing backups by protected resource in the console](#list-backups-by-protected-resources)
+ [Listing backups by backup vault in the console](#list-backups-by-vault)
+ [Listing backups programmatically](#list-backups-programmatically)

## Listing backups by protected resource in the console
<a name="list-backups-by-protected-resources"></a>

Follow these steps to view a list of backups of a particular resource on the AWS Backup console. 

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the navigation pane, choose **Protected resources**.

1. Choose a protected resource in the list to view the list of backups. Only resources that have been backed up by AWS Backup are listed under **Protected resources**. 

You can view the backups for the resource. From this view, you can also choose a backup and restore it.

## Listing backups by backup vault in the console
<a name="list-backups-by-vault"></a>

Follow these steps to view a list of backups organized in a backup vault.

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the navigation pane, choose **Backup vaults**.

1. In the **Backups** section, view the list of all the backups organized in this backup vault. In this view, you can sort backups by any of the column headers (including status), as well as select a backup to restore it, edit it, or delete it.

## Listing backups programmatically
<a name="list-backups-programmatically"></a>

You can list backups programmatically using the `ListRecoveryPoint` API operations:
+ `[ListRecoveryPointsByBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByBackupVault.html)`
+ `[ListRecoveryPointsByResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByResource.html)`

For example, the following AWS Command Line Interface (AWS CLI) command lists all your backups with the `EXPIRED` status:

```
aws backup list-recovery-points-by-backup-vault \
  --backup-vault-name {{sample-vault}} \
  --query 'RecoveryPoints[?Status == `EXPIRED`]'
```