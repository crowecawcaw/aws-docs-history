

# Amazon EBS volume constraints
<a name="volume_constraints"></a>

The size of an Amazon EBS volume is constrained by the physics and arithmetic of block data storage, as well as by the implementation decisions of operating system (OS) and file system designers. AWS imposes additional limits on volume size to safeguard the reliability of its services.

The following sections describe the most important factors that limit the usable size of an EBS volume and offer recommendations for configuring your EBS volumes.

**Topics**
+ [Storage capacity](#ebs-storage-capacity)
+ [Service limitations](#aws_limits)
+ [Partitioning schemes](#partitioning)
+ [Data block sizes](#block_size)

## Storage capacity
<a name="ebs-storage-capacity"></a>

The following table summarizes the theoretical and implemented storage capacities for the most commonly used file systems on Amazon EBS, assuming a 4,096 byte block size.


| Partitioning scheme | Max addressable blocks  | Theoretical max size (blocks × block size) | Ext4 implemented max size\* | XFS implemented max size\*\* | NTFS implemented max size | Max supported by EBS | 
| --- | --- | --- | --- | --- | --- | --- | 
| MBR | 232 | 2 TiB | 2 TiB | 2 TiB | 2 TiB | 2 TiB | 
| GPT | 264 | 64 ZiB | 1 EiB =10242 TiB <br />(50 TiB certified on RHEL7) | 500 TiB<br />(certified on RHEL7) | 256 TiB | 64 TiB † | 

\* [Ext4 Howto](https://archive.kernel.org/oldwiki/ext4.wiki.kernel.org/index.php/Ext4_Howto.html) and [What are the file and system size limits for Red Hat Enterprise Linux?](https://access.redhat.com/solutions/1532)

\*\* [What are the file and system size limits for Red Hat Enterprise Linux?](https://access.redhat.com/solutions/1532)

† `io2` Block Express volumes support up to 64 TiB for GPT partitions. For more information, see [Provisioned IOPS SSD (`io2`) Block Express volumes](provisioned-iops.md#io2-block-express).

## Service limitations
<a name="aws_limits"></a>

Amazon EBS abstracts the massively distributed storage of a data center into virtual hard disk drives. To an operating system installed on an EC2 instance, an attached EBS volume appears to be a physical hard disk drive containing 512-byte disk sectors. The OS manages the allocation of data blocks (or clusters) onto those virtual sectors through its storage management utilities. The allocation is in conformity with a volume partitioning scheme, such as master boot record (MBR) or GUID partition table (GPT), and within the capabilities of the installed file system (ext4, NTFS, and so on). 

EBS is not aware of the data contained in its virtual disk sectors; it only ensures the integrity of the sectors. This means that AWS actions and OS actions are independent of each other. When you are selecting a volume size, be aware of the capabilities and limits of both, as in the following cases: 
+ EBS currently supports a maximum volume size of 64 TiB. This means that you can create an EBS volume as large as 64 TiB, but whether the OS recognizes all of that capacity depends on its own design characteristics and on how the volume is partitioned.
+ Boot volumes must use either the MBR or GPT partitioning scheme. The AMI you launch an instance from determines the boot mode and subsequently the partition scheme used for the boot volume.

  With **MBR**, boot volumes are limited to 2 TiB in size.

  With **GPT**, boot volumes can be up to 64 TiB in size when used with GRUB2 (Linux) or UEFI boot mode (Windows).

  For more information, see [Make an Amazon EBS volume available for use](ebs-using-volumes.md).
+ Non-boot volumes that are 2 TiB (2048 GiB) or larger must use a GPT partition table to access the entire volume. 

## Partitioning schemes
<a name="partitioning"></a>

Among other impacts, the partitioning scheme determines how many logical data blocks can be uniquely addressed in a single volume. For more information, see [Data block sizes](#block_size). The common partitioning schemes in use are *Master Boot Record* (MBR) and *GUID partition table* (GPT). The important differences between these schemes can be summarized as follows.

### MBR
<a name="mbr-partitioning"></a>

MBR uses a 32-bit data structure to store block addresses. This means that each data block is mapped with one of 232 possible integers. The maximum addressable size of a volume is given by the following formula:

```
232 × Block size
```

The block size for MBR volumes is conventionally limited to 512 bytes. Therefore:

```
232 × 512 bytes = 2 TiB
```

Engineering workarounds to increase this 2-TiB limit for MBR volumes have not met with widespread industry adoption. Consequently, Linux and Windows never detect an MBR volume as being larger than 2 TiB even if AWS shows its size to be larger. 

### GPT
<a name="gpt-partitioning"></a>

GPT uses a 64-bit data structure to store block addresses. This means that each data block is mapped with one of 264 possible integers. The maximum addressable size of a volume is given by the following formula:

```
264 × Block size
```

The block size for GPT volumes is commonly 4,096 bytes. Therefore:

```
264 × 4,096 bytes
   = 264 × 212 bytes
   = 270 × 26 bytes
   = 64 ZiB
```

Real-world computer systems don't support anything close to this theoretical maximum. Implemented file-system size is currently limited to 50 TiB for ext4 and 256 TiB for NTFS.

## Data block sizes
<a name="block_size"></a>

Data storage on a modern hard drive is managed through *logical block addressing*, an abstraction layer that allows the operating system to read and write data in logical blocks without knowing much about the underlying hardware. The operating system relies on the storage device to map the blocks to its physical sectors, and reads and writes data to disk using data blocks that are a multiple of the sector size.

Amazon EBS advertises either 512-byte or 4,096-byte (4 KiB) physical sectors to the operating system, depending on the following factors:

1. The Amazon EC2 instance type

1. The operating system

1. The NVMe driver version

Amazon EBS advertises 4-KiB physical sectors only if all factors support it. If any one of these do not support 4-KiB physical sectors, Amazon EBS advertises 512-byte physical sectors.

**Amazon EC2 instance type support**  
The following table shows the sector sizes that Amazon EBS advertises for the different Amazon EC2 instance types.


<table>
<thead>
  <tr><th>Instance type</th><th>Linux</th><th>Windows</th></tr>
</thead>
<tbody>
  <tr><td>All Xen-based instance types</td><td colspan="2">Amazon EBS always advertises 512-byte physical sectors</td></tr>
  <tr><td>A1 | C5 | C5a | C5ad | C5d | C5n | C6g | C6gd | DL1 | D3 | D3en | G4ad | G4dn | G5 | G5g | I3 | I3en | Inf1 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6g | M6gd | P3dn | P4d | P4de | R5 | R5a | R5ad | R5d | R5dn | R5n | R6g | R6gd | T3 | T3a | T4g | U-12tb1 | U-18tb1 | U-24tb1 | U-3tb1 | U-6tb1 | U-9tb1 | X2gd | X2iezn | VT1 | Z1d</td><td>Amazon EBS always advertises 512-byte physical sectors</td><td>Amazon EBS advertises 512-byte or 4-KiB physical sectors 1</td></tr>
  <tr><td>All other Nitro-based instances</td><td colspan="2">Amazon EBS advertises 512-byte or 4-KiB physical sectors 1</td></tr>
</tbody>
</table>


1 Depends on the operating system support. See the following section.

**Operating system support**  
The following table provides example operating systems and the corresponding physical sector sizes advertised by Amazon EBS. This is **not an exhaustive list**. We recommend that you verify the physical sector size advertised by Amazon EBS in your operating system.




| Operating system | Advertised physical sector size | 
| --- | --- | 
|  +  Amazon Linux with kernel version 4.14 and earlier <br />+  RHEL 7.9 and earlier <br />+  Ubuntu 20.04 and earlier <br />+  Windows 7/Windows Server 2008 and earlier   | 512 byte | 
|  +  Amazon Linux with kernel version 5.3 and later <br />+  RHEL8.8 and later <br />+  Ubuntu 22.04 and later <br />+  Windows 8/Windows Server 2012 and later 1   | 4 KiB | 

1 For Windows workloads, make sure that you are using the latest version of the [AWS NVMe drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/aws-nvme-drivers.html). Amazon EBS advertises 4-KiB physical sectors with AWS NVMe driver version 1.4.1 and later.

### Non-default block sizes
<a name="block-size-additional"></a>

The industry default size for logical data blocks is currently 4 KiB. Because certain workloads benefit from a smaller or larger block size, file systems support non-default block sizes that can be specified during formatting. Scenarios in which non-default block sizes should be used (such as optimizations) are outside the scope of this topic, but the choice of block size has consequences for the storage capacity of the volume. The following table shows theoretical storage capacity as a function of block size. However, note that the EBS-imposed limit on volume size (64 TiB for io2 Block Express) is currently equal to the maximum size enabled by 16-KiB data blocks.


| Block size | Max volume size | 
| --- | --- | 
| 4 KiB (default) | 16 TiB | 
| 8 KiB | 32 TiB | 
| 16 KiB | 64 TiB | 
| 32 KiB | 128 TiB | 
| 64 KiB (maximum) | 256 TiB | 