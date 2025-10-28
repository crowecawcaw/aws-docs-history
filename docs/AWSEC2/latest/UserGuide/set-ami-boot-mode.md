# Set the boot mode of an Amazon EC2 AMI

By default, an AMI inherits the boot mode of the EC2 instance used to create the AMI.
For example, if you create an AMI from an EC2 instance running on Legacy BIOS, the
boot mode of the new AMI is `legacy-bios`. If you create an AMI from an
EC2 instance with a boot mode of `uefi-preferred`, the boot mode of the
new AMI is `uefi-preferred`.

When you register an AMI, you can set the boot mode of the AMI to
`uefi`, `legacy-bios`, or `uefi-preferred`.

When the AMI boot mode is set to `uefi-preferred`, the instance boots as follows:

- For instance types that support both UEFI and Legacy BIOS (for example,
  `m5.large`), the instance boots using UEFI.
- For instance types that support only Legacy BIOS (for example, `m4.large`),
  the instance boots using Legacy BIOS.
  If you set the AMI boot mode to `uefi-preferred`, the operating system must
  support the ability to boot both UEFI and Legacy BIOS.

To convert an existing Legacy BIOS-based instance to UEFI, or an existing UEFI-based
instance to Legacy BIOS, you must first modify the instance's volume and operating system
to support the selected boot mode. Then, create a snapshot of the volume.
Finally, create an AMI from the snapshot.

###### Considerations

- Setting the AMI boot mode parameter does not automatically configure the operating system
  for the specified boot mode. You must first make
  suitable modifications to the instance's volume and operating system to support
  booting using the selected boot mode. Otherwise, the resulting AMI is not usable.
  For example, if you are converting a Legacy BIOS-based Windows instance to
  UEFI, you can use the [MBR2GPT](https://learn.microsoft.com/en-us/windows/deployment/mbr-to-gpt "https://learn.microsoft.com/en-us/windows/deployment/mbr-to-gpt") tool from Microsoft to convert the system disk from MBR to GPT.
  The modifications that are required are operating system-specific. For more
  information, see the manual for your operating system.
- You can't use the [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command or the [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") cmdlet to create an AMI that
  supports both [NitroTPM](nitrotpm.md "nitrotpm.md") and UEFI Preferred.
- Some features, like UEFI Secure Boot, are only available on instances that boot on UEFI.
  When you use the `uefi-preferred` AMI boot mode parameter with an
  instance type that does not support UEFI, the instance launches as Legacy BIOS
  and the UEFI-dependent feature is disabled. If you rely on the availability of
  a UEFI-dependent feature, set your AMI boot mode parameter to `uefi`.

AWS CLI

###### To set the boot mode of an AMI

1. Make suitable modifications to the instance's volume and operating system to support
   booting via the selected boot mode. The modifications that are required are
   operating system-specific. For more information, see the manual for your
   operating system.

###### Warning

If you don't perform this step, the AMI will not be usable. 2. To find the volume ID of the instance, use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command. You'll create a
snapshot of this volume in the next step.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` \
    --query Reservations[].Instances[].BlockDeviceMappings
```

The following is example output.

```
[
    [
        {
            "DeviceName": "/dev/xvda",
            "Ebs": {
                "AttachTime": "2024-07-11T01:05:51+00:00",
                "DeleteOnTermination": true,
                "Status": "attached",
                "VolumeId": "`vol-1234567890abcdef0`"
            }
        }
    ]
]
```

3. To create a snapshot of the volume, use the [create-snapshot](../../../cli/latest/reference/ec2/create-snapshot.md "../../../cli/latest/reference/ec2/create-snapshot.md") command. Use the volume ID from the
   previous step.

```
aws ec2 create-snapshot \
    --volume-id `vol-01234567890abcdef` \
    --description "`my snapshot`"
```

The following is example output.

```
{
    "Description": "my snapshot",
    "Encrypted": false,
    "OwnerId": "123456789012",
    "Progress": "",
    "SnapshotId": "snap-0abcdef1234567890",
    "StartTime": "",
    "State": "pending",
    "VolumeId": "vol-01234567890abcdef",
    "VolumeSize": 30,
    "Tags": []
}
```

4. Wait until the state of the snapshot is `completed` before
   you go to the next step. To get the state of the snapshot, use the [describe-snapshots](../../../cli/latest/reference/ec2/describe-snapshots.md "../../../cli/latest/reference/ec2/describe-snapshots.md") command with
   the snapshot ID from the previous step.

```
aws ec2 describe-snapshots \
    --snapshot-ids `snap-0abcdef1234567890` \
    --query Snapshots[].State \
    --output text
```

The following is example output.

```
completed
```

5. To create a new AMI, use the [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command. Use the value of `SnapshotId`
   from the output of **CreateSnapshot**.
   - To set the boot mode to UEFI, add the `--boot-mode` parameter with
     a value of `uefi`.

   ```
   aws ec2 register-image \
      --description "`my image`" \
      --name "`my-image`" \
      --block-device-mappings "DeviceName=/dev/sda1,Ebs={SnapshotId=`snap-0abcdef1234567890`,DeleteOnTermination=true}" \
      --root-device-name /dev/sda1 \
      --virtualization-type hvm \
      --ena-support \
      **--boot-mode uefi**
   ```

   - To set the boot mode to `uefi-preferred`, set the value of
     `--boot-mode` to `uefi-preferred`

   ```
   aws ec2 register-image \
      --description "`my description`" \
      --name "`my-image`" \
      --block-device-mappings "DeviceName=/dev/sda1,Ebs={SnapshotId=`snap-0abcdef1234567890`,DeleteOnTermination=true}" \
      --root-device-name /dev/sda1 \
      --virtualization-type hvm \
      --ena-support \
      **--boot-mode uefi-preferred**
   ```

6. (Optional) To verify that the newly-created AMI has the boot mode that
   you specified, use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command.

```
aws ec2 describe-images \
    --image-id `ami-1234567890abcdef0` \
    --query Images[].BootMode \
    --output text
```

The following is example output.

```
uefi
```

PowerShell

###### To set the boot mode of an AMI

1. Make suitable modifications to the instance's volume and operating system to support
   booting via the selected boot mode. The modifications that are required are
   operating system-specific. For more information, see the manual for your
   operating system.

###### Warning

If you don't perform this step, the AMI will not be usable. 2. To find the volume ID of the instance, use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet.

```
(Get-EC2Instance `
    -InstanceId `i-1234567890abcdef0`).Instances.BlockDeviceMappings.Ebs
```

The following is example output.

```
AssociatedResource  :
AttachTime          : 7/11/2024 1:05:51 AM
DeleteOnTermination : True
Operator            :
Status              : attached
VolumeId            : vol-01234567890abcdef
```

3. To create a snapshot of the volume, use the [New-EC2Snapshot](../../../powershell/latest/reference/items/New-EC2Snapshot.md "../../../powershell/latest/reference/items/New-EC2Snapshot.md") cmdlet. Use the
   volume ID from the previous step.

```
New-EC2Snapshot `
    -VolumeId `vol-01234567890abcdef` `
    -Description "`my snapshot`"
```

The following is example output.

```
AvailabilityZone          :
Description               : my snapshot
Encrypted                 : False
FullSnapshotSizeInBytes   : 0
KmsKeyId                  :
OwnerId                   : 123456789012
RestoreExpiryTime         :
SnapshotId                : snap-0abcdef1234567890
SseType                   :
StartTime                 : 4/25/2025 6:08:59 PM
State                     : pending
StateMessage              :
VolumeId                  : vol-01234567890abcdef
VolumeSize                : 30
```

4. Wait until the state of the snapshot is `completed` before you go to the
   next step. To get the state of the snapshot, use the [Get-EC2Snapshot](../../../powershell/latest/reference/items/Get-EC2Snapshot.md "../../../powershell/latest/reference/items/Get-EC2Snapshot.md") cmdlet with the
   snapshot ID from the previous step.

```
(Get-EC2Snapshot `
    -SnapshotId `snap-0abcdef1234567890`).State.Value
```

The following is example output.

```
completed
```

5. To create a new AMI, use the [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") cmdlet. Use the
   value of `SnapshotId` from the output of
   **New-EC2Snapshot**.
   - To set the boot mode to UEFI, add the `-BootMode` parameter with a value
     of `uefi`.

   ```
   $block = @{SnapshotId=snap-0abcdef1234567890}
   Register-EC2Image `
      -Description "`my image`" `
      -Name "`my-image`" `
      -BlockDeviceMapping @{DeviceName="`/dev/xvda`";Ebs=$block} `
      -RootDeviceName `/dev/xvda` `
      -EnaSupport $true `
      **-BootMode uefi**
   ```

   - To set the boot mode to `uefi-preferred`, set the value of
     `-BootMode` to `uefi-preferred`

   ```
   $block = @{SnapshotId=snap-0abcdef1234567890}
   Register-EC2Image `
      -Description "`my image`" `
      -Name "`my-image`" `
      -BlockDeviceMapping @{DeviceName="`/dev/xvda`";Ebs=$block} `
      -RootDeviceName `/dev/xvda` `
      -EnaSupport $true `
      **-BootMode uefi-preferred**
   ```

6. (Optional) To verify that the newly-created AMI has the boot mode that
   you specified, use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md") cmdlet.

```
(Get-EC2Image `
    -ImageId `ami-1234567890abcdef0`).BootMode.Value
```

The following is example output.

```
uefi
```
