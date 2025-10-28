# Recommendations for Windows Server retired components on Elastic Beanstalk

This topic provides recommendations if your applications are currently running on the retired Windows Server 2012 R2 platform branches. It also addresses the
deprecated support for the TLS 1.0 and 1.1 protocol versions on our AWS service API endpoints and the impacted platform branches.

## Windows Server 2012 R2 platform branches retired

Elastic Beanstalk retired Windows Server 2012 R2 platform branches on [December 4, 2023](../relnotes/release-2023-12-04-windows-2012-retire.md "../relnotes/release-2023-12-04-windows-2012-retire.md"), and made the AMIs associated with those
platforms private on April 10, 2024. This action prevents the launching of instances in your Windows Server 2012 environments that use the default
Beanstalk AMI.

If you have any environments running on retired Windows platform branches we recommend that you migrate them to one of the following Windows Server platforms,
which are current and fully supported:

- Windows Server 2022 with IIS 10.0 version 2.x
- Windows Server 2019 with IIS 10.0 version 2.x

For full migration considerations, see [Migrating from earlier major versions of the Windows server platform](dotnet-v2migration.md#dotnet-v2migration.migration "dotnet-v2migration.md#dotnet-v2migration.migration").

For more information about platform deprecation, see [Elastic Beanstalk platform support policy](platforms-support-policy.md "platforms-support-policy.md").

###### Note

If you cannot migrate to these fully supported platforms, we recommend using custom AMIs created with Windows Server 2012 R2 or Windows Server 2012
R2 Core AMIs as the base image, if you have not done so already. For detailed instructions, see [Preserving access to an Amazon Machine Image (AMI) for a retired platform](using-features.md "using-features.md"). Reach out to the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") if you need temporary
access to an AMI while you perform one of these migration steps.

## TLS 1.2 Compatibility

As of December 31, 2023, AWS started fully enforcing TLS 1.2 across all AWS API endpoints. This action removed the ability to use TLS versions 1.0
and 1.1 with all AWS APIs. This information was originally communicated on [June 28,
2022](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/ "https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/"). To avoid the risk of availability impact, upgrade any environments running the platform versions identified here to a newer version as soon
as possible, if you have not done so already.

###### Potential impact

Elastic Beanstalk platforms versions that run TLS v1.1 or earlier are impacted. This change impacts environment actions that include but are not limited
to the following: configuration deployments, application deployments, auto scaling, new environment launch, log rotation, enhanced health reports, and
publishing application logs to the Amazon S3 bucket that's associated with your applications.

###### Affected Windows Platform Versions

Customers with Elastic Beanstalk environments on the following platform version are advised to upgrade
each of their corresponding environments to Windows platform version 2.8.3 or later, released
on [Feb 18,
2022](../relnotes/release-2022-02-18-windows.md "../relnotes/release-2022-02-18-windows.md").

- Windows Server 2019 — platform version 2.8.2 or prior versions

Customers with Elastic Beanstalk environments on the following platform versions are advised to upgrade
each of their corresponding environments to Windows platform version 2.10.7 or later, released
on [Dec 28,
2022](../relnotes/release-2022-12-28-windows.md "../relnotes/release-2022-12-28-windows.md").

- Windows Server 2016 — platform version 2.10.6 or prior versions
- Windows Server 2012 — all platform versions; this platform was retired on [December 4, 2023](../relnotes/release-2023-12-04-windows-2012-retire.md "../relnotes/release-2023-12-04-windows-2012-retire.md")
- Windows Server 2008 — all platform versions; this platform was retired on [October 28,
  2019](../relnotes/release-2019-10-28-windows.md "../relnotes/release-2019-10-28-windows.md")

For a list of the most recent and supported Windows Server platform versions, see [Supported Platforms](../platforms/platforms-supported.md#platforms-supported.net "../platforms/platforms-supported.md#platforms-supported.net") in the _AWS Elastic Beanstalk Platforms_ guide.

For details and best practices about updating your environment, see [Updating your Elastic Beanstalk environment's platform version](using-features.platform.md "using-features.platform.md").
