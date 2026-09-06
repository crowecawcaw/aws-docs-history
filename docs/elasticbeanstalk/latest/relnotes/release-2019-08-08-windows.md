

# Release: AWS Elastic Beanstalk Windows Server platform update on August 8, 2019
<a name="release-2019-08-08-windows"></a>

This release applies Windows July 2019 security updates to the Windows Server platform for Elastic Beanstalk, and updates platform versions. The release also adds Amazon EC2 instance types in certain AWS Regions.

**Release date:** August 8, 2019

## Changes
<a name="release-2019-08-08-windows.changes"></a>


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied July 2019 security updates for Windows.<br />See Microsoft's <a href="https://portal.msrc.microsoft.com/en-us/">Security TechCenter</a> and <a href="https://technet.microsoft.com/en-us/library/security/">Security Advisories and Bulletins</a>.</td></tr>
  <tr><td><b>Instance types</b></td><td>Added support for more Amazon EC2 instance types in some AWS Regions, as follows: 
<table>
<thead>
  <tr><th><b>Instance types</b></th><th><b>Regions</b></th></tr>
</thead>
<tbody>
  <tr><td><b>m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,</b><br /><b>r5.16xlarge, r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, m5a.16xlarge,</b><br /><b>r5a.8xlarge, r5a.16xlarge, T3a</b></td><td> <ul><li>US East (Ohio) – us-east-2</li></ul> </td></tr>
  <tr><td><b>m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,</b><br /><b>r5.16xlarge, r5d.8xlarge, r5d.16xlarge, M5a, R5a, T3a</b></td><td> <ul><li>US West (N. California) – us-west-1</li></ul> </td></tr>
  <tr><td><b>m5.8xlarge, m5.16xlarge, m5d.8xlarge, r5.8xlarge, r5.16xlarge,</b><br /><b>r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, m5a.16xlarge, r5a.8xlarge</b></td><td> <ul><li>US West (Oregon) – us-west-2</li></ul> </td></tr>
  <tr><td><b>m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,</b><br /><b>r5.16xlarge</b></td><td> <ul><li>Asia Pacific (Hong Kong) – ap-east-1</li></ul> </td></tr>
  <tr><td><b>m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,</b><br /><b>r5.16xlarge, r5d.8xlarge, r5d.16xlarge</b></td><td> <ul><li>Asia Pacific (Mumbai) – ap-south-1</li><li>Asia Pacific (Seoul) – ap-northeast-2</li><li>Canada (Central) – ca-central-1</li><li>Europe (London) – eu-west-2</li><li>Europe (Paris) – eu-west-3</li><li>Europe (Stockholm) – eu-north-1</li></ul> </td></tr>
  <tr><td><b>M5, M5d, R5, R5d</b></td><td> <ul><li>Asia Pacific (Osaka) – ap-northeast-3</li></ul> </td></tr>
  <tr><td><b>m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,</b><br /><b>r5.16xlarge, r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, m5a.16xlarge,</b><br /><b>r5a.8xlarge, r5a.16xlarge</b></td><td> <ul><li>Asia Pacific (Singapore) – ap-southeast-1</li></ul> </td></tr>
  <tr><td><b>m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,</b><br /><b>r5.metal, r5d.8xlarge, r5d.16xlarge, r5d.metal</b></td><td> <ul><li>Asia Pacific (Tokyo) – ap-northeast-1</li></ul> </td></tr>
  <tr><td><b>r5.8xlarge, r5.16xlarge, r5d.8xlarge, M5, M5d, T3a</b></td><td> <ul><li>China (Beijing) – cn-north-1</li></ul> </td></tr>
  <tr><td><b>r5d.8xlarge, r5d.16xlarge, M5, M5d, T3a</b></td><td> <ul><li>China (Ningxia) – cn-northwest-1</li></ul> </td></tr>
  <tr><td><b>m5.8xlarge, m5.16xlarge, m5d.8xlarge, r5.8xlarge, r5.16xlarge,</b><br /><b>r5d.8xlarge, r5d.16xlarge, m5a.large, m5a.xlarge, m5a.2xlarge,</b><br /><b>m5a.4xlarge, m5a.8xlarge, m5a.12xlarge, m5a.24xlarge, r5a.large,</b><br /><b>r5a.xlarge, r5a.2xlarge, r5a.4xlarge, r5a.8xlarge, r5a.12xlarge,</b><br /><b>r5a.24xlarge</b></td><td> <ul><li>Europe (Frankfurt) – eu-central-1</li></ul> </td></tr>
  <tr><td><b>m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,</b><br /><b>r5.16xlarge, r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, r5a.8xlarge,</b><br /><b>T3a</b></td><td> <ul><li>Europe (Ireland) – eu-west-1</li></ul> </td></tr>
  <tr><td><b>m5.8xlarge, m5.16xlarge</b></td><td> <ul><li>South America (São Paulo) – sa-east-1</li></ul> </td></tr>
  <tr><td><b>m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,</b><br /><b>r5.16xlarge, r5d.8xlarge, r5d.16xlarge, T3a</b></td><td> <ul><li>AWS GovCloud (US-East) – us-gov-east-1</li><li>AWS GovCloud (US-West) – us-gov-west-1</li></ul> </td></tr>
  <tr><td><b>g3.4xlarge, g3.8xlarge, g3.16xlarge</b></td><td> <ul><li>China (Beijing) – cn-north-1</li><li>Europe (London) – eu-west-2</li></ul> </td></tr>
  <tr><td><b>g3s.xlarge</b></td><td> <ul><li>Europe (London) – eu-west-2</li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2019-08-08-windows.platforms"></a>

### .NET on Windows Server with IIS
<a name="release-2019-08-08-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 2.2.0**  |  * 64bit Windows Server 2016 v2.2.0 running IIS 10.0 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 2.2.0**  |  * 64bit Windows Server Core 2016 v2.2.0 running IIS 10.0 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 2.2.0**  |  * 64bit Windows Server 2012 R2 v2.2.0 running IIS 8.5 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.0**  |  * 64bit Windows Server Core 2012 R2 v2.2.0 running IIS 8.5 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server Core 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 with IIS 8 version 1.2.0**  |  * 64bit Windows Server 2012 v1.2.0 running IIS 8 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 | 
|  **Windows Server 2012 R2 with IIS 8.5**  |  * 64bit Windows Server 2012 R2 running IIS 8.5 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  |  * 64bit Windows Server Core 2012 R2 running IIS 8.5 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  **Windows Server 2012 with IIS 8**  |  * 64bit Windows Server 2012 running IIS 8 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  **Windows Server 2016 with IIS 10.0 version 2.2.0**  | 2019.07.12 | 3.15.780 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 3.1.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 2.2.0**  | 2019.07.12 | 3.15.780 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 3.1.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 2.2.0**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.0**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 | 
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  | 2019.07.12 | 3.15.780 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 3.1.0 | 
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  | 2019.07.12 | 3.15.780 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 3.1.0 | 
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 | 
|  **Windows Server 2012 with IIS 8 version 1.2.0**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 | 
|  **Windows Server 2012 R2 with IIS 8.5**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 | 
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 | 
|  **Windows Server 2012 with IIS 8**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 | 