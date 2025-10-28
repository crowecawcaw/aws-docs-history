# Updating throughput capacity

You can modify a file system's throughput capacity using the Amazon FSx console, the AWS Command Line Interface
(AWS CLI), or the Amazon FSx API.

###### Note

You must wait a minimum of six hours between updating the throughput capacity for second-generation file systems.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems**, and choose the ONTAP file system
   that you want to increase the throughput capacity for.
3. For **Actions**, choose **Update throughput
   capacity**. Or, in the **Summary** panel, choose
   **Update** next to the file system's **Throughput
   capacity**.
4. Choose the new value for **Throughput capacity** from the
   list.
5. Choose **Update** to initiate the throughput capacity
   update.
6. You can monitor the update progress on the **File systems**
   detail page, on the **Updates** tab.

You can monitor the progress of the update by using the Amazon FSx console, the AWS CLI,
and the API. For more information, see [Monitoring throughput capacity
changes](monitoring-throughput-capacity-changes.md "monitoring-throughput-capacity-changes.md").
To modify a file system's throughput capacity, use the AWS CLI command [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md"). Set the following parameters:

- `--file-system-id` to the ID of the file system that you are
  updating.
- `ThroughputCapacity` to the desired value to update the file system to.
  You can monitor the progress of the update by using the Amazon FSx console, the AWS CLI, and
  the API. For more information, see [Monitoring throughput capacity
  changes](monitoring-throughput-capacity-changes.md "monitoring-throughput-capacity-changes.md").
