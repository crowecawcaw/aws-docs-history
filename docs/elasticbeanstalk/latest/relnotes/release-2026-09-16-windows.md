

# Release: Elastic Beanstalk Windows Server platform update on September 16, 2026
<a name="release-2026-09-16-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** September 16, 2026

## Changes
<a name="release-2026-09-16-windows.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied September 2026 security updates for Windows.<br />This release includes updates from the monthly Microsoft <i>Patch Tuesday</i> Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 10 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.12/10.0.12.md">10.0.12</a>.<br />Updated .NET 9 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.20/9.0.20.md">9.0.20</a>.<br />Updated .NET 8 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.31/8.0.31.md">8.0.31</a>.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2026.09.09.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version <a href="https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.5226.0">3.3.5226.0</a>.</td></tr>
  <tr><td><b>X-Ray daemon</b></td><td>Updated the X-Ray daemon to version <a href="https://github.com/aws/aws-xray-daemon/releases/tag/v3.7.0">3.7.0</a>.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version <a href="https://github.com/aws/amazon-cloudwatch-agent/releases/tag/v1.300072.0">1.300072.0b1766</a>.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2026-09-16-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2026-09-16-windows.platforms.net)

### .NET on Windows Server
<a name="release-2026-09-16-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.5**  |  * 64bit Windows Server 2025 v2.23.5 running IIS 10.0 *  | .NET 10.0.12, supports 10.0.12, 9.0.20, 8.0.31<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.5**  |  * 64bit Windows Server Core 2025 v2.23.5 running IIS 10.0 *  | .NET 10.0.12, supports 10.0.12, 9.0.20, 8.0.31<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.5**  |  * 64bit Windows Server 2022 v2.23.5 running IIS 10.0 *  | .NET 10.0.12, supports 10.0.12, 9.0.20, 8.0.31<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.5**  |  * 64bit Windows Server Core 2022 v2.23.5 running IIS 10.0 *  | .NET 10.0.12, supports 10.0.12, 9.0.20, 8.0.31<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.5**  |  * 64bit Windows Server 2019 v2.23.5 running IIS 10.0 *  | .NET 10.0.12, supports 10.0.12, 9.0.20, 8.0.31<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.5**  |  * 64bit Windows Server Core 2019 v2.23.5 running IIS 10.0 *  | .NET 10.0.12, supports 10.0.12, 9.0.20, 8.0.31<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.5**  |  * 64bit Windows Server 2016 v2.23.5 running IIS 10.0 *  | .NET 10.0.12, supports 10.0.12, 9.0.20, 8.0.31<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.5**  |  * 64bit Windows Server Core 2016 v2.23.5 running IIS 10.0 *  | .NET 10.0.12, supports 10.0.12, 9.0.20, 8.0.31<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.5**  | 2026.09.09 |  | 2.5.2 | 3.3.5226.0 | 4.0 | 3.7.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.5**  | 2026.09.09 |  | 2.5.2 | 3.3.5226.0 | 4.0 | 3.7.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.5**  | 2026.09.09 | 3.7.1252.1 | 2.5.2 | 3.3.5226.0 | 4.0 | 3.7.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.5**  | 2026.09.09 | 3.7.1252.1 | 2.5.2 | 3.3.5226.0 | 4.0 | 3.7.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.5**  | 2026.09.09 | 3.7.1252.1 | 2.5.2 | 3.3.5226.0 | 4.0 | 3.7.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.5**  | 2026.09.09 | 3.7.1252.1 | 2.5.2 | 3.3.5226.0 | 4.0 | 3.7.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.5**  | 2026.09.09 | 3.7.1252.1 | 2.5.2 | 3.3.5226.0 | 4.0 | 3.7.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.5**  | 2026.09.09 | 3.7.1252.1 | 2.5.2 | 3.3.5226.0 | 4.0 | 3.7.0 | 