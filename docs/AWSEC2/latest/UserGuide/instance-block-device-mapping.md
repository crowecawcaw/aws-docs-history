# Add block device mappings to Amazon EC2 instance

By default, an instance that you launch includes any storage devices specified in the
block device mapping of the AMI from which you launched the instance. You can specify changes
to the block device mapping for an instance when you launch it, and these updates overwrite or
merge with the block device mapping of the AMI.

###### Limitations

- For the root volume, you can only modify the following: volume size, volume type, and
  the **Delete on Termination** flag.
- When you modify an EBS volume, you can't decrease its size. Therefore, you must
  specify a snapshot whose size is equal to or greater than the size of the snapshot
  specified in the block device mapping of the AMI.

###### Tasks

- [Update the block device mapping when launching an
  instance](#Using_OverridingAMIBDM "#Using_OverridingAMIBDM")
- [Update the block device mapping of a running instance](#update-instance-bdm "#update-instance-bdm")
- [View the EBS volumes in an instance block device mapping](#view-instance-bdm "#view-instance-bdm")
- [View the instance block device mapping for instance store
  volumes](#bdm-instance-metadata "#bdm-instance-metadata")

## Update the block device mapping when launching an

instance

You can add EBS volumes and instance store volumes to an instance when you launch it.
Note that updating the block device mapping for an instance doesn't make a permanent change
to the block device mapping of the AMI from which it was launched.

Console

###### To update the volumes for an instance at launch

1. Follow the procedure to [launch an instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md"),
   but don't launch the instance until you've completed the following
   steps to update the volumes.
2. (Optional) To add a volume, choose **Configure storage**,
   **Add new volume**. Select the volume size and
   volume type.
3. (Optional) To suppress a volume that was specified by the block device
   mapping of the AMI, choose **Configure storage**,
   **Remove**.
4. (Optional) To modify the configuration of an EBS volume, on the
   **Configure storage** pane, choose
   **Advanced**. Expand the information for the volume,
   and make whatever changes you need.
5. In the **Summary** panel, review your instance configuration, and then
   choose **Launch instance**. For more information,
   see [Launch an EC2 instance using the launch
   instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

AWS CLI

###### To update the volumes for an instance at launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command with the `--block-device-mappings` option.

```
--block-device-mappings file://mapping.json
```

For example, suppose that an AMI block device mapping specifies the following:

- `/dev/xvda` - EBS root volume
- `/dev/sdh` - EBS volume created from `snap-1234567890abcdef0`
- `/dev/sdj` - Empty EBS volume with a size of `100`
- `/dev/sdb` - Instance store volume `ephemeral0`

Suppose that the following is the instance block device mapping in
`mapping.json`.

```
[
    {
        "DeviceName": "/dev/xvda",
        "Ebs": {
            "VolumeSize": 100
        }
    },
    {
        "DeviceName": "/dev/sdj",
        "NoDevice": ""
    },
    {
        "DeviceName": "/dev/sdh",
        "Ebs": {
            "VolumeSize": 300
        }
    },
    {
        "DeviceName": "/dev/sdc",
        "VirtualName": "ephemeral1"
    }
]
```

The instance block device mapping does the following:

- Overrides the size of the root volume, `/dev/xvda`, increasing it
  to 100 GiB.
- Prevents `/dev/sdj` from attaching to the instance.
- Overrides the size of `/dev/sdh`, increasing it to 300 GiB.
  Notice that you don't need to specify the snapshot ID again.
- Adds an ephemeral volume, `/dev/sdc`. If the instance type doesn't
  support multiple instance store volumes, this has no effect. If the instance type
  supports NVMe instance store volumes, they are automatically enumerated and
  included in the instance block device mapping and can't be overridden.

PowerShell

###### To update the volumes for an instance at launch

Use the `-BlockDeviceMapping` parameter with the
[New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the `-BlockDeviceMapping` parameter.

```
-BlockDeviceMapping $bdm
```

Suppose that the following is the instance block device mapping
in `$bdm`.

```
$bdm = @()

$root = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping
$root.DeviceName = "/dev/xvda"
$ebs1 = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice
$ebs1.VolumeSize = 100
$root.Ebs = $ebs1
$bdm += $root

$sdj = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping
$sdj.DeviceName = "/dev/sdj"
$sdj.NoDevice = ""
$bdm += $sdj

$sdh = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping
$sdh.DeviceName = "/dev/sdh"
$ebs2 = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice
$ebs2.VolumeSize = 300
$sdh.Ebs = $ebs2
$bdm += $sdh

$sdc = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping
$sdc.DeviceName = "/dev/sdc"
$sdc.VirtualName = "ephemeral1"
$bdm += $sdc
```

The instance block device mapping does the following:

- Overrides the size of the root volume, `/dev/xvda`, increasing it
  to 100 GiB.
- Prevents `/dev/sdj` from attaching to the instance.
- Overrides the size of `/dev/sdh`, increasing it to 300 GiB.
  Notice that you don't need to specify the snapshot ID again.
- Adds an ephemeral volume, `/dev/sdc`. If the instance type doesn't
  support multiple instance store volumes, this has no effect. If the instance type
  supports NVMe instance store volumes, they are automatically enumerated and
  included in the instance block device mapping and can't be overridden.

## Update the block device mapping of a running instance

You do not need to stop the instance before changing this attribute.

AWS CLI

###### To update the block device mapping of a running instance

Use the [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md") command.

Add the `--block-device-mappings` option:

```
--block-device-mappings file://mapping.json
```

In `mapping.json`, specify the updates. For example, the
following update changes the root volume to persist.

```
[
  {
    "DeviceName": "`/dev/sda1`",
    "Ebs": {
      "DeleteOnTermination": false
    }
  }
]
```

PowerShell

###### To update the block device mapping of a running instance

Use the [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md") cmdlet.

Add the `-BlockDeviceMapping` option:

```
-BlockDeviceMapping $bdm
```

In `bdm`, specify the updates. For example, the following update
changes the root volume to persist.

```
$ebd = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice
$ebd.DeleteOnTermination = false
$bdm = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping
$bdm.DeviceName = "`/dev/sda1`"
$bdm.Ebs = $ebd
```

## View the EBS volumes in an instance block device mapping

You can easily enumerate the EBS volumes mapped to an instance.

Console

###### To view the EBS volumes for an instance

1.  Open the Amazon EC2 console.
2.  In the navigation pane, choose **Instances**.
3.  Select the instance and look at the details displayed in the
    **Storage** tab. At a minimum, the following information is
    available for the root volume (where the term **root device** is
    equivalent to **root volume**):

        * **Root device type** (for example, **EBS**)
        * **Root device name** (for example, `/dev/xvda`)
        * **Block devices** (for example, `/dev/xvda`,
         `/dev/sdf`, and `/dev/sdj`)

    If the instance was launched with additional EBS volumes using a block device
    mapping, they appear under **Block devices**. Any instance store volumes
    do not appear on this tab.

4.  To display additional information about an EBS volume, choose its volume ID to go to
    the volume page.

AWS CLI

###### To view the EBS volumes for an instance

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md")
command.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` \
    --query Reservations[*].Instances[0].BlockDeviceMappings
```

PowerShell

###### To view the EBS volumes for an instance

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
cmdlet.

```
(Get-EC2Instance -InstanceId `i-0bac57d7472c89bac`).Instances.BlockDeviceMappings
```

## View the instance block device mapping for instance store

volumes

The instance type determines the number and type of instance store volumes that are available to
the instance. If the number of instance store volumes in a block device mapping exceeds the
number of instance store volumes available to an instance, the additional volumes are
ignored. To view the instance store volumes for your instance, run the **lsblk**
command (Linux instances) or open **Windows Disk Management**
(Windows instances). To learn how many instance store volumes are supported by each instance
type, see [Amazon EC2 instance type specifications](../../../ec2/latest/instancetypes/ec2-instance-type-specifications.md "../../../ec2/latest/instancetypes/ec2-instance-type-specifications.md").

When you view the block device mapping for your instance, you can see only the EBS
volumes, not the instance store volumes. The method you use to view the instance store
volumes for your instance depends on the volume type.

### NVMe instance store volumes

You can use the NVMe command line package, [nvme-cli](https://github.com/linux-nvme/nvme-cli "https://github.com/linux-nvme/nvme-cli"),
to query the NVMe instance store volumes in the block device mapping. Download and install the package on
your instance, and then run the following command.

```
`[ec2-user ~]$` sudo nvme list
```

The following is example output for an instance. The text in the Model column indicates
whether the volume is an EBS volume or an instance store volume. In this example, both
`/dev/nvme1n1` and `/dev/nvme2n1` are instance store
volumes.

```
Node             SN                   Model                                    Namespace
---------------- -------------------- ---------------------------------------- ---------
/dev/nvme0n1     vol06afc3f8715b7a597 Amazon Elastic Block Store               1
/dev/nvme1n1     AWS2C1436F5159EB6614 Amazon EC2 NVMe Instance Storage         1
/dev/nvme2n1     AWSB1F4FF0C0A6C281EA Amazon EC2 NVMe Instance Storage         1         ...
```

You can use Disk Management or PowerShell to list both EBS and instance store
NVMe volumes. For more information, see [Map NVMe disks on Amazon EC2 Windows instance to
volumes](windows-list-disks-nvme.md "windows-list-disks-nvme.md").

### HDD or SSD instance store volumes

You can use instance metadata to query the HDD or SSD instance store volumes in the block device mapping.
NVMe instance store volumes are not included.

The base URI for all requests for instance metadata is
`http://169.254.169.254/latest/`. For more information, see [Use instance metadata to manage your EC2
instance](ec2-instance-metadata.md "ec2-instance-metadata.md").

First, connect to your running instance. From the instance, use this query to get its
block device mapping.

IMDSv2

```
`[ec2-user ~]$` `TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/block-device-mapping/`
```

IMDSv1

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/block-device-mapping/`
```

The response includes the names of the block devices for the instance. For example, the
output for an instance store–backed `m1.small` instance looks like
this.

```
ami
ephemeral0
root
swap
```

The `ami` device is the root volume as seen by the instance. The
instance store volumes are named `ephemeral[0-23]`. The
`swap` device is for the page file. If you've also mapped EBS volumes,
they appear as `ebs1`, `ebs2`, and so on.

To get details about an individual block device in the block device mapping, append its
name to the previous query, as shown here.

IMDSv2

```
`[ec2-user ~]$` `TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/block-device-mapping/ephemeral0`
```

IMDSv1

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/block-device-mapping/ephemeral0`
```

First, connect to your running instance. From the instance, use this query to get its
block device mapping.

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/block-device-mapping/`
```

The response includes the names of the block devices for the instance. For example, the
output for an instance store–backed `m1.small` instance looks like
this.

```
ami
ephemeral0
root
swap
```

The `ami` device is the root volume as seen by the instance. The
instance store volumes are named `ephemeral[0-23]`. The
`swap` device is for the page file. If you've also mapped EBS volumes,
they appear as `ebs1`, `ebs2`, and so on.

To get details about an individual block device in the block device mapping, append its
name to the previous query, as shown here.

```
`PS C:\>` `Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/block-device-mapping/ephemeral0`
```
