# Release: Elastic Beanstalk Windows Server platform update on March 28, 2023

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates framework and AWS components.

**Release date:** March 28, 2023

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                       |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------ | ----------------------------------------------------------------------------------- | ---- | ------------------------- | ---------------------------------------------------------- | ---- | ------------------ | ----------------------------------------- | ---- | ------------------ | ---------------------------------------------------------------------------------------- | ---- | ------------------ | --------------------------------------------------------------------------------------- | --- |
| **Windows security updates** | Applied March 2023 security updates for Windows.<br>See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |                                                                                                                                                                                                                       | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_.NET Core_<br>• | Updated .NET 6 to version 6.0.15 on Windows Server 2019 and 2016 platform versions. |      |
| **AWS component updates**    |                                                                                                                                                                                                                       | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AMI_<br>•       | Updated the base AMI to version 2023.03.15.                                         | <br> | \*_CloudWatch Agent_<br>• | Updated the CloudWatch Agent to version 1.247358.0b252413. | <br> | \*_EC2Launch_<br>• | Updated EC2Launch V2 to version 2.0.1245. | <br> | \*_SSM Agent_<br>• | Updated the SSM Agent to version 3.1.2144.0 on Windows Server 2012 R2 platform versions. | <br> | \*_EC2Config_<br>• | Updated EC2Config to version 4.9.5288 on Windows Server Core 2012 R2 platform versions. |     |

## New platform versions

### .NET on Windows Server

#### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                          | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.11.2**               | _64bit Windows Server 2019 v2.11.2 running IIS 10.0_        | .NET 6.0.15, supports 6.0.15, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.2**          | _64bit Windows Server Core 2019 v2.11.2 running IIS 10.0_   | .NET 6.0.15, supports 6.0.15, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.2**               | _64bit Windows Server 2016 v2.11.2 running IIS 10.0_        | .NET 6.0.15, supports 6.0.15, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.2**          | _64bit Windows Server Core 2016 v2.11.2 running IIS 10.0_   | .NET 6.0.15, supports 6.0.15, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.2**             | _64bit Windows Server 2012 R2 v2.11.2 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.2** | _64bit Windows Server Core 2012 R2 v2.11.2 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

#### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.11.2**               | 2023.03.15  | 3.15.1998        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.2**          | 2023.03.15  | 3.15.1998        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.2**               | 2023.03.15  | 3.15.1998        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.2**          | 2023.03.15  | 3.15.1998        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.2**             | 2023.03.15  | 3.15.1998        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.2** | 2023.03.15  | 3.15.1998        | 4.9.5288  | 3.1.2144.0 | 3.6        | 3.2.0     |
