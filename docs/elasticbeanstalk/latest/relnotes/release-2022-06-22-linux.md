# Release: Elastic Beanstalk Amazon Linux platform updates on June 22, 2022

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux.
The release includes security updates.
It also includes
AMI,

ECS based Docker,
Go,

.NET Core,
Node.js,
and PHP updates.

**Release date:** June 22, 2022

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ | --------------- | ---- | ------- | ------- | ---- | ----------------- | ------------------------------------------------------------------------------------------------------------- | ---- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2.html "https://alas.aws.amazon.com/alas2.html") on or before **June 16, 2022\*<br>• to all released Amazon Linux 2 platforms.<br>The<br>**Go**<br>and **.NET Core**<br>releases are security releases.<br>For more information, see<br>**Platform-specific updates\*<br>• in this table. |
| **Cross-platform updates**    | Made these cross-platform updates:<br>                                                                                                                                                                                                                                                                                                                                                                 | \*_Component_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Base AMI_<br>• | Updated the base AMI to version **2.0.20220606**.                                                             |      |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                                                                                                              | \*_Platform_<br>•  | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Docker_<br>•   | Updated Amazon ECS to version \*_1.61.1_<br>• on the \*ECS running on Amazon Linux 2<br>• platform<br>branch. | <br> | \*_Go_<br>• | Updated Go to release **1.18.3**. For details, see [go1.18](https://golang.org/doc/devel/release.html#go1.18 "https://golang.org/doc/devel/release.html#go1.18") in _The Go Programming Language Release<br>History_.<br>The Go 1.18.3 release is a security release. | <br> | \*_.NET Core_<br>• | Updated .NET Core to releases [6.0.6](https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.6/6.0.6.md "https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.6/6.0.6.md") and<br>and [3.1.26](https://github.com/dotnet/core/blob/main/release-notes/3.1/3.1.26/3.1.26.md "https://github.com/dotnet/core/blob/main/release-notes/3.1/3.1.26/3.1.26.md")<br>Both .NET Core updates are security releases. | <br> | \*_Node.js_<br>• | Updated Node.js 16 to add support for Node version<br>[16.15.1](https://nodejs.org/en/blog/release/v16.15.1/ "https://nodejs.org/en/blog/release/v16.15.1/"). | <br> | \*_PHP_<br>• | Updated PHP 8.0 and 7.4 to releases [8.0.18](https://www.php.net/releases/8_0_18.php "https://www.php.net/releases/8_0_18.php") and [7.4.29](https://www.php.net/releases/7_4_29.php "https://www.php.net/releases/7_4_29.php"), respectively. |     |

## New platform versions

###### These currently supported platforms are updated:

- [Docker](#release-2022-06-22-linux.platforms.docker "#release-2022-06-22-linux.platforms.docker")
- [Go](#release-2022-06-22-linux.platforms.go "#release-2022-06-22-linux.platforms.go")
- [Java SE](#release-2022-06-22-linux.platforms.javase "#release-2022-06-22-linux.platforms.javase")
- [Tomcat](#release-2022-06-22-linux.platforms.java "#release-2022-06-22-linux.platforms.java")
- [.NET Core on Linux](#release-2022-06-22-linux.platforms.dotnetlinux "#release-2022-06-22-linux.platforms.dotnetlinux")
- [Node.js](#release-2022-06-22-linux.platforms.nodejs "#release-2022-06-22-linux.platforms.nodejs")
- [PHP](#release-2022-06-22-linux.platforms.PHP "#release-2022-06-22-linux.platforms.PHP")
- [Python](#release-2022-06-22-linux.platforms.python "#release-2022-06-22-linux.platforms.python")
- [Ruby](#release-2022-06-22-linux.platforms.ruby "#release-2022-06-22-linux.platforms.ruby")

### Docker

###### Note

_ECS Amazon Linux 2 v3.1.3_ is running ECS Agent 1.61.1.

| Platform Version and _Solution Stack Name_                                     | AMI          | Docker     | Docker Compose | Proxy Server |
| ------------------------------------------------------------------------------ | ------------ | ---------- | -------------- | ------------ |
| **Docker AL2 version 3.4.17**<br>_64bit Amazon Linux 2 v3.4.17 running Docker_ | 2.0.20220606 | 20.10.13-2 | 1.29.2         | nginx 1.20.0 |
| **ECS AL2 version 3.1.3**<br>_64bit Amazon Linux 2 v3.1.3 running ECS_         | 2.0.20220606 |            |                |              |

### Go

| Platform Version and _Solution Stack Name_                               | AMI          | Language  | AWS X-Ray | Proxy Server |
| ------------------------------------------------------------------------ | ------------ | --------- | --------- | ------------ |
| **Go 1 AL2 version 3.5.3**<br>_64bit Amazon Linux 2 v3.5.3 running Go 1_ | 2.0.20220606 | Go 1.18.3 | 3.2.0     | nginx 1.20.0 |

### Java SE

| Platform Version and _Solution Stack Name_                                           | AMI          | Language             | Tools                                 | AWS X-Ray | Proxy Server |
| ------------------------------------------------------------------------------------ | ------------ | -------------------- | ------------------------------------- | --------- | ------------ |
| **Corretto 11 version 3.2.16**<br>_64bit Amazon Linux 2 v3.2.16 running Corretto 11_ | 2.0.20220606 | Corretto 11.0.15.9.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.20.0 |
| **Corretto 8 version 3.2.16**<br>_64bit Amazon Linux 2 v3.2.16 running Corretto 8_   | 2.0.20220606 | Corretto 8.332.08.1  | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.20.0 |

### Tomcat

| Platform Version and _Solution Stack Name_                                                                          | AMI          | Language             | AWS X-Ray | Application Server | Proxy Server                          |
| ------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------- | --------- | ------------------ | ------------------------------------- |
| **Corretto 11 with Tomcat 8.5 AL2 version 4.2.16**<br>_64bit Amazon Linux 2 v4.2.16 running Tomcat 8.5 Corretto 11_ | 2.0.20220606 | Corretto 11.0.15.9.1 | 3.2.0     | Tomcat 8.5.75      | nginx 1.20.0 (default), Apache 2.4.53 |
| **Corretto 8 with Tomcat 8.5 AL2 version 4.2.16**<br>_64bit Amazon Linux 2 v4.2.16 running Tomcat 8.5 Corretto 8_   | 2.0.20220606 | Corretto 8.332.08.1  | 3.2.0     | Tomcat 8.5.75      | nginx 1.20.0 (default), Apache 2.4.53 |

### .NET Core on Linux

| Platform Version and _Solution Stack Name_                                            | Framework                                  | Proxy Server | AMI          | AWS X-Ray |
| ------------------------------------------------------------------------------------- | ------------------------------------------ | ------------ | ------------ | --------- |
| **.NET Core on AL2 version 2.3.3**<br>_64bit Amazon Linux 2 v2.3.3 running .NET Core_ | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26 | nginx 1.20.0 | 2.0.20220606 | 3.2.0     |

### Node.js

| Platform Version and _Solution Stack Name_                                           | AMI          | Node.js versions (npm versions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Proxy Server                          | Git    | AWS X-Ray |
| ------------------------------------------------------------------------------------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------ | --------- |
| **Node.js 16 AL2 version 5.5.4**<br>_64bit Amazon Linux 2 v5.5.4 running Node.js 16_ | 2.0.20220606 | 16.15.1 (8.11.0), 16.15.0 (8.5.5), 16.14.2 (8.5.0), 16.14.1 (8.5.0), 16.14.0 (8.3.1), 16.13.2 (8.1.2), 16.13.1 (8.1.2), 16.13.0 (8.1.0),<br>16.12.0 (8.1.0), 16.11.1 (8.0.0), 16.11.0 (8.0.0), 16.10.0 (7.24.0), 16.9.1 (7.21.1), 16.9.0 (7.21.1), 16.8.0 (7.21.0), 16.7.0 (7.20.3),<br>16.6.2 (7.20.3), 16.6.1 (7.20.3), 16.6.0 (7.19.1), 16.5.0 (7.19.1), 16.4.2 (7.18.1), 16.4.1 (7.18.1), 16.4.0 (7.18.1), 16.3.0 (7.15.1), 16.2.0<br>(7.13.0), 16.1.0 (7.11.2), 16.0.0 (7.10.0)<br>Default version: 16.15.1                                                                                                                                                                                                                                                                                   | nginx 1.20.0 (default), Apache 2.4.53 | 2.32.0 | 3.2.0     |
| **Node.js 14 AL2 version 5.5.4**<br>_64bit Amazon Linux 2 v5.5.4 running Node.js 14_ | 2.0.20220606 | 14.19.3 (6.14.17), 14.19.2 (6.14.17), 14.19.1 (6.14.16), 14.19.0 (6.14.16), 14.18.3 (6.14.15), 14.18.2 (6.14.15), 14.18.1 (6.14.15),<br>14.18.0 (6.14.15), 14.17.6 (6.14.15), 14.17.5 (6.14.14), 14.17.4 (6.14.14), 14.17.3 (6.14.13), 14.17.2 (6.14.13), 14.17.1 (6.14.13), 14.17.0<br>(6.14.13), 14.16.1 (6.14.12), 14.16.0 (6.14.11), 14.15.5 (6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8),<br>14.15.0 (6.14.8), 14.14.0 (6.14.8), 14.13.1 (6.14.8), 14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0<br>(6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7), 14.7.0 (6.14.7), 14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0<br>(6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br>Default version: 14.19.3 | nginx 1.20.0 (default), Apache 2.4.53 | 2.32.0 | 3.2.0     |

### PHP

| Platform Version and _Solution Stack Name_                                       | AMI          | Language   | Composer | Proxy Server                          |
| -------------------------------------------------------------------------------- | ------------ | ---------- | -------- | ------------------------------------- |
| **PHP 8.0 AL2 version 3.3.15**<br>_64bit Amazon Linux 2 v3.3.15 running PHP 8.0_ | 2.0.20220606 | PHP 8.0.18 | 2.0.13   | nginx 1.20.0 (default), Apache 2.4.53 |

### Python

| Platform Version and _Solution Stack Name_                                             | AMI          | Language      | Package Manager  | Packager | meld3 | AWS X-Ray | Proxy Server                          |
| -------------------------------------------------------------------------------------- | ------------ | ------------- | ---------------- | -------- | ----- | --------- | ------------------------------------- |
| **Python 3.8 AL2 version 3.3.15**<br>_64bit Amazon Linux 2 v3.3.15 running Python 3.8_ | 2.0.20220606 | Python 3.8.5  | pipenv 2021.11.9 |          |       | 3.2.0     | nginx 1.20.0 (default), Apache 2.4.53 |
| **Python 3.7 AL2 version 3.3.15**<br>_64bit Amazon Linux 2 v3.3.15 running Python 3.7_ | 2.0.20220606 | Python 3.7.10 | pipenv 2021.11.9 |          |       | 3.2.0     | nginx 1.20.0 (default), Apache 2.4.53 |

### Ruby

| Platform Version and _Solution Stack Name_                                       | AMI          | Language        | Package Manager | Application Server | AWS X-Ray | Proxy Server |
| -------------------------------------------------------------------------------- | ------------ | --------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 3.0 AL2 version 3.4.8**<br>_64bit Amazon Linux 2 v3.4.8 running Ruby 3.0_ | 2.0.20220606 | Ruby 3.0.4-p208 | RubyGems 3.3.15 | Puma 5.6.4         | 3.2.0     | nginx 1.20.0 |
| **Ruby 2.7 AL2 version 3.4.8**<br>_64bit Amazon Linux 2 v3.4.8 running Ruby 2.7_ | 2.0.20220606 | Ruby 2.7.6-p219 | RubyGems 3.3.15 | Puma 5.6.4         | 3.2.0     | nginx 1.20.0 |
