

# Windows operating systems supported by Elastic Disaster Recovery
<a name="Supported-Operating-Systems-Windows"></a>

AWS Elastic Disaster Recovery allows replication of physical, virtual or cloud-based source servers to the AWS Cloud for several versions of Windows. 

## General Notes
<a name="General-Notes"></a>

**Important**  
**Windows 2003** is no longer supported.

[Review the AWS Replication Agent installation requirements.](installation-requirements.md)

**These Windows operating systems are supported:**


| Operating system | Supported versions | Prerequisites and Limitations | 
| --- | --- | --- | 
| Microsoft Windows Server 2025 64-bit |  | Requires .NET Framework version 4.5 or above.  | 
| Microsoft Windows Server 2022 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  | 
| Microsoft Windows Server 2019 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  | 
| Microsoft Windows Server 2016 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  | 
| Microsoft Windows 10 64-bit |   | Ensure that the [auto sleep function in Windows 10](https://answers.microsoft.com/en-us/windows/forum/all/turn-off-auto-sleep-in-windows-10/79f2d86c-3378-495f-8da2-4d78021876d4) is disabled. Data replication may be interrupted if the feature is activated. | 
| Microsoft Windows Server 2012 <br />**This version has reached end of life. We recommend that you update to a more recent version.** | 64-bit and R2 64-bit |  + Microsoft Windows Server version 2012 uses a version of the AWS Replication Agent, AwsReplicationWindows2012LegacyInstaller.exe, that is only valid for that version. You can download it from `https://aws-elastic-disaster-recovery-<REGION>.s3.amazonaws.com/latest/windows_legacy/windows_2012_legacy/AwsReplicationWindows2012LegacyInstaller.exe` . Replace `<REGION>` with the AWS Region into which you are replicating. <br />+ Requires .Net Framework version 4.5 or above to be installed by the end user.   | 
| Microsoft Windows Server 2008 <br />**This version has reached end of life. We recommend that you update to a more recent version.** | 64-bit and R2 64-bit | + Windows Server 2008 requires .Net Framework version 3.5 to be installed by the end user. <br />Windows Server 2008 **R2** requires .Net Framework version 4.5 or above to be installed by the end user.<br />+ Windows 2008 x64 requires SP2 and other Microsoft updates to support the SHA-2 signature of the AWS Replication Agent driver.<br />+ The AWS Replication Agent and agent installer requires a separate installer file, `AwsReplicationWindowsLegacyInstaller.exe` for end-of-life versions of Windows because they use older versions of software components that cannot be upgraded.<br />+  **Windows Server 2008 and Windows Server 2008 R2 with GPT-partitioned system disks (UEFI boot) are not supported.** These operating systems must use an MBR-partitioned system disk (BIOS boot) for recovery. <br />+  [Nitro instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) can only be used with Windows Server 2008 R2 and upwards. Earlier versions are not supported. <br />+  A shutdown (from the OS menu or Windows CLI) of a Windows source server triggers a rescan in AWS DRS once the source server is restarted.   | 
| Microsoft Windows 7 64-bit<br />**This version has reached end of life. We recommend that you update to a more recent version.** |  |  + The AWS Replication Agent and agent installer requires a separate installer file, `AwsReplicationWindowsLegacyInstaller.exe` for end-of-life versions of Windows because they use older versions of software components that cannot be upgraded.<br />+  [Nitro instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) can only be used with Windows Server 2008 R2 and upwards. Earlier versions are not supported.<br />+  A shutdown (from the OS menu or Windows CLI) of a Windows source server triggers a rescan in AWS DRS once the source server is restarted.   | 