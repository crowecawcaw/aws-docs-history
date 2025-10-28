# Add optional Windows Server components to Amazon EC2 Windows instances

To access and install the optional components, you must find the correct EBS snapshot for
your version of Windows Server, create a volume from the snapshot, and attach the volume to
your instance.

###### Before you begin

Use the AWS Management Console or a command line tool to get the instance ID and Availability Zone
of your instance. You must create your EBS volume in the same Availability Zone
as your instance.

Use one of the following procedures to add Windows Server components to your instance.

Console

###### To add Windows components to your instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. From the **Filter** bar, choose **Public
   snapshots**.
4. Add the **Owner Alias** filter and choose
   **amazon**.
5. Add the **Description** filter and enter
   `Windows`.
6. Press Enter
7. Select the snapshot that matches your system architecture and language
   preference. For example, select **Windows 2019 English Installation
   Media** if your instance is running Windows Server 2019.
8. Choose **Actions**, **Create volume from
   snapshot**.
9. For **Availability Zone**, select the Availability Zone that
   matches your Windows instance. Choose **Add tag** and enter
   `Name` for the tag key and a descriptive name for the
   tag value. Choose **Create volume**.
10. In the **Successfully created volume** message (green
    banner), choose the volume that you just created.
11. Choose **Actions**, **Attach
    volume**.
12. From **Instance**, select the instance ID.
13. For **Device name**, enter the name of the device for the
    attachment. If you need help with the device name, see [Device names for volumes on Amazon EC2 instances](device_naming.md "device_naming.md").
14. Choose **Attach volume**.
15. Connect to your instance and make the volume available. For more information, see
    [Make an Amazon EBS volume
    available for use](../../../ebs/latest/userguide/ebs-using-volumes.md "../../../ebs/latest/userguide/ebs-using-volumes.md") in the _Amazon EBS User Guide_.

###### Important

Do not initialize the volume. 16. Open **Control Panel**, **Programs and Features**. Choose
**Turn Windows features on or off**. If you are prompted for installation media,
specify the EBS volume with the installation media. 17. (Optional) When you are finished with the installation media, you can detach the volume.
After you detach the volume, you can delete it.

AWS CLI

###### To add Windows components to your instance

1. Use the [describe-snapshots](../../../cli/latest/reference/ec2/describe-snapshots.md "../../../cli/latest/reference/ec2/describe-snapshots.md") command with
   the `owner-ids` parameter and `description` filter to get a list of the available installation
   media snapshots.

```
aws ec2 describe-snapshots \
    --owner-ids amazon \
    --filters Name=description,Values=Windows*
```

2. In the output, note the ID of the snapshot that matches your system architecture and language preference.
   For example:

```
{
    "Snapshots": [
    ...
        {
            "OwnerAlias": "amazon",
            "Description": "Windows 2019 English Installation Media",
            "Encrypted": false,
            "VolumeId": "vol-be5eafcb",
            "State": "completed",
            "VolumeSize": 6,
            "Progress": "100%",
            "StartTime": "2019-10-25T20:00:47.000Z",
            "SnapshotId": "snap-22da283e",
            "OwnerId": "123456789012"
        },
    ...
   ]
}
```

3. Use the [create-volume](../../../cli/latest/reference/ec2/create-volume.md "../../../cli/latest/reference/ec2/create-volume.md") command to create a volume
   from the snapshot. Specify the same Availability Zone as your instance.

```
aws ec2 create-volume \
    --snapshot-id `snap-0abcdef1234567890` \
    --volume-type `gp2` \
    --availability-zone `us-east-1a`
```

4. In the output, note the volume ID.

```
{
    "AvailabilityZone": "us-east-1a",
    "Encrypted": false,
    "VolumeType": "gp2",
    "VolumeId": "vol-01234567890abcdef",
    "State": "creating",
    "Iops": 100,
    "SnapshotId": "snap-0abcdef1234567890",
    "CreateTime": "2017-04-18T10:33:10.940Z",
    "Size": 6
}
```

5. Use the [attach-volume](../../../cli/latest/reference/ec2/attach-volume.md "../../../cli/latest/reference/ec2/attach-volume.md") command to attach the volume
   to your instance.

```
aws ec2 attach-volume \
    --volume-id `vol-0c98b37f30bcbc290` \
    --instance-id `i-01474ef662b89480` \
    --device `xvdg`
```

6. Connect to your instance and make the volume available. For more information, see
   [Make an Amazon EBS volume
   available for use](../../../ebs/latest/userguide/ebs-using-volumes.md "../../../ebs/latest/userguide/ebs-using-volumes.md") in the _Amazon EBS User Guide_.

###### Important

Do not initialize the volume. 7. Open **Control Panel**, **Programs and Features**. Choose
**Turn Windows features on or off**. If you are prompted for installation media,
specify the EBS volume with the installation media. 8. (Optional) When you are finished with the installation media, use the [detach-volume](../../../cli/latest/reference/ec2/detach-volume.md "../../../cli/latest/reference/ec2/detach-volume.md") command to detach
the volume from your instance. After you detach the volume, you can use the [delete-volume](../../../cli/latest/reference/ec2/delete-volume.md "../../../cli/latest/reference/ec2/delete-volume.md") command to
delete the volume.

PowerShell

###### To add Windows components to your instance

1. Use the [Get-EC2Snapshot](../../../powershell/latest/reference/items/Get-EC2Snapshot.md "../../../powershell/latest/reference/items/Get-EC2Snapshot.md")
   cmdlet with the `Owner` and `description` filters to get a list of
   the available installation media snapshots.

```
Get-EC2Snapshot `
    -Owner amazon `
    -Filter @{ Name="description"; Values="Windows*" }
```

2. In the output, note the ID of the snapshot that matches your system architecture and language preference.
   For example:

```
...
DataEncryptionKeyId :
Description         : Windows 2019 English Installation Media
Encrypted           : False
KmsKeyId            :
OwnerAlias          : amazon
OwnerId             : 123456789012
Progress            : 100%
SnapshotId          : snap-0abcdef1234567890
StartTime           : 10/25/2019 8:00:47 PM
State               : completed
StateMessage        :
Tags                : {}
VolumeId            : vol-01234567890abcdef
VolumeSize          : 6
...
```

3. Use the [New-EC2Volume](../../../powershell/latest/reference/items/New-EC2Volume.md "../../../powershell/latest/reference/items/New-EC2Volume.md")
   cmdlet to create a volume from the snapshot. Specify the same Availability Zone as your instance.

```
New-EC2Volume `
    -AvailabilityZone `us-east-1a` `
    -VolumeType `gp2` `
    -SnapshotId `snap-0abcdef1234567890`
```

4. In the output, note the volume ID.

```
Attachments      : {}
AvailabilityZone : us-east-1a
CreateTime       : 4/18/2017 10:50:25 AM
Encrypted        : False
Iops             : 100
KmsKeyId         :
Size             : 6
SnapshotId       : snap-0abcdef1234567890
State            : creating
Tags             : {}
VolumeId         : vol-01234567890abcdef
VolumeType       : gp2
```

5. Use the [Add-EC2Volume](../../../powershell/latest/reference/items/Add-EC2Volume.md "../../../powershell/latest/reference/items/Add-EC2Volume.md")
   cmdlet to attach the volume to your instance.

```
Add-EC2Volume `
    -InstanceId `i-1234567890abcdef0` `
    -VolumeId `vol-01234567890abcdef` `
    -Device `xvdh`
```

6. Connect to your instance and make the volume available. For more information, see
   [Make an Amazon EBS volume
   available for use](../../../ebs/latest/userguide/ebs-using-volumes.md "../../../ebs/latest/userguide/ebs-using-volumes.md") in the _Amazon EBS User Guide_.

###### Important

Do not initialize the volume. 7. Open **Control Panel**, **Programs and Features**. Choose
**Turn Windows features on or off**. If you are prompted for installation media,
specify the EBS volume with the installation media. 8. (Optional) When you are finished with the installation media, use the [Dismount-EC2Volume](../../../powershell/latest/reference/items/Dismount-EC2Volume.md "../../../powershell/latest/reference/items/Dismount-EC2Volume.md") cmdlet to detach
the volume from your instance. After you detach the volume, you can use the [Remove-EC2Volume](../../../powershell/latest/reference/items/Remove-EC2Volume.md "../../../powershell/latest/reference/items/Remove-EC2Volume.md") cmdlet to
delete the volume.
