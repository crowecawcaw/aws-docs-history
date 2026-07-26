# Release: Elastic Beanstalk Windows Server platform update on July 24, 2026

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** July 24, 2026

## Changes

The following table lists the changes included in this release.

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Windows security updates** | Applied July 2026 security updates for Windows.<br>This release includes updates from the monthly Microsoft *Patch Tuesday<br>• Windows release. Windows security updates in<br>this release are current up to the second Tuesday of the month.<br>For more details and a list of security updates, see the Microsoft [Security<br>Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *_Framework_<br>• | *_Details_<br>• | <br> | --<br>• | --<br>• | <br> | *_.NET Core_<br>• | Updated .NET 10 to version [10.0.10](https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.10/10.0.10.md "https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.10/10.0.10.md").<br>Updated .NET 9 to version [9.0.18](https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.18/9.0.18.md "https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.18/9.0.18.md").<br>Updated .NET 8 to version [8.0.29](https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.29/8.0.29.md "https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.29/8.0.29.md"). |      |
| **AWS component updates**    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *_Component_<br>• | *_Details_<br>• | <br> | --<br>• | --<br>• | <br> | *_AMI_<br>•       | Updated the base AMI to version 2026.07.15.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | <br> | *_SSM Agent_<br>• | Updated the SSM Agent to version [3.3.4793.0](https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.4793.0 "https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.4793.0"). | <br> | *_X-Ray daemon_<br>• | Updated the X-Ray daemon to version [3.6.6](https://github.com/aws/aws-xray-daemon/releases/tag/v3.6.6 "https://github.com/aws/aws-xray-daemon/releases/tag/v3.6.6"). |     |

## New platform versions

###### These platforms are updated:

- [.NET on Windows Server](#release-2026-07-24-windows.platforms.net "#release-2026-07-24-windows.platforms.net")

### .NET on Windows Server

#### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                                 | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.23.3**      | _64bit Windows Server 2025 v2.23.3 running IIS 10.0_      | .NET 10.0.10, supports 10.0.10, 9.0.18, 8.0.29<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.23.3** | _64bit Windows Server Core 2025 v2.23.3 running IIS 10.0_ | .NET 10.0.10, supports 10.0.10, 9.0.18, 8.0.29<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.23.3**      | _64bit Windows Server 2022 v2.23.3 running IIS 10.0_      | .NET 10.0.10, supports 10.0.10, 9.0.18, 8.0.29<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.23.3** | _64bit Windows Server Core 2022 v2.23.3 running IIS 10.0_ | .NET 10.0.10, supports 10.0.10, 9.0.18, 8.0.29<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.23.3**      | _64bit Windows Server 2019 v2.23.3 running IIS 10.0_      | .NET 10.0.10, supports 10.0.10, 9.0.18, 8.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.23.3** | _64bit Windows Server Core 2019 v2.23.3 running IIS 10.0_ | .NET 10.0.10, supports 10.0.10, 9.0.18, 8.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.23.3**      | _64bit Windows Server 2016 v2.23.3 running IIS 10.0_      | .NET 10.0.10, supports 10.0.10, 9.0.18, 8.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.23.3** | _64bit Windows Server Core 2016 v2.23.3 running IIS 10.0_ | .NET 10.0.10, supports 10.0.10, 9.0.18, 8.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

#### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Launch | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.23.3**      | 2026.07.15  |                  | 2.5.1     | 3.3.4793.0 | 4.0        | 3.6.6     |
| **Windows Server Core 2025 with IIS 10.0 version 2.23.3** | 2026.07.15  |                  | 2.5.1     | 3.3.4793.0 | 4.0        | 3.6.6     |
| **Windows Server 2022 with IIS 10.0 version 2.23.3**      | 2026.07.15  | 3.7.1252.1       | 2.5.1     | 3.3.4793.0 | 4.0        | 3.6.6     |
| **Windows Server Core 2022 with IIS 10.0 version 2.23.3** | 2026.07.15  | 3.7.1252.1       | 2.5.1     | 3.3.4793.0 | 4.0        | 3.6.6     |
| **Windows Server 2019 with IIS 10.0 version 2.23.3**      | 2026.07.15  | 3.7.1252.1       | 2.5.1     | 3.3.4793.0 | 4.0        | 3.6.6     |
| **Windows Server Core 2019 with IIS 10.0 version 2.23.3** | 2026.07.15  | 3.7.1252.1       | 2.5.1     | 3.3.4793.0 | 4.0        | 3.6.6     |
| **Windows Server 2016 with IIS 10.0 version 2.23.3**      | 2026.07.15  | 3.7.1252.1       | 2.5.1     | 3.3.4793.0 | 4.0        | 3.6.6     |
| **Windows Server Core 2016 with IIS 10.0 version 2.23.3** | 2026.07.15  | 3.7.1252.1       | 2.5.1     | 3.3.4793.0 | 4.0        | 3.6.6     |
