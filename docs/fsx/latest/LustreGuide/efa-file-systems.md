# Working with EFA-enabled file systems

If you are creating a file system with over 10 GBps of throughput capacity,
we recommend enabling Elastic Fabric Adapter (EFA) to optimize throughput per client
instance. EFA is a high-performance network interface that uses a custom-built
operating system bypass technique and the AWS Scalable Reliable Datagram (SRD)
network protocol to increase performance. For information about EFA,
see [Elastic Fabric Adapter
for AI/ML and HPC workloads on Amazon EC2](../../../AWSEC2/latest/UserGuide/efa.md "../../../AWSEC2/latest/UserGuide/efa.md") in the _Amazon EC2 User Guide_.

EFA-enabled file systems support two additional performance features: GPUDirect Storage (GDS) and ENA Express.
GDS support builds on EFA to further enhance performance by enabling direct data transfer between the file system
and the GPU memory, bypassing the CPU. This direct path eliminates the need for redundant memory copies and CPU
involvement in the data transfer operations. With EFA and GDS support, you can achieve higher throughput to
individual EFA-enabled client instances. ENA Express provides optimized network communication for
Amazon EC2 instances using an advanced path selection algorithm and enhanced congestion control mechanism.
With ENA Express support, you can achieve higher throughput to individual ENA Express-enabled client instances.
For information about ENA Express,
see [Improve network
performance between EC2 instances with ENA Express](../../../AWSEC2/latest/UserGuide/ena-express.md "../../../AWSEC2/latest/UserGuide/ena-express.md") in the _Amazon EC2 User Guide_.

###### Topics

- [Considerations when using EFA-enabled file systems](#efa-considerations "#efa-considerations")
- [Prerequisites for using EFA-enabled file systems](#efa-prerequisites "#efa-prerequisites")
- [Creating an EFA-enabled file system](#create-efa-file-system "#create-efa-file-system")

## Considerations when using EFA-enabled file systems

Here are a few important items to consider when creating EFA-enabled file systems:

- **Multiple connectivity options:** EFA-enabled
  file systems can communicate with client instances using ENA, ENA Express, and EFA.
- **Deployment type:** EFA is supported on Persistent 2
  file systems with a metadata configuration specified, including file systems using the Intelligent-Tiering
  storage class.
- **Updating EFA setting:** You can choose to enable
  EFA when you create a new file system but you cannot enable or disable EFA on an existing file system.
- **Scaling throughput with storage capacity:** You can
  scale storage capacity on an EFA-enabled SSD-based file system to increase throughput capacity but you cannot
  change the throughput tier of an EFA-enabled file system.
- **AWS Regions:** For a list of AWS Regions that support
  EFA-enabled Persistent 2 file systems,
  see [Deployment type availability](using-fsx-lustre.md#persistent-deployment-regions "using-fsx-lustre.md#persistent-deployment-regions").

## Prerequisites for using EFA-enabled file systems

The following are prerequisites for using EFA-enabled file systems:

**To create your EFA-enabled file system:**

- Use an EFA-enabled security group. For more information,
  see [EFA-enabled security groups](limit-access-security-groups.md#efa-security-groups "limit-access-security-groups.md#efa-security-groups").
- Use the same Availability Zone and /16 CIDR as your EFA-enabled
  client instances within your Amazon VPC.
- On Intelligent-Tiering file systems, EFA is only supported with
  a throughput capacity of 4,000 MBps or increments of 4,000 MBps.

**To access your file system using Elastic Fabric Adapter (EFA):**

- Use Nitro v4 (or higher) EC2 instances that support EFA, excluding the trn2 instance family.
  See [Supported
  instance types](../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types "../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types") in the _Amazon EC2 User Guide_.
- Run AL2023, RHEL 9.5 and newer, or Ubuntu 22+ with kernel version of 6.8 and newer.
  For more information,
  see [Installing the Lustre client](install-lustre-client.md "install-lustre-client.md").
- Install the EFA modules and configure EFA interfaces on your client instances.
  For more information,
  see [Configuring EFA clients](configure-efa-clients.md "configure-efa-clients.md").

**To access your file system using GPUDirect Storage (GDS):**

- Use an Amazon EC2 P5, P5e, P5en, or P6-B200 client instance.
- Install the NVIDIA Compute Unified Device Architecture (CUDA) package,
  the open source NVIDIA driver, and the NVIDIA GPUDirect Storage Driver on your
  client instance. For more information,
  see [Install the GDS driver (optional)](configure-efa-clients.md#install-gds-driver "configure-efa-clients.md#install-gds-driver").

**To access your file system using ENA Express:**

- Use Amazon EC2 instances that support ENA Express.
  See [Supported
  instance types for ENA Express](../../../AWSEC2/latest/UserGuide/ena-express.md#ena-express-supported-instance-types "../../../AWSEC2/latest/UserGuide/ena-express.md#ena-express-supported-instance-types") in the _Amazon EC2 User Guide_.
- Update the settings for your Linux instance.
  See [Prerequisites
  for Linux instances](../../../AWSEC2/latest/UserGuide/ena-express.md#ena-express-prereq-linux "../../../AWSEC2/latest/UserGuide/ena-express.md#ena-express-prereq-linux") in the _Amazon EC2 User Guide_.
- Enable ENA Express on network interfaces for your client instances.
  For details, see [Review ENA Express settings
  for your EC2 instance](../../../AWSEC2/latest/UserGuide/ena-express-list-view.md "../../../AWSEC2/latest/UserGuide/ena-express-list-view.md") in the _Amazon EC2 User Guide_.

## Creating an EFA-enabled file system

This section contains instructions on how to create an FSx for Lustre EFA-enabled file system
using the AWS CLI. For information on how to create an EFA-enabled file system using the Amazon FSx console,
see [Step 1: Create your FSx for Lustre file system](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1").

Use the [create-file-system](../../../cli/latest/reference/fsx/create-file-system.md "../../../cli/latest/reference/fsx/create-file-system.md") CLI command (or the equivalent [CreateFileSystem](../APIReference/API_CreateFileSystem.md "../APIReference/API_CreateFileSystem.md") API operation). The following
example creates an FSx for Lustre EFA-enabled file system with a
`PERSISTENT_2` deployment type.

```
`aws fsx create-file-system\
 --storage-capacity 4800 \
 --storage-type SSD \
 --file-system-type LUSTRE \
 --file-system-type-version 2.15 \
 --subnet-ids subnet-01234567890 \
 --security-group-ids sg-0123456789abcdefg \
 --lustre-configuration '{"DeploymentType": "PERSISTENT_2", "EfaSupport": true}'`
```

After successfully creating the file system, Amazon FSx returns the file
system's description in JSON format.
