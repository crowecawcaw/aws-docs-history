# Deleting an Amazon FSx for OpenZFS volume

This section provides information on how to delete an FSx for OpenZFS volume using the Amazon FSx console, the AWS CLI, and the
Amazon FSx API.

When you delete a volume, the operation has the following results:

- Deletes all data in the volume
- Deletes all snapshots
- Deletes all child volumes and their snapshots

###### Note

You cannot delete a root volume. You also cannot delete any volumes from
a client mount (for example, with a `rm -r /fsx/vol1` command).

Before you delete a volume, make sure you have confirmed the following:

- Make sure that no applications are accessing the data in the volume
  that you want to delete.
- Make sure there are no Amazon S3 access points attached to the volume.
  For information on how to list S3 access points attached to FSx for OpenZFS volumes,
  see [Listing S3 access point attachments](access-points-list.md "access-points-list.md").
  For information on how to delete S3 access points,
  see [Deleting an S3 access point attachment](delete-access-point.md "delete-access-point.md").

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose **File systems**, and then choose the
   FSx for OpenZFS file system that you want to delete a volume from.
3. Choose the **Volumes** tab.
4. Choose the volume that you want to delete.
5. For **Actions**, choose **Delete volume**.
6. In the delete dialog, do the following:
   1. Acknowledge that you understand the results of deleting the volume.
   2. Confirm the volume deletion by entering **delete** in the
      **Confirm delete** field.

7. Choose **Delete volume(s)**.

- To delete an FSx for OpenZFS volume, use the [delete-volume](../../../cli/latest/reference/fsx/delete-volume.md "../../../cli/latest/reference/fsx/delete-volume.md") CLI command (or the equivalent [DeleteVolume](../APIReference/API_DeleteVolume.md "../APIReference/API_DeleteVolume.md") API operation), as shown in the following
  example.

```
`aws fsx delete-volume --volume-id fsxvol-0123456789abcdef1`
```
