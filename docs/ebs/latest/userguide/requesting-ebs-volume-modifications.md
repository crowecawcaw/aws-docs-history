# Request Amazon EBS volume modifications

With Elastic Volumes, you can dynamically increase the size, increase or decrease the
performance, and change the volume type of your Amazon EBS volumes without detaching them.

###### Process overview

1. (Optional) Before modifying a volume that contains valuable data, it is a best
   practice to create a snapshot of the volume in case you need to roll back your changes.
   For more information, see [Create Amazon EBS snapshots](ebs-creating-snapshot.md "ebs-creating-snapshot.md").
2. Request the volume modification.
3. Monitor the progress of the volume modification. For more information, see [Monitor the progress of Amazon EBS volume modifications](monitoring-volume-modifications.md "monitoring-volume-modifications.md").
4. If the size of the volume was modified, extend the volume's file system to take
   advantage of the increased storage capacity. For more information, see
   [Extend the file system after resizing an Amazon EBS volume](recognize-expanded-volume-linux.md "recognize-expanded-volume-linux.md").

###### Contents

- [Modify an EBS volume using Elastic Volumes](#modify-ebs-volume "#modify-ebs-volume")
- [Modify an EBS volume if Elastic Volumes is not
  supported](#modify-volume-stop-start "#modify-volume-stop-start")
- [Initialize Elastic Volumes support (if needed)](#initialize-modification-support "#initialize-modification-support")

## Modify an EBS volume using Elastic Volumes

Before you begin, see the following:

- [Considerations](ebs-modify-volume.md#elastic-volumes-considerations "ebs-modify-volume.md#elastic-volumes-considerations")
- [Limitations](ebs-modify-volume.md#elastic-volumes-limitations "ebs-modify-volume.md#elastic-volumes-limitations")
- [Requirements](modify-volume-requirements.md "modify-volume-requirements.md")

Console

###### To modify an EBS volume

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.
3. Select the volume to modify and choose **Actions**,
   **Modify volume**.
4. The **Modify volume** screen displays the volume ID and the
   volume's current configuration, including type, size, IOPS, and throughput. Set new
   configuration values as follows:
   - To modify the type, choose a value for **Volume type**.
   - To modify the size, enter a new value for **Size**.
   - (`gp3`, `io1`, and `io2` only) To modify the IOPS, enter a new value for
     **IOPS**.
   - (`gp3` only) To modify the throughput, enter a new value for
     **Throughput**.

5. After you have finished changing the volume settings, choose **Modify**.
   When prompted for confirmation, choose **Modify**.
6. If you've increased the size of your volume, then you must also extend the
   volume's partition to make use of the additional storage capacity. For more
   information, see [Extend the file system after resizing an Amazon EBS volume](recognize-expanded-volume-linux.md "recognize-expanded-volume-linux.md").
7. (_Windows instances only_) If you increase the size of an
   NVMe volume on an instance that does not have the AWS NVMe drivers, you must
   reboot the instance to enable Windows to see the new volume size. For more
   information about installing the AWS NVMe drivers, see [AWS NVMe drivers](../../../AWSEC2/latest/UserGuide/aws-nvme-drivers.md "../../../AWSEC2/latest/UserGuide/aws-nvme-drivers.md").

AWS CLI

###### To modify an EBS volume

Use the [modify-volume](../../../cli/latest/reference/ec2/modify-volume.md "../../../cli/latest/reference/ec2/modify-volume.md")
command. For example, if you have a volume of type `gp2` with a size of
100 GiB, the following example changes its configuration to a volume of type
`io1` with 10,000 IOPS and a size of 200 GiB.

```
aws ec2 modify-volume \
    --volume-id `vol-01234567890abcdef` \
    --volume-type io1 \
    --iops 10000 \
    --size 200
```

The following is example output.

```
{
    "VolumeModification": {
        "TargetSize": 200,
        "TargetVolumeType": "io1",
        "ModificationState": "modifying",
        "VolumeId": "vol-01234567890abcdef",
        "TargetIops": 10000,
        "StartTime": "2022-01-19T22:21:02.959Z",
        "Progress": 0,
        "OriginalVolumeType": "gp2",
        "OriginalIops": 300,
        "OriginalSize": 100
    }
}
```

If you've increased the size of your volume, then you must also extend the
volume's partition to make use of the additional storage capacity. For more
information, see [Extend the file system after resizing an Amazon EBS volume](recognize-expanded-volume-linux.md "recognize-expanded-volume-linux.md").

PowerShell

###### To modify an EBS volume

Use the [Edit-EC2Volume](../../../powershell/latest/reference/items/Edit-EC2Volume.md "../../../powershell/latest/reference/items/Edit-EC2Volume.md") cmdlet. For example, if you have a volume of type
`gp2` with a size of 100 GiB, the following example changes its
configuration to a volume of type `io1` with 10,000 IOPS and a
size of 200 GiB.

```
Edit-EC2Volume `
    -VolumeId `vol-01234567890abcdef` `
    -VolumeType io1 `
    -Iops 10000 `
    -Size 200
```

If you've increased the size of your volume, then you must also extend the
volume's partition to make use of the additional storage capacity. For more
information, see [Extend the file system after resizing an Amazon EBS volume](recognize-expanded-volume-linux.md "recognize-expanded-volume-linux.md").

## Modify an EBS volume if Elastic Volumes is not

supported

If you are using a supported instance type, you can use Elastic Volumes to dynamically
modify the size, performance, and volume type of your Amazon EBS volumes without detaching
them.

If you cannot use Elastic Volumes but you need to modify the root (boot) volume, you
must stop the instance, modify the volume, and then restart the instance.

After the instance has started, you can check the file system size to see if your
instance recognizes the larger volume space. On Linux, use the
**df -h** command to check the file system size.

```
`[ec2-user ~]$` `df -h``Filesystem Size Used Avail Use% Mounted on
/dev/xvda1 7.9G 943M 6.9G 12% /
tmpfs 1.9G 0 1.9G 0% /dev/shm`
```

If the size does not reflect your newly expanded volume, you must extend the file system
of your device so that your instance can use the new space. For more information, see [Extend the file system after resizing an Amazon EBS volume](recognize-expanded-volume-linux.md "recognize-expanded-volume-linux.md").

With Windows instances, you might have to bring the volume online in order to use it.
For more information, see [Make an Amazon EBS volume available for use](ebs-using-volumes.md "ebs-using-volumes.md").
You do not need to reformat the volume.

## Initialize Elastic Volumes support (if needed)

Before you can modify a volume that was attached to an instance before November 3, 2016
23:40 UTC, you must initialize volume modification support using one of the following
actions:

- Detach and attach the volume
- Stop and start the instance

Console

###### To determine whether your instances are ready

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Instances**.
3. Choose the **Show/Hide Columns** icon (the gear). Select the
   **Launch time** attribute column and then choose
   **Confirm**.
4. Sort the list of instances by the **Launch Time** column. For
   each instance that was started before the cutoff date, choose the
   **Storage** tab and check the **Attachment
   time** column to see when its volumes were attached.

AWS CLI

###### To determine whether your instances are ready

Use the following [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command to determine whether the volume was attached
before November 3, 2016 23:40 UTC.

```
aws ec2 describe-instances \
    --query "Reservations[*].Instances[*].[InstanceId,LaunchTime<='2016-11-01',BlockDeviceMappings[*][Ebs.AttachTime<='2016-11-01']]" \
    --output text
```

The first line of the output for each instance shows its ID and whether it was
started before the cutoff date (True or False). The first line is followed by one or
more lines that show whether each EBS volume was attached before the cutoff date (True
or False). In the following example output, you must initialize volume modification
for the first instance because it was started before the cutoff date and its root
volume was attached before the cutoff date. The other instances are ready because they
were started after the cutoff date.

```
i-e905622e              True
True
i-719f99a8              False
True
i-006b02c1b78381e57     False
False
False
i-e3d172ed              False
True
```

PowerShell

###### To determine whether an instance is ready

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet to determine whether a volume was attached before
November 3, 2016 23:40 UTC.

```
(Get-EC2Instance `
    -InstanceId `i-1234567890abcdef0`).Instances.BlockDeviceMappings | `
     Format-Table @{Name="VolumeId";Expression={$_.Ebs.VolumeId}}, `
                  @{Name="AttachTime";Expression={$_.Ebs.AttachTime}}
```

The following is example output.

```
VolumeId              AttachTime
--------              ----------
vol-0b243c8d927752d2b 3/23/2020 12:21:14 AM
vol-043eadbeb4a8387c3 9/5/2020 7:39:22 PM
vol-0c3f0c4e55c082753 4/23/2019 4:07:40 PM
```
