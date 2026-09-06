

# Release: Elastic Beanstalk Windows Server platform update on June 18, 2026
<a name="release-2026-06-18-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** June 18, 2026

## Changes
<a name="release-2026-06-18-windows.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied June 2026 security updates for Windows.<br />This release includes updates from the monthly Microsoft <i>Patch Tuesday</i> Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 10 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.9/10.0.9.md">10.0.9</a>.<br />Updated .NET 9 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.17/9.0.17.md">9.0.17</a>.<br />Updated .NET 8 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.28/8.0.28.md">8.0.28</a>.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2026.06.10.</td></tr>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version <a href="https://github.com/aws/aws-sdk-net/releases/tag/3.7.1252.1">3.7.1252.1</a> (Windows Server 2016, 2019, and 2022 platforms only).</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version <a href="https://github.com/aws/amazon-cloudwatch-agent/releases/tag/v1.300069.0">1.300069.0b1529</a>.</td></tr>
  <tr><td><b>EC2Launch</b></td><td>Updated EC2Launch to version 2.5.1.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version <a href="https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.4515.0">3.3.4515.0</a>.</td></tr>
  <tr><td><b>X-Ray daemon</b></td><td>Updated the X-Ray daemon to version <a href="https://github.com/aws/aws-xray-daemon/releases/tag/v3.6.5">3.6.5</a>.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2026-06-18-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2026-06-18-windows.platforms.net)

### .NET on Windows Server
<a name="release-2026-06-18-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server 2025 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server Core 2025 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server 2022 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server Core 2022 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server 2019 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server Core 2019 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server 2016 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server Core 2016 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.2**  | 2026.06.10 |  | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.2**  | 2026.06.10 |  | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 | 