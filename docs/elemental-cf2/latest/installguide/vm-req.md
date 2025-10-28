This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# System Requirements for Virtual Machines (VMs)

This section describes the system requirements if you're using a virtual machine
(VM).

###### Note

Other than recommended and minimum hardware requirements, this information pertains
only to VMs. It is not intended for kernel-based virtual machines (KVMs).

## Required Software

This is the software that you need when using a VM.

- VMware® vSphere® Hypervisor (ESXi) version 6 or higher, installed
  onto bare-metal hardware.
- VMware® vCenter Server™, required to install the AWS Elemental OVA.
- VMware® vSphere® web client or desktop client.

###### Important

Do not use the free versions of these products; they do not include all the
required features.

## Guests per Host Hardware

Each instance of AWS Elemental products is considered a _guest_.

We recommend one AWS Elemental Live or AWS Elemental Server virtual machine per host
hardware.

For other AWS Elemental products, make sure the combined loads for all products do not
exceed recommended hardware requirements. See the following sections for details.

## Recommended Hardware Requirements

The resources that you have available impact your performance. For encoders, the
resources determine the speed for encoding assets and the number of streams, bitrate,
and type of encoding that's possible. We recommend the following hardware
specifications for optimum performance.

AWS Elemental Conductor Live, AWS Elemental Conductor File, AWS Elemental Statmux

- RAM: 16 GB
- Disk space: 500 GB
- CPU cores: 24
- Processor speed: 2.3 GHz or more (Comparable to an Intel® Xeon
  processor E5-2630)

AWS Elemental Server and AWS Elemental Live

- RAM: 16 GB
- Disk space: 500 GB
- CPU cores: 32
- Processor speed: 2.0 GHz or more (Comparable to an Intel® Xeon
  processor E5-2650)

AWS Elemental Delta

- RAM: 128 GB
- Disk space: 500 GB
- CPU cores: 24
- Processor speed: 2.3 GHz or more (Comparable to an Intel® Xeon
  processor E5-2630)

## Minimum Hardware Requirements

You can use host hardware with these minimum resources to run AWS Elemental products
for functional testing or for integrating with the AWS Elemental software API. These
resource levels are not for performance testing.

All products except AWS Elemental Delta

- RAM: 12 GB
- Disk space: 400 GB
- CPU cores: 8

EDLTlong;

- RAM: 16 GB
- Disk space: 40 GB
- CPU cores: 8

## Compatible Hardware Platform

Verify that the host hardware platform is compatible with the VMware platform. Look at
the _VMware Compatibility Guide_ at vmware.com.
AWS Elemental has specifically tested and qualified the following hardware:

- Cisco® UCS®
- HP® ProLiant® BL460c Gen8 Server Blade in an HP® C7000 enclosure
- Supermicro® SuperBlade™ and Supermicro® SYS-1027GR-TRF chassis
