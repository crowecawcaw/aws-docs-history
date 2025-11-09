# Release: Elastic Beanstalk Windows Server platform update and Windows Server 2019 support on January 15, 2020

This release provides new Windows Server version 2 (v2) platform versions for AWS Elastic Beanstalk.
Most notably, the release adds support for Windows Server 2019 platform versions.

**Release date:** January 15, 2020

## Changes

The following table lists the changes included in this release. Be aware that at the time these release notes are published, the new platform versions
might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description** |
| ---------------------------- | --------------- | ----------- | ---------------- | ---- | ------- | ------- | ---- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| **Operating system updates** |                 | \*_OS_<br>• | \*_Details_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Windows Server 2019_<br>• | Added support for Windows Server 2019 as two new Windows Server v2 platform versions: one with Windows Server 2019, one with<br>Windows Server Core 2019.<br>For details from Microsoft, see [Get<br>started with Windows Server 2019](https://docs.microsoft.com/en-us/windows-server/get-started-19/get-started-19 "https://docs.microsoft.com/en-us/windows-server/get-started-19/get-started-19"). |     |

## New platform versions

### .NET on Windows Server with IIS

#### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.4.0**               | _64bit Windows Server 2019 v2.4.0 running IIS 10.0_        | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.4.0**          | _64bit Windows Server Core 2019 v2.4.0 running IIS 10.0_   | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.4.0**               | _64bit Windows Server 2016 v2.4.0 running IIS 10.0_        | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.4.0**          | _64bit Windows Server Core 2016 v2.4.0 running IIS 10.0_   | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.4.0**             | _64bit Windows Server 2012 R2 v2.4.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.4.0** | _64bit Windows Server Core 2012 R2 v2.4.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |

#### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X‑Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.4.0**               | 2019.12.16  | 3.15.903         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.4.0**          | 2019.12.16  | 3.15.903         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 2.4.0**               | 2019.12.16  | 3.15.903         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.4.0**          | 2019.12.16  | 3.15.903         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.4.0**             | 2019.12.16  | 3.15.903         | 4.9.3865                                                                                                  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.4.0** | 2019.12.16  | 3.15.903         | 4.9.3865                                                                                                  | 2.3.722.0 | 3.6        | 3.1.0     |
