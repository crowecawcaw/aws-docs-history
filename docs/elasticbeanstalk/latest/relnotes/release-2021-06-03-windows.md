

# Release: Elastic Beanstalk Windows Server platform update on June 3, 2021
<a name="release-2021-06-03-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components and includes a platform deprecation announcement.

**Release date:** June 3, 2021

## Changes
<a name="release-2021-06-03-windows.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied May 2021 security updates for Windows.<br />See the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Platform deprecation</b></td><td>Today we're announcing that platform branch <b>Windows Server 2012 with IIS 8</b> <i>will retire on May 31, 2022</i>. <i>This platform branch is now deprecated.</i> This retiring platform branch is composed of two platform versions: <i>Windows Server 2012 with IIS 8</i> <b>version 0.1.0</b> and <i>Windows Server 2012 with IIS 8</i> <b>version 1.2.0</b>. <br />If you currently use this retiring platform branch, we strongly recommend that you start planning your migration to one of the <i>Windows Server version 2</i> platforms, which are current and fully supported:<ul><li> Windows Server 2019 with IIS 10.0 version 2.x </li><li> Windows Server 2016 with IIS 10.0 version 2.x </li><li> Windows Server 2012 R2 with IIS 8.5 version 2.x </li></ul><br />For full migration considerations, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-v2migration.html">Major Version Migration</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>. <br />Deprecated platform branches aren't listed on the <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html">Supported platforms</a> page of the <i>AWS Elastic Beanstalk Platforms</i> guide. They are listed on a separate page, <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html">Retiring platform versions</a>.<br />For more information about platform deprecation, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html">Elastic Beanstalk platform support policy</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET Core 2.1 to version 2.1.28.<br />Updated .NET Core 3 to version 3.1.15 on Windows Server 2019 and 2016 platform versions.<br />Updated .NET 5 to version 5.0.6 on Windows Server 2019 and 2016 platform versions.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.15.1302.</td></tr>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2021.05.11.</td></tr>
  <tr><td><b>EC2Config</b></td><td>Updated EC2Config to version 4.9.4381 on Windows Server 2012 platform versions.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.247347.6.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2021-06-03-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2021-06-03-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.6.6**  |  * 64bit Windows Server 2019 v2.6.6 running IIS 10.0 *  | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.6.6**  |  * 64bit Windows Server Core 2019 v2.6.6 running IIS 10.0 *  | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.6.6**  |  * 64bit Windows Server 2016 v2.6.6 running IIS 10.0 *  | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.6.6**  |  * 64bit Windows Server Core 2016 v2.6.6 running IIS 10.0 *  | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.6.6**  |  * 64bit Windows Server 2012 R2 v2.6.6 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.6**  |  * 64bit Windows Server Core 2012 R2 v2.6.6 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.6.6**  | 2021.05.11 | 3.15.1302 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.6.6**  | 2021.05.11 | 3.15.1302 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.6.6**  | 2021.05.11 | 3.15.1302 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.6.6**  | 2021.05.11 | 3.15.1302 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.6.6**  | 2021.05.11 | 3.15.1302 | 4.9.4381 | 3.0.529.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.6**  | 2021.05.11 | 3.15.1302 | 4.9.4381 | 3.0.529.0 | 3.6 | 3.2.0 | 