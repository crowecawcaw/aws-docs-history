

# Release: AWS Elastic Beanstalk Windows Server platform update on September 24, 2018
<a name="release-2018-09-24-windows"></a>

This release applies Windows September 2018 security updates to the Windows Server platform for Elastic Beanstalk, and updates platform configurations. The release also adds Amazon EC2 instance types in certain AWS Regions.

**Release date:** September 24, 2018

## Changes
<a name="release-2018-09-24-windows.changes"></a>


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied September 2018 security updates for Windows.<br />See Microsoft's <a href="https://portal.msrc.microsoft.com/en-us/">Security TechCenter</a> and <a href="https://technet.microsoft.com/en-us/library/security/">Security Advisories and Bulletins</a>.</td></tr>
  <tr><td><b>Instance types</b></td><td>Added support for more Amazon EC2 instance types in some AWS Regions, as follows:
<table>
<thead>
  <tr><th><b>Instance type</b></th><th><b>Regions</b></th></tr>
</thead>
<tbody>
  <tr><td><b>p3</b></td><td> <ul><li>Asia Pacific (Singapore)—ap-southeast-1</li><li>Asia Pacific (Sydney)—ap-southeast-2</li><li>Canada (Central)—ca-central-1</li><li>China (Ningxia)—cn-northwest-1</li><li>EU (Frankfurt)—eu-central-1</li><li>EU (London)—eu-west-2</li></ul> </td></tr>
  <tr><td><b>c5d</b></td><td> <ul><li>US West (N. California)—us-west-1</li><li>Asia Pacific (Seoul)—ap-northeast-2</li><li>Asia Pacific (Singapore)—ap-southeast-1</li><li>Asia Pacific (Sydney)—ap-southeast-2</li><li>Asia Pacific (Tokyo)—ap-northeast-1</li><li>EU (Frankfurt)—eu-central-1</li><li>EU (London)—eu-west-2</li></ul> </td></tr>
  <tr><td><b>m5d</b></td><td> <ul><li>US West (N. California)—us-west-1</li><li>Asia Pacific (Seoul)—ap-northeast-2</li><li>Asia Pacific (Singapore)—ap-southeast-1</li><li>Asia Pacific (Sydney)—ap-southeast-2</li><li>Asia Pacific (Tokyo)—ap-northeast-1</li><li>EU (Frankfurt)—eu-central-1</li><li>EU (London)—eu-west-2</li></ul> </td></tr>
  <tr><td><b>t3</b></td><td> <ul><li>US East (N. Virginia)—us-east-1</li><li>US East (Ohio)—us-east-2</li><li>US West (N. California)—us-west-1</li><li>US West (Oregon)—us-west-2</li><li>Asia Pacific (Singapore)—ap-southeast-1</li><li>Asia Pacific (Sydney)—ap-southeast-2</li><li>Asia Pacific (Tokyo)—ap-northeast-1</li><li>Canada (Central)—ca-central-1</li><li>EU (Frankfurt)—eu-central-1</li><li>EU (Ireland)—eu-west-1</li><li>EU (London)—eu-west-2</li><li>South America (São Paulo)—sa-east-1</li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## Updated platform configurations
<a name="release-2018-09-24-windows.platforms"></a>

### .NET on Windows Server with IIS
<a name="release-2018-09-24-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Configuration  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server Core 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 with IIS 8 version 1.2.0**  |  * 64bit Windows Server 2012 v1.2.0 running IIS 8 *  | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 | 
|  **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**  |  * 64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5 *  | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 | 
|  **Windows Server 2012 R2 with IIS 8.5**  |  * 64bit Windows Server 2012 R2 running IIS 8.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  |  * 64bit Windows Server Core 2012 R2 running IIS 8.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 with IIS 8**  |  * 64bit Windows Server 2012 running IIS 8 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 | 
|  **Windows Server 2008 R2 with IIS 7.5**  |  * 64bit Windows Server 2008 R2 running IIS 7.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Configuration  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  | 2018.09.15 | 3.3.352.0 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.2.800.0 | 3.6 | 1.0.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  | 2018.09.15 | 3.3.352.0 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.2.800.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  | 2018.09.15 | 3.3.352.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  | 2018.09.15 | 3.3.352.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 with IIS 8 version 1.2.0**  | 2018.09.15 | 3.3.352.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**  | 2018.09.15 | 3.3.352.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 with IIS 8.5**  | 2018.09.15 | 3.3.352.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  | 2018.09.15 | 3.3.352.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 with IIS 8**  | 2018.09.15 | 3.3.352.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2008 R2 with IIS 7.5**  | 2018.09.15 | 3.3.352.0 | 4.9.2756 | 2.2.800.0 | 3.6 | 1.0.0 | 