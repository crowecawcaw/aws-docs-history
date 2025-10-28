# Map Amazon EBS volumes to NVMe device names

EBS uses single-root I/O virtualization (SR-IOV) to provide volume attachments on
Nitro-based instances using the NVMe specification. These devices rely on standard NVMe
drivers on the operating system. These drivers typically discover attached devices
during instance boot, and create device nodes based on the order in
which the devices respond, not on how the devices are specified in the block device
mapping.

In Linux, NVMe device names follow the pattern `/dev/nvme<x>n<y>`,
where <x> is the enumeration order, and, for EBS, <y> is 1. Occasionally, devices
can respond to discovery in a different order in subsequent instance starts, which causes the
device name to change. Additionally, the device name assigned by the block device driver can be
different from the name specified in the block device mapping.

We recommend that you use stable identifiers for your EBS volumes within
your instance, such as one of the following:

- For Nitro-based instances, the block device mappings that are specified in the
  Amazon EC2 console when you are attaching an EBS volume or during
  `AttachVolume` or `RunInstances` API calls are
  captured in the vendor-specific data field of the NVMe controller
  identification. With Amazon Linux AMIs later than version 2017.09.01, we provide a
  `udev` rule that reads this data and creates a symbolic link to
  the block-device mapping.
- The EBS volume ID and the mount point are stable between instance state
  changes. The NVMe device name can change depending on the order in which the
  devices respond during instance boot. We recommend using the EBS volume ID and
  the mount point for consistent device identification.
- NVMe EBS volumes have the EBS volume ID set as the serial number in the device
  identification. Use the `lsblk -o +SERIAL` command to list the serial
  number.
- The NVMe device name format can vary depending on whether the EBS volume was
  attached during or after the instance launch. NVMe device names for volumes
  attached after instance launch include the `/dev/` prefix, while NVMe
  device names for volumes attached during instance launch do not include the
  `/dev/` prefix.
  - For Amazon Linux or FreeBSD AMI, use the `sudo ebsnvme-id /dev/`nvme0n1` -u`
    command for a consistent NVMe device name.
  - For other distributions, use the `sudo nvme id-ctrl -V /dev/`nvme0n1``command to determine the NVMe device name. You might need to include the`--vendor-specific`
    command option.

- When a device is formatted, a UUID is generated that persists for the life of
  the filesystem. A device label can be specified at the same time. For more
  information, see [Make an Amazon EBS volume available for use](ebs-using-volumes.md "ebs-using-volumes.md")
  and [Boot from the wrong volume](../../../AWSEC2/latest/UserGuide/instance-booting-from-wrong-volume.md "../../../AWSEC2/latest/UserGuide/instance-booting-from-wrong-volume.md").

###### Amazon Linux AMIs

With Amazon Linux AMI 2017.09.01 or later (including Amazon Linux 2), you can run the
**ebsnvme-id** command as follows to map the NVMe device name to
a volume ID and device name:

The following example shows the command and output for a volume attached
during instance launch. Note that the NVMe device name does not include the
`/dev/` prefix.

```
`[ec2-user ~]$` `sudo /sbin/ebsnvme-id /dev/nvme`0`n1``Volume ID: vol-01324f611e2463981
sda`
```

The following example shows the command and output for a volume attached
after instance launch. Note that the NVMe device name includes the `/dev/`
prefix.

```
`[ec2-user ~]$` `sudo /sbin/ebsnvme-id /dev/nvme`1`n1``Volume ID: vol-064784f1011136656
/dev/sdf`
```

Amazon Linux also creates a symbolic link from the device name in the block device
mapping (for example, `/dev/sdf`), to the NVMe device name.

###### FreeBSD AMIs

Starting with FreeBSD 12.2-RELEASE, you can run the **ebsnvme-id**
command as shown above. Pass either the name of the NVMe device (for example,
`nvme0`) or the disk device (for example,
`nvd0` or `nda0`). FreeBSD also creates
symbolic links to the disk devices (for example,
`/dev/aws/disk/ebs/``volume_id`).

###### Other Linux AMIs

With a kernel version of 4.2 or later, you can run the **nvme
id-ctrl** command as follows to map an NVMe device to a volume ID.
First, install the NVMe command line package, `nvme-cli`, using
the package management tools for your Linux distribution. For download and
installation instructions for other distributions, refer to the documentation
specific to your distribution.

The following example gets the volume ID and NVMe device name for a volume
that was attached during instance launch. Note that the NVMe device name does not
include the `/dev/` prefix. The device name is available through the NVMe
controller vendor-specific extension (bytes 384:4095 of the controller
identification):

```
`[ec2-user ~]$` `sudo nvme id-ctrl -V /dev/nvme`0`n1``NVME Identify Controller:
vid : 0x1d0f
ssvid : 0x1d0f
sn : `vol01234567890abcdef`
mn : Amazon Elastic Block Store
...
0000: 2f 64 65 76 2f 73 64 6a 20 20 20 20 20 20 20 20 "`sda`..."`
```

The following example gets the volume ID and NVMe device name for a volume
that was attached after instance launch. Note that the NVMe device name includes the
`/dev/` prefix.

```
`[ec2-user ~]$` `sudo nvme id-ctrl -V /dev/nvme`1`n1``NVME Identify Controller:
vid : 0x1d0f
ssvid : 0x1d0f
sn : `volabcdef01234567890`
mn : Amazon Elastic Block Store
...
0000: 2f 64 65 76 2f 73 64 6a 20 20 20 20 20 20 20 20 "`/dev/sdf`..."`
```

The **lsblk** command lists available devices and their
mount points (if applicable). This helps you determine the correct device name to use.
In this example, `/dev/nvme0n1p1` is mounted as the root device and
`/dev/nvme1n1` is attached but not mounted.

```
`[ec2-user ~]$` `lsblk``NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
nvme1n1 259:3 0 100G 0 disk
nvme0n1 259:0 0 8G 0 disk
 nvme0n1p1 259:1 0 8G 0 part /
 nvme0n1p128 259:2 0 1M 0 part`
```

You can run the `ebsnvme-id` command to map the NVMe device
disk number to an EBS volume ID and device name. By default, all EBS NVMe devices
are enumerated. You can pass a disk number to enumerate information for a specific
device. The `ebsnvme-id` tool is included in the latest AWS provided
Windows Server AMIs located in
`C:\ProgramData\Amazon\Tools`.

Starting with AWS NVMe driver package `1.5.0,` the
latest version of the `ebsnvme-id` tool is installed by the driver
package. The latest version is only available in the driver package. The standalone
download link for the `ebsnvme-id` tool will no longer receive updates.
The last version available through the standalone link is `1.1.0`, which
can be downloaded using the link [ebsnvme-id.zip](https://s3.amazonaws.com/ec2-windows-drivers-downloads/EBSNVMeID/Latest/ebsnvme-id.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/EBSNVMeID/Latest/ebsnvme-id.zip") and extracting the contents to your Amazon EC2 instance to
get access to `ebsnvme-id.exe`.

```
`PS` `C:\ProgramData\Amazon\Tools> ebsnvme-id.exe``Disk Number: 0
Volume ID: vol-0d6d7ee9f6e471a7f
Device Name: sda1

Disk Number: 1
Volume ID: vol-03a26248ff39b57cf
Device Name: xvdd

Disk Number: 2
Volume ID: vol-038bd1c629aa125e6
Device Name: xvde

Disk Number: 3
Volume ID: vol-034f9d29ec0b64c89
Device Name: xvdb

Disk Number: 4
Volume ID: vol-03e2dbe464b66f0a1
Device Name: xvdc`
```

````
`PS` `C:\ProgramData\Amazon\Tools> ebsnvme-id.exe `4```Disk Number: 4
Volume ID: vol-03e2dbe464b66f0a1
Device Name: xvdc`
````
