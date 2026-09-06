

# Release: AWS Elastic Beanstalk Windows Server platform update on May 2, 2019
<a name="release-2019-05-02-windows"></a>

This release applies Windows April 2019 security updates to the Windows Server platform for Elastic Beanstalk, and updates platform configurations. The release also adds Amazon EC2 instance types in certain AWS Regions.

**Release date:** May 2, 2019

## Changes
<a name="release-2019-05-02-windows.changes"></a>


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied April 2019 security updates for Windows.<br />See Microsoft's <a href="https://portal.msrc.microsoft.com/en-us/">Security TechCenter</a> and <a href="https://technet.microsoft.com/en-us/library/security/">Security Advisories and Bulletins</a>.</td></tr>
  <tr><td><b>Instance types</b></td><td>Added support for more Amazon EC2 instance types in some AWS Regions. In particular, we added support for the new M5ad and R5ad instances. They add high-speed, low latency local (physically connected) block storage to the existing M5a and R5a instances. For more information, see <a href="https://aws.amazon.com/blogs/aws/new-amd-epyc-powered-amazon-ec2-m5ad-and-r5ad-instances/">New AMD EPYC-Powered Amazon EC2 M5ad and R5ad Instances</a>.<br />The added instance types are listed in the following table.
<table>
<thead>
  <tr><th><b>Instance types</b></th><th><b>Regions</b></th></tr>
</thead>
<tbody>
  <tr><td><b>m5ad</b></td><td> <ul><li>US East (Ohio) – us-east-2</li><li>US West (Oregon) – us-west-2</li><li>Asia Pacific (Singapore) – ap-southeast-1</li></ul> </td></tr>
  <tr><td><b>r5ad</b></td><td> <ul><li>US East (Ohio) – us-east-2</li><li>US East (N. Virginia) – us-east-1</li><li>US West (Oregon) – us-west-2</li><li>Asia Pacific (Singapore) – ap-southeast-1</li></ul> </td></tr>
  <tr><td><b>z1d</b></td><td> <ul><li>Asia Pacific (Sydney) – ap-southeast-2</li><li>Europe (Frankfurt) – eu-central-1</li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2019-05-02-windows.platforms"></a>

### .NET on Windows Server with IIS
<a name="release-2019-05-02-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 2.0.3**  |  * 64bit Windows Server 2016 v2.0.3 running IIS 10.0 *  | .NET Core 2.2.4, supports 2.2.4, 2.1.10<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 2.0.3**  |  * 64bit Windows Server Core 2016 v2.0.3 running IIS 10.0 *  | .NET Core 2.2.4, supports 2.2.4, 2.1.10<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 2.0.3**  |  * 64bit Windows Server 2012 R2 v2.0.3 running IIS 8.5 *  | .NET Core 2.2.4, supports 2.2.4, 2.1.10<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.3**  |  * 64bit Windows Server Core 2012 R2 v2.0.3 running IIS 8.5 *  | .NET Core 2.2.4, supports 2.2.4, 2.1.10<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.2.4, supports 2.2.4, 2.1.10, 2.0.9, 1.1.12, 1.0.15<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server Core 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.2.4, supports 2.2.4, 2.1.10, 2.0.9, 1.1.12, 1.0.15<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.2.4, supports 2.2.4, 2.1.10, 2.0.9, 1.1.12, 1.0.15<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.2.4, supports 2.2.4, 2.1.10, 2.0.9, 1.1.12, 1.0.15<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 with IIS 8 version 1.2.0**  |  * 64bit Windows Server 2012 v1.2.0 running IIS 8 *  | .NET Core 2.2.4, supports 2.2.4, 2.1.10, 2.0.9, 1.1.12, 1.0.15<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 | 
|  **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**  |  * 64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5 *  | .NET Core 2.1.10, supports 2.1.10, 2.0.9, 1.1.12, 1.0.15<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 | 
|  **Windows Server 2012 R2 with IIS 8.5**  |  * 64bit Windows Server 2012 R2 running IIS 8.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  |  * 64bit Windows Server Core 2012 R2 running IIS 8.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 with IIS 8**  |  * 64bit Windows Server 2012 running IIS 8 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 | 
|  **Windows Server 2008 R2 with IIS 7.5**  |  * 64bit Windows Server 2008 R2 running IIS 7.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 2.0.3**  | 2019.04.21 | 3.15.715 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.444.0 | 3.6 | 3.0.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 2.0.3**  | 2019.04.21 | 3.15.715 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.444.0 | 3.6 | 3.0.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 2.0.3**  | 2019.04.21 | 3.15.715 | 4.9.3289 | 2.3.444.0 | 3.6 | 3.0.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.3**  | 2019.04.21 | 3.15.715 | 4.9.3289 | 2.3.444.0 | 3.6 | 3.0.0 | 
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  | 2019.04.21 | 3.15.715 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  | 2019.04.21 | 3.15.715 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  | 2019.04.21 | 3.15.715 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  | 2019.04.21 | 3.15.715 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 with IIS 8 version 1.2.0**  | 2019.04.21 | 3.15.715 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**  | 2019.04.21 | 3.15.715 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 with IIS 8.5**  | 2019.04.21 | 3.15.715 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  | 2019.04.21 | 3.15.715 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2012 with IIS 8**  | 2019.04.21 | 3.15.715 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 
|  **Windows Server 2008 R2 with IIS 7.5**  | 2019.04.21 | 3.15.715 | 4.9.3289 | 2.3.444.0 | 3.6 | 1.0.0 | 