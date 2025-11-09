# Release: Elastic Beanstalk Windows Server platform update on June 19, 2025

This release provides new Windows Server platform versions for AWS Elastic Beanstalk, Windows security updates, and updates framework and AWS components.

**Release date:** June 19, 2025

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                             | **Description**                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------ | ------------------------------------------------------------- | ---- | ------------------------- | -------------------------------------- | ---- | ------------------------- | -------------------------------------------------------- | ---- | ------------------ | -------------------------------------- | --- |
| **Framework updates**                    |                                                                                                                                                                                                                                                                                                                                                              | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_.NET Core_<br>• | Updated .NET 9 to version 9.0.6 and .NET 8 to version 8.0.17. |      |
| **AWS component updates**                |                                                                                                                                                                                                                                                                                                                                                              | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AMI_<br>•       | Updated the base AMI to version 2025.06.11.                   | <br> | \*_AWS SDK for .NET_<br>• | Updated the SDK to version 3.7.1062.0. | <br> | \*_CloudWatch Agent_<br>• | Updated the CloudWatch Agent to version 1.300056.0b1123. | <br> | \*_EC2Launch_<br>• | Updated EC2Launch V2 to version 2.1.1. |     |
| **Additional changes with this release** | • Elastic Beanstalk now supports an architecture flag in Windows deployment manifests, enabling control over PowerShell script execution architecture.<br>• New skipIISReset flag in Windows deployment manifests allows users to bypass IIS resets during deployments, reducing application downtime and deployment time in multi-application environments. |

## New platform versions

###### These platforms are updated:

- [.NET on Windows Server](#release-2025-06-19-windows.platforms.net "#release-2025-06-19-windows.platforms.net")

### .NET on Windows Server

#### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.19.2**      | _64bit Windows Server 2025 v2.19.2 running IIS 10.0_      | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.2** | _64bit Windows Server Core 2025 v2.19.2 running IIS 10.0_ | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.19.2**      | _64bit Windows Server 2022 v2.19.2 running IIS 10.0_      | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.2** | _64bit Windows Server Core 2022 v2.19.2 running IIS 10.0_ | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.19.2**      | _64bit Windows Server 2019 v2.19.2 running IIS 10.0_      | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.2** | _64bit Windows Server Core 2019 v2.19.2 running IIS 10.0_ | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.19.2**      | _64bit Windows Server 2016 v2.19.2 running IIS 10.0_      | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.2** | _64bit Windows Server Core 2016 v2.19.2 running IIS 10.0_ | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

#### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.19.2**      | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.2** | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server 2022 with IIS 10.0 version 2.19.2**      | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.2** | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server 2019 with IIS 10.0 version 2.19.2**      | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.2** | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server 2016 with IIS 10.0 version 2.19.2**      | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.2** | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
