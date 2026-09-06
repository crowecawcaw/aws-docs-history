

# Release: Elastic Beanstalk Windows Server platform update on December 28, 2022
<a name="release-2022-12-28-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** December 28, 2022

**Windows Platform Version 2.10.7**  
This release introduced TLS v1.2 to Elastic Beanstalk platform branches *Windows Server 2016* and *Windows Server 2012*. Subsequent releases of these platform branches include TLS v1.2 or later versions. Note that *Windows Server 2012* is now [retired](release-2023-12-04-windows-2012-retire.md). For a list of the most recent and supported Windows Server platform versions, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.net) in the *AWS Elastic Beanstalk Platforms* guide.  
As of December 31 2023, AWS started fully enforcing TLS 1.2 across all AWS API endpoints. As a result, any environments running Windows platform versions that are older than the versions of *Windows Server 2016* and *Windows Server 2012* in this release still use TLS 1.0 and 1.1. Applications running on these older versions, may no longer be able to perform actions such as configuration deployments, application deployments, auto scaling, new environment launch, log rotation and enhanced health reports.  
To avoid the risk of availability impact, please upgrade your platform versions to a newer version as soon as possible.

## Changes
<a name="release-2022-12-28-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied December 2022 security updates for Windows.<br />See the Microsoft <a href="https://msrc.microsoft.com/update-guide/en-us">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 6 to version 6.0.12 on Windows Server 2019 and 2016 platform versions.<br />Updated .NET 3 to version 3.1.32 on Windows Server 2019 and 2016 platform versions.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.15.1886.</td></tr>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2022.12.14</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.247356.0b252264.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version 3.1.1856.0.</td></tr>
  <tr><td><b>EC2Launch</b></td><td>Updated EC2Launch V2 to version 2.0.1082.</td></tr>
  <tr><td><b>EC2Config</b></td><td>Updated EC2Config to version 4.9.5103 on Windows Server 2012 R2 Server Core platform versions.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2022-12-28-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2022-12-28-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.10.7**  |  * 64bit Windows Server 2019 v2.10.7 running IIS 10.0 *  | .NET 6.0.12, supports 6.0.12, 5.0.17, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.10.7**  |  * 64bit Windows Server Core 2019 v2.10.7 running IIS 10.0 *  | .NET 6.0.12, supports 6.0.12, 5.0.17, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.10.7**  |  * 64bit Windows Server 2016 v2.10.7 running IIS 10.0 *  | .NET 6.0.12, supports 6.0.12, 5.0.17, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.10.7**  |  * 64bit Windows Server Core 2016 v2.10.7 running IIS 10.0 *  | .NET 6.0.12, supports 6.0.12, 5.0.17, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.10.7**  |  * 64bit Windows Server 2012 R2 v2.10.7 running IIS 8.5 *  | .NET Core 2.1.30, supports 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.7**  |  * 64bit Windows Server Core 2012 R2 v2.10.7 running IIS 8.5 *  | .NET Core 2.1.30, supports 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.10.7**  | 2022.12.14 | 3.15.1886 |  | 3.1.1856.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.10.7**  | 2022.12.14 | 3.15.1886 |  | 3.1.1856.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.10.7**  | 2022.12.14 | 3.15.1886 |  | 3.1.1856.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.10.7**  | 2022.12.14 | 3.15.1886 |  | 3.1.1856.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.10.7**  | 2022.12.14 | 3.15.1886 |  | 3.1.1856.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.7**  | 2022.12.14 | 3.15.1886 | 4.9.5103 | 3.1.1856.0 | 3.6 | 3.2.0 | 