# Release: Elastic Beanstalk Windows Server platform update on April 18, 2024

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates AWS components.

**Release date:** April 18, 2024

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------ | -------------------------------------------------------------------- | ---- | ------------------------- | ------------------------------------------------------- | ---- | ------------------ | ---------------------------------- | --- |
| **Windows security updates** | Applied April 2024 security updates for Windows.<br>This release includes updates from the monthly Microsoft \*Patch Tuesday<br>• Windows release. Windows security updates in<br>this release are current up to the second Tuesday of the month.<br>For more details and a list of security updates, see the Microsoft [Security<br>Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_.NET Core_<br>• | Updated .NET 6 to version 6.0.29.<br>Updated .NET 8 to version 8.0.4 |      |
| **AWS component updates**    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AMI_<br>•       | Updated the base AMI to version 2024.04.10.                          | <br> | \*_CloudWatch Agent_<br>• | Updated the CloudWatch Agent to version 1.300035.0b547. | <br> | \*_AWS X-Ray_<br>• | Updated the AWS to version 3.3.11. |     |

## New platform versions

### .NET on Windows Server

#### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.15.0**      | _64bit Windows Server 2022 v2.15.0 running IIS 10.0_      | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.0** | _64bit Windows Server Core 2022 v2.15.0 running IIS 10.0_ | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.15.0**      | _64bit Windows Server 2019 v2.15.0 running IIS 10.0_      | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.0** | _64bit Windows Server Core 2019 v2.15.0 running IIS 10.0_ | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.15.0**      | _64bit Windows Server 2016 v2.15.0 running IIS 10.0_      | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.0** | _64bit Windows Server Core 2016 v2.15.0 running IIS 10.0_ | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

#### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.15.0**      | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.0** | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |
| **Windows Server 2019 with IIS 10.0 version 2.15.0**      | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.0** | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |
| **Windows Server 2016 with IIS 10.0 version 2.15.0**      | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.0** | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |
