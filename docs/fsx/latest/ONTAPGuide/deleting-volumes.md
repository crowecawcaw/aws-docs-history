

# Deleting volumes
<a name="deleting-volumes"></a>

You can delete an FSx for ONTAP volume using the Amazon FSx console, the AWS CLI, and the Amazon FSx API, in addition to the NetApp ONTAP command line interface (CLI) and REST API.

Before you delete a volume, make sure that no applications are accessing the data in the volume that you want to delete.

**Important**  
You can only delete volumes using the Amazon FSx console, API, or CLI if the volume has Amazon FSx backups enabled.

## Taking a final volume backup
<a name="final-volume-backup"></a>

When you delete a volume using the Amazon FSx console, you have the option to take a final backup of the volume. As a best practice, we recommend that you choose to take a final backup. If you find you don't need it after a certain period of time, you can delete this and other manually created volume backups. When you delete a volume by using the `delete-volume` CLI command, Amazon FSx takes a final backup by default.

For more information about volume backups, see [Protecting your data with volume backups](using-backups.md).

## To delete a volume (console)
<a name="delete-volume-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, choose **File systems**, and then choose the ONTAP file system that you want to delete a volume from.

1. Choose the **Volumes** tab.

1. Choose the volume that you want to delete.

1. For **Actions**, choose **Delete volume**.

1. (SnapLock Enterprise volumes only) For **Bypass SnapLock Enterprise Retention**, choose **Yes**. 

1. In the confirmation dialog box, for **Create final backup**, you have two options:
   + Choose **Yes** to take a final backup of the volume. The name of the final backup is displayed.
   + Choose **No** if you don't want a final backup of the volume. You are asked to acknowledge that once the volume is deleted, automatic backups are no longer available.

1. Confirm the volume deletion by entering **delete** in the **Confirm delete** field.

1. Choose **Delete volume(s)**.

## To delete a volume (CLI)
<a name="delete-volume-cli"></a>
+ To delete an FSx for ONTAP volume, use the [delete-volume](https://docs.aws.amazon.com/cli/latest/reference/fsx/delete-volume.html) CLI command (or the equivalent [DeleteVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteVolume.html) API operation), as shown in the following example.

  ```
  aws fsx delete-volume --volume-id fsvol-1234567890abcde
  ```