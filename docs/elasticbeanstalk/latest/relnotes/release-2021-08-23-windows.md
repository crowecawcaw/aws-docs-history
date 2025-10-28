# Release: Elastic Beanstalk Windows Server platform update on August 23, 2021

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates framework and AWS components.

**Release date:** August 23, 2021

## Changes

The following table lists the changes included in this release.

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                      |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows security updates** | Applied August 2021 security updates for Windows. See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance").  |
| **Framework updates**        |
| **Framework**                | **Details**                                                                                                                                                                                                          |
| ---                          | ---                                                                                                                                                                                                                  |
| **.NET Core**                | Updated .NET Core 2.1 to version 2.1.29. Updated .NET Core 3 to version 3.1.18 on Windows Server 2019 and 2016 platform versions. Updated .NET 5 to version 5.0.9 on Windows Server 2019 and 2016 platform versions. |
|                              | **AWS component updates**                                                                                                                                                                                            |
| **Component**                | **Details**                                                                                                                                                                                                          |
| ---                          | ---                                                                                                                                                                                                                  |
| **AWS SDK for .NET**         | Updated the SDK to version 3.15.1371.                                                                                                                                                                                |
| **AMI**                      | Updated the base AMI to version 2021.08.11.                                                                                                                                                                          |
| **CloudWatch Agent**         | Updated the CloudWatch Agent to version 1.247349.0.                                                                                                                                                                  |

| ## New platform versions ### .NET on Windows Server #### Configuration basics
| Platform Version | Solution Stack Name | Framework | Proxy Server |
| --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.7.0** | _64bit Windows Server 2019 v2.7.0 running IIS 10.0_ | .NET 5.0.9, supports 5.0.9, 3.1.18, 2.1.29 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.7.0** | _64bit Windows Server Core 2019 v2.7.0 running IIS 10.0_ | .NET 5.0.9, supports 5.0.9, 3.1.18, 2.1.29 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2016 with IIS 10.0 version 2.7.0** | _64bit Windows Server 2016 v2.7.0 running IIS 10.0_ | .NET 5.0.9, supports 5.0.9, 3.1.18, 2.1.29 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.7.0** | _64bit Windows Server Core 2016 v2.7.0 running IIS 10.0_ | .NET 5.0.9, supports 5.0.9, 3.1.18, 2.1.29 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.7.0** | _64bit Windows Server 2012 R2 v2.7.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.1.29 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.7.0** | _64bit Windows Server Core 2012 R2 v2.7.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.1.29 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | #### More details
| Platform Version | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --- | --- | --- | --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.7.0** | 2021.08.11 | 3.15.1371 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.1124.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.7.0** | 2021.08.11 | 3.15.1371 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.1124.0 | 3.6 | 3.2.0 |
| **Windows Server 2016 with IIS 10.0 version 2.7.0** | 2021.08.11 | 3.15.1371 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.1124.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.7.0** | 2021.08.11 | 3.15.1371 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.1124.0 | 3.6 | 3.2.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.7.0** | 2021.08.11 | 3.15.1371 | 4.9.4419 | 3.0.1124.0 | 3.6 | 3.2.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.7.0** | 2021.08.11 | 3.15.1371 | 4.9.4419 | 3.0.1124.0 | 3.6 | 3.2.0 |
