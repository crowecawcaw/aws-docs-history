

# Increasing file system storage capacity
<a name="increase-storage-capacity"></a>

You can increase your FSx for Windows File Server file system's storage capacity as your storage requirements change. Use the Amazon FSx console, the AWS CLI, or the Amazon FSx API to increase a file system's storage capacity as described in the following procedures. For more information, see [Managing storage capacity](managing-storage-configuration.md#managing-storage-capacity).

## To increase storage capacity for a file system (console)
<a name="increase-storage-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Navigate to **File systems** and choose the Windows file system that you want to increase storage capacity for.

1. For **Actions**, choose **Update storage**. Or, in the **Summary** panel, choose **Update** next to the file system's **Storage capacity**. 

   The **Update storage capacity** window appears.

1. For **Input type**, choose **Percentage** to enter the new storage capacity as a percentage change from the current value, or choose **Absolute** to enter the new value in GiB.

1. Enter the **Desired storage capacity**.
**Note**  
The desired capacity value must be at least 10 percent larger than the current value, up to the maximum value of 65,536 GiB.

1. Choose **Update** to initiate the storage capacity update.

1. You can monitor the update progress on the **File systems** detail page, in the **Updates** tab.

## To increase storage capacity for a file system (CLI)
<a name="increase-storage-console"></a>

To increase the storage capacity for an FSx for Windows File Server file system, use the AWS CLI command [update-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-file-system.html). Set the following parameters:
+ `--file-system-id` to the ID of the file system you are updating.
+ `--storage-capacity` to a value that is at least 10 percent greater than the current value.

You can monitor the progress of the update by using the AWS CLI command [describe-file-systems](https://docs.aws.amazon.com/cli/latest/reference/fsx/describe-file-systems.html). Look for the `administrative-actions` in the output. 

For more information, see [AdministrativeAction](https://docs.aws.amazon.com/fsx/latest/APIReference/API_AdministrativeAction.html).