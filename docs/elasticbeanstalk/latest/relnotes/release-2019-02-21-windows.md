

# Release: AWS Elastic Beanstalk Windows Server platform update on February 21, 2019
<a name="release-2019-02-21-windows"></a>

This release applies Windows February 2019 security updates to the Windows Server v1 and earlier platform versions for Elastic Beanstalk. The release also adds Amazon EC2 instance types in certain AWS Regions.

**Release date:** February 21, 2019

## Changes
<a name="release-2019-02-21-windows.changes"></a>

This release updates Windows Server v1 and earlier platform versions. To learn more about Windows Server v2 platform versions, see [Release: AWS Elastic Beanstalk Windows Server platform update to new major version 2 on February 21, 2019](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-02-21-windows-v2.html).


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied February 2019 security updates for Windows.<br />See Microsoft's <a href="https://portal.msrc.microsoft.com/en-us/">Security TechCenter</a> and <a href="https://technet.microsoft.com/en-us/library/security/">Security Advisories and Bulletins</a>.</td></tr>
  <tr><td><b>Instance types</b></td><td>Added support for more Amazon EC2 instance types in some AWS Regions, as follows:
<table>
<thead>
  <tr><th><b>Instance type</b></th><th><b>Region</b></th></tr>
</thead>
<tbody>
  <tr><td><b>C5d, M5d, R5, R5d, T3</b></td><td> <ul><li>Asia Pacific (Mumbai) – ap-south-1</li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2019-02-21-windows.platforms"></a>

### .NET on Windows Server with IIS
<a name="release-2019-02-22-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server Core 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 with IIS 8 version 1.2.0**  |  * 64bit Windows Server 2012 v1.2.0 running IIS 8 *  | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 | 
|  **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**  |  * 64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5 *  | .NET Core 2.1.8, supports 2.1.8, 2.0.9, 1.1.11, 1.0.14<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 | 
|  **Windows Server 2012 R2 with IIS 8.5**  |  * 64bit Windows Server 2012 R2 running IIS 8.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  |  * 64bit Windows Server Core 2012 R2 running IIS 8.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 with IIS 8**  |  * 64bit Windows Server 2012 running IIS 8 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 | 
|  **Windows Server 2008 R2 with IIS 7.5**  |  * 64bit Windows Server 2008 R2 running IIS 7.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  | 2019.02.13 | 3.15.666 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  | 2019.02.13 | 3.15.666 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 with IIS 8 version 1.2.0**  | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**  | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 with IIS 8.5**  | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 with IIS 8**  | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2008 R2 with IIS 7.5**  | 2019.02.13 | 3.15.666 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 