# Release: Elastic Beanstalk Windows Server platform update on August 20, 2024

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates and
updates AWS components. It also includes updates that improve Windows deployment time.

**Release date:** August 20, 2024

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                             | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------ | --------------------------------------------------------------------- | ---- | ------------------------- | ------------------------------------- | ---- | ------------------ | ----------------------------------------- | ---- | ------------------ | --------------------------------------- | --- |
| **Windows security updates**             | Applied August 2024 security updates for Windows.<br>This release includes updates from the monthly Microsoft \*Patch Tuesday<br>• Windows release. Windows security updates in<br>this release are current up to the second Tuesday of the month.<br>For more details and a list of security updates, see the Microsoft [Security<br>Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance").                                                                                                        |
| **Framework updates**                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_.NET Core_<br>• | Updated .NET 6 to version 6.0.33.<br>Updated .NET 8 to version 8.0.8. |      |
| **AWS component updates**                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AMI_<br>•       | Updated the base AMI to version 2024.08.14.                           | <br> | \*_AWS SDK for .NET_<br>• | Updated the SDK to version 3.7.864.0. | <br> | \*_EC2Launch_<br>• | Updated EC2Launch V2 to version 2.0.1981. | <br> | \*_AWS X-Ray_<br>• | Updated X-Ray daemon to version 3.3.13. |     |
| **Additional changes with this release** | This release improves the deployment time for the Windows platform components. The deployment time is reduced by up to 100 seconds.<br>To improve the Windows deployment response time we introduced the following software modules to the Windows platform: [NuGet](https://learn.microsoft.com/en-us/nuget/ "https://learn.microsoft.com/en-us/nuget/") package, [AWS.Tools.Installer<br>for Powershell](../../../powershell.md "../../../powershell.md") , AWS.Tools.Common, and AWS.Tools.S3. These new modules should not have any additional impact to your<br>applications. |

## New platform versions

### .NET on Windows Server

#### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.15.4**      | _64bit Windows Server 2022 v2.15.4 running IIS 10.0_      | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.4** | _64bit Windows Server Core 2022 v2.15.4 running IIS 10.0_ | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.15.4**      | _64bit Windows Server 2019 v2.15.4 running IIS 10.0_      | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.4** | _64bit Windows Server Core 2019 v2.15.4 running IIS 10.0_ | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.15.4**      | _64bit Windows Server 2016 v2.15.4 running IIS 10.0_      | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.4** | _64bit Windows Server Core 2016 v2.15.4 running IIS 10.0_ | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

#### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.15.4**      | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.4** | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server 2019 with IIS 10.0 version 2.15.4**      | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.4** | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server 2016 with IIS 10.0 version 2.15.4**      | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.4** | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
