# Restoring a backup to a new volume

The following procedures describe how to restore an FSx for ONTAP backup to a new volume using the AWS Management Console and AWS CLI.
When restoring a volume to a second-generation file system,
you can [monitor](monitor-backup-restore.md "monitor-backup-restore.md") the progress using the AWS Management Console, AWS CLI, and API.

###### To restore a volume backup to a new volume (Console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the navigation pane, choose **Backups**, and
   then choose the FSx for ONTAP volume backup that you want to restore.
3. In the upper right **Actions** menu, choose **Restore backup**.
   The **Create volume from backup page appears.**
4. Choose the FSx for ONTAP **File system** and **Storage virtual machine**
   that you want to restore the backup to from the dropdown menus.
5. In the upper right **Actions** menu, choose **Restore backup**.
   The **Create volume from backup page appears.**
6. Choose the FSx for ONTAP **File system** and **Storage virtual machine**
   that you want to restore the backup to from the dropdown menus.
7. Under **Volume details**, there are several selections.
   First, enter the **Volume name**. You can use up to 203 alphanumeric or underscore (\_)
   characters.
8. For **Volume size**, enter any whole number in
   the range of 20–314572800 to specify the size in mebibytes
   (MiB).
9. For **Volume type**, choose **Read-Write (RW)**
   to create a volume that is readable and writable
   or **Data Protection (DP)** to create a volume that
   is read-only and can be used as the destination of a NetApp SnapMirror
   or SnapVault relationship. For more information,
   see [Volume types](managing-volumes.md#volume-types "managing-volumes.md#volume-types").
10. For **Junction path**, enter a location within
    the file system to mount the volume. The name must have a leading
    forward slash, for example `/vol3`.
11. For **Storage efficiency**, choose
    **Enabled** to enable the ONTAP
    storage-efficiency features (deduplication, compression, and
    compaction). For more information, see
    [Storage efficiency](managing-storage-capacity.md#storage-efficiency "managing-storage-capacity.md#storage-efficiency").
12. For **Volume security style**, choose either **Unix (Linux)**,
    **NTFS**, or **Mixed**. A volume's security style determines
    whether preference is given to NTFS or UNIX ACLs for multi-protocol access. The MIXED mode is
    not required for multi-protocol access and is only recommended for advanced users.
13. For **Snapshot policy**, choose a snapshot policy for the volume.
    For more information about snapshot policies, see [Snapshot policies](snapshots-ontap.md#snapshot-policies "snapshots-ontap.md#snapshot-policies").

If you choose **Custom policy**, you must specify the policy's name in the
**custom-policy** field. The custom policy must already exist on the SVM or in the file system. You can create
a custom snapshot policy with the ONTAP CLI or REST API. For more information, see
[Create a Snapshot Policy](https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html "https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html")
in the NetApp ONTAP Product Documentation. 14. For **Tiering policy cooling period**, valid values are 2-183 days. A volume's tiering policy cooling period
defines the number of days before data that has not been accessed is marked cold and moved to capacity pool storage.
This setting only affects the `Auto` and `Snapshot-only` policies. 15. In the **Advanced** section, for **SnapLock Configuration**, you can
leave the default **Disabled** setting or choose **Enabled** to configure a
SnapLock volume. For more information about configuring a
SnapLock Compliance volume or a SnapLock Enterprise volume, see [Understanding SnapLock Compliance](snaplock-compliance.md "snaplock-compliance.md")
and [Understanding SnapLock Enterprise](snaplock-enterprise.md "snaplock-enterprise.md"). For more information about SnapLock, see
[Protecting your data with SnapLock](snaplock.md "snaplock.md"). 16. Choose **Confirm** to create the volume. 17. If you are restoring the backup to a second-generation file system, you can monitor the backup restore progress on the
**Updates** tab on the **Volume** page. For more information, see
[Monitoring progress when restoring a backup](monitor-backup-restore.md "monitor-backup-restore.md").

###### To restore a backup to a new volume (CLI)

Use the [create-volume-from-backup](../../../cli/latest/reference/fsx/create-volume-from-backup.md "../../../cli/latest/reference/fsx/create-volume-from-backup.md") CLI command, or the equivalent
[CreateVolumeFromBackup](../APIReference/API_CreateVolumeFromBackup.md "../APIReference/API_CreateVolumeFromBackup.md") API command to restore a volume backup to a new volume.

- ```
  `$` `aws fsx create-volume-from-backup --backup-id `backup-08e6fc1133fff3532` \
   --name demo --ontap-configuration JunctionPath=/demo,SizeInMegabytes=100000,\
   StorageVirtualMachineId=svm-0f04a9c7c27e1908b,TieringPolicy={Name=ALL}`
  ```

```

The system response for a successful restore request to restore a backup to a second-generation file system looks as follows.
 The response includes the `"AdministrativeActions"` object which provides status and progress information about request..



```

`{ 
 "Volume": { 
 "CreationTime": 1692721488.428, 
 "FileSystemId": "fs-07ab735385276ed60", 
 "Lifecycle": "CREATING", 
 "Name": "demo", 
 "OntapConfiguration": { 
 "FlexCacheEndpointType": "NONE", 
 "JunctionPath": "/demo", 
 "SizeInMegabytes": 100000, 
 "StorageEfficiencyEnabled": true,
 "StorageVirtualMachineId": "svm-0f04a9c7c27e1908b", 
 "StorageVirtualMachineRoot": false, 
 "TieringPolicy": { 
 "Name": "ALL" 
 }, 
 "OntapVolumeType": "DP", 
 "SnapshotPolicy": "default", 
 "CopyTagsToBackups": false, 
 }, 
 "ResourceARN": "arn:aws:fsx:us-east-1:752825163408:volume/fs-07ab735385276ed60/fsvol-0b6ec764c9c5f654a", 
 "VolumeId": "fsvol-0b6ec764c9c5f654a", 
 "VolumeType": "ONTAP", 
 ---> "AdministrativeActions": [
 { 
 "AdministrativeActionType": "DOWNLOAD_DATA_FROM_BACKUP", 
 "RequestTime": 1685729972.069, 
 "Status": "PENDING" 
 } 
 ] <----
 } 
 }`

```

The system response for a successful request to restore a backup to a first-generation file system looks as follows.



```

`{ 
 "Volume": { 
 "CreationTime": 1692721488.428, 
 "FileSystemId": "fs-07ab735385276ed60", 
 "Lifecycle": "CREATING", 
 "Name": "demo", 
 "OntapConfiguration": { 
 "FlexCacheEndpointType": "NONE", 
 "JunctionPath": "/demo", 
 "SizeInMegabytes": 100000, 
 "StorageEfficiencyEnabled": true,
 "StorageVirtualMachineId": "svm-0f04a9c7c27e1908b", 
 "StorageVirtualMachineRoot": false, 
 "TieringPolicy": { 
 "Name": "ALL" 
 }, 
 "OntapVolumeType": "DP", 
 "SnapshotPolicy": "default", 
 "CopyTagsToBackups": false, 
 }, 
 "ResourceARN": "arn:aws:fsx:us-east-1:752825163408:volume/fs-07ab735385276ed60/fsvol-0b6ec764c9c5f654a", 
 "VolumeId": "fsvol-0b6ec764c9c5f654a", 
 "VolumeType": "ONTAP",
 } 
 }`

```

When restoring a volume to a second-generation file system,
 you can [monitor the progress](monitor-backup-restore.md "monitor-backup-restore.md") using the AWS Management Console, AWS CLI, and API.
```
