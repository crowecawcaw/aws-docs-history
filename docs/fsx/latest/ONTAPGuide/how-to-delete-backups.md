# Deleting backups

You can delete both automatic daily backups and user-initiated backups of your volumes using the Amazon FSx console, Amazon FSx API, or AWS Command Line Interface
(AWS CLI).
Deleting a backup is a permanent, unrecoverable action. Any data in a deleted backup is
also deleted. Do not delete a backup unless you're sure you won't need that backup
again in the future. You can't delete a backup if the source volume is [offline](offline-volumes.md "offline-volumes.md").

You can delete a volume while it is being restored from a backup on all FSx for ONTAP file systems. Deleting a volume
during the restore effectively cancels the in-progress restore operation.

###### Note

Amazon FSx doesn't support deleting the most recent `AVAILABLE` backup of an ONTAP volume unless all other backups of the volume
have been deleted.

To delete backups created using AWS Backup, see
[Deleting backups](../../../aws-backup/latest/devguide/deleting-backups.md "../../../aws-backup/latest/devguide/deleting-backups.md") in the AWS Backup Developer Guide.

###### To delete a backup (console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the console dashboard, choose **Backups** from the left side
   navigation.
3. Choose the backup that you want to delete from the **Backups** table,
   and then choose **Delete backup**.
4. In the **Delete backups** dialog box that opens, confirm that the ID of
   the backup shown is the backup that you want to delete.
5. Confirm that the check box is checked for the backup that you want to delete.
6. Choose **Delete backups**.
   Your backup and all included data are now permanently and irrecoverably deleted.

###### To delete a backup (CLI)

- Use the delete-backup CLI command or the equivalent DeleteBackup API action to delete an
  FSx for ONTAP volume backup, as shown in the following example.

```
`$` `aws fsx delete-backup --backup-id `backup-a0123456789abcdef``
```

The system response includes the ID of the backup being deleted, and its lifecycle status with a value of `DELETED`,
indicating that the request was successful.

```
{
    "BackupId": "backup-a0123456789abcdef",
    "Lifecycle": "DELETED"
}
```
