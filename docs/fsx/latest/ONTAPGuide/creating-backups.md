# Creating user-initiated backups

The following procedure describes how to create a user-initiated
backup of a volume.

You cannot create a volume backup if the volume is offline. For more information, see
[Viewing offline volumes](offline-volumes.md "offline-volumes.md").

###### To create a user-initiated backup (console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems** and choose the ONTAP file system that you
   want to back up a volume for.
3. Choose the **Volumes** tab.
4. Choose the volume you want to back up.
5. From **Actions**, choose **Create backup**.
6. In the **Create backup** dialog box that opens, provide a name for your
   backup. Backup names can be a maximum of 256 Unicode characters, including letters, white
   space, numbers, and the special characters . + - = \_ : /
7. Choose **Create backup**.
   You have now created a backup of one of your file system's volumes. You can see all of
   your backups in the Amazon FSx console by choosing **Backups** in the
   left side navigation. You can search for the name you gave your backup, and the table filters
   to only show matching results.

When you create a user-initiated backup as this procedure described, it has the type
`USER_INITIATED`, and it has the `CREATING` status until it is fully
available.
