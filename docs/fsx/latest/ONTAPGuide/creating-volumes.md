# Creating volumes

You can create an FSx for ONTAP FlexVol or FlexGroup volume using the Amazon FSx console, the AWS CLI, and the
Amazon FSx API, in addition to the NetApp ONTAP command line interface (CLI) and REST
API.

###### Note

The volume's security style is automatically set to the root volume's security style.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose
   **Volumes**.
3. Choose **Create volume**.
4. For **File system type**, choose **Amazon FSx for NetApp ONTAP**.
5. In the **File system details** section, provide the following information:
   - For **File system**, choose the file system to create the volume on.
   - For **Storage virtual machine**, choose the storage virtual machine (SVM)
     to create the volume on.

6. In the **Volume style** section, choose **FlexVol**.
7. In the **Volume details** section, provide the following information:
   - In the **Volume name** field, provide a name for
     the volume. You can use up to 203 alphanumeric or underscore (\_)
     characters.
   - For **Volume size**, enter any whole
     number in the range of 20–314572800 to specify the size
     in mebibytes (MiB).
   - For **Volume type**, choose **Read-Write (RW)**
     to create a volume that is readable and writable
     or **Data Protection (DP)** to create a volume that
     is read-only and can be used as the destination of a NetApp SnapMirror
     or SnapVault relationship. For more information,
     see [Volume types](managing-volumes.md#volume-types "managing-volumes.md#volume-types").
   - For **Junction path**, enter a location within
     the file system to mount the volume. The name must have a leading
     forward slash, for example `/vol3`.
   - For **Storage efficiency**, choose
     **Enabled** to enable the ONTAP
     storage-efficiency features (deduplication, compression, and
     compaction) on this volume. For more information,
     see [Storage efficiency](managing-storage-capacity.md#storage-efficiency "managing-storage-capacity.md#storage-efficiency").
   - For **Volume security style**, choose
     between **Unix (Linux)** and
     **NTFS** for the volume. For more
     information, see [Volume security style](managing-volumes.md#volume-security-style "managing-volumes.md#volume-security-style").
   - For **Snapshot policy**, choose a snapshot policy for the volume.
     For more information about snapshot policies, see [Snapshot policies](snapshots-ontap.md#snapshot-policies "snapshots-ontap.md#snapshot-policies").

   If you choose **Custom policy**, you must specify the policy's name in the
   **custom-policy** field. The custom policy must already exist on the SVM or in the file system. You can create
   a custom snapshot policy with the ONTAP CLI or REST API. For more information, see
   [Create a Snapshot Policy](https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html "https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html")
   in the NetApp ONTAP Product Documentation.

8. In the **Storage tiering** section, provide the following information:
   - For **Capacity pool tiering policy**,
     choose the storage pool tiering policy for the volume, which can be
     **Auto** (the default), **Snapshot Only**, **All**, or
     **None**. For more information, see
     [Volume tiering policies](volume-storage-capacity.md#data-tiering-policy "volume-storage-capacity.md#data-tiering-policy").
   - If you choose either **Auto** or **Snapshot Only**, you can
     set the **Tiering policy cooling period** to define the number of days before data that has not been accessed
     is marked cold and moved to capacity pool storage. You can provide a value between 2 and 183 days. The default setting is 31 days.

9. In the **Advanced** section, for **SnapLock Configuration**,
   choose between **Enabled** and **Disabled**. For more information about configuring a
   SnapLock Compliance volume or a SnapLock Enterprise volume, see [Understanding SnapLock Compliance](snaplock-compliance.md "snaplock-compliance.md")
   and [Understanding SnapLock Enterprise](snaplock-enterprise.md "snaplock-enterprise.md"). For more information about SnapLock, see
   [Protecting your data with SnapLock](snaplock.md "snaplock.md").
10. Choose **Confirm** to create the volume.
    You can monitor the update progress on the **File
    systems** detail page, in the **Status**
    column of the **Volumes** pane. The volume is ready for use
    when its status is **Created**.

###### Note

You can only create FlexGroup volumes for file systems with multiple HA pairs using the Amazon FSx console.
To create FlexVol volumes for file systems with multiple HA pairs, use the AWS CLI, Amazon FSx API, or NetApp management tools.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose
   **Volumes**.
3. Choose **Create volume**.
4. For **File system type**, choose **Amazon FSx for NetApp ONTAP**.
5. In the **File system details** section, provide the following information:
   - For **File system**, choose the file system to create the volume on.
   - For **Storage virtual machine**, choose the storage virtual machine (SVM)
     to create the volume on.

6. In the **Volume style** section, choose **FlexGroup**.
7. In the **Volume details** section, provide the following information:
   - In the **Volume name** field, provide a name for
     the volume. You can use up to 203 alphanumeric or underscore (\_)
     characters.
   - For **Volume size**, enter any whole number in
     the range of 800 gibibytes (GiB)–2,400 tebibytes (TiB) per HA pair. For example, a file system with 12
     high-availability (HA) pairs
     would have a minimum volume size of 9,600 GiB
     and a maximum size of 20,480 TiB.
   - For **Volume type**, choose **Read-Write (RW)**
     to create a volume that is readable and writable
     or **Data Protection (DP)** to create a volume that
     is read-only and can be used as the destination of a NetApp SnapMirror
     or SnapVault relationship. For more information,
     see [Volume types](managing-volumes.md#volume-types "managing-volumes.md#volume-types").
   - For **Junction path**, enter a location within
     the file system to mount the volume. The name must have a leading
     forward slash, for example `/vol3`.
   - For **Storage efficiency**, choose
     **Enabled** to enable the ONTAP
     storage-efficiency features (deduplication, compression, and
     compaction). For more information,
     see [Storage efficiency](managing-storage-capacity.md#storage-efficiency "managing-storage-capacity.md#storage-efficiency").
   - For **Volume security style**, choose
     between **Unix (Linux)** and
     **NTFS** for the volume. For more
     information, see [Volume security style](managing-volumes.md#volume-security-style "managing-volumes.md#volume-security-style").

   ###### Note

   The volume's security style is automatically set to the root volume's security style.
   - For **Snapshot policy**, choose a snapshot policy for the volume.
     For more information about snapshot policies, see [Snapshot policies](snapshots-ontap.md#snapshot-policies "snapshots-ontap.md#snapshot-policies").

   If you choose **Custom policy**, you must specify the policy's name in the
   **custom-policy** field. The custom policy must already exist on the SVM or in the file system. You can create
   a custom snapshot policy with the ONTAP CLI or REST API. For more information, see
   [Create a Snapshot Policy](https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html "https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html")
   in the NetApp ONTAP Product Documentation.

8. In the **Storage tiering** section, provide the following information:
   - For **Capacity pool tiering policy**,
     choose the storage pool tiering policy for the volume, which can be
     **Auto** (the default), **Snapshot Only**, **All**, or
     **None**. For more information, see
     [Volume tiering policies](volume-storage-capacity.md#data-tiering-policy "volume-storage-capacity.md#data-tiering-policy").
   - If you choose either **Auto** or **Snapshot Only**, you can
     set the **Tiering policy cooling period** to define the number of days before data that has not been accessed
     is marked cold and moved to capacity pool storage. You can provide a value between 2–183 days. The default setting is 31 days.

9. In the **Advanced** section, for **SnapLock Configuration**,
   choose between **Enabled** and **Disabled**. For more information about configuring a
   SnapLock Compliance volume or a SnapLock Enterprise volume, see [Understanding SnapLock Compliance](snaplock-compliance.md "snaplock-compliance.md")
   and [Understanding SnapLock Enterprise](snaplock-enterprise.md "snaplock-enterprise.md"). For more information about SnapLock, see
   [Protecting your data with SnapLock](snaplock.md "snaplock.md").
10. Choose **Confirm** to create the volume.
    You can monitor the update progress on the **File
    systems** detail page, in the **Status**
    column of the **Volumes** pane. The volume is ready for use
    when its status is **Created**.

- To create an FSx for ONTAP volume, use the [create-volume](../../../cli/latest/reference/fsx/create-volume.md "../../../cli/latest/reference/fsx/create-volume.md") CLI command (or the equivalent [CreateVolume](../APIReference/API_CreateVolume.md "../APIReference/API_CreateVolume.md") API operation), as shown in the following
  example.

```
`aws fsx create-volume \
 --volume-type ONTAP \
 --name vol1 \
 --ontap-configuration CopyTagsToBackups=true,JunctionPath=/vol1,SecurityStyle=NTFS, \
 SizeInMegabytes=1024,SnapshotPolicy=default, \
 StorageVirtualMachineId=svm-abcdef0123456789a,OntapVolumeType=RW, \
 StorageEfficiencyEnabled=true`
```

After successfully creating the volume, Amazon FSx returns its description in
JSON format, as shown in the following
example.

```
{
    "Volume": {
        "CreationTime": "2022-08-12T13:03:37.625000-04:00",
        "FileSystemId": "fs-abcdef0123456789c",
        "Lifecycle": "CREATING",
        "Name": "vol1",
        "OntapConfiguration": {
            "CopyTagsToBackups": true,
            "FlexCacheEndpointType": "NONE",
            "JunctionPath": "/vol1",
            "SecurityStyle": "NTFS",
            "SizeInMegabytes": 1024,
            "SnapshotPolicy": "default",
            "StorageEfficiencyEnabled": true,
            "StorageVirtualMachineId": "svm-abcdef0123456789a",
            "StorageVirtualMachineRoot": false,
            "TieringPolicy": {
                "Name": "NONE"
            },
            "OntapVolumeType": "RW"
        },
        "ResourceARN": "arn:aws:fsx:us-east-2:111122223333:volume/fs-abcdef0123456789c/fsvol-abcdef0123456789b",
        "VolumeId": "fsvol-abcdef0123456789b",
        "VolumeType": "ONTAP"


    }
}
```

You can also create a new volume by restoring a backup of a volume to a new volume. For more information, see
[Restoring backups to a new volume](using-backups.md#restoring-backups "using-backups.md#restoring-backups").
