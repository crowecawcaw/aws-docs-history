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
[AL1 platform retirement FAQ](../dg/using-features.migration-al.FAQ.md "../dg/using-features.migration-al.FAQ.md") in the _AWS Elastic Beanstalk Developer Guide_.

The following sections provide information about all retiring platform versions.

###### Topics

- [Docker](#platforms-retiring.docker "#platforms-retiring.docker")
- [Go](#platforms-retiring.go "#platforms-retiring.go")
- [Java SE](#platforms-retiring.javase "#platforms-retiring.javase")
- [Tomcat](#platforms-retiring.java "#platforms-retiring.java")
- [.NET Core on Linux](#platforms-retiring.dotnetlinux "#platforms-retiring.dotnetlinux")
- [.NET on Windows Server](#platforms-retiring.net "#platforms-retiring.net")
- [Node.js](#platforms-retiring.nodejs "#platforms-retiring.nodejs")
- [PHP](#platforms-retiring.PHP "#platforms-retiring.PHP")
- [Python](#platforms-retiring.python "#platforms-retiring.python")
- [Ruby](#platforms-retiring.ruby "#platforms-retiring.ruby")

## Docker

Elastic Beanstalk has scheduled the following Docker platform versions for retirement.

| Platform Version and _Solution Stack Name_                                   | AMI          | ECS Agent | Docker  | Docker Compose | Proxy Server | End Date   |
| ---------------------------------------------------------------------------- | ------------ | --------- | ------- | -------------- | ------------ | ---------- |
| **Docker AL2 version 4.9.5**<br>_64bit Amazon Linux 2 v4.9.5 running Docker_ | 2.0.20260727 |           | 25.0.16 | 5.3.1          | nginx 1.30.3 | 2026-06-30 |
| **ECS AL2 version 3.10.5**<br>_64bit Amazon Linux 2 v3.10.5 running ECS_     | 2.0.20260727 | 1.105.1   | 25.0.16 |                |              | 2026-06-30 |

For information about current platform versions, see [Docker](platforms-supported.md#platforms-supported.docker "platforms-supported.md#platforms-supported.docker").

## Go

Elastic Beanstalk has scheduled the following Go platform versions for retirement.

| Platform Version and _Solution Stack Name_                                 | AMI          | Language  | AWS X-Ray | Proxy Server | End Date   |
| -------------------------------------------------------------------------- | ------------ | --------- | --------- | ------------ | ---------- |
| **Go 1 AL2 version 3.19.5**<br>_64bit Amazon Linux 2 v3.19.5 running Go 1_ | 2.0.20260727 | Go 1.26.5 | 3.6.5     | nginx 1.30.3 | 2026-06-30 |

For information about current platform versions, see [Go](platforms-supported.md#platforms-supported.go "platforms-supported.md#platforms-supported.go").

## Java SE

Elastic Beanstalk has scheduled the following Java SE platform versions for retirement.

| Platform Version and _Solution Stack Name_                                           | AMI          | Language              | Tools                                    | AWS X-Ray | Proxy Server | End Date   |
| ------------------------------------------------------------------------------------ | ------------ | --------------------- | ---------------------------------------- | --------- | ------------ | ---------- |
| **Corretto 17 version 3.14.5**<br>_64bit Amazon Linux 2 v3.14.5 running Corretto 17_ | 2.0.20260727 | Corretto 17.0.19.10.1 | Ant 1.10.17, Gradle 8.14.5, Maven 3.9.16 | 3.6.5     | nginx 1.30.3 | 2026-06-30 |
| **Corretto 11 version 3.14.5**<br>_64bit Amazon Linux 2 v3.14.5 running Corretto 11_ | 2.0.20260727 | Corretto 11.0.31.11.1 | Ant 1.10.17, Gradle 8.14.5, Maven 3.9.16 | 3.6.5     | nginx 1.30.3 | 2026-06-30 |
| **Corretto 8 version 3.14.5**<br>_64bit Amazon Linux 2 v3.14.5 running Corretto 8_   | 2.0.20260727 | Corretto 8.492.09.1   | Ant 1.10.17, Gradle 8.14.5, Maven 3.9.16 | 3.6.5     | nginx 1.30.3 | 2026-06-30 |

For information about current platform versions, see [Java SE](platforms-supported.md#platforms-supported.javase "platforms-supported.md#platforms-supported.javase").

## Tomcat

Elastic Beanstalk has scheduled the following Tomcat platform versions for retirement.

| Platform Version and _Solution Stack Name_                                                                      | AMI          | Language              | AWS X-Ray | Application Server | Proxy Server                          | End Date   |
| --------------------------------------------------------------------------------------------------------------- | ------------ | --------------------- | --------- | ------------------ | ------------------------------------- | ---------- |
| **Corretto 11 with Tomcat 9 AL2 version 4.14.5**<br>_64bit Amazon Linux 2 v4.14.5 running Tomcat 9 Corretto 11_ | 2.0.20260727 | Corretto 11.0.31.11.1 | 3.6.5     | Tomcat 9.0.120     | nginx 1.30.3 (default), Apache 2.4.68 | 2026-06-30 |
| **Corretto 8 with Tomcat 9 AL2 version 4.14.5**<br>_64bit Amazon Linux 2 v4.14.5 running Tomcat 9 Corretto 8_   | 2.0.20260727 | Corretto 8.492.09.1   | 3.6.5     | Tomcat 9.0.120     | nginx 1.30.3 (default), Apache 2.4.68 | 2026-06-30 |

For information about current platform versions, see [Tomcat](platforms-supported.md#platforms-supported.java "platforms-supported.md#platforms-supported.java").

## .NET Core on Linux

Elastic Beanstalk has scheduled the following .NET Core on Linux platform versions for retirement.

| Platform Version and _Solution Stack Name_                                              | Framework                    | Proxy Server | AMI              | AWS X-Ray | End Date   |
| --------------------------------------------------------------------------------------- | ---------------------------- | ------------ | ---------------- | --------- | ---------- |
| **.NET 9 on AL2023 version 3.11.5**<br>_64bit Amazon Linux 2023 v3.11.5 running .NET 9_ | .NET 9.0.18, supports 9.0.18 | nginx 1.30.3 | 2023.12.20260727 | 3.6.5     | 2027-03-31 |
| **.NET 8 on AL2023 version 3.11.5**<br>_64bit Amazon Linux 2023 v3.11.5 running .NET 8_ | .NET 8.0.29, supports 8.0.29 | nginx 1.30.3 | 2023.12.20260727 | 3.6.5     | 2027-03-31 |
| **.NET Core on AL2 version 2.16.5**<br>_64bit Amazon Linux 2 v2.16.5 running .NET Core_ | .NET 8.0.29, supports 8.0.29 | nginx 1.30.3 | 2.0.20260727     | 3.6.5     | 2026-06-30 |

For information about current platform versions, see [.NET Core on Linux](platforms-supported.md#platforms-supported.dotnetlinux "platforms-supported.md#platforms-supported.dotnetlinux").

## .NET on Windows Server

###### Note

Elastic Beanstalk platform branches based on _Windows Server 2016_ and _Windows Server Core 2016_ will retire on
**September 30, 2026**. Additionally, all Amazon Machine Images (AMIs) for these platform branches will become
inaccessible on **January 15, 2027**. This is to ensure that customer Elastic Beanstalk environments are aligned with the most
current support offered by AWS.

Starting on September 30, 2026, retired platform branches will no longer be available for new environments on Elastic Beanstalk. While you can continue
to operate existing environments running on retired platform branches, these branches will no longer receive security updates, platform updates,
or bug fixes from Elastic Beanstalk, creating significant security and operational risks. After January 15, 2027, the default AMIs associated with these
platform branches will be inaccessible, and any activity that attempts to launch new EC2 instances based on these AMIs will fail, including
auto-scaling, instance replacement, and application or configuration deployments that launch new instances.

We strongly recommend that you start planning your migration to a current and fully supported Windows Server platform, such as
_Windows Server 2025 with IIS 10.0_, _Windows Server 2022 with IIS 10.0_, or
_Windows Server 2019 with IIS 10.0_. For a list of currently supported platforms see
[Elastic Beanstalk supported platforms](platforms-supported.md "platforms-supported.md").

If you cannot migrate to a fully supported platform, you can use a custom AMI with Windows Server 2016 as the base image. For detailed
instructions, see [Preserving access to an AMI for a retired platform](../dg/using-features.customenv-env-copy.md "../dg/using-features.customenv-env-copy.md") in the
_AWS Elastic Beanstalk Developer Guide_. If you need temporary access to an AMI while you perform a migration, contact AWS Support.

Elastic Beanstalk has scheduled the following .NET on Windows Server platform versions for retirement.

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                               | Proxy Server | End Date   |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------ | ---------- |
| **Windows Server 2016 with IIS 10.0 version 2.23.3**      | _64bit Windows Server 2016 v2.23.3 running IIS 10.0_      | .NET 10.0.10, supports 10.0.10, 9.0.18, 8.0.29<br>.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0     | 2026-09-30 |
| **Windows Server Core 2016 with IIS 10.0 version 2.23.3** | _64bit Windows Server Core 2016 v2.23.3 running IIS 10.0_ | .NET 10.0.10, supports 10.0.10, 9.0.18, 8.0.29<br>.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0     | 2026-09-30 |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Launch | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.23.3**      | 2026.07.15  | 3.7.1252.1       | 2.5.1     | 3.3.4793.0 | 4.0        | 3.6.6     |
| **Windows Server Core 2016 with IIS 10.0 version 2.23.3** | 2026.07.15  | 3.7.1252.1       | 2.5.1     | 3.3.4793.0 | 4.0        | 3.6.6     |

For information about current platform versions, see [.NET on Windows Server](platforms-supported.md#platforms-supported.net "platforms-supported.md#platforms-supported.net").

## Node.js

Elastic Beanstalk has scheduled the following Node.js platform versions for retirement.

| Platform Version and _Solution Stack Name_                                                   | AMI              | Node.js versions (npm versions)              | Proxy Server                          | Git    | AWS X-Ray | End Date   |
| -------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------- | ------------------------------------- | ------ | --------- | ---------- |
| **Node.js 20 AL2023 version 6.11.5**<br>_64bit Amazon Linux 2023 v6.11.5 running Node.js 20_ | 2023.12.20260727 | 20.20.2 (10.8.2)<br>Default version: 20.20.2 | nginx 1.30.3 (default), Apache 2.4.68 | 2.50.1 | 3.6.5     | 2026-07-31 |

For information about current platform versions, see [Node.js](platforms-supported.md#platforms-supported.nodejs "platforms-supported.md#platforms-supported.nodejs").

## PHP

Elastic Beanstalk has scheduled the following PHP platform versions for retirement.

| Platform Version and _Solution Stack Name_                                             | AMI              | Language   | Package Manager            | Proxy Server                          | End Date   |
| -------------------------------------------------------------------------------------- | ---------------- | ---------- | -------------------------- | ------------------------------------- | ---------- |
| **PHP 8.2 AL2023 version 4.13.5**<br>_64bit Amazon Linux 2023 v4.13.5 running PHP 8.2_ | 2023.12.20260727 | PHP 8.2.32 | Composer 2.10.2, PIE 1.4.9 | nginx 1.30.3 (default), Apache 2.4.68 | 2027-03-31 |

For information about current platform versions, see [PHP](platforms-supported.md#platforms-supported.PHP "platforms-supported.md#platforms-supported.PHP").

## Python

Elastic Beanstalk has scheduled the following Python platform versions for retirement.

| Platform Version and _Solution Stack Name_                                                   | AMI              | Language      | Package Manager             | AWS X-Ray | Proxy Server                          | End Date   |
| -------------------------------------------------------------------------------------------- | ---------------- | ------------- | --------------------------- | --------- | ------------------------------------- | ---------- |
| **Python 3.9 AL2023 version 4.13.5**<br>_64bit Amazon Linux 2023 v4.13.5 running Python 3.9_ | 2023.12.20260727 | Python 3.9.25 | pip 26.0.1, pipenv 2025.0.4 | 3.6.5     | nginx 1.30.3 (default), Apache 2.4.68 | 2026-07-31 |

For information about current platform versions, see [Python](platforms-supported.md#platforms-supported.python "platforms-supported.md#platforms-supported.python").

## Ruby

Elastic Beanstalk has scheduled the following Ruby platform versions for retirement.

| Platform Version and _Solution Stack Name_                                               | AMI              | Language   | Package Manager | Application Server | AWS X-Ray | Proxy Server | End Date   |
| ---------------------------------------------------------------------------------------- | ---------------- | ---------- | --------------- | ------------------ | --------- | ------------ | ---------- |
| **Ruby 3.2 AL2023 version 4.14.5**<br>_64bit Amazon Linux 2023 v4.14.5 running Ruby 3.2_ | 2023.12.20260727 | Ruby 3.2.8 | RubyGems 3.4.19 | Puma 8.0.2         | 3.6.5     | nginx 1.30.3 | 2026-07-31 |

For information about current platform versions, see [Ruby](platforms-supported.md#platforms-supported.ruby "platforms-supported.md#platforms-supported.ruby").
