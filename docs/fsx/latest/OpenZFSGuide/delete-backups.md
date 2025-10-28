# Deleting backups

Deleting a backup is a permanent, unrecoverable action. Any data in a deleted backup is also
deleted. Do not delete a backup unless you're sure you won't need that backup again in the
future.

###### Note

You can't delete backups taken by AWS Backup in the Amazon FSx console, CLI, or API. For information on deleting a backup taken by AWS Backup, see [Deleting Backups](../../../aws-backup/latest/devguide/deleting-backups.md "../../../aws-backup/latest/devguide/deleting-backups.md") in the*AWS Backup Developer Guide*.

###### To delete a backup

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the console dashboard, choose **Backups** from the left side
   navigation.
3. From the **Backups** table, choose the backup that you want
   to delete.
4. For **Actions**, choose **Delete backup**.
5. In the **Delete backups** dialog box that opens, confirm that the ID of
   the backup identifies the backup that you want to delete.
6. Confirm that the check box is checked for the backup that you want to delete.
7. Choose **Delete backups**.
   Your backup and all included data are now permanently and irrecoverably deleted.
