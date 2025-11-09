# Release: Elastic Beanstalk Windows Server platform update on April 17, 2025

This release provides new Windows Server platform versions for AWS Elastic Beanstalk, Windows security updates, and updates framework and AWS components. This release removes support for .NET 6.

**Release date:** April 17, 2025

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------------- | -------------------------------------- | ---- | ------------------------- | -------------------------------------------------------- | ---- | ------------------ | ----------------------------------------- | ---- | ------------------ | -------------------------------------------- | ---- | --------------------------- | ------------------------------------------------------------- | ---- | ------------------------------ | ---------------------------------------------------------------------------------------------------- | --- |
| **Windows security updates** | Applied April 2025 security updates for Windows.<br>This release includes updates from the monthly Microsoft \*Patch Tuesday<br>• Windows release. Windows security updates in<br>this release are current up to the second Tuesday of the month.<br>For more details and a list of security updates, see the Microsoft [Security<br>Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_.NET Core_<br>• | Updated .NET 8 to version 8.0.15.<br>.NET 6 is being removed from all Windows Server platform versions because it's past Microsoft's end of support date. For<br>more information, see [.NET and .NET Core Support<br>Policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core "https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core") on the Microsoft website.<br>• Windows Server 2016, 2019, 2022 and 2025 platforms — .NET 6 removed |      |
| **AWS component updates**    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AMI_<br>•       | Updated the base AMI to version 2025.04.09.                                                                                                                                                                                                                                                                                                                                                                                                                                       | <br> | \*_AWS SDK for .NET_<br>• | Updated the SDK to version 3.7.1020.0. | <br> | \*_CloudWatch Agent_<br>• | Updated the CloudWatch Agent to version 1.300054.0b1074. | <br> | \*_EC2Launch_<br>• | Updated EC2Launch V2 to version 2.0.2107. | <br> | \*_SSM Agent_<br>• | Updated the SSM Agent to version 3.3.1957.0. | <br> | \*_Deployment logging_<br>• | Added timestamps and severity information to deployment logs. | <br> | \*_Environment variables_<br>• | Fixed an issue where the platform would throw an error when environment variables have empty values. |     |

## New platform versions

###### These platforms are updated:

- [.NET on Windows Server](#release-2025-04-17-windows.platforms.net "#release-2025-04-17-windows.platforms.net")

### .NET on Windows Server

#### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                               | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.19.0**      | _64bit Windows Server 2025 v2.19.0 running IIS 10.0_      | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.0** | _64bit Windows Server Core 2025 v2.19.0 running IIS 10.0_ | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.19.0**      | _64bit Windows Server 2022 v2.19.0 running IIS 10.0_      | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.0** | _64bit Windows Server Core 2022 v2.19.0 running IIS 10.0_ | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.19.0**      | _64bit Windows Server 2019 v2.19.0 running IIS 10.0_      | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.0** | _64bit Windows Server Core 2019 v2.19.0 running IIS 10.0_ | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.19.0**      | _64bit Windows Server 2016 v2.19.0 running IIS 10.0_      | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.0** | _64bit Windows Server Core 2016 v2.19.0 running IIS 10.0_ | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

#### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.19.0**      | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.0** | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server 2022 with IIS 10.0 version 2.19.0**      | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.0** | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server 2019 with IIS 10.0 version 2.19.0**      | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.0** | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server 2016 with IIS 10.0 version 2.19.0**      | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.0** | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
