# Modifying throughput capacity

You can increase or decrease your file system's throughput capacity using the Amazon FSx console, the
AWS Command Line Interface (AWS CLI), or the Amazon FSx API, as described in the following procedures.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems**, and choose the Windows file system that you
   want to increase the throughput capacity for.
3. For **Actions**, choose **Update throughput**.

Or, in the
**Summary** panel, choose **Update** next to the file
system's **Throughput capacity**.

The **Update throughput capacity** window appears. 4. Choose the new value for **Throughput capacity** from the list. 5. Choose **Update** to initiate the throughput capacity update.

###### Note

Multi-AZ file systems fail over and fail back when updating throughput scaling, and are fully
available. Single-AZ file systems experience a very brief period of unavailability during
the update. 6. You can monitor the update progress on the **File systems** detail page,
in the **Updates** tab.

You can monitor the progress of the update by using the Amazon FSx console, the AWS CLI, and
the API. For more information, see [Monitoring throughput capacity updates](monitoring-throughput-capacity-changes.md "monitoring-throughput-capacity-changes.md").
To increase or decrease a file system's throughput capacity, use the AWS CLI command [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md"). Set the following parameters:

- `--file-system-id` to the ID of the file system that you are updating.
- `ThroughputCapacity` to the desired value; valid values are 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4608, 6144, 9216, 12288 MBps.
  You can monitor the progress of the update by using the Amazon FSx console, the AWS CLI, and the
  API. For more information, see [Monitoring throughput capacity updates](monitoring-throughput-capacity-changes.md "monitoring-throughput-capacity-changes.md").
