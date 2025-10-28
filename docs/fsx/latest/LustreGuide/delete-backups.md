# Deleting backups

Deleting a backup is a permanent, unrecoverable action. Any data in a deleted backup is also
deleted. Do not delete a backup unless you're sure you won't need that backup again in the
future. You can't delete backups taken by AWS Backup in the Amazon FSx
console, CLI, or API.

###### To delete a backup

1. Open the Amazon FSx for Lustre console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the console dashboard, choose **Backups** from the left side
   navigation.
3. Choose the backup that you want to delete from the **Backups** table, and
   then choose **Delete backup**.
4. In the **Delete backups** dialog box that opens, confirm that the ID of
   the backup identifies the backup that you want to delete.
5. Confirm that the check box is checked for the backup that you want to delete.
6. Choose **Delete backups**.
   Your backup and all included data are now permanently and unrecoverably deleted.
