# Release: AWS Elastic Beanstalk Windows Server platform update on December 1, 2019

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates .NET Core versions.

**Release date:** December 1, 2019

## Changes

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows security updates** | Applied November 2019 security updates for Windows. See Microsoft's [Security TechCenter](https://portal.msrc.microsoft.com/en-us/ "https://portal.msrc.microsoft.com/en-us/") and [Security Advisories and Bulletins](https://technet.microsoft.com/en-us/library/security/ "https://technet.microsoft.com/en-us/library/security/"). |
| **Framework updates**        |
| **Framework**                | **Details**                                                                                                                                                                                                                                                                                                                            |
| ---                          | ---                                                                                                                                                                                                                                                                                                                                    |
| **.NET Core**                | Updated .NET Core versions to 2.2.8, 2.1.14.                                                                                                                                                                                                                                                                                           |

| ## New platform versions ### .NET on Windows Server with IIS #### Configuration basics
| Platform Version | Solution Stack Name | Framework | Proxy Server |
| --- | --- | --- | --- |
| **Windows Server 2016 with IIS 10.0 version 2.3.1** | _64bit Windows Server 2016 v2.3.1 running IIS 10.0_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.3.1** | _64bit Windows Server Core 2016 v2.3.1 running IIS 10.0_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.3.1** | _64bit Windows Server 2012 R2 v2.3.1 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.1** | _64bit Windows Server Core 2012 R2 v2.3.1 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2016 with IIS 10.0 version 1.2.0** | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0** | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0** | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 with IIS 8 version 1.2.0** | _64bit Windows Server 2012 v1.2.0 running IIS 8_ | .NET Core 2.2.8, supports 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 |
| **Windows Server 2012 R2 with IIS 8.5** | _64bit Windows Server 2012 R2 running IIS 8.5_ | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5** | _64bit Windows Server Core 2012 R2 running IIS 8.5_ | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 with IIS 8** | _64bit Windows Server 2012 running IIS 8_ | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 | #### More details
| Platform Version | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X‑Ray |
| --- | --- | --- | --- | --- | --- | --- |
| **Windows Server 2016 with IIS 10.0 version 2.3.1** | 2019.11.13 | 3.15.876 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.722.0 | 3.6 | 3.1.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.3.1** | 2019.11.13 | 3.15.876 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.722.0 | 3.6 | 3.1.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.3.1** | 2019.11.13 | 3.15.876 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.1** | 2019.11.13 | 3.15.876 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 |
| **Windows Server 2016 with IIS 10.0 version 1.2.0** | 2019.11.13 | 3.15.876 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.722.0 | 3.6 | 3.1.0 |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0** | 2019.11.13 | 3.15.876 | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.722.0 | 3.6 | 3.1.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0** | 2019.11.13 | 3.15.876 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.11.13 | 3.15.876 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 |
| **Windows Server 2012 with IIS 8 version 1.2.0** | 2019.11.13 | 3.15.876 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 |
| **Windows Server 2012 R2 with IIS 8.5** | 2019.11.13 | 3.15.876 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5** | 2019.11.13 | 3.15.876 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 |
| **Windows Server 2012 with IIS 8** | 2019.11.13 | 3.15.876 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 |
