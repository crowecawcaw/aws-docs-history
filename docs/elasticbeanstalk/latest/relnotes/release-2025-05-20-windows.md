

# Release: Elastic Beanstalk Windows Server platform update on May 20, 2025
<a name="release-2025-05-20-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release adds support for .NET 9 and updates framework and AWS components.

**Release date:** May 20, 2025

## Changes
<a name="release-2025-05-20-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Added support for .NET 9. This platform includes .NET 9 version 9.0.5.<br />Updated .NET 8 to version 8.0.16.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2025.05.15.</td></tr>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.7.1044.0.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.300055.1b1106.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version 3.3.2299.0.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2025-05-20-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2025-05-20-windows.platforms.net)

### .NET on Windows Server
<a name="release-2025-05-20-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.19.1**  |  * 64bit Windows Server 2025 v2.19.1 running IIS 10.0 *  | .NET 9.0.5, supports 9.0.5, 8.0.16<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.19.1**  |  * 64bit Windows Server Core 2025 v2.19.1 running IIS 10.0 *  | .NET 9.0.5, supports 9.0.5, 8.0.16<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.19.1**  |  * 64bit Windows Server 2022 v2.19.1 running IIS 10.0 *  | .NET 9.0.5, supports 9.0.5, 8.0.16<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.19.1**  |  * 64bit Windows Server Core 2022 v2.19.1 running IIS 10.0 *  | .NET 9.0.5, supports 9.0.5, 8.0.16<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.19.1**  |  * 64bit Windows Server 2019 v2.19.1 running IIS 10.0 *  | .NET 9.0.5, supports 9.0.5, 8.0.16<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.19.1**  |  * 64bit Windows Server Core 2019 v2.19.1 running IIS 10.0 *  | .NET 9.0.5, supports 9.0.5, 8.0.16<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.19.1**  |  * 64bit Windows Server 2016 v2.19.1 running IIS 10.0 *  | .NET 9.0.5, supports 9.0.5, 8.0.16<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.19.1**  |  * 64bit Windows Server Core 2016 v2.19.1 running IIS 10.0 *  | .NET 9.0.5, supports 9.0.5, 8.0.16<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.19.1**  | 2025.05.15 | 3.7.1044.0 |  | 3.3.2299.0 | 3.6 | 3.3.14 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.19.1**  | 2025.05.15 | 3.7.1044.0 |  | 3.3.2299.0 | 3.6 | 3.3.14 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.19.1**  | 2025.05.15 | 3.7.1044.0 |  | 3.3.2299.0 | 3.6 | 3.3.14 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.19.1**  | 2025.05.15 | 3.7.1044.0 |  | 3.3.2299.0 | 3.6 | 3.3.14 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.19.1**  | 2025.05.15 | 3.7.1044.0 |  | 3.3.2299.0 | 3.6 | 3.3.14 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.19.1**  | 2025.05.15 | 3.7.1044.0 |  | 3.3.2299.0 | 3.6 | 3.3.14 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.19.1**  | 2025.05.15 | 3.7.1044.0 |  | 3.3.2299.0 | 3.6 | 3.3.14 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.19.1**  | 2025.05.15 | 3.7.1044.0 |  | 3.3.2299.0 | 3.6 | 3.3.14 | 