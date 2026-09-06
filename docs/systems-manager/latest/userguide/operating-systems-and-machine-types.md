

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Supported operating systems and machine types
<a name="operating-systems-and-machine-types"></a>

Before working with Systems Manager, verify that your operating system (OS), OS version, and machine type are supported as managed nodes.

**Topics**
+ [Supported operating systems for Systems Manager](#prereqs-operating-systems)
+ [Supported machine types in hybrid and multicloud environments](#supported-machine-types)

## Supported operating systems for Systems Manager
<a name="prereqs-operating-systems"></a>

AWS Systems Manager provides support for a defined set of operating system (OS) versions that are actively supported by the OS vendor and are listed as supported in the AWS Systems Manager documentation. AWS Systems Manager OS support is aligned with vendors' lifecycles, as defined in their software terms of service. Not all operating systems or OS versions supported by a vendor are supported by AWS Systems Manager.

AWS Systems Manager support for an OS version ends when the OS vendor declares that version end-of-life (EOL). Support does not extend to vendor paid Extended Long-Term Support (ELTS), or similar paid programs. While customers can continue to use and install OS versions that have gone past vendor EOL, AWS Support will only provide assistance if an issue is reproducible on a supported OS version.

New AWS Systems Manager product releases, including new major releases of SSM Agent, do not add support for OS versions that are scheduled to reach vendor EOL within six months of the release date.

The following sections list the OSs and OS versions supported by Systems Manager.

**Note**  
If you plan to manage and configure AWS IoT Greengrass core devices by using Systems Manager, those devices must meet the requirements for AWS IoT Greengrass. For more information, see [Setting up AWS IoT Greengrass core devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html) in the *AWS IoT Greengrass Version 2 Developer Guide*.  
If you plan to manage and configure AWS IoT and non-AWS edge devices, those devices must meet the requirements listed here and be configured as on-premises managed nodes for Systems Manager. For more information, see [Managing edge devices with Systems Manager](systems-manager-setting-up-edge-devices.md).

**Important**  
We strongly recommend that you avoid using OS versions that have reached End-of-Life (EOL). OS vendors including AWS typically don't provide security patches or other updates for versions that have reached EOL. Continuing to use an EOL system greatly increases the risk of not being able to apply upgrades, including security fixes, and other operational problems. AWS does not test Systems Manager functionality on OS versions that have reached EOL.  
Patch Manager might not support all the OS versions listed in this topic. For a list of OS versions supported by Patch Manager, see [Patch Manager prerequisites](patch-manager-prerequisites.md).

**Topics**
+ [Linux](#prereqs-os-linux)
+ [macOS (Amazon EC2 instances only)](#prereqs-os-mac)
+ [Windows Server](#prereqs-os-windows-server)

Select an OS platform to see the supported major and minor versions.

### Linux
<a name="prereqs-os-linux"></a>


**AlmaLinux**  

| Versions | x86 | x86\_64 | ARM64 | 
| --- | --- | --- | --- | 
| 8.3–8.10 |  | ✓ | ✓ | 
| 9.x |  | ✓ | ✓ | 


**Amazon Linux 2**  

| Versions | x86 | x86\_64 | ARM64 | 
| --- | --- | --- | --- | 
| 2.0 and all later versions |  | ✓ | ✓ | 


**Amazon Linux 2023**  

| Versions | x86 | x86\_64 | ARM64 | 
| --- | --- | --- | --- | 
| 2023.0.20230315.0 and all later versions |  | ✓ | ✓ | 


**Bottlerocket**  

| Versions | x86\_64 | ARM64 | 
| --- | --- | --- | 
| 1.0.0 and all later versions | ✓ | ✓ | 


**CentOS Stream**  

| Versions | x86 | x86\_64 | ARM64 | 
| --- | --- | --- | --- | 
| 9 |  | ✓ | ✓ | 


**Debian Server**  

| Versions | x86 | x86\_64 | ARM64 | 
| --- | --- | --- | --- | 
| Bullseye (11) |  | ✓ | ✓ | 
| Bookworm (12) |  | ✓ | ✓ | 


**Oracle Linux**  

| Versions | x86 | x86\_64 | ARM64 | 
| --- | --- | --- | --- | 
| 7.5–7.8 |  | ✓ |  | 
| 8.x |  | ✓ |  | 
| 9.x |  | ✓ |  | 


**Red Hat Enterprise Linux (RHEL)**  

| Versions | x86 | x86\_64 | ARM64 | 
| --- | --- | --- | --- | 
| 7.0–7.5 |  | ✓ |  | 
| 7.6–8.x |  | ✓ | ✓ | 
| 9.x |  | ✓ | ✓ | 
| 10.x |  | ✓ | ✓ | 


**Rocky Linux**  

| Versions | x86 | x86\_64 | ARM64 | 
| --- | --- | --- | --- | 
| 8.x |  | ✓ | ✓ | 
| 9.x |  | ✓ | ✓ | 


**SUSE Linux Enterprise Server (SLES)**  

| Versions | x86 | x86\_64 | ARM64 | 
| --- | --- | --- | --- | 
| 15.3 and later versionsx |  | ✓ | ✓ | 


**Ubuntu Server**  

| Versions | x86 | x86\_64 | ARM64 | 
| --- | --- | --- | --- | 
| 18.04 LTS |  | ✓ | ✓ | 
| 20.04 LTS |  | ✓ | ✓ | 
| 22.04 LTS |  | ✓ | ✓ | 
| 24.04 LTS |  | ✓ | ✓ | 
| 25.04 |  | ✓ | ✓ | 

### macOS (Amazon EC2 instances only)
<a name="prereqs-os-mac"></a>



| Version | x86 | x86\_64 | Mac with Apple silicon | 
| --- | --- | --- | --- | 
| 13.x (Ventura) |  | ✓ | ✓ | 
| 14.x (Sonoma) |  | ✓ | ✓ | 
| 15.x (Sequoia) |  | ✓ | ✓ | 

**Note**  
macOS is not supported in all AWS Regions. For more information about Amazon EC2 support for macOS, see [Amazon EC2 Mac instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html) in the *Amazon EC2 User Guide*.

### Windows Server
<a name="prereqs-os-windows-server"></a>

SSM Agent requires Windows PowerShell 3.0 or later to run certain AWS Systems Manager documents (SSM documents) on Windows Server instances (for example, the legacy `AWS-ApplyPatchBaseline` document). Verify that your Windows Server instances are running Windows Management Framework 3.0 or later. This framework includes Windows PowerShell. For more information, see [Windows Management Framework 3.0](https://www.microsoft.com/en-us/download/details.aspx?id=34595&751be11f-ede8-5a0c-058c-2ee190a24fa6=True).



| Version | x86 | x86\_64 | ARM64 | 
| --- | --- | --- | --- | 
| 2012 and 2012 R2² |  | ✓ |  | 
| 2016 |  | ✓ |  | 
| 2019 |  | ✓ |  | 
| 2022 |  | ✓ |  | 
| 2025 |  | ✓ |  | 

**¹** **Windows Server 2012 and 2012 R2 support**: Windows Server 2012 and 2012 R2 reached end of support on October 10, 2023. To use SSM Agent with these versions, we recommend using Extended Security Updates (ESUs) from Microsoft. For more information, see [Windows Server 2012 and 2012 R2 reaching end of support](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-server-2012-r2-end-of-support) on the Microsoft website.

## Supported machine types in hybrid and multicloud environments
<a name="supported-machine-types"></a>

Systems Manager supports several machine types as *managed nodes*. A managed node is any machine configured to work with Systems Manager.

This user guide uses the term *hybrid and multicloud* to refer to an environment that contains any combination of the following machine types:
+ Amazon Elastic Compute Cloud (Amazon EC2) instances
+ Servers on your own premises (on-premises servers)
+ AWS IoT Greengrass core devices
+ AWS IoT and non-AWS edge devices
+ Virtual machines (VMs), including VMs in other cloud environments

For information about AWS support for hybrid and multicloud environments, see [AWS Solutions for Hybrid and Multicloud](https://aws.amazon.com/hybrid-multicloud/).