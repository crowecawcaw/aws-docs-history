# Deleting backups

You can delete any user-initiated and automatic daily backups of your file system using the
Amazon FSx console, CLI, or API, described in the following procedures. For deleting backups taken by
AWS Backup, which have type of **AWS Backup**,
you must use the the AWS Backup console, CLI, or API. Deleting a backup is a permanent, unrecoverable action.
Any data in a deleted backup is also deleted. Do not delete a backup unless you're sure you
won't need that backup again in the future.

###### To delete a backup (console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the console dashboard, choose **Backups** from the left side
   navigation.
3. Choose the backup that you want to delete from the **Backups** table, and
   then choose **Delete backup**.
4. In the **Delete backups** dialog box that opens, confirm that the ID of
   the backup identifies the backup that you want to delete.
5. Confirm that the check box is checked for the backup that you want to delete.
6. Choose **Delete backups**.
   Your backup and all included data are now permanently and unrecoverably deleted.
