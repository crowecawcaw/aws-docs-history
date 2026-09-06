

# Release: Elastic Beanstalk Windows Server platform update on March 21, 2024
<a name="release-2024-03-21-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates AWS components.

**Release date:** March 21, 2024

## Changes
<a name="release-2024-03-21-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied March 2024 security updates for Windows.<br />This release includes updates from the monthly Microsoft <i>Patch Tuesday</i> Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 6 to version 6.0.28.<br />Updated .NET 8 to version 8.0.3.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2024.03.13.</td></tr>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.7.766.0.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.300034.0b498.</td></tr>
  <tr><td><b>EC2Launch</b></td><td>Updated EC2Launch V2 to version 2.0.1815.0.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>Additional changes with this release</b></td><td><b>Windows Secure Time Seeding feature disabled</b><ul><li> The Windows Secure Time Seeding feature has been disabled for the Windows 2016, 2019, and 2022 platform branches. The feature allows Windows to reset the system clock with data gathered from SSL connections. It has been disabled because it can cause problematic time skews with Amazon Network Time Protocol (NTP) synchronization. </li><li> Elastic Beanstalk AMIs will continue to synchronize time based on Amazon NTP. </li><li> This change will not impact time accuracy. It will only disable the ability for Windows to override the system time based on SSL information. </li></ul></td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2024-03-21-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2024-03-20-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2022 with IIS 10.0 version 2.14.1**  |  * 64bit Windows Server 2022 v2.14.1 running IIS 10.0 *  | .NET 8.0.3, supports 8.0.3, 6.0.28<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.14.1**  |  * 64bit Windows Server Core 2022 v2.14.1 running IIS 10.0 *  | .NET 8.0.3, supports 8.0.3, 6.0.28<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.14.1**  |  * 64bit Windows Server 2019 v2.14.1 running IIS 10.0 *  | .NET 8.0.3, supports 8.0.3, 6.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.14.1**  |  * 64bit Windows Server Core 2019 v2.14.1 running IIS 10.0 *  | .NET 8.0.3, supports 8.0.3, 6.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.14.1**  |  * 64bit Windows Server 2016 v2.14.1 running IIS 10.0 *  | .NET 8.0.3, supports 8.0.3, 6.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.14.1**  |  * 64bit Windows Server Core 2016 v2.14.1 running IIS 10.0 *  | .NET 8.0.3, supports 8.0.3, 6.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2022 with IIS 10.0 version 2.14.1**  | 2024.03.13 | 3.7.766.0 |  | 3.2.2303.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.14.1**  | 2024.03.13 | 3.7.766.0 |  | 3.2.2303.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.14.1**  | 2024.03.13 | 3.7.766.0 |  | 3.2.2303.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.14.1**  | 2024.03.13 | 3.7.766.0 |  | 3.2.2303.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.14.1**  | 2024.03.13 | 3.7.766.0 |  | 3.2.2303.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.14.1**  | 2024.03.13 | 3.7.766.0 |  | 3.2.2303.0 | 3.6 | 3.2.0 | 