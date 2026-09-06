

# Release: Elastic Beanstalk Windows Server platform update on August 18, 2026
<a name="release-2026-08-18-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components. In addition, this release adds support for automatically joining Windows Server instances to an Active Directory domain.

**Release date:** August 18, 2026

## Changes
<a name="release-2026-08-18-windows.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied August 2026 security updates for Windows.<br />This release includes updates from the monthly Microsoft <i>Patch Tuesday</i> Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 10 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.11/10.0.11.md">10.0.11</a>.<br />Updated .NET 9 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.19/9.0.19.md">9.0.19</a>.<br />Updated .NET 8 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.30/8.0.30.md">8.0.30</a>.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2026.08.12.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version <a href="https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.4851.0">3.3.4851.0</a>.</td></tr>
  <tr><td><b>EC2Launch</b></td><td>Updated EC2Launch to version <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launchv2-versions.html">2.5.2</a>.</td></tr>
  <tr><td><b>X-Ray daemon</b></td><td>Updated the X-Ray daemon to version <a href="https://github.com/aws/aws-xray-daemon/releases/tag/v3.6.7">3.6.7</a>.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version <a href="https://github.com/aws/amazon-cloudwatch-agent/releases/tag/v1.300071.0">1.300071.0b1720</a>.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>Additional changes with this release</b></td><td> <ul><li> Windows Server environments can now automatically join their instances to an Active Directory domain that you manage with AWS Directory Service. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-activedirectory.html">Joining instances to an Active Directory domain</a>. </li></ul> </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2026-08-18-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2026-08-18-windows.platforms.net)

### .NET on Windows Server
<a name="release-2026-08-18-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server 2025 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server Core 2025 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server 2022 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server Core 2022 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server 2019 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server Core 2019 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server 2016 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server Core 2016 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.4**  | 2026.08.12 |  | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.4**  | 2026.08.12 |  | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 