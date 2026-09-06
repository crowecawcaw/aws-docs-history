

# Release: Elastic Beanstalk Windows Server platform update on April 22, 2026
<a name="release-2026-04-22-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components. This release adds AI-powered environment analysis and deployment logs to Windows Server platforms.

**Release date:** April 22, 2026

## Changes
<a name="release-2026-04-22-windows.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied April 2026 security updates for Windows.<br />This release includes updates from the monthly Microsoft <i>Patch Tuesday</i> Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 10 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.7/10.0.7.md">10.0.7</a>.<br />Updated .NET 9 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.15/9.0.15.md">9.0.15</a>.<br />Updated .NET 8 to version <a href="https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.26/8.0.26.md">8.0.26</a>.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2026.04.15.</td></tr>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version <a href="https://github.com/aws/aws-sdk-net/releases/tag/3.7.1251.0">3.7.1251.0</a>.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version <a href="https://github.com/aws/amazon-cloudwatch-agent/releases/tag/v1.300066.1">1.300066.1b1374</a>.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version <a href="https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.4121.0">3.3.4121.0</a>.</td></tr>
  <tr><td><b>X-Ray daemon</b></td><td>Updated the X-Ray daemon to version <a href="https://github.com/aws/aws-xray-daemon/releases/tag/v3.6.2">3.6.2</a>.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>Additional changes with this release</b></td><td>This release adds AI-powered environment analysis to Windows Server platforms. This feature uses Amazon Bedrock to analyze environment health issues and provide actionable recommendations. It is available through the Elastic Beanstalk console and AWS CLI for environments with enhanced health reporting enabled. To learn more about this feature, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-ai-analysis.html">AI-powered environment analysis</a>.<br />This release adds deployment logs to Windows Server platforms. You can now view step-by-step deployment logs directly from the Deployments tab in the Elastic Beanstalk console, including while a deployment is still in progress. To learn more, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-deployment-logs.html">Deployment logs</a>.</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2026-04-22-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2026-04-22-windows.platforms.net)

### .NET on Windows Server
<a name="release-2026-04-22-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server 2025 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server Core 2025 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server 2022 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server Core 2022 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server 2019 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server Core 2019 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server 2016 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server Core 2016 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 | 