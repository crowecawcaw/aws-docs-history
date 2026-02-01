• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Supported operating systems and

machine types

Before working with Systems Manager, verify that your operating system (OS), OS version, and
machine type are supported as managed nodes.

###### Topics

- [Supported operating systems for
  Systems Manager](#prereqs-operating-systems "#prereqs-operating-systems")
- [Supported machine types in hybrid and
  multicloud environments](#supported-machine-types "#supported-machine-types")

## Supported operating systems for

Systems Manager

The following sections list the OSs and OS versions supported by Systems Manager.

###### Note

If you plan to manage and configure AWS IoT Greengrass core devices by using Systems Manager,
those devices must meet the requirements for AWS IoT Greengrass. For more information, see
[Setting up AWS IoT Greengrass core
devices](../../../greengrass/v2/developerguide/setting-up.md "../../../greengrass/v2/developerguide/setting-up.md") in the _AWS IoT Greengrass Version 2 Developer Guide_.

If you plan to manage and configure AWS IoT and non-AWS edge devices,
those devices must meet the requirements listed here and be configured as
on-premises managed nodes for Systems Manager. For more information, see [Managing edge devices with
Systems Manager](systems-manager-setting-up-edge-devices.md "systems-manager-setting-up-edge-devices.md").

###### Important

We strongly recommend that you avoid using OS versions that have reached End-of-Life (EOL).
OS vendors including AWS typically don't provide security patches or other updates for versions that have reached EOL.
Continuing to use an EOL system greatly increases the risk of not being able to apply upgrades, including security
fixes, and other operational problems. AWS does not test Systems Manager functionality on OS versions that have reached EOL.

Patch Manager, a tool in Systems Manager, might not support all the OS versions listed in
this topic. For a list of OS versions supported by Patch Manager, see [Patch Manager prerequisites](patch-manager-prerequisites.md "patch-manager-prerequisites.md").

###### Operating system types

- [Linux](#prereqs-os-linux "#prereqs-os-linux")
- [macOS (Amazon EC2 instances only)](#prereqs-os-mac "#prereqs-os-mac")
- [Windows Server](#prereqs-os-windows-server "#prereqs-os-windows-server")

Select an OS platform to see the supported major and minor versions.

### Linux

| AlmaLinux | Versions | x86 | x86_64 | ARM64 |
| --------- | -------- | --- | ------ | ----- |
| 8.3–8.10  |          | ✓   | ✓      |
| 9*.x*     |          | ✓   | ✓      |

| Amazon Linux 2             | Versions | x86 | x86_64 | ARM64 |
| -------------------------- | -------- | --- | ------ | ----- |
| 2.0 and all later versions |          | ✓   | ✓      |

| Amazon Linux 2023                        | Versions | x86 | x86_64 | ARM64 |
| ---------------------------------------- | -------- | --- | ------ | ----- |
| 2023.0.20230315.0 and all later versions |          | ✓   | ✓      |

| Bottlerocket                 | Versions | x86_64 | ARM64 |
| ---------------------------- | -------- | ------ | ----- |
| 1.0.0 and all later versions | ✓        | ✓      |

| CentOS Stream | Versions | x86 | x86_64 | ARM64 |
| ------------- | -------- | --- | ------ | ----- |
| 9             |          | ✓   | ✓      |

| Debian Server | Versions | x86 | x86_64 | ARM64 |
| ------------- | -------- | --- | ------ | ----- |
| Bullseye (11) |          | ✓   | ✓      |
| Bookworm (12) |          | ✓   | ✓      |

| Oracle Linux | Versions | x86 | x86_64 | ARM64 |
| ------------ | -------- | --- | ------ | ----- |
| 7.5–7.8      |          | ✓   |        |
| 8*.x*        |          | ✓   |        |
| 9*.x*        |          | ✓   |        |

| Red Hat Enterprise Linux (RHEL) | Versions | x86 | x86_64 | ARM64 |
| ------------------------------- | -------- | --- | ------ | ----- |
| 7.0–7.5                         |          | ✓   |        |
| 7.6–8*.x*                       |          | ✓   | ✓      |
| 9*.x*                           |          | ✓   | ✓      |
| 10._x_                          |          | ✓   | ✓      |

| Rocky Linux | Versions | x86 | x86_64 | ARM64 |
| ----------- | -------- | --- | ------ | ----- |
| 8*.x*       |          | ✓   | ✓      |
| 9*.x*       |          | ✓   | ✓      |

| SUSE Linux Enterprise Server (SLES) | Versions | x86 | x86_64 | ARM64 |
| ----------------------------------- | -------- | --- | ------ | ----- |
| 15.3 and later versionsx            |          | ✓   | ✓      |

| Ubuntu Server           | Versions | x86 | x86_64 | ARM64 |
| ----------------------- | -------- | --- | ------ | ----- |
| 16.04 LTS and 18.04 LTS |          | ✓   | ✓      |
| 20.04 LTS               |          | ✓   | ✓      |
| 22.04 LTS               |          | ✓   | ✓      |
| 24.04 LTS               |          | ✓   | ✓      |
| 25.04                   |          | ✓   | ✓      |

### macOS (Amazon EC2 instances only)

| Version               | x86 | x86_64 | Mac with Apple silicon |
| --------------------- | --- | ------ | ---------------------- |
| 13\*.x<br>• (Ventura) |     | ✓      | ✓                      |
| 14\*.x<br>• (Sonoma)  |     | ✓      | ✓                      |
| 15\*.x<br>• (Sequoia) |     | ✓      | ✓                      |

###### Note

macOS is not supported in all AWS Regions. For more information about
Amazon EC2 support for macOS, see [Amazon EC2 Mac
instances](../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md "../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md") in the _Amazon EC2 User Guide_.

### Windows Server

SSM Agent requires Windows PowerShell 3.0 or later to run
certain AWS Systems Manager documents (SSM documents) on Windows Server instances (for
example, the legacy `AWS-ApplyPatchBaseline` document). Verify that
your Windows Server instances are running Windows Management Framework
3.0 or later. This framework includes Windows
PowerShell. For more information, see [Windows Management Framework 3.0](https://www.microsoft.com/en-us/download/details.aspx?id=34595&751be11f-ede8-5a0c-058c-2ee190a24fa6=True "https://www.microsoft.com/en-us/download/details.aspx?id=34595&751be11f-ede8-5a0c-058c-2ee190a24fa6=True").

| Version               | x86 | x86_64 | ARM64 |
| --------------------- | --- | ------ | ----- |
| 2012 and 2012 R2**²** |     | ✓      |       |
| 2016                  |     | ✓      |       |
| 2019                  |     | ✓      |       |
| 2022                  |     | ✓      |       |
| 2025                  |     | ✓      |       |

**¹**
**Windows Server 2012 and 2012 R2 support**: Windows Server
2012 and 2012 R2 reached end of support on October 10, 2023. To use SSM Agent
with these versions, we recommend using Extended Security Updates (ESUs) from
Microsoft. For more information, see [Windows Server 2012 and 2012 R2 reaching end of support](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-server-2012-r2-end-of-support "https://learn.microsoft.com/en-us/lifecycle/announcements/windows-server-2012-r2-end-of-support") on the Microsoft
website.

## Supported machine types in hybrid and

multicloud environments

Systems Manager supports a number of machine types as _managed
nodes_. A managed node is any machine configured to work with
Systems Manager.

This user guide uses the term _hybrid and
multicloud_ to refer to an environment that contains any combination
of the following machine types:

- Amazon Elastic Compute Cloud (Amazon EC2) instances
- Servers on your own premises (on-premises servers)
- AWS IoT Greengrass core devices
- AWS IoT and non-AWS edge devices
- Virtual machines (VMs), including VMs in other cloud environments

For information about AWS support for hybrid and multicloud environments, see
[AWS Solutions for Hybrid and
Multicloud](https://aws.amazon.com/hybrid-multicloud/ "https://aws.amazon.com/hybrid-multicloud/").
