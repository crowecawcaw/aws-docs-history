

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
+ [Node.js](#platforms-retiring.nodejs)
+ [PHP](#platforms-retiring.PHP)
+ [Ruby](#platforms-retiring.ruby)

## .NET Core on Linux
<a name="platforms-retiring.dotnetlinux"></a>

Elastic Beanstalk has scheduled the following .NET Core on Linux platform versions for retirement.



|  Platform Version and *Solution Stack Name*   |  Framework  |  Proxy Server  |  AMI  |  AWS X-Ray  |  End Date  | 
| --- | --- | --- | --- | --- | --- | 
|  ** .NET 9 on AL2023 version 3.11.10** <br /> * 64bit Amazon Linux 2023 v3.11.10 running .NET 9 *  | .NET 9.0.20, supports 9.0.20 | nginx 1.30.5 | 2023.12.20260930 | 3.7.0 | 2027-03-31 | 
|  ** .NET 8 on AL2023 version 3.11.10** <br /> * 64bit Amazon Linux 2023 v3.11.10 running .NET 8 *  | .NET 8.0.31, supports 8.0.31 | nginx 1.30.5 | 2023.12.20260930 | 3.7.0 | 2027-03-31 | 

For information about current platform versions, see [.NET Core on Linux](platforms-supported.md#platforms-supported.dotnetlinux).

## Node.js
<a name="platforms-retiring.nodejs"></a>

Elastic Beanstalk has scheduled the following Node.js platform versions for retirement.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  |  End Date  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Node.js 22 AL2023 version 6.11.10** <br /> * 64bit Amazon Linux 2023 v6.11.10 running Node.js 22 *  | 2023.12.20260930 | 22.23.3 (10.9.9)<br /> Default version: v22.23.3 | nginx 1.30.5 (default), Apache 2.4.68 | 2.50.1 | 3.7.0 | 2027-07-31 | 

For information about current platform versions, see [Node.js](platforms-supported.md#platforms-supported.nodejs).

## PHP
<a name="platforms-retiring.PHP"></a>

Elastic Beanstalk has scheduled the following PHP platform versions for retirement.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Proxy Server  |  End Date  | 
| --- | --- | --- | --- | --- | --- | 
|  ** PHP 8.2 AL2023 version 4.13.10** <br /> * 64bit Amazon Linux 2023 v4.13.10 running PHP 8.2 *  | 2023.12.20260930 | PHP 8.2.33 | Composer 2.10.3, PIE 1.5.1 | nginx 1.30.5 (default), Apache 2.4.68 | 2027-03-31 | 

For information about current platform versions, see [PHP](platforms-supported.md#platforms-supported.PHP).

## Ruby
<a name="platforms-retiring.ruby"></a>

Elastic Beanstalk has scheduled the following Ruby platform versions for retirement.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X-Ray  |  Proxy Server  |  End Date  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 3.3 AL2023 version 4.14.10** <br /> * 64bit Amazon Linux 2023 v4.14.10 running Ruby 3.3 *  | 2023.12.20260930 | Ruby 3.3.12-p206 | RubyGems 3.5.22 | Puma 8.0.2 | 3.7.0 | nginx 1.30.5 | 2027-07-31 | 

For information about current platform versions, see [Ruby](platforms-supported.md#platforms-supported.ruby).