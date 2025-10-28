# Troubleshooting SSD decrease operation issues

This section describes common issues and resolutions related to SSD capacity decrease operations.

###### Topics

- [Your SSD decrease operation is paused due to high SSD utilization](#ssd-decrease-paused-high-utilization "#ssd-decrease-paused-high-utilization")
- [Your SSD decrease operation is paused due to FlexClone relationships](#ssd-decrease-flexclone-relationship "#ssd-decrease-flexclone-relationship")
- [Redirecting client access for volume(s) failed during SSD decrease](#ssd-decrease-redirect-client-access-failed "#ssd-decrease-redirect-client-access-failed")
- [Your SSD decrease operation is taking longer than expected](#ssd-decrease-operation-duration "#ssd-decrease-operation-duration")

## Your SSD decrease operation is paused due to high SSD utilization

If your SSD storage tier exceeds 80% utilization during a decrease operation, Amazon FSx automatically pauses the operation. You might see an Administrative Actions message similar to:

```
Your file system has insufficient free space in aggr_1. Please free up space or increase your file system's storage capacity.
```

The operation will resume once utilization falls below 80%. To resolve this issue, you can do the following:

- Delete unnecessary data from volumes that have already been moved to the new disks.
- Tier more data to the capacity pool by modifying volume tiering policies.
- Submit a request to increase SSD capacity by calling [`update-file-system`](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md") with a new target value.

You should update your file system's SSD storage capacity so that your file system's resulting SSD capacity doesn't exceed 80% utilization after the decrease operation. For more details, see [Updating file system SSD storage and IOPS](storage-capacity-and-IOPS.md#increase-primary-storage "storage-capacity-and-IOPS.md#increase-primary-storage").

You can identify which volumes have been moved to the new disks by checking the `Message` field in the `STORAGE_OPTIMIZATION` administrative action.

You can also call [`describe-volumes`](../../../cli/latest/reference/fsx/describe-volumes.md "../../../cli/latest/reference/fsx/describe-volumes.md") if the aggregate is `aggr1` or `aggr1_old`.

## Your SSD decrease operation is paused due to FlexClone relationships

If FlexClone volumes are created after initiating an SSD decrease operation, Amazon FSx pauses the operation until the clones are deleted. This is because ONTAP splits clone relationships while moving volumes, which would result in duplicated storage on the new disks. To resolve this issue, you can identify and delete any FlexClone volumes that were created after the decrease operation started.

After you delete all FlexClone volumes, the decrease operation will automatically resume.

## Redirecting client access for volume(s) failed during SSD decrease

During an SSD decrease operation, Amazon FSx needs to redirect client access from the old disks to the new disks for each volume. If this process fails, you might see an Administrative Actions message similar to:

```
Redirecting client access for volume(s) fsvol-123 has failed due to insufficient SSD IOPS, throughput capacity, or because the volume is full.
```

To resolve this issue, you can do the following:

- Check your file system's resource utilization metrics in Amazon CloudWatch to ensure that your workload isn't consuming more than 50% of the following resources:
  - `NetworkThroughputUtilization`
  - `FileServerDiskThroughputUtilization`
  - `FileServerDiskIopsUtilization`
  - `CPUUtilization`
  - `DiskIopsUtilization`

- If the volume is full, increase the volume's storage capacity.
- Reduce the workload on your file system during the decrease operation.

After addressing these issues, Amazon FSx will automatically retry to redirect client access once an hour.

## Your SSD decrease operation is taking longer than expected

The time required to complete an SSD decrease operation depends on several factors, including the amount of data stored on the file system, ongoing workload activity, and available system resources. If your operation is taking longer than expected, you can do the following:

- Verify that your file system has adequate resources available (less than 50% CPU, disk throughput, and SSD IOPS utilization).
- Reduce write-heavy workloads during the operation to minimize resource contention.

You can track the progress of the operation by checking the `ProgressPercent` property in the `STORAGE_OPTIMIZATION` administrative action.
