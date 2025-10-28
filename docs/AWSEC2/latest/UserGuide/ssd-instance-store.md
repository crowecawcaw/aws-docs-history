# SSD instance store volumes for EC2 instances

Like other instance store volumes, you must map the SSD instance store volumes for your
instance when you launch it. The data on an SSD instance volume persists only for the life of
its associated instance. For more information, see [Add instance store volumes to an EC2 instance](add-instance-store-volumes.md "add-instance-store-volumes.md").

## NVMe SSD volumes

Some instances offer non-volatile memory express (NVMe) solid state drives (SSD)
instance store volumes. For more information about the type of instance store volume
supported by each instance type, see [Instance store volume limits for EC2 instances](instance-store-volumes.md "instance-store-volumes.md").

The data on NVMe instance storage is encrypted using an XTS-AES-256 block cipher
implemented in a hardware module on the instance. The encryption keys are generated using
the hardware module and are unique to each NVMe instance storage device. All encryption
keys are destroyed when the instance is stopped or terminated and cannot be recovered.
You cannot disable this encryption and you cannot provide your own encryption key.

To access NVMe volumes, the NVMe drivers must be installed. The following AMIs meet this requirement:

- AL2023
- Amazon Linux 2
- Amazon Linux AMI 2018.03 and later
- Ubuntu 14.04 or later with `linux-aws` kernel

###### Note

AWS Graviton-based instance types require Ubuntu 18.04 or later with `linux-aws` kernel

- Red Hat Enterprise Linux 7.4 or later
- SUSE Linux Enterprise Server 12 SP2 or later
- CentOS 7.4.1708 or later
- FreeBSD 11.1 or later
- Debian GNU/Linux 9 or later

- Bottlerocket
  After you connect to your instance, you can list the NVMe devices using the
  **lspci** command. The following is example output for an
  `i3.8xlarge` instance, which supports four NVMe devices.

```
`[ec2-user ~]$` `lspci``00:00.0 Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma] (rev 02)
00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II]
00:01.1 IDE interface: Intel Corporation 82371SB PIIX3 IDE [Natoma/Triton II]
00:01.3 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 01)
00:02.0 VGA compatible controller: Cirrus Logic GD 5446
00:03.0 Ethernet controller: Device 1d0f:ec20
00:17.0 Non-Volatile memory controller: Device 1d0f:cd01
00:18.0 Non-Volatile memory controller: Device 1d0f:cd01
00:19.0 Non-Volatile memory controller: Device 1d0f:cd01
00:1a.0 Non-Volatile memory controller: Device 1d0f:cd01
00:1f.0 Unassigned class [ff80]: XenSource, Inc. Xen Platform Device (rev 01)`
```

If you are using a supported operating system but you do not see the NVMe
devices, verify that the NVMe module is loaded using the following command.

- Amazon Linux, Amazon Linux 2, Ubuntu 14/16, Red Hat Enterprise Linux, SUSE Linux Enterprise Server, CentOS 7

```
`$` `lsmod | grep nvme``nvme 48813 0`
```

- Ubuntu 18

```
`$` `cat /lib/modules/$(uname -r)/modules.builtin | grep nvme``s/nvme/host/nvme-core.ko
kernel/drivers/nvme/host/nvme.ko
kernel/drivers/nvmem/nvmem_core.ko`
```

The NVMe volumes are compliant with the NVMe 1.0e specification. You can use
the NVMe commands with your NVMe volumes. With Amazon Linux, you can install the
`nvme-cli` package from the repo using the **yum
install** command. With other supported versions of Linux, you can download the
`nvme-cli` package if it's not available in the image.

The latest AWS Windows AMIs for the following operating systems contain the AWS
NVMe drivers used to interact with SSD instance store volumes that are exposed as NVMe block
devices for better performance:

- Windows Server 2025
- Windows Server 2022
- Windows Server 2019
- Windows Server 2016
- Windows Server 2012 R2
  After you connect to your instance, you can verify that you see the NVMe volumes in Disk
  Manager. On the taskbar, open the context (right-click) menu for the Windows logo and choose
  **Disk Management**.

The AWS Windows AMIs provided by Amazon include the AWS NVMe driver. If you are not
using the latest AWS Windows AMIs, you can [install the
current AWS NVMe driver](aws-nvme-drivers.md "aws-nvme-drivers.md").

## Non-NVMe SSD volumes

The following instances support instance store volumes that use non-NVMe SSDs to deliver high random I/O
performance: C3, I2, M3, R3, and X1. For more information about the instance store volumes supported by each
instance type, see [Instance store volume limits for EC2 instances](instance-store-volumes.md "instance-store-volumes.md").

## SSD-based instance store volume I/O performance

As you fill the SSD-based instance store volumes for your instance, the number of write IOPS
that you can achieve decreases. This is due to the extra work the SSD controller must do to
find available space, rewrite existing data, and erase unused space so that it can be
rewritten. This process of garbage collection results in internal write amplification to
the SSD, expressed as the ratio of SSD write operations to user write operations. This
decrease in performance is even larger if the write operations are not in multiples of
4,096 bytes or not aligned to a 4,096-byte boundary. If you write a smaller amount of bytes
or bytes that are not aligned, the SSD controller must read the surrounding data and store
the result in a new location. This pattern results in significantly increased write
amplification, increased latency, and dramatically reduced I/O performance.

SSD controllers can use several strategies to reduce the impact of write amplification.
One such strategy is to reserve space in the SSD instance storage so that the controller
can more efficiently manage the space available for write operations. This is called
_over-provisioning_. The SSD-based instance store volumes provided to
an instance do not have any space reserved for over-provisioning. To reduce write
amplification, we recommend that you leave 10 percent of the volume unpartitioned so that the SSD
controller can use it for over-provisioning. This decreases the storage that you can use,
but increases performance even if the disk is close to full capacity.

For instance store volumes that support TRIM, you can use the TRIM command to notify
the SSD controller whenever you no longer need data that you have written. This provides the
controller with more free space, which can reduce write amplification and increase performance.
For more information, see [Instance store volume TRIM support](#InstanceStoreTrimSupport "#InstanceStoreTrimSupport").

## Instance store volume TRIM support

Some instance types support SSD volumes with TRIM. For more information, see
[Instance store volume limits for EC2 instances](instance-store-volumes.md "instance-store-volumes.md").

###### Note

(Windows instances only) Instances running Windows Server 2012 R2 support TRIM as
of AWS PV Driver version 7.3.0. Instances running earlier versions of Windows Server
do not support TRIM.

Instance store volumes that support TRIM are fully trimmed before they are allocated to
your instance. These volumes are not formatted with a file system when an instance launches,
so you must format them before they can be mounted and used. For faster access to these
volumes, you should skip the TRIM operation when you format them.

(Windows instances) To temporarily disable TRIM support during initial formatting, use
the `fsutil behavior set DisableDeleteNotify 1` command. After formatting is
complete, re-enable TRIM support by using `fsutil behavior set DisableDeleteNotify
 0`.

With instance store volumes that support TRIM, you can use the TRIM command to notify
the SSD controller when you no longer need data that you've written. This provides the
controller with more free space, which can reduce write amplification and increase
performance. On **Linux instances**, use the `fstrim`
command to enable
periodic TRIM. On **Windows instances**, use the `fsutil 
 behavior set DisableDeleteNotify 0` command to ensure TRIM support is enabled
during normal operation.
