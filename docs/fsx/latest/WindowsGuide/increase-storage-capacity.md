# Increasing file system storage capacity

You can increase your FSx for Windows File Server file system's storage capacity as your storage requirements change. Use
the Amazon FSx console, the AWS CLI, or the Amazon FSx API to increase a file system's storage capacity as described in the
following procedures. For more information, see [Managing storage capacity](managing-storage-configuration.md#managing-storage-capacity "managing-storage-configuration.md#managing-storage-capacity").

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems** and choose the Windows
   file system that you want to increase storage capacity for.
3. For **Actions**, choose **Update
   storage**. Or, in the **Summary** panel,
   choose **Update** next to the file system's
   **Storage capacity**.

The **Update storage capacity** window
appears. 4. For **Input type**, choose
**Percentage** to enter the new storage capacity as
a percentage change from the current value, or choose
**Absolute** to enter the new value in GiB. 5. Enter the **Desired storage capacity**.

###### Note

The desired capacity value must be at least 10 percent larger than
the current value, up to the maximum value of 65,536 GiB. 6. Choose **Update** to initiate the storage capacity
update. 7. You can monitor the update progress on the **File
systems** detail page, in the **Updates**
tab.
To increase the storage capacity for an FSx for Windows File Server file system, use the
AWS CLI command [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md"). Set the following parameters:

- `--file-system-id` to the ID of the file system you are
  updating.
- `--storage-capacity` to a value that is at least 10 percent
  greater than the current value.
  You can monitor the progress of the update by using the AWS CLI command [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md"). Look for the
  `administrative-actions` in the output.

For more information, see [AdministrativeAction](../APIReference/API_AdministrativeAction.md "../APIReference/API_AdministrativeAction.md").
