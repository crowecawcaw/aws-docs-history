

# Release: Elastic Beanstalk Windows Server platform update on November 23, 2021
<a name="release-2021-11-23-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** November 23, 2021

## Changes
<a name="release-2021-11-23-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied November 2021 security updates for Windows.<br />See the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET Core 3 to version 3.1.21 on Windows Server 2019 and 2016 platform versions.<br />Updated .NET 5 to version 5.0.12 on Windows Server 2019 and 2016 platform versions.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.15.1451.</td></tr>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2021.11.10.</td></tr>
  <tr><td><b>EC2Launch</b></td><td>Updated EC2Config to EC2Launch v2 agent (version 2.0.651) on Windows 2012 R2 platform versions. (EC2Config remains on Windows 2012 R2 Server Core platform versions.)<br />Updated EC2Launch v1 agent to EC2Launch v2 agent (version 2.0.651) on Windows Server 2019 and 2016 platform versions.<br />For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2launch-v2.html">EC2Launch v2</a> in the <i>Amazon EC2 User Guide</i>.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2021-11-23-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2021-11-23-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.8.0**  |  * 64bit Windows Server 2019 v2.8.0 running IIS 10.0 *  | .NET 5.0.12, supports 5.0.12, 3.1.21, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.8.0**  |  * 64bit Windows Server Core 2019 v2.8.0 running IIS 10.0 *  | .NET 5.0.12, supports 5.0.12, 3.1.21, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.8.0**  |  * 64bit Windows Server 2016 v2.8.0 running IIS 10.0 *  | .NET 5.0.12, supports 5.0.12, 3.1.21, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.8.0**  |  * 64bit Windows Server Core 2016 v2.8.0 running IIS 10.0 *  | .NET 5.0.12, supports 5.0.12, 3.1.21, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.8.0**  |  * 64bit Windows Server 2012 R2 v2.8.0 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.0**  |  * 64bit Windows Server Core 2012 R2 v2.8.0 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.8.0**  | 2021.11.10 | 3.15.1451 |  | 3.1.338.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.8.0**  | 2021.11.10 | 3.15.1451 |  | 3.1.338.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.8.0**  | 2021.11.10 | 3.15.1451 |  | 3.1.338.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.8.0**  | 2021.11.10 | 3.15.1451 |  | 3.1.338.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.8.0**  | 2021.11.10 | 3.15.1451 | 4.9.4508 | 3.1.338.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.0**  | 2021.11.10 | 3.15.1451 | 4.9.4508 | 3.1.338.0 | 3.6 | 3.2.0 | 