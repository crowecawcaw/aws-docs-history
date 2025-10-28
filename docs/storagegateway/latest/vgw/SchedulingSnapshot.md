# Editing a snapshot schedule

For stored volumes, AWS Storage Gateway creates a default snapshot schedule of once a day.

###### Note

You can't remove the default snapshot schedule. Stored volumes require at
least one snapshot schedule. However, you can change a snapshot schedule by
specifying either the time the snapshot occurs each day or the frequency (every 1,
2, 4, 8, 12, or 24 hours), or both.

For cached volumes, AWS Storage Gateway doesn't create a default snapshot schedule. No default
schedule is created because your data is stored in Amazon S3, so you don't need snapshots or
a snapshot schedule for disaster recovery purposes. However, you can set up a snapshot
schedule at any time if you need to. Creating snapshot for your cached volume provides
an additional way to recover your data if necessary.

By using the following steps, you can edit the snapshot schedule for a volume.

###### To edit the snapshot schedule for a volume

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose **Volumes**, and then choose
   the volume the snapshot was created from.
3. For **Actions**, choose **Edit snapshot
   schedule**.
4. In the **Edit snapshot schedule** dialog box, modify the
   schedule, and then choose **Save**.
