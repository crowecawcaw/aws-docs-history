

# Release: Elastic Beanstalk Windows Server platform update on December 23, 2019
<a name="release-2019-12-23-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates and updates AWS components. It also updates .NET Core versions.

**Release date:** December 23, 2019

## Changes
<a name="release-2019-12-23-windows.changes"></a>

The following table lists the changes included in this release. Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied December 2019 security updates for Windows.<br />See Microsoft's <a href="https://portal.msrc.microsoft.com/en-us/">Security TechCenter</a> and <a href="https://technet.microsoft.com/en-us/library/security/">Security Advisories and Bulletins</a>.</td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AWS SDK for .NET</b></td><td>Updated the SDK to version 3.15.903.</td></tr>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2019.12.16.</td></tr>
  <tr><td><b>CloudWatch agent</b></td><td>Updated the CloudWatch agent to version 1.232905.0.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>Instance types</b></td><td>Starting with today's Windows Server platform update, <i>we will no longer announce added Amazon EC2 instance types</i>. Any new platform version will support all instance types available at the time of the platform version's release.<br />For a list of available instance types per AWS Region, see <a href="https://aws.amazon.com/ec2/pricing/on-demand/">Amazon EC2 Pricing</a> and <a href="https://aws.amazon.com/ec2/spot/pricing/">Amazon EC2 Spot Instances Pricing</a>.</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2019-12-23-windows.platforms"></a>

### .NET on Windows Server with IIS
<a name="release-2019-12-23-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2016 with IIS 10.0 version 2.3.2**  |  * 64bit Windows Server 2016 v2.3.2 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.3.2**  |  * 64bit Windows Server Core 2016 v2.3.2 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.3.2**  |  * 64bit Windows Server 2012 R2 v2.3.2 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.2**  |  * 64bit Windows Server Core 2012 R2 v2.3.2 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server 2016 v1.2.0 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server Core 2016 v1.2.0 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 with IIS 8 version 1.2.0**  |  * 64bit Windows Server 2012 v1.2.0 running IIS 8 *  | .NET Core 2.2.8, supports 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 | 
|  ** Windows Server 2012 R2 with IIS 8.5 **  |  * 64bit Windows Server 2012 R2 running IIS 8.5 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 **  |  * 64bit Windows Server Core 2012 R2 running IIS 8.5 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 with IIS 8 **  |  * 64bit Windows Server 2012 running IIS 8 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2016 with IIS 10.0 version 2.3.2**  | 2019.12.16 | 3.15.903 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.3.2**  | 2019.12.16 | 3.15.903 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.3.2**  | 2019.12.16 | 3.15.903 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.2**  | 2019.12.16 | 3.15.903 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 1.2.0**  | 2019.12.16 | 3.15.903 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 1.2.0**  | 2019.12.16 | 3.15.903 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  | 2019.12.16 | 3.15.903 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  | 2019.12.16 | 3.15.903 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2012 with IIS 8 version 1.2.0**  | 2019.12.16 | 3.15.903 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 **  | 2019.12.16 | 3.15.903 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 **  | 2019.12.16 | 3.15.903 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 | 
|  ** Windows Server 2012 with IIS 8 **  | 2019.12.16 | 3.15.903 | 4.9.3865 | 2.3.722.0 | 3.6 | 3.1.0 | 