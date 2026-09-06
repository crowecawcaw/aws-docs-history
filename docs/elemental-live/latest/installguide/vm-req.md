

# System requirements for Virtual Machines (VMs)
<a name="vm-req"></a>

This section describes the system requirements for AWS Elemental Live if you're using a virtual machine (VM).

## Constraints with VMs
<a name="elive-vm-constraints"></a>

The VMs must be deployed on on-premise hardware. Cloud-based VMs are not supported. To implement video transcoding in the cloud, see [AWS Elemental MediaLive](https://aws.amazon.com/medialive).

## Required software
<a name="elive-vm-reqs-software"></a>

This is the software that you need when using a VM.
+ VMware vSphere Hypervisor (ESXi) version  7 update 2 or higher, installed onto bare-metal hardware. 
+ VMware vCenter Server, required to install the AWS Elemental OVA.
+ VMware vSphere web client or desktop client.

**Important**  
Do not use the free versions of these products; they do not include all the required features.

## Guests per host hardware
<a name="elive-vm-reqs-guests"></a>

We recommend one virtual machine per host hardware.

## Recommended hardware requirements
<a name="elive-vm-reqs-hardware"></a>

The resources that you have available impact your performance. The resources determine the speed for encoding assets and the number of streams, bitrate, and type of encoding that's possible. We recommend the following hardware specifications for optimum performance.
+ RAM: 32 GB
+ Disk space: 500 GB
+ CPU cores: 32
+ Processor speed: 2.3 GHz or more 

  The processor must support Page Address Extension 

  Comparable to an Intel Xeon 6250 processor, or to an AMD EPYC 7502P processor

## Minimum hardware requirements
<a name="elive-vm-reqs-hardware-min"></a>

The following minimum host hardware resource levels are not for performance testing. You can use them to run AWS Elemental Live for functional testing, or for integrating with the AWS Elemental software API. 
+ RAM: 16 GB
+ Disk space: 400 GB
+ CPU cores: 6
+ Processor speed: 2.3 GHz or more

  Comparable to an Intel Xeon E-2276G processor, or to an AMD Opteron 1352 processor

## Compatible hardware platform
<a name="elive-vm-reqs-host-platform"></a>

The host hardware platform must be compatible with the VMware platform. For information, contact your AWS Elemental Sales Team.