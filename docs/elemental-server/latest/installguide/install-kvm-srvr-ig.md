This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Installing AWS Elemental Server Node-locked Licenses on a

Kernel-Based Virtual Machine (KVM)

This section is for IT administrators who perform first-time installation of
AWS Elemental Server software on a KVM (kernel-based virtual machine).

###### KVM Guest System Requirements

The resources available to your virtual machine (VM) determine the speed for encoding
assets and the number of streams, bitrate, and possible types of encoding. Your VM guest
should have, at minimum, the following resources allocated to it:

- RAM: 16 GB
- Disk space: 500 GB
- CPU cores: 24
- Processor speed: 2.3 GHz or more (comparable to that of an Intel® Xeon®
  Processor ES-2630)
  For minimum resources required for testing purposes, see [Minimum Hardware Requirements](vm-req.md#vm-req-min "vm-req.md#vm-req-min").

###### Phase 1 Setup

This section explains how to perform the following on each blade:

- Create a virtual machine with the OVA image.
- Install the licenses.
- Install the AWS Elemental Server software.
- Configure eth0 as the management interface on each virtual machine.

###### Prerequisite Knowledge

To complete this process, you must have the following knowledge:

- You have a basic understanding of server virtualization.
- You have installed and know how to use KVM.
- You know how to move files from a VM guest to other systems over the network. We
  recommend using a utility such as SCP.
- You know how to locate recently downloaded files.
  The procedure for installing any version of AWS Elemental Server is the same; only the version number in the file name changes. In this procedure, we show how to install version 2.18.3.12345 of the software.

Installation consists of four parts:

1. Downloading files from AWS Elemental
2. Installing the host operating system (OS)
3. Installing the AWS Elemental software
4. Setting up licensing

###### Topics

- [Step A: Prepare Hardware and Download
  Files](install-kvm-srvr-ig-prep.md "install-kvm-srvr-ig-prep.md")
- [Step B: Deploy the VM](install-kvm-srvr-ig-install-vm.md "install-kvm-srvr-ig-install-vm.md")
- [Step C: Enable CPU Passthrough](install-kvm-srvr-ig-passthrough.md "install-kvm-srvr-ig-passthrough.md")
- [Step D: Install the AWS Elemental Software](install-kvm-srvr-ig-install-sw.md "install-kvm-srvr-ig-install-sw.md")
- [Step E: Set-up Licensing](install-kvm-srvr-ig-licensing.md "install-kvm-srvr-ig-licensing.md")
- [Step F: Complete Node
  Configuration](install-kvm-srvr-ig-complete.md "install-kvm-srvr-ig-complete.md")
