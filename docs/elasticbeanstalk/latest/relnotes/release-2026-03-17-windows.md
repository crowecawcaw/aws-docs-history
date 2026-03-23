# Release: Elastic Beanstalk Windows Server platform update on March 17, 2026

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates framework and AWS components.

**Release date:** March 17, 2026

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------ | ------------------------------------------------------------------------------------------------------------ | ---- | ------------------------- | -------------------------------------- | ---- | ------------------------- | -------------------------------------------------------- | ---- | ------------------ | ------------------------------------- | ---- | ------------------ | -------------------------------------------- | --- |
| **Windows security updates** | Applied March 2026 security updates for Windows.<br>This release includes updates from the monthly Microsoft \*Patch Tuesday<br>• Windows release. Windows security updates in<br>this release are current up to the second Tuesday of the month.<br>For more details and a list of security updates, see the Microsoft [Security<br>Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_.NET Core_<br>• | Updated .NET 9 to version 9.0.14.<br>Updated .NET 8 to version 8.0.25.<br>Updated .NET 10 to version 10.0.5. |      |
| **AWS component updates**    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AMI_<br>•       | Updated the base AMI to version 2026.03.11.                                                                  | <br> | \*_AWS SDK for .NET_<br>• | Updated the SDK to version 3.7.1239.0. | <br> | \*_CloudWatch Agent_<br>• | Updated the CloudWatch Agent to version 1.300064.1b1344. | <br> | \*_EC2Launch_<br>• | Updated EC2Launch to version 2.4.0.0. | <br> | \*_SSM Agent_<br>• | Updated the SSM Agent to version 3.3.3883.0. |     |

## New platform versions

###### These platforms are updated:

- [.NET on Windows Server](#release-2026-03-17-windows.platforms.net "#release-2026-03-17-windows.platforms.net")

### .NET on Windows Server

#### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                               | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.22.3**      | _64bit Windows Server 2025 v2.22.3 running IIS 10.0_      | .NET 9.0.14, supports 9.0.14, 8.0.25, 10.0.5<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.22.3** | _64bit Windows Server Core 2025 v2.22.3 running IIS 10.0_ | .NET 9.0.14, supports 9.0.14, 8.0.25, 10.0.5<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.22.3**      | _64bit Windows Server 2022 v2.22.3 running IIS 10.0_      | .NET 9.0.14, supports 9.0.14, 8.0.25, 10.0.5<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.22.3** | _64bit Windows Server Core 2022 v2.22.3 running IIS 10.0_ | .NET 9.0.14, supports 9.0.14, 8.0.25, 10.0.5<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.22.3**      | _64bit Windows Server 2019 v2.22.3 running IIS 10.0_      | .NET 9.0.14, supports 9.0.14, 8.0.25, 10.0.5<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.22.3** | _64bit Windows Server Core 2019 v2.22.3 running IIS 10.0_ | .NET 9.0.14, supports 9.0.14, 8.0.25, 10.0.5<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.22.3**      | _64bit Windows Server 2016 v2.22.3 running IIS 10.0_      | .NET 9.0.14, supports 9.0.14, 8.0.25, 10.0.5<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.22.3** | _64bit Windows Server Core 2016 v2.22.3 running IIS 10.0_ | .NET 9.0.14, supports 9.0.14, 8.0.25, 10.0.5<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

#### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Launch | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.22.3**      | 2026.03.11  | 3.7.1239.0       | 2.4.0.0   | 3.3.3883.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2025 with IIS 10.0 version 2.22.3** | 2026.03.11  | 3.7.1239.0       | 2.4.0.0   | 3.3.3883.0 | 4.0        | 3.6.1     |
| **Windows Server 2022 with IIS 10.0 version 2.22.3**      | 2026.03.11  | 3.7.1239.0       | 2.4.0.0   | 3.3.3883.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2022 with IIS 10.0 version 2.22.3** | 2026.03.11  | 3.7.1239.0       | 2.4.0.0   | 3.3.3883.0 | 4.0        | 3.6.1     |
| **Windows Server 2019 with IIS 10.0 version 2.22.3**      | 2026.03.11  | 3.7.1239.0       | 2.4.0.0   | 3.3.3883.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2019 with IIS 10.0 version 2.22.3** | 2026.03.11  | 3.7.1239.0       | 2.4.0.0   | 3.3.3883.0 | 4.0        | 3.6.1     |
| **Windows Server 2016 with IIS 10.0 version 2.22.3**      | 2026.03.11  | 3.7.1239.0       | 2.4.0.0   | 3.3.3883.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2016 with IIS 10.0 version 2.22.3** | 2026.03.11  | 3.7.1239.0       | 2.4.0.0   | 3.3.3883.0 | 4.0        | 3.6.1     |
