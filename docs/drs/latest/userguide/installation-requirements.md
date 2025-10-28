# Installation requirements for AWS Replication

Agent

Before installing the AWS Replication Agent on your source servers, ensure that they meet
the following requirements:

###### Topics

- [General requirements](#general-requirements "#general-requirements")
- [Source server requirements](#general-requirements2 "#general-requirements2")
- [Linux installation requirements](#linux-requirements "#linux-requirements")
- [Windows installation requirements](#windows-requirements "#windows-requirements")

## General requirements

- Ensure that the source server operating system is supported by AWS.
  - [Supported Windows operating systems.](Supported-Operating-Systems-Windows.md "Supported-Operating-Systems-Windows.md")
  - [Supported Linux operating systems.](Supported-Operating-Systems-Linux.md "Supported-Operating-Systems-Linux.md")

- Ensure that your setup meets all replication networking requirements. [Learn more about network
  requirements.](preparing-environments.md "preparing-environments.md")
- Ensure MAC address stability – ensure that the MAC addresses of the source servers
  do not change upon a reboot or any other common changes in your network environment.
  AWS Elastic Disaster Recovery calculates the unique ID of the source server from the MAC address. When a
  MAC address changes, AWS Elastic Disaster Recovery is no longer able to correctly identify the source
  server. Consequently, replication stops. If this happens, you need to reinstall the
  AWS Replication Agent and start replication from the beginning.

###### Note

Elastic Disaster Recovery Agents can only be installed on instances that are in AWS Regions that are
supported by Elastic Disaster Recovery. In case of AWS-AWS disaster recovery (in-AWS), Elastic Disaster Recovery should be initialized in both source and target region (done by going through the initialization wizard).

## Source server requirements

- Verify that your source server has at least 300 MB of free RAM to run the AWS
  Replication Agent.
- AWS Elastic Disaster Recovery only supports 64-bit operating systems built for the
  x86 system architecture.
- AWS Elastic Disaster Recovery does not support paravirtualized source servers.
- The AWS Replication Agent installer supports multipath.

## Linux installation requirements

Ensure that your Linux source server meets the following installation requirements prior
to installing the AWS Replication Agent:

- Python 2 (2.4 or above) or Python 3 (3.0 or above) is installed on the server.
- Verify that you meet these disk space requirements:
  - At least 4 GB of free disk space on the
    root directory (/) of your source server for the installation. To check the available
    disk space on the root directory, run the `df -h /` command.
  - At least 500 MB of free diskspace on the _/tmp_ directory for the
    duration of the installation process. To check the available disk
    space on the /tmp directory run the `df -h
/tmp` command.
  - If `/boot` is a separate partition, ensure that it has a minimum of 50 MB free space needed for the installation. To check the available disk
    space on the /boot directory run the `df -h
/boot` command.

- The active bootloader software is GRUB 1 or 2.
- Secure Boot is not supported in Linux.
- Machines that boot off a disk configured with GPT partitioning must have the
  package 'grub2-pc-modules' installed
- When performing a failback for a Linux server, you must boot the Failback Client
  with BIOS boot mode.
- Ensure that /tmp is mounted as read+write.
- Boot disks that span multiple physical disks are not supported.
- Ensure that /tmp is mounted with the exec option. Verify that the /tmp directory is
  mounted in a way that allows you to run scripts and applications from it.

To verify that the /tmp directory is mounted without the noexec option, run the
`sudo mount | grep '/tmp'` command.

If the result is similar to the example, i the issue exists in
your OS: /dev/xvda1 on /tmp type ext4 (rw,noexec)

|To fix and remove the noexec option from the mounted /tmp directory, run the `sudo mount -o remount,exec /tmp` command. **Example of the troubleshooting procedure:** ![Terminal commands showing mount operations and grep searches for "/tmp" directory.](images/agent66.png) <br>• The AWS Elastic Disaster Recovery user needs to be a user in the sudoers list - a user who can perform sudo. <br>• Ensure that the dhclient package is installed. If not, please install the package, by running `yum install dhclient`. <br>• Verify that you have kernel-devel/linux-headers installed that are exactly the same version as the kernel you are running. The version number of the kernel headers should be identical to the version number of the kernel. Follow these steps: 1. Identify the version of your running kernel by running the `uname -r` command. The 'uname -r' output version should match the version of one of the installed kernel headers packages (kernel-devel-<version number> / linux-headers-<version number>). 2. Identify the version of your kernel-devel/linux-headers by running: + On RHEL/CENTOS/Oracle/SUSE: `rpm -qa | grep kernel`. This command looks for kernel-devel. + On Debian/Ubuntu: `apt-cache search linux-headers`. 3. Verify that the folder that contains the kernel-devel/linux-headers is not a symbolic link. If the content of the kernel-devel/linux-headers, which match the version of the kernel, is actually a symbolic link, you need to remove the link before installing the required package. To verify that the folder that contains the kernel-devel/linux-headers is not a symbolic link, run the following command: + On RHEL/CENTOS/Oracle: `ls -l /usr/src/kernels` + On Debian/Ubuntu/SUSE: `ls -l /usr/src` These results show that the linux-headers are not a symbolic link. ![Terminal output showing directory listing with linux-headers files and their details.](images/agent5.png) 4. If the content of the kernel-devel/linux-headers, which match the version of the kernel, is a symbolic link, you need to delete the link using the `rm /usr/src/<LINK NAME>` command. For example: rm /usr/src/linux-headers-4.4.1 5. Install the correct kernel-devel/linux-headers from the repositories. If none of the already installed kernel-devel/linux-headers packages match your running kernel version, you need to install the matching package. ###### Note You can have several kernel headers versions simultaneously on your OS, and you can therefore safely install new kernel headers packages in addition to your existing ones, without uninstalling the other versions of the package. A new kernel headers package does not impact the kernel, and does not overwrite older versions of the kernel headers. You must install a kernel headers package with the exact same version number of the running kernel. To install the correct kernel-devel/linux-headers, run: + On RHEL/CENTOS/Oracle/SUSE: `sudo yum install kernel-devel-`uname -r`` + On Oracle with Unbreakable Enterprise Kernel: `sudo yum install kernel-uek-devel-`uname -r`` + On Debian/Ubuntu: `sudo apt-get install linux-headers-`uname -r`` 6. If no matching package was found on the repositories configured on your server, you can download it manually from the Internet and then install it. To download the matching kernel-devel/linux-headers package, navigate to: + RHEL, CENTOS, Oracle, and SUSE [package directory](http://rpm.pbone.net/ "http://rpm.pbone.net/") + Debian [package directory](https://packages.debian.org/ "https://packages.debian.org/") + Ubuntu [package directory](https://packages.ubuntu.com/ "https://packages.ubuntu.com/") ## Windows installation requirements <br>• Install all available Windows updates on the server. <br>• A minimum of 4 GB of free disk space is required to launch a drill or recovery instance. <br>• When performing a recovery, you must boot the Failback Client with the same boot mode (BIOS or UEFI) as the Windows source server. <br>• A graceful reboot from the OS menu or Windows CLI of a Windows source server does not trigger a rescan in AWS DRS once the source server is restarted. Hard reboots, disk changes, and crashes trigger a rescan. <br>• Mount points must be assigned a drive letter to be recognized by Elastic Disaster Recovery. A folder path is not recognized.
