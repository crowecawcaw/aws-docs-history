

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Operating systems supported by MGN
<a name="Supported-Operating-Systems"></a>

AWS Transform MGN supports replication of physical, virtual or cloud-based source servers for multiple versions of Windows and Linux operating systems. 

## Supported Windows operating systems
<a name="Supported-Operating-Systems-Windows"></a>

AWS Transform MGN allows replication of physical, virtual or cloud-based source servers to the AWS Cloud for multiple versions of Windows. 

**Note**  
** Support deprecation notes**  
 **Windows 2003**: Effective February 15, 2026, this operating system is no longer supported. 
**Windows 2008**: Effective December 30, 2026, this operating system is no longer supported.
**Windows 7**: Effective December 30, 2026, this operating system is no longer supported.

### General Notes
<a name="General-Notes"></a>
+ [Review the AWS Replication Agent installation requirements.](installation-requirements.md)
+ Windows source servers require a minimum of 2 GB of free disk space to launch a test or cutover instance.
+ The WMI service must be activated to install the AWS Replication Agent.

**These Windows operating systems are supported:**


| Operating system | Supported versions | Prerequisites and Limitations | 
| --- | --- | --- | 
| Microsoft Windows Server 2025 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  | 
| Microsoft Windows Server 2022 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  | 
| Microsoft Windows Server 2019 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  | 
| Microsoft Windows Server 2016 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  | 
| Microsoft Windows 11 64-bit |   | Ensure that the [auto sleep function](https://support.microsoft.com/en-us/windows/shut-down-sleep-or-hibernate-your-pc-2941d165-7d0a-a5e8-c5ad-8c972e8e6eff) is disabled. Data replication may be interrupted if the feature is activated. | 
| Microsoft Windows 10 64-bit |   | Ensure that the [auto sleep function in Windows 10](https://answers.microsoft.com/en-us/windows/forum/all/turn-off-auto-sleep-in-windows-10/79f2d86c-3378-495f-8da2-4d78021876d4) is disabled. Data replication may be interrupted if the feature is activated. | 
| Microsoft Windows Server 2012 <br />This version has reached end of life. We recommend that you update to a more recent version. | 64-bit and R2 64-bit | Requires .Net Framework version 4.5 or above to be installed by the end user. | 
| Microsoft Windows Server 2008 <br />This version has reached end of life. We recommend that you update to a more recent version. | 64-bit and R2 64-bit | + Windows Server 2008 requires .Net Framework version 3.5 to be installed by the end user. <br />Windows Server 2008 **R2** requires .Net Framework version 4.5 or above to be installed by the end user.<br />+ Windows 2008 x64 requires SP2 and other Microsoft updates to support the SHA-2 signature of the AWS Replication Agent driver.<br />+ Windows Server 2008 R2 requires SP1 and the necessary KB updates for SHA-2 Code Signing Support to be installed prior to deploying the AWS Replication Agent. See [2019 SHA-2 Code Signing Support requirement for Windows and WSUS](https://support.microsoft.com/en-us/topic/2019-sha-2-code-signing-support-requirement-for-windows-and-wsus-64d1c82d-31ee-c273-3930-69a4cde8e64f).<br />+ The AWS Replication Agent and agent installer requires a separate installer file, `AwsReplicationWindowsLegacyInstaller.exe` for end-of-life versions of Windows because they use older versions of software components that cannot be upgraded.<br />+  Windows 2008 with GPT partitioned system drives are not supported. <br />+  [Nitro instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) can only be used with Windows Server 2008 R2 and upwards. Earlier versions are not supported. <br />+  The WMI service must be activated to install the AWS Replication Agent. <br />+  A shutdown (from the OS menu or Windows CLI) of a Windows source server triggers a rescan in AWS MGN once the source server is restarted.   | 
| Microsoft Windows Server 2003 64-bit<br />This version has reached end of life. We recommend that you update to a more recent version. |  |  + Requires .Net Framework version 3.5 to be installed by the end user.<br />+ Does not support TLS 1.2, so you cannot download the AWS Replication Agent installer directly using the default browser. You must copy the file to the server using another method.<br />+  The AWS Replication Agent and agent installer requires a separate installer file, `AwsReplicationWindowsLegacyInstaller.exe` for end-of-life versions of Windows because they use older versions of software components that cannot be upgraded.<br />+  The WMI service must be activated to install the AWS Replication Agent. <br />+  [Nitro instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) can only be used with Windows Server 2008 R2 and upwards. Earlier versions are not supported. <br />+  A shutdown (from the OS menu or Windows CLI) of a Windows source server triggers a rescan in AWS MGN once the source server is restarted.   | 
| Microsoft Windows 7 64-bit<br />This version has reached end of life. We recommend that you update to a more recent version. |  |  + The AWS Replication Agent and agent installer requires a separate installer file, `AwsReplicationWindowsLegacyInstaller.exe` for end-of-life versions of Windows because they use older versions of software components that cannot be upgraded.<br />+  [Nitro instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) can only be used with Windows Server 2008 R2 and upwards. Earlier versions are not supported. <br />+  A shutdown (from the OS menu or Windows CLI) of a Windows source server triggers a rescan in AWS MGN once the source server is restarted.   | 

## Supported Linux operating systems
<a name="Supported-Operating-Systems-Linux"></a>

**Note**  
** Support deprecation notes **  
**Red Hat Enterprise Linux (RHEL) version 5.x and CentOS version 5.x**: Effective December 30, 2025, these operating systems are no longer supported.
**Debian 6.x- 9.x**: Effective April 30, 2026, these operating systems are no longer supported.
**Ubuntu 12.04**: Effective August 20, 2026, this operating system is no longer supported.
**Oracle versions 6.x**: Effective August 28, 2026, these operating systems are no longer supported.
**CentOS versions 6.x**: Effective August 28, 2026, these operating systems are no longer supported.
**SLES versions 11.x**: Effective August 28, 2026, these operating systems are no longer supported.
**CentOS 7-7.9**: Effective November 20, 2026, these operating systems are no longer supported.
**Amazon Linux 1 (AL1)**: Effective November 20, 2026, this operating system is no longer supported.
**Ubuntu 14.04**: Effective December 20, 2026, this operating system is no longer supported.
**Debian 10**: Effective December 30, 2026, this operating system is no longer supported.
**Red Hat Enterprise Linux (RHEL) versions 6.x**: Effective December 30, 2026, these operating systems are no longer supported.
**CentOS versions 8.x**: Effective December 30, 2026, these operating systems are no longer supported.

### General Notes
<a name="General-Notes"></a>
+ [Review the AWS Replication Agent installation requirements.](installation-requirements.md)
+ MGN does not support 32 bit versions of Linux.
+ For source machines configured with LVM, on RHEL/Oracle version less than or equal to 9.4, make sure to update the lvm package to `lvm2-2.03.23-1.el9` or latest.
+  Kernel version 4.9.256 is not supported. Agent installation fails on servers that run this kernel version. 
+  Kernel versions earlier than 2.6.18-164 are not supported by AWS Transform MGN. Therefore, servers that run these kernel versions cannot be replicated by AWS Transform MGN. 

**These Linux operating systems are supported:**


| Operating system | Supported versions | Prerequisites and Limitations | 
| --- | --- | --- | 
| Amazon Linux | 1, 2, 2023 |  + Amazon Linux 1 is only supported for AWS to AWS recovery.<br />+ Amazon Linux 1 is not supported in Canada West (Calgary).<br />+ Only agent-based replication is supported.  | 
| RHEL | 6.0 to 9.8, 10, 10.1, 10.2 |  +  For RHEL 8.x, a prerequisite is to run `$ sudo yum install elfutils-libelf-devel`<br />+  Kernel versions 2.6.32-71 are not supported in RHEL 6.0 <br />+  The post-launch actions feature is not supported on RHEL 5.x and RHEL 6.x <br />+  Nitro instance types work with RHEL 7.4\+ <br />+   AWS requires that servers running Red Hat Enterprise Linux (RHEL) must have Cloud Access (BYOL) licenses in order to be recovered to AWS. Note that servers running RHEL Cloud Access Gold Images allow you to access AWS Red Hat Update Infrastructure (RHUI), Red Hat Satellite, or Red Hat Subscription Manager (RHSM). If you are using RHEL Cloud Access Gold Images, you are not able to access RHUI upon failover to AWS unless you link your AWS account to your Red Hat account via the Red Hat portal, and select the Gold image AMI in the launch template.  <br />+   You must select an AWS provided RHEL AMI in the Launch Template for servers running Red Hat Enterprise Linux (RHEL) Pay as You Go (PAYG) images. This allows access to RHUI after migration. Note that usage of these images incurs Amazon EC2 charges for software and infrastructure per AWS Marketplace rates.  <br />+  RHEL 8.3 and 8.4 are not supported in Mexico (Central) region. <br />+  RHEL 8.3, 8.4, and 8.10 are not supported in Asia Pacific (New Zealand) and Asia Pacific (Taipei) regions. <br />+  **FSx for ONTAP storage**: If using FSx for ONTAP as the target storage type, pre-install iSCSI and multipath packages on the source server before migration: `sudo yum install -y iscsi-initiator-utils device-mapper-multipath` (or `dnf` for RHEL 8\+). RHEL subscription credentials are tied to the source instance and are not valid on the migrated target.   | 
| CentOS | 6.0 to 8.0, Stream 9, Stream 10 |  +  Kernel versions 2.6.32-71 are not supported in CentOS 6.0 <br />+  For Centos 8.x, a prerequisite is to run `$ sudo yum install elfutils-libelf-devel`<br />+  The post-launch actions feature is not supported on CentOS 5.x and CentOS 6.x <br />+  Nitro instance types work with CentOS 7.4\+ <br />+   CentOS Stream 9: these kernels were tested:   5.14.0-689.el9.x86\_64   5.14.0-691.el9.x86\_64   5.14.0-694.el9.x86\_64   5.14.0-697.el9.x86\_64   5.14.0-700.el9.x86\_64   <br />CentOS Stream is a rolling-release OS. Kernels outside this list are supported via local driver compilation. <br />+   CentOS Stream 10: these kernels are supported:   6.12.0-216.el10.x86\_64   6.12.0-218.el10.x86\_64   6.12.0-222.el10.x86\_64   6.12.0-224.el10.x86\_64   6.12.0-225.el10.x86\_64   6.12.0-228.el10.x86\_64   <br />CentOS Stream is a rolling-release OS. Kernels outside this list are not supported. <br />+  **FSx for ONTAP storage**: If using FSx for ONTAP as the target storage type, pre-install iSCSI and multipath packages on the source server before migration: `sudo yum install -y iscsi-initiator-utils device-mapper-multipath`. CentOS repository credentials are tied to the source instance and are not valid on the migrated target.   | 
| Oracle Linux | 6.0 to 7.8, 8.5 to 8.9, 9.0 to 9.4, 9.6, 9.7, and 10.1 |  + For Oracle Linux 8.x, a prerequisite is to run`$ sudo yum install elfutils-libelf-devel` <br />+  Kernel versions 2.6.32-71 are not supported in Oracle Linux 6.0 <br />+  The post-launch actions feature is not supported on Oracle Linux 6.x. <br />+  Nitro instance types work with Oracle Linux 7.4\+ <br />+   Oracle Linux 6.0 to 7.8 source servers must be running either Unbreakable Enterprise Kernel Release 3 or higher or a Red Hat Compatible Kernel.  <br />+   Oracle Linux 8.5 to 8.9 (running either Unbreakable Enterprise Kernel Release 3 or higher or a Red Hat Compatible Kernel) – these UEK kernels were tested:   5.15.0-200.131.27.el9uek.x86\_64   5.15.0-101.103.2.1.el9uek.x86\_64   5.15.0-3.60.5.1.el9uek.x86\_64   5.15.0-0.30.19.el9uek.x86\_64   5.15.0-206.153.7.1.el8uek.x86\_64   5.15.0-200.131.27.el8uek.x86\_64   5.15.0-101.103.2.1.el8uek.x86\_64   5.15.0-3.60.5.1.el8uek.x86\_64   5.4.17-2136.314.6.3.el8uek.x86\_64   5.4.17-2136.307.3.1.el8uek.x86\_64   5.4.17-2136.300.7.el8uek.x86\_64   4.18.0-372.32.1.0.1.el8\_6.x86\_64   <br />+   Oracle Linux 9.0 to 9.4 (running Unbreakable Enterprise Kernel Release 7 or Red Hat Compatible Kernel only)  <br />+   Oracle Linux 9.6 and 9.7 (running Unbreakable Enterprise Kernel Release 8 or Red Hat Compatible Kernel only)  <br />+   Oracle Linux 10.1 (running Unbreakable Enterprise Kernel Release 8 or Red Hat Compatible Kernel only) – these kernels are supported:   6.12.0-100.28.2.el10uek.x86\_64 - 6.12.0-105.51.5.el10uek.x86\_64   6.12.0-124.8.1.el10\_1 - 6.12.0-124.56.1.el10\_1     | 
| Rocky Linux | 8 to 9.8, 10, 10.1, 10.2 |  + For Rocky Linux 8.x, a prerequisite is to run `$ sudo yum install elfutils-libelf-devel`<br />+ For UEFI-based Rocky Linux 10.2 systems without repository access, install `grub2-efi-x64-modules` before you run the agent installer.  | 
| SUSE Linux Enterprise Server | 11 SP4 to 15 SP7 |  + The AWS Replication Agent is supported on SUSE Linux Enterprise Server (SLES) 11 SP4 and higher.<br />+   For SUSE Linux (SLES) 11 SP4 to work, you must install the Xen drivers and then reboot the servers before installing the AWS Replication Agent. Use this command to install the drivers: `$ sudo zypper install -y xen-kmp-default`.<br />+  **FSx for ONTAP storage**: If using FSx for ONTAP as the target storage type, pre-install iSCSI and multipath packages on the source server before migration: `sudo zypper install -y open-iscsi multipath-tools`. SLES subscription credentials are tied to the source instance and are not valid on the migrated target.   | 
| Ubuntu | 12.04 to 24.04 |  +  Only Kernel 3.x or above are supported <br />+  Azure kernels are not supported as they are not compatible with the Amazon EC2 hardware. Ubuntu servers from Azure are required to switch the kernel to a standard kernel or the AWS tuned Ubuntu kernel 'linux-aws'.   | 
| Debian | 10 to 11 |  Only Kernel 3.x or above are supported  | 
| Debian | 6.x to 9.x | Deprecated April 30, 2026. Effective April 30, 2026, these operating systems are no longer supported. | 
| AlmaLinux | 8.6, 8.7, 8.8, 8.9, 8.10, 9.6, 9.7, 9.8, 10, 10.1, 10.2 | Before you install the agent on AlmaLinux, complete the following prerequisites:+ Run the following command with sudo privileges: <pre>$ sudo yum install elfutils-libelf-devel</pre><br />+ For UEFI-based AlmaLinux 9.8 and 10.2 systems without repository access, install `grub2-efi-x64-modules` before you run the agent installer. | 