# Release: Elastic Beanstalk Windows Server platform update on March 26, 2025

This release provides new Windows Server platform versions for AWS Elastic Beanstalk, Windows security updates, and
updates framework and AWS components. This release also introduces a feature that adds support for Elastic Beanstalk environment variables
to store secrets and parameters from AWS Secrets Manager and AWS Systems Manager Parameter Store.

**Release date:** March 26, 2025

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------------- | -------------------------------------- | ---- | ------------------------- | -------------------------------------------------------- | ---- | ------------------ | ----------------------------------------- | ---- | ------------------ | ------------------------------------------- | --- |
| **Windows security updates** | Applied March 2025 security updates for Windows.<br>This release includes updates from the monthly Microsoft \*Patch Tuesday<br>• Windows release. Windows security updates in<br>this release are current up to the second Tuesday of the month.<br>For more details and a list of security updates, see the Microsoft [Security<br>Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_\*\*New!\*\<br>• — Elastic Beanstalk supports configuration of environment variables to store secret and parameter<br>data._<br>• | Starting with this release Elastic Beanstalk supports the option to reference AWS Secrets Manager secrets and Systems Manager Parameter Store parameters with<br>environment variables.<br>To learn more about this feature, see [Using<br>Elastic Beanstalk with Secrets Manager and Systems Manager Parameter Store](../dg/AWSHowTo.md "../dg/AWSHowTo.md"). | <br> | \*_.NET Core_<br>•        | Updated .NET 8 to version 8.0.14.      |      |
| **AWS component updates**    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AMI_<br>•                                                                                                                         | Updated the base AMI to version 2025.03.12.                                                                                                                                                                                                                                                                                                                    | <br> | \*_AWS SDK for .NET_<br>• | Updated the SDK to version 3.7.1000.0. | <br> | \*_CloudWatch Agent_<br>• | Updated the CloudWatch Agent to version 1.300053.0b1046. | <br> | \*_EC2Launch_<br>• | Updated EC2Launch V2 to version 2.0.2081. | <br> | \*_AWS X-Ray_<br>• | Updated the X-Ray daemon to version 3.3.14. |     |

## New platform versions

###### These platforms are updated:

- [.NET on Windows Server](#release-2025-03-26-windows.platforms.net "#release-2025-03-26-windows.platforms.net")

### .NET on Windows Server

#### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                       | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.18.0**      | _64bit Windows Server 2025 v2.18.0 running IIS 10.0_      | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.18.0** | _64bit Windows Server Core 2025 v2.18.0 running IIS 10.0_ | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.18.0**      | _64bit Windows Server 2022 v2.18.0 running IIS 10.0_      | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.18.0** | _64bit Windows Server Core 2022 v2.18.0 running IIS 10.0_ | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.18.0**      | _64bit Windows Server 2019 v2.18.0 running IIS 10.0_      | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.18.0** | _64bit Windows Server Core 2019 v2.18.0 running IIS 10.0_ | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.18.0**      | _64bit Windows Server 2016 v2.18.0 running IIS 10.0_      | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.18.0** | _64bit Windows Server Core 2016 v2.18.0 running IIS 10.0_ | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

#### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.18.0**      | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2025 with IIS 10.0 version 2.18.0** | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server 2022 with IIS 10.0 version 2.18.0**      | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2022 with IIS 10.0 version 2.18.0** | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server 2019 with IIS 10.0 version 2.18.0**      | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2019 with IIS 10.0 version 2.18.0** | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server 2016 with IIS 10.0 version 2.18.0**      | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2016 with IIS 10.0 version 2.18.0** | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
