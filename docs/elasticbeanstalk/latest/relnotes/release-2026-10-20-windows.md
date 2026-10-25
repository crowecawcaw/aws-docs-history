

# Release: Elastic Beanstalk Windows Server platform update on October 20, 2026
<a name="release-2026-10-20-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** October 20, 2026

To update your environments to the new platform versions, see [Updating your Elastic Beanstalk environment's platform version](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.platform.upgrade.html) in the *AWS Elastic Beanstalk Developer Guide*. If you've turned on [managed platform updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-platform-update-managed.html), Elastic Beanstalk applies the new platform versions to your environments during their weekly maintenance window.

## Changes
<a name="release-2026-10-20-windows.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied October 2026 security updates for Windows.<br />This release includes updates from the monthly Microsoft <i>Patch Tuesday</i> Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 10 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.13/10.0.13.md">10.0.13</a>.<br />Updated .NET 9 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.21/9.0.21.md">9.0.21</a>.<br />Updated .NET 8 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.32/8.0.32.md">8.0.32</a>.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2026.10.14.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version <a href="https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.5390.0">3.3.5390.0</a>.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version <a href="https://github.com/aws/amazon-cloudwatch-agent/releases/tag/v1.300074.0">1.300074.0b1920</a>.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>Additional changes with this release</b></td><td>For environments that join instances to an Active Directory domain, each instance now records its domain-join status in the environment's Amazon S3 bucket when it launches. Environments without Active Directory options are unaffected.</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2026-10-20-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2026-10-20-windows.platforms.net)

### .NET on Windows Server
<a name="release-2026-10-20-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.7**  |  * 64bit Windows Server 2025 v2.23.7 running IIS 10.0 *  | .NET 10.0.13, supports 10.0.13, 9.0.21, 8.0.32<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.7**  |  * 64bit Windows Server Core 2025 v2.23.7 running IIS 10.0 *  | .NET 10.0.13, supports 10.0.13, 9.0.21, 8.0.32<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.7**  |  * 64bit Windows Server 2022 v2.23.7 running IIS 10.0 *  | .NET 10.0.13, supports 10.0.13, 9.0.21, 8.0.32<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.7**  |  * 64bit Windows Server Core 2022 v2.23.7 running IIS 10.0 *  | .NET 10.0.13, supports 10.0.13, 9.0.21, 8.0.32<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.7**  |  * 64bit Windows Server 2019 v2.23.7 running IIS 10.0 *  | .NET 10.0.13, supports 10.0.13, 9.0.21, 8.0.32<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.7**  |  * 64bit Windows Server Core 2019 v2.23.7 running IIS 10.0 *  | .NET 10.0.13, supports 10.0.13, 9.0.21, 8.0.32<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.7**  | 2026.10.14 |  | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.7**  | 2026.10.14 |  | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.7**  | 2026.10.14 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.7**  | 2026.10.14 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.7**  | 2026.10.14 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.7**  | 2026.10.14 | 3.7.1252.1 | 2.5.2 | 3.3.5390.0 | 4.0 | 3.7.0 | 