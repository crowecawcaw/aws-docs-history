# Elastic Beanstalk supported platforms

AWS Elastic Beanstalk provides managed platforms that support running web applications developed for specific programming languages, frameworks, and web
containers. Elastic Beanstalk offers one or more platform versions for each platform. When you create an environment and choose a platform, Elastic Beanstalk provisions the resources
that your application needs, including one or more Amazon Elastic Compute Cloud (Amazon EC2) instances. The software stack running on the Amazon EC2 instances depends on the
platform version you chose.

For more information about platforms, see [AWS Elastic Beanstalk Platforms](../dg/concepts-all-platforms.md "../dg/concepts-all-platforms.md") in the _AWS Elastic Beanstalk
Developer Guide_. Detailed release notes are available for recent releases at [AWS Elastic Beanstalk Release Notes](../relnotes.md "../relnotes.md").

The following sections provide information about all current platform versions. For lists of historical platform versions and the date ranges they were current, see [Platform history](platform-history.md "platform-history.md").

###### Topics

- [Docker](#platforms-supported.docker "#platforms-supported.docker")
- [Go](#platforms-supported.go "#platforms-supported.go")
- [Java SE](#platforms-supported.javase "#platforms-supported.javase")
- [Tomcat](#platforms-supported.java "#platforms-supported.java")
- [.NET Core on Linux](#platforms-supported.dotnetlinux "#platforms-supported.dotnetlinux")
- [.NET on Windows Server](#platforms-supported.net "#platforms-supported.net")
- [Node.js](#platforms-supported.nodejs "#platforms-supported.nodejs")
- [PHP](#platforms-supported.PHP "#platforms-supported.PHP")
- [Python](#platforms-supported.python "#platforms-supported.python")
- [Ruby](#platforms-supported.ruby "#platforms-supported.ruby")
- [Elastic Beanstalk platform versions scheduled for retirement](platforms-retiring.md "platforms-retiring.md")
- [Elastic Beanstalk platform versions in public beta](platforms-beta.md "platforms-beta.md")

## Docker

Docker is a container platform that allows you to define your own software stack and store it in an image that can be downloaded from a remote
repository. The Docker platform includes an nginx proxy server.

See [Deploying Elastic Beanstalk Applications from Docker Containers](../dg/create_deploy_docker.md "../dg/create_deploy_docker.md") in the
_AWS Elastic Beanstalk Developer Guide_ for more information about the Docker platform.

| Platform Version and _Solution Stack Name_                                         | AMI             | ECS Agent | Docker  | Docker Compose | Proxy Server |
| ---------------------------------------------------------------------------------- | --------------- | --------- | ------- | -------------- | ------------ |
| **Docker AL2023 version 4.7.4**<br>_64bit Amazon Linux 2023 v4.7.4 running Docker_ | 2023.9.20251027 |           | 25.0.13 | 2.40.0         | nginx 1.28.0 |
| **ECS AL2023 version 4.2.8**<br>_64bit Amazon Linux 2023 v4.2.8 running ECS_       | 2023.9.20251027 | 1.100.0   | 25.0.13 |                |              |
| **Docker AL2 version 4.3.4**<br>_64bit Amazon Linux 2 v4.3.4 running Docker_       | 2.0.20251027    |           | 25.0.13 | 2.40.0         | nginx 1.28.0 |
| **ECS AL2 version 3.5.8**<br>_64bit Amazon Linux 2 v3.5.8 running ECS_             | 2.0.20251027    | 1.100.0   | 25.0.13 |                |              |

For information about previous platform versions, see [Docker platform history](platform-history-docker.md "platform-history-docker.md").

## Go

Elastic Beanstalk supports the following Go platform versions.

| Platform Version and _Solution Stack Name_                                     | AMI             | Language  | AWS X-Ray | Proxy Server |
| ------------------------------------------------------------------------------ | --------------- | --------- | --------- | ------------ |
| **Go 1 AL2023 version 4.4.8**<br>_64bit Amazon Linux 2023 v4.4.8 running Go 1_ | 2023.9.20251027 | Go 1.24.8 | 3.3.15    | nginx 1.28.0 |
| **Go 1 AL2 version 3.13.8**<br>_64bit Amazon Linux 2 v3.13.8 running Go 1_     | 2.0.20251027    | Go 1.25.3 | 3.3.15    | nginx 1.28.0 |

For information about previous platform versions, see [Go platform history](platform-history-go.md "platform-history-go.md").

## Java SE

Elastic Beanstalk supports the following Java SE platform versions.

| Platform Version and _Solution Stack Name_                                                   | AMI             | Language              | Tools                                    | AWS X-Ray | Proxy Server |
| -------------------------------------------------------------------------------------------- | --------------- | --------------------- | ---------------------------------------- | --------- | ------------ |
| **Corretto 25 AL2023 version 4.7.1**<br>_64bit Amazon Linux 2023 v4.7.1 running Corretto 25_ | 2023.9.20251027 | Corretto 25.0.1.8.1   | Ant 1.10.15, Gradle 9.2.0, Maven 3.9.11  | 3.3.15    | nginx 1.28.0 |
| **Corretto 21 AL2023 version 4.7.1**<br>_64bit Amazon Linux 2023 v4.7.1 running Corretto 21_ | 2023.9.20251027 | Corretto 21.0.9.10.1  | Ant 1.10.15, Gradle 9.2.0, Maven 3.9.11  | 3.3.15    | nginx 1.28.0 |
| **Corretto 17 AL2023 version 4.7.1**<br>_64bit Amazon Linux 2023 v4.7.1 running Corretto 17_ | 2023.9.20251027 | Corretto 17.0.17.10.1 | Ant 1.10.15, Gradle 9.2.0, Maven 3.9.11  | 3.3.15    | nginx 1.28.0 |
| **Corretto 11 AL2023 version 4.7.1**<br>_64bit Amazon Linux 2023 v4.7.1 running Corretto 11_ | 2023.9.20251027 | Corretto 11.0.29.7.1  | Ant 1.10.15, Gradle 8.14.3, Maven 3.9.11 | 3.3.15    | nginx 1.28.0 |
| **Corretto 8 AL2023 version 4.7.1**<br>_64bit Amazon Linux 2023 v4.7.1 running Corretto 8_   | 2023.9.20251027 | Corretto 8.472.08.1   | Ant 1.10.15, Gradle 8.14.3, Maven 3.9.11 | 3.3.15    | nginx 1.28.0 |
| **Corretto 17 version 3.9.8**<br>_64bit Amazon Linux 2 v3.9.8 running Corretto 17_           | 2.0.20251027    | Corretto 17.0.17.10.1 | Ant 1.10.15, Gradle 8.14.3, Maven 3.9.11 | 3.3.15    | nginx 1.28.0 |
| **Corretto 11 version 3.9.8**<br>_64bit Amazon Linux 2 v3.9.8 running Corretto 11_           | 2.0.20251027    | Corretto 11.0.29.7.1  | Ant 1.10.15, Gradle 8.14.3, Maven 3.9.11 | 3.3.15    | nginx 1.28.0 |
| **Corretto 8 version 3.9.8**<br>_64bit Amazon Linux 2 v3.9.8 running Corretto 8_             | 2.0.20251027    | Corretto 8.472.08.1   | Ant 1.10.15, Gradle 8.14.3, Maven 3.9.11 | 3.3.15    | nginx 1.28.0 |

For information about previous platform versions, see [Java SE platform history](platform-history-javase.md "platform-history-javase.md").

## Tomcat

Elastic Beanstalk supports the following Tomcat platform versions.

| Platform Version and _Solution Stack Name_                                                                            | AMI             | Language              | AWS X-Ray | Application Server | Proxy Server                          |
| --------------------------------------------------------------------------------------------------------------------- | --------------- | --------------------- | --------- | ------------------ | ------------------------------------- |
| **Corretto 25 with Tomcat 11 AL2023 version 5.8.1**<br>_64bit Amazon Linux 2023 v5.8.1 running Tomcat 11 Corretto 25_ | 2023.9.20251027 | Corretto 25.0.1.8.1   | 3.3.15    | Tomcat 11.0.13     | nginx 1.28.0 (default), Apache 2.4.65 |
| **Corretto 21 with Tomcat 11 AL2023 version 5.8.1**<br>_64bit Amazon Linux 2023 v5.8.1 running Tomcat 11 Corretto 21_ | 2023.9.20251027 | Corretto 21.0.9.10.1  | 3.3.15    | Tomcat 11.0.13     | nginx 1.28.0 (default), Apache 2.4.65 |
| **Corretto 17 with Tomcat 11 AL2023 version 5.8.1**<br>_64bit Amazon Linux 2023 v5.8.1 running Tomcat 11 Corretto 17_ | 2023.9.20251027 | Corretto 17.0.17.10.1 | 3.3.15    | Tomcat 11.0.13     | nginx 1.28.0 (default), Apache 2.4.65 |
| **Corretto 21 with Tomcat 10 AL2023 version 5.8.1**<br>_64bit Amazon Linux 2023 v5.8.1 running Tomcat 10 Corretto 21_ | 2023.9.20251027 | Corretto 21.0.9.10.1  | 3.3.15    | Tomcat 10.1.48     | nginx 1.28.0 (default), Apache 2.4.65 |
| **Corretto 17 with Tomcat 10 AL2023 version 5.8.1**<br>_64bit Amazon Linux 2023 v5.8.1 running Tomcat 10 Corretto 17_ | 2023.9.20251027 | Corretto 17.0.17.10.1 | 3.3.15    | Tomcat 10.1.48     | nginx 1.28.0 (default), Apache 2.4.65 |
| **Corretto 17 with Tomcat 9 AL2023 version 5.8.1**<br>_64bit Amazon Linux 2023 v5.8.1 running Tomcat 9 Corretto 17_   | 2023.9.20251027 | Corretto 17.0.17.10.1 | 3.3.15    | Tomcat 9.0.108     | nginx 1.28.0 (default), Apache 2.4.65 |
| **Corretto 11 with Tomcat 9 AL2023 version 5.8.1**<br>_64bit Amazon Linux 2023 v5.8.1 running Tomcat 9 Corretto 11_   | 2023.9.20251027 | Corretto 11.0.29.7.1  | 3.3.15    | Tomcat 9.0.108     | nginx 1.28.0 (default), Apache 2.4.65 |
| **Corretto 11 with Tomcat 9 AL2 version 4.9.8**<br>_64bit Amazon Linux 2 v4.9.8 running Tomcat 9 Corretto 11_         | 2.0.20251027    | Corretto 11.0.29.7.1  | 3.3.15    | Tomcat 9.0.108     | nginx 1.28.0 (default), Apache 2.4.65 |
| **Corretto 8 with Tomcat 9 AL2 version 4.9.8**<br>_64bit Amazon Linux 2 v4.9.8 running Tomcat 9 Corretto 8_           | 2.0.20251027    | Corretto 8.472.08.1   | 3.3.15    | Tomcat 9.0.108     | nginx 1.28.0 (default), Apache 2.4.65 |

For information about previous platform versions, see [Tomcat platform history](platform-history-java.md "platform-history-java.md").

## .NET Core on Linux

Elastic Beanstalk supports the following .NET Core on Linux platform versions.

| Platform Version and _Solution Stack Name_                                              | Framework                    | Proxy Server | AMI             | AWS X-Ray |
| --------------------------------------------------------------------------------------- | ---------------------------- | ------------ | --------------- | --------- |
| **.NET 9 on AL2023 version 3.5.8**<br>_64bit Amazon Linux 2023 v3.5.8 running .NET 9_   | .NET 9.0.10, supports 9.0.10 | nginx 1.28.0 | 2023.9.20251027 | 3.3.15    |
| **.NET 8 on AL2023 version 3.5.8**<br>_64bit Amazon Linux 2023 v3.5.8 running .NET 8_   | .NET 8.0.21, supports 8.0.21 | nginx 1.28.0 | 2023.9.20251027 | 3.3.15    |
| **.NET Core on AL2 version 2.11.8**<br>_64bit Amazon Linux 2 v2.11.8 running .NET Core_ | .NET 8.0.21, supports 8.0.21 | nginx 1.28.0 | 2.0.20251027    | 3.3.15    |

For information about previous platform versions, see [.NET Core on Linux platform history](platform-history-dotnetlinux.md "platform-history-dotnetlinux.md").

## .NET on Windows Server

You can get started in minutes using the [AWS Toolkit for Visual Studio](https://aws.amazon.com/visualstudio/ "https://aws.amazon.com/visualstudio/"). The toolkit includes the
AWS libraries, project templates, code samples, and documentation. The
AWS SDK for .NET supports the development of applications using .NET Framework 2.0 or later.

###### Note

This platform doesn't support the following Elastic Beanstalk features:

- Worker environments. For details, see [AWS Elastic Beanstalk Worker
  Environments](../dg/using-features-managing-env-tiers.md "../dg/using-features-managing-env-tiers.md") in the _AWS Elastic Beanstalk Developer Guide_.

To learn how to get started deploying a .NET application using the AWS Toolkit for Visual Studio, see
[Creating and Deploying Elastic Beanstalk Applications in .NET Using
AWS Toolkit for Visual Studio](../dg/create_deploy_NET.md "../dg/create_deploy_NET.md") in the _AWS Elastic Beanstalk Developer
Guide_.

For information about the latest Microsoft security updates, see [Security TechCenter](https://portal.msrc.microsoft.com/en-us/ "https://portal.msrc.microsoft.com/en-us/")
and [Security Advisories and Bulletins](https://technet.microsoft.com/en-us/library/security/ "https://technet.microsoft.com/en-us/library/security/").

For information about previous
.NET on Windows Server platform versions for Elastic Beanstalk, see [.NET on Windows Server platform history](platform-history-dotnet.md "platform-history-dotnet.md").

Elastic Beanstalk supports the following .NET on Windows Server platform versions.

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                       | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.21.0**      | _64bit Windows Server 2025 v2.21.0 running IIS 10.0_      | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.21.0** | _64bit Windows Server Core 2025 v2.21.0 running IIS 10.0_ | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.21.0**      | _64bit Windows Server 2022 v2.21.0 running IIS 10.0_      | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.21.0** | _64bit Windows Server Core 2022 v2.21.0 running IIS 10.0_ | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.21.0**      | _64bit Windows Server 2019 v2.21.0 running IIS 10.0_      | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.21.0** | _64bit Windows Server Core 2019 v2.21.0 running IIS 10.0_ | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.21.0**      | _64bit Windows Server 2016 v2.21.0 running IIS 10.0_      | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.21.0** | _64bit Windows Server Core 2016 v2.21.0 running IIS 10.0_ | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.21.0**      | 2025.10.15  | 3.7.1144.0       |           | 3.3.3270.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2025 with IIS 10.0 version 2.21.0** | 2025.10.15  | 3.7.1144.0       |           | 3.3.3270.0 | 4.0        | 3.6.1     |
| **Windows Server 2022 with IIS 10.0 version 2.21.0**      | 2025.10.15  | 3.7.1144.0       |           | 3.3.3270.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2022 with IIS 10.0 version 2.21.0** | 2025.10.15  | 3.7.1144.0       |           | 3.3.3270.0 | 4.0        | 3.6.1     |
| **Windows Server 2019 with IIS 10.0 version 2.21.0**      | 2025.10.15  | 3.7.1144.0       |           | 3.3.3270.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2019 with IIS 10.0 version 2.21.0** | 2025.10.15  | 3.7.1144.0       |           | 3.3.3270.0 | 4.0        | 3.6.1     |
| **Windows Server 2016 with IIS 10.0 version 2.21.0**      | 2025.10.15  | 3.7.1144.0       |           | 3.3.3270.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2016 with IIS 10.0 version 2.21.0** | 2025.10.15  | 3.7.1144.0       |           | 3.3.3270.0 | 4.0        | 3.6.1     |

## Node.js

Each Node.js platform version on Amazon Linux 2 supports multiple Node.js language versions. Only the default Node.js version is pre-installed.
Valid Node.js versions, as well as the default version, are listed in the following table. Starting with Amazon Linux 2023, only one Node.js version
is available on each platform version. Each Node.js version includes a respective version of npm (the Node.js package manager). The table lists npm
versions in parentheses.

Elastic Beanstalk supports the following Node.js platform versions.

| Platform Version and _Solution Stack Name_                                                 | AMI             | Node.js versions (npm versions)               | Proxy Server                          | Git    | AWS X-Ray |
| ------------------------------------------------------------------------------------------ | --------------- | --------------------------------------------- | ------------------------------------- | ------ | --------- |
| **Node.js 22 AL2023 version 6.6.8**<br>_64bit Amazon Linux 2023 v6.6.8 running Node.js 22_ | 2023.9.20251027 | 22.21.1 (10.9.4)<br>Default version: v22.21.1 | nginx 1.28.0 (default), Apache 2.4.65 | 2.50.1 | 3.3.15    |
| **Node.js 20 AL2023 version 6.6.8**<br>_64bit Amazon Linux 2023 v6.6.8 running Node.js 20_ | 2023.9.20251027 | 20.19.5 (10.8.2)<br>Default version: 20.19.5  | nginx 1.28.0 (default), Apache 2.4.65 | 2.50.1 | 3.3.15    |

For information about previous platform versions, see [Node.js platform history](platform-history-nodejs.md "platform-history-nodejs.md").

###### Note

When support for the version of Node.js that you are using is removed from the platform version, you must change or remove the version setting
prior to doing a [platform update](../dg/using-features.platform.md "../dg/using-features.platform.md"). This may occur when a security
vulnerability is identified for the Node.js version, or when the version is retired.

When this happens, attempting to update to a new version of the platform that doesn't support the configured Node.js version fails. To
avoid needing to create a new environment:

- _Amazon Linux 2_ – change the Node.js version setting in `package.json` to a Node.js
  version that is supported by both the old platform version and the new one, or remove the setting, and then deploy the new source bundle. Only
  then perform the platform update.
- _Amazon Linux AMI_ – change the `NodeVersion` configuration option to a version that is supported
  by both the old platform version and the new one, or [remove the
  option setting](../dg/environment-configuration-methods-after.md "../dg/environment-configuration-methods-after.md"), and then perform the platform update.

## PHP

Elastic Beanstalk supports the following PHP platform versions.

| Platform Version and _Solution Stack Name_                                           | AMI             | Language   | Composer | Proxy Server                          |
| ------------------------------------------------------------------------------------ | --------------- | ---------- | -------- | ------------------------------------- |
| **PHP 8.4 AL2023 version 4.7.8**<br>_64bit Amazon Linux 2023 v4.7.8 running PHP 8.4_ | 2023.9.20251027 | PHP 8.4.14 | 2.8.12   | nginx 1.28.0 (default), Apache 2.4.65 |
| **PHP 8.3 AL2023 version 4.7.8**<br>_64bit Amazon Linux 2023 v4.7.8 running PHP 8.3_ | 2023.9.20251027 | PHP 8.3.26 | 2.8.12   | nginx 1.28.0 (default), Apache 2.4.65 |
| **PHP 8.2 AL2023 version 4.7.8**<br>_64bit Amazon Linux 2023 v4.7.8 running PHP 8.2_ | 2023.9.20251027 | PHP 8.2.29 | 2.8.12   | nginx 1.28.0 (default), Apache 2.4.65 |
| **PHP 8.1 AL2023 version 4.7.8**<br>_64bit Amazon Linux 2023 v4.7.8 running PHP 8.1_ | 2023.9.20251027 | PHP 8.1.33 | 2.8.12   | nginx 1.28.0 (default), Apache 2.4.65 |
| **PHP 8.1 AL2 version 3.10.8**<br>_64bit Amazon Linux 2 v3.10.8 running PHP 8.1_     | 2.0.20251027    | PHP 8.1.33 | 2.8.12   | nginx 1.28.0 (default), Apache 2.4.65 |

For information about previous platform versions, see [PHP platform history](platform-history-php.md "platform-history-php.md").

## Python

Elastic Beanstalk supports the following Python platform versions.

| Platform Version and _Solution Stack Name_                                                   | AMI             | Language       | Package Manager | Packager | meld3 | AWS X-Ray | Proxy Server                          |
| -------------------------------------------------------------------------------------------- | --------------- | -------------- | --------------- | -------- | ----- | --------- | ------------------------------------- |
| **Python 3.13 AL2023 version 4.7.5**<br>_64bit Amazon Linux 2023 v4.7.5 running Python 3.13_ | 2023.9.20251027 | Python 3.13.9  | pipenv 2025.0.4 |          |       | 3.3.15    | nginx 1.28.0 (default), Apache 2.4.65 |
| **Python 3.12 AL2023 version 4.7.5**<br>_64bit Amazon Linux 2023 v4.7.5 running Python 3.12_ | 2023.9.20251027 | Python 3.12.12 | pipenv 2025.0.4 |          |       | 3.3.15    | nginx 1.28.0 (default), Apache 2.4.65 |
| **Python 3.11 AL2023 version 4.7.5**<br>_64bit Amazon Linux 2023 v4.7.5 running Python 3.11_ | 2023.9.20251027 | Python 3.11.14 | pipenv 2025.0.4 |          |       | 3.3.15    | nginx 1.28.0 (default), Apache 2.4.65 |
| **Python 3.9 AL2023 version 4.7.5**<br>_64bit Amazon Linux 2023 v4.7.5 running Python 3.9_   | 2023.9.20251027 | Python 3.9.24  | pipenv 2025.0.4 |          |       | 3.3.15    | nginx 1.28.0 (default), Apache 2.4.65 |

For information about previous platform versions, see [Python platform history](platform-history-python.md "platform-history-python.md").

## Ruby

Elastic Beanstalk supports the following Ruby platform versions.

| Platform Version and _Solution Stack Name_                                             | AMI             | Language         | Package Manager | Application Server | AWS X-Ray | Proxy Server |
| -------------------------------------------------------------------------------------- | --------------- | ---------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 3.4 AL2023 version 4.7.3**<br>_64bit Amazon Linux 2023 v4.7.3 running Ruby 3.4_ | 2023.9.20251027 | Ruby 3.4.7-p58   | RubyGems 3.6.9  | Puma 7.1.0         | 3.3.15    | nginx 1.28.0 |
| **Ruby 3.3 AL2023 version 4.7.3**<br>_64bit Amazon Linux 2023 v4.7.3 running Ruby 3.3_ | 2023.9.20251027 | Ruby 3.3.10-p183 | RubyGems 3.5.22 | Puma 7.1.0         | 3.3.15    | nginx 1.28.0 |
| **Ruby 3.2 AL2023 version 4.7.3**<br>_64bit Amazon Linux 2023 v4.7.3 running Ruby 3.2_ | 2023.9.20251027 | Ruby 3.2.8       | RubyGems 3.4.19 | Puma 7.1.0         | 3.3.15    | nginx 1.28.0 |

For information about previous platform versions, see [Ruby platform history](platform-history-ruby.md "platform-history-ruby.md").
