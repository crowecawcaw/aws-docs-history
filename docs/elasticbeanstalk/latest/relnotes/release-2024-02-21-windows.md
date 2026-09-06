

# Release: Elastic Beanstalk Windows Server platform update on February 21, 2024
<a name="release-2024-02-21-windows"></a>

This release provides support for Windows 2022 with two new platform branches: Windows Server 2022 and Windows Server Core 2022. This release also provides new Windows Server platform versions for AWS Elastic Beanstalk, along with Windows security updates. It also updates framework and AWS components.

**Release date:** February 21, 2024

## Changes
<a name="release-2024-02-21-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Operating system updates</b></td><td> 
<table>
<thead>
  <tr><th><b>OS</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows Server 2022</b></td><td><b>**New!** </b>— Added support for Windows Server 2022 as two new Windows Server platform branches:<ul><li> Windows Server 2022 with IIS 10.0 </li><li> Windows Server Core 2022 with IIS 10.0 </li></ul><br />For more information, see <a href="https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-in-windows-server-2022"> What's new in Windows Server 2022</a> on the Microsoft website.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>Windows security updates</b></td><td>Applied February 2024 security updates for Windows.<br />This release includes updates from the monthly Microsoft <i>Patch Tuesday</i> Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 6 to version 6.0.27.<br />Updated .NET 8 to version 8.0.2.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2024.02.14.</td></tr>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.7.747.0.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.300033.0b462.</td></tr>
  <tr><td><b>EC2Launch</b></td><td>Updated EC2Launch V2 to version 2.0.1739.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version 3.2.2222.0.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2024-02-21-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2024-02-21-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2022 with IIS 10.0 version 2.14.0**  |  * 64bit Windows Server 2022 v2.14.0 running IIS 10.0 *  | .NET 8.0.2, supports 8.0.2, 6.0.27<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.14.0**  |  * 64bit Windows Server Core 2022 v2.14.0 running IIS 10.0 *  | .NET 8.0.2, supports 8.0.2, 6.0.27<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.14.0**  |  * 64bit Windows Server 2019 v2.14.0 running IIS 10.0 *  | .NET 8.0.2, supports 8.0.2, 6.0.27<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.14.0**  |  * 64bit Windows Server Core 2019 v2.14.0 running IIS 10.0 *  | .NET 8.0.2, supports 8.0.2, 6.0.27<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.14.0**  |  * 64bit Windows Server 2016 v2.14.0 running IIS 10.0 *  | .NET 8.0.2, supports 8.0.2, 6.0.27<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.14.0**  |  * 64bit Windows Server Core 2016 v2.14.0 running IIS 10.0 *  | .NET 8.0.2, supports 8.0.2, 6.0.27<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2022 with IIS 10.0 version 2.14.0**  | 2024.02.14 | 3.7.747.0 |  | 3.2.2222.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.14.0**  | 2024.02.14 | 3.7.747.0 |  | 3.2.2222.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.14.0**  | 2024.02.14 | 3.7.747.0 |  | 3.2.2222.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.14.0**  | 2024.02.14 | 3.7.747.0 |  | 3.2.2222.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.14.0**  | 2024.02.14 | 3.7.747.0 |  | 3.2.2222.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.14.0**  | 2024.02.14 | 3.7.747.0 |  | 3.2.2222.0 | 3.6 | 3.2.0 | 