# Compatibility for changing the instance type

You can change the instance type only if the instance's current configuration is
compatible with the instance type that you want. If the instance type that you want is not
compatible with the instance's current configuration, you must launch a new instance with a
configuration that is compatible with the instance type, and then migrate your application
to the new instance.

Compatibility is determined through the following:

**Virtualization type**

Linux AMIs use one of two types of virtualization: paravirtual (PV) or hardware
virtual machine (HVM). If an instance was launched from a PV AMI, you can't change to an
instance type that is HVM only. For more information, see [Virtualization types](ComponentsAMIs.md#virtualization_types "ComponentsAMIs.md#virtualization_types"). To check the
virtualization type of your instance, check the **Virtualization**
value on the details pane of the **Instances** screen in the Amazon EC2
console.

**Architecture**

AMIs are specific to the architecture of the processor, so you must select an
instance type with the same processor architecture as the current instance type. For
example:

- If the current instance type has a processor based on the Arm architecture, you
  are limited to the instance types that support a processor based on the Arm
  architecture, such as C6g and M6g.
- The following instance types are the only instance types that support 32-bit
  AMIs: `t2.nano`, `t2.micro`, `t2.small`,
  `t2.medium`, `c3.large`, `t1.micro`,
  `m1.small`, `m1.medium`, and `c1.medium`. If you
  are changing the instance type of a 32-bit instance, you are limited to these
  instance types.

**Network adapters**

If you switch from a driver for one network adapter to another, the network adapter
settings are reset when the operating system creates the new adapter. To reconfigure the
settings, you might need access to a local account with administrator permissions. The
following are examples of moving from one network adapter to another:

- AWS PV (T2 instances) to Intel 82599 VF (M4 instances)
- Intel 82599 VF (most M4 instances) to ENA (M5 instances)
- ENA (M5 instances) to high-bandwidth ENA (M5n instances)

**Enhanced networking**

Instance types that support [enhanced
networking](enhanced-networking.md "enhanced-networking.md") require the necessary drivers installed. For example,
[Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type") require EBS-backed
AMIs with the Elastic Network Adapter (ENA) drivers installed. To change from an
instance type that does not support enhanced networking to an instance type that
supports enhanced networking, you must install the [ENA drivers](enhanced-networking-ena.md "enhanced-networking-ena.md") or [ixgbevf drivers](sriov-networking.md "sriov-networking.md") on the instance, as
appropriate.

###### Note

When you resize an instance with ENA Express enabled, the new instance
type must also support ENA Express. For a list of instance types that support
ENA Express, see [Supported instance types for ENA
Express](ena-express.md#ena-express-supported-instance-types "ena-express.md#ena-express-supported-instance-types").

To change from an instance type that supports ENA Express to an instance type
that does not support it, ensure that ENA Express is not currently enabled before
you resize the instance.

**NVMe**

EBS volumes are exposed as NVMe block devices on [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type").
If you change from an instance type
that does not support NVMe to an instance type that supports NVMe, you must first
install the NVMe drivers on your instance. Also,
the device names for devices that you specify in the block device mapping are renamed
using NVMe device names (`/dev/nvme[0-26]n1`).

[Linux instances] Therefore, to mount file systems at boot time using `/etc/fstab`,
you must use UUID/Label instead of device names.

**Volume limit**

The maximum number of Amazon EBS volumes that you can attach to an instance depends on the
instance type and instance size. For more information, see [Amazon EBS volume limits for Amazon EC2 instances](volume_limits.md "volume_limits.md").

You can only change to an instance type or instance size that supports the same number
or a larger number of volumes than is currently attached to the instance. If you change to
an instance type or instance size that does not support the number of currently attached
volumes, the request fails. For example, if you change from an `m7i.4xlarge`
instance with 32 attached volumes to an `m6i.4xlarge`, which supports a maximum
of 27 volumes, the request fails.

**NitroTPM**

If you launched the instance using an AMI with [NitroTPM](nitrotpm.md "nitrotpm.md")
enabled and an instance type that supports NitroTPM, the instance launches with NitroTPM
enabled. You can only change to an instance type that also supports NitroTPM.
