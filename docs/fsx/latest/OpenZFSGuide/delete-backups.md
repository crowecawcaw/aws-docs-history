

# Deleting backups
<a name="delete-backups"></a>

Deleting a backup is a permanent, unrecoverable action. Any data in a deleted backup is also deleted. Do not delete a backup unless you're sure you won't need that backup again in the future. 

**Note**  
You can't delete backups taken by AWS Backup in the Amazon FSx console, CLI, or API. For information on deleting a backup taken by AWS Backup, see [Deleting Backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html) in the*AWS Backup Developer Guide*.

**To delete a backup**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. From the console dashboard, choose **Backups** from the left side navigation.

1. From the **Backups** table, choose the backup that you want to delete.

1. For **Actions**, choose **Delete backup**.

1. In the **Delete backups** dialog box that opens, confirm that the ID of the backup identifies the backup that you want to delete.

1. Confirm that the check box is checked for the backup that you want to delete.

1. Choose **Delete backups**.

Your backup and all included data are now permanently and irrecoverably deleted.