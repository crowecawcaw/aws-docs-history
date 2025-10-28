# Release: AWS Elastic Beanstalk Windows Server platform update on January 24, 2019

This release applies Windows January 2019 security updates to the Windows Server platform for Elastic Beanstalk, and updates platform
configurations. The release also adds Amazon EC2 instance types in certain AWS Regions.

**Release date:** January 24, 2019

## Changes

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows security updates** | Applied January 2019 security updates for Windows. See Microsoft's [Security TechCenter](https://portal.msrc.microsoft.com/en-us/ "https://portal.msrc.microsoft.com/en-us/") and [Security Advisories and Bulletins](https://technet.microsoft.com/en-us/library/security/ "https://technet.microsoft.com/en-us/library/security/"). |
| **.NET Core updates**        | Added support for .NET Core 2.2 for configurations with Windows Server 2012 or later. For details, see [Announcing .NET Core 2.2](https://devblogs.microsoft.com/dotnet/announcing-net-core-2-2/ "https://devblogs.microsoft.com/dotnet/announcing-net-core-2-2/") in the _.NET Blog_.                                                |
| **Instance types**           | Added support for more Amazon EC2 instance types in some AWS Regions, as follows:                                                                                                                                                                                                                                                     |
| **Instance type**            | **Region**                                                                                                                                                                                                                                                                                                                            |
| ---                          | ---                                                                                                                                                                                                                                                                                                                                   |
| **X1e**                      | <br>• Asia Pacific (Seoul) – ap-northeast-2                                                                                                                                                                                                                                                                                           |

| ## Updated platform configurations ### .NET on Windows Server with IIS #### Configuration basics
| Configuration | Solution Stack Name | Framework | Proxy Server |
| --- | --- | --- | --- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0** | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_ | .NET Core 2.2.1, supports 2.2.1, 2.1.7, 2.0.9, 1.1.10, 1.0.13 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0** | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_ | .NET Core 2.2.1, supports 2.2.1, 2.1.7, 2.0.9, 1.1.10, 1.0.13 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0** | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.1, supports 2.2.1, 2.1.7, 2.0.9, 1.1.10, 1.0.13 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.1, supports 2.2.1, 2.1.7, 2.0.9, 1.1.10, 1.0.13 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 with IIS 8 version 1.2.0** | _64bit Windows Server 2012 v1.2.0 running IIS 8_ | .NET Core 2.2.1, supports 2.2.1, 2.1.7, 2.0.9, 1.1.10, 1.0.13 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0** | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_ | .NET Core 2.1.7, supports 2.1.7, 2.0.9, 1.1.10, 1.0.13 .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 |
| **Windows Server 2012 R2 with IIS 8.5** | _64bit Windows Server 2012 R2 running IIS 8.5_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5** | _64bit Windows Server Core 2012 R2 running IIS 8.5_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 with IIS 8** | _64bit Windows Server 2012 running IIS 8_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 |
| **Windows Server 2008 R2 with IIS 7.5** | _64bit Windows Server 2008 R2 running IIS 7.5_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 | #### More details
| Configuration | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X‑Ray |
| --- | --- | --- | --- | --- | --- | --- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0** | 2019.01.10 | 3.3.434.0 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.344.0 | 3.6 | 1.0.0 |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0** | 2019.01.10 | 3.3.434.0 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.344.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0** | 2019.01.10 | 3.3.434.0 | 4.9.3160 | 2.3.344.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.01.10 | 3.3.434.0 | 4.9.3160 | 2.3.344.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 with IIS 8 version 1.2.0** | 2019.01.10 | 3.3.434.0 | 4.9.3160 | 2.3.344.0 | 3.6 | 1.0.0 |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0** | 2019.01.10 | 3.3.434.0 | 4.9.3160 | 2.3.344.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 with IIS 8.5** | 2019.01.10 | 3.3.434.0 | 4.9.3160 | 2.3.344.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5** | 2019.01.10 | 3.3.434.0 | 4.9.3160 | 2.3.344.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 with IIS 8** | 2019.01.10 | 3.3.434.0 | 4.9.3160 | 2.3.344.0 | 3.6 | 1.0.0 |
| **Windows Server 2008 R2 with IIS 7.5** | 2019.01.10 | 3.3.434.0 | 4.9.3160 | 2.3.344.0 | 3.6 | 1.0.0 |
