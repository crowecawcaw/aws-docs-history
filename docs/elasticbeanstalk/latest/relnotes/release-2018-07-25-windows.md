# Release: AWS Elastic Beanstalk Windows Server platform update on July 25, 2018

This release applies Windows July 2018 security updates to the Windows Server platform for Elastic Beanstalk, and updates platform
configurations. The release also adds Amazon EC2 instance types in certain AWS Regions.

**Release date:** July 25, 2018

## Changes

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows security updates** | Applied July 2018 security updates for Windows. See Microsoft's [Security TechCenter](https://portal.msrc.microsoft.com/en-us/ "https://portal.msrc.microsoft.com/en-us/") and [Security Advisories and Bulletins](https://technet.microsoft.com/en-us/library/security/ "https://technet.microsoft.com/en-us/library/security/"). |
| **Instance types**           | Added support for more Amazon EC2 instance types in some AWS Regions, as follows:                                                                                                                                                                                                                                                  |
| **Instance type**            | **Regions**                                                                                                                                                                                                                                                                                                                        |
| ---                          | ---                                                                                                                                                                                                                                                                                                                                |
| **X1e**                      | AWS GovCloud (US)—us-gov-west-1                                                                                                                                                                                                                                                                                                    |

| ## Updated platform configurations ### .NET on Windows Server with IIS #### Configuration basics
| Configuration | Solution Stack Name | Framework | Proxy Server |
| --- | --- | --- | --- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0** | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_ | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0** | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_ | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0** | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 with IIS 8 version 1.2.0** | _64bit Windows Server 2012 v1.2.0 running IIS 8_ | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0** | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_ | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 |
| **Windows Server 2012 R2 with IIS 8.5** | _64bit Windows Server 2012 R2 running IIS 8.5_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5** | _64bit Windows Server Core 2012 R2 running IIS 8.5_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 with IIS 8** | _64bit Windows Server 2012 running IIS 8_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 |
| **Windows Server 2008 R2 with IIS 7.5** | _64bit Windows Server 2008 R2 running IIS 7.5_ | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 | #### More details
| Configuration | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X‑Ray |
| --- | --- | --- | --- | --- | --- | --- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0** | 2018.07.11 | 3.3.311.0 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.800.0 | 3.6 | 1.0.0 |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0** | 2018.07.11 | 3.3.311.0 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.800.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0** | 2018.07.11 | 3.3.311.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.07.11 | 3.3.311.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 with IIS 8 version 1.2.0** | 2018.07.11 | 3.3.311.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0** | 2018.07.11 | 3.3.311.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 with IIS 8.5** | 2018.07.11 | 3.3.311.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5** | 2018.07.11 | 3.3.311.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 |
| **Windows Server 2012 with IIS 8** | 2018.07.11 | 3.3.311.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 |
| **Windows Server 2008 R2 with IIS 7.5** | 2018.07.11 | 3.3.311.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 |
