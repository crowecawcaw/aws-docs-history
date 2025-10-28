# Updating storage capacity and provisioned IOPS

You can increase or decrease a file system's SSD-based storage and the amount of provisioned SSD IOPS by using the Amazon FSx console, the AWS CLI,
and the API.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose **File systems**. In the **File
   systems** list, select the FSx for ONTAP file system
   that you want to update SSD storage capacity and SSD IOPS
   for.
3. Choose **Actions** > **Update storage capacity**. Or, in the
   **Summary** section, choose
   **Update** next to the file system's
   **SSD storage capacity** value.
4. To increase SSD storage capacity, choose **Modify storage capacity**.
5. For **Input type**, choose one of the following:
   - To enter the new SSD storage capacity as a percentage change
     from the current value, choose
     **Percentage**.
   - To enter the new value in GiB, choose
     **Absolute**.

6. Depending on the input type, enter a value for **Desired % increase**.
   - For **Percentage**, enter the percentage increase value. This value must be
     at least 10 percent greater than the current value.
   - For **Absolute**, enter the new value in GiB, up to the maximum allowed value
     of 196,608 GiB.

7. For **Provisioned SSD IOPS**, you have two options to modify
   the number of provisioned SSD IOPS for your file system:
   - If you want Amazon FSx to automatically scale your SSD IOPS to maintain 3 provisioned SSD IOPS per
     GiB of SSD storage capacity (up to a maximum of 160,000), choose **Automatic**.
   - If you want to specify the number of SSD IOPS, choose **User-provisioned**.
     Enter an absolute number of IOPS that's at least three
     times the amount of GiB of your SSD storage tier, and
     less than or equal to 160,000.

###### Note

For more information about the maximum number of SSD IOPS that you can provision for your
FSx for ONTAP file system, see [Impact of throughput capacity on
performance](performance.md#impact-throughput-cap-performance "performance.md#impact-throughput-cap-performance"). 8. Choose **Update**.

###### Note

At the bottom of the prompt, a configuration preview is shown for your new SSD storage capacity and SSD IOPS. For second-generation file systems,
the per-HA-pair value is also shown.
To increase the SSD storage capacity and provisioned IOPS for an FSx for ONTAP file system,
use the AWS CLI command [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md") or the equivalent
[UpdateFileSystem](../APIReference/API_UpdateFileSystem.md "../APIReference/API_UpdateFileSystem.md") API action.
Set the following parameters with your values:

- Set `--file-system-id` to the ID of the file system that you are updating.
- To increase your SSD storage capacity, set `--storage-capacity` to the
  target storage capacity value, which must be at least 10 percent greater than the current value.
- To modify your provisioned SSD IOPS, use the `--ontap-configuration
DiskIopsConfiguration` property. This property has two
  parameters, `Iops` and `Mode`:
  - If you want to specify the number of provisioned IOPS, use
    `Iops=`number_of_IOPS``(up to a maximum of 160,000) and`Mode=USER_PROVISIONED`. The IOPS value
    must be greater than or equal to three times the
    requested SSD storage capacity. If you're not increasing
    the storage capacity, the IOPs value must be greater
    than or equal to three times the current SSD storage
    capacity.
  - If you want Amazon FSx to automatically increase your SSD IOPS, use `Mode=AUTOMATIC` and
    don't use the `Iops` parameter. Amazon FSx will
    automatically maintain 3 SSD IOPS per GiB of the provisioned SSD storage capacity (up to a maximum of 160,000).

###### Note

For more information about the maximum number of SSD IOPS that you can provision for your
FSx for ONTAP file system, see [Impact of throughput capacity on
performance](performance.md#impact-throughput-cap-performance "performance.md#impact-throughput-cap-performance").
The following example increases the file system’s SSD storage to 2000 GiB and sets amount of user provisioned SSD IOPS to 7000.

```
`aws fsx update-file-system \
--file-system-id `fs-0123456789abcdef0` \
--storage-capacity `2000` \
--ontap-configuration 'DiskIopsConfiguration={Iops=`7000`,Mode=`USER_PROVISIONED`}'`
```

To monitor the progress of the update, use the
[describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") AWS CLI command.
Look for the `AdministrativeActions` section in the output.

For more information, see
[AdministrativeAction](../APIReference/API_AdministrativeAction.md "../APIReference/API_AdministrativeAction.md")
in the _Amazon FSx for NetApp ONTAP API Reference_.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose **File systems**. In the **File
   systems** list, select the FSx for ONTAP file system
   that you want to update SSD storage capacity and SSD IOPS
   for.
3. Choose **Actions** > **Update file system** > **Update SSD storage capacity/IOPS**.
   Or, in the
   **Summary** section, choose
   **Update** next to the file system's
   **SSD storage capacity** value.
4. To decrease SSD storage capacity, for **Action type**, choose **Decrease**.
5. For **Input type**, choose one of the following:
   - To enter the new SSD storage capacity as a percentage change
     from the current value, choose
     **Percentage**.
   - To enter the new value in GiB, choose
     **Absolute**.

6. Depending on the input type, do one of the following.
   - For **Percentage**, enter the **Desired % decrease** value. This value must be
     at least 9 percent less than the current value.
   - For **Absolute**, enter the **Desired storage capacity** value in GiB.

7. Choose **Update**.

###### Note

At the bottom of the prompt, a configuration preview is shown for your new SSD storage capacity and SSD IOPS. For second-generation file systems,
the per-HA-pair value is also shown.
To decrease the SSD storage capacity and provisioned IOPS for an FSx for ONTAP file system,
use the AWS CLI command [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md") or the equivalent
[UpdateFileSystem](../APIReference/API_UpdateFileSystem.md "../APIReference/API_UpdateFileSystem.md") API action.
Set the following parameters with your values:

1. To decrease SSD capacity, use the following command:

```
`aws fsx update-file-system \
--file-system-id fs-0123456789abcdef0 \
--storage-capacity 4096`
```

If you're using the user-provisioned IOPS mode and want to retain your current IOPS level, include the `DiskIopsConfiguration` parameter:

```
`aws fsx update-file-system \
--file-system-id fs-0123456789abcdef0 \
--storage-capacity 4096 \
--ontap-configuration 'DiskIopsConfiguration={Iops=15000,Mode=USER_PROVISIONED}'`
```

2. To monitor the progress of the decrease operation, use the **describe-file-systems** command:

```
`aws fsx describe-file-systems --file-system-id fs-0123456789abcdef0`
```

The command returns information about the decrease operation in the `AdministrativeActions` section. For example:

```
{
    "FileSystem": {
        "StorageCapacity": 4096,
        "StorageType": "SSD",
        "AdministrativeActions": [
            {
                "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
                "Message": "Moving data for [vol1 vol2]. 2 volume(s) remaining. https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/troubleshooting.html",
                "ProgressPercent": 4,
                "RequestTime": 1748981251.591,
                "Status": "IN_PROGRESS",
                "TargetFileSystemValues": {
                    "StorageCapacity": 4096
                }
            }
        ]
    }
}
```

To monitor the progress of the update, use the
[`describe-file-systems`](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") AWS CLI command.
Look for the `AdministrativeActions` section in the output.

For more information, see
[`AdministrativeAction`](../APIReference/API_AdministrativeAction.md "../APIReference/API_AdministrativeAction.md")
in the Amazon FSx for NetApp ONTAP API Reference.
