# AWS DRS supported Linux operating systems

## General Notes

- [Review the AWS Replication Agent
  installation requirements.](installation-requirements.md "installation-requirements.md")
- Linux kernel versions up to 6.8 are supported.
- For source machines configured with LVM, on RHEL/Oracle version less than or equal to 9.4, please make sure to update the lvm package to `lvm2-2.03.23-1.el9` or latest.
- AWS Elastic Disaster Recovery does not support 32 bit versions of
  Linux.
- Hard reboots, disk changes, and crashes trigger a rescan. Graceful reboots do not trigger a
  rescan in the following versions:
  - RHEL/CentOS/Oracle Linux 6+ (kernel versions 2.6.32–431 and
    above)
  - SUSE 12+
  - Ubuntu 16+ LTS
  - AL 2 and AL 2023
  - Rocky 8+
  - Debian 9+

###### Important

**Support deprecation notes**

- **CentOS versions 6.x**:
  - As of November 28, 2025, the installation of new AWS Replication Agents on
    source servers running these operating systems, including all minor version
    releases, is no longer permitted.
  - Effective August 28, 2026, AWS Replication Agents that had been installed on
    source servers running these operating systems, including all minor version
    releases, will cease to function.

- **SLES versions 11.x**:
  - As of November 28, 2025, the installation of new AWS Replication Agents on
    source servers running these operating systems, including all minor version
    releases, is no longer permitted.
  - Effective August 28, 2026, AWS Replication Agents that had been installed on
    source servers running these operating systems, including all minor version
    releases, will cease to function.

- **Oracle versions 6.x**:
  - As of November 28, 2025, the installation of new AWS Replication Agents on
    source servers running these operating systems, including all minor version
    releases, is no longer permitted.
  - Effective August 28, 2026, AWS Replication Agents that had been installed on
    source servers running these operating systems, including all minor version
    releases, will cease to function.

- **Ubuntu 12.04**:
  - As of November 20, 2025, the installation of new AWS Replication Agents on
    source servers running this operating system, including all minor version
    releases, will no longer be permitted.
  - Effective August 20, 2026, AWS Replication Agents that had been installed
    on source servers running this operating system, including all minor version
    releases, will cease to function.

- **Red Hat Enterprise Linux (RHEL) version 5.x and CentOS
  version 5.x**:
  - As of April 1, 2025, the installation of new AWS Replication Agents on
    source servers running these operating systems, including all minor version
    releases, is no longer permitted.
  - Effective December 30, 2025, AWS Replication Agents that had been installed
    on source servers running these operating systems, including all minor version
    releases, will cease to function.

- **Debian 6.x- 9.x**:

      + As of July 30, 2025, the installation of new AWS Replication Agents on source
       servers running these operating systems, including all minor version releases, is
       no longer permitted.
      + Effective April 30, 2026, AWS Replication Agents that had been installed on
       source servers running these operating systems, including all minor version
       releases, will cease to function.

  **These Linux operating systems are supported:**

| Operating system | Supported versions                     | Prerequisites and Limitations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Linux     | 1, 2, 2023                             | Amazon Linux 1 is only supported for AWS to AWS recovery.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| RHEL             | 6.0 to 9.5                             | • For RHEL 8.x, a prerequisite is to run `$ sudo yum install elfutils-libelf-devel`<br>• Kernel versions 2.6.32-71 are not supported in RHEL 6.0<br>• The post-launch actions feature is not supported on RHEL 5.x and RHEL 6.x<br>• Nitro instance types work with RHEL 7.4+<br>• AWS requires that servers running Red Hat Enterprise Linux (RHEL) must have Cloud Access (BYOL) licenses in order to be recovered to AWS.<br>Note that servers running RHEL Cloud Access Gold Images allow you to access AWS Red Hat Update Infrastructure (RHUI), Red Hat Satellite,<br>or Red Hat Subscription Manager (RHSM). If you are using RHEL Cloud Access Gold Images, you will not be able to access RHUI upon failover<br>to AWS unless you link your AWS account to your Red Hat account via the Red Hat portal, and select the Gold image AMI in the launch template.<br>• You must select an AWS provided RHEL AMI in the Launch Template for<br>servers running Red Hat Enterprise Linux (RHEL) Pay as You Go (PAYG) images.<br>This allows access to RHUI after failover.                                                                                                                                              |
| CentOS           | 6.0 to 8.0                             | • Kernel versions 2.6.32-71 are not supported in CentOS 6.0<br>• The post-launch actions feature is not supported on CentOS 5.x and CentOS 6.x<br>• Nitro instance types work with CentOS 7.4+                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Oracle Linux     | 6.0 to 7.0, 8.5 to 8.9, and 9.0 to 9.4 | • For Oracle Linux 8.x, a prerequisite is to run`$ sudo yum install elfutils-libelf-devel`<br>• Kernel versions 2.6.32-71 are not supported in Oracle Linux 6.0<br>• The post-launch actions feature is not supported on Oracle Linux 6.x.<br>• Nitro instance types work with Oracle Linux 7.4+<br>• Oracle Linux 6.0 to 7.0 source servers must be running either<br>Unbreakable Enterprise Kernel Release 3 or higher or a Red Hat Compatible<br>Kernel.<br>• Oracle Linux 8.5 to 8.9 (running either Unbreakable Enterprise<br>Kernel Release 3 or higher or a Red Hat Compatible Kernel) – the following UEK<br>kernels were tested:<br>+ 5.15.0-200.131.27.el9uek.x86_64<br>+ 5.15.0-101.103.2.1.el9uek.x86_64<br>+ 5.15.0-3.60.5.1.el9uek.x86_64<br>+ 5.15.0-0.30.19.el9uek.x86_64<br>+ 5.15.0-206.153.7.1.el8uek.x86_64<br>+ 5.15.0-200.131.27.el8uek.x86_64<br>+ 5.15.0-101.103.2.1.el8uek.x86_64<br>+ 5.15.0-3.60.5.1.el8uek.x86_64<br>+ 5.4.17-2136.314.6.3.el8uek.x86_64<br>+ 5.4.17-2136.307.3.1.el8uek.x86_64<br>+ 5.4.17-2136.300.7.el8uek.x86_64<br>+ 4.18.0-372.32.1.0.1.el8_6.x86_64<br>• Oracle Linux 9.0 to 9.4 (running Unbreakable Enterprise Kernel<br>Release 7 or Red Hat Compatible Kernel only) |
| Rocky Linux      | 8                                      | For Rocky Linux 8.x, a prerequisite is to run<br>`$ sudo yum install elfutils-libelf-devel`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SUSE             | 11 SP4 to 15 SP5                       | • The AWS Replication Agent is supported on SUSE Linux Enterprise Server (SLES) 11 SP4 and higher.<br>• For SUSE Linux (SLES) 11 SP4 to work, you must install the Xen drivers and then reboot the<br>servers before installing the AWS Replication Agent. Use this command to<br>install the drivers: `$ sudo zypper install -y<br>xen-kmp-default`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Ubuntu           | 12.04 to 24.04                         | • Only Kernel 3.x or above are supported<br>• Azure kernels are not supported as they are not compatible with the<br>Amazon EC2 hardware. Ubuntu servers from Azure are required to switch the<br>kernel to a standard kernel or the AWS tuned Ubuntu kernel 'linux-aws'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Debian           | 10 to 11                               | Only Kernel 3.x or above are supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
