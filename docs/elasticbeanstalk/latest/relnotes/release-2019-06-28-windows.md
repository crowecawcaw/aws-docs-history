

# Release: AWS Elastic Beanstalk Windows Server platform update on June 28, 2019
<a name="release-2019-06-28-windows"></a>

This release applies Windows June 2019 security updates to the Windows Server platform for Elastic Beanstalk, and updates platform versions. The release also adds Amazon EC2 instance types in certain AWS Regions.

**Release date:** June 28, 2019

## Changes
<a name="release-2019-06-28-windows.changes"></a>


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied June 2019 security updates for Windows.<br />See Microsoft's <a href="https://portal.msrc.microsoft.com/en-us/">Security TechCenter</a> and <a href="https://technet.microsoft.com/en-us/library/security/">Security Advisories and Bulletins</a>.</td></tr>
  <tr><td><b>Instance types</b></td><td>Added support for more Amazon EC2 instance types in some AWS Regions, as follows: 
<table>
<thead>
  <tr><th><b>Instance types</b></th><th><b>Regions</b></th></tr>
</thead>
<tbody>
  <tr><td><b>T3a</b></td><td> <ul><li>US East (Ohio) – us-east-2</li><li>US East (N. Virginia) – us-east-1</li><li>US West (Oregon) – us-west-2</li><li>Asia Pacific (Singapore) – ap-southeast-1</li><li>Europe (Ireland) – eu-west-1</li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2019-06-28-windows.platforms"></a>

### .NET on Windows Server with IIS
<a name="release-2019-06-28-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 2.1.0**  |  * 64bit Windows Server 2016 v2.1.0 running IIS 10.0 *  | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 2.1.0**  |  * 64bit Windows Server Core 2016 v2.1.0 running IIS 10.0 *  | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 2.1.0**  |  * 64bit Windows Server 2012 R2 v2.1.0 running IIS 8.5 *  | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.1.0**  |  * 64bit Windows Server Core 2012 R2 v2.1.0 running IIS 8.5 *  | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server Core 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 with IIS 8 version 1.2.0**  |  * 64bit Windows Server 2012 v1.2.0 running IIS 8 *  | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 | 
|  **Windows Server 2012 R2 with IIS 8.5**  |  * 64bit Windows Server 2012 R2 running IIS 8.5 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  |  * 64bit Windows Server Core 2012 R2 running IIS 8.5 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 with IIS 8**  |  * 64bit Windows Server 2012 running IIS 8 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 2.1.0**  | 2019.06.12 | 3.15.756 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 3.0.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 2.1.0**  | 2019.06.12 | 3.15.756 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 3.0.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 2.1.0**  | 2019.06.12 | 3.15.756 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.0.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.1.0**  | 2019.06.12 | 3.15.756 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.0.0 | 
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  | 2019.06.12 | 3.15.756 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 1.0.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  | 2019.06.12 | 3.15.756 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  | 2019.06.12 | 3.15.756 | 4.9.3429 | 2.3.542.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  | 2019.06.12 | 3.15.756 | 4.9.3429 | 2.3.542.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 with IIS 8 version 1.2.0**  | 2019.06.12 | 3.15.756 | 4.9.3429 | 2.3.542.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 with IIS 8.5**  | 2019.06.12 | 3.15.756 | 4.9.3429 | 2.3.542.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  | 2019.06.12 | 3.15.756 | 4.9.3429 | 2.3.542.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 with IIS 8**  | 2019.06.12 | 3.15.756 | 4.9.3429 | 2.3.542.0 | 3.6 | 1.0.0 | 