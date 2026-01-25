# Block device mappings for volumes on Amazon EC2 instances

Each instance that you launch has an associated root volume, which is either an Amazon EBS volume
or an instance store volume. You can use block device mappings to specify additional EBS volumes
or instance store volumes to attach to an instance when it's launched. You can also attach
additional EBS volumes to a running instance. However, the only way to attach instance store
volumes to an instance is to use block device mappings to attach the volumes as the instance is
launched.

###### Contents

- [Block device mapping concepts](#block-device-mapping-def "#block-device-mapping-def")
- [Add block device mappings to an AMI](ami-block-device-mapping.md "ami-block-device-mapping.md")
- [Add block device mappings to Amazon EC2 instance](instance-block-device-mapping.md "instance-block-device-mapping.md")

## Block device mapping concepts

A _block device_ is a storage device that moves data in sequences of
bytes or bits (blocks). These devices support random access and generally use buffered I/O.
Examples include hard disks, CD-ROM drives, and flash drives. A block device can be physically
attached to a computer or accessed remotely as if it were physically attached to the
computer.

Amazon EC2 supports two types of block devices:

- Instance store volumes (virtual devices whose underlying hardware is physically
  attached to the host computer for the instance)
- EBS volumes (remote storage devices)

A _block device mapping_ defines the block devices (instance store
volumes and EBS volumes) to attach to an instance. You can specify a block device mapping as
part of creating an AMI so that the mapping is used by all instances launched from the AMI.
Alternatively, you can specify a block device mapping when you launch an instance, so this
mapping overrides the one specified in the AMI from which you launched the instance. Note that
all NVMe instance store volumes supported by an instance type are automatically enumerated
and assigned a device name on instance launch; including them in your block device mapping
has no effect.

###### Contents

- [Block device mapping entries](#parts-of-a-block-device-mapping "#parts-of-a-block-device-mapping")
- [Block device mapping instance store caveats](#instance_store_caveats "#instance_store_caveats")
- [Example block device mapping](#block-device-mapping-ex "#block-device-mapping-ex")
- [How devices are made available in the operating system](#bdm-to-os "#bdm-to-os")

### Block device mapping entries

When you create a block device mapping, you specify the following information for each
block device that you need to attach to the instance:

- The device name used within Amazon EC2. The block device driver for the instance assigns
  the actual volume name when mounting the volume. The name assigned can be different
  from the name that Amazon EC2 recommends. For more information, see [Device names for volumes on Amazon EC2 instances](device_naming.md "device_naming.md").

For Instance store volumes, you also specify the following information:

- The virtual device: `ephemeral[0-23]`.
  Note that the number and size of available instance store volumes for your instance
  varies by instance type.

For NVMe instance store volumes, the following information also applies:

- These volumes are automatically enumerated and assigned
  a device name; including them in your block device mapping has no effect.

For EBS volumes, you also specify the following information:

- The ID of the snapshot to use to create the block device
  (snap-_xxxxxxxx_). This value is optional as long as you specify a
  volume size. You can't specify the ID of an archived snapshot.
- The size of the volume, in GiB. The specified size must be greater
  than or equal to the size of the specified snapshot.
- Whether to delete the volume on instance termination (`true` or
  `false`). The default value is `true` for the root volume and
  `false` for attached volumes. When you create an AMI, its block device
  mapping inherits this setting from the instance. When you launch an instance, it
  inherits this setting from the AMI.
- The volume type, which can be `gp2` and `gp3` for General Purpose SSD, `io1` and `io2` for Provisioned IOPS SSD,
  `st1` for Throughput Optimized HDD, `sc1` for Cold HDD, or `standard` for Magnetic.
- The number of input/output operations per second (IOPS) that the
  volume supports. (Used only with `io1` and `io2` volumes.)
- Some instance types support more than one EBS card. You can select the EBS card for
  the volume to be attached to by specifying the EBS card index. For more information,
  see [EBS cards](ebs_cards.md#ebs_cards.title "ebs_cards.md#ebs_cards.title").

### Block device mapping instance store caveats

There are several caveats to consider when launching instances with AMIs that have
instance store volumes in their block device mappings.

- Some instance types include more instance store volumes than others, and some
  instance types contain no instance store volumes at all. If your instance type
  supports one instance store volume, and your AMI has mappings for two instance store
  volumes, then the instance launches with one instance store volume.
- Instance store volumes can only be mapped at launch time. You cannot stop an
  instance without instance store volumes (such as the `t2.micro`), change
  the instance to a type that supports instance store volumes, and then restart the
  instance with instance store volumes. However, you can create an AMI from the
  instance and launch it on an instance type that supports instance store volumes, and
  map those instance store volumes to the instance.
- If you launch an instance with instance store volumes mapped, and then stop the
  instance and change it to an instance type with fewer instance store volumes and
  restart it, the instance store volume mappings from the initial launch still show up
  in the instance metadata. However, only the maximum number of supported instance store
  volumes for that instance type are available to the instance.

###### Note

When an instance is stopped, all data on the instance store volumes is
lost.

- Depending on instance store capacity at launch time, M3 instances may ignore AMI
  instance store block device mappings at launch unless they are specified at launch.
  You should specify instance store block device mappings at launch time, even if the
  AMI you are launching has the instance store volumes mapped in the AMI, to ensure
  that the instance store volumes are available when the instance launches.

### Example block device mapping

This figure shows an example block device mapping for an EBS-backed instance. It maps
`/dev/sdb` to `ephemeral0` and maps two EBS volumes,
one to `/dev/sdh` and the other to `/dev/sdj`. It also
shows the EBS volume that is the root volume, `/dev/sda1`.

![Relationship between instance, instance store volumes, and EBS volumes.](images/block_device_mapping_figure.png)

Note that this example block device mapping is used in the example commands and APIs in
this topic. You can find example commands and APIs that create block device mappings in
[Specify a block device mapping for an AMI](ami-block-device-mapping.md#create-ami-bdm "ami-block-device-mapping.md#create-ami-bdm") and [Update the block device mapping when launching an
instance](instance-block-device-mapping.md#Using_OverridingAMIBDM "instance-block-device-mapping.md#Using_OverridingAMIBDM").

### How devices are made available in the operating system

Device names like `/dev/sdh` and `xvdh` are used
by Amazon EC2 to describe block devices. The block device mapping is used by Amazon EC2 to specify the
block devices to attach to an EC2 instance. After a block device is attached to an instance,
it must be mounted by the operating system before you can access the storage device. When a
block device is detached from an instance, it is unmounted by the operating system and you
can no longer access the storage device.

Linux instances – The device names specified in the block device mapping
are mapped to their corresponding block devices when the instance first boots. The instance
type determines which instance store volumes are formatted and mounted by default. You can
mount additional instance store volumes at launch, as long as you don't exceed the number of
instance store volumes available for your instance type. For more information, see
[Instance store temporary block storage for EC2 instances](InstanceStorage.md "InstanceStorage.md"). The block device driver for
the instance determines which devices are used when the volumes are formatted and mounted.

Windows instances – The device names specified in
the block device mapping are mapped to their corresponding block devices when the instance
first boots, and then the Ec2Config service initializes and mounts the drives. The root
volume is mounted as `C:\`. The instance store volumes are mounted as
`Z:\`, `Y:\`, and so on. When an EBS volume is
mounted, it can be mounted using any available drive letter. However, you can configure how
drive letters are assigned to EBS volumes; for more information, see [Windows launch agents on Amazon EC2 Windows instances](configure-launch-agents.md "configure-launch-agents.md").
