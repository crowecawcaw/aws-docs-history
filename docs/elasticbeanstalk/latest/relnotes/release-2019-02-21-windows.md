# Release: AWS Elastic Beanstalk Windows Server platform update on February 21, 2019

This release applies Windows February 2019 security updates to the Windows Server v1 and earlier platform versions for Elastic Beanstalk.
The release also adds Amazon EC2 instance types in certain AWS Regions.

**Release date:** February 21, 2019

## Changes

This release updates Windows Server v1 and earlier platform versions. To learn more about Windows Server v2 platform versions, see [Release: AWS Elastic Beanstalk Windows Server platform update
to new major version 2 on February 21, 2019](release-2019-02-21-windows-v2.md "release-2019-02-21-windows-v2.md").

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows security updates** | Applied February 2019 security updates for Windows. See Microsoft's [Security TechCenter](https://portal.msrc.microsoft.com/en-us/ "https://portal.msrc.microsoft.com/en-us/") and [Security Advisories and Bulletins](https://technet.microsoft.com/en-us/library/security/ "https://technet.microsoft.com/en-us/library/security/"). |
| **Instance types**           | Added support for more Amazon EC2 instance types in some AWS Regions, as follows:                                                                                                                                                                                                                                                      |
| **Instance type**            | **Region**                                                                                                                                                                                                                                                                                                                             |
| ---                          | ---                                                                                                                                                                                                                                                                                                                                    |
| **C5d, M5d, R5, R5d, T3**    | <br>• Asia Pacific (Mumbai) – ap-south-1                                                                                                                                                                                                                                                                                               |

| ## New platform versions ### .NET on Windows Server with IIS #### Configuration basics
| Platform Version | Solution Stack Name | Framework | Proxy Server |
| --- | --- | --- | --- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0** | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_ | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0** | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_ | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0** | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 with IIS 8 version 1.2.0** | _64bit Windows Server 2012 v1.2.0 running IIS 8_ | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0** | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_ | .NET Core 2.1.8, supports 2.1.8, 2.0.9, 1.1.11, 1.0.14 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 |
| **Windows Server 2012 R2 with IIS 8.5** | _64bit Windows Server 2012 R2 running IIS 8.5_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5** | _64bit Windows Server Core 2012 R2 running IIS 8.5_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 with IIS 8** | _64bit Windows Server 2012 running IIS 8_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 |
| **Windows Server 2008 R2 with IIS 7.5** | _64bit Windows Server 2008 R2 running IIS 7.5_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 | #### More details
| Platform Version | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X‑Ray |
| --- | --- | --- | --- | --- | --- | --- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0** | 2019.02.13 | 3.15.666 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6 | 1.0.0 |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0** | 2019.02.13 | 3.15.666 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0** | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 with IIS 8 version 1.2.0** | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0** | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 with IIS 8.5** | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5** | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 with IIS 8** | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 |
| **Windows Server 2008 R2 with IIS 7.5** | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 |
