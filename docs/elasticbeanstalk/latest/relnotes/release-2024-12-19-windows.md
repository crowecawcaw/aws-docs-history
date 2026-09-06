

# Release: Elastic Beanstalk Windows Server platform update on December 19, 2024
<a name="release-2024-12-19-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates AWS components.

**Release date:** December 19, 2024

## Changes
<a name="release-2024-12-19-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied December 2024 security updates for Windows.<br />This release includes updates from the monthly Microsoft <i>Patch Tuesday</i> Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>No changes to .NET 8 or .NET 6 for this release.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2024.12.13.</td></tr>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.7.945.0.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.300049.1b929.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version 3.3.1345.0.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2024-12-19-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2024-12-19-windows.platforms.net)

### .NET on Windows Server
<a name="release-2024-12-19-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2022 with IIS 10.0 version 2.16.1**  |  * 64bit Windows Server 2022 v2.16.1 running IIS 10.0 *  | .NET 8.0.11, supports 8.0.11, 6.0.36<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.16.1**  |  * 64bit Windows Server Core 2022 v2.16.1 running IIS 10.0 *  | .NET 8.0.11, supports 8.0.11, 6.0.36<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.16.1**  |  * 64bit Windows Server 2019 v2.16.1 running IIS 10.0 *  | .NET 8.0.11, supports 8.0.11, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.16.1**  |  * 64bit Windows Server Core 2019 v2.16.1 running IIS 10.0 *  | .NET 8.0.11, supports 8.0.11, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.16.1**  |  * 64bit Windows Server 2016 v2.16.1 running IIS 10.0 *  | .NET 8.0.11, supports 8.0.11, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.16.1**  |  * 64bit Windows Server Core 2016 v2.16.1 running IIS 10.0 *  | .NET 8.0.11, supports 8.0.11, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2022 with IIS 10.0 version 2.16.1**  | 2024.12.13 | 3.7.945.0 |  | 3.3.1345.0 | 3.6 | 3.3.13 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.16.1**  | 2024.12.13 | 3.7.945.0 |  | 3.3.1345.0 | 3.6 | 3.3.13 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.16.1**  | 2024.12.13 | 3.7.945.0 |  | 3.3.1345.0 | 3.6 | 3.3.13 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.16.1**  | 2024.12.13 | 3.7.945.0 |  | 3.3.1345.0 | 3.6 | 3.3.13 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.16.1**  | 2024.12.13 | 3.7.945.0 |  | 3.3.1345.0 | 3.6 | 3.3.13 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.16.1**  | 2024.12.13 | 3.7.945.0 |  | 3.3.1345.0 | 3.6 | 3.3.13 | 