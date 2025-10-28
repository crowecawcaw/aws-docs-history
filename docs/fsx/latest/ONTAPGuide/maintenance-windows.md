# Optimizing performance with Amazon FSx maintenance windows

As a fully-managed service, FSx for ONTAP regularly performs maintenance on and updates to
your file system. This maintenance has no impact for most workloads. For workloads that are
performance-sensitive, on rare occasions you may notice a brief (<60 seconds) impact on
performance when maintenance is occurring; Amazon FSx enables you to use the maintenance window
to control when any such potential maintenance activity occurs.

Patching occurs infrequently, typically once every several weeks. When patching occurs, each of your file system's file servers is patched one at a time, and each file server typically takes up to an hour to be patched.
Before any file server is patched within an HA pair, your file system automatically fails over to the file servers' HA partner, which may result in a brief (less than 60 seconds)
I/O pause for any I/O directed toward that HA pair. Your file system will then fail back, which may result in another brief (less than 60 seconds) I/O pause.
You choose the maintenance window start time during file system creation. If you don't choose a window, one is automatically assigned.

###### Important

To ensure that your file system can be patched successfully, FSx for ONTAP will bring online any offline volumes for the duration of the patching process.
Any volumes that Amazon FSx brings back online will not be accessible to clients.

FSx for ONTAP allows you to adjust your maintenance window as needed to accommodate your workload
and operational requirements. You can move your maintenance window as frequently as required, provided
that a maintenance window occurs at least once every 14 days. If a patch is released and a maintenance window
does not occur within 14 days, FSx for ONTAP will proceed with maintenance on
the file system to ensure its security and reliability.

###### Note

To ensure data integrity during maintenance activity, FSx for ONTAP closes all opportunistic
locks and completes any pending write operations to the underlying storage volumes that are
hosting your file system before maintenance begins.

You can use the Amazon FSx Management Console, AWS CLI, AWS API, or one of the AWS SDKs to change the
maintenance window for your file systems.

###### To change the weekly maintenance window (console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Choose **File systems** in the left hand navigation column.
3. Choose the file system that you want to change the weekly maintenance window for.
   The **Summary** file system details page appears.
4. Choose **Administration** to display the
   file system administration **Settings** panel.
5. Choose **Update** to display the **Change maintenance window** window.
6. Enter the new day and time that you want the weekly maintenance window to start.
7. Choose **Save** to save your changes. The new maintenance start time is displayed
   in the file system administration **Settings** panel.
   To change the weekly maintenance window using the [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md") CLI command,
   see [To update a file system
   (CLI)](updating-file-system.md#update-file-system-cli "updating-file-system.md#update-file-system-cli").
