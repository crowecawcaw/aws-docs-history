# Release: Elastic Beanstalk Windows Server platform update on

June 26, 2023

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates.
It also updates framework and AWS components.

**Release date:** June 26, 2023

###### Important

Customers with Elastic Beanstalk environments on the following platform versions are advised to
upgrade each of their corresponding environments to Windows platform version 2.10.7 or later,
released on [Dec 28,
2022](release-2022-12-28-windows.md "release-2022-12-28-windows.md").

- Windows Server 2016 — platform version 2.10.6 or prior versions
- Windows Server 2012 — platform version 2.10.6 or prior versions
- Windows Server 2008 — (all platform versions)
  An upcoming TLS configuration change to all AWS API endpoints is scheduled to begin on
  June 28, 2023. This change will impact availability for your environments that run on the
  listed platform versions. Impacted actions include, but aren’t limited to, the following:
  configuration deployments, application deployments, auto scaling, new environment launch, log
  rotation, and enhanced health reports. For more information, see [Updating your Elastic
  Beanstalk environment's platform version](../dg/using-features.platform.md "../dg/using-features.platform.md") in the
  _AWS Elastic Beanstalk Developer Guide_.

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                 | **Description**                                                                                                                                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows security updates** | Applied June 2023 security updates for Windows. See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance "https://portal.msrc.microsoft.com/en-us/security-guidance"). |
| **Framework updates**        |
| **Framework**                | **Details**                                                                                                                                                                                                       |
| ---                          | ---                                                                                                                                                                                                               |
| **.NET Core**                | Updated .NET 6 to version 6.0.18 on Windows Server 2019 and 2016 platform versions.                                                                                                                               |
|                              | **AWS component updates**                                                                                                                                                                                         |
| **Component**                | **Details**                                                                                                                                                                                                       |
| ---                          | ---                                                                                                                                                                                                               |
| **AMI**                      | Updated the base AMI to version 2023.06.14.                                                                                                                                                                       |

| ## New platform versions ### .NET on Windows Server #### Configuration basics
| Platform Version | Solution Stack Name | Framework | Proxy Server |
| --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.11.5** | _64bit Windows Server 2019 v2.11.5 running IIS 10.0_ | .NET 6.0.18, supports 6.0.18, 3.1.32 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.5** | _64bit Windows Server Core 2019 v2.11.5 running IIS 10.0_ | .NET 6.0.18, supports 6.0.18, 3.1.32 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2016 with IIS 10.0 version 2.11.5** | _64bit Windows Server 2016 v2.11.5 running IIS 10.0_ | .NET 6.0.18, supports 6.0.18, 3.1.32 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.5** | _64bit Windows Server Core 2016 v2.11.5 running IIS 10.0_ | .NET 6.0.18, supports 6.0.18, 3.1.32 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.5** | _64bit Windows Server 2012 R2 v2.11.5 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.5** | _64bit Windows Server Core 2012 R2 v2.11.5 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30 .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | #### More details
| Platform Version | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --- | --- | --- | --- | --- | --- | --- |
| **Windows Server 2019 with IIS 10.0 version 2.11.5** | 2023.06.14 | 3.7.568.0 | | 3.1.2144.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.5** | 2023.06.14 | 3.7.568.0 | | 3.1.2144.0 | 3.6 | 3.2.0 |
| **Windows Server 2016 with IIS 10.0 version 2.11.5** | 2023.06.14 | 3.7.568.0 | | 3.1.2144.0 | 3.6 | 3.2.0 |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.5** | 2023.06.14 | 3.7.568.0 | | 3.1.2144.0 | 3.6 | 3.2.0 |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.5** | 2023.06.14 | 3.7.568.0 | | 3.1.2144.0 | 3.6 | 3.2.0 |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.5** | 2023.06.14 | 3.7.568.0 | 4.9.5288 | 3.1.2144.0 | 3.6 | 3.2.0 |
