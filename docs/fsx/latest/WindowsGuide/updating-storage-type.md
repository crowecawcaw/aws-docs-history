

# Updating the storage type of a FSx for Windows file system
<a name="updating-storage-type"></a>

You can change the storage type of a file system that uses HDD storage to use SSD storage. You can use the the Amazon FSx console, the AWS CLI, or the Amazon FSx API to change a file system's storage type, as shown in the following procedures. For more information, see [Managing your file system's storage type](managing-storage-configuration.md#managing-storage-type).

## To update a file system's storage type (console)
<a name="storage-type-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Navigate to **File systems** and choose the Windows file system that you want to update the storage type for.

1. Under **Actions**, choose **Update storage type**. Or, in the **Summary** panel, select the **Update** button next to **HDD**. The **Update storage type** window appears.

1. For **Desired storage type**, choose **SSD**. Choose **Update** to initiate the storage type update.

   You can [monitor the progress](monitoring-storage-type-updates.md) of the storage type update using the console and the CLI.

## To update a file system's storage type (CLI)
<a name="ssd-iops-cli"></a>

To update storage type for an FSx for Windows File Server file system, use the AWS CLI command [update-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-file-system.html). Set the following parameters:
+ `--file-system-id` to the ID of the file system that you want to update.
+ `--storage-type` to SSD. You can't switch from SSD storage type to HDD storage type.

You can monitor the progress of the update by using the AWS CLI command [describe-file-systems](https://docs.aws.amazon.com/cli/latest/reference/fsx/describe-file-systems.html). Look for the `administrative-actions` in the output. 

For more information, see [AdministrativeAction](https://docs.aws.amazon.com/fsx/latest/APIReference/API_AdministrativeAction.html).