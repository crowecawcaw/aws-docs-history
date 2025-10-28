# Monitoring progress when restoring a backup

You can monitor the progress when restoring a volume backup to second-generation file system in the AWS Management Console, AWS CLI, and API.
As with all Amazon FSx administrative actions, a backup restore status is available
in the console, CLI, and API for 30 days after the operation is completed.

###### To monitor progress when restoring a backup (console)

Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").

1. In the left navigation menu, choose **Volumes**.
2. Choose the volume that the backup is being restored to.
3. Choose the **Updates** tab.
4. The **Backup restore** **Update type** provides the following
   information:
   - **PENDING** indicates that the file metadata is being
     downloaded onto the volume. The volume's **Lifecycle state** is
     **CREATING**.
   - **IN_PROGRESS** indicates that the volume is available
     and clients can mount the volume with read-only access to data.
     The **Progress %** shows the percentage of data
     that has been downloaded to the volume.
   - **COMPLETED** indicates that all data has been downloaded to the volume,
     and the backup restore is complete. Clients now have read-write access.
     For `RW` volumes, the volume's type changes from `DP` to `RW` at this point.

###### To monitor progress when restoring a backup (CLI)

- When you restore a backup to a new volume on a second-generation FSx for ONTAP file system,
  you can monitor the progress of the restore using the
  [`describe-volumes`](../APIReference/API_DescribeVolumes.md "../APIReference/API_DescribeVolumes.md") CLI command.

When restoring a backup to a second-generation file system, the response includes the `AdministrativeActions` object, which
provides status information about the data downloading process. The

```
`$` `aws fsx describe-volumes`
`{
 “Volumes”: [
 {
 “CreationTime”: 1691686114.674,
 “FileSystemId”: fs-029ff92192bd4d375,
 “LifeCycle”: “CREATING”,
 “Name”: vol1,
 “OntapConfiguration”: {
 “FlexCacheEndpointType”: “NONE”,
 “JunctionPath”: “/vol1”,
 “SizeInMegabytes”: 100000,
 “StorageEfficiencyEnabled”: true,
 “StorageVirtualMachineId”: “svm-0ed1d714019426ca9”,
 “StorageVirtualMachineRoot”: false,
 “TieringPolicy”: {
 “Name”: “ALL”
 },
 “OntapVolumeType”: “DP”,
 “SnapshotPolicy”: “default”,
 “CopyTagsToBackups”: false,
 },
 “ResourceARN”: “arn:aws:fsx:us-east-1:630831496844:volume/fs-08ac75f715c6aec76/fsvol-094c015af930790fa”,
 “VolumeId”: “fsvol-094c015af930790fa”,
 “VolumeType”: “ONTAP”,
 “AdministrativeActions”: [
 {
 “AdministrativeActionType”: “DOWNLOAD_DATA_FROM_BACKUP”,
 “RequestTime”: 1685729972.069,
 “Status”: “PENDING”
 }
 ]
 }`
```

Once Amazon FSx loads all of the file metadata onto the restored volume, these fields have the following values:

    + `"LifeCycle": "CREATED"` – indicates that the volume is ready to be mounted.
    + `"OntapVolumeType": "DP"` – indicates that the volume is read-only while the file data is downloading.
    + `"ProgressPercent` –shows the percentage of file data that is loaded onto the volume.
    + `"Status": "IN_PROGRESS"` – downloading the file data to the volume is in progress.

At this stage in the restore process you can mount the volume with read-only access to all the data in the backup that you are restoring.

When Amazon FSx has completed downloading all the file data onto the new volume, clients have full read-write access
if this is `RW` volume. The indicators have the following values:

    + `"LifeCycle": "CREATED"` – unchanged
    + `"OntapVolumeType": "RW"` – indicates that clients have full read-write access.
    + `"Status": "COMPLETED"` – indicates that the restore is complete.

If the restore process fails, the `AdminstrativeAction > Status` will have a value of `FAILED`.
An error message is provided in the `FailureDetails` object. For more information, see
[AdministrativeActionFailureDetails](../APIReference/API_AdministrativeActionFailureDetails.md "../APIReference/API_AdministrativeActionFailureDetails.md")
in the Amazon FSx API Reference
