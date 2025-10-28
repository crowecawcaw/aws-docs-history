# Monitoring volumes

You can see the volumes that are currently on your file system using
the Amazon FSx console, the AWS CLI, and the Amazon FSx API and SDKs.

###### To monitor the volumes on your file system:

- **Using the console** – Choose a file
  system to view the **File systems** detail page. Choose the
  **Volumes** tab to list all the volumes on the file
  system, and then choose the volume you want to view.
- **Using the CLI or API** – Use the
  [describe-volumes](../../../cli/latest/reference/fsx/describe-volumes.md "../../../cli/latest/reference/fsx/describe-volumes.md") CLI command or the [DescribeVolumes](../APIReference/API_DescribeVolumes.md "../APIReference/API_DescribeVolumes.md") API operation.

```
`$` `aws fsx describe-volumes`
`{
 "Volumes": [
 {
 "CreationTime": "2024-03-04T20:17:44+00:00",
 "FileSystemId": "fs-abcdef0123a0bb087",
 "Lifecycle": "CREATED",
 "Name": "SVM8_ext_root",
 "OntapConfiguration": {
 "FlexCacheEndpointType": "NONE",
 "JunctionPath": "/",
 "SecurityStyle": "NTFS",
 "SizeInMegabytes": 1024,
 "StorageEfficiencyEnabled": false,
 "StorageVirtualMachineId": "svm-01234567890abcdef",
 "StorageVirtualMachineRoot": true,
 "TieringPolicy": {
 "Name": "NONE"
 },
 "UUID": "42ce3de0-da64-11ee-a22d-7f7cdfb8d381",
 "OntapVolumeType": "RW",
 "SnapshotPolicy": "default",
 "CopyTagsToBackups": false,
 "VolumeStyle": "FLEXVOL",
 "AggregateConfiguration": {
 "Aggregates": [
 "aggr1"
 ]
 },
 "SizeInBytes": 1073741824
 },
 "ResourceARN": "arn:aws:fsx:us-east-2:111122223333:volume/fs-abcdef0123a0bb087/fsvol-abcdef0123456789a",
 "VolumeId": "fsvol-abcdef0123456789a",
 "VolumeType": "ONTAP"
 }
 ]
}`
```
