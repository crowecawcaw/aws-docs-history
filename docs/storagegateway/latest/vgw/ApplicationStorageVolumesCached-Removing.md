# Deleting storage

volumes

You might need to delete a volume as your application needs change—for example,
if you migrate your application to use a larger storage volume. Before you delete a
volume, make sure that there are no applications currently writing to the volume. Also,
make sure that there are no snapshots in progress for the volume. If a snapshot schedule
is defined for the volume, you can check it on the **Snapshot
Schedules** tab of the Storage Gateway console. For more information, see [Editing a snapshot schedule](SchedulingSnapshot.md "SchedulingSnapshot.md").

You can delete volumes using the Storage Gateway console or the Storage Gateway API. For information
on using the Storage Gateway API to remove volumes, see [Delete Volume](../APIReference/API_DeleteVolume.md "../APIReference/API_DeleteVolume.md"). The following
procedure demonstrates using the console.

Before you delete a volume, back up your data or take a snapshot of your critical
data. For stored volumes, your local disks aren't erased. After you delete a volume, you
can't get it back.

###### To delete a volume

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Volumes**, then select one or more volumes to
   delete.
3. For **Actions** choose **Delete volume**.
   The confirmation dialog box appears.
4. Verify that you want to delete the specified volumes, then type the word
   _delete_ in the confirmation box and choose
   **Delete**.
