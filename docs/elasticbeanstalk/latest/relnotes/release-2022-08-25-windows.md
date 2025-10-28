# Release: Elastic Beanstalk Windows Server platform update on August 25, 2022

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates framework and AWS components.

**Release date:** August 25, 2022

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows security updates** | Applied August 2022 security updates for Windows. See the Microsoft [Security Update Guide](https://msrc.microsoft.com/update-guide/en-us "https://msrc.microsoft.com/update-guide/en-us"). |
| **Framework updates**        |
| **Framework**                | **Details**                                                                                                                                                                                 |
| ---                          | ---                                                                                                                                                                                         |
| **.NET Core**                | Updated .NET 6 to version 6.0.8 on Windows Server 2019 and 2016 platform versions. Updated .NET 3 to version 3.1.28 on Windows Server 2019 and 2016 platform versions.                      |
|                              | **AWS component updates**                                                                                                                                                                   |
| **Component**                | **Details**                                                                                                                                                                                 |
| ---                          | ---                                                                                                                                                                                         |
| **AWS SDK for .NET**         | Updated the SDK to version 3.15.1737.                                                                                                                                                       |
| **AMI**                      | Updated the base AMI to version 2022.08.10.                                                                                                                                                 |
| **CloudWatch Agent**         | Updated the CloudWatch Agent to version 1.247354.0b251981.                                                                                                                                  |
| **SSM Agent**                | Updated the SSM Agent to version 3.1.1634.0 on Windows Server 2019 and 2016 platform versions.                                                                                              |
| **EC2Launch**                | Updated EC2Launch V2 to version 2.0.863.                                                                                                                                                    |

| ## New platform versions ### .NET on Windows Server #### Configuration basics
| Platform Version | Solution Stack Name | Framework | Proxy Server |
| --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.10.3** | _64bit Windows Server 2019 v2.10.3 running IIS 10.0_ | .NET 6.0.8, supports 6.0.8, 5.0.17, 3.1.28 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.3** | _64bit Windows Server Core 2019 v2.10.3 running IIS 10.0_ | .NET 6.0.8, supports 6.0.8, 5.0.17, 3.1.28 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2016 with IIS 10.0 version 2.10.3** | _64bit Windows Server 2016 v2.10.3 running IIS 10.0_ | .NET 6.0.8, supports 6.0.8, 5.0.17, 3.1.28 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.3** | _64bit Windows Server Core 2016 v2.10.3 running IIS 10.0_ | .NET 6.0.8, supports 6.0.8, 5.0.17, 3.1.28 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.3** | _64bit Windows Server 2012 R2 v2.10.3 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.3** | _64bit Windows Server Core 2012 R2 v2.10.3 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | #### More details
| Platform Version | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --- | --- | --- | --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.10.3** | 2022.08.10 | 3.15.1737 | | 3.1.1634.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.3** | 2022.08.10 | 3.15.1737 | | 3.1.1634.0 | 3.6 | 3.2.0 |
| **Windows Server 2016 with IIS 10.0 version 2.10.3** | 2022.08.10 | 3.15.1737 | | 3.1.1634.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.3** | 2022.08.10 | 3.15.1737 | | 3.1.1634.0 | 3.6 | 3.2.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.3** | 2022.08.10 | 3.15.1737 | | 3.1.1188.0 | 3.6 | 3.2.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.3** | 2022.08.10 | 3.15.1737 | 4.9.4588 | 3.1.1188.0 | 3.6 | 3.2.0 |
