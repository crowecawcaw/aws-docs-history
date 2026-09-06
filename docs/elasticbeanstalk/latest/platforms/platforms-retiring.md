

# Elastic Beanstalk platform versions scheduled for retirement
<a name="platforms-retiring"></a>

AWS Elastic Beanstalk provides managed platforms that support running web applications developed for specific programming languages, frameworks, and web containers. Elastic Beanstalk offers one or more platform versions for each platform. For details about currently supported platform versions, see [Elastic Beanstalk supported platforms](platforms-supported.md).

This page lists platform versions that Elastic Beanstalk has scheduled for retirement, because some of their components are reaching their End of Life (EOL). These platform versions remain available until the published retirement date of their retiring components. For a list of component retirement dates, see [AWS Elastic Beanstalk platform schedules](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-schedule.html) in the *AWS Elastic Beanstalk Developer Guide*.

**Note**  
On [July 18, 2022](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-07-18-linux-al1-retire.html) Elastic Beanstalk set the status of all platform branches based on Amazon Linux AMI (AL1) to **retired**. For more information, see [AL1 platform retirement FAQ](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.migration-al.FAQ.html) in the *AWS Elastic Beanstalk Developer Guide*. 

**Note**  
On [August 6, 2026](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-08-06-al2-08-2026-retire.html) Elastic Beanstalk set the status of all platform branches based on Amazon Linux 2 (AL2) to **retired**. For more information, see [Migrating your AWS Elastic Beanstalk Linux application from Amazon Linux 2 to Amazon Linux 2023](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.migration-al.generic.from-al2.html) in the *AWS Elastic Beanstalk Developer Guide*. 

The following sections provide information about all retiring platform versions.

**Topics**
+ [.NET Core on Linux](#platforms-retiring.dotnetlinux)
+ [.NET on Windows Server](#platforms-retiring.net)
+ [Node.js](#platforms-retiring.nodejs)
+ [PHP](#platforms-retiring.PHP)
+ [Ruby](#platforms-retiring.ruby)

## .NET Core on Linux
<a name="platforms-retiring.dotnetlinux"></a>

Elastic Beanstalk has scheduled the following .NET Core on Linux platform versions for retirement.



|  Platform Version and *Solution Stack Name*   |  Framework  |  Proxy Server  |  AMI  |  AWS X-Ray  |  End Date  | 
| --- | --- | --- | --- | --- | --- | 
|  ** .NET 9 on AL2023 version 3.11.7** <br /> * 64bit Amazon Linux 2023 v3.11.7 running .NET 9 *  | .NET 9.0.19, supports 9.0.19 | nginx 1.30.4 | 2023.12.20260817 | 3.6.7 | 2027-03-31 | 
|  ** .NET 8 on AL2023 version 3.11.7** <br /> * 64bit Amazon Linux 2023 v3.11.7 running .NET 8 *  | .NET 8.0.30, supports 8.0.30 | nginx 1.30.4 | 2023.12.20260817 | 3.6.7 | 2027-03-31 | 

For information about current platform versions, see [.NET Core on Linux](platforms-supported.md#platforms-supported.dotnetlinux).

## .NET on Windows Server
<a name="platforms-retiring.net"></a>

**Note**  
  
Elastic Beanstalk platform branches based on *Windows Server 2016* and *Windows Server Core 2016* will retire on **September 30, 2026**. Additionally, all Amazon Machine Images (AMIs) for these platform branches will become inaccessible on **January 15, 2027**. This is to ensure that customer Elastic Beanstalk environments are aligned with the most current support offered by AWS.  
Starting on September 30, 2026, retired platform branches will no longer be available for new environments on Elastic Beanstalk. While you can continue to operate existing environments running on retired platform branches, these branches will no longer receive security updates, platform updates, or bug fixes from Elastic Beanstalk, creating significant security and operational risks. After January 15, 2027, the default AMIs associated with these platform branches will be inaccessible, and any activity that attempts to launch new EC2 instances based on these AMIs will fail, including auto-scaling, instance replacement, and application or configuration deployments that launch new instances.  
We strongly recommend that you start planning your migration to a current and fully supported Windows Server platform, such as *Windows Server 2025 with IIS 10.0*, *Windows Server 2022 with IIS 10.0*, or *Windows Server 2019 with IIS 10.0*. For a list of currently supported platforms see [Elastic Beanstalk supported platforms](platforms-supported.md).  
If you cannot migrate to a fully supported platform, you can use a custom AMI with Windows Server 2016 as the base image. For detailed instructions, see [Preserving access to an AMI for a retired platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.customenv-env-copy.html) in the *AWS Elastic Beanstalk Developer Guide*. If you need temporary access to an AMI while you perform a migration, contact AWS Support.

Elastic Beanstalk has scheduled the following .NET on Windows Server platform versions for retirement.

### Configuration basics
<a name="platforms-retiring.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |  End Date  | 
| --- | --- | --- | --- | --- | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server 2016 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 2026-09-30 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server Core 2016 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 2026-09-30 | 

### More details
<a name="platforms-retiring.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 

For information about current platform versions, see [.NET on Windows Server](platforms-supported.md#platforms-supported.net).

## Node.js
<a name="platforms-retiring.nodejs"></a>

Elastic Beanstalk has scheduled the following Node.js platform versions for retirement.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  |  End Date  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Node.js 22 AL2023 version 6.11.7** <br /> * 64bit Amazon Linux 2023 v6.11.7 running Node.js 22 *  | 2023.12.20260817 | 22.23.2 (10.9.8)<br /> Default version: v22.23.2 | nginx 1.30.4 (default), Apache 2.4.68 | 2.50.1 | 3.6.7 | 2027-07-31 | 

For information about current platform versions, see [Node.js](platforms-supported.md#platforms-supported.nodejs).

## PHP
<a name="platforms-retiring.PHP"></a>

Elastic Beanstalk has scheduled the following PHP platform versions for retirement.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Proxy Server  |  End Date  | 
| --- | --- | --- | --- | --- | --- | 
|  ** PHP 8.2 AL2023 version 4.13.7** <br /> * 64bit Amazon Linux 2023 v4.13.7 running PHP 8.2 *  | 2023.12.20260817 | PHP 8.2.33 | Composer 2.10.2, PIE 1.4.10 | nginx 1.30.4 (default), Apache 2.4.68 | 2027-03-31 | 

For information about current platform versions, see [PHP](platforms-supported.md#platforms-supported.PHP).

## Ruby
<a name="platforms-retiring.ruby"></a>

Elastic Beanstalk has scheduled the following Ruby platform versions for retirement.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X-Ray  |  Proxy Server  |  End Date  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 3.3 AL2023 version 4.14.7** <br /> * 64bit Amazon Linux 2023 v4.14.7 running Ruby 3.3 *  | 2023.12.20260817 | Ruby 3.3.12-p206 | RubyGems 3.5.22 | Puma 8.0.2 | 3.6.7 | nginx 1.30.4 | 2027-07-31 | 

For information about current platform versions, see [Ruby](platforms-supported.md#platforms-supported.ruby).