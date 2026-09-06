

# AMD SEV-SNP for Amazon EC2 instances
<a name="sev-snp"></a>

AMD Secure Encrypted Virtualization-Secure Nested Paging (AMD SEV-SNP) is a CPU feature that provides the following properties:
+ **Attestation** – AMD SEV-SNP enables you to retrieve a signed attestation report that contains a cryptographic measure that can be used to validate the instance's state and identity, and that it is running on genuine AMD hardware. For more information, see [Attest an Amazon EC2 instance with AMD SEV-SNP](snp-attestation.md).
+ **Memory encryption** – Starting with AMD EPYC (Milan), AWS Graviton2, and Intel Xeon Scalable (Ice Lake) processors, instance memory is always encrypted.

You can use AMD SEV-SNP with Dedicated Hosts or with shared tenancy.

**Topics**
+ [Concepts and terminology](#snp-concepts)
+ [Requirements](#snp-requirements)
+ [Considerations](#snp-considerations)
+ [Pricing](#snp-pricing)
+ [Find supported instance types](snp-find-instance-types.md)
+ [Enable AMD SEV-SNP](snp-work-launch.md)
+ [Attestation with AMD SEV-SNP](snp-attestation.md)

## Concepts and terminology
<a name="snp-concepts"></a>

Before you begin using AMD SEV-SNP, ensure that you are familiar with the following concepts and terminology.

**AMD SEV-SNP attestation report**  
The AMD SEV-SNP attestation report is a document that an instance can request from the CPU. The AMD SEV-SNP attestation report can be used to validate the state and identity of an instance, and to verify that it is running in a sanctioned AMD environment. The report includes a launch measurement, which is a cryptographic hash of the initial boot state of an instance, including its initial instance memory contents and initial state of the vCPUs. The AMD SEV-SNP attestation report is signed with either a VCEK signature (on Dedicated Hosts) or a VLEK signature (on shared tenancy) that chains back to an AMD root of trust.

**VCEK**  
The Versioned Chip Endorsement Key (VCEK) is a per-chip signing key that is certified by AMD and used by the AMD CPU to sign the AMD SEV-SNP attestation reports on Dedicated Hosts. VCEK signatures can be validated using certificates provided by AMD.

**VLEK**  
The Versioned Loaded Endorsement Key (VLEK) is a versioned signing key that is certified by AMD and used by the AMD CPU to sign the AMD SEV-SNP attestation reports on shared tenancy. VLEK signatures can be validated using certificates provided by AMD.

**OVMF binary**  
The Open Virtual Machine Firmware (OVMF) is the early-boot code that is used to provide a UEFI environment for the instance. The early-boot code is run before the code in the AMI is booted. The OVMF also finds and runs the boot loader provided in the AMI. For more information, see the [OVMF repository](https://github.com/tianocore/tianocore.github.io/wiki/OVMF).

## Requirements
<a name="snp-requirements"></a>

The requirements for AMD SEV-SNP depend on whether you use Dedicated Hosts or shared tenancy.

**Requirements for Dedicated Hosts**  
To use AMD SEV-SNP with Dedicated Hosts, you must meet the following requirements:
+ Use one of the following supported instance types:
  + **General purpose**: `m6a.large` \| `m6a.xlarge` \| `m6a.2xlarge` \| `m6a.4xlarge` \| `m6a.8xlarge`
  + **Compute optimized**: `c6a.large` \| `c6a.xlarge` \| `c6a.2xlarge` \| `c6a.4xlarge` \| `c6a.8xlarge` \| `c6a.12xlarge` \| `c6a.16xlarge`
  + **Memory optimized**: `r6a.large` \| `r6a.xlarge` \| `r6a.2xlarge` \| `r6a.4xlarge`
+ Allocate a Dedicated Host with AMD SEV-SNP enabled. For more information, see [Allocate a Dedicated Host with AMD SEV-SNP](snp-work-launch.md#snp-allocate-dh).
+ Launch your instance in any commercial AWS Region.
+ Use an AMI with `uefi` or `uefi-preferred` boot mode and an operating system that supports AMD SEV-SNP. For AWS, AMD SEV-SNP is supported on AL2023, RHEL 9.3, SLES 15 SP4, and Ubuntu 23.04 and later.

**Requirements for shared tenancy**  
To use AMD SEV-SNP with shared tenancy, you must meet the following requirements:
+ Use one of the following supported instance types:
  + **General purpose**: `m6a.large` \| `m6a.xlarge` \| `m6a.2xlarge` \| `m6a.4xlarge` \| `m6a.8xlarge`
  + **Compute optimized**: `c6a.large` \| `c6a.xlarge` \| `c6a.2xlarge` \| `c6a.4xlarge` \| `c6a.8xlarge` \| `c6a.12xlarge` \| `c6a.16xlarge`
  + **Memory optimized**: `r6a.large` \| `r6a.xlarge` \| `r6a.2xlarge` \| `r6a.4xlarge`
+ Launch your instance in a supported AWS Region: US East (Ohio) or Europe (Ireland).
+ Use an AMI with `uefi` or `uefi-preferred` boot mode and an operating system that supports AMD SEV-SNP. For AWS, AMD SEV-SNP is supported on AL2023, RHEL 9.3, SLES 15 SP4, and Ubuntu 23.04 and later.

## Considerations
<a name="snp-considerations"></a>

You can only enable AMD SEV-SNP when you launch an instance. When AMD SEV-SNP is enabled for your instance launch, the following rules apply.
+ After it is enabled, AMD SEV-SNP can't be disabled. It remains enabled throughout the instance lifecycle.
+ You can only [change the instance type](ec2-instance-resize.md) to another instance type that supports AMD SEV-SNP.
+ Hibernation and Nitro Enclaves aren't supported.

**Additional considerations for Dedicated Hosts**  
The following additional considerations apply when you use AMD SEV-SNP with Dedicated Hosts:
+ Firmware updates are applied when you allocate a host. To get the latest firmware, release the existing host and allocate a new one. For more information, see [Update firmware on a AMD SEV-SNP Dedicated Host](snp-work-launch.md#snp-firmware).
+ You can launch instances with or without AMD SEV-SNP enabled on a Dedicated Host that has AMD SEV-SNP support.
+ Host Resource Groups and Dedicated Host Reservations are supported.

**Additional considerations for shared tenancy**  
The following additional considerations apply when you use AMD SEV-SNP with shared tenancy:
+ If the underlying host for your instance is scheduled for maintenance, you'll receive a scheduled event notification 14 days before the event. You must manually stop or restart your instance to move it to a new host.

## Pricing
<a name="snp-pricing"></a>

**Dedicated Hosts**  
There is no additional charge for using AMD SEV-SNP on Dedicated Hosts. You pay only the standard Dedicated Host pricing. For more information, see [Dedicated Host pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/).

**Shared tenancy**  
When you launch an Amazon EC2 instance with AMD SEV-SNP enabled on shared tenancy, you are charged an additional hourly usage fee that is equivalent to 10 percent of the [On-Demand hourly rate](https://aws.amazon.com/ec2/pricing/on-demand/) of the selected instance type. This AMD SEV-SNP usage fee is a separate charge to your Amazon EC2 instance usage. Reserved Instances, Savings Plans, and operating system usage don't impact this fee.

If you configure a Spot Instance to launch with AMD SEV-SNP enabled on shared tenancy, you are charged an additional hourly usage fee that is equivalent to 10 percent of the [On-Demand hourly rate](https://aws.amazon.com/ec2/pricing/on-demand/) of the selected instance type. If the allocation strategy uses price as an input, Spot Fleet does not include this additional fee; only the Spot price is used.