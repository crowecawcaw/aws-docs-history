

# Release: AWS Elastic Beanstalk Windows Server platform update to new major version 2 on February 21, 2019
<a name="release-2019-02-21-windows-v2"></a>

This release introduces Windows Server platform version 2 (v2)—a new major version that brings the platform closer to the Elastic Beanstalk Linux-based platforms.

**Release date:** February 21, 2019

## Changes
<a name="release-2019-02-21-windows-v2.changes"></a>

The release introduces Windows Server platform v2, a new major version that brings the Windows Server platform closer to the Elastic Beanstalk Linux-based platforms in several important ways.

The Windows Server platform now supports:
+ *Versioning* – Each release gets a new version number, and you can refer to past versions (that are still available to you) when creating and managing environments.
+ *Enhanced health*
+ *Immutable* and *Rolling with an Additional Batch* deployments
+ *Immutable updates*
+ *Managed platform updates*

Windows Server v2 platform versions have an increased default root volume size of 35 GB (up from 30 GB).

For full migration considerations, see [Major Version Migration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-v2migration.html) in the *AWS Elastic Beanstalk Developer Guide*.

**Notes**  
Elastic Beanstalk isn't updating Windows Server platform versions that use IIS versions earlier than 8.5 to the new v2 platform. These versions don't support the new platform features.
The Windows Server platform v2 doesn't support .NET Core 1.x and 2.0. If you'd like to migrate your application to , and your application uses one of these .NET Core versions, update your application to a .NET Core version that v2 supports. For a list of supported versions, see [.NET on Windows Server with IIS](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.net) in the *AWS Elastic Beanstalk Platforms*.
The deployment and update features that are new to Windows Server v2 depend on enhanced health. When you migrate an environment to v2, enhanced health is disabled. Enable it to use these features. For details, see [Enabling AWS Elastic Beanstalk Enhanced Health Reporting](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-enable.html) in the *AWS Elastic Beanstalk Developer Guide*.

To get enhanced health reporting in the Elastic Beanstalk Command Line Interface (EB CLI) for Windows Server platform v2, you need the latest EB CLI version—3.14.6 or later. Here's how to get it:
+ To install the eb CLI: `pip install awsebcli` (for details, see [Install the EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html))
+ To upgrade: `pip install awsebcli --upgrade`
+ To verify the EB CLI version: `eb --version`

## New platform versions
<a name="release-2019-02-21-windows-v2.platforms"></a>

### .NET on Windows Server with IIS
<a name="release-2019-02-21-windows-v2.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 2.0.1**  |  * 64bit Windows Server 2016 v2.0.1 running IIS 10.0 *  | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 2.0.1**  |  * 64bit Windows Server Core 2016 v2.0.1 running IIS 10.0 *  | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 2.0.1**  |  * 64bit Windows Server 2012 R2 v2.0.1 running IIS 8.5 *  | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.1**  |  * 64bit Windows Server Core 2012 R2 v2.0.1 running IIS 8.5 *  | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 2.0.1**  | 2019.02.13 | 3.15.666 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.444.0 | 3.6 | 3.0.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 2.0.1**  | 2019.02.13 | 3.15.666 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.444.0 | 3.6 | 3.0.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 2.0.1**  | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 3.0.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.1**  | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 3.0.0 | 