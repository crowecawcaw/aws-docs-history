

# Release: Elastic Beanstalk Windows Server platform update on January 22, 2026
<a name="release-2026-01-22-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components, and adds support for extracting JSON keys from Secrets Manager secrets.

**Release date:** January 22, 2026

## Changes
<a name="release-2026-01-22-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied January 2026 security updates for Windows.<br />This release includes updates from the monthly Microsoft <i>Patch Tuesday</i> Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 9 to version 9.0.12.<br />Updated .NET 8 to version 8.0.23.<br />Updated .NET 10 to version 10.0.2.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2026.01.14.</td></tr>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.7.1201.0.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.300063.0b1323.</td></tr>
  <tr><td><b>EC2Launch</b></td><td>Updated EC2Launch V2 to version 2.3.108.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version 3.3.3270.0.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>Additional Changes</b></td><td>This release enables extracting specific fields from JSON-formatted Secrets Manager secrets. See <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.secrets.env-vars.html#AWSHowTo.secrets.json">Extracting JSON keys from Secrets Manager secrets</a> for more information.</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2026-01-22-windows.platforms"></a>

**Notes**  
The following tables list *only supported* platform branches. They do not list platform branches that are scheduled for retirement (deprecated). For full version information of Elastic Beanstalk *retiring* (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.

**Topics**
+ [.NET on Windows Server](#release-2026-01-22-windows.platforms.net)

### .NET on Windows Server
<a name="release-2026-01-22-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.22.1**  |  * 64bit Windows Server 2025 v2.22.1 running IIS 10.0 *  | .NET 10.0.2, supports 10.0.2, 9.0.12, 8.0.23<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.22.1**  |  * 64bit Windows Server Core 2025 v2.22.1 running IIS 10.0 *  | .NET 10.0.2, supports 10.0.2, 9.0.12, 8.0.23<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.22.1**  |  * 64bit Windows Server 2022 v2.22.1 running IIS 10.0 *  | .NET 10.0.2, supports 10.0.2, 9.0.12, 8.0.23<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.22.1**  |  * 64bit Windows Server Core 2022 v2.22.1 running IIS 10.0 *  | .NET 10.0.2, supports 10.0.2, 9.0.12, 8.0.23<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.22.1**  |  * 64bit Windows Server 2019 v2.22.1 running IIS 10.0 *  | .NET 10.0.2, supports 10.0.2, 9.0.12, 8.0.23<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.22.1**  |  * 64bit Windows Server Core 2019 v2.22.1 running IIS 10.0 *  | .NET 10.0.2, supports 10.0.2, 9.0.12, 8.0.23<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.22.1**  |  * 64bit Windows Server 2016 v2.22.1 running IIS 10.0 *  | .NET 10.0.2, supports 10.0.2, 9.0.12, 8.0.23<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.22.1**  |  * 64bit Windows Server Core 2016 v2.22.1 running IIS 10.0 *  | .NET 10.0.2, supports 10.0.2, 9.0.12, 8.0.23<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.22.1**  | 2026.01.14 | 3.7.1201.0 | 2.3.108 | 3.3.3270.0 | 4.0 | 3.6.1 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.22.1**  | 2026.01.14 | 3.7.1201.0 | 2.3.108 | 3.3.3270.0 | 4.0 | 3.6.1 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.22.1**  | 2026.01.14 | 3.7.1201.0 | 2.3.108 | 3.3.3270.0 | 4.0 | 3.6.1 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.22.1**  | 2026.01.14 | 3.7.1201.0 | 2.3.108 | 3.3.3270.0 | 4.0 | 3.6.1 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.22.1**  | 2026.01.14 | 3.7.1201.0 | 2.3.108 | 3.3.3270.0 | 4.0 | 3.6.1 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.22.1**  | 2026.01.14 | 3.7.1201.0 | 2.3.108 | 3.3.3270.0 | 4.0 | 3.6.1 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.22.1**  | 2026.01.14 | 3.7.1201.0 | 2.3.108 | 3.3.3270.0 | 4.0 | 3.6.1 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.22.1**  | 2026.01.14 | 3.7.1201.0 | 2.3.108 | 3.3.3270.0 | 4.0 | 3.6.1 | 