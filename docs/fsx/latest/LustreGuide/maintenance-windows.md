# Amazon FSx for Lustre maintenance windows

Amazon FSx for Lustre performs routine software patching for the Lustre software it manages.
Patching occurs infrequently, typically once every several weeks. The maintenance window
is your opportunity to control what day and time of the week this software patching occurs.
You choose the maintenance window during file system creation. If you have no time preference,
then a 30-minute default window is assigned.

Patching should require only a fraction of your 30-minute maintenance window. During these
few minutes of time, your file system will be temporarily unavailable. File operations issued by
clients while the file system is unavailable will transparently retry and eventually succeed after
maintenance is complete. Note that the in-memory cache will be erased during maintenance, leading
to higher latencies until after maintenance has been completed.

FSx for Lustre allows you to adjust your maintenance window as needed to accommodate your
workload and operational requirements. You can move your maintenance window as frequently
as required, provided that a maintenance window is scheduled at least once every 14 days.
If a patch is released and you haven’t scheduled a maintenance window within 14 days,
FSx for Lustre will proceed with maintenance on the file system to ensure its security and
reliability.

You can use the Amazon FSx Management Console, AWS CLI, AWS API, or one of the AWS SDKs
to change the maintenance window for your file systems.

###### To change the maintenance window using the console

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Choose **File systems** in the navigation pane.
3. Choose the file system that you want to change the maintenance window for. The file
   system details page appears.
4. Choose the **Maintenance** tab. The maintenance window
   **Settings** panel appears.
5. Choose **Edit** and enter the new day and time that you want the maintenance window to start.
6. Choose **Save** to save your changes. The new maintenance start time is displayed in the **Settings** panel.
   You can change the maintenance window for your file system using the [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md") CLI command.
   Run the following command, replacing the file system ID with the ID for your file system, and the
   date and time with when you want to begin the window.

```
aws fsx update-file-system --file-system-id fs-`01234567890123456` --lustre-configuration WeeklyMaintenanceStartTime=`1:01:30`
```
