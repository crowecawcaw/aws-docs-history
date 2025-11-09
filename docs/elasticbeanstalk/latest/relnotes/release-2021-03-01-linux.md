# Release: Elastic Beanstalk Amazon Linux AMI platform updates on March 1, 2021

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux AMI. The release includes security updates.
It also includes Multicontainer Docker, Go, and Node.js updates.

**Release date:** March 1, 2021

## Changes

The following table lists the changes included in this release.

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------- | ---- | ------- | ------- | ---- | ------------------------------ | ---------------------------------------- | ---- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/ "https://alas.aws.amazon.com/") on or before **February 24, 2021\*<br>• to all Amazon Linux AMI platforms.<br>The **Node.js*<br>• release is a security release. For more information, see \*\*Platform-specific<br>updates*<br>• in this table. |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                                                                  | \*_Platform_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Multicontainer Docker_<br>• | Updated the ECS agent to version 1.50.2. | <br> | \*_Go_<br>• | Updated Go to release 1.16. For details, see [go1.16](https://golang.org/doc/devel/release.html#go1.16 "https://golang.org/doc/devel/release.html#go1.16") in<br>_The Go Programming Language Release History_. | <br> | \*_Node.js_<br>• | Updated the Node.js platform to add support for Node versions<br>[12.21.0](https://nodejs.org/en/blog/release/v12.21.0/ "https://nodejs.org/en/blog/release/v12.21.0/"),<br>[12.20.2](https://nodejs.org/en/blog/release/v12.20.2/ "https://nodejs.org/en/blog/release/v12.20.2/"),<br>[10.24.0](https://nodejs.org/en/blog/release/v10.24.0/ "https://nodejs.org/en/blog/release/v10.24.0/"),<br>[10.23.3](https://nodejs.org/en/blog/release/v10.23.3/ "https://nodejs.org/en/blog/release/v10.23.3/"), and<br>[10.23.2](https://nodejs.org/en/blog/release/v10.23.2/ "https://nodejs.org/en/blog/release/v10.23.2/").<br>The new Node.js versions are security releases. |     |

## New platform versions

###### Note

The following tables list all supported platform branches for each platform. Only Amazon Linux AMI platform branches are updated.

###### These platforms are updated:

- [Docker](#release-2021-03-01-linux.platforms.docker "#release-2021-03-01-linux.platforms.docker")
- [Multicontainer Docker](#release-2021-03-01-linux.platforms.mcdocker "#release-2021-03-01-linux.platforms.mcdocker")
- [Preconfigured Docker](#release-2021-03-01-linux.platforms.dockerpreconfig "#release-2021-03-01-linux.platforms.dockerpreconfig")
- [Go](#release-2021-03-01-linux.platforms.go "#release-2021-03-01-linux.platforms.go")
- [Java SE](#release-2021-03-01-linux.platforms.javase "#release-2021-03-01-linux.platforms.javase")
- [Tomcat](#release-2021-03-01-linux.platforms.java "#release-2021-03-01-linux.platforms.java")
- [Node.js](#release-2021-03-01-linux.platforms.nodejs "#release-2021-03-01-linux.platforms.nodejs")
- [PHP](#release-2021-03-01-linux.platforms.PHP "#release-2021-03-01-linux.platforms.PHP")
- [Python](#release-2021-03-01-linux.platforms.python "#release-2021-03-01-linux.platforms.python")
- [Ruby](#release-2021-03-01-linux.platforms.ruby "#release-2021-03-01-linux.platforms.ruby")

### Docker

| Platform Version and _Solution Stack Name_                                                                    | AMI          | Docker      | Docker Compose | Proxy Server |
| ------------------------------------------------------------------------------------------------------------- | ------------ | ----------- | -------------- | ------------ |
| **Docker AL2 version 3.2.5**<br>_64bit Amazon Linux 2 v3.2.5 running Docker_                                  | 2.0.20210219 | 19.03.13-ce | 1.28.4         | nginx 1.18.0 |
| **Single Container Docker version 2.16.5**<br>_64bit Amazon Linux 2018.03 v2.16.5 running Docker 19.03.13-ce_ | 2018.03.0    | 19.03.13-ce |                | nginx 1.18.0 |

### Multicontainer Docker

| Platform Version and _Solution Stack Name_                                                                                            | AMI       | Docker      | ECS Agent |
| ------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------- | --------- |
| **Multicontainer Docker version 2.25.1**<br>_64bit Amazon Linux 2018.03 v2.25.1 running Multi-container Docker 19.03.13-ce (Generic)_ | 2018.03.0 | 19.03.13-ce | 1.50.2    |

### Preconfigured Docker

| Platform Version and _Solution Stack Name_                                                                                         | AMI       | Platform           | Container OS         | Language | Proxy Server | Application Server | Docker Image                                  |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------ | -------------------- | -------- | ------------ | ------------------ | --------------------------------------------- |
| **Glassfish 5.0 (Docker) version 2.16.5**<br>_64bit Amazon Linux v2.16.5 running GlassFish 5.0 Java 8 (Preconfigured<br>• Docker)_ | 2018.03.0 | Docker 19.03.13-ce | Amazon Linux 2018.03 | Java 8   | nginx 1.18.0 | Glassfish 5.0      | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 |

### Go

| Platform Version and _Solution Stack Name_                                      | AMI          | Language | AWS X‑Ray | Proxy Server |
| ------------------------------------------------------------------------------- | ------------ | -------- | --------- | ------------ |
| **Go 1 AL2 version 3.2.0**<br>_64bit Amazon Linux 2 v3.2.0 running Go 1_        | 2.0.20210219 | Go 1.16  | 3.2.0     | nginx 1.18.0 |
| **Go 1 version 2.18.0**<br>_64bit Amazon Linux 2018.03 v2.18.0 running Go 1.16_ | 2018.03.0    | Go 1.16  | 3.1.0     | nginx 1.18.0 |

### Java SE

| Platform Version and _Solution Stack Name_                                         | AMI          | Language             | Tools                                 | AWS X‑Ray | Proxy Server |
| ---------------------------------------------------------------------------------- | ------------ | -------------------- | ------------------------------------- | --------- | ------------ |
| **Corretto 11 version 3.1.6**<br>_64bit Amazon Linux 2 v3.1.6 running Corretto 11_ | 2.0.20210219 | Corretto 11.0.10.9.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.18.0 |
| **Corretto 8 version 3.1.6**<br>_64bit Amazon Linux 2 v3.1.6 running Corretto 8_   | 2.0.20210219 | Corretto 8.282.08.1  | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.18.0 |
| **Java 8 version 2.11.4**<br>_64bit Amazon Linux 2018.03 v2.11.4 running Java 8_   | 2018.03.0    | Java 1.8.0_272       | Ant 1.9.6, Gradle 2.7, Maven 3.3.3    | 3.1.0     | nginx 1.18.0 |
| **Java 7 version 2.11.4**<br>_64bit Amazon Linux 2018.03 v2.11.4 running Java 7_   | 2018.03.0    | Java 1.7.0_261       | Ant 1.9.6, Gradle 2.7, Maven 3.3.3    | 3.1.0     | nginx 1.18.0 |

### Tomcat

| Platform Version and _Solution Stack Name_                                                                        | AMI          | Language             | AWS X‑Ray | Application Server | Proxy Server                          |
| ----------------------------------------------------------------------------------------------------------------- | ------------ | -------------------- | --------- | ------------------ | ------------------------------------- |
| **Corretto 11 with Tomcat 8.5 AL2 version 4.1.6**<br>_64bit Amazon Linux 2 v4.1.6 running Tomcat 8.5 Corretto 11_ | 2.0.20210219 | Corretto 11.0.10.9.1 | 3.2.0     | Tomcat 8.5.60      | nginx 1.18.0 (default), Apache 2.4.46 |
| **Corretto 8 with Tomcat 8.5 AL2 version 4.1.6**<br>_64bit Amazon Linux 2 v4.1.6 running Tomcat 8.5 Corretto 8_   | 2.0.20210219 | Corretto 8.282.08.1  | 3.2.0     | Tomcat 8.5.60      | nginx 1.18.0 (default), Apache 2.4.46 |
| **Corretto 11 with Tomcat 7 AL2 version 4.1.6**<br>_64bit Amazon Linux 2 v4.1.6 running Tomcat 7 Corretto 11_     | 2.0.20210219 | Corretto 11.0.10.9.1 | 3.2.0     | Tomcat 7.0.76      | nginx 1.18.0 (default), Apache 2.4.46 |
| **Corretto 8 with Tomcat 7 AL2 version 4.1.6**<br>_64bit Amazon Linux 2 v4.1.6 running Tomcat 7 Corretto 8_       | 2.0.20210219 | Corretto 8.282.08.1  | 3.2.0     | Tomcat 7.0.76      | nginx 1.18.0 (default), Apache 2.4.46 |
| **Java 8 with Tomcat 8.5 version 3.4.4**<br>_64bit Amazon Linux 2018.03 v3.4.4 running Tomcat 8.5 Java 8_         | 2018.03.0    | Java 1.8.0_272       | 3.1.0     | Tomcat 8.5.60      | Apache 2.4.46 (default), Nginx 1.18.0 |
| **Java 7 with Tomcat 7 version 3.4.4**<br>_64bit Amazon Linux 2018.03 v3.4.4 running Tomcat 7 Java 7_             | 2018.03.0    | Java 1.7.0_261       | 3.1.0     | Tomcat 7.0.107     | Apache 2.4.46 (default), Nginx 1.18.0 |

### Node.js

| Platform Version and _Solution Stack Name_                                           | AMI          | Node.js versions (npm versions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Proxy Server                          | Git    | AWS X‑Ray |
| ------------------------------------------------------------------------------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------ | --------- |
| **Node.js 14 AL2 version 5.3.0**<br>_64bit Amazon Linux 2 v5.3.0 running Node.js 14_ | 2.0.20210219 | 14.16.0 (6.14.11), 14.15.5 (6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8), 14.15.0 (6.14.8), 14.14.0 (6.14.8), 14.13.1 (6.14.8), 14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0 (6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7), 14.7.0 (6.14.7), 14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0 (6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br>Default version: 14.16.0                                                                                                                                                                                                                                                                                       | nginx 1.18.0 (default), Apache 2.4.46 | 2.23.3 | 3.2.0     |
| **Node.js 12 AL2 version 5.3.0**<br>_64bit Amazon Linux 2 v5.3.0 running Node.js 12_ | 2.0.20210219 | 12.21.0 (6.14.11), 12.20.2 (6.14.11), 12.20.1 (6.14.10), 12.20.0 (6.14.8), 12.19.1 (6.14.8), 12.19.0 (6.14.8), 12.18.4 (6.14.6), 12.18.3 (6.14.6), 12.18.2 (6.14.5), 12.18.1 (6.14.5), 12.18.0 (6.14.4), 12.17.0 (6.14.4), 12.16.3 (6.14.4), 12.16.2 (6.14.4), 12.16.1 (6.13.4), 12.16.0 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 12.13.1 (6.12.1), 12.13.0 (6.12.0), 12.12.0 (6.11.3), 12.11.1 (6.11.3), 12.11.0 (6.11.3), 12.10.0 (6.10.3), 12.9.1 (6.10.2), 12.9.0 (6.10.2), 12.8.1 (6.10.2), 12.8.0 (6.10.2), 12.7.0 (6.10.0), 12.6.0 (6.9.0), 12.5.0 (6.9.0), 12.4.0 (6.9.0), 12.3.1 (6.9.0), 12.3.0 (6.9.0), 12.2.0 (6.9.0), 12.1.0 (6.9.0), 12.0.0 (6.9.0)<br>Default version: 12.21.0                                      | nginx 1.18.0 (default), Apache 2.4.46 | 2.23.3 | 3.2.0     |
| **Node.js 10 AL2 version 5.3.0**<br>_64bit Amazon Linux 2 v5.3.0 running Node.js 10_ | 2.0.20210219 | 10.24.0 (6.14.11), 10.23.3 (6.14.11), 10.23.2 (6.14.10), 10.23.1 (6.14.10), 10.23.0 (6.14.8), 10.22.1 (6.14.6), 10.22.0 (6.14.6), 10.21.0 (6.14.4), 10.20.1 (6.14.4), 10.20.0 (6.14.4), 10.19.0 (6.13.4), 10.18.1 (6.13.4), 10.18.0 (6.13.4), 10.17.0 (6.11.3), 10.16.3 (6.9.0), 10.16.2 (6.9.0), 10.16.1 (6.9.0), 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.2 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.2 (6.4.1), 10.14.1 (6.4.1), 10.14.0 (6.4.1), 10.13.0 (6.4.1), 10.12.0 (6.4.1), 10.11.0 (6.4.1), 10.10.0 (6.4.1), 10.9.0 (6.2.0), 10.8.0 (6.2.0), 10.7.0 (6.1.0), 10.6.0 (6.1.0), 10.5.0 (6.1.0), 10.4.1 (6.1.0), 10.4.0 (6.1.0), 10.3.0 (6.1.0), 10.2.1 (5.6.0), 10.2.0 (5.6.0), 10.1.0 (5.6.0), 10.0.0 (5.6.0)<br>Default version: 10.24.0 | nginx 1.18.0 (default), Apache 2.4.46 | 2.23.3 | 3.2.0     |
| **Node.js version 4.17.3**<br>_64bit Amazon Linux 2018.03 v4.17.3 running Node.js_   | 2018.03.0    | 12.21.0 (6.14.11), 12.20.2 (6.14.11), 12.20.1 (6.14.10), 12.20.0 (6.14.8), 12.19.1 (6.14.8), 12.19.0 (6.14.8), 12.18.4 (6.14.6),12.18.3 (6.14.6), 12.18.2 (6.14.5), 12.18.1 (6.14.5), 12.18.0 (6.14.4), 12.16.4 (6.14.4), 12.16.2 (6.14.4), 12.16.1 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 10.24.0 (6.14.11), 10.23.3 (6.14.11), 10.23.2 (6.14.10), 10.23.1 (6.14.10), 10.23.0 (6.14.8), 10.22.1 (6.14.6), 10.22.0 (6.14.6), 10.21.0 (6.14.4), 10.20.1 (6.14.4), 10.20.0(6.14.4), 10.19.0 (6.13.4), 10.18.1 (6.13.4), 10.18.0 (6.13.4), 10.17.0 (6.11.3), 10.16.3 (6.9.0), 10.16.2 (6.9.0), 10.16.1 (6.9.0), 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1)<br>Default version: 12.21.0     | nginx 1.18.0, Apache 2.4.43           | 2.18.4 | 3.1.0     |

### PHP

| Platform Version and _Solution Stack Name_                                         | AMI          | Language   | Composer | Proxy Server                          |
| ---------------------------------------------------------------------------------- | ------------ | ---------- | -------- | ------------------------------------- |
| **PHP 7.4 AL2 version 3.1.6**<br>_64bit Amazon Linux 2 v3.1.6 running PHP 7.4_     | 2.0.20210219 | PHP 7.4.15 | 1.9.3    | nginx 1.18.0 (default), Apache 2.4.46 |
| **PHP 7.3 AL2 version 3.1.6**<br>_64bit Amazon Linux 2 v3.1.6 running PHP 7.3_     | 2.0.20210219 | PHP 7.3.27 | 1.9.3    | nginx 1.18.0 (default), Apache 2.4.46 |
| **PHP 7.2 AL2 version 3.1.6**<br>_64bit Amazon Linux 2 v3.1.6 running PHP 7.2_     | 2.0.20210219 | PHP 7.2.34 | 1.9.3    | nginx 1.18.0 (default), Apache 2.4.46 |
| **PHP 7.3 version 2.9.15**<br>_64bit Amazon Linux 2018.03 v2.9.15 running PHP 7.3_ | 2018.03.0    | PHP 7.3.23 | 1.9.0    | Apache 2.4.46                         |
| **PHP 7.2 version 2.9.15**<br>_64bit Amazon Linux 2018.03 v2.9.15 running PHP 7.2_ | 2018.03.0    | PHP 7.2.34 | 1.9.0    | Apache 2.4.46                         |

### Python

| Platform Version and _Solution Stack Name_                                               | AMI          | Language      | Package Manager  | Packager          | meld3       | AWS X‑Ray | Proxy Server                          |
| ---------------------------------------------------------------------------------------- | ------------ | ------------- | ---------------- | ----------------- | ----------- | --------- | ------------------------------------- |
| **Python 3.8 AL2 version 3.2.0**<br>_64bit Amazon Linux 2 v3.2.0 running Python 3.8_     | 2.0.20210219 | Python 3.8.5  | pipenv 2020.8.13 |                   |             | 3.2.0     | nginx 1.18.0 (default), Apache 2.4.46 |
| **Python 3.7 AL2 version 3.2.0**<br>_64bit Amazon Linux 2 v3.2.0 running Python 3.7_     | 2.0.20210219 | Python 3.7.9  | pipenv 2020.8.13 |                   |             | 3.2.0     | nginx 1.18.0 (default), Apache 2.4.46 |
| **Python 3.6 version 2.9.19**<br>_64bit Amazon Linux 2018.03 v2.9.19 running Python 3.6_ | 2018.03.0    | Python 3.6.12 | pip 9.0.3        | setuptools 28.8.0 | meld3 1.0.2 | 3.1.0     | Apache 2.4.46 with mod_wsgi 3.5       |

### Ruby

| Platform Version and _Solution Stack Name_                                                                                 | AMI          | Language         | Package Manager | Application Server | AWS X‑Ray | Proxy Server |
| -------------------------------------------------------------------------------------------------------------------------- | ------------ | ---------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 2.7 AL2 version 3.2.3**<br>_64bit Amazon Linux 2 v3.2.3 running Ruby 2.7_                                           | 2.0.20210219 | Ruby 2.7.2-p137  | RubyGems 3.2.8  | Puma 5.2.1         | 3.2.0     | nginx 1.18.0 |
| **Ruby 2.6 AL2 version 3.2.3**<br>_64bit Amazon Linux 2 v3.2.3 running Ruby 2.6_                                           | 2.0.20210219 | Ruby 2.6.6-p146  | RubyGems 3.2.8  | Puma 5.2.1         | 3.2.0     | nginx 1.18.0 |
| **Ruby 2.5 AL2 version 3.2.3**<br>_64bit Amazon Linux 2 v3.2.3 running Ruby 2.5_                                           | 2.0.20210219 | Ruby 2.5.8-p224  | RubyGems 3.2.8  | Puma 5.2.1         | 3.2.0     | nginx 1.18.0 |
| **Ruby 2.6 with Puma version 2.12.4**<br>_64bit Amazon Linux 2018.03 v2.12.4 running Ruby 2.6 (Puma)_                      | 2018.03.0    | Ruby 2.6.6-p146  | RubyGems 3.1.2  | Puma 2.16.0        | 3.1.0     | nginx 1.18.0 |
| **Ruby 2.6 with Passenger version 2.12.4**<br>_64bit Amazon Linux 2018.03 v2.12.4 running Ruby 2.6 (Passenger Standalone)_ | 2018.03.0    | Ruby 2.6.6-p146  | RubyGems 3.1.2  | Passenger 4.0.60   | 3.1.0     | nginx 1.18.0 |
| **Ruby 2.5 with Puma version 2.12.4**<br>_64bit Amazon Linux 2018.03 v2.12.4 running Ruby 2.5 (Puma)_                      | 2018.03.0    | Ruby 2.5.8-p224  | RubyGems 3.1.2  | Puma 2.16.0        | 3.1.0     | nginx 1.18.0 |
| **Ruby 2.5 with Passenger version 2.12.4**<br>_64bit Amazon Linux 2018.03 v2.12.4 running Ruby 2.5 (Passenger Standalone)_ | 2018.03.0    | Ruby 2.5.8-p224  | RubyGems 3.1.2  | Passenger 4.0.60   | 3.1.0     | nginx 1.18.0 |
| **Ruby 2.4 with Puma version 2.12.4**<br>_64bit Amazon Linux 2018.03 v2.12.4 running Ruby 2.4 (Puma)_                      | 2018.03.0    | Ruby 2.4.10-p364 | RubyGems 3.1.2  | Puma 2.16.0        | 3.1.0     | nginx 1.18.0 |
| **Ruby 2.4 with Passenger version 2.12.4**<br>_64bit Amazon Linux 2018.03 v2.12.4 running Ruby 2.4 (Passenger Standalone)_ | 2018.03.0    | Ruby 2.4.10-p364 | RubyGems 3.1.2  | Passenger 4.0.60   | 3.1.0     | nginx 1.18.0 |
