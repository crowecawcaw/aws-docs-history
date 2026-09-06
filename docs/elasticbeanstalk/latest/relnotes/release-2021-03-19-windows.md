

# Release: Elastic Beanstalk Windows Server platform update on March 19, 2021
<a name="release-2021-03-19-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** March 19, 2021

## Changes
<a name="release-2021-03-19-windows.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied March 2021 security updates for Windows.<br />See the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET Core 2.1 to version 2.1.26.<br />Updated .NET Core 3 to version 3.1.13 on Windows Server 2019 and 2016 platform versions.<br />Updated .NET 5 to version 5.0.4 on Windows Server 2019 and 2016 platform versions.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.15.1248.</td></tr>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2021.03.10.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version 3.0.431.0 on Windows Server 2012 platform versions.<br />Updated the SSM Agent to version 3.0.529.0 on Windows Server 2019 and 2016 platform versions.</td></tr>
  <tr><td><b>EC2Config</b></td><td>Updated EC2Config to version 4.9.4326 on Windows Server 2012 platform versions.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.247347.5.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2021-03-19-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2021-03-19-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.6.4**  |  * 64bit Windows Server 2019 v2.6.4 running IIS 10.0 *  | .NET 5.0.4, supports 5.0.4, 3.1.13, 2.2.8, 2.1.26<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.6.4**  |  * 64bit Windows Server Core 2019 v2.6.4 running IIS 10.0 *  | .NET 5.0.4, supports 5.0.4, 3.1.13, 2.2.8, 2.1.26<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.6.4**  |  * 64bit Windows Server 2016 v2.6.4 running IIS 10.0 *  | .NET 5.0.4, supports 5.0.4, 3.1.13, 2.2.8, 2.1.26<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.6.4**  |  * 64bit Windows Server Core 2016 v2.6.4 running IIS 10.0 *  | .NET 5.0.4, supports 5.0.4, 3.1.13, 2.2.8, 2.1.26<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.6.4**  |  * 64bit Windows Server 2012 R2 v2.6.4 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.26<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.4**  |  * 64bit Windows Server Core 2012 R2 v2.6.4 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.26<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.6.4**  | 2021.03.10 | 3.15.1248 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.6.4**  | 2021.03.10 | 3.15.1248 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.6.4**  | 2021.03.10 | 3.15.1248 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.6.4**  | 2021.03.10 | 3.15.1248 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.6.4**  | 2021.03.10 | 3.15.1248 | 4.9.4326 | 3.0.431.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.4**  | 2021.03.10 | 3.15.1248 | 4.9.4326 | 3.0.431.0 | 3.6 | 3.2.0 | 