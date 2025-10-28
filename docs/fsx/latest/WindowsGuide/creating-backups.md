# Creating user-initiated backups

In addition to automatic daily file system backups, you can create a user-initiated
file system backup at anytime, using the Amazon FSx console as described in the following procedure.

###### To create a user-initiated file system backup

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the console dashboard, choose the name of the file system that you want to back
   up.
3. From **Actions**, choose **Create backup**.
4. In the **Create backup** dialog box that opens, provide a name for your
   backup. Backup names can be a maximum of 256 Unicode characters, including letters, white
   space, numbers, and the special characters . + - = \_ : /
5. Choose **Create backup**.
   You have now created your file system backup. You can find a table of all your backups in
   the Amazon FSx console by choosing **Backups** in the left side navigation. Your new
   user-initiated backup has the type `USER_INITIATED`, and its status is `CREATING`
   until it becomes `AVAILABLE`. For more information, see
   [Working with user-initiated backups](using-backups.md#user-initiated-backups "using-backups.md#user-initiated-backups").
