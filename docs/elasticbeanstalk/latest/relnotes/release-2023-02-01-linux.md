# Release: Elastic Beanstalk Amazon Linux 2 platform updates on February 1, 2023

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux 2. The release includes security updates.
It also includes
AMI,
nginx,

Docker,
ECS based Docker,
Go,
Corretto,
Tomcat,
.NET Core,
Node.js,
PHP,
Python updates,

and Ruby updates.

**Release date:** February 1, 2023

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | --------------- | ---- | ------- | ------- | ---- | --------------- | -------------------------------------------------------------------------------------------------------- | ---- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2.html "https://alas.aws.amazon.com/alas2.html") on or before<br>**January 23, 2023\*<br>• to all Amazon Linux 2 platforms.<br>Some of the platform updates are security releases.<br>For more information, see<br>**Platform-specific updates\*<br>• in this table. |
| **Cross-platform updates**    | Made these cross-platform updates:<br>                                                                                                                                                                                                                                                                                                                                            | \*_Component_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AMI_<br>•    | Updated the base AMI to version 2.0.20230119.                                                            | <br> | \*_nginx_<br>• | Updated platforms supporting the nginx server to [version 1.22.1](https://nginx.org/en/CHANGES-1.22 "https://nginx.org/en/CHANGES-1.22").<br>This version includes security fixes.                    |      |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                                                                                         | \*_Platform_<br>•  | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Docker_<br>• | Updated Amazon ECS Agent to version \*_1.68.0_<br>• on the \*ECS Amazon Linux 2<br>• platform<br>branch. | <br> | \*_Go_<br>•    | Updated Go to release 1.19.5. For details, see [go1.19.5](https://go.dev/doc/devel/release#go1.19.5 "https://go.dev/doc/devel/release#go1.19.5") in<br>_The Go Programming Language Release History_. | <br> | **Corretto**, \*_Tomcat_<br>• | Updated Corretto 17 to version 17.0.6.10.1. For change log, see [Change Log for Amazon Corretto 17](https://github.com/corretto/corretto-17/blob/develop/CHANGELOG.md "https://github.com/corretto/corretto-17/blob/develop/CHANGELOG.md").<br>Updated Corretto 11 to version 11.0.18.10.1. For change log, see [Change Log for Amazon Corretto 11](https://github.com/corretto/corretto-11/blob/develop/CHANGELOG.md "https://github.com/corretto/corretto-11/blob/develop/CHANGELOG.md").<br>Updated Corretto 8 to version 8.362.08.1. For change log, see [Change Log for Amazon Corretto 8](https://github.com/corretto/corretto-8/blob/develop/CHANGELOG.md "https://github.com/corretto/corretto-8/blob/develop/CHANGELOG.md").<br>All three updates are security releases. | <br> | \*_.NET Core_<br>• | Updated .NET Core to release [6.0.13](https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.13/6.0.13.md#notable-changes "https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.13/6.0.13.md#notable-changes")<br>.<br>This is a security release.<br>**.Net Core on Linux platform — .NET Core 5 removed**<br>.NET Core 5 is being removed from the .Net Core on Linux platform, because it's past Microsoft’s end of support dates. For more<br>information, see [.NET and .NET Core Support<br>Policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core "https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core") on the Microsoft website. | <br> | \*_PHP_<br>• | Updated PHP 8.1 release to [8.1.14](https://www.php.net/releases/8_1_14.php "https://www.php.net/releases/8_1_14.php").<br>This is a security release.<br>NotePHP 7.4 is a retiring (deprecated) platform branch. For full version information of Elastic Beanstalk retiring<br>platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the<br>\*AWS Elastic Beanstalk Platforms<br>• guide. | <br> | \*_Python_<br>• | Updated Python 3.7 to [Python<br>3.7.16](https://docs.python.org/release/3.7.16/whatsnew/changelog.html#changelog "https://docs.python.org/release/3.7.16/whatsnew/changelog.html#changelog").<br>Updated Python 3.8 to [Python<br>3.8.16](https://docs.python.org/release/3.8.16/whatsnew/changelog.html "https://docs.python.org/release/3.8.16/whatsnew/changelog.html").<br>Both of these updates are security releases. | <br> | \*_Ruby_<br>• | Updated RubyGems to release 3.4.3. For details, see [3.4.3<br>Released](https://blog.rubygems.org/2023/01/06/3.4.3-released.html "https://blog.rubygems.org/2023/01/06/3.4.3-released.html") on the _RubyGems blog_.<br>Updated Puma to version [6.0.2](https://github.com/puma/puma/releases/tag/v6.0.2 "https://github.com/puma/puma/releases/tag/v6.0.2"). |     |

## New platform versions

###### Note

The following tables list all supported platform branches for each platform. Only Amazon Linux 2 platform branches are updated.

###### These platforms are updated:

- [Docker](#release-2023-02-01-linux.platforms.docker "#release-2023-02-01-linux.platforms.docker")
- [Go](#release-2023-02-01-linux.platforms.go "#release-2023-02-01-linux.platforms.go")
- [Java SE](#release-2023-02-01-linux.platforms.javase "#release-2023-02-01-linux.platforms.javase")
- [Tomcat](#release-2023-02-01-linux.platforms.java "#release-2023-02-01-linux.platforms.java")
- [.NET Core on Linux](#release-2023-02-01-linux.platforms.dotnetlinux "#release-2023-02-01-linux.platforms.dotnetlinux")
- [Node.js](#release-2023-02-01-linux.platforms.nodejs "#release-2023-02-01-linux.platforms.nodejs")
- [PHP](#release-2023-02-01-linux.platforms.PHP "#release-2023-02-01-linux.platforms.PHP")
- [Python](#release-2023-02-01-linux.platforms.python "#release-2023-02-01-linux.platforms.python")
- [Ruby](#release-2023-02-01-linux.platforms.ruby "#release-2023-02-01-linux.platforms.ruby")

### Docker

| Platform Version and _Solution Stack Name_                                   | AMI          | ECS Agent | Docker     | Docker Compose | Proxy Server |
| ---------------------------------------------------------------------------- | ------------ | --------- | ---------- | -------------- | ------------ |
| **Docker AL2 version 3.5.4**<br>_64bit Amazon Linux 2 v3.5.4 running Docker_ | 2.0.20230119 |           | 20.10.17-1 | 1.29.2         | nginx 1.22.1 |
| **ECS AL2 version 3.2.4**<br>_64bit Amazon Linux 2 v3.2.4 running ECS_       | 2.0.20230119 | 1.68.0    |            |                |              |

### Go

| Platform Version and _Solution Stack Name_                               | AMI          | Language  | AWS X-Ray | Proxy Server |
| ------------------------------------------------------------------------ | ------------ | --------- | --------- | ------------ |
| **Go 1 AL2 version 3.6.4**<br>_64bit Amazon Linux 2 v3.6.4 running Go 1_ | 2.0.20230119 | Go 1.19.5 | 3.2.0     | nginx 1.22.1 |

### Java SE

| Platform Version and _Solution Stack Name_                                         | AMI          | Language              | Tools                                 | AWS X-Ray | Proxy Server |
| ---------------------------------------------------------------------------------- | ------------ | --------------------- | ------------------------------------- | --------- | ------------ |
| **Corretto 17 version 3.4.4**<br>_64bit Amazon Linux 2 v3.4.4 running Corretto 17_ | 2.0.20230119 | Corretto 17.0.6.10.1  | Ant 1.10.7, Gradle 7.4.2, Maven 3.6.2 | 3.2.0     | nginx 1.22.1 |
| **Corretto 11 version 3.4.4**<br>_64bit Amazon Linux 2 v3.4.4 running Corretto 11_ | 2.0.20230119 | Corretto 11.0.18.10.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.22.1 |
| **Corretto 8 version 3.4.4**<br>_64bit Amazon Linux 2 v3.4.4 running Corretto 8_   | 2.0.20230119 | Corretto 8.362.08.1   | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.22.1 |

### Tomcat

| Platform Version and _Solution Stack Name_                                                                        | AMI          | Language              | AWS X-Ray | Application Server | Proxy Server                          |
| ----------------------------------------------------------------------------------------------------------------- | ------------ | --------------------- | --------- | ------------------ | ------------------------------------- |
| **Corretto 11 with Tomcat 8.5 AL2 version 4.3.4**<br>_64bit Amazon Linux 2 v4.3.4 running Tomcat 8.5 Corretto 11_ | 2.0.20230119 | Corretto 11.0.18.10.1 | 3.2.0     | Tomcat 8.5.79      | nginx 1.22.1 (default), Apache 2.4.54 |
| **Corretto 8 with Tomcat 8.5 AL2 version 4.3.4**<br>_64bit Amazon Linux 2 v4.3.4 running Tomcat 8.5 Corretto 8_   | 2.0.20230119 | Corretto 8.362.08.1   | 3.2.0     | Tomcat 8.5.79      | nginx 1.22.1 (default), Apache 2.4.54 |

### .NET Core on Linux

| Platform Version and _Solution Stack Name_                                            | Framework                            | Proxy Server | AMI          | AWS X-Ray |
| ------------------------------------------------------------------------------------- | ------------------------------------ | ------------ | ------------ | --------- |
| **.NET Core on AL2 version 2.5.0**<br>_64bit Amazon Linux 2 v2.5.0 running .NET Core_ | .NET 6.0.13, supports 6.0.13, 3.1.32 | nginx 1.22.1 | 2.0.20230119 | 3.2.0     |

### Node.js

| Platform Version and _Solution Stack Name_                                           | AMI          | Node.js versions (npm versions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Proxy Server                          | Git    | AWS X-Ray |
| ------------------------------------------------------------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------ | --------- |
| **Node.js 16 AL2 version 5.6.4**<br>_64bit Amazon Linux 2 v5.6.4 running Node.js 16_ | 2.0.20230119 | 16.19.0 (8.19.3), 16.18.1 (8.19.2), 16.18.0 (8.19.2), 16.17.1 (8.15.0), 16.17.0 (8.15.0), 16.16.0 (8.11.0), 16.15.1 (8.11.0), 16.15.0<br>(8.5.5), 16.14.2 (8.5.0), 16.14.1 (8.5.0), 16.14.0 (8.3.1), 16.13.2 (8.1.2), 16.13.1 (8.1.2), 16.13.0 (8.1.0), 16.12.0 (8.1.0), 16.11.1<br>(8.0.0), 16.11.0 (8.0.0), 16.10.0 (7.24.0), 16.9.1 (7.21.1), 16.9.0 (7.21.1), 16.8.0 (7.21.0), 16.7.0 (7.20.3), 16.6.2 (7.20.3), 16.6.1<br>(7.20.3), 16.6.0 (7.19.1), 16.5.0 (7.19.1), 16.4.2 (7.18.1), 16.4.1 (7.18.1), 16.4.0 (7.18.1), 16.3.0 (7.15.1), 16.2.0 (7.13.0), 16.1.0<br>(7.11.2), 16.0.0 (7.10.0)<br>Default version: 16.19.0                                                                                                                                                                                                                                                                   | nginx 1.22.1 (default), Apache 2.4.54 | 2.38.1 | 3.2.0     |
| **Node.js 14 AL2 version 5.6.4**<br>_64bit Amazon Linux 2 v5.6.4 running Node.js 14_ | 2.0.20230119 | 14.21.2 (6.14.17), 14.21.1 (6.14.17), 14.21.0 (6.14.17), 14.20.1 (6.14.17), 14.20.0 (6.14.17), 14.19.3 (6.14.17), 14.19.2 (6.14.17),<br>14.19.1 (6.14.16), 14.19.0 (6.14.16), 14.18.3 (6.14.15), 14.18.2 (6.14.15), 14.18.1 (6.14.15), 14.18.0 (6.14.15), 14.17.6 (6.14.15), 14.17.5<br>(6.14.14), 14.17.4 (6.14.14), 14.17.3 (6.14.13), 14.17.2 (6.14.13), 14.17.1 (6.14.13), 14.17.0 (6.14.13), 14.16.1 (6.14.12), 14.16.0<br>(6.14.11), 14.15.5 (6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8), 14.15.0 (6.14.8), 14.14.0 (6.14.8),<br>14.13.1 (6.14.8), 14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0 (6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7),<br>14.7.0 (6.14.7), 14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0 (6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br>Default version: 14.21.2 | nginx 1.22.1 (default), Apache 2.4.54 | 2.38.1 | 3.2.0     |

### PHP

| Platform Version and _Solution Stack Name_                                     | AMI          | Language   | Composer | Proxy Server                          |
| ------------------------------------------------------------------------------ | ------------ | ---------- | -------- | ------------------------------------- |
| **PHP 8.1 AL2 version 3.5.4**<br>_64bit Amazon Linux 2 v3.5.4 running PHP 8.1_ | 2.0.20230119 | PHP 8.1.14 | 2.3.5    | nginx 1.22.1 (default), Apache 2.4.54 |
| **PHP 8.0 AL2 version 3.5.4**<br>_64bit Amazon Linux 2 v3.5.4 running PHP 8.0_ | 2.0.20230119 | PHP 8.0.25 | 2.0.13   | nginx 1.22.1 (default), Apache 2.4.54 |

### Python

| Platform Version and _Solution Stack Name_                                           | AMI          | Language      | Package Manager  | Packager | meld3 | AWS X-Ray | Proxy Server                          |
| ------------------------------------------------------------------------------------ | ------------ | ------------- | ---------------- | -------- | ----- | --------- | ------------------------------------- |
| **Python 3.8 AL2 version 3.4.4**<br>_64bit Amazon Linux 2 v3.4.4 running Python 3.8_ | 2.0.20230119 | Python 3.8.16 | pipenv 2021.11.9 |          |       | 3.2.0     | nginx 1.22.1 (default), Apache 2.4.54 |
| **Python 3.7 AL2 version 3.4.4**<br>_64bit Amazon Linux 2 v3.4.4 running Python 3.7_ | 2.0.20230119 | Python 3.7.16 | pipenv 2021.11.9 |          |       | 3.2.0     | nginx 1.22.1 (default), Apache 2.4.54 |

### Ruby

| Platform Version and _Solution Stack Name_                                       | AMI          | Language        | Package Manager | Application Server | AWS X-Ray | Proxy Server |
| -------------------------------------------------------------------------------- | ------------ | --------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 3.0 AL2 version 3.6.3**<br>_64bit Amazon Linux 2 v3.6.3 running Ruby 3.0_ | 2.0.20230119 | Ruby 3.0.5-p211 | RubyGems 3.4.3  | Puma 6.0.2         | 3.2.0     | nginx 1.22.1 |
| **Ruby 2.7 AL2 version 3.6.3**<br>_64bit Amazon Linux 2 v3.6.3 running Ruby 2.7_ | 2.0.20230119 | Ruby 2.7.7-p221 | RubyGems 3.4.3  | Puma 6.0.2         | 3.2.0     | nginx 1.22.1 |
