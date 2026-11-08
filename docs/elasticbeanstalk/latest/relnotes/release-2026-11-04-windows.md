

# Release: Elastic Beanstalk Windows Server platform update on November 4, 2026
<a name="release-2026-11-04-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates AWS components.

**Release date:** November 4, 2026

To update your environments to the new platform versions, see [Updating your Elastic Beanstalk environment's platform version](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.platform.upgrade.html) in the *AWS Elastic Beanstalk Developer Guide*. If you've turned on [managed platform updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-platform-update-managed.html), Elastic Beanstalk applies the new platform versions to your environments during their weekly maintenance window.

## Changes
<a name="release-2026-11-04-windows.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied the October 2026 out-of-band Windows updates that Microsoft released after the October <i>Patch Tuesday</i> release. These updates refresh the trusted root certificates, so instances start with current trusted root certificates even if they can't reach Microsoft's certificate update service.<br />For more details and a list of security updates, see the Microsoft <a href="https://msrc.microsoft.com/update-guide/en-us">Security Update Guide</a>.</td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2026.10.28.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2026-11-04-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2026-11-04-windows.platforms.net)

### .NET on Windows Server
<a name="release-2026-11-04-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.9**  |  * 64bit Windows Server 2025 v2.23.9 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.9**  |  * 64bit Windows Server Core 2025 v2.23.9 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.9**  |  * 64bit Windows Server 2022 v2.23.9 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.9**  |  * 64bit Windows Server Core 2022 v2.23.9 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.9**  |  * 64bit Windows Server 2019 v2.23.9 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.9**  |  * 64bit Windows Server Core 2019 v2.23.9 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.9**  | 2026.10.28 |  | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.9**  | 2026.10.28 |  | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.9**  | 2026.10.28 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.9**  | 2026.10.28 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.9**  | 2026.10.28 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.9**  | 2026.10.28 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 