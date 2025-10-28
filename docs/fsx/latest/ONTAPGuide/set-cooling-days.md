# Updating the minimum cooling days

Minimum cooling days for a volume set the threshold that's used to
determine which data is warm and which data is cold. You can set a volume's minimum
cooling days using AWS CLI and API, and the ONTAP CLI.

- Modify a volume configuration by using the
  [update-volume](../../../cli/latest/reference/fsx/update-volume.md "../../../cli/latest/reference/fsx/update-volume.md") CLI command
  ([UpdateVolume](../APIReference/API_UpdateVolume.md "../APIReference/API_UpdateVolume.md") is the equivalent Amazon FSx API action).
  The following CLI command example sets a volume's `CoolingPeriod` to 104 days.

```
aws fsx update-volume \
    --volume-id `fsxvol-abcde0123456789f`
    --ontap-configuration TieringPolicy={Name=SNAPSHOT_ONLY}
aws fsx update-volume --volume-id fsvol-006530558c14224ac --ontap-configuration TieringPolicy={CoolingPeriod=104}

```

The system responds with the volume description for a successful request.

```
{
    "Volume": {
        "CreationTime": "2021-10-05T14:27:44.332000-04:00",
        "FileSystemId": "fs-abcde0123456789f",
        "Lifecycle": "CREATED",
        "Name": "vol1",
        "OntapConfiguration": {
            "FlexCacheEndpointType": "NONE",
            "JunctionPath": "/vol1",
            "SecurityStyle": "UNIX",
            "SizeInMegabytes": 1048576,
            "StorageEfficiencyEnabled": true,
            "StorageVirtualMachineId": "svm-abc0123de456789f",
            "StorageVirtualMachineRoot": false,
            "TieringPolicy": {
                "CoolingPeriod": 104,
                "Name": "SNAPSHOT_ONLY"
            },
            "UUID": "aaaa1111-bb22-cc33-dd44-abcde01234f5",
            "OntapVolumeType": "RW"
        },
        "ResourceARN": "arn:aws:fsx:us-east-2:111122223333:volume/fs-abcde0123456789f/fsvol-abc012def3456789a",
        "VolumeId": "fsvol-abc012def3456789a",
        "VolumeType": "ONTAP"
    }
}
```

Use the `volume modify` ONTAP CLI command to set the
minimum number of cooling days for an existing volume. For more
information, see [`volume modify`](https://docs.netapp.com/us-en/ontap-cli-9111/volume-modify.html "https://docs.netapp.com/us-en/ontap-cli-9111/volume-modify.html") in the NetApp ONTAP
Documentation Center.

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Enter the ONTAP CLI advanced mode using the following command.

```
`FSx::>` `set adv`

`Warning: These advanced commands are potentially dangerous; use them only when
 directed to do so by NetApp personnel.
Do you want to continue? {y|n}:` `y`
```

3. Use the following command to change your volume’s tiering minimum cooling days,
   replacing the following values:
   - Replace `svm_name` with the name of the SVM that
     the volume is created on.
   - Replace `vol_name` with name of the volume for which you
     are setting the cooling days.
   - Replace `cooling_days` with the desired, an integer between 2-183.

```
`FSx::>` `volume modify -vserver `svm_name` -volume `vol_name` -tiering-minimum-cooling-days `cooling_days``
```

The system responds as follows for a successful request.

```
Volume modify successful on volume vol_name of Vserver svm_name.
```
