# Release: Elastic Beanstalk Windows Server platform update on January 18, 2024

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates AWS components.

**Release date:** January 18, 2024

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows security updates** | Applied January 2024 security updates for Windows. This release includes updates from the monthly Microsoft _Patch Tuesday_ Windows release. Windows security updates in this release are current up to the second Tuesday of the month. For more details and a list of security updates, see the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |
| **Framework**                | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **.NET Core**                | Updated .NET 6 to version 6.0.26. Updated .NET 8 to version 8.0.1.                                                                                                                                                                                                                                                                                                                                                                                          |
|                              | **AWS component updates**                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Component**                | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **AMI**                      | Updated the base AMI to version 2024.01.10.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **AWS SDK for .NET**         | Updated the SDK to version 3.7.722.0.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **CloudWatch Agent**         | Updated the CloudWatch Agent to version 1.300032.3b392.                                                                                                                                                                                                                                                                                                                                                                                                     |
| **EC2Launch**                | Updated EC2Launch V2 to version 2.0.1702.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **AWSPowershell**            | Updated AWSPowershell to version 4.1.486.                                                                                                                                                                                                                                                                                                                                                                                                                   |

| ## New platform versions ### .NET on Windows Server #### Configuration basics
| Platform Version | Solution Stack Name | Framework | Proxy Server |
| --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.13.2** | _64bit Windows Server 2019 v2.13.2 running IIS 10.0_ | .NET 8.0.1, supports 8.0.1, 6.0.26 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.13.2** | _64bit Windows Server Core 2019 v2.13.2 running IIS 10.0_ | .NET 8.0.1, supports 8.0.1, 6.0.26 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2016 with IIS 10.0 version 2.13.2** | _64bit Windows Server 2016 v2.13.2 running IIS 10.0_ | .NET 8.0.1, supports 8.0.1, 6.0.26 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.13.2** | _64bit Windows Server Core 2016 v2.13.2 running IIS 10.0_ | .NET 8.0.1, supports 8.0.1, 6.0.26 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | #### More details
| Platform Version | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --- | --- | --- | --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.13.2** | 2024.01.10 | 3.7.722.0 | | 3.2.1705.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.13.2** | 2024.01.10 | 3.7.722.0 | | 3.2.1705.0 | 3.6 | 3.2.0 |
| **Windows Server 2016 with IIS 10.0 version 2.13.2** | 2024.01.10 | 3.7.722.0 | | 3.2.1705.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.13.2** | 2024.01.10 | 3.7.722.0 | | 3.2.1705.0 | 3.6 | 3.2.0 |
