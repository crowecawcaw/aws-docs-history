# Create an EBS volume from an imported snapshot

You can create EBS volumes from an EBS snapshot. You can attach an EBS volume
to an EC2 instance.

AWS CLI

###### To create a volume and attach it to an EC2 instance

1. Use the [describe-import-snapshot-tasks](../../../cli/latest/reference/ec2/describe-import-snapshot-tasks.md "../../../cli/latest/reference/ec2/describe-import-snapshot-tasks.md")
   command to determine the ID of the snapshot that was created by the import task.
2. Use the following [create-volume](../../../cli/latest/reference/ec2/create-volume.md "../../../cli/latest/reference/ec2/create-volume.md") command
   to create a volume from the snapshot. You must select the Availability Zone of the instance
   to which you'll attach the volume.

```
aws ec2 create-volume \
    --availability-zone `us-east-1a` \
    --snapshot-id `snap-1234567890abcdef0`
```

The following is example output.

```
{
    "AvailabilityZone": "us-east-1a",
    "VolumeId": "vol-1234567890abcdef0",
    "State": "creating",
    "SnapshotId": "snap-1234567890abcdef0"
}
```

3. Use the following [attach-volume](../../../cli/latest/reference/ec2/attach-volume.md "../../../cli/latest/reference/ec2/attach-volume.md") command to attach the EBS volume that you created in the
   previous step to one of your existing instances.

```
aws ec2 attach-volume \
    --volume-id `vol-1234567890abcdef0` \
    --instance-id `i-1234567890abcdef0` \
    --device `/dev/sdf`
```

The following is example output.

```
{
    "AttachTime": "YYYY-MM-DDTHH:MM:SS.000Z",
    "InstanceId": "i-1234567890abcdef0",
    "VolumeId": "vol-1234567890abcdef0",
    "State": "attaching",
    "Device": "/dev/sdf"
}
```

4. Mount the attached volume. For more information, see the documentation for the operating
   system for your instance.

PowerShell

###### To create a volume and attach it to an EC2 instance

1. Use the [Get-EC2ImportSnapshotTask](../../../powershell/latest/reference/items/Get-EC2ImportSnapshotTask.md "../../../powershell/latest/reference/items/Get-EC2ImportSnapshotTask.md") cmdlet to determine the ID
   of the snapshot that was created by the import task.
2. Use the [New-EC2Volume](../../../powershell/latest/reference/items/New-EC2Volume.md "../../../powershell/latest/reference/items/New-EC2Volume.md") cmdlet to create a volume from the snapshot.
   You must select the Availability Zone of the instance to which you'll
   attach the volume.

```
New-EC2Volume `
    -AvailabilityZone `us-east-1a` `
    -SnapshotId `snap-1234567890abcdef0`
```

The following is example output.

```
Attachments        : {}
AvailabilityZone   : us-east-1a
CreateTime         : 7/15/2025 3:37:56 PM
Encrypted          : False
FastRestored       : False
Iops               : 3000
KmsKeyId           :
MultiAttachEnabled : False
Operator           :
OutpostArn         :
Size               : 41
SnapshotId         : snap-1234567890abcdef0
SseType            :
State              : creating
Tags               : {}
Throughput         : 125
VolumeId           : vol-1234567890abcdef0
VolumeType         : gp3
```

3. Use the [Add-EC2Volume](../../../powershell/latest/reference/items/Add-EC2Volume.md "../../../powershell/latest/reference/items/Add-EC2Volume.md") cmdlet

```
Add-EC2Volume `
    -VolumeId `vol-1234567890abcdef0` `
    -InstanceId `i-1234567890abcdef0` `
    -Device `xvdb`
```

The following is example output.

```
AssociatedResource    :
AttachTime            : 7/15/2025 3:47:20 PM
DeleteOnTermination   : False
Device                : xvdb
InstanceId            : i-1234567890abcdef0
InstanceOwningService :
State                 : attaching
VolumeId              : vol-1234567890abcdef0
```

4. Mount the attached volume. For more information, see the documentation for the operating
   system for your instance.
