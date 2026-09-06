

# Modifying file system maintenance windows
<a name="maintenance-windows"></a>

Amazon FSx for OpenZFS performs routine software patching for the OpenZFS software it manages. The maintenance window is your opportunity to control what day and time of the week this software patching occurs. You can choose the maintenance window during file system creation, or at a later time. If you have no time preference, a 30-minute default window is assigned.

FSx for OpenZFS allows you to adjust your maintenance window as needed to accommodate your workload and operational requirements. You can move your maintenance window as frequently as required, provided that a maintenance window is scheduled at least once every 14 days. If a patch is released and you haven’t scheduled a maintenance window within 14 days, FSx for OpenZFS will proceed with maintenance on the file system to ensure its security and reliability.

 Patching occurs infrequently, typically once every month during the maintenance window that you specify. Patching should require only a portion of your 30-minute maintenance window. We recommend scheduling your maintenance window during idle periods when there is minimal load on your file system. While patching is in progress, you should expect that your Single-AZ (non-HA) file systems will be unavailable, typically for less than 15 minutes. Your Single-AZ (HA) and Multi-AZ (HA) file systems will remain available and automatically fail over and fail back between the preferred file server and the standby file server. For more information, see [Failover process for FSx for OpenZFS](availability-durability.md#multi-az-failover). 

For file systems that use the Intelligent-Tiering storage class, the in-memory cache will be erased during maintenance, leading to higher latencies, particularly on metadata, until after maintenance has been completed.

**Note**  
To ensure data integrity during maintenance activity, FSx for OpenZFS completes pending write operations to the underlying storage volumes that host your file system before maintenance begins.

 You can use the Amazon FSx Management Console, AWS CLI, AWS API, or one of the AWS SDKs to change the maintenance window for your file systems. 

## Changing the weekly maintenance window
<a name="change-maintenance-window"></a>

**To change the weekly maintenance window (console)**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Choose **File systems** in the left hand navigation column.

1. Choose the file system that you want to change the weekly maintenance window for. The file system details page displays.

1. Choose **Administration** to display the file system administration **Settings** panel.

1. Choose **Update** to display the **Change maintenance window** window.

1.  Enter the new day and time that you want the weekly maintenance window to start.

1. Choose **Save** to save your changes. The new maintenance start time is displayed in the file system administration **Settings** panel.

To change the weekly maintenance window using the [update-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-file-system.html) CLI command, see [Updating a file system (Amazon FSx console, AWS CLI, and Amazon FSx API)](updating-file-system.md#update-file-system-console-cli-api).