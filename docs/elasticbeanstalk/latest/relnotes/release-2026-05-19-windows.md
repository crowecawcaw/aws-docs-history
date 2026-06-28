# Release: Elastic Beanstalk Windows Server platform update on May 19, 2026

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components. Windows Server 2016 platforms are now in retiring status.

**Release date:** May 19, 2026

## Changes

The following table lists the changes included in this release.

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows security updates** | Applied May 2026 security updates for Windows.<br>This release includes updates from the monthly Microsoft *Patch Tuesday<br>• Windows release. Windows security updates in<br>this release are current up to the second Tuesday of the month.<br>For more details and a list of security updates, see the Microsoft [Security<br>Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Platform retirement**      | The *_Windows Server 2016 with IIS 10.0_<br>• and **Windows Server Core 2016 with IIS 10.0**<br>platform branches are now in *retiring<br>• status. These platforms reach end of life on<br>**September 30, 2026**. We recommend that you migrate your environments to a supported Windows Server platform branch<br>before the retirement date.                                                                                                                        |
| **Framework updates**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *_Framework_<br>• | *_Details_<br>• | <br> | --<br>• | --<br>• | <br> | *_.NET Core_<br>• | Updated .NET 10 to version [10.0.8](https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.8/10.0.8.md "https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.8/10.0.8.md").<br>Updated .NET 9 to version [9.0.16](https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.16/9.0.16.md "https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.16/9.0.16.md").<br>Updated .NET 8 to version [8.0.27](https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.27/8.0.27.md "https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.27/8.0.27.md"). |      |
| **AWS component updates**    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *_Component_<br>• | *_Details_<br>• | <br> | --<br>• | --<br>• | <br> | *_AMI_<br>•       | Updated the base AMI to version 2026.05.13.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | <br> | *_AWS SDK for .NET_<br>• | Updated the SDK to version [3.7.1251.1](https://github.com/aws/aws-sdk-net/releases/tag/3.7.1251.1 "https://github.com/aws/aws-sdk-net/releases/tag/3.7.1251.1"). | <br> | *_CloudWatch Agent_<br>• | Updated the CloudWatch Agent to version [1.300067.0b1404](https://github.com/aws/amazon-cloudwatch-agent/releases/tag/v1.300067.0 "https://github.com/aws/amazon-cloudwatch-agent/releases/tag/v1.300067.0"). | <br> | *_EC2Launch_<br>• | Updated EC2Launch to version 2.5.0. | <br> | *_SSM Agent_<br>• | Updated the SSM Agent to version [3.3.4268.0](https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.4268.0 "https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.4268.0"). | <br> | *_X-Ray daemon_<br>• | Updated the X-Ray daemon to version [3.6.3](https://github.com/aws/aws-xray-daemon/releases/tag/v3.6.3 "https://github.com/aws/aws-xray-daemon/releases/tag/v3.6.3"). |     |

## New platform versions

###### These platforms are updated:

- [.NET on Windows Server](#release-2026-05-19-windows.platforms.net "#release-2026-05-19-windows.platforms.net")

### .NET on Windows Server

#### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                               | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.23.1**      | _64bit Windows Server 2025 v2.23.1 running IIS 10.0_      | .NET 10.0.8, supports 10.0.8, 9.0.16, 8.0.27<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.23.1** | _64bit Windows Server Core 2025 v2.23.1 running IIS 10.0_ | .NET 10.0.8, supports 10.0.8, 9.0.16, 8.0.27<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.23.1**      | _64bit Windows Server 2022 v2.23.1 running IIS 10.0_      | .NET 10.0.8, supports 10.0.8, 9.0.16, 8.0.27<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.23.1** | _64bit Windows Server Core 2022 v2.23.1 running IIS 10.0_ | .NET 10.0.8, supports 10.0.8, 9.0.16, 8.0.27<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.23.1**      | _64bit Windows Server 2019 v2.23.1 running IIS 10.0_      | .NET 10.0.8, supports 10.0.8, 9.0.16, 8.0.27<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.23.1** | _64bit Windows Server Core 2019 v2.23.1 running IIS 10.0_ | .NET 10.0.8, supports 10.0.8, 9.0.16, 8.0.27<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.23.1**      | _64bit Windows Server 2016 v2.23.1 running IIS 10.0_      | .NET 10.0.8, supports 10.0.8, 9.0.16, 8.0.27<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.23.1** | _64bit Windows Server Core 2016 v2.23.1 running IIS 10.0_ | .NET 10.0.8, supports 10.0.8, 9.0.16, 8.0.27<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

#### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Launch | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.23.1**      | 2026.05.13  | 3.7.1251.1       | 2.5.0     | 3.3.4268.0 | 4.0        | 3.6.3     |
| **Windows Server Core 2025 with IIS 10.0 version 2.23.1** | 2026.05.13  | 3.7.1251.1       | 2.5.0     | 3.3.4268.0 | 4.0        | 3.6.3     |
| **Windows Server 2022 with IIS 10.0 version 2.23.1**      | 2026.05.13  | 3.7.1251.1       | 2.5.0     | 3.3.4268.0 | 4.0        | 3.6.3     |
| **Windows Server Core 2022 with IIS 10.0 version 2.23.1** | 2026.05.13  | 3.7.1251.1       | 2.5.0     | 3.3.4268.0 | 4.0        | 3.6.3     |
| **Windows Server 2019 with IIS 10.0 version 2.23.1**      | 2026.05.13  | 3.7.1251.1       | 2.5.0     | 3.3.4268.0 | 4.0        | 3.6.3     |
| **Windows Server Core 2019 with IIS 10.0 version 2.23.1** | 2026.05.13  | 3.7.1251.1       | 2.5.0     | 3.3.4268.0 | 4.0        | 3.6.3     |
| **Windows Server 2016 with IIS 10.0 version 2.23.1**      | 2026.05.13  | 3.7.1251.1       | 2.5.0     | 3.3.4268.0 | 4.0        | 3.6.3     |
| **Windows Server Core 2016 with IIS 10.0 version 2.23.1** | 2026.05.13  | 3.7.1251.1       | 2.5.0     | 3.3.4268.0 | 4.0        | 3.6.3     |
