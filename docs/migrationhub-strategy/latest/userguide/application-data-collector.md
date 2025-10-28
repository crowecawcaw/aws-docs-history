AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Strategy Recommendations application data collector

This section describes how to use the Strategy Recommendations application data collector.

For information about downloading and setting up an application data collector, see [Step 1: Download the Strategy Recommendations
collector](getting-started-dowmload-collector.md "getting-started-dowmload-collector.md").

###### Topics

- [Data collected by the
  collector](#data-collected-by-collector "#data-collected-by-collector")
- [Upgrading the collector](#upgrade-collector "#upgrade-collector")

## Data collected by the Strategy Recommendations

collector

This section describes the type of data that the Migration Hub Strategy Recommendations application data collector
collects. An application data collector is an agentless data collector that identifies
running applications on your servers, performs source code analysis, and analyzes your
databases.

| Data field                       | Description                                                                                                                |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| OS type                          | Windows or Linux                                                                                                           |
| OS version                       | The specific version of the OS. For example, Windows Server 2003, RHEL 5.2.                                                |
| OS architecture                  | 32-bit or 64-bit OS                                                                                                        |
| Is Server VM                     | The server is a VM or a physical machine.                                                                                  |
| Virtualization software          | For example, vCenter, Hyper-V.                                                                                             |
| Location                         | For example, Amazon Elastic Compute Cloud console (Amazon EC2), or on-premises.                                            |
| Is dualBoot                      | Allows booting into multiple OSs                                                                                           |
| Firmware type                    | BIOS, UEFI                                                                                                                 |
| Boot loader                      | GRUB, GRUB 2                                                                                                               |
| Partition table type             | MBR, GPT                                                                                                                   |
| CPU speed                        | CPU speed in GHz. For example, 2.4 GHz.                                                                                    |
| **Windows OS data**              |
| Windows Edition                  | Standard, Data Center, Enterprise                                                                                          |
| .NET framework version           | The version of the .NET framework installed.                                                                               |
| .NET Core version                | The version of .NET Core installed.                                                                                        |
| **Linux data**                   |
| Linux OS distribution            | RHEL, CentOS, SUSE, and so on.                                                                                             |
| Kernel version                   | uname -r output, such as `4.9.217-0.1.ac.205.84.332.metal1.x86_64`                                                         |
| **For each disk volume**         |
| File system type                 | FAT32, NTFS, ReFS, ext4, jfs, and so on.                                                                                   |
| Disk volume size                 | Total disk size                                                                                                            |
| Disk volume free space           | Free disk space                                                                                                            |
| Virtual disk image format        | vmdk, vhd, vhdx                                                                                                            |
| Disk type (Windows)              | Basic, Dynamic                                                                                                             |
| **Application level data**       |                                                                                                                            | Application name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The name of the running process. For example, SQLServr.exe, MSdtsservr.exe, and so on. |
| Application type                 | IIS, JBoss, Tomcat, and so on.                                                                                             |
| Programming language & version   | C#, Java                                                                                                                   |
| JDK version                      | The version of the JDK installed.                                                                                          |
| Is source code available         | If you provide a source code repository, it indicates that source code is available.                                       |
| Application bit size             | 16-bit, 32-bit, 64-bit                                                                                                     |
| **Windows**                      |                                                                                                                            | .NET framework version used by app                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | The version of the .NET framework DLL being loaded at runtime for the application.     |
| .NET Core version                | The version .NET Core DLL being loaded at runtime for the application.                                                     |
| Uses WPF framework ?             | Determines if the .NET based application is a type of WPF app or not.                                                      |
| Uses WCF framework ?             | Determines if the .NET based application is a type of WCF app or not.                                                      |
| ASP.NET version                  | The version of ASP.NET.                                                                                                    |
| IIS version                      | The version of IIS server installed on the Windows machine.                                                                |
| Application OS drivers bit size  | 32-bit, 64-bit                                                                                                             |
| Windows registry usage           | Queries the registry keys of the machine to find information like database version, Java version, .NET version, and so on. |
| All DLLs used by the application | Fetches the list of all the DLLs loaded at runtime by a Windows process.                                                   |
| PowerShell version               | Checks the PowerShell version installed on the machine, which should be 5.1 or later.                                      |
| **Linux**                        |
| Application framework type       | Tomcat, Spring Boot, JBoss, WebLogic, WebSphere                                                                            |
| Application framework version    | The version of the application framework.                                                                                  |
| **Database**                     |
| Database type                    | MS SQL, Oracle, MySQL, and so on.                                                                                          |
| Database version                 | The version of the database.                                                                                               | ### Remove your data from Strategy Recommendations To have all your data removed from Strategy Recommendations, contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") and request full data deletion. ## Upgrading the Strategy Recommendations collector The Migration Hub Strategy Recommendations application data collector upgrades automatically. You can use the following procedure to manually upgrade the collector, if needed. ###### To upgrade the Strategy Recommendations collector 1. Use the following command to connect to the collector VM using an SSH client. `` ssh ec2-user@`CollectorIPAddress` `` 2. Change to the upgrade directory in the collector VM as shown in the following example. `cd  /home/ec2-user/collector/upgrades` 3. Use the following command to run the upgrade script. `sudo bash application-data-collector-upgrade` |
