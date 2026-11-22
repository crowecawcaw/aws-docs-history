

# Deleting backups

You can delete both automatic daily backups and user-initiated backups of your volumes using the Amazon FSx console, Amazon FSx API, or AWS Command Line Interface (AWS CLI). Deleting a backup is a permanent, unrecoverable action. Any data in a deleted backup is also deleted. Do not delete a backup unless you're sure you won't need that backup again in the future. You can't delete a backup if the source volume is [offline](offline-volumes.md).

You can delete a volume while it is being restored from a backup on all FSx for ONTAP file systems. Deleting a volume during the restore effectively cancels the in-progress restore operation.

**Note**  
Amazon FSx doesn't support deleting the most recent `AVAILABLE` backup of an ONTAP volume unless all other backups of the volume have been deleted.

This restriction still applies after you delete the volume. If AWS Backup manages the volume's backups, AWS Backup can't delete the recovery point of the most recent backup when its retention period ends. You also can't delete that recovery point manually. Both requests fail with a `BadRequest` error whose message restates this restriction. Vault Lock and IAM permissions don't cause this error.

The recovery point remains in the `EXPIRED` state in your backup vault. This commonly happens when your backup plan keeps backups of the same volume for different retention periods, such as daily and monthly backups. After the volume's other backups expire or you delete them, manually delete the `EXPIRED` recovery point.

To avoid this, take a [final backup](deleting-volumes.md#final-volume-backup) when you delete a volume. The final backup becomes the volume's most recent backup. You can then delete the volume's other backups in any order. Delete the final backup last.

**Important**  
You continue to incur backup storage charges for an `EXPIRED` recovery point and for the final backup, which AWS Backup doesn't manage, until you delete them. For more information about FSx for ONTAP pricing, see [Amazon FSx for NetApp ONTAP Pricing](https://aws.amazon.com/fsx/netapp-ontap/pricing/).

To delete backups created using AWS Backup, see [Deleting backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html) in the AWS Backup Developer Guide.

**To delete a backup (console)**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. From the console dashboard, choose **Backups** from the left side navigation.

1. Choose the backup that you want to delete from the **Backups** table, and then choose **Delete backup**.

1. In the **Delete backups** dialog box that opens, confirm that the ID of the backup shown is the backup that you want to delete.

1. Confirm that the check box is checked for the backup that you want to delete.

1. Choose **Delete backups**.

Your backup and all included data are now permanently and irrecoverably deleted.

**To delete a backup (CLI)**
+ Use the delete-backup CLI command or the equivalent DeleteBackup API action to delete an FSx for ONTAP volume backup, as shown in the following example.

  ```
  $ aws fsx delete-backup --backup-id {{backup-a0123456789abcdef}}
  ```

  The system response includes the ID of the backup being deleted, and its lifecycle status with a value of `DELETED`, indicating that the request was successful.

  ```
  {
      "BackupId": "backup-a0123456789abcdef",
      "Lifecycle": "DELETED"
  }
  ```