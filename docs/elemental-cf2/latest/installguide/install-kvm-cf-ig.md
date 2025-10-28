This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Installing AWS Elemental Conductor File Node-locked Licenses on a

Kernel-based Virtual Machine (KVM)

This section is for IT administrators who perform the first-time installation of
AWS Elemental Conductor File software on a kernel-based virtual machine (KVM).

###### KVM Guest System Requirements

The resources available to your KVM determine the speed for encoding assets and the
number of streams, bitrate, and type of encoding possible. Your KVM guest should have,
at minimum, the following resources allocated to it:

- RAM: 16 GB
- Disk space: 500 GB
- CPU cores: 24
- Processor speed: 2.3 GHz or more (comparable to that of an Intel® Xeon®
  Processor ES-2630)
  For minimum resources required for testing purposes, see [Minimum Hardware Requirements](vm-req.md#vm-req-min "vm-req.md#vm-req-min").

###### Phase 1 Setup

This section explains how to perform the KVM phase 1 setup on each blade, including
the following:

- Create a KVM with the OVA image.
- Install the licenses.
- Install the AWS Elemental Conductor File software.
- Configure eth0 as the management interface on each KVM.

###### Prerequisite Knowledge

To complete this process, you must have the following knowledge:

- A basic understanding of server virtualization.
- Installing and using KVM.
- Moving files from a KVM guest to other systems over the network. We recommend using a utility
  such as SCP.
- Locating recently downloaded files.
  The procedure for installing any version of AWS Elemental Conductor File is the same; only the version number in the file name changes. In this procedure, we show how to install version 2.18.3.12345 of the software.

Installation consists of four parts:

1. Downloading files from AWS Elemental
2. Installing the host operating system (OS)
3. Installing the AWS Elemental software
4. Setting up licensing

###### Topics

- [Step A: Prepare the Hardware and Download Files](install-kvm-cf-ig-prep.md "install-kvm-cf-ig-prep.md")
- [Step B: Deploy the KVM](install-kvm-cf-ig-install-vm.md "install-kvm-cf-ig-install-vm.md")
- [Step C: Enable CPU Passthrough](install-kvm-cf-ig-passthrough.md "install-kvm-cf-ig-passthrough.md")
- [Step D: Install the AWS Elemental Software](install-kvm-cf-ig-install-sw.md "install-kvm-cf-ig-install-sw.md")
- [Step E: Set-up Licensing](install-kvm-cf-ig-licensing.md "install-kvm-cf-ig-licensing.md")
- [Step F: Complete Node Configuration](install-kvm-cf-ig-complete.md "install-kvm-cf-ig-complete.md")
