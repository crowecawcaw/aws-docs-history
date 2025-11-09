# Release: AWS Elastic Beanstalk Windows Server platform update to new major version 2 on February 21, 2019

This release introduces Windows Server platform version 2 (v2)—a new major version that brings the platform closer to the
Elastic Beanstalk Linux-based platforms.

**Release date:** February 21, 2019

## Changes

The release introduces Windows Server platform v2, a new major version that brings the Windows Server platform closer to the Elastic Beanstalk Linux-based
platforms in several important ways.

The Windows Server platform now supports:

- _Versioning_ – Each release gets a new version number, and you can refer to past versions (that are still available to
  you) when creating and managing environments.
- _Enhanced health_
- _Immutable_ and _Rolling with an Additional Batch_ deployments
- _Immutable updates_
- _Managed platform updates_

Windows Server v2 platform versions have an increased default root volume size of 35 GB (up from 30 GB).

For full migration considerations, see [Major Version Migration](../dg/dotnet-v2migration.md "../dg/dotnet-v2migration.md") in the
_AWS Elastic Beanstalk Developer Guide_.

###### Notes

- Elastic Beanstalk isn't updating Windows Server platform versions that use IIS versions earlier than 8.5 to the new v2 platform. These versions don't
  support the new platform features.
- The Windows Server platform v2 doesn't support .NET Core 1.x and 2.0. If you'd like to migrate your application to , and your application uses
  one of these .NET Core versions, update your application to a .NET Core version that v2 supports. For a list of supported versions, see [.NET on Windows Server with IIS](../platforms/platforms-supported.md#platforms-supported.net "../platforms/platforms-supported.md#platforms-supported.net") in the
  _AWS Elastic Beanstalk Platforms_.
- The deployment and update features that are new to Windows Server v2 depend on enhanced health. When you migrate an environment to v2, enhanced
  health is disabled. Enable it to use these features. For details, see [Enabling AWS Elastic Beanstalk
  Enhanced Health Reporting](../dg/health-enhanced-enable.md "../dg/health-enhanced-enable.md") in the _AWS Elastic Beanstalk Developer Guide_.

To get enhanced health reporting in the Elastic Beanstalk Command Line Interface (EB CLI) for Windows Server platform v2, you need the latest EB CLI
version—3.14.6 or later. Here's how to get it:

- To install the eb CLI: `pip install awsebcli` (for details, see [Install the EB CLI](../dg/eb-cli3-install.md "../dg/eb-cli3-install.md"))
- To upgrade: `pip install awsebcli --upgrade`
- To verify the EB CLI version: `eb --version`

## New platform versions

### .NET on Windows Server with IIS

#### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                              | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.0.1**               | _64bit Windows Server 2016 v2.0.1 running IIS 10.0_        | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.0.1**          | _64bit Windows Server Core 2016 v2.0.1 running IIS 10.0_   | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.0.1**             | _64bit Windows Server 2012 R2 v2.0.1 running IIS 8.5_      | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.1** | _64bit Windows Server Core 2012 R2 v2.0.1 running IIS 8.5_ | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |

#### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X‑Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.0.1**               | 2019.02.13  | 3.15.666         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.0.1**          | 2019.02.13  | 3.15.666         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.0.1**             | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.1** | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 3.0.0     |
