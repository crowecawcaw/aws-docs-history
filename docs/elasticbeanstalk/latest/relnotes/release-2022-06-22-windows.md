

# Release: Elastic Beanstalk Windows Server platform update on June 22, 2022
<a name="release-2022-06-22-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components and includes a platform branch retirement announcement.

**Release date:** June 22, 2022

## Changes
<a name="release-2022-06-22-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied June 2022 security updates for Windows.<br />See the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Platform branch retirement</b></td><td>Today we're announcing the retirement of platform branch <b>Windows Server 2012 with IIS 8</b>. This retired platform branch is composed of two platform versions: <i>Windows Server 2012 with IIS 8</i> <b>version 0.1.0</b> and <i>Windows Server 2012 with IIS 8</i> <b>version 1.2.0</b>. <br />If you currently use this retiring platform branch, we strongly recommend that you migrate to one of the <i>Windows Server version 2</i> platforms, which are current and fully supported:<ul><li> Windows Server 2019 with IIS 10.0 version 2.x </li><li> Windows Server 2016 with IIS 10.0 version 2.x </li><li> Windows Server 2012 R2 with IIS 8.5 version 2.x </li></ul><br />For full migration considerations, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-v2migration.html">Major Version Migration</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>. <br />For more information and a listing of retired platform components, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html">Elastic Beanstalk platform support policy</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 6 to version 6.0.6 on Windows Server 2019 and 2016 platform versions.<br />Updated .NET 3 to version 3.1.26 on Windows Server 2019 and 2016 platform versions.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.15.1678.</td></tr>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2022.06.15.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.247352.0.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version 3.1.1188.0</td></tr>
  <tr><td><b>EC2Config</b></td><td>Updated EC2Config to version 4.9.4588 on Windows Server 2012 R2 Server Core platform versions.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2022-06-22-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2022-06-22-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.10.1**  |  * 64bit Windows Server 2019 v2.10.1 running IIS 10.0 *  | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.10.1**  |  * 64bit Windows Server Core 2019 v2.10.1 running IIS 10.0 *  | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.10.1**  |  * 64bit Windows Server 2016 v2.10.1 running IIS 10.0 *  | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.10.1**  |  * 64bit Windows Server Core 2016 v2.10.1 running IIS 10.0 *  | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.10.1**  |  * 64bit Windows Server 2012 R2 v2.10.1 running IIS 8.5 *  | .NET Core 2.1.30, supports 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.1**  |  * 64bit Windows Server Core 2012 R2 v2.10.1 running IIS 8.5 *  | .NET Core 2.1.30, supports 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.10.1**  | 2022.06.15 | 3.15.1678 |  | 3.1.1188.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.10.1**  | 2022.06.15 | 3.15.1678 |  | 3.1.1188.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.10.1**  | 2022.06.15 | 3.15.1678 |  | 3.1.1188.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.10.1**  | 2022.06.15 | 3.15.1678 |  | 3.1.1188.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.10.1**  | 2022.06.15 | 3.15.1678 |  | 3.1.1188.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.1**  | 2022.06.15 | 3.15.1678 | 4.9.4588 | 3.1.1188.0 | 3.6 | 3.2.0 | 