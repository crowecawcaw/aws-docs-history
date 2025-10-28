# Your volume has insufficient storage capacity

If you are running out of space on your volumes, you can use the procedures shown here to
diagnose and resolve the situation.

###### Topics

- [Determine how your volume storage capacity is being used](#volume-storage-usage "#volume-storage-usage")
- [Increasing a volume's storage capacity](#increase-volume-capacity "#increase-volume-capacity")
- [Using volume autosizing](#volume-autosizing "#volume-autosizing")
- [Your file system's primary storage is full](#file-system-primary-capacity "#file-system-primary-capacity")
- [Deleting snapshots](#ts-deleting-snapshots "#ts-deleting-snapshots")
- [Increasing a volume's maximum file capacity](#max-file-capacity "#max-file-capacity")

## Determine how your volume storage capacity is being used

You can see how your volume's storage capacity is being consumed by using the `volume show-space`
NetApp ONTAP CLI command. This information can help you make decisions about how to reclaim or conserve volume
storage capacity. For more information, see [To monitor a volume's storage capacity (console)](monitor-volume-storage-console.md#volume-capacity-usage "monitor-volume-storage-console.md#volume-capacity-usage").

## Increasing a volume's storage capacity

You can increase a volume's storage capacity by using the Amazon FSx console, AWS CLI, and Amazon FSx API. For
more information about updating a volume with an increased capacity, see [Updating volumes](updating-volumes.md "updating-volumes.md").

Alternatively, you can increase a volume's storage capacity using the
[`volume modify`](https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/volume__modify.html "https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/volume__modify.html") NetApp ONTAP CLI command. For more information, see
[To change a volume's storage capacity (console)](manage-volume-capacity.md#increase-volume-size "manage-volume-capacity.md#increase-volume-size").

## Using volume autosizing

You can use volume autosizing so that a volume automatically grows by a specified amount, or to a specified size
when it reaches a used space threshold. You can do this for FlexVol volume types, which is the default volume type for
FSx for ONTAP, using the [`volume autosize`](https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/volume__autosize.html "https://docs.netapp.com/ontap-9/topic/com.netapp.doc.dot-cm-cmpr-9101/volume__autosize.html") NetApp ONTAP CLI command. For more information, see
[Enabling autosizing](enable-volume-autosizing.md "enable-volume-autosizing.md").

## Your file system's primary storage is full

If your FSx for ONTAP file system's primary storage is full, you cannot add any more data to the volumes in your file system,
even if a volume is showing that it has enough available storage capacity. You can view the amount of available primary storage
capacity in the **Monitoring & performance** tab on the file system details page in the Amazon FSx console.
For more information, see [Monitoring SSD storage utilization](monitor-fs-storage-console.md "monitor-fs-storage-console.md")

To resolve this issue, you can increase the size of your file system's primary storage tier. For more information, see
[Updating file system SSD storage and IOPS](storage-capacity-and-IOPS.md#increase-primary-storage "storage-capacity-and-IOPS.md#increase-primary-storage").

## Deleting snapshots

Snapshots are enabled by default on your volumes, using the default snapshot policy.
Snapshots are stored in the `.snapshot` directory at the root of a volume.
You can manage volume storage capacity with respect to snapshots in the following ways:

- [Manually delete snapshots](manually-delete-snapshots.md "manually-delete-snapshots.md") – reclaim storage
  capacity by deleting snapshots manually.
- [Create a snapshot autodelete policy](snapshot-autodelete-policy.md "snapshot-autodelete-policy.md") – create
  a policy that deletes snapshots more aggressively than the default snapshot policy.
- [Turn off automatic snapshots](disable-snapshots.md "disable-snapshots.md") – conserve storage capacity
  by turning off automatic snapshots.

When you delete a snapshot, you do not reclaim the amount of storage equal to the size of the snapshot you are deleting.
You can see the amount of storage you can reclaim when deleting a snapshot by using the
[volume snapshot compute-reclaimable -vserver](https://docs.netapp.com/us-en/ontap-cli-9141/volume-snapshot-compute-reclaimable.html "https://docs.netapp.com/us-en/ontap-cli-9141/volume-snapshot-compute-reclaimable.html") ONTAP
CLI command, using your data to replace `svm_name`, `vol_name`, and `snapshot_name`.

```
`fsid8970abc52::>` `volume snapshot compute-reclaimable -vserver `svm_name` -volume `vol_name` -snapshot `snapshot_name``
`A total of 667648 bytes can be reclaimed.`
```

For more information about deleting snapshots and managing snapshot policies to conserve storage capacity, see
[Deleting snapshots](snapshots-ontap.md#delete-snapshots "snapshots-ontap.md#delete-snapshots").

## Increasing a volume's maximum file capacity

An FSx for ONTAP volume can run out of file capacity when the number of available inodes, or file pointers, is exhausted.
By default, the number of available inodes on a volume is 1 for every 32KiB of volume size. For more information,
see [Volume file capacity](volume-storage-capacity.md#managing-volume-file-capacity "volume-storage-capacity.md#managing-volume-file-capacity").

The number of inodes in a volume increases commensurately with the volume's storage capacity, up to a threshold of 648 GiB.
By default, volumes that have storage capacity of 648 GiB or more all have the same number of inodes,
21,251,126. To view a volume's maximum file capacity, see [Monitoring a volume's file capacity](view-volume-file-capacity.md "view-volume-file-capacity.md").

If you create a volume larger than 648 GiB, and you want to have more that 21,251,126
inodes, you must increase the maximum number of files on the volume manually. If your volume is
running out of storage capacity, you can check its maximum file capacity. If it's nearing its
file capacity, you can manually increase it. For more information, see [To increase the maximum number of files on a volume (ONTAP CLI)](increase-volume-max-files.md#increase-max-files "increase-volume-max-files.md#increase-max-files").
