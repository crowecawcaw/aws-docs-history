# Release: Elastic Beanstalk Windows Server platform update on October 16, 2024

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates and
updates AWS components.

**Release date:** October 16, 2024

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
| **Windows security updates** | Applied October 2024 security updates for Windows. This release includes updates from the monthly Microsoft _Patch Tuesday_ Windows release. Windows security updates in this release are current up to the second Tuesday of the month. For more details and a list of security updates, see the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |
| **Framework**                | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **.NET Core**                | Updated .NET 6 to version 6.0.35. Updated .NET 8 to version 8.0.10.                                                                                                                                                                                                                                                                                                                                                                                         |
|                              | **AWS component updates**                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Component**                | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **AMI**                      | Updated the base AMI to version 2024.10.09.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **AWS SDK for .NET**         | Updated the SDK to version 3.7.901.0.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **EC2Launch**                | Updated EC2Launch V2 to version 2.0.2046.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **SSM Agent**                | Updated the SSM Agent to version 3.3.859.0.                                                                                                                                                                                                                                                                                                                                                                                                                 |

| ## New platform versions ### .NET on Windows Server #### Configuration basics
| Platform Version | Solution Stack Name | Framework | Proxy Server |
| --- | --- | --- | --- |
| **Windows Server 2022 with IIS 10.0 version 2.15.6** | _64bit Windows Server 2022 v2.15.6 running IIS 10.0_ | .NET 8.0.10, supports 8.0.10, 6.0.35 .NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.6** | _64bit Windows Server Core 2022 v2.15.6 running IIS 10.0_ | .NET 8.0.10, supports 8.0.10, 6.0.35 .NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
| **Windows Server 2019 with IIS 10.0 version 2.15.6** | _64bit Windows Server 2019 v2.15.6 running IIS 10.0_ | .NET 8.0.10, supports 8.0.10, 6.0.35 .NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.6** | _64bit Windows Server Core 2019 v2.15.6 running IIS 10.0_ | .NET 8.0.10, supports 8.0.10, 6.0.35 .NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
| **Windows Server 2016 with IIS 10.0 version 2.15.6** | _64bit Windows Server 2016 v2.15.6 running IIS 10.0_ | .NET 8.0.10, supports 8.0.10, 6.0.35 .NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.6** | _64bit Windows Server Core 2016 v2.15.6 running IIS 10.0_ | .NET 8.0.10, supports 8.0.10, 6.0.35 .NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | #### More details
| Platform Version | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --- | --- | --- | --- | --- | --- | --- |
| **Windows Server 2022 with IIS 10.0 version 2.15.6** | 2024.10.09 | 3.7.901.0 | | 3.3.859.0 | 3.6 | 3.3.13 |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.6** | 2024.10.09 | 3.7.901.0 | | 3.3.859.0 | 3.6 | 3.3.13 |
| **Windows Server 2019 with IIS 10.0 version 2.15.6** | 2024.10.09 | 3.7.901.0 | | 3.3.859.0 | 3.6 | 3.3.13 |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.6** | 2024.10.09 | 3.7.901.0 | | 3.3.859.0 | 3.6 | 3.3.13 |
| **Windows Server 2016 with IIS 10.0 version 2.15.6** | 2024.10.09 | 3.7.901.0 | | 3.3.859.0 | 3.6 | 3.3.13 |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.6** | 2024.10.09 | 3.7.901.0 | | 3.3.859.0 | 3.6 | 3.3.13 |
