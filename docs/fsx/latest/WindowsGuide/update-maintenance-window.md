

# Changing the weekly maintenance window
<a name="update-maintenance-window"></a>

FSx for Windows File Server lets you adjust when your file system's maintenance window starts to accommodate your workload and operational requirements. You can use the AWS Management Console, AWS CLI, and Amazon FSx API to change when the weekly maintenance window starts, described in the following procedure.

**To change the start time of the weekly maintenance window (console)**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Choose **File systems** in the left hand navigation column.

1. Choose the file system that you want to change the weekly maintenance window for. The file system details page displays.

1. Choose **Administration** to display the file system administration **Settings** panel.

1. Choose **Update** to display the **Change maintenance window** window.

1.  Enter the new day and time that you want the weekly maintenance window to start.

1. Choose **Save** to save your changes. The new maintenance start time is displayed in the **Administration Settings** panel.

To change the start time of the weekly maintenance window using the [update-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-file-system.html) CLI command, see [Update a file system using the AWS CLI](walkthrough03-update-file-system.md).