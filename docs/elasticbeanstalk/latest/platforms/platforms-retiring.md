# Elastic Beanstalk platform versions scheduled for retirement

AWS Elastic Beanstalk provides managed platforms that support running web applications developed for specific programming languages, frameworks, and web
containers. Elastic Beanstalk offers one or more platform versions for each platform. For details about currently supported platform versions, see [Elastic Beanstalk supported platforms](platforms-supported.md "platforms-supported.md").

This page lists platform versions that Elastic Beanstalk has scheduled for retirement, because some of their components are reaching their End of Life (EOL). These
platform versions remain available until the published retirement date of their retiring components. For a list of component retirement dates, see
[AWS Elastic Beanstalk platform schedules](../dg/platforms-schedule.md "../dg/platforms-schedule.md") in the _AWS Elastic Beanstalk Developer Guide_.

###### Note

On [July 18, 2022](../relnotes/release-2022-07-18-linux-al1-retire.md "../relnotes/release-2022-07-18-linux-al1-retire.md") Elastic Beanstalk set the
status of all platform branches based on Amazon Linux AMI (AL1) to **retired**.
For more information, see
[AL1 platform retirement FAQ](../dg/using-features.migration-al.md "../dg/using-features.migration-al.md") in the _AWS Elastic Beanstalk Developer Guide_.

The following sections provide information about all retiring platform versions.

###### Topics

- [Docker](#platforms-retiring.docker "#platforms-retiring.docker")
- [Go](#platforms-retiring.go "#platforms-retiring.go")
- [Java SE](#platforms-retiring.javase "#platforms-retiring.javase")
- [Tomcat](#platforms-retiring.java "#platforms-retiring.java")
- [.NET Core on Linux](#platforms-retiring.dotnetlinux "#platforms-retiring.dotnetlinux")
- [Node.js](#platforms-retiring.nodejs "#platforms-retiring.nodejs")
- [PHP](#platforms-retiring.PHP "#platforms-retiring.PHP")
- [Python](#platforms-retiring.python "#platforms-retiring.python")
- [Ruby](#platforms-retiring.ruby "#platforms-retiring.ruby")

## Docker

Elastic Beanstalk has scheduled the following Docker platform versions for retirement.

| Platform Version and _Solution Stack Name_                                   | AMI          | ECS Agent | Docker  | Docker Compose | Proxy Server | End Date   |
| ---------------------------------------------------------------------------- | ------------ | --------- | ------- | -------------- | ------------ | ---------- |
| **Docker AL2 version 4.5.3**<br>_64bit Amazon Linux 2 v4.5.3 running Docker_ | 2.0.20260202 |           | 25.0.14 | 5.0.2          | nginx 1.28.1 | 2026-06-30 |
| **ECS AL2 version 3.6.4**<br>_64bit Amazon Linux 2 v3.6.4 running ECS_       | 2.0.20260202 | 1.101.2   | 25.0.14 |                |              | 2026-06-30 |

For information about current platform versions, see [Docker](platforms-supported.md#platforms-supported.docker "platforms-supported.md#platforms-supported.docker").

## Go

Elastic Beanstalk has scheduled the following Go platform versions for retirement.

| Platform Version and _Solution Stack Name_                                 | AMI          | Language  | AWS X-Ray | Proxy Server | End Date   |
| -------------------------------------------------------------------------- | ------------ | --------- | --------- | ------------ | ---------- |
| **Go 1 AL2 version 3.15.0**<br>_64bit Amazon Linux 2 v3.15.0 running Go 1_ | 2.0.20260202 | Go 1.26.0 | 3.6.1     | nginx 1.28.1 | 2026-06-30 |

For information about current platform versions, see [Go](platforms-supported.md#platforms-supported.go "platforms-supported.md#platforms-supported.go").

## Java SE

Elastic Beanstalk has scheduled the following Java SE platform versions for retirement.

| Platform Version and _Solution Stack Name_                                           | AMI          | Language             | Tools                                    | AWS X-Ray | Proxy Server | End Date   |
| ------------------------------------------------------------------------------------ | ------------ | -------------------- | ---------------------------------------- | --------- | ------------ | ---------- |
| **Corretto 17 version 3.10.4**<br>_64bit Amazon Linux 2 v3.10.4 running Corretto 17_ | 2.0.20260202 | Corretto 17.0.18.9.1 | Ant 1.10.15, Gradle 8.14.4, Maven 3.9.12 | 3.6.1     | nginx 1.28.1 | 2026-06-30 |
| **Corretto 11 version 3.10.4**<br>_64bit Amazon Linux 2 v3.10.4 running Corretto 11_ | 2.0.20260202 | Corretto 11.0.30.7.1 | Ant 1.10.15, Gradle 8.14.4, Maven 3.9.12 | 3.6.1     | nginx 1.28.1 | 2026-06-30 |
| **Corretto 8 version 3.10.4**<br>_64bit Amazon Linux 2 v3.10.4 running Corretto 8_   | 2.0.20260202 | Corretto 8.482.08.1  | Ant 1.10.15, Gradle 8.14.4, Maven 3.9.12 | 3.6.1     | nginx 1.28.1 | 2026-06-30 |

For information about current platform versions, see [Java SE](platforms-supported.md#platforms-supported.javase "platforms-supported.md#platforms-supported.javase").

## Tomcat

Elastic Beanstalk has scheduled the following Tomcat platform versions for retirement.

| Platform Version and _Solution Stack Name_                                                                      | AMI          | Language             | AWS X-Ray | Application Server | Proxy Server                          | End Date   |
| --------------------------------------------------------------------------------------------------------------- | ------------ | -------------------- | --------- | ------------------ | ------------------------------------- | ---------- |
| **Corretto 11 with Tomcat 9 AL2 version 4.10.4**<br>_64bit Amazon Linux 2 v4.10.4 running Tomcat 9 Corretto 11_ | 2.0.20260202 | Corretto 11.0.30.7.1 | 3.6.1     | Tomcat 9.0.110     | nginx 1.28.1 (default), Apache 2.4.66 | 2026-06-30 |
| **Corretto 8 with Tomcat 9 AL2 version 4.10.4**<br>_64bit Amazon Linux 2 v4.10.4 running Tomcat 9 Corretto 8_   | 2.0.20260202 | Corretto 8.482.08.1  | 3.6.1     | Tomcat 9.0.110     | nginx 1.28.1 (default), Apache 2.4.66 | 2026-06-30 |

For information about current platform versions, see [Tomcat](platforms-supported.md#platforms-supported.java "platforms-supported.md#platforms-supported.java").

## .NET Core on Linux

Elastic Beanstalk has scheduled the following .NET Core on Linux platform versions for retirement.

| Platform Version and _Solution Stack Name_                                              | Framework                    | Proxy Server | AMI          | AWS X-Ray | End Date   |
| --------------------------------------------------------------------------------------- | ---------------------------- | ------------ | ------------ | --------- | ---------- |
| **.NET Core on AL2 version 2.12.4**<br>_64bit Amazon Linux 2 v2.12.4 running .NET Core_ | .NET 8.0.24, supports 8.0.24 | nginx 1.28.1 | 2.0.20260202 | 3.6.1     | 2026-06-30 |

For information about current platform versions, see [.NET Core on Linux](platforms-supported.md#platforms-supported.dotnetlinux "platforms-supported.md#platforms-supported.dotnetlinux").

## Node.js

Elastic Beanstalk has scheduled the following Node.js platform versions for retirement.

| Platform Version and _Solution Stack Name_                                                 | AMI              | Node.js versions (npm versions)              | Proxy Server                          | Git    | AWS X-Ray | End Date   |
| ------------------------------------------------------------------------------------------ | ---------------- | -------------------------------------------- | ------------------------------------- | ------ | --------- | ---------- |
| **Node.js 20 AL2023 version 6.7.4**<br>_64bit Amazon Linux 2023 v6.7.4 running Node.js 20_ | 2023.10.20260202 | 20.20.0 (10.8.2)<br>Default version: 20.20.0 | nginx 1.28.1 (default), Apache 2.4.66 | 2.50.1 | 3.6.1     | 2026-07-31 |

For information about current platform versions, see [Node.js](platforms-supported.md#platforms-supported.nodejs "platforms-supported.md#platforms-supported.nodejs").

## PHP

Elastic Beanstalk has scheduled the following PHP platform versions for retirement.

| Platform Version and _Solution Stack Name_                                           | AMI              | Language   | Composer | Proxy Server                          | End Date   |
| ------------------------------------------------------------------------------------ | ---------------- | ---------- | -------- | ------------------------------------- | ---------- |
| **PHP 8.1 AL2023 version 4.9.3**<br>_64bit Amazon Linux 2023 v4.9.3 running PHP 8.1_ | 2023.10.20260202 | PHP 8.1.34 | 2.9.5    | nginx 1.28.1 (default), Apache 2.4.66 | 2026-03-31 |
| **PHP 8.1 AL2 version 3.12.3**<br>_64bit Amazon Linux 2 v3.12.3 running PHP 8.1_     | 2.0.20260202     | PHP 8.1.33 | 2.9.5    | nginx 1.28.1 (default), Apache 2.4.66 | 2026-03-31 |

For information about current platform versions, see [PHP](platforms-supported.md#platforms-supported.PHP "platforms-supported.md#platforms-supported.PHP").

## Python

Elastic Beanstalk has scheduled the following Python platform versions for retirement.

| Platform Version and _Solution Stack Name_                                                 | AMI              | Language      | Package Manager             | AWS X-Ray | Proxy Server                          | End Date   |
| ------------------------------------------------------------------------------------------ | ---------------- | ------------- | --------------------------- | --------- | ------------------------------------- | ---------- |
| **Python 3.9 AL2023 version 4.9.3**<br>_64bit Amazon Linux 2023 v4.9.3 running Python 3.9_ | 2023.10.20260202 | Python 3.9.25 | pip 26.0.1, pipenv 2025.0.4 | 3.6.1     | nginx 1.28.1 (default), Apache 2.4.66 | 2026-07-31 |

For information about current platform versions, see [Python](platforms-supported.md#platforms-supported.python "platforms-supported.md#platforms-supported.python").

## Ruby

Elastic Beanstalk has scheduled the following Ruby platform versions for retirement.

| Platform Version and _Solution Stack Name_                                             | AMI              | Language   | Package Manager | Application Server | AWS X-Ray | Proxy Server | End Date   |
| -------------------------------------------------------------------------------------- | ---------------- | ---------- | --------------- | ------------------ | --------- | ------------ | ---------- |
| **Ruby 3.2 AL2023 version 4.9.0**<br>_64bit Amazon Linux 2023 v4.9.0 running Ruby 3.2_ | 2023.10.20260202 | Ruby 3.2.8 | RubyGems 3.4.19 | Puma 7.2.0         | 3.6.1     | nginx 1.28.1 | 2026-07-31 |

For information about current platform versions, see [Ruby](platforms-supported.md#platforms-supported.ruby "platforms-supported.md#platforms-supported.ruby").
