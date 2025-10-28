# Release: Elastic Beanstalk Windows Server platform update on November 5, 2020

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates framework and AWS components.

**Release date:** November 5, 2020

## Changes

The following table lists the changes included in this release.

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                      |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows security updates** | Applied October 2020 security updates for Windows. See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |
| **Framework**                | **Details**                                                                                                                                                                                                          |
| ---                          | ---                                                                                                                                                                                                                  |
| **.NET Core**                | Updated .NET Core 2.1 to version 2.1.23. Updated .NET Core 3 to version 3.1.9 on Windows Server 2019 and 2016 platform versions.                                                                                     |
|                              | **AWS component updates**                                                                                                                                                                                            |
| **Component**                | **Details**                                                                                                                                                                                                          |
| ---                          | ---                                                                                                                                                                                                                  |
| **AWS SDK for .NET**         | Updated the SDK to version 3.15.1140.                                                                                                                                                                                |
| **AMI**                      | Updated the base AMI to version 2020.10.14.                                                                                                                                                                          |
| **CloudWatch Agent**         | Updated the CloudWatch Agent to version 1.247346.0b249609.                                                                                                                                                           |

| ## New platform versions ### .NET on Windows Server #### Configuration basics
| Platform Version | Solution Stack Name | Framework | Proxy Server |
| --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.5.11** | _64bit Windows Server 2019 v2.5.11 running IIS 10.0_ | .NET Core 3.1.9, supports 3.1.9, 2.2.8, 2.1.23 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.11** | _64bit Windows Server Core 2019 v2.5.11 running IIS 10.0_ | .NET Core 3.1.9, 2.2.8, 2.1.23, supports .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2016 with IIS 10.0 version 2.5.11** | _64bit Windows Server 2016 v2.5.11 running IIS 10.0_ | .NET Core 3.1.9, 2.2.8, 2.1.23, supports .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.11** | _64bit Windows Server Core 2016 v2.5.11 running IIS 10.0_ | .NET Core 3.1.9, 2.2.8, 2.1.23, supports .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.11** | _64bit Windows Server 2012 R2 v2.5.11 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.23 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.11** | _64bit Windows Server Core 2012 R2 v2.5.11 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.23 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | #### More details
| Platform Version | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X‑Ray |
| --- | --- | --- | --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.5.11** | 2020.10.14 | 3.15.1140 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.842.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.11** | 2020.10.14 | 3.15.1140 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.842.0 | 3.6 | 3.2.0 |
| **Windows Server 2016 with IIS 10.0 version 2.5.11** | 2020.10.14 | 3.15.1140 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.842.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.11** | 2020.10.14 | 3.15.1140 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.842.0 | 3.6 | 3.2.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.11** | 2020.10.14 | 3.15.1140 | 4.9.4222 | 2.3.842.0 | 3.6 | 3.2.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.11** | 2020.10.14 | 3.15.1140 | 4.9.4222 | 2.3.842.0 | 3.6 | 3.2.0 |
