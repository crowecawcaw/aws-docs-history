# Elastic Fabric Adapter for AI/ML and HPC workloads on Amazon EC2

An Elastic Fabric Adapter (EFA) is a network device that you can attach to your Amazon EC2 instance to
accelerate Artificial Intelligence (AI), Machine Learning (ML), and High Performance Computing
(HPC) applications. EFA enables you to achieve the application performance of an on-premises
AI/ML or HPC cluster, with the scalability, flexibility, and elasticity provided by the AWS
Cloud.

EFA provides lower and more consistent latency and higher throughput than the TCP transport
traditionally used in cloud-based HPC systems. It enhances the performance of inter-instance
communication that is critical for scaling AI/ML and HPC applications. It is optimized to work
on the existing AWS network infrastructure and it can scale depending on application
requirements.

EFA integrates with Libfabric 1.7.0 and later, and it supports Nvidia Collective
Communications Library (NCCL) for AI and ML applications, and Open MPI 4.1 and later
and Intel MPI 2019 Update 5 and later for HPC applications.

EFA supports RDMA (Remote Direct Memory Access) write on most supported instance types that have
Nitro version 4 and later. RDMA read is supported on all instances with Nitro version 4 and later.
For more information, see [Supported instance types](#efa-instance-types "#efa-instance-types").

###### Contents

- [EFA basics](#efa-basics "#efa-basics")
- [Supported interfaces and libraries](#efa-mpi "#efa-mpi")
- [Supported instance types](#efa-instance-types "#efa-instance-types")
- [Supported operating systems](#efa-os "#efa-os")
- [EFA limitations](#efa-limits "#efa-limits")
- [EFA pricing](#efa-pricing "#efa-pricing")
- [Get started with EFA and MPI](efa-start.md "efa-start.md")
- [Get started with EFA and NCCL](efa-start-nccl.md "efa-start-nccl.md")
- [Maximize network bandwidth](efa-acc-inst-types.md "efa-acc-inst-types.md")
- [Create and attach an EFA](create-efa.md "create-efa.md")
- [Detach and delete an EFA](detach-efa.md "detach-efa.md")
- [Monitor an EFA](efa-working-monitor.md "efa-working-monitor.md")
- [Verify the EFA installer](efa-verify.md "efa-verify.md")
- [Release notes](efa-changelog.md "efa-changelog.md")

## EFA basics

An EFA device can be attached to an EC2 instance in two ways:

1. Using a traditional EFA interface, also called EFA with ENA, which creates both an EFA
   device and an ENA device.
2. Using an EFA-only interface, which creates just the EFA device.

The EFA device provides capabilities like built-in OS-bypass and congestion control through
the Scalable Reliable Datagram (SRD) protocol. The EFA device features enable low-latency,
reliable transport functionality that allows EFA interface to provide better application
performance for HPC and ML applications on Amazon EC2. While the ENA device offers traditional
IP networking.

![Contrasting a traditional HPC software stack with one that uses an EFA.](images/efa_stack.png)

Traditionally, AI/ML applications use NCCL and HPC applications use the Message Passing Interface
(MPI) to interface with the system's network transport. In the AWS cloud, this has meant that
applications interface with NCCL or MPI, which then uses the operating system's TCP/IP stack and
the ENA device driver to enable network communication between instances.

With a traditional EFA (EFA with ENA) or EFA-only interface, AI/ML applications use NCCL and
HPC applications use MPI, to interface directly with the Libfabric API. The Libfabric API
bypasses the operating system kernel and communicates directly with the EFA device to put packets
on the network. This reduces overhead and enables AI/ML and HPC applications to run more efficiently.

###### Note

Libfabric is a core component of the OpenFabrics Interfaces (OFI) framework,
which defines and exports the user-space API of OFI. For more information, see
the [Libfabric OpenFabrics](https://ofiwg.github.io/libfabric/ "https://ofiwg.github.io/libfabric/")
website.

### Differences between ENA, EFA, and EFA-only network

interfaces

Amazon EC2 provides two types of network interfaces:

- **ENA** interfaces provide all of the traditional IP
  networking and routing features that are required to support IP networking for a VPC.
  For more information, see [Enable enhanced networking with ENA on your EC2 instances](enhanced-networking-ena.md "enhanced-networking-ena.md").
- **EFA** (EFA with ENA) interfaces provide both the
  ENA device for IP networking and the EFA device for low-latency, high-throughput
  communication.
- **EFA-only** interfaces support only the EFA device
  capabilities, without the ENA device for traditional IP networking.

The following table provides a comparison of ENA, EFA, and EFA-only network interfaces.

|                                                       | ENA                                          | EFA (EFA with ENA)                                                    | EFA-only                                                              |
| ----------------------------------------------------- | -------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Supports IP networking functionality                  | Yes                                          | Yes                                                                   | No                                                                    |
| Can be assigned IPv4 or IPv6 addresses                | Yes                                          | Yes                                                                   | No                                                                    |
| Can be used as primary network interface for instance | Yes                                          | Yes                                                                   | No                                                                    |
| Counts towards ENI attachment limit for instance      | Yes                                          | Yes                                                                   | Yes                                                                   |
| Instance type support                                 | Supported on all Nitro-based instances types | [Supported instance types](#efa-instance-types "#efa-instance-types") | [Supported instance types](#efa-instance-types "#efa-instance-types") |
| Parameter naming in EC2 APIs                          | `interface`                                  | `efa`                                                                 | `efa-only`                                                            |
| Field naming in EC2 console                           | No selection                                 | EFA with ENA                                                          | EFA-only                                                              |

## Supported interfaces and libraries

EFAs support the following interfaces and libraries:

- Open MPI 4.1 and later
- Intel MPI 2019 Update 5 and later
- NVIDIA Collective Communications Library (NCCL) 2.4.2 and later
- AWS Neuron SDK version 2.3 and later

## Supported instance types

All of the following instance types support EFA. Additionally, the tables
indicate RDMA read and RDMA write support for the instance types.

Nitro v6

| Instance type         | RDMA read support | RDMA write support |
| --------------------- | ----------------- | ------------------ |
| General Purpose       |
| m8a.48xlarge          | Yes               | Yes                |
| m8a.metal-48xl        | Yes               | Yes                |
| m8i.48xlarge          | Yes               | Yes                |
| m8i.96xlarge          | Yes               | Yes                |
| m8i.metal-48xl        | Yes               | Yes                |
| m8i.metal-96xl        | Yes               | Yes                |
| Compute Optimized     |
| c8a.48xlarge          | Yes               | Yes                |
| c8a.metal-48xl        | Yes               | Yes                |
| c8gn.16xlarge         | Yes               | Yes                |
| c8gn.24xlarge         | Yes               | Yes                |
| c8gn.48xlarge         | Yes               | Yes                |
| c8gn.metal-24xl       | Yes               | Yes                |
| c8gn.metal-48xl       | Yes               | Yes                |
| c8i.48xlarge          | Yes               | Yes                |
| c8i.96xlarge          | Yes               | Yes                |
| c8i.metal-48xl        | Yes               | Yes                |
| c8i.metal-96xl        | Yes               | Yes                |
| Memory Optimized      |
| r8a.48xlarge          | Yes               | Yes                |
| r8a.metal-48xl        | Yes               | Yes                |
| r8gb.16xlarge         | Yes               | Yes                |
| r8gb.24xlarge         | Yes               | Yes                |
| r8gb.metal-24xl       | Yes               | Yes                |
| r8gn.16xlarge         | Yes               | Yes                |
| r8gn.24xlarge         | Yes               | Yes                |
| r8gn.48xlarge         | Yes               | Yes                |
| r8gn.metal-24xl       | Yes               | Yes                |
| r8gn.metal-48xl       | Yes               | Yes                |
| r8i.48xlarge          | Yes               | Yes                |
| r8i.96xlarge          | Yes               | Yes                |
| r8i.metal-48xl        | Yes               | Yes                |
| r8i.metal-96xl        | Yes               | Yes                |
| x8aedz.24xlarge       | Yes               | Yes                |
| x8aedz.metal-24xl     | Yes               | Yes                |
| Storage Optimized     |
| i8ge.48xlarge         | Yes               | No                 |
| i8ge.metal-48xl       | Yes               | No                 |
| Accelerated Computing |
| p6-b200.48xlarge      | Yes               | Yes                |
| p6-b300.48xlarge      | Yes               | Yes                |

Nitro v5

| Instance type              | RDMA read support | RDMA write support |
| -------------------------- | ----------------- | ------------------ |
| General Purpose            |
| m8g.24xlarge               | Yes               | No                 |
| m8g.48xlarge               | Yes               | No                 |
| m8g.metal-24xl             | Yes               | No                 |
| m8g.metal-48xl             | Yes               | No                 |
| m8gd.24xlarge              | No                | No                 |
| m8gd.48xlarge              | No                | No                 |
| m8gd.metal-24xl            | No                | No                 |
| m8gd.metal-48xl            | No                | No                 |
| Compute Optimized          |
| c7gn.16xlarge              | Yes               | No                 |
| c7gn.metal                 | Yes               | No                 |
| c8g.24xlarge               | Yes               | No                 |
| c8g.48xlarge               | Yes               | No                 |
| c8g.metal-24xl             | Yes               | No                 |
| c8g.metal-48xl             | Yes               | No                 |
| c8gd.24xlarge              | No                | No                 |
| c8gd.48xlarge              | No                | No                 |
| c8gd.metal-24xl            | No                | No                 |
| c8gd.metal-48xl            | No                | No                 |
| Memory Optimized           |
| r8g.24xlarge               | No                | No                 |
| r8g.48xlarge               | No                | No                 |
| r8g.metal-24xl             | No                | No                 |
| r8g.metal-48xl             | No                | No                 |
| r8gd.24xlarge              | No                | No                 |
| r8gd.48xlarge              | No                | No                 |
| r8gd.metal-24xl            | No                | No                 |
| r8gd.metal-48xl            | No                | No                 |
| x8g.24xlarge               | No                | No                 |
| x8g.48xlarge               | No                | No                 |
| x8g.metal-24xl             | No                | No                 |
| x8g.metal-48xl             | No                | No                 |
| Storage Optimized          |
| i7ie.48xlarge              | Yes               | No                 |
| i7ie.metal-48xl            | Yes               | No                 |
| i8g.48xlarge               | No                | No                 |
| Accelerated Computing      |
| p5en.48xlarge              | Yes               | Yes                |
| p6e-gb200.36xlarge         | Yes               | Yes                |
| trn2.48xlarge              | Yes               | Yes                |
| trn2u.48xlarge             | Yes               | Yes                |
| High Performance Computing |
| hpc7g.4xlarge              | Yes               | No                 |
| hpc7g.8xlarge              | Yes               | No                 |
| hpc7g.16xlarge             | Yes               | No                 |

Nitro v4

| Instance type              | RDMA read support | RDMA write support |
| -------------------------- | ----------------- | ------------------ |
| General Purpose            |
| m6a.48xlarge               | Yes               | Yes                |
| m6a.metal                  | Yes               | Yes                |
| m6i.32xlarge               | Yes               | Yes                |
| m6i.metal                  | Yes               | Yes                |
| m6id.32xlarge              | Yes               | Yes                |
| m6id.metal                 | Yes               | Yes                |
| m6idn.32xlarge             | Yes               | Yes                |
| m6idn.metal                | Yes               | Yes                |
| m6in.32xlarge              | Yes               | Yes                |
| m6in.metal                 | Yes               | Yes                |
| m7a.48xlarge               | Yes               | No                 |
| m7a.metal-48xl             | Yes               | No                 |
| m7g.16xlarge               | Yes               | No                 |
| m7g.metal                  | Yes               | No                 |
| m7gd.16xlarge              | Yes               | No                 |
| m7gd.metal                 | Yes               | No                 |
| m7i.48xlarge               | Yes               | No                 |
| m7i.metal-48xl             | Yes               | No                 |
| Compute Optimized          |
| c6a.48xlarge               | Yes               | Yes                |
| c6a.metal                  | Yes               | Yes                |
| c6gn.16xlarge              | Yes               | Yes                |
| c6i.32xlarge               | Yes               | Yes                |
| c6i.metal                  | Yes               | Yes                |
| c6id.32xlarge              | Yes               | Yes                |
| c6id.metal                 | Yes               | Yes                |
| c6in.32xlarge              | Yes               | Yes                |
| c6in.metal                 | Yes               | Yes                |
| c7a.48xlarge               | Yes               | No                 |
| c7a.metal-48xl             | Yes               | No                 |
| c7g.16xlarge               | Yes               | Yes                |
| c7g.metal                  | Yes               | Yes                |
| c7gd.16xlarge              | Yes               | No                 |
| c7gd.metal                 | Yes               | No                 |
| c7i.48xlarge               | Yes               | No                 |
| c7i.metal-48xl             | Yes               | No                 |
| Memory Optimized           |
| r6a.48xlarge               | Yes               | Yes                |
| r6a.metal                  | Yes               | Yes                |
| r6i.32xlarge               | Yes               | Yes                |
| r6i.metal                  | Yes               | Yes                |
| r6id.32xlarge              | Yes               | Yes                |
| r6id.metal                 | Yes               | Yes                |
| r6idn.32xlarge             | Yes               | Yes                |
| r6idn.metal                | Yes               | Yes                |
| r6in.32xlarge              | Yes               | Yes                |
| r6in.metal                 | Yes               | Yes                |
| r7a.48xlarge               | No                | No                 |
| r7a.metal-48xl             | No                | No                 |
| r7g.16xlarge               | No                | No                 |
| r7g.metal                  | No                | No                 |
| r7gd.16xlarge              | No                | No                 |
| r7gd.metal                 | No                | No                 |
| r7i.48xlarge               | No                | No                 |
| r7i.metal-48xl             | No                | No                 |
| r7iz.32xlarge              | No                | No                 |
| r7iz.metal-32xl            | No                | No                 |
| u7i-6tb.112xlarge          | Yes               | Yes                |
| u7i-8tb.112xlarge          | Yes               | Yes                |
| u7i-12tb.224xlarge         | Yes               | Yes                |
| u7in-16tb.224xlarge        | Yes               | Yes                |
| u7in-24tb.224xlarge        | Yes               | Yes                |
| u7in-32tb.224xlarge        | Yes               | Yes                |
| u7inh-32tb.480xlarge       | Yes               | Yes                |
| x2idn.32xlarge             | Yes               | Yes                |
| x2idn.metal                | Yes               | Yes                |
| x2iedn.32xlarge            | Yes               | Yes                |
| x2iedn.metal               | Yes               | Yes                |
| Storage Optimized          |
| i4g.16xlarge               | Yes               | Yes                |
| i4i.32xlarge               | Yes               | Yes                |
| i4i.metal                  | Yes               | Yes                |
| i7i.24xlarge               | Yes               | No                 |
| i7i.48xlarge               | Yes               | No                 |
| i7i.metal-48xl             | Yes               | No                 |
| im4gn.16xlarge             | Yes               | Yes                |
| Accelerated Computing      |
| f2.48xlarge                | Yes               | Yes                |
| g6.8xlarge                 | Yes               | Yes                |
| g6.12xlarge                | Yes               | Yes                |
| g6.16xlarge                | Yes               | Yes                |
| g6.24xlarge                | Yes               | Yes                |
| g6.48xlarge                | Yes               | Yes                |
| g6e.8xlarge                | Yes               | Yes                |
| g6e.12xlarge               | Yes               | Yes                |
| g6e.16xlarge               | Yes               | Yes                |
| g6e.24xlarge               | Yes               | Yes                |
| g6e.48xlarge               | Yes               | Yes                |
| gr6.8xlarge                | Yes               | Yes                |
| p5.4xlarge                 | Yes               | Yes                |
| p5.48xlarge                | Yes               | Yes                |
| p5e.48xlarge               | Yes               | Yes                |
| trn1.32xlarge              | Yes               | Yes                |
| trn1n.32xlarge             | Yes               | Yes                |
| High Performance Computing |
| hpc6a.48xlarge             | Yes               | Yes                |
| hpc6id.32xlarge            | Yes               | Yes                |
| hpc7a.12xlarge             | Yes               | No                 |
| hpc7a.24xlarge             | Yes               | No                 |
| hpc7a.48xlarge             | Yes               | No                 |
| hpc7a.96xlarge             | Yes               | No                 |

Nitro v3

| Instance type         | RDMA read support | RDMA write support |
| --------------------- | ----------------- | ------------------ |
| General Purpose       |
| m5dn.24xlarge         | No                | No                 |
| m5dn.metal            | No                | No                 |
| m5n.24xlarge          | No                | No                 |
| m5n.metal             | No                | No                 |
| m5zn.12xlarge         | No                | No                 |
| m5zn.metal            | No                | No                 |
| Compute Optimized     |
| c5n.9xlarge           | No                | No                 |
| c5n.18xlarge          | No                | No                 |
| c5n.metal             | No                | No                 |
| Memory Optimized      |
| r5dn.24xlarge         | No                | No                 |
| r5dn.metal            | No                | No                 |
| r5n.24xlarge          | No                | No                 |
| r5n.metal             | No                | No                 |
| x2iezn.12xlarge       | No                | No                 |
| x2iezn.metal          | No                | No                 |
| Storage Optimized     |
| i3en.12xlarge         | No                | No                 |
| i3en.24xlarge         | No                | No                 |
| i3en.metal            | No                | No                 |
| Accelerated Computing |
| dl1.24xlarge          | Yes               | No                 |
| dl2q.24xlarge         | No                | No                 |
| g4dn.8xlarge          | No                | No                 |
| g4dn.12xlarge         | No                | No                 |
| g4dn.16xlarge         | No                | No                 |
| g4dn.metal            | No                | No                 |
| g5.8xlarge            | No                | No                 |
| g5.12xlarge           | No                | No                 |
| g5.16xlarge           | No                | No                 |
| g5.24xlarge           | No                | No                 |
| g5.48xlarge           | No                | No                 |
| inf1.24xlarge         | No                | No                 |
| p3dn.24xlarge         | No                | No                 |
| p4d.24xlarge          | Yes               | No                 |
| p4de.24xlarge         | Yes               | No                 |
| vt1.24xlarge          | No                | No                 |
| Previous Generation   |
| p3dn.24xlarge         | No                | No                 |

###### To see the available instance types that support EFAs in a specific Region

The available instance types vary by Region. To see the available instance types that
support EFAs in a Region, use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md")
command with the `--region` parameter. Include the `--filters`
parameter to scope the results to the instance types that support EFA and the
`--query` parameter to scope the output to the value of
`InstanceType`.

```
aws ec2 describe-instance-types \
    --region `us-east-1`  \
    --filters Name=network-info.efa-supported,Values=true \
    --query "InstanceTypes[*].[InstanceType]"  \
    --output text | sort
```

## Supported operating systems

Operating system support differs depending on the processor type. The following table
shows the supported operating systems.

| Operating system                       | Intel/AMD (`x86_64`) instance types | AWS Graviton (`arm64`) instance types |
| -------------------------------------- | ----------------------------------- | ------------------------------------- |
| Amazon Linux 2023                      | ✓                                   | ✓                                     |
| Amazon Linux 2                         | ✓                                   | ✓                                     |
| RHEL 8 and 9                           | ✓                                   | ✓                                     |
| Debian 11 and 12                       | ✓                                   | ✓                                     |
| Rocky Linux 8 and 9                    | ✓                                   | ✓                                     |
| Ubuntu 22.04 and 24.04                 | ✓                                   | ✓                                     |
| SUSE Linux Enterprise 15 SP2 and later | ✓                                   | ✓                                     |
| OpenSUSE Leap 15.5 and later           | ✓                                   |                                       |

###### Note

Some of the listed operating systems might not be supported with Intel MPI. If you are using
Intel MPI, refer to the [Intel MPI documentation](https://www.intel.com/content/www/us/en/developer/articles/system-requirements/mpi-library-system-requirements.html "https://www.intel.com/content/www/us/en/developer/articles/system-requirements/mpi-library-system-requirements.html") to verify support for your operating system.

## EFA limitations

EFAs have the following limitations:

- RDMA write is not supported with all instance types. For more information, see
  [Supported instance types](#efa-instance-types "#efa-instance-types").
- EFA traffic1 between P4d/P4de/DL1 instances and other instance types is currently not supported.
- [Instance types that support multiple network cards](using-eni.md#network-cards "using-eni.md#network-cards")
  can be configured with one EFA per network card. All other supported instance types
  support only one EFA per instance.
- `c7g.16xlarge`, `m7g.16xlarge`, and `r7g.16xlarge`
  Dedicated Instances and Dedicated Hosts are not supported when an EFA is attached.
- EFA traffic1 can't cross Availability Zones or VPCs. This does not apply to normal
  IP traffic from the ENA device of an EFA interface.
- EFA traffic1 is not routable. Normal IP traffic from the ENA device of an EFA
  interface remains routable.
- EFA is not supported on AWS Outposts.
- The EFA device of an EFA (EFA with ENA) interface is supported on Windows instances
  only for AWS Cloud Digital Interface Software Development Kit (AWS CDI SDK) based applications. If you
  attach an EFA (EFA with ENA) interface to a Windows instance for non-CDI SDK based
  applications, it functions as an ENA interface, without the added EFA device capabilities.
  The EFA-only interface is not supported by AWS CDI based applications on Windows or Linux.
  For more information, see the [AWS Cloud Digital Interface Software Development Kit (AWS CDI SDK) User Guide](../../../CDI-SDK/latest/ug/what-is.md "../../../CDI-SDK/latest/ug/what-is.md").

1*EFA traffic* refers to the traffic transmitted through the EFA device of
either an EFA (EFA with ENA) or EFA-only interface.

## EFA pricing

EFA is available as an optional Amazon EC2 networking feature that you can enable on any supported
instance at no additional cost.
