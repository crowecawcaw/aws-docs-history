

# Amazon EBS volume types
<a name="ebs-volume-types"></a>

Amazon EBS provides the following volume types, which differ in performance characteristics and price, so that you can tailor your storage performance and cost to the needs of your applications. 

**Important**  
There are several factors that can affect the performance of EBS volumes, such as instance configuration, I/O characteristics, and workload demand. To fully use the IOPS provisioned on an EBS volume, use [EBS–optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html). For more information about getting the most out of your EBS volumes, see [Amazon EBS volume performance](ebs-performance.md).

For more information about pricing, see [Amazon EBS Pricing](https://aws.amazon.com/ebs/pricing/).

**Volume types**
+ [Solid state drive (SSD) volumes](#vol-type-ssd)
+ [Hard disk drive (HDD) volumes](#vol-type-hdd)
+ [Previous generation volumes](#vol-type-prev)

## Solid state drive (SSD) volumes
<a name="vol-type-ssd"></a>

SSD-backed volumes are optimized for transactional workloads involving frequent read/write operations with small I/O size, where the dominant performance attribute is IOPS. SSD-backed volume types include **General Purpose SSD** and **Provisioned IOPS SSD **. The following is a summary of the use cases and characteristics of SSD-backed volumes.


<table>
<thead>
  <tr><th></th><th colspan="2"><a href="general-purpose.md">Amazon EBS General Purpose SSD volumes</a></th><th colspan="2"><a href="provisioned-iops.md">Amazon EBS Provisioned IOPS SSD volumes</a></th></tr>
</thead>
<tbody>
  <tr><td><b>Volume type</b></td><td><code>gp3</code> 6</td><td><code>gp2</code></td><td><code>io2</code> Block Express</td><td><code>io1</code></td></tr>
  <tr><td><b>Durability</b></td><td colspan="2">99.8% - 99.9% durability (0.1% - 0.2% annual failure rate)</td><td>99.999% durability (0.001% annual failure rate)</td><td>99.8% - 99.9% durability (0.1% - 0.2% annual failure rate)</td></tr>
  <tr><td><b>Use cases</b></td><td colspan="2"> <ul><li>Transactional workloads</li><li>Virtual desktops</li><li>Medium-sized, single-instance databases</li><li>Low-latency interactive applications</li><li>Boot volumes</li><li>Development and test environments</li></ul> </td><td>Workloads that require:<ul><li> Consistent sub-millisecond latency with average latency under 500 microseconds 5 </li><li> Sustained IOPS performance </li><li> More than 80,000 IOPS or 2,000 MiB/s of throughput </li></ul></td><td> <ul><li> Workloads that require sustained IOPS performance or more than 16,000 IOPS </li><li> I/O-intensive database workloads </li></ul> </td></tr>
  <tr><td><b>Volume size</b></td><td>1 GiB - 64 TiB </td><td>1 GiB - 16 TiB </td><td>4 GiB - 64 TiB </td><td>4 GiB - 16 TiB </td></tr>
  <tr><td><b>Max IOPS</b></td><td>80,000 3 (25.6 KiB I/O 4)</td><td>16,000 (16 KiB I/O 4)</td><td>256,000 3 (16 KiB I/O 4) </td><td>64,000 (16 KiB I/O 4)</td></tr>
  <tr><td><b>Max throughput</b></td><td>2,000 MiB/s</td><td>250 MiB/s 1</td><td>4,000 MiB/s</td><td>1,000 MiB/s 2</td></tr>
  <tr><td><b>Amazon EBS Multi-attach</b></td><td colspan="2">Not supported</td><td colspan="2">Supported</td></tr>
  <tr><td><b>NVMe reservations</b></td><td colspan="2">Not supported</td><td>Supported</td><td>Not supported</td></tr>
  <tr><td><b>Boot volume</b></td><td colspan="4">Supported</td></tr>
</tbody>
</table>


1 The throughput limit is between 128 MiB/s and 250 MiB/s, depending on the volume size. For more information, see [`gp2` volume performance](general-purpose.md#gp2-performance). Volumes created before **December 3, 2018** that have not been modified since creation might not reach full performance unless you [modify the volume](ebs-modify-volume.md).

2 To achieve maximum throughput of 1,000 MiB/s, the volume must be provisioned with 64,000 IOPS and it must be attached to a [ Nitro-based instance](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html). Volumes created before **December 6, 2017** that have not been modified since creation might not reach full performance unless you [modify the volume](ebs-modify-volume.md).

3 [ Nitro-based instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) support volumes provisioned with up to 256,000 IOPS. Other instance types can be attached to volumes provisioned with up to 64,000 IOPS, but can achieve up to 32,000 IOPS.

4 Represents the required I/O size to reach maximum IOPS within the volume's throughput limit.

5 `io2` Block Express volumes are designed to deliver an average latency of under 500 microseconds for 16KiB I/O operations.

6 On Outposts, gp3 volumes support sizes up to 16 TiB, IOPS up to 16,000, and throughput up to 1,000 MiB/s.

For more information about the SSD-backed volume types, see the following:
+ [Amazon EBS General Purpose SSD volumes](general-purpose.md)
+ [Amazon EBS Provisioned IOPS SSD volumes](provisioned-iops.md)

## Hard disk drive (HDD) volumes
<a name="vol-type-hdd"></a>

HDD-backed volumes are optimized for large streaming workloads where the dominant performance attribute is throughput. HDD volume types include ** Throughput Optimized HDD** and **Cold HDD**. The following is a summary of the use cases and characteristics of HDD-backed volumes.


<table>
<thead>
  <tr><th></th><th><a href="hdd-vols.md#EBSVolumeTypes_st1">Throughput Optimized HDD volumes</a></th><th><a href="hdd-vols.md#EBSVolumeTypes_sc1">Cold HDD volumes</a></th></tr>
</thead>
<tbody>
  <tr><td><b>Volume type</b></td><td><code>st1</code></td><td><code>sc1</code></td></tr>
  <tr><td><b>Durability</b></td><td colspan="2">99.8% - 99.9% durability (0.1% - 0.2% annual failure rate)</td></tr>
  <tr><td><b>Use cases</b></td><td> <ul><li> Big data </li><li> Data warehouses </li><li> Log processing </li></ul> </td><td> <ul><li> Throughput-oriented storage for data that is infrequently accessed </li><li> Scenarios where the lowest storage cost is important </li></ul> </td></tr>
  <tr><td><b>Volume size</b></td><td colspan="2">125 GiB - 16 TiB</td></tr>
  <tr><td><b>Max IOPS per volume</b> (1 MiB I/O)</td><td>500</td><td>250</td></tr>
  <tr><td><b>Max throughput per volume</b></td><td>500 MiB/s</td><td>250 MiB/s</td></tr>
  <tr><td><b>Amazon EBS Multi-attach</b></td><td colspan="2">Not supported</td></tr>
  <tr><td><b>Boot volume</b></td><td colspan="2">Not supported</td></tr>
</tbody>
</table>


For more information about the Hard disk drives (HDD) volumes, see [Amazon EBS Throughput Optimized HDD and Cold HDD volumes](hdd-vols.md).

## Previous generation volumes
<a name="vol-type-prev"></a>

Magnetic (`standard`) volumes are previous generation volumes that are backed by magnetic drives. They are suited for workloads with small datasets where data is accessed infrequently and performance is not of primary importance. These volumes deliver approximately 100 IOPS on average, with burst capability of up to hundreds of IOPS, and they can range in size from 1 GiB to 1 TiB.

**Tip**  
Magnetic is a previous generation volume type. If you need higher performance or performance consistency than previous-generation volumes can provide, we recommend using one of the current generation volume types.

The following table describes previous-generation EBS volume types.


|  | Magnetic | 
| --- | --- | 
| Volume type | standard | 
| Use cases | Workloads where data is infrequently accessed | 
| Volume size | 1 GiB-1 TiB | 
| Max IOPS per volume | 40–200 | 
| Max throughput per volume | 40–90 MiB/s | 
| Boot volume | Supported | 