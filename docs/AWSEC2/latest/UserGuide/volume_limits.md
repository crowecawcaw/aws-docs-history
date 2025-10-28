# Amazon EBS volume limits for Amazon EC2 instances

The maximum number of Amazon EBS volumes that you can attach to an instance depends on
the instance type and instance size. If you exceed the volume attachment limit for
an instance, the attachment request fails with the `AttachmentLimitExceeded`
error.

When considering how many volumes to attach to your instance, you should consider
whether you need increased I/O bandwidth or increased storage capacity.

###### Bandwidth versus capacity

For consistent and predictable bandwidth use cases, use Amazon EBS-optimized
instances with General Purpose SSD volumes or Provisioned IOPS SSD volumes. For maximum performance, match
the IOPS you have provisioned for your volumes with the bandwidth available for
your instance type.

For RAID configurations, you might find that arrays larger than 8 volumes have
diminished performance returns due to increased I/O overhead. Test your individual
application performance and tune it as required.

###### Contents

- [Volume limits for instances built on the Nitro
  System](volume_limits.md#nitro-system-limits "volume_limits.md#nitro-system-limits")
  - [Dedicated EBS volume limit](volume_limits.md#dedicated-limit "volume_limits.md#dedicated-limit")
  - [Shared EBS volume limit](volume_limits.md#shared-limit "volume_limits.md#shared-limit")

- [Volume limits for Xen-based instances](volume_limits.md#xen-limits "volume_limits.md#xen-limits")
  - [Linux instances](volume_limits.md#linux-specific-volume-limits "volume_limits.md#linux-specific-volume-limits")
  - [Windows instances](volume_limits.md#windows-specific-volume-limits "volume_limits.md#windows-specific-volume-limits")

## Volume limits for instances built on the Nitro

System

The volume limits for instances built on the Nitro System depend on the instance
type. Some Nitro instance types have a **dedicated EBS volume
limit**, while most have a **shared volume limit**.
To view the volume attachment limits for each instance type, see the following:

- [Amazon EBS specifications – General purpose](../../../ec2/latest/instancetypes/gp.md#gp_storage-ebs "../../../ec2/latest/instancetypes/gp.md#gp_storage-ebs")
- [Amazon EBS specifications – Compute optimized](../../../ec2/latest/instancetypes/co.md#co_storage-ebs "../../../ec2/latest/instancetypes/co.md#co_storage-ebs")
- [Amazon EBS specifications – Memory optimized](../../../ec2/latest/instancetypes/mo.md#mo_storage-ebs "../../../ec2/latest/instancetypes/mo.md#mo_storage-ebs")
- [Amazon EBS specifications – Storage optimized](../../../ec2/latest/instancetypes/so.md#so_storage-ebs "../../../ec2/latest/instancetypes/so.md#so_storage-ebs")
- [Amazon EBS specifications – Accelerated computing](../../../ec2/latest/instancetypes/ac.md#ac_storage-ebs "../../../ec2/latest/instancetypes/ac.md#ac_storage-ebs")
- [Amazon EBS specifications – High-performance computing](../../../ec2/latest/instancetypes/hpc.md#hpc_storage-ebs "../../../ec2/latest/instancetypes/hpc.md#hpc_storage-ebs")
- [Amazon EBS specifications – Previous generation](../../../ec2/latest/instancetypes/pg.md#pg_storage-ebs "../../../ec2/latest/instancetypes/pg.md#pg_storage-ebs")

### Dedicated EBS volume limit

The following Nitro instance types have a dedicated EBS volume limit that varies
depending on instance size. The limit is not shared with other device attachments. In
other words, you can attach any number of EBS volumes up to the volume attachment
limit, regardless of the number of attached devices, such as NVMe instance store
volumes and network interfaces.

- **General purpose:** M7a | M7i | M7i-flex | M8a | M8g | M8gd | M8i | M8i-flex
- **Compute optimized:** C7a | C7i | C7i-flex | C8g | C8gd | C8gn | C8i | C8i-flex
- **Memory optimized:** R7a | R7i | R7iz | R8g | R8gb | R8gd | R8gn | R8i | R8i-flex | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb | U7inh-32tb | X8g
- **Storage optimized:** I7i | I7ie | I8g | I8ge
- **Accelerated computing:** F2 | G6 | G6e | G6f | Gr6 | Gr6f | P4d | P4de | P5 | P5e | P5en | P6-B200 | P6e-GB200 | Trn2 | Trn2u
- **High performance computing:** Hpc7a

### Shared EBS volume limit

All other Nitro instance types (not listed in [Dedicated EBS volume limit](#dedicated-limit "#dedicated-limit")) have a volume attachment limit that is shared between
Amazon EBS volumes, network interfaces, and NVMe instance store volumes. You can attach any
number of Amazon EBS volumes up to that limit, less the number of attached network interfaces
and NVMe instance store volumes. Keep in mind that every instance must have at least one
network interface, and that NVMe instance store volumes are automatically attached at
launch.

Most Nitro instances support a maximum of 28 attachments. The following examples
demonstrate how to calculate how many EBS volumes you can attach.

###### Examples

- With an `m5.xlarge` instance with only the primary network interface,
  you can attach 27 EBS volumes.

28 volumes - 1 network interface = 27

- With an `m5.xlarge` instance with two additional network interfaces,
  you can attach 25 EBS volumes.

28 volumes - 3 network interfaces = 25

- With an `m5d.xlarge` instance with two additional network interfaces,
  you can attach 24 EBS volumes.

28 volumes - 3 network interfaces - 1 NVMe instance store volume = 24

## Volume limits for Xen-based instances

The volume limits for Xen-based instances, such as T2, depend on the
operating system.

For more information, see [Xen-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type").

### Linux instances

Attaching more than 40 volumes to a Xen-based Linux instance can cause boot failures. This
number includes the root volume, plus any attached instance store volumes and Amazon EBS volumes.

If you experience boot problems on an instance with a large number of volumes, stop the
instance, detach any volumes that are not essential to the boot process, start the instance,
and then reattach the volumes after the instance is running.

###### Important

Attaching more than 40 volumes to a Xen-based Linux instance is supported on a best effort
basis only and is not guaranteed.

### Windows instances

The following table shows the volume limits for Xen-based Windows instances based on the
driver used. That these numbers include the root volume, plus any attached instance store volumes
and Amazon EBS volumes.

| Driver     | Volume Limit |
| ---------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS PV     | 26           |
| Citrix PV  | 26           |
| Red Hat PV | 17           | We recommend that you do not that attach more than 26 volumes to a Xen-based Windows instance with AWS PV or Citrix PV drivers, as it is likely to cause performance issues. To determine which PV drivers your instance is using, or to upgrade your Windows instance from Red Hat to Citrix PV drivers, see [Upgrade PV drivers on EC2 Windows instances](Upgrading_PV_drivers.md "Upgrading_PV_drivers.md"). ###### Important Attaching more than the following number of volumes to a Xen-based Windows instance is supported on a best effort basis only and is not guaranteed. For more information about how device names are related to volumes, see [How volumes are attached and mapped for Amazon EC2 Windows instances](ec2-windows-volumes.md "ec2-windows-volumes.md"). |
