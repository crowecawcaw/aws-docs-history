# Release: Elastic Beanstalk Amazon Linux 2 platform updates on September 2, 2021

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux 2. The release includes security updates.
It also includes Docker, Go, Tomcat, .NET Core, Node.js, and Ruby updates.

**Release date:** September 2, 2021

## Changes

The following table lists the changes included in this release.

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------- | ---- | ------- | ------- | ---- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2.html "https://alas.aws.amazon.com/alas2.html") on or before **August 16, 2021\*<br>• to all released Amazon Linux 2 platforms.<br>The **.NET Core*<br>• and **Node.js**<br>releases are security releases. For more information, see<br>\*\*Platform-specific updates*<br>• in this table. |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                                                                                                                 | \*_Platform_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Docker_<br>• | Updated Docker to version [20.10.7](https://docs.docker.com/engine/release-notes/#20107 "https://docs.docker.com/engine/release-notes/#20107"). | <br> | \*_Go_<br>• | Updated Go to release **1.17**. For details, see [go1.17](https://golang.org/doc/devel/release.html#go1.17 "https://golang.org/doc/devel/release.html#go1.17") in _The Go Programming Language Release<br>History_. | <br> | \*_Tomcat_<br>• | Updated Tomcat 8.5 to [Tomcat<br>8.5.69](<https://tomcat.apache.org/tomcat-8.5-doc/changelog.html#Tomcat_8.5.69_(schultz)> "https://tomcat.apache.org/tomcat-8.5-doc/changelog.html#Tomcat_8.5.69_(schultz)"). | <br> | \*_.NET Core_<br>• | Updated .NET Core to releases<br>[5.0.9](https://github.com/dotnet/core/blob/master/release-notes/5.0/5.0.9/5.0.9.md "https://github.com/dotnet/core/blob/master/release-notes/5.0/5.0.9/5.0.9.md").<br>[3.1.18](https://github.com/dotnet/core/blob/master/release-notes/3.1/3.1.18/3.1.18.md "https://github.com/dotnet/core/blob/master/release-notes/3.1/3.1.18/3.1.18.md"), and<br>[2.1.30](https://github.com/dotnet/core/blob/master/release-notes/2.1/2.1.30/2.1.30.md "https://github.com/dotnet/core/blob/master/release-notes/2.1/2.1.30/2.1.30.md").<br>These are security releases. | <br> | \*_Node.js_<br>• | Updated Node.js 14 to add support for Node versions<br>[14.17.5](https://nodejs.org/en/blog/release/v14.17.5/ "https://nodejs.org/en/blog/release/v14.17.5/") and<br>[14.17.4](https://nodejs.org/en/blog/release/v14.17.4/ "https://nodejs.org/en/blog/release/v14.17.4/").<br>Updated Node.js 12 to add support for Node versions<br>[12.22.5](https://nodejs.org/en/blog/release/v12.22.5/ "https://nodejs.org/en/blog/release/v12.22.5/") and<br>[12.22.4](https://nodejs.org/en/blog/release/v12.22.4/ "https://nodejs.org/en/blog/release/v12.22.4/").<br>The new Node.js versions are security releases. | <br> | \*_Ruby_<br>• | Updated RubyGems to release [3.2.25](https://blog.rubygems.org/2021/07/30/3.2.25-released.html "https://blog.rubygems.org/2021/07/30/3.2.25-released.html").<br>Updated Puma to version [5.4.0](https://github.com/puma/puma/releases/tag/v5.4.0 "https://github.com/puma/puma/releases/tag/v5.4.0"). |     |

## New platform versions

###### These platforms are updated:

- [Docker](#release-2021-09-02-linux.platforms.docker "#release-2021-09-02-linux.platforms.docker")
- [Go](#release-2021-09-02-linux.platforms.go "#release-2021-09-02-linux.platforms.go")
- [Java SE](#release-2021-09-02-linux.platforms.javase "#release-2021-09-02-linux.platforms.javase")
- [Tomcat](#release-2021-09-02-linux.platforms.java "#release-2021-09-02-linux.platforms.java")
- [.NET Core on Linux](#release-2021-09-02-linux.platforms.dotnetlinux "#release-2021-09-02-linux.platforms.dotnetlinux")
- [Node.js](#release-2021-09-02-linux.platforms.nodejs "#release-2021-09-02-linux.platforms.nodejs")
- [PHP](#release-2021-09-02-linux.platforms.PHP "#release-2021-09-02-linux.platforms.PHP")
- [Python](#release-2021-09-02-linux.platforms.python "#release-2021-09-02-linux.platforms.python")
- [Ruby](#release-2021-09-02-linux.platforms.ruby "#release-2021-09-02-linux.platforms.ruby")

### Docker

| Platform Version and _Solution Stack Name_                                   | AMI          | Docker  | Docker Compose | Proxy Server |
| ---------------------------------------------------------------------------- | ------------ | ------- | -------------- | ------------ |
| **Docker AL2 version 3.4.5**<br>_64bit Amazon Linux 2 v3.4.5 running Docker_ | 2.0.20210721 | 20.10.7 | 1.29.2         | nginx 1.20.0 |

### Go

| Platform Version and _Solution Stack Name_                               | AMI          | Language | AWS X-Ray | Proxy Server |
| ------------------------------------------------------------------------ | ------------ | -------- | --------- | ------------ |
| **Go 1 AL2 version 3.4.0**<br>_64bit Amazon Linux 2 v3.4.0 running Go 1_ | 2.0.20210721 | Go 1.17  | 3.2.0     | nginx 1.20.0 |

### Java SE

| Platform Version and _Solution Stack Name_                                         | AMI          | Language             | Tools                                 | AWS X-Ray | Proxy Server |
| ---------------------------------------------------------------------------------- | ------------ | -------------------- | ------------------------------------- | --------- | ------------ |
| **Corretto 11 version 3.2.5**<br>_64bit Amazon Linux 2 v3.2.5 running Corretto 11_ | 2.0.20210721 | Corretto 11.0.12.7.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.20.0 |
| **Corretto 8 version 3.2.5**<br>_64bit Amazon Linux 2 v3.2.5 running Corretto 8_   | 2.0.20210721 | Corretto 8.302.08.1  | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.20.0 |

### Tomcat

| Platform Version and _Solution Stack Name_                                                                        | AMI          | Language             | AWS X-Ray | Application Server | Proxy Server                          |
| ----------------------------------------------------------------------------------------------------------------- | ------------ | -------------------- | --------- | ------------------ | ------------------------------------- |
| **Corretto 11 with Tomcat 8.5 AL2 version 4.2.5**<br>_64bit Amazon Linux 2 v4.2.5 running Tomcat 8.5 Corretto 11_ | 2.0.20210721 | Corretto 11.0.12.7.1 | 3.2.0     | Tomcat 8.5.69      | nginx 1.20.0 (default), Apache 2.4.48 |
| **Corretto 8 with Tomcat 8.5 AL2 version 4.2.5**<br>_64bit Amazon Linux 2 v4.2.5 running Tomcat 8.5 Corretto 8_   | 2.0.20210721 | Corretto 8.302.08.1  | 3.2.0     | Tomcat 8.5.69      | nginx 1.20.0 (default), Apache 2.4.48 |

### .NET Core on Linux

| Platform Version and _Solution Stack Name_                                            | Framework                                  | Proxy Server | AMI          | AWS X-Ray |
| ------------------------------------------------------------------------------------- | ------------------------------------------ | ------------ | ------------ | --------- |
| **.NET Core on AL2 version 2.2.5**<br>_64bit Amazon Linux 2 v2.2.5 running .NET Core_ | .NET 5.0.9, supports 5.0.9, 3.1.18, 2.1.30 | nginx 1.20.0 | 2.0.20210721 | 3.2.0     |

### Node.js

| Platform Version and _Solution Stack Name_                                           | AMI          | Node.js versions (npm versions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Proxy Server                          | Git    | AWS X-Ray |
| ------------------------------------------------------------------------------------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------ | --------- |
| **Node.js 14 AL2 version 5.4.5**<br>_64bit Amazon Linux 2 v5.4.5 running Node.js 14_ | 2.0.20210721 | 14.17.5 (6.14.14), 14.17.4 (6.14.14), 14.17.3 (6.14.13), 14.17.2 (6.14.13), 14.17.1 (6.14.13), 14.17.0 (6.14.13), 14.16.1 (6.14.12), 14.16.0 (6.14.11), 14.15.5 (6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8), 14.15.0 (6.14.8), 14.14.0 (6.14.8), 14.13.1 (6.14.8), 14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0 (6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7), 14.7.0 (6.14.7), 14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0 (6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br>Default version: 14.17.5                                                                                                                                                                                                                               | nginx 1.20.0 (default), Apache 2.4.48 | 2.32.0 | 3.2.0     |
| **Node.js 12 AL2 version 5.4.5**<br>_64bit Amazon Linux 2 v5.4.5 running Node.js 12_ | 2.0.20210721 | 12.22.5 (6.14.14), 12.22.4 (6.14.14), 12.22.3 (6.14.13), 12.22.2 (6.14.13), 12.22.1 (6.14.12), 12.22.0 (6.14.11), 12.21.0 (6.14.11), 12.20.2 (6.14.11), 12.20.1 (6.14.10), 12.20.0 (6.14.8), 12.19.1 (6.14.8), 12.19.0 (6.14.8), 12.18.4 (6.14.6), 12.18.3 (6.14.6), 12.18.2 (6.14.5), 12.18.1 (6.14.5), 12.18.0 (6.14.4), 12.17.0 (6.14.4), 12.16.3 (6.14.4), 12.16.2 (6.14.4), 12.16.1 (6.13.4), 12.16.0 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 12.13.1 (6.12.1), 12.13.0 (6.12.0), 12.12.0 (6.11.3), 12.11.1 (6.11.3), 12.11.0 (6.11.3), 12.10.0 (6.10.3), 12.9.1 (6.10.2), 12.9.0 (6.10.2), 12.8.1 (6.10.2), 12.8.0 (6.10.2), 12.7.0 (6.10.0), 12.6.0 (6.9.0), 12.5.0 (6.9.0), 12.4.0 (6.9.0), 12.3.1 (6.9.0), 12.3.0 (6.9.0), 12.2.0 (6.9.0), 12.1.0 (6.9.0), 12.0.0 (6.9.0)<br>Default version: 12.22.5 | nginx 1.20.0 (default), Apache 2.4.48 | 2.32.0 | 3.2.0     |

### PHP

| Platform Version and _Solution Stack Name_                                     | AMI          | Language   | Composer | Proxy Server                          |
| ------------------------------------------------------------------------------ | ------------ | ---------- | -------- | ------------------------------------- |
| **PHP 8.0 AL2 version 3.3.5**<br>_64bit Amazon Linux 2 v3.3.5 running PHP 8.0_ | 2.0.20210721 | PHP 8.0.8  | 2.0.13   | nginx 1.20.0 (default), Apache 2.4.48 |
| **PHP 7.4 AL2 version 3.3.5**<br>_64bit Amazon Linux 2 v3.3.5 running PHP 7.4_ | 2.0.20210721 | PHP 7.4.21 | 1.10.22  | nginx 1.20.0 (default), Apache 2.4.48 |

### Python

| Platform Version and _Solution Stack Name_                                           | AMI          | Language      | Package Manager  | Packager | meld3 | AWS X-Ray | Proxy Server                          |
| ------------------------------------------------------------------------------------ | ------------ | ------------- | ---------------- | -------- | ----- | --------- | ------------------------------------- |
| **Python 3.8 AL2 version 3.3.5**<br>_64bit Amazon Linux 2 v3.3.5 running Python 3.8_ | 2.0.20210721 | Python 3.8.5  | pipenv 2020.8.13 |          |       | 3.2.0     | nginx 1.20.0 (default), Apache 2.4.48 |
| **Python 3.7 AL2 version 3.3.5**<br>_64bit Amazon Linux 2 v3.3.5 running Python 3.7_ | 2.0.20210721 | Python 3.7.10 | pipenv 2020.8.13 |          |       | 3.2.0     | nginx 1.20.0 (default), Apache 2.4.48 |

### Ruby

| Platform Version and _Solution Stack Name_                                       | AMI          | Language        | Package Manager | Application Server | AWS X-Ray | Proxy Server |
| -------------------------------------------------------------------------------- | ------------ | --------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 2.7 AL2 version 3.3.5**<br>_64bit Amazon Linux 2 v3.3.5 running Ruby 2.7_ | 2.0.20210721 | Ruby 2.7.4-p191 | RubyGems 3.2.25 | Puma 5.4.0         | 3.2.0     | nginx 1.20.0 |
| **Ruby 2.6 AL2 version 3.3.5**<br>_64bit Amazon Linux 2 v3.3.5 running Ruby 2.6_ | 2.0.20210721 | Ruby 2.6.8-p205 | RubyGems 3.2.25 | Puma 5.4.0         | 3.2.0     | nginx 1.20.0 |
