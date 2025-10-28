# Disabling automatic snapshots

Automatic snapshots are enabled by the default snapshot policy for volumes in your
FSx for ONTAP file system. If you don't need snapshots of your data (for example, if you're using
test data), you can disable snapshots by setting the volume's
[snapshot policy](snapshots-ontap.md#snapshot-policies "snapshots-ontap.md#snapshot-policies") to `none` using the AWS Management Console, AWS CLI
and API, and the ONTAP CLI, as described in the following procedures.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems** and choose the ONTAP
   file system that you want to update a volume for.
3. Choose the **Volumes** tab.
4. Choose the volume that you want to update.
5. For **Actions**, choose **Update
   volume**.

The **Update volume** dialog box displays with
the volume's current settings. 6. For **Snapshot policy**, choose **None**. 7. Choose **Update** to update the volume.

- Use the
  [update-volume](../../../cli/latest/reference/fsx/update-volume.md "../../../cli/latest/reference/fsx/update-volume.md") AWS CLI command (or the equivalent [UpdateVolume](../APIReference/API_UpdateVolume.md "../APIReference/API_UpdateVolume.md") API command), to set the `SnapshotPolicy` to `none`,
  as shown in the following example.

```
`aws fsx update-volume \
 --volume-id fsvol-1234567890abcdefa \
 --name new_vol \
 --ontap-configuration CopyTagsToBackups=true,JunctionPath=/new_vol, \
 SizeInMegabytes=2048,SnapshotPolicy=none, \
 StorageEfficiencyEnabled=true, \
 TieringPolicy=all`
```

Set the volume's snapshot policy to use the `none` default policy to turn off automatic
snapshots.

1. Use the
   [`volume snapshot policy show`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-policy-show.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-policy-show.html") ONTAP CLI command to show the `none` policy.

```
`::>` `snapshot policy show -policy none`

`Vserver: FsxIdabcdef01234567892
 Number of Is
Policy Name Schedules Enabled Comment
------------------------ --------- ------- ----------------------------------
none 0 false Policy for no automatic snapshots.
 Schedule Count Prefix SnapMirror Label
 ---------------------- ----- ---------------------- -------------------
 - - - -`
```

2.  Use the
    [`volume modify`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-modify.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-modify.html")
    ONTAP ClI command to set the volume's snapshot policy to `none` to disable automatic snapshots.
    Replace the following placeholder values with your data:

        * ``svm_name`` — use your SVM's name.
        * ``vol_name`` — use your volume's name.

    When prompted to continue, enter `y`.

```
`::>` `volume modify -vserver `svm_name` -volume `vol_name` -snapshot-policy none`

`Warning: You are changing the Snapshot policy on volume "`vol_name`" to "none". Snapshot copies on this volume
 that do not match any of the prefixes of the new Snapshot policy will not be deleted. However, when
 the new Snapshot policy takes effect, depending on the new retention count, any existing Snapshot copies
 that continue to use the same prefixes might be deleted. See the 'volume modify' man page for more information.
Do you want to continue? {y|n}: y
Volume modify successful on volume `vol_name` of Vserver `svm_name`.`
```
