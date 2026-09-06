

# Replace an Amazon EBS volume using a snapshot
<a name="ebs-restoring-volume"></a>

Amazon EBS snapshots are the preferred backup tool on Amazon EC2 because of their speed, convenience, and cost. When creating a volume from a snapshot, you recreate its state at a specific point in time with the data saved up to that specific point intact. By attaching a volume created from a snapshot to an instance, you can duplicate data across Regions, create test environments, replace a damaged or corrupted production volume in its entirety, or retrieve specific files and directories and transfer them to another attached volume. For more information, see [Amazon EBS snapshots](ebs-snapshots.md).

You can use one of the following procedures to replace an Amazon EBS volume with another volume created from a previous snapshot of that volume.

**Requirement**  
You must create the volume in the same Availability Zone as the instance. Volumes must be attached to instances in the same Availability Zone.

------
#### [ Console ]

**To replace a volume**

1. Create a volume from the snapshot and write down the ID of the new volume. For more information, see [Create an Amazon EBS volume](ebs-creating-volume.md).

1. On the Instances page, select the instance on which to replace the volume and write down the instance ID.

   With the instance still selected, choose the **Storage** tab. In the **Block devices** section, find the volume to replace and write down the device name for the volume, for example `/dev/sda1`.

1. On the **Storage** tab, choose the volume ID, and then [ unmount and detach the volume from the instance](ebs-detaching-volume.md#umount-detach-volume).

1. Select the new volume that you created in step 1 and choose **Actions**, **Attach volume**.

   For **Instance** and **Device name**, enter the instance ID and device name that you wrote down in Step 2, and then choose **Attach volume**.

1. Connect to your instance and mount the volume. For more information, see [Make an Amazon EBS volume available for use](ebs-using-volumes.md).

------
#### [ AWS CLI ]

**To replace a volume**

1. Create a new volume from the snapshot. Use the [create-volume](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-volume.html) command with the `--snapshot-id` option. For `--availability-zone`, specify the same Availability Zone as the instance. Note the ID of the new volume in the output.

   ```
   aws ec2 create-volume \
       --volume-type {{gp3}} \
       --snapshot-id {{snap-0abcdef1234567890}} \
       --availability-zone {{us-east-1a}}
   ```

1. Get the device name of the volume to replace. Use the [describe-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html) command. For `--instance-ids`, specify the ID of the instance on which to replace the volume. Note the device name and volume ID of the volume to replace.

   ```
   aws ec2 describe-instances \
       --instance-ids {{i-1234567890abcdef0}} \
       --query Reservations[].Instances[].BlockDeviceMappings
   ```

1. Detach the volume to replace from the instance. Use the [detach-volume](https://docs.aws.amazon.com/cli/latest/reference/ec2/detach-volume.html) command.

   ```
   aws ec2 detach-volume --volume-id {{vol-xxxxxxxxxxxxxxxxx}}
   ```

1. Attach the replacement volume to the instance. Use the [attach-volume](https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-volume.html) command. For `--volume-id`, specify the ID of the replacement volume. For `--instance-id`, specify the ID of the instance on which to attach the volume. For `--device`, specify the same device name that you noted previously.

   ```
   aws ec2 attach-volume \
       --volume-id {{vol-01234567890abcdef}} \
       --instance-id {{i-1234567890abcdef0}} \
       --device {{/dev/sdf}}
   ```

1. Connect to your instance and mount the volume. For more information, see [Make an Amazon EBS volume available for use](ebs-using-volumes.md).

------
#### [ PowerShell ]

**To replace a volume**

1. Create a new volume from the snapshot. Use the [New-EC2Volume](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Volume.html) cmdlet with the `-SnapshotId` option. For `-AvailabilityZone`, specify the same Availability Zone as the instance. Note the ID of the new volume in the output.

   ```
   New-EC2Volume `
       -VolumeType {{gp3}} `
       -SnapshotId {{snap-0abcdef1234567890}} `
       -AvailabilityZone {{us-east-1a}}
   ```

1. Get the device name of the volume to replace. Use the [Get-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Instance.html) cmdlet. For `-InstanceId`, specify the ID of the instance on which to replace the volume. Note the device name and volume ID of the volume to replace.

   ```
   (Get-EC2Instance `
       -InstanceId {{i-1234567890abcdef0}}).Instances.BlockDeviceMappings | `
        Format-Table DeviceName, @{Name="VolumeId";Expression={$_.Ebs.VolumeId}}
   ```

1. Detach the volume to replace from the instance. Use the [Dismount-EC2Volume](https://docs.aws.amazon.com/powershell/latest/reference/items/Dismount-EC2Volume.html) cmdlet.

   ```
   DismountEC2Volume -VolumeId {{vol-xxxxxxxxxxxxxxxxx}}
   ```

1. Attach the replacement volume to the instance. Use the [Add-EC2Volume](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-EC2Volume.html) cmdlet. For `-VolumeId`, specify the ID of the replacement volume. For `-InstanceId`, specify the ID of the instance on which to attach the volume. For `-Device`, specify the same device name that you noted previously.

   ```
   Add-EC2Volume`
       -VolumeId {{vol-01234567890abcdef}} `
       -InstanceId {{i-1234567890abcdef0}} `
       -Device {{/dev/sdf}}
   ```

1. Connect to your instance and mount the volume. For more information, see [Make an Amazon EBS volume available for use](ebs-using-volumes.md).

------