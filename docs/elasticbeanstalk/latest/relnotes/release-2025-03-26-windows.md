

# Release: Elastic Beanstalk Windows Server platform update on March 26, 2025
<a name="release-2025-03-26-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk, Windows security updates, and updates framework and AWS components. This release also introduces a feature that adds support for Elastic Beanstalk environment variables to store secrets and parameters from AWS Secrets Manager and AWS Systems Manager Parameter Store.

**Release date:** March 26, 2025

## Changes
<a name="release-2025-03-26-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied March 2025 security updates for Windows.<br />This release includes updates from the monthly Microsoft <i>Patch Tuesday</i> Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>**New!** — Elastic Beanstalk supports configuration of environment variables to store secret and parameter data.</b></td><td>Starting with this release Elastic Beanstalk supports the option to reference AWS Secrets Manager secrets and Systems Manager Parameter Store parameters with environment variables.<br />To learn more about this feature, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.secrets.html">Using Elastic Beanstalk with Secrets Manager and Systems Manager Parameter Store</a>.</td></tr>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 8 to version 8.0.14.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2025.03.12.</td></tr>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.7.1000.0.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.300053.0b1046.</td></tr>
  <tr><td><b>EC2Launch</b></td><td>Updated EC2Launch V2 to version 2.0.2081.</td></tr>
  <tr><td><b>AWS X-Ray</b></td><td>Updated the X-Ray daemon to version 3.3.14.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2025-03-26-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2025-03-26-windows.platforms.net)

### .NET on Windows Server
<a name="release-2025-03-26-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server 2025 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server Core 2025 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server 2022 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server Core 2022 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server 2019 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server Core 2019 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server 2016 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server Core 2016 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 | 