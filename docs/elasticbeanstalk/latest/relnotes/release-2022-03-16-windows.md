# Release: Elastic Beanstalk Windows Server platform update on March 16, 2022

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates framework and AWS components.

**Release date:** March 16, 2022

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                       |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------ | ------------------------------------------- | ---- | ------------------------- | --------------------------------------------------- | ---- | ------------------ | ------------------------------------------- | ---- | ------------------ | ---------------------------------------------------------------------------------------------- | --- |
| **Windows security updates** | Applied March 2022 security updates for Windows.<br>See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |                                                                                                                                                                                                                       | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_.NET Core_<br>•        | Updated .NET Core 3 to version 3.1.23 on Windows Server 2019 and 2016 platform versions.<br>Updated .NET 5 to version 5.0.15 on Windows Server 2019 and 2016 platform versions.<br>The following runtime versions are being removed from the listed platform versions,<br>because they're past Microsoft’s end of support dates.<br>For more information, see<br>[.NET and .NET Core Support Policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core "https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core")<br>on the Microsoft website.<br>• Windows Server 2012 R2 platforms — .NET Core 3.0 removed<br>• Windows Server 2016 and 2019 platforms — .NET Core 2.1 removed |      |
| **AWS component updates**    |                                                                                                                                                                                                                       | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AWS SDK for .NET_<br>• | Updated the SDK to version 3.15.1583.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | <br> | \*_AMI_<br>• | Updated the base AMI to version 2022.03.09. | <br> | \*_CloudWatch Agent_<br>• | Updated the CloudWatch Agent to version 1.247350.0. | <br> | \*_SSM Agent_<br>• | Updated the SSM Agent to version 3.1.1045.0 | <br> | \*_EC2Config_<br>• | Updated EC2Config to version 4.9.4556 on Windows Server 2012 R2 Server Core platform versions. |     |

## New platform versions

### .NET on Windows Server

#### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                          | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.9.0**               | _64bit Windows Server 2019 v2.9.0 running IIS 10.0_        | .NET 5.0.15, supports 5.0.15, 3.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.9.0**          | _64bit Windows Server Core 2019 v2.9.0 running IIS 10.0_   | .NET 5.0.15, supports 5.0.15, 3.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.9.0**               | _64bit Windows Server 2016 v2.9.0 running IIS 10.0_        | .NET 5.0.15, supports 5.0.15, 3.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.9.0**          | _64bit Windows Server Core 2016 v2.9.0 running IIS 10.0_   | .NET 5.0.15, supports 5.0.15, 3.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.9.0**             | _64bit Windows Server 2012 R2 v2.9.0 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.9.0** | _64bit Windows Server Core 2012 R2 v2.9.0 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

#### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.9.0**               | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.9.0**          | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.9.0**               | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.9.0**          | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.9.0**             | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.9.0** | 2022.03.09  | 3.15.1583        | 4.9.4556  | 3.1.1045.0 | 3.6        | 3.2.0     |
