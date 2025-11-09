# Release: Elastic Beanstalk Windows Server platform update on

July 17, 2025

This release provides new Windows Server platform versions
for AWS Elastic Beanstalk. It updates framework and AWS components and applies Windows security updates.
This release also adds support for creating multiple IIS websites and installs the IIS ARR by default on Windows AMIs.

**Release date:** July 17, 2025

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------------- | --------------------------------------------------------------------- | ---- | ------------ | ------------------------------------------- | ---- | --------------------- | ------------------------------------------- | ---- | ------------------ | -------------------------------------------- | ---- | ------------------------- | ----------------------------------------------------------- | --- |
| **Windows security updates**                | Applied July 2025 security updates for Windows.<br>This release includes updates from the monthly Microsoft \*Patch Tuesday<br>• Windows release. Windows security updates in<br>this release are current up to the second Tuesday of the month.<br>For more details and a list of security updates, see the Microsoft [Security<br>Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_.NET Core_<br>•        | Updated .NET 9 to version 9.0.7.<br>Updated .NET 8 to version 8.0.18. |      |
| **AWS component updates**                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AWS SDK for .NET_<br>• | Updated the SDK to version 3.7.1077.0.                                | <br> | \*_AMI_<br>• | Updated the base AMI to version 2025.07.09. | <br> | \*_X-Ray daemon_<br>• | Updated the X-Ray daemon to version 3.3.15. | <br> | \*_SSM Agent_<br>• | Updated the SSM Agent to version 3.3.2471.0. | <br> | \*_CloudWatch Agent_<br>• | Updated the CloudWatch Agent to version<br>1.300057.0b1161. |     |
| **Additional changes with this<br>release** | This release adds support for creating multiple IIS websites and<br>deploying applications to them using the [deployment manifest](../dg/dotnet-manifest-schema.md "../dg/dotnet-manifest-schema.md"). The IIS Application Request Routing Module<br>(ARR) is now installed by default on Windows AMIs. These changes provide<br>more customization options for IIS sites and routing configuration.                                                                      |

## New platform

versions

###### These platforms are updated:

- [.NET on Windows
  Server](#release-2025-07-17-windows.platforms.net "#release-2025-07-17-windows.platforms.net")

### .NET on Windows

Server

#### Configuration basics

| Platform Version                                             | Solution Stack Name                                          | Framework                                                                     | Proxy Server |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version<br>2.19.3**      | _64bit Windows Server 2025 v2.19.3 running IIS 10.0_         | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version<br>2.19.3** | _64bit Windows Server Core 2025 v2.19.3 running IIS<br>10.0_ | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version<br>2.19.3**      | _64bit Windows Server 2022 v2.19.3 running IIS 10.0_         | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version<br>2.19.3** | _64bit Windows Server Core 2022 v2.19.3 running IIS<br>10.0_ | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version<br>2.19.3**      | _64bit Windows Server 2019 v2.19.3 running IIS 10.0_         | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version<br>2.19.3** | _64bit Windows Server Core 2019 v2.19.3 running IIS<br>10.0_ | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version<br>2.19.3**      | _64bit Windows Server 2016 v2.19.3 running IIS 10.0_         | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version<br>2.19.3** | _64bit Windows Server Core 2016 v2.19.3 running IIS<br>10.0_ | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

#### More details

| Platform Version                                             | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version<br>2.19.3**      | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2025 with IIS 10.0 version<br>2.19.3** | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server 2022 with IIS 10.0 version<br>2.19.3**      | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2022 with IIS 10.0 version<br>2.19.3** | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server 2019 with IIS 10.0 version<br>2.19.3**      | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2019 with IIS 10.0 version<br>2.19.3** | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server 2016 with IIS 10.0 version<br>2.19.3**      | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2016 with IIS 10.0 version<br>2.19.3** | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
