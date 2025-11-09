# Release: Elastic Beanstalk Windows Server platform update on July 2, 2021

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates framework and AWS components.

**Release date:** July 2, 2021

## Changes

The following table lists the changes included in this release.

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                      |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------- | ---- | ------- | ------- | ---- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ------------ | ------------------------------------------- | ---- | ------------------ | ---------------------------------------------------------------------------------------------- | ---- | ------------------ | ------------------------------------------------------------------------------- | --- |
| **Windows security updates** | Applied June 2021 security updates for Windows.<br>See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |                                                                                                                                                                                                                      | \*_Framework_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_.NET Core_<br>•        | Updated .NET Core 3 to version 3.1.16 on Windows Server 2019 and 2016 platform versions.<br>Updated .NET 5 to version 5.0.7 on Windows Server 2019 and 2016 platform versions. |      |
| **AWS component updates**    |                                                                                                                                                                                                                      | \*_Component_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AWS SDK for .NET_<br>• | Updated the SDK to version 3.15.1326.                                                                                                                                          | <br> | \*_AMI_<br>• | Updated the base AMI to version 2021.06.09. | <br> | \*_SSM Agent_<br>• | Updated the SSM Agent to version 3.0.1124.0 on Windows Server 2019 and 2016 platform versions. | <br> | \*_EC2Config_<br>• | Updated EC2Config to version 4.9.4419 on Windows Server 2012 platform versions. |     |

## New platform versions

### .NET on Windows Server

#### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                       | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.6.7**               | _64bit Windows Server 2019 v2.6.7 running IIS 10.0_        | .NET 5.0.7, supports 5.0.7, 3.1.16, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.7**          | _64bit Windows Server Core 2019 v2.6.7 running IIS 10.0_   | .NET 5.0.7, supports 5.0.7, 3.1.16, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.7**               | _64bit Windows Server 2016 v2.6.7 running IIS 10.0_        | .NET 5.0.7, supports 5.0.7, 3.1.16, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.7**          | _64bit Windows Server Core 2016 v2.6.7 running IIS 10.0_   | .NET 5.0.7, supports 5.0.7, 3.1.16, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.7**             | _64bit Windows Server 2012 R2 v2.6.7 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.7** | _64bit Windows Server Core 2012 R2 v2.6.7 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

#### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent  | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.6.7**               | 2021.06.09  | 3.15.1326        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.7**          | 2021.06.09  | 3.15.1326        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.7**               | 2021.06.09  | 3.15.1326        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.7**          | 2021.06.09  | 3.15.1326        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.7**             | 2021.06.09  | 3.15.1326        | 4.9.4419                                                                                                  | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.7** | 2021.06.09  | 3.15.1326        | 4.9.4419                                                                                                  | 3.0.1124.0 | 3.6        | 3.2.0     |
