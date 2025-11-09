# Release: AWS Elastic Beanstalk Windows Server platform update on September 24, 2019

This release applies Windows September 2019 security updates to the Windows Server platform for Elastic Beanstalk, and updates platform
versions. The release also adds Amazon EC2 instance types in certain AWS Regions.

**Release date:** September 24, 2019

## Changes

| **Category**                 | **Description**                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- | ---------------- | ---- | ------- | ------- | ---- | ------------- | -------------------------------------------------------------- | --- |
| **Windows security updates** | Applied September 2019 security updates for Windows.<br>See Microsoft's [Security TechCenter](https://portal.msrc.microsoft.com/en-us/ "https://portal.msrc.microsoft.com/en-us/") and [Security Advisories and Bulletins](https://technet.microsoft.com/en-us/library/security/ "https://technet.microsoft.com/en-us/library/security/"). |
| **Instance types**           | Added support for more Amazon EC2 instance types in some AWS Regions, as follows:<br>                                                                                                                                                                                                                                                      | \*_Instance types_<br>• | \*_Regions_<br>• | <br> | --<br>• | --<br>• | <br> | \*_i3en_<br>• | • US East (Ohio) – us-east-2<br>• Europe (Ireland) – eu-west-1 |     |

## New platform versions

### .NET on Windows Server with IIS

#### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.2.2**               | _64bit Windows Server 2016 v2.2.2 running IIS 10.0_        | .NET Core 2.2.7, supports 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.2.2**          | _64bit Windows Server Core 2016 v2.2.2 running IIS 10.0_   | .NET Core 2.2.7, supports 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.2.2**             | _64bit Windows Server 2012 R2 v2.2.2 running IIS 8.5_      | .NET Core 2.2.7, supports 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.2** | _64bit Windows Server Core 2012 R2 v2.2.2 running IIS 8.5_ | .NET Core 2.2.7, supports 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

#### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X‑Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.2.2**               | 2019.09.11  | 3.15.826         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.2.2**          | 2019.09.11  | 3.15.826         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.2.2**             | 2019.09.11  | 3.15.826         | 4.9.3519                                                                                                  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.2** | 2019.09.11  | 3.15.826         | 4.9.3519                                                                                                  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.09.11  | 3.15.826         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.09.11  | 3.15.826         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.09.11  | 3.15.826         | 4.9.3519                                                                                                  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.09.11  | 3.15.826         | 4.9.3519                                                                                                  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.09.11  | 3.15.826         | 4.9.3519                                                                                                  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.09.11  | 3.15.826         | 4.9.3519                                                                                                  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.09.11  | 3.15.826         | 4.9.3519                                                                                                  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.09.11  | 3.15.826         | 4.9.3519                                                                                                  | 2.3.634.0 | 3.6        | 3.1.0     |
