

# Release: Elastic Beanstalk Windows Server platform update on October 28, 2026
<a name="release-2026-10-28-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release updates framework and AWS components.

**Release date:** October 28, 2026

To update your environments to the new platform versions, see [Updating your Elastic Beanstalk environment's platform version](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.platform.upgrade.html) in the *AWS Elastic Beanstalk Developer Guide*. If you've turned on [managed platform updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-platform-update-managed.html), Elastic Beanstalk applies the new platform versions to your environments during their weekly maintenance window.

## Changes
<a name="release-2026-10-28-windows.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 10 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.14/10.0.14.md">10.0.14</a>.<br />Updated .NET 9 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.22/9.0.22.md">9.0.22</a>.<br />Updated .NET 8 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.33/8.0.33.md">8.0.33</a>.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>X-Ray daemon</b></td><td>Updated the X-Ray daemon to version <a href="https://github.com/aws/aws-xray-daemon/blob/master/CHANGELOG.md#371-2026-10-21">3.7.1</a>.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2026-10-28-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2026-10-28-windows.platforms.net)

### .NET on Windows Server
<a name="release-2026-10-28-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.8**  |  * 64bit Windows Server 2025 v2.23.8 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.8**  |  * 64bit Windows Server Core 2025 v2.23.8 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.8**  |  * 64bit Windows Server 2022 v2.23.8 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.8**  |  * 64bit Windows Server Core 2022 v2.23.8 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.8**  |  * 64bit Windows Server 2019 v2.23.8 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.8**  |  * 64bit Windows Server Core 2019 v2.23.8 running IIS 10.0 *  | .NET 10.0.14, supports 10.0.14, 9.0.22, 8.0.33<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.8**  | 2026.10.14 |  | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.8**  | 2026.10.14 |  | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.8**  | 2026.10.14 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.8**  | 2026.10.14 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.8**  | 2026.10.14 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.8**  | 2026.10.14 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.1 | 