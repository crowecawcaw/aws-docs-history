# Release: Elastic Beanstalk Amazon Linux platform updates on March 2, 2022

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux. The release includes security updates.
It also introduces a new branch, **Node.js 16**, and announces the deprecation of two platform branches.
It also includes AMI, Go, Corretto, Node.js, PHP, and Ruby updates.

**Release date:** March 2, 2022

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | --------------- | ---- | ------- | ------- | ---- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2.html "https://alas.aws.amazon.com/alas2.html") on or before **February 21, 2022\*<br>• to all released Amazon Linux 2 platforms.<br>Some of the platform updates are security releases.<br>For more information, see **Platform-specific updates\*<br>• in this<br>table. |
| **Cross-platform updates**    | Made these cross-platform updates:<br>                                                                                                                                                                                                                                                                                                                                                   | \*_Component_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Base AMI_<br>• | Updated the base AMI to version **2.0.20220207**.                                                                                                                                                                     |      |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                                                                                                | \*_Platform_<br>•  | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Go_<br>•       | Updated Go to release **1.17.7**. For details, see [go1.17](https://golang.org/doc/devel/release.html#go1.17 "https://golang.org/doc/devel/release.html#go1.17") in _The Go Programming Language Release<br>History_. | <br> | \*_Corretto_<br>• | Updated Corretto 11 to version **11.0.14.10.1**. For more information, see [Change Log for Amazon Corretto 11](https://github.com/corretto/corretto-11/blob/develop/CHANGELOG.md "https://github.com/corretto/corretto-11/blob/develop/CHANGELOG.md") in the Corretto 11 repository<br>on GitHub. | <br> | \*_Node.js_<br>• | Added a new platform branch, **Node.js 16**. For documentation of the latest version, see [Node.js v16.x Documentation](https://nodejs.org/dist/latest-v16.x/docs/api/ "https://nodejs.org/dist/latest-v16.x/docs/api/").<br>Graviton instance type support for the Node.js 16 platform branch will be available in the next Node.js platform update.<br>Updated Node.js 14 to add support for Node version<br>[14.19.0](https://nodejs.org/en/blog/release/v14.19.0/ "https://nodejs.org/en/blog/release/v14.19.0/").<br>Updated Node.js 12 to add support for Node version<br>[12.22.10](https://nodejs.org/en/blog/release/v12.22.10/ "https://nodejs.org/en/blog/release/v12.22.10/").<br>This new Node.js 12 version is a security release.<br>The platform branch \*_Node.js 12 running on 64bit Amazon Linux 2_<br>• has been scheduled for retirement on October 31, 2022. For more<br>information, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md")<br>in the \*AWS Elastic Beanstalk Platforms<br>• guide. | <br> | \*_PHP_<br>• | The platform branch \*_PHP 7.4 running on 64bit Amazon Linux 2_<br>• has been scheduled for retirement on May 31, 2023. For more<br>information, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md")<br>in the \*AWS Elastic Beanstalk Platforms<br>• guide. | <br> | \*_Ruby_<br>• | Updated RubyGems to release [3.3.7](https://blog.rubygems.org/2022/02/09/3.3.7-released.html "https://blog.rubygems.org/2022/02/09/3.3.7-released.html").<br>Updated Puma to version [5.6.2](https://github.com/puma/puma/releases/tag/v5.6.2 "https://github.com/puma/puma/releases/tag/v5.6.2").<br>This new Puma version is a security release.<br>The platform branch \*_Ruby 2.6 running on 64bit Amazon Linux 2_<br>• has been scheduled for retirement on September 30, 2022.<br>For more information, see [Elastic Beanstalk platform<br>versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the \*AWS Elastic Beanstalk Platforms<br>• guide. |     |

## New platform versions

###### These currently supported platforms are updated:

- [Docker](#release-2022-03-02-linux.platforms.docker "#release-2022-03-02-linux.platforms.docker")
- [Go](#release-2022-03-02-linux.platforms.go "#release-2022-03-02-linux.platforms.go")
- [Java SE](#release-2022-03-02-linux.platforms.javase "#release-2022-03-02-linux.platforms.javase")
- [Tomcat](#release-2022-03-02-linux.platforms.java "#release-2022-03-02-linux.platforms.java")
- [.NET Core on Linux](#release-2022-03-02-linux.platforms.dotnetlinux "#release-2022-03-02-linux.platforms.dotnetlinux")
- [Node.js](#release-2022-03-02-linux.platforms.nodejs "#release-2022-03-02-linux.platforms.nodejs")
- [PHP](#release-2022-03-02-linux.platforms.PHP "#release-2022-03-02-linux.platforms.PHP")
- [Python](#release-2022-03-02-linux.platforms.python "#release-2022-03-02-linux.platforms.python")
- [Ruby](#release-2022-03-02-linux.platforms.ruby "#release-2022-03-02-linux.platforms.ruby")

### Docker

| Platform Version and _Solution Stack Name_                                     | AMI          | Docker    | Docker Compose | Proxy Server |
| ------------------------------------------------------------------------------ | ------------ | --------- | -------------- | ------------ |
| **Docker AL2 version 3.4.12**<br>_64bit Amazon Linux 2 v3.4.12 running Docker_ | 2.0.20220207 | 20.10.7-5 | 1.29.2         | nginx 1.20.0 |

### Go

| Platform Version and _Solution Stack Name_                               | AMI          | Language  | AWS X-Ray | Proxy Server |
| ------------------------------------------------------------------------ | ------------ | --------- | --------- | ------------ |
| **Go 1 AL2 version 3.4.6**<br>_64bit Amazon Linux 2 v3.4.6 running Go 1_ | 2.0.20220207 | Go 1.17.7 | 3.2.0     | nginx 1.20.0 |

### Java SE

| Platform Version and _Solution Stack Name_                                           | AMI          | Language              | Tools                                 | AWS X-Ray | Proxy Server |
| ------------------------------------------------------------------------------------ | ------------ | --------------------- | ------------------------------------- | --------- | ------------ |
| **Corretto 11 version 3.2.12**<br>_64bit Amazon Linux 2 v3.2.12 running Corretto 11_ | 2.0.20220207 | Corretto 11.0.14.10.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.20.0 |
| **Corretto 8 version 3.2.12**<br>_64bit Amazon Linux 2 v3.2.12 running Corretto 8_   | 2.0.20220207 | Corretto 8.322.06.3   | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.20.0 |

### Tomcat

| Platform Version and _Solution Stack Name_                                                                          | AMI          | Language              | AWS X-Ray | Application Server | Proxy Server                          |
| ------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------- | --------- | ------------------ | ------------------------------------- |
| **Corretto 11 with Tomcat 8.5 AL2 version 4.2.12**<br>_64bit Amazon Linux 2 v4.2.12 running Tomcat 8.5 Corretto 11_ | 2.0.20220207 | Corretto 11.0.14.10.1 | 3.2.0     | Tomcat 8.5.72      | nginx 1.20.0 (default), Apache 2.4.52 |
| **Corretto 8 with Tomcat 8.5 AL2 version 4.2.12**<br>_64bit Amazon Linux 2 v4.2.12 running Tomcat 8.5 Corretto 8_   | 2.0.20220207 | Corretto 8.322.06.3   | 3.2.0     | Tomcat 8.5.72      | nginx 1.20.0 (default), Apache 2.4.52 |

### .NET Core on Linux

| Platform Version and _Solution Stack Name_                                              | Framework                                    | Proxy Server | AMI          | AWS X-Ray |
| --------------------------------------------------------------------------------------- | -------------------------------------------- | ------------ | ------------ | --------- |
| **.NET Core on AL2 version 2.2.11**<br>_64bit Amazon Linux 2 v2.2.11 running .NET Core_ | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30 | nginx 1.20.0 | 2.0.20220207 | 3.2.0     |

### Node.js

| Platform Version and _Solution Stack Name_                                           | AMI          | Node.js versions (npm versions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Proxy Server                          | Git    | AWS X-Ray |
| ------------------------------------------------------------------------------------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------ | --------- |
| **Node.js 16 AL2 version 5.5.0**<br>_64bit Amazon Linux 2 v5.5.0 running Node.js 16_ | 2.0.20220207 | 16.14.0 (8.3.1), 16.13.2 (8.1.2), 16.13.1 (8.1.2), 16.13.0 (8.1.0), 16.12.0 (8.1.0), 16.11.1 (8.0.0), 16.11.0 (8.0.0), 16.10.0 (7.24.0), 16.9.1 (7.21.1), 16.9.0 (7.21.1), 16.8.0 (7.21.0), 16.7.0 (7.20.3), 16.6.2 (7.20.3), 16.6.1 (7.20.3), 16.6.0 (7.19.1), 16.5.0 (7.19.1), 16.4.2 (7.18.1), 16.4.1 (7.18.1), 16.4.0 (7.18.1), 16.3.0 (7.15.1), 16.2.0 (7.13.0), 16.1.0 (7.11.2), 16.0.0 (7.10.0)<br>Default version: 16.14.0                                                                                                                                                                                                                                                                                         | nginx 1.20.0 (default), Apache 2.4.52 | 2.32.0 | 3.2.0     |
| **Node.js 14 AL2 version 5.5.0**<br>_64bit Amazon Linux 2 v5.5.0 running Node.js 14_ | 2.0.20220207 | 14.19.0 (6.14.16), 14.18.3 (6.14.15), 14.18.2 (6.14.15), 14.18.1 (6.14.15), 14.18.0 (6.14.15), 14.17.6 (6.14.15), 14.17.5 (6.14.14), 14.17.4 (6.14.14), 14.17.3 (6.14.13), 14.17.2 (6.14.13), 14.17.1 (6.14.13), 14.17.0 (6.14.13), 14.16.1 (6.14.12), 14.16.0 (6.14.11), 14.15.5 (6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8), 14.15.0 (6.14.8), 14.14.0 (6.14.8), 14.13.1 (6.14.8), 14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0 (6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7), 14.7.0 (6.14.7), 14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0 (6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br>Default version: 14.19.0 | nginx 1.20.0 (default), Apache 2.4.52 | 2.32.0 | 3.2.0     |

### PHP

| Platform Version and _Solution Stack Name_                                       | AMI          | Language   | Composer | Proxy Server                          |
| -------------------------------------------------------------------------------- | ------------ | ---------- | -------- | ------------------------------------- |
| **PHP 8.0 AL2 version 3.3.11**<br>_64bit Amazon Linux 2 v3.3.11 running PHP 8.0_ | 2.0.20220207 | PHP 8.0.13 | 2.0.13   | nginx 1.20.0 (default), Apache 2.4.52 |

### Python

| Platform Version and _Solution Stack Name_                                             | AMI          | Language      | Package Manager  | Packager | meld3 | AWS X-Ray | Proxy Server                          |
| -------------------------------------------------------------------------------------- | ------------ | ------------- | ---------------- | -------- | ----- | --------- | ------------------------------------- |
| **Python 3.8 AL2 version 3.3.11**<br>_64bit Amazon Linux 2 v3.3.11 running Python 3.8_ | 2.0.20220207 | Python 3.8.5  | pipenv 2021.11.9 |          |       | 3.2.0     | nginx 1.20.0 (default), Apache 2.4.52 |
| **Python 3.7 AL2 version 3.3.11**<br>_64bit Amazon Linux 2 v3.3.11 running Python 3.7_ | 2.0.20220207 | Python 3.7.10 | pipenv 2021.11.9 |          |       | 3.2.0     | nginx 1.20.0 (default), Apache 2.4.52 |

### Ruby

| Platform Version and _Solution Stack Name_                                       | AMI          | Language        | Package Manager | Application Server | AWS X-Ray | Proxy Server |
| -------------------------------------------------------------------------------- | ------------ | --------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 3.0 AL2 version 3.4.3**<br>_64bit Amazon Linux 2 v3.4.3 running Ruby 3.0_ | 2.0.20220207 | Ruby 3.0.3-p157 | RubyGems 3.3.7  | Puma 5.6.2         | 3.2.0     | nginx 1.20.0 |
| **Ruby 2.7 AL2 version 3.4.3**<br>_64bit Amazon Linux 2 v3.4.3 running Ruby 2.7_ | 2.0.20220207 | Ruby 2.7.5-p203 | RubyGems 3.3.7  | Puma 5.6.2         | 3.2.0     | nginx 1.20.0 |
