# Updating volumes

You can update the configuration of an FSx for ONTAP volume using the Amazon FSx console,
the AWS CLI, and the Amazon FSx API, in addition to the NetApp ONTAP command line interface
(CLI) and REST API. You can modify the following properties of an existing FSx for ONTAP volume:

- Volume name
- Junction path
- Volume size
- Storage efficiency
- Capacity pool tiering policy
- Volume security style
- Snapshot policy
- Tiering policy cooling period
- Copy tags to backups (using the AWS CLI and Amazon FSx API)
  For more information, see [Managing FSx for ONTAP volumes](managing-volumes.md "managing-volumes.md").

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems** and choose the ONTAP
   file system that you want to update a volume for.
3. Choose the **Volumes** tab.
4. Choose the volume that you want to update.
5. For **Actions**, choose **Update
   volume**.

The **Update volume** dialog box displays with
the volume's current settings. 6. For **Junction path**, enter an existing location
within the file system to mount the volume. The name must have a
leading forward slash, such as `/vol5`. 7. For **Volume size**, you can increase or decrease
the size of the volume within the range specified in the Amazon FSx console. For FlexVol volumes,
the maximum size is 300 TiB. For FlexGroup volumes, the maximum size is 300 TiB
multiplied by the total number of constituent volumes that your FlexGroup has, up to a maximum of
20 PiB. 8. For **[Storage efficiency](managing-storage-capacity.md#storage-efficiency "managing-storage-capacity.md#storage-efficiency")**, choose
**Enabled** to enable the ONTAP storage
efficiency features (deduplication, compression, and compaction) on the volume, or
choose **Disabled** to disable
them. 9. For **Capacity pool tiering policy**, choose a
new storage pool tiering policy for the volume, which can be
**Auto** (the default),
**Snapshot-only**, **All**, or
**None**. For more information about capacity
pool tiering policies, see [Volume tiering policies](volume-storage-capacity.md#data-tiering-policy "volume-storage-capacity.md#data-tiering-policy"). 10. For **[Volume security style](managing-volumes.md#volume-security-style "managing-volumes.md#volume-security-style")**, choose either **Unix (Linux)**,
**NTFS**, or **Mixed**. A volume's security style determines
whether preference is given to NTFS or UNIX ACLs for multi-protocol access. The MIXED mode is
not required for multi-protocol access and is only recommended for advanced users. 11. For **Snapshot policy**, choose a snapshot policy for the volume.
For more information about snapshot policies, see [Snapshot policies](snapshots-ontap.md#snapshot-policies "snapshots-ontap.md#snapshot-policies").

If you choose **Custom policy**, you must specify the policy's name in the
**custom-policy** field. The custom policy must already exist on the SVM or in the file system. You can create
a custom snapshot policy with the ONTAP CLI or REST API. For more information, see
[Create a Snapshot Policy](https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html "https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html")
in the NetApp ONTAP Product Documentation. 12. For **Tiering policy cooling period**, valid values are 2-183 days. A volume's tiering policy cooling period
defines the number of days before data that has not been accessed is marked cold and moved to capacity pool storage.
This setting only affects the `Auto` and `Snapshot-only` policies. 13. Choose **Update** to update the volume.

- To update the configuration of an FSx for ONTAP volume, use the
  [update-volume](../../../cli/latest/reference/fsx/update-volume.md "../../../cli/latest/reference/fsx/update-volume.md") CLI command (or the equivalent [UpdateVolume](../APIReference/API_UpdateVolume.md "../APIReference/API_UpdateVolume.md") API operation), as shown in the following
  example.

```
`aws fsx update-volume \
 --volume-id fsvol-1234567890abcdefa \
 --name new_vol \
 --ontap-configuration CopyTagsToBackups=true,JunctionPath=/new_vol, \
 SizeInMegabytes=2048,SnapshotPolicy=default-1weekly, \
 StorageEfficiencyEnabled=true, \
 TieringPolicy=all`
```
