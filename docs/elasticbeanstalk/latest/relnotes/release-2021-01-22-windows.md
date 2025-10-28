# Release: Elastic Beanstalk Windows Server platform update on January 22, 2021

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates framework and AWS components.

**Release date:** January 22, 2021

## Changes

The following table lists the changes included in this release.

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows security updates** | Applied January 2021 and December 2020 security updates for Windows. See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |
| **Framework**                | **Details**                                                                                                                                                                                                                            |
| ---                          | ---                                                                                                                                                                                                                                    |
| **.NET Core**                | Updated .NET Core 2.1 to version 2.1.24. Updated .NET Core 3 to version 3.1.11 on Windows Server 2019 and 2016 platform versions. Updated .NET 5 to version 5.0.2 on Windows Server 2019 and 2016 platform versions.                   |
|                              | **AWS component updates**                                                                                                                                                                                                              |
| **Component**                | **Details**                                                                                                                                                                                                                            |
| ---                          | ---                                                                                                                                                                                                                                    |
| **AWS SDK for .NET**         | Updated the SDK to version 3.15.1204.                                                                                                                                                                                                  |
| **AMI**                      | Updated the base AMI to version 2021.01.13.                                                                                                                                                                                            |
| **SSM Agent**                | Updated the SSM Agent to version 3.0.431.0 on Windows Server 2019 and 2016 platform versions.                                                                                                                                          |
| **CloudWatch Agent**         | Updated the CloudWatch Agent to version 1.247347.3.                                                                                                                                                                                    |

| ## New platform versions ### .NET on Windows Server #### Configuration basics
| Platform Version | Solution Stack Name | Framework | Proxy Server |
| --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.6.2** | _64bit Windows Server 2019 v2.6.2 running IIS 10.0_ | .NET 5.0.2, supports 5.0.2, 3.1.11, 2.2.8, 2.1.24 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.2** | _64bit Windows Server Core 2019 v2.6.2 running IIS 10.0_ | .NET 5.0.2, supports 5.0.2, 3.1.11, 2.2.8, 2.1.24 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2016 with IIS 10.0 version 2.6.2** | _64bit Windows Server 2016 v2.6.2 running IIS 10.0_ | .NET 5.0.2, supports 5.0.2, 3.1.11, 2.2.8, 2.1.24 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.2** | _64bit Windows Server Core 2016 v2.6.2 running IIS 10.0_ | .NET 5.0.2, supports 5.0.2, 3.1.11, 2.2.8, 2.1.24 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.2** | _64bit Windows Server 2012 R2 v2.6.2 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.24 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.2** | _64bit Windows Server Core 2012 R2 v2.6.2 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.24 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | #### More details
| Platform Version | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X‑Ray |
| --- | --- | --- | --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.6.2** | 2021.01.13 | 3.15.1204 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.431.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.2** | 2021.01.13 | 3.15.1204 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.431.0 | 3.6 | 3.2.0 |
| **Windows Server 2016 with IIS 10.0 version 2.6.2** | 2021.01.13 | 3.15.1204 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.431.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.2** | 2021.01.13 | 3.15.1204 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.431.0 | 3.6 | 3.2.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.2** | 2021.01.13 | 3.15.1204 | 4.9.4279 | 2.3.871.0 | 3.6 | 3.2.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.2** | 2021.01.13 | 3.15.1204 | 4.9.4279 | 2.3.871.0 | 3.6 | 3.2.0 |
