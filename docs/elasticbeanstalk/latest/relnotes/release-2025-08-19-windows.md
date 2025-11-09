# Release: Elastic Beanstalk Windows Server platform update on August 19, 2025

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates framework and AWS components.

**Release date:** August 19, 2025

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------ | --------------------------------------------------------------------- | ---- | ------------------------- | -------------------------------------- | ---- | ------------------------- | -------------------------------------------------------- | ---- | ------------------ | --------------------------------------- | ---- | ------------------ | -------------------------------------------- | --- |
| **Windows security updates** | Applied August 2025 security updates for Windows.<br>This release includes updates from the monthly Microsoft \*Patch Tuesday<br>• Windows release. Windows security updates in<br>this release are current up to the second Tuesday of the month.<br>For more details and a list of security updates, see the Microsoft [Security<br>Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_.NET Core_<br>• | Updated .NET 9 to version 9.0.8.<br>Updated .NET 8 to version 8.0.19. |      |
| **AWS component updates**    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AMI_<br>•       | Updated the base AMI to version 2025.08.13.                           | <br> | \*_AWS SDK for .NET_<br>• | Updated the SDK to version 3.7.1101.0. | <br> | \*_CloudWatch Agent_<br>• | Updated the CloudWatch Agent to version 1.300057.1b1167. | <br> | \*_EC2Launch_<br>• | Updated EC2Launch V2 to version 2.2.63. | <br> | \*_SSM Agent_<br>• | Updated the SSM Agent to version 3.3.2656.0. |     |

## New platform versions

###### These platforms are updated:

- [.NET on Windows Server](#release-2025-08-19-windows.platforms.net "#release-2025-08-19-windows.platforms.net")

### .NET on Windows Server

#### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.19.4**      | _64bit Windows Server 2025 v2.19.4 running IIS 10.0_      | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.4** | _64bit Windows Server Core 2025 v2.19.4 running IIS 10.0_ | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.19.4**      | _64bit Windows Server 2022 v2.19.4 running IIS 10.0_      | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.4** | _64bit Windows Server Core 2022 v2.19.4 running IIS 10.0_ | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.19.4**      | _64bit Windows Server 2019 v2.19.4 running IIS 10.0_      | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.4** | _64bit Windows Server Core 2019 v2.19.4 running IIS 10.0_ | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.19.4**      | _64bit Windows Server 2016 v2.19.4 running IIS 10.0_      | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.4** | _64bit Windows Server Core 2016 v2.19.4 running IIS 10.0_ | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

#### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.19.4**      | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.4** | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server 2022 with IIS 10.0 version 2.19.4**      | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.4** | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server 2019 with IIS 10.0 version 2.19.4**      | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.4** | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server 2016 with IIS 10.0 version 2.19.4**      | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.4** | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
