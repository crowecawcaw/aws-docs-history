# Updating a tiering policy

You can modify a volume's tiering policy using the AWS Management Console, AWS CLI and API, and the ONTAP CLI.

Use the following procedure to modify a volume's data-tiering policy using the AWS Management Console.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Choose **Volumes** in the left navigation pane, then choose the ONTAP volume
   for which you want to modify the data-tiering policy.
3. Choose **Update volume** from the **Actions** drop down menu.
   The **Update volume** window appears.
4. For **Capacity pool tiering policy**, choose the new policy for the volume.
   For more information, see [Volume tiering policies](volume-storage-capacity.md#data-tiering-policy "volume-storage-capacity.md#data-tiering-policy").
5. Choose **Update** to apply the new policy to the volume.

- Modify a volume's tiering policy using the
  [update-volume](../../../cli/latest/reference/fsx/update-volume.md "../../../cli/latest/reference/fsx/update-volume.md") CLI command
  ([UpdateVolume](../APIReference/API_UpdateVolume.md "../APIReference/API_UpdateVolume.md") is the equivalent Amazon FSx API action).
  The following CLI command example sets a volume's data-tiering policy to `SNAPSHOT_ONLY`.

```
aws fsx update-volume \
    --volume-id `fsxvol-abcde0123456789f`
    --ontap-configuration TieringPolicy={Name=SNAPSHOT_ONLY}
```

For a successful request, the system responds with the volume description.

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
                "CoolingPeriod": 2,
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

You use the `volume modify` ONTAP CLI command to set a volume's tiering policy.
For more information, see
[`volume modify`](https://docs.netapp.com/us-en/ontap-cli-9111/volume-modify.html "https://docs.netapp.com/us-en/ontap-cli-9111/volume-modify.html") in the NetApp ONTAP Documentation Center.

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

3. Use the following command to modify the volume data-tiering policy, replacing the following values:
   - Replace `svm_name` with the name of the SVM that
     the volume is created on.
   - Replace `vol_name` with name of the volume for which you
     are setting the data-tiering policy.
   - Replace `tiering_policy` with the desired policy. Valid values are
     `snapshot-only`, `auto`, `all`, or `none`. For more information, see
     [Volume tiering policies](volume-storage-capacity.md#data-tiering-policy "volume-storage-capacity.md#data-tiering-policy").

```
`FSx::>` volume modify -vserver `svm_name` -volume `vol_name` -tiering-policy `tiering_policy`
```
