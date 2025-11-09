# Release: Elastic Beanstalk Amazon Linux 2 platform updates on December 6, 2022

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux 2. The release includes security updates.
It also includes
AMI,

ECS based Docker,
Go,

.NET Core,
Node.js,
PHP,
Python,
and Ruby updates.

**Release date:** December 6, 2022

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | --------------- | ---- | ------- | ------- | ---- | --------------- | -------------------------------------------------------------------------------------------------------- | ---- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2.html "https://alas.aws.amazon.com/alas2.html") on or before<br>**November 3, 2022\*<br>• to all Amazon Linux 2 platforms.<br>Some of the platform updates are security releases.<br>For more information, see<br>**Platform-specific updates\*<br>• in this table. |
| **Cross-platform updates**    | Made these cross-platform updates:<br>                                                                                                                                                                                                                                                                                                                                            | \*_Component_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AMI_<br>•    | Updated the base AMI to version 2.0.20221103.                                                            |      |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                                                                                         | \*_Platform_<br>•  | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Docker_<br>• | Updated Amazon ECS Agent to version \*_1.65.1_<br>• on the \*ECS Amazon Linux 2<br>• platform<br>branch. | <br> | \*_Go_<br>• | Updated Go to release 1.19.3. For details, see [go1.19.3](https://go.dev/doc/devel/release#go1.19.3 "https://go.dev/doc/devel/release#go1.19.3") in<br>_The Go Programming Language Release History_.<br>This is a security release. | <br> | \*_.NET Core_<br>• | Updated .NET Core to releases [6.0.11](https://github.com//dotnet/core/blob/main/release-notes/6.0/6.0.11/6.0.11.md#notable-changes "https://github.com//dotnet/core/blob/main/release-notes/6.0/6.0.11/6.0.11.md#notable-changes") and [3.1.31](https://github.com/dotnet/core/blob/master/release-notes/3.1/3.1.31/3.1.31.md#notable-changes "https://github.com/dotnet/core/blob/master/release-notes/3.1/3.1.31/3.1.31.md#notable-changes"). | <br> | \*_Node.js_<br>• | Updated Node.js 16 to add support for Node version [16.18.1](https://nodejs.org/en/blog/release/v16.18.1/ "https://nodejs.org/en/blog/release/v16.18.1/").<br>Updated Node.js 14 to add support for Node versions [14.21.1](https://nodejs.org/en/blog/release/v14.21.1/ "https://nodejs.org/en/blog/release/v14.21.1/").<br>The new Node.js updates are security releases.<br>NoteNode.js 12 is a retiring (deprecated) platform branch. For full version information of Elastic Beanstalk retiring<br>platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the<br>\*AWS Elastic Beanstalk Platforms<br>• guide. | <br> | \*_PHP_<br>• | Updated PHP 8.1 release to [8.1.13](https://www.php.net/releases/8_1_13.php "https://www.php.net/releases/8_1_13.php").<br>Updated PHP 8.0 release to [8.0.25](https://www.php.net/releases/8_0_25.php "https://www.php.net/releases/8_0_25.php").<br>This PHP 8.0 update is a security<br>release.<br>NotePHP 7.4 is a retiring (deprecated) platform branch. For full version information of Elastic Beanstalk retiring<br>platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the<br>\*AWS Elastic Beanstalk Platforms<br>• guide. | <br> | \*_Python_<br>• | Updated Python 3.8 to [Python<br>3.8.15](https://docs.python.org/release/3.8.15/whatsnew/changelog.html#python-3-8-15-final "https://docs.python.org/release/3.8.15/whatsnew/changelog.html#python-3-8-15-final").<br>This is a security release. | <br> | \*_Ruby_<br>• | Updated Ruby 3.0 and 2.7 to releases<br>[3.0.5](https://www.ruby-lang.org/en/news/2022/11/24/ruby-3-0-5-released/ "https://www.ruby-lang.org/en/news/2022/11/24/ruby-3-0-5-released/") and<br>[2.7.7](https://www.ruby-lang.org/en/news/2022/11/24/ruby-2-7-7-released/ "https://www.ruby-lang.org/en/news/2022/11/24/ruby-2-7-7-released/"), respectively.<br>Both of these updates are security releases.<br>Updated RubyGems to release 3.3.26. For details, see [3.3.26<br>Released](https://blog.rubygems.org/2022/11/17/3.3.26-released.html "https://blog.rubygems.org/2022/11/17/3.3.26-released.html") on the _RubyGems blog_.<br>NoteRuby 2.6 is a retiring (deprecated) platform branch. For full version information of Elastic Beanstalk retiring<br>platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the<br>\*AWS Elastic Beanstalk Platforms<br>• guide. |     |

## New platform versions

###### Note

The following tables list all supported platform branches for each platform. Only Amazon Linux 2 platform branches are updated.

###### These platforms are updated:

- [Docker](#release-2022-12-06-linux.platforms.docker "#release-2022-12-06-linux.platforms.docker")
- [Go](#release-2022-12-06-linux.platforms.go "#release-2022-12-06-linux.platforms.go")
- [Java SE](#release-2022-12-06-linux.platforms.javase "#release-2022-12-06-linux.platforms.javase")
- [Tomcat](#release-2022-12-06-linux.platforms.java "#release-2022-12-06-linux.platforms.java")
- [.NET Core on Linux](#release-2022-12-06-linux.platforms.dotnetlinux "#release-2022-12-06-linux.platforms.dotnetlinux")
- [Node.js](#release-2022-12-06-linux.platforms.nodejs "#release-2022-12-06-linux.platforms.nodejs")
- [PHP](#release-2022-12-06-linux.platforms.PHP "#release-2022-12-06-linux.platforms.PHP")
- [Python](#release-2022-12-06-linux.platforms.python "#release-2022-12-06-linux.platforms.python")
- [Ruby](#release-2022-12-06-linux.platforms.ruby "#release-2022-12-06-linux.platforms.ruby")

### Docker

| Platform Version and _Solution Stack Name_                                   | AMI          | ECS Agent | Docker     | Docker Compose | Proxy Server |
| ---------------------------------------------------------------------------- | ------------ | --------- | ---------- | -------------- | ------------ |
| **Docker AL2 version 3.5.2**<br>_64bit Amazon Linux 2 v3.5.2 running Docker_ | 2.0.20221103 |           | 20.10.17-1 | 1.29.2         | nginx 1.22.0 |
| **ECS AL2 version 3.2.2**<br>_64bit Amazon Linux 2 v3.2.2 running ECS_       | 2.0.20221103 | 1.65.1    |            |                |              |

### Go

| Platform Version and _Solution Stack Name_                               | AMI          | Language  | AWS X-Ray | Proxy Server |
| ------------------------------------------------------------------------ | ------------ | --------- | --------- | ------------ |
| **Go 1 AL2 version 3.6.2**<br>_64bit Amazon Linux 2 v3.6.2 running Go 1_ | 2.0.20221103 | Go 1.19.3 | 3.2.0     | nginx 1.22.0 |

### Java SE

| Platform Version and _Solution Stack Name_                                         | AMI          | Language             | Tools                                 | AWS X-Ray | Proxy Server |
| ---------------------------------------------------------------------------------- | ------------ | -------------------- | ------------------------------------- | --------- | ------------ |
| **Corretto 17 version 3.4.2**<br>_64bit Amazon Linux 2 v3.4.2 running Corretto 17_ | 2.0.20221103 | Corretto 17.0.5.8.1  | Ant 1.10.7, Gradle 7.4.2, Maven 3.6.2 | 3.2.0     | nginx 1.22.0 |
| **Corretto 11 version 3.4.2**<br>_64bit Amazon Linux 2 v3.4.2 running Corretto 11_ | 2.0.20221103 | Corretto 11.0.17.8.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.22.0 |
| **Corretto 8 version 3.4.2**<br>_64bit Amazon Linux 2 v3.4.2 running Corretto 8_   | 2.0.20221103 | Corretto 8.352.08.1  | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.22.0 |

### Tomcat

| Platform Version and _Solution Stack Name_                                                                        | AMI          | Language             | AWS X-Ray | Application Server | Proxy Server                          |
| ----------------------------------------------------------------------------------------------------------------- | ------------ | -------------------- | --------- | ------------------ | ------------------------------------- |
| **Corretto 11 with Tomcat 8.5 AL2 version 4.3.2**<br>_64bit Amazon Linux 2 v4.3.2 running Tomcat 8.5 Corretto 11_ | 2.0.20221103 | Corretto 11.0.17.8.1 | 3.2.0     | Tomcat 8.5.79      | nginx 1.22.0 (default), Apache 2.4.54 |
| **Corretto 8 with Tomcat 8.5 AL2 version 4.3.2**<br>_64bit Amazon Linux 2 v4.3.2 running Tomcat 8.5 Corretto 8_   | 2.0.20221103 | Corretto 8.352.08.1  | 3.2.0     | Tomcat 8.5.79      | nginx 1.22.0 (default), Apache 2.4.54 |

### .NET Core on Linux

| Platform Version and _Solution Stack Name_                                            | Framework                                    | Proxy Server | AMI          | AWS X-Ray |
| ------------------------------------------------------------------------------------- | -------------------------------------------- | ------------ | ------------ | --------- |
| **.NET Core on AL2 version 2.4.2**<br>_64bit Amazon Linux 2 v2.4.2 running .NET Core_ | .NET 6.0.11, supports 6.0.11, 5.0.17, 3.1.31 | nginx 1.22.0 | 2.0.20221103 | 3.2.0     |

### Node.js

| Platform Version and _Solution Stack Name_                                           | AMI          | Node.js versions (npm versions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Proxy Server                          | Git    | AWS X-Ray |
| ------------------------------------------------------------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- | ------ | --------- |
| **Node.js 16 AL2 version 5.6.2**<br>_64bit Amazon Linux 2 v5.6.2 running Node.js 16_ | 2.0.20221103 | 16.18.1 (8.19.2), 16.18.0 (8.19.2), 16.17.1 (8.15.0), 16.17.0 (8.15.0), 16.16.0 (8.11.0), 16.15.1 (8.11.0), 16.15.0 (8.5.5), 16.14.2<br>(8.5.0), 16.14.1 (8.5.0), 16.14.0 (8.3.1), 16.13.2 (8.1.2), 16.13.1 (8.1.2), 16.13.0 (8.1.0), 16.12.0 (8.1.0), 16.11.1 (8.0.0), 16.11.0<br>(8.0.0), 16.10.0 (7.24.0), 16.9.1 (7.21.1), 16.9.0 (7.21.1), 16.8.0 (7.21.0), 16.7.0 (7.20.3), 16.6.2 (7.20.3), 16.6.1 (7.20.3), 16.6.0<br>(7.19.1), 16.5.0 (7.19.1), 16.4.2 (7.18.1), 16.4.1 (7.18.1), 16.4.0 (7.18.1), 16.3.0 (7.15.1), 16.2.0 (7.13.0), 16.1.0 (7.11.2), 16.0.0<br>(7.10.0)<br>Default version: 16.18.1                                                                                                                                                                                                                                                                  | nginx 1.22.0 (default), Apache 2.4.54 | 2.37.1 | 3.2.0     |
| **Node.js 14 AL2 version 5.6.2**<br>_64bit Amazon Linux 2 v5.6.2 running Node.js 14_ | 2.0.20221103 | 14.21.1 (6.14.17), 14.21.0 (6.14.17), 14.20.1 (6.14.17), 14.20.0 (6.14.17), 14.19.3 (6.14.17), 14.19.2 (6.14.17), 14.19.1 (6.14.16),<br>14.19.0 (6.14.16), 14.18.3 (6.14.15), 14.18.2 (6.14.15), 14.18.1 (6.14.15), 14.18.0 (6.14.15), 14.17.6 (6.14.15), 14.17.5 (6.14.14), 14.17.4<br>(6.14.14), 14.17.3 (6.14.13), 14.17.2 (6.14.13), 14.17.1 (6.14.13), 14.17.0 (6.14.13), 14.16.1 (6.14.12), 14.16.0 (6.14.11), 14.15.5<br>(6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8), 14.15.0 (6.14.8), 14.14.0 (6.14.8), 14.13.1 (6.14.8),<br>14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0 (6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7), 14.7.0 (6.14.7),<br>14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0 (6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br>Default version: 14.21.1 | nginx 1.22.0 (default), Apache 2.4.54 | 2.37.1 | 3.2.0     |

### PHP

| Platform Version and _Solution Stack Name_                                     | AMI          | Language   | Composer | Proxy Server                          |
| ------------------------------------------------------------------------------ | ------------ | ---------- | -------- | ------------------------------------- |
| **PHP 8.1 AL2 version 3.5.2**<br>_64bit Amazon Linux 2 v3.5.2 running PHP 8.1_ | 2.0.20221103 | PHP 8.1.13 | 2.3.5    | nginx 1.22.0 (default), Apache 2.4.54 |
| **PHP 8.0 AL2 version 3.5.2**<br>_64bit Amazon Linux 2 v3.5.2 running PHP 8.0_ | 2.0.20221103 | PHP 8.0.25 | 2.0.13   | nginx 1.22.0 (default), Apache 2.4.54 |

### Python

| Platform Version and _Solution Stack Name_                                           | AMI          | Language      | Package Manager  | Packager | meld3 | AWS X-Ray | Proxy Server                          |
| ------------------------------------------------------------------------------------ | ------------ | ------------- | ---------------- | -------- | ----- | --------- | ------------------------------------- |
| **Python 3.8 AL2 version 3.4.2**<br>_64bit Amazon Linux 2 v3.4.2 running Python 3.8_ | 2.0.20221103 | Python 3.8.15 | pipenv 2021.11.9 |          |       | 3.2.0     | nginx 1.22.0 (default), Apache 2.4.54 |
| **Python 3.7 AL2 version 3.4.2**<br>_64bit Amazon Linux 2 v3.4.2 running Python 3.7_ | 2.0.20221103 | Python 3.7.10 | pipenv 2021.11.9 |          |       | 3.2.0     | nginx 1.22.0 (default), Apache 2.4.54 |

### Ruby

| Platform Version and _Solution Stack Name_                                       | AMI          | Language        | Package Manager | Application Server | AWS X-Ray | Proxy Server |
| -------------------------------------------------------------------------------- | ------------ | --------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 3.0 AL2 version 3.6.1**<br>_64bit Amazon Linux 2 v3.6.1 running Ruby 3.0_ | 2.0.20221103 | Ruby 3.0.5-p211 | RubyGems 3.3.26 | Puma 6.0.0         | 3.2.0     | nginx 1.22.0 |
| **Ruby 2.7 AL2 version 3.6.1**<br>_64bit Amazon Linux 2 v3.6.1 running Ruby 2.7_ | 2.0.20221103 | Ruby 2.7.7-p221 | RubyGems 3.3.26 | Puma 6.0.0         | 3.2.0     | nginx 1.22.0 |
