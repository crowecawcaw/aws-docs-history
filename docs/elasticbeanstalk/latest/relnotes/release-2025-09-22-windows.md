

# Release: Elastic Beanstalk Windows Server platform update on September 22, 2025
<a name="release-2025-09-22-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release updates framework and AWS components and applies Windows security updates.

**Release date:** September 22, 2025

## Changes
<a name="release-2025-09-22-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied September 2025 security updates for Windows.<br />This release includes updates from the monthly Microsoft <i>Patch Tuesday</i> Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 9 to version 9.0.9.<br />Updated .NET 8 to version 8.0.20.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2025.09.10.</td></tr>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.7.1120.0.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.300059.0b1207.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version 3.3.3050.0.</td></tr>
  <tr><td><b>AWS X-Ray</b></td><td>Updated the X-Ray daemon to version 3.6.0.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>Additional changes with this release</b></td><td> <ul><li>  PowerShell 2.0 has been removed from Windows Server 2025 platforms in accordance with Microsoft's deprecation of this legacy version. For more information, see Microsoft's <a href="https://support.microsoft.com/en-us/topic/powershell-2-0-removal-from-windows-fe6d1edc-2ed2-4c33-b297-afe82a64200a">support article</a>.  </li><li>  In this release, the host rename was moved prior to platform bootstrapping.  </li></ul> </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2025-09-22-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2025-09-22-windows.platforms.net)

### .NET on Windows Server
<a name="release-2025-09-22-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.20.0**  |  * 64bit Windows Server 2025 v2.20.0 running IIS 10.0 *  | .NET 9.0.9, supports 9.0.9, 8.0.20<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.20.0**  |  * 64bit Windows Server Core 2025 v2.20.0 running IIS 10.0 *  | .NET 9.0.9, supports 9.0.9, 8.0.20<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.20.0**  |  * 64bit Windows Server 2022 v2.20.0 running IIS 10.0 *  | .NET 9.0.9, supports 9.0.9, 8.0.20<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.20.0**  |  * 64bit Windows Server Core 2022 v2.20.0 running IIS 10.0 *  | .NET 9.0.9, supports 9.0.9, 8.0.20<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.20.0**  |  * 64bit Windows Server 2019 v2.20.0 running IIS 10.0 *  | .NET 9.0.9, supports 9.0.9, 8.0.20<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.20.0**  |  * 64bit Windows Server Core 2019 v2.20.0 running IIS 10.0 *  | .NET 9.0.9, supports 9.0.9, 8.0.20<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.20.0**  |  * 64bit Windows Server 2016 v2.20.0 running IIS 10.0 *  | .NET 9.0.9, supports 9.0.9, 8.0.20<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.20.0**  |  * 64bit Windows Server Core 2016 v2.20.0 running IIS 10.0 *  | .NET 9.0.9, supports 9.0.9, 8.0.20<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.20.0**  | 2025.09.10 | 3.7.1120.0 |  | 3.3.3050.0 | 3.6 | 3.6.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.20.0**  | 2025.09.10 | 3.7.1120.0 |  | 3.3.3050.0 | 3.6 | 3.6.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.20.0**  | 2025.09.10 | 3.7.1120.0 |  | 3.3.3050.0 | 3.6 | 3.6.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.20.0**  | 2025.09.10 | 3.7.1120.0 |  | 3.3.3050.0 | 3.6 | 3.6.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.20.0**  | 2025.09.10 | 3.7.1120.0 |  | 3.3.3050.0 | 3.6 | 3.6.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.20.0**  | 2025.09.10 | 3.7.1120.0 |  | 3.3.3050.0 | 3.6 | 3.6.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.20.0**  | 2025.09.10 | 3.7.1120.0 |  | 3.3.3050.0 | 3.6 | 3.6.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.20.0**  | 2025.09.10 | 3.7.1120.0 |  | 3.3.3050.0 | 3.6 | 3.6.0 | 