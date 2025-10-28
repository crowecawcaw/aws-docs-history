# Updating an Amazon FSx for OpenZFS file system

This section provides information on how to update modifyable properties, including storage capacity, throughput capacity, and maintenance windows, on your file system using the Amazon FSx console,
the AWS CLI, and the Amazon FSx API.

###### Topics

- [Updating a file system (Amazon FSx
  console, AWS CLI, and Amazon FSx API)](#update-file-system-console-cli-api "#update-file-system-console-cli-api")
- [Modifiable file system properties](#updatable-properties "#updatable-properties")
- [Modifying provisioned SSD storage capacity
  and IOPS](managing-storage-capacity.md "managing-storage-capacity.md")
- [Modifying provisioned SSD read cache](managing-ssd-read-cache.md "managing-ssd-read-cache.md")
- [Modifying throughput capacity](managing-throughput-capacity.md "managing-throughput-capacity.md")
- [Modifying network type](manage-network-type.md "manage-network-type.md")
- [Modifying file system maintenance windows](maintenance-windows.md "maintenance-windows.md")

## Updating a file system (Amazon FSx

console, AWS CLI, and Amazon FSx API)

Amazon FSx Console

###### To update how file system tags are copied

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose **File
   systems**, and then choose the FSx for OpenZFS file system
   that you want to update.
3. For **Actions**, choose **Update file
   system**. The **Update file system**
   dialog box displays.
   - For **Copy tags to backups**, choose
     whether to copy tags from the file system to any backup
     that's taken.
   - For **Copy tags to volumes**, choose
     whether to copy tags from the file system to any volume that
     you create.

4. Choose **Update** to update the file system with
   your changes.

###### To update automatic daily backups

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. To display the file system details page, in the left navigation
   pane, choose **File systems**, and then choose the
   FSx for OpenZFS file system that you want to update.
3. Choose the **Backups** tab, and then choose Update.
4. Modify the automatic daily backup settings for this file system,
   and then choose **Save**.

###### To update the file system's VPC route tables

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. To display the file system details page, in the left navigation pane,
   choose **File systems**, and then choose the
   FSx for OpenZFS file system that you want to update.
3. For **Actions**, choose **Update route
   tables**. This option is only available for Multi-AZ file systems.
4. In the **Manage route tables** dialog box. do
   one of the following:
   - To associate a new VPC route table, select a route table
     from the **Associate new route tables** dropdown
     list, and then choose **Associate**.
   - To disassociate an existing VPC route table, select a route table
     from the **Current route tables** pane, and then
     choose **Disassociate**.

5. Choose **Close**.

AWS CLI and Amazon FSx API

###### To update a file system (CLI and Amazon FSx API)

- To update the configuration of an FSx for OpenZFS file system, use the [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md") CLI command (or the equivalent [UpdateFileSystem](../APIReference/API_UpdateFileSystem.md "../APIReference/API_UpdateFileSystem.md") API operation), as shown in the following
  example.

```
`aws fsx update-file-system \
 --file-system-id fs-0123456789abcdef0 \
 --open-zfs-configuration AutomaticBackupRetentionDays=30,DailyAutomaticBackupStartTime=01:00, \
 WeeklyMaintenanceStartTime=1:01:30,AddRouteTableIds=rtb-0123abcd`
```

## Modifiable file system properties

This section provides information on how to update the following FSx for OpenZFS file system properites. You can update an FSx for OpenZFS file system's configuration using the Amazon FSx
console, the AWS CLI, and the Amazon FSx API.

- **Automatic daily backups** – Back up
  your file system automatically on a daily basis. Modify the backup window
  and the backup retention period. For more information about backups, see
  [Working with automatic daily backups](using-backups.md#automatic-backups "using-backups.md#automatic-backups").
- **Copy tags to backups** – Copy file
  system tags to file system backups.
- **Copy tags to volumes** – Copy file
  system tags to the volumes that are attached to the file system.
- **Provisioned SSD IOPS** – Set a fixed
  number of IOPS or have Amazon FSx automatically maintain 3 SSD IOPS per GiB of
  storage capacity. For information on how to increase SSD IOPS, see [Updating SSD storage capacity and provisioned IOPS](managing-storage-capacity.md#increase-storage-capacity "managing-storage-capacity.md#increase-storage-capacity").
- **Storage capacity** – For file systems with SSD (provisioned) storage, storage capacity cannot be decreased after creation, only increased.
  For information on how to increase SSD (provisioned) storage capacity, see [Updating SSD storage capacity and provisioned IOPS](managing-storage-capacity.md#increase-storage-capacity "managing-storage-capacity.md#increase-storage-capacity").
  For file systems using the Intelligent-Tiering storage class, storage capacity will automatically grow and strink to fit your data needs as they change.
- **SSD read cache** – For file systems using the Intelligent-Tiering storage class, you can modify the sizing mode of the optional provisioned SSD read cache at any time.
  For information on how to modify your SSD read cache, see [Modifying provisioned SSD read cache](managing-ssd-read-cache.md "managing-ssd-read-cache.md").
- **Throughput capacity** – You can increase or decrease your file system's
  throughput capacity at any point. For information on how to update throughput capacity, see [Modifying throughput capacity](managing-throughput-capacity.md#increase-throughput-capacity "managing-throughput-capacity.md#increase-throughput-capacity").
- **Network type** – You can change your
  file system's network type at any time. For information on how to change network type,
  see [Modifying network type](manage-network-type.md "manage-network-type.md").
- **Weekly maintenance window** – Set the day of the week and time that Amazon FSx
  performs file system maintenance and updates. For information on how to change the weekly maintenance window, see [Changing the weekly maintenance window](maintenance-windows.md#change-maintenance-window "maintenance-windows.md#change-maintenance-window").
- **Amazon VPC route tables** – For Multi-AZ file systems, FSx for OpenZFS creates an endpoint for accessing your file system in a VPC route table.
  You can associate new route tables that you create with your existing Multi-AZ file systems—allowing
  you to configure which clients can access your data even as your network evolves. You can
  also disassociate (remove) existing route tables from your file system.
