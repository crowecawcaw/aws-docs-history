

# Release: Elastic Beanstalk Windows Server platform update and Windows Server 2019 support on January 15, 2020
<a name="release-2020-01-15-windows-2019"></a>

This release provides new Windows Server version 2 (v2) platform versions for AWS Elastic Beanstalk. Most notably, the release adds support for Windows Server 2019 platform versions.

**Release date:** January 15, 2020

## Changes
<a name="release-2020-01-15-windows-2019.changes"></a>

The following table lists the changes included in this release. Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


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
  <tr><td><b>Windows Server 2019</b></td><td>Added support for Windows Server 2019 as two new Windows Server v2 platform versions: one with Windows Server 2019, one with Windows Server Core 2019.<br />For details from Microsoft, see <a href="https://docs.microsoft.com/en-us/windows-server/get-started-19/get-started-19">Get started with Windows Server 2019</a>.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2020-01-15-windows-2019.platforms"></a>

### .NET on Windows Server with IIS
<a name="release-2020-01-15-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.4.0**  |  * 64bit Windows Server 2019 v2.4.0 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.4.0**  |  * 64bit Windows Server Core 2019 v2.4.0 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.4.0**  |  * 64bit Windows Server 2016 v2.4.0 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.4.0**  |  * 64bit Windows Server Core 2016 v2.4.0 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.4.0**  |  * 64bit Windows Server 2012 R2 v2.4.0 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.4.0**  |  * 64bit Windows Server Core 2012 R2 v2.4.0 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.4.0**  | 2019.12.16 | 3.15.903 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.4.0**  | 2019.12.16 | 3.15.903 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.4.0**  | 2019.12.16 | 3.15.903 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.4.0**  | 2019.12.16 | 3.15.903 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.4.0**  | 2019.12.16 | 3.15.903 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.4.0**  | 2019.12.16 | 3.15.903 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 | 