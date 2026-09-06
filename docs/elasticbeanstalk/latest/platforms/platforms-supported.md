

# Elastic Beanstalk supported platforms
<a name="platforms-supported"></a>

AWS Elastic Beanstalk provides managed platforms that support running web applications developed for specific programming languages, frameworks, and web containers. Elastic Beanstalk offers one or more platform versions for each platform. When you create an environment and choose a platform, Elastic Beanstalk provisions the resources that your application needs, including one or more Amazon Elastic Compute Cloud (Amazon EC2) instances. The software stack running on the Amazon EC2 instances depends on the platform version you chose.

For more information about platforms, see [AWS Elastic Beanstalk Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-all-platforms.html) in the *AWS Elastic Beanstalk Developer Guide*. Detailed release notes are available for recent releases at [AWS Elastic Beanstalk Release Notes](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/). 

The following sections provide information about all current platform versions. For lists of historical platform versions and the date ranges they were current, see [Platform history](platform-history.md).

Elastic Beanstalk has scheduled some platform versions for retirement, because some of their components are reaching their End of Life (EOL). These platform versions remain available until the published retirement date of their retiring components. For a list of component retirement dates, see [AWS Elastic Beanstalk platform schedules](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-schedule.html) in the *AWS Elastic Beanstalk Developer Guide*. For a list of platform versions scheduled for retirement, see [Elastic Beanstalk platform versions scheduled for retirement](platforms-retiring.md).

**Topics**
+ [Docker](#platforms-supported.docker)
+ [Go](#platforms-supported.go)
+ [Java SE](#platforms-supported.javase)
+ [Tomcat](#platforms-supported.java)
+ [.NET Core on Linux](#platforms-supported.dotnetlinux)
+ [.NET on Windows Server](#platforms-supported.net)
+ [Node.js](#platforms-supported.nodejs)
+ [PHP](#platforms-supported.PHP)
+ [Python](#platforms-supported.python)
+ [Ruby](#platforms-supported.ruby)
+ [Elastic Beanstalk platform versions scheduled for retirement](platforms-retiring.md)
+ [Elastic Beanstalk platform versions in public beta](platforms-beta.md)

## Docker
<a name="platforms-supported.docker"></a>

Docker is a container platform that allows you to define your own software stack and store it in an image that can be downloaded from a remote repository. The Docker platform includes an nginx proxy server.

See [Deploying Elastic Beanstalk Applications from Docker Containers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker.html) in the *AWS Elastic Beanstalk Developer Guide* for more information about the Docker platform.



|  Platform Version and *Solution Stack Name*   |  AMI  |  ECS Agent  |  Docker  |  Docker Compose  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Docker AL2023 version 4.13.7** <br /> * 64bit Amazon Linux 2023 v4.13.7 running Docker *  | 2023.12.20260817 |  | 25.0.16 | 5.5.0 | nginx 1.30.4 | 
|  ** ECS AL2023 version 4.7.7** <br /> * 64bit Amazon Linux 2023 v4.7.7 running ECS *  | 2023.12.20260817 | 1.106.0 | 25.0.16 |  |  | 

 For information about previous platform versions, see [Docker platform history](platform-history-docker.md).

## Go
<a name="platforms-supported.go"></a>

Elastic Beanstalk supports the following Go platform versions.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Go 1 AL2023 version 4.9.7** <br /> * 64bit Amazon Linux 2023 v4.9.7 running Go 1 *  | 2023.12.20260817 | Go 1.25.12 | 3.6.7 | nginx 1.30.4 | 

 For information about previous platform versions, see [Go platform history](platform-history-go.md).

## Java SE
<a name="platforms-supported.javase"></a>

Elastic Beanstalk supports the following Java SE platform versions.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 25 AL2023 version 4.12.7** <br /> * 64bit Amazon Linux 2023 v4.12.7 running Corretto 25 *  | 2023.12.20260817 | Corretto 25.0.4.7.1 | Ant 1.10.17, Gradle 9.7.1, Maven 3.9.16 | 3.6.7 | nginx 1.30.4 | 
|  ** Corretto 21 AL2023 version 4.12.7** <br /> * 64bit Amazon Linux 2023 v4.12.7 running Corretto 21 *  | 2023.12.20260817 | Corretto 21.0.12.8.1 | Ant 1.10.17, Gradle 9.7.1, Maven 3.9.16 | 3.6.7 | nginx 1.30.4 | 
|  ** Corretto 17 AL2023 version 4.12.7** <br /> * 64bit Amazon Linux 2023 v4.12.7 running Corretto 17 *  | 2023.12.20260817 | Corretto 17.0.20.8.1 | Ant 1.10.17, Gradle 9.7.1, Maven 3.9.16 | 3.6.7 | nginx 1.30.4 | 
|  ** Corretto 11 AL2023 version 4.12.7** <br /> * 64bit Amazon Linux 2023 v4.12.7 running Corretto 11 *  | 2023.12.20260817 | Corretto 11.0.32.9.1 | Ant 1.10.17, Gradle 8.14.5, Maven 3.9.16 | 3.6.7 | nginx 1.30.4 | 
|  ** Corretto 8 AL2023 version 4.12.7** <br /> * 64bit Amazon Linux 2023 v4.12.7 running Corretto 8 *  | 2023.12.20260817 | Corretto 8.502.07.1 | Ant 1.10.17, Gradle 8.14.5, Maven 3.9.16 | 3.6.7 | nginx 1.30.4 | 

 For information about previous platform versions, see [Java SE platform history](platform-history-javase.md).

## Tomcat
<a name="platforms-supported.java"></a>

Elastic Beanstalk supports the following Tomcat platform versions.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 25 with Tomcat 11 AL2023 version 5.14.7** <br /> * 64bit Amazon Linux 2023 v5.14.7 running Tomcat 11 Corretto 25 *  | 2023.12.20260817 | Corretto 25.0.4.7.1 | 3.6.7 | Tomcat 11.0.25 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** Corretto 21 with Tomcat 11 AL2023 version 5.14.7** <br /> * 64bit Amazon Linux 2023 v5.14.7 running Tomcat 11 Corretto 21 *  | 2023.12.20260817 | Corretto 21.0.12.8.1 | 3.6.7 | Tomcat 11.0.25 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** Corretto 17 with Tomcat 11 AL2023 version 5.14.7** <br /> * 64bit Amazon Linux 2023 v5.14.7 running Tomcat 11 Corretto 17 *  | 2023.12.20260817 | Corretto 17.0.20.8.1 | 3.6.7 | Tomcat 11.0.25 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** Corretto 21 with Tomcat 10 AL2023 version 5.14.7** <br /> * 64bit Amazon Linux 2023 v5.14.7 running Tomcat 10 Corretto 21 *  | 2023.12.20260817 | Corretto 21.0.12.8.1 | 3.6.7 | Tomcat 10.1.59 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** Corretto 17 with Tomcat 10 AL2023 version 5.14.7** <br /> * 64bit Amazon Linux 2023 v5.14.7 running Tomcat 10 Corretto 17 *  | 2023.12.20260817 | Corretto 17.0.20.8.1 | 3.6.7 | Tomcat 10.1.59 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** Corretto 17 with Tomcat 9 AL2023 version 5.14.7** <br /> * 64bit Amazon Linux 2023 v5.14.7 running Tomcat 9 Corretto 17 *  | 2023.12.20260817 | Corretto 17.0.20.8.1 | 3.6.7 | Tomcat 9.0.120 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** Corretto 11 with Tomcat 9 AL2023 version 5.14.7** <br /> * 64bit Amazon Linux 2023 v5.14.7 running Tomcat 9 Corretto 11 *  | 2023.12.20260817 | Corretto 11.0.32.9.1 | 3.6.7 | Tomcat 9.0.120 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** Corretto 8 with Tomcat 9 AL2023 version 5.14.7** <br /> * 64bit Amazon Linux 2023 v5.14.7 running Tomcat 9 Corretto 8 *  | 2023.12.20260817 | Corretto 8.502.07.1 | 3.6.7 | Tomcat 9.0.121 | nginx 1.30.4 (default), Apache 2.4.68 | 

 For information about previous platform versions, see [Tomcat platform history](platform-history-java.md).

## .NET Core on Linux
<a name="platforms-supported.dotnetlinux"></a>

Elastic Beanstalk supports the following .NET Core on Linux platform versions.



|  Platform Version and *Solution Stack Name*   |  Framework  |  Proxy Server  |  AMI  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | 
|  ** .NET 10 on AL2023 version 3.11.7** <br /> * 64bit Amazon Linux 2023 v3.11.7 running .NET 10 *  | .NET 10.0.11, supports 10.0.11 | nginx 1.30.4 | 2023.12.20260817 | 3.6.7 | 
|  ** .NET 9 on AL2023 version 3.11.7** <br /> * 64bit Amazon Linux 2023 v3.11.7 running .NET 9 *  | .NET 9.0.19, supports 9.0.19 | nginx 1.30.4 | 2023.12.20260817 | 3.6.7 | 
|  ** .NET 8 on AL2023 version 3.11.7** <br /> * 64bit Amazon Linux 2023 v3.11.7 running .NET 8 *  | .NET 8.0.30, supports 8.0.30 | nginx 1.30.4 | 2023.12.20260817 | 3.6.7 | 

 For information about platform versions scheduled for retirement as published in [Platform Support Policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html), see [.NET Core on Linux](platforms-retiring.md#platforms-retiring.dotnetlinux) on the *Retiring Platform Versions* page. For information about previous platform versions, see [.NET Core on Linux platform history](platform-history-dotnetlinux.md).

## .NET on Windows Server
<a name="platforms-supported.net"></a>

You can get started in minutes using the [AWS Toolkit for Visual Studio](https://aws.amazon.com/visualstudio/). The toolkit includes the AWS libraries, project templates, code samples, and documentation. The AWS SDK for .NET supports the development of applications using .NET Framework 2.0 or later. 

**Note**  
This platform doesn't support the following Elastic Beanstalk features:  
Worker environments. For details, see [AWS Elastic Beanstalk Worker Environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features-managing-env-tiers.html) in the *AWS Elastic Beanstalk Developer Guide*.

To learn how to get started deploying a .NET application using the AWS Toolkit for Visual Studio, see [Creating and Deploying Elastic Beanstalk Applications in .NET Using AWS Toolkit for Visual Studio](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.html) in the *AWS Elastic Beanstalk Developer Guide*.

For information about the latest Microsoft security updates, see [Security TechCenter](https://portal.msrc.microsoft.com/en-us/) and [Security Advisories and Bulletins](https://technet.microsoft.com/en-us/library/security/).

 For information about .NET on Windows Server platform versions scheduled for retirement as published in [Platform Support Policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html), see [.NET on Windows Server](platforms-retiring.md#platforms-retiring.net) on the *Retiring Platform Versions* page. For information about previous .NET on Windows Server platform versions for Elastic Beanstalk, see [.NET on Windows Server platform history](platform-history-dotnet.md).

Elastic Beanstalk supports the following .NET on Windows Server platform versions.

### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server 2025 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server Core 2025 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server 2022 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server Core 2022 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server 2019 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server Core 2019 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server 2016 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.4**  |  * 64bit Windows Server Core 2016 v2.23.4 running IIS 10.0 *  | .NET 10.0.11, supports 10.0.11, 9.0.19, 8.0.30<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 | 

### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2025 with IIS 10.0 version 2.23.4**  | 2026.08.12 |  | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.4**  | 2026.08.12 |  | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server 2022 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server 2019 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.4**  | 2026.08.12 | 3.7.1252.1 | 2.5.2 | 3.3.4851.0 | 4.0 | 3.6.7 | 

## Node.js
<a name="platforms-supported.nodejs"></a>

Each Node.js platform version on Amazon Linux 2 supports multiple Node.js language versions. Only the default Node.js version is pre-installed. Valid Node.js versions, as well as the default version, are listed in the following table. Starting with Amazon Linux 2023, only one Node.js version is available on each platform version. Each Node.js version includes a respective version of npm (the Node.js package manager). The table lists npm versions in parentheses.

Elastic Beanstalk supports the following Node.js platform versions.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js 24 AL2023 version 6.11.7** <br /> * 64bit Amazon Linux 2023 v6.11.7 running Node.js 24 *  | 2023.12.20260817 | 24.19.0 (11.17.0)<br /> Default version: v24.19.0 | nginx 1.30.4 (default), Apache 2.4.68 | 2.50.1 | 3.6.7 | 
|  ** Node.js 22 AL2023 version 6.11.7** <br /> * 64bit Amazon Linux 2023 v6.11.7 running Node.js 22 *  | 2023.12.20260817 | 22.23.2 (10.9.8)<br /> Default version: v22.23.2 | nginx 1.30.4 (default), Apache 2.4.68 | 2.50.1 | 3.6.7 | 

 For information about platform versions scheduled for retirement as published in [Platform Support Policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html), see [Node.js](platforms-retiring.md#platforms-retiring.nodejs) on the *Retiring Platform Versions* page. For information about previous platform versions, see [Node.js platform history](platform-history-nodejs.md).

**Note**  
When support for the version of Node.js that you are using is removed from the platform version, you must change or remove the version setting prior to doing a [platform update](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.platform.upgrade.html). This may occur when a security vulnerability is identified for the Node.js version, or when the version is retired.  
When this happens, attempting to update to a new version of the platform that doesn't support the configured Node.js version fails. To avoid needing to create a new environment:  
 *Amazon Linux 2* – change the Node.js version setting in `package.json` to a Node.js version that is supported by both the old platform version and the new one, or remove the setting, and then deploy the new source bundle. Only then perform the platform update.
 *Amazon Linux AMI* – change the `NodeVersion` configuration option to a version that is supported by both the old platform version and the new one, or [remove the option setting](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-configuration-methods-after.html), and then perform the platform update.

## PHP
<a name="platforms-supported.PHP"></a>

Elastic Beanstalk supports the following PHP platform versions.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** PHP 8.5 AL2023 version 4.13.7** <br /> * 64bit Amazon Linux 2023 v4.13.7 running PHP 8.5 *  | 2023.12.20260817 | PHP 8.5.9 | Composer 2.10.2, PIE 1.4.10 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** PHP 8.4 AL2023 version 4.13.7** <br /> * 64bit Amazon Linux 2023 v4.13.7 running PHP 8.4 *  | 2023.12.20260817 | PHP 8.4.24 | Composer 2.10.2, PIE 1.4.10 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** PHP 8.3 AL2023 version 4.13.7** <br /> * 64bit Amazon Linux 2023 v4.13.7 running PHP 8.3 *  | 2023.12.20260817 | PHP 8.3.33 | Composer 2.10.2, PIE 1.4.10 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** PHP 8.2 AL2023 version 4.13.7** <br /> * 64bit Amazon Linux 2023 v4.13.7 running PHP 8.2 *  | 2023.12.20260817 | PHP 8.2.33 | Composer 2.10.2, PIE 1.4.10 | nginx 1.30.4 (default), Apache 2.4.68 | 

 For information about platform versions scheduled for retirement as published in [Platform Support Policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html), see [PHP](platforms-retiring.md#platforms-retiring.PHP) on the *Retiring Platform Versions* page. For information about previous platform versions, see [PHP platform history](platform-history-php.md).

## Python
<a name="platforms-supported.python"></a>

Elastic Beanstalk supports the following Python platform versions.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Python 3.14 AL2023 version 4.13.7** <br /> * 64bit Amazon Linux 2023 v4.13.7 running Python 3.14 *  | 2023.12.20260817 | Python 3.14.7 | pip 26.2.1, pipenv 2026.8.0 | 3.6.7 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** Python 3.13 AL2023 version 4.13.7** <br /> * 64bit Amazon Linux 2023 v4.13.7 running Python 3.13 *  | 2023.12.20260817 | Python 3.13.15 | pip 26.2.1, pipenv 2026.8.0 | 3.6.7 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** Python 3.12 AL2023 version 4.13.7** <br /> * 64bit Amazon Linux 2023 v4.13.7 running Python 3.12 *  | 2023.12.20260817 | Python 3.12.14 | pip 26.2.1, pipenv 2026.8.0 | 3.6.7 | nginx 1.30.4 (default), Apache 2.4.68 | 
|  ** Python 3.11 AL2023 version 4.13.7** <br /> * 64bit Amazon Linux 2023 v4.13.7 running Python 3.11 *  | 2023.12.20260817 | Python 3.11.15 | pip 26.2.1, pipenv 2026.8.0 | 3.6.7 | nginx 1.30.4 (default), Apache 2.4.68 | 

 For information about previous platform versions, see [Python platform history](platform-history-python.md).

## Ruby
<a name="platforms-supported.ruby"></a>

Elastic Beanstalk supports the following Ruby platform versions.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 4.0 AL2023 version 4.14.7** <br /> * 64bit Amazon Linux 2023 v4.14.7 running Ruby 4.0 *  | 2023.12.20260817 | Ruby 4.0.6 | RubyGems 4.0.16 | Puma 8.0.2 | 3.6.7 | nginx 1.30.4 | 
|  ** Ruby 3.4 AL2023 version 4.14.7** <br /> * 64bit Amazon Linux 2023 v4.14.7 running Ruby 3.4 *  | 2023.12.20260817 | Ruby 3.4.10-p104 | RubyGems 3.6.9 | Puma 8.0.2 | 3.6.7 | nginx 1.30.4 | 
|  ** Ruby 3.3 AL2023 version 4.14.7** <br /> * 64bit Amazon Linux 2023 v4.14.7 running Ruby 3.3 *  | 2023.12.20260817 | Ruby 3.3.12-p206 | RubyGems 3.5.22 | Puma 8.0.2 | 3.6.7 | nginx 1.30.4 | 

 For information about platform versions scheduled for retirement as published in [Platform Support Policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html), see [Ruby](platforms-retiring.md#platforms-retiring.ruby) on the *Retiring Platform Versions* page. For information about previous platform versions, see [Ruby platform history](platform-history-ruby.md).