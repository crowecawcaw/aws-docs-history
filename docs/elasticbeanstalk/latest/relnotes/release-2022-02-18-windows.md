# Release: Elastic Beanstalk Windows Server platform update on February 18, 2022

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates framework and AWS components.

**Release date:** February 18, 2022

###### Windows Platform Version 2.8.3

This release introduced TLS v1.2 to Elastic Beanstalk platform branches on _Windows Server 2019_. Subsequent _Windows Server 2019_ platform releases include TLS v1.2 or later versions. For a list of the most recent and supported Windows
Server platform versions, see [Supported Platforms](../platforms/platforms-supported.md#platforms-supported.net "../platforms/platforms-supported.md#platforms-supported.net") in the _AWS Elastic Beanstalk Platforms_ guide.

As of December 31 2023, AWS started fully enforcing TLS 1.2 across all AWS API endpoints. Any environments running _Windows Server 2019_ versions that are older than this release still use TLS 1.0 and 1.1. Applications running on these older versions, may
no longer be able to perform actions such as configuration deployments, application deployments, auto scaling, new environment launch, log rotation and
enhanced health reports.

To avoid the risk of availability impact, please upgrade your platform versions to a newer version as soon as possible.

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------------- | ----------------------------------------------------------------------------------- | ---- | ------------ | ------------------------------------------- | ---- | ------------------ | ------------------------------------------------------------------------------------------------------ | ---- | ------------------ | --------------------------------------------------------------------------------------- | ---- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| **Windows security updates** | Applied February 2022 security updates for Windows.<br>See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |                                                                                                                                                                                                                          | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_.NET Core_<br>•        | Updated .NET 5 to version 5.0.14 on Windows Server 2019 and 2016 platform versions. |      |
| **AWS component updates**    |                                                                                                                                                                                                                          | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AWS SDK for .NET_<br>• | Updated the SDK to version 3.15.1546.                                               | <br> | \*_AMI_<br>• | Updated the base AMI to version 2022.02.10. | <br> | \*_SSM Agent_<br>• | Updated the SSM Agent to version 3.1.804.0 on Windows Server 2019, 2016 and 2012 R2 platform versions. | <br> | \*_EC2Config_<br>• | Updated EC2Config to version 4.9.4536 on Windows Server 2012 R2 Core platform versions. | <br> | \*_EC2Launch_<br>• | Updated EC2Launch agent to version 2.0.698 on Windows Server 2019, 2016 and 2012 R2 platform versions. This does<br>*not<br>• include Windows Server 2012 R2 *Core<br>• platform versions. |     |

## New platform versions

### .NET on Windows Server

#### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                  | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.8.3**               | _64bit Windows Server 2019 v2.8.3 running IIS 10.0_        | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.8.3**          | _64bit Windows Server Core 2019 v2.8.3 running IIS 10.0_   | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.8.3**               | _64bit Windows Server 2016 v2.8.3 running IIS 10.0_        | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.8.3**          | _64bit Windows Server Core 2016 v2.8.3 running IIS 10.0_   | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.8.3**             | _64bit Windows Server 2012 R2 v2.8.3 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x      | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.3** | _64bit Windows Server Core 2012 R2 v2.8.3 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x      | IIS 8.5      |

#### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.8.3**               | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.8.3**          | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.8.3**               | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.8.3**          | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.8.3**             | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.3** | 2022.02.10  | 3.15.1546        | 4.9.4536  | 3.1.804.0 | 3.6        | 3.2.0     |
