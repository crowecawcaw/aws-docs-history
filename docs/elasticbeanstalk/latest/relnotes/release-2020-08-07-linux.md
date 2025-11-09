# Release: Elastic Beanstalk Amazon Linux AMI platform updates on August 7, 2020

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux AMI. The release includes security updates.
It also includes Multicontainer Docker, Go, Tomcat, Node.js, PHP, and Python updates.

**Release date:** August 7, 2020

## Changes

The following table lists the changes included in this release.

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------- | ---- | ------- | ------- | ---- | ------------------------------ | ---------------------------------------- | ---- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/ "https://alas.aws.amazon.com/") on or before **July 29, 2020\*<br>• to all Amazon Linux AMI platforms.<br>The **PHP 7.2.31*<br>• and \*\*Python 3.6.11*<br>• releases include security fixes. For more<br>information, see \*_Platform-specific updates_<br>• in this table. |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                                                                                              | \*_Platform_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Multicontainer Docker_<br>• | Updated the ECS agent to version 1.42.0. | <br> | \*_Go_<br>• | Updated Go to release 1.14.5. For details, see [go1.14](https://golang.org/doc/devel/release.html#go1.14 "https://golang.org/doc/devel/release.html#go1.14") in<br>_The Go Programming Language Release History_. | <br> | \*_Tomcat_<br>• | Updated Tomcat 8.5 to [Tomcat<br>8.5.57](<https://tomcat.apache.org/tomcat-8.5-doc/changelog.html#Tomcat_8.5.57_(markt)> "https://tomcat.apache.org/tomcat-8.5-doc/changelog.html#Tomcat_8.5.57_(markt)"). | <br> | \*_Node.js_<br>• | Updated the Node.js platform to add support for Node versions<br>[12.18.3](https://nodejs.org/en/blog/release/v12.18.3/ "https://nodejs.org/en/blog/release/v12.18.3/"),<br>[12.18.2](https://nodejs.org/en/blog/release/v12.18.2/ "https://nodejs.org/en/blog/release/v12.18.2/"), and<br>[10.22.0](https://nodejs.org/en/blog/release/v10.22.0/ "https://nodejs.org/en/blog/release/v10.22.0/"). | <br> | \*_PHP_<br>• | Updated PHP 7.3 and 7.2 to releases<br>[7.3.19](https://www.php.net/releases/7_3_19.php "https://www.php.net/releases/7_3_19.php") and<br>[7.2.31](https://www.php.net/releases/7_2_31.php "https://www.php.net/releases/7_2_31.php"), respectively.<br>The \*_PHP 7.2.31_<br>• release includes security fixes. | <br> | \*_Python_<br>• | Updated Python 3.6 to [Python<br>3.6.11](https://docs.python.org/3.6/whatsnew/changelog.html#python-3-6-11-final "https://docs.python.org/3.6/whatsnew/changelog.html#python-3-6-11-final").<br>The \*_Python 3.6.11_<br>• release includes security fixes. |     |

## New platform versions

###### Note

The following tables list all supported platform branches for each platform. Only Amazon Linux AMI platform branches are updated.

###### These platforms are updated:

- [Docker](#release-2020-08-07-linux.platforms.docker "#release-2020-08-07-linux.platforms.docker")
- [Multicontainer Docker](#release-2020-08-07-linux.platforms.mcdocker "#release-2020-08-07-linux.platforms.mcdocker")
- [Preconfigured Docker](#release-2020-08-07-linux.platforms.dockerpreconfig "#release-2020-08-07-linux.platforms.dockerpreconfig")
- [Go](#release-2020-08-07-linux.platforms.go "#release-2020-08-07-linux.platforms.go")
- [Java SE](#release-2020-08-07-linux.platforms.javase "#release-2020-08-07-linux.platforms.javase")
- [Tomcat](#release-2020-08-07-linux.platforms.java "#release-2020-08-07-linux.platforms.java")
- [Node.js](#release-2020-08-07-linux.platforms.nodejs "#release-2020-08-07-linux.platforms.nodejs")
- [PHP](#release-2020-08-07-linux.platforms.PHP "#release-2020-08-07-linux.platforms.PHP")
- [Python](#release-2020-08-07-linux.platforms.python "#release-2020-08-07-linux.platforms.python")
- [Ruby](#release-2020-08-07-linux.platforms.ruby "#release-2020-08-07-linux.platforms.ruby")

### Docker

| Platform Version and _Solution Stack Name_                                                                   | AMI          | Docker Version | Proxy Server |
| ------------------------------------------------------------------------------------------------------------ | ------------ | -------------- | ------------ |
| **Docker AL2 version 3.1.0**<br>_64bit Amazon Linux 2 v3.1.0 running Docker_                                 | 2.0.20200723 | 19.03.6-ce     | nginx 1.18.0 |
| **Single Container Docker version 2.15.3**<br>_64bit Amazon Linux 2018.03 v2.15.3 running Docker 19.03.6-ce_ | 2018.03.0    | 19.03.6-ce     | nginx 1.16.1 |

### Multicontainer Docker

| Platform Version and _Solution Stack Name_                                                                                           | AMI       | Docker Version | ECS Agent |
| ------------------------------------------------------------------------------------------------------------------------------------ | --------- | -------------- | --------- |
| **Multicontainer Docker version 2.21.0**<br>_64bit Amazon Linux 2018.03 v2.21.0 running Multi-container Docker 19.03.6-ce (Generic)_ | 2018.03.0 | 19.03.6-ce     | 1.42.0    |

### Preconfigured Docker

| Platform Version and _Solution Stack Name_                                                                                         | AMI       | Platform          | Container OS         | Language | Proxy Server | Application Server | Docker Image                                  |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------- | -------------------- | -------- | ------------ | ------------------ | --------------------------------------------- |
| **Glassfish 5.0 (Docker) version 2.15.3**<br>_64bit Amazon Linux v2.15.3 running GlassFish 5.0 Java 8 (Preconfigured<br>• Docker)_ | 2018.03.0 | Docker 19.03.6-ce | Amazon Linux 2018.03 | Java 8   | nginx 1.16.1 | Glassfish 5.0      | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 |

### Go

| Platform Version and _Solution Stack Name_                                           | AMI          | Language  | AWS X‑Ray | Proxy Server |
| ------------------------------------------------------------------------------------ | ------------ | --------- | --------- | ------------ |
| **Go 1 AL2 version 3.1.0**<br>_64bit Amazon Linux 2 v3.1.0 running Go 1_             | 2.0.20200723 | Go 1.14.6 | 3.2.0     | nginx 1.18.0 |
| **Go 1.14 version 2.15.6**<br>_64bit Amazon Linux 2018.03 v2.15.6 running Go 1.14.5_ | 2018.03.0    | Go 1.14.5 | 3.1.0     | nginx 1.16.1 |

### Java SE

| Platform Version and _Solution Stack Name_                                         | AMI          | Language             | Tools                                 | AWS X‑Ray | Proxy Server |
| ---------------------------------------------------------------------------------- | ------------ | -------------------- | ------------------------------------- | --------- | ------------ |
| **Corretto 11 version 3.0.5**<br>_64bit Amazon Linux 2 v3.0.5 running Corretto 11_ | 2.0.20200723 | Corretto 11.0.8.10.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.18.0 |
| **Corretto 8 version 3.0.5**<br>_64bit Amazon Linux 2 v3.0.5 running Corretto 8_   | 2.0.20200723 | Corretto 8.262.10.1  | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.18.0 |
| **Java 8 version 2.10.10**<br>_64bit Amazon Linux 2018.03 v2.10.10 running Java 8_ | 2018.03.0    | Java 1.8.0_252       | Ant 1.9.6, Gradle 2.7, Maven 3.3.3    | 3.1.0     | nginx 1.16.1 |
| **Java 7 version 2.10.10**<br>_64bit Amazon Linux 2018.03 v2.10.10 running Java 7_ | 2018.03.0    | Java 1.7.0_261       | Ant 1.9.6, Gradle 2.7, Maven 3.3.3    | 3.1.0     | nginx 1.16.1 |

### Tomcat

| Platform Version and _Solution Stack Name_                                                                        | AMI          | Language             | AWS X‑Ray | Application Server | Proxy Server                                         |
| ----------------------------------------------------------------------------------------------------------------- | ------------ | -------------------- | --------- | ------------------ | ---------------------------------------------------- |
| **Corretto 11 with Tomcat 8.5 AL2 version 4.1.0**<br>_64bit Amazon Linux 2 v4.1.0 running Tomcat 8.5 Corretto 11_ | 2.0.20200723 | Corretto 11.0.8.10.1 | 3.2.0     | Tomcat 8.5.56      | nginx 1.18.0 (default), Apache 2.4.43                |
| **Corretto 8 with Tomcat 8.5 AL2 version 4.1.0**<br>_64bit Amazon Linux 2 v4.1.0 running Tomcat 8.5 Corretto 8_   | 2.0.20200723 | Corretto 8.262.10.1  | 3.2.0     | Tomcat 8.5.56      | nginx 1.18.0 (default), Apache 2.4.43                |
| **Corretto 11 with Tomcat 7 AL2 version 4.1.0**<br>_64bit Amazon Linux 2 v4.1.0 running Tomcat 7 Corretto 11_     | 2.0.20200723 | Corretto 11.0.8.10.1 | 3.2.0     | Tomcat 7.0.76      | nginx 1.18.0 (default), Apache 2.4.43                |
| **Corretto 8 with Tomcat 7 AL2 version 4.1.0**<br>_64bit Amazon Linux 2 v4.1.0 running Tomcat 7 Corretto 8_       | 2.0.20200723 | Corretto 8.262.10.1  | 3.2.0     | Tomcat 7.0.76      | nginx 1.18.0 (default), Apache 2.4.43                |
| **Java 8 with Tomcat 8.5 version 3.3.9**<br>_64bit Amazon Linux 2018.03 v3.3.9 running Tomcat 8.5 Java 8_         | 2018.03.0    | Java 1.8.0_252       | 3.1.0     | Tomcat 8.5.57      | Apache 2.4.43 (default), Apache 2.2.34, Nginx 1.16.1 |
| **Java 7 with Tomcat 7 version 3.3.9**<br>_64bit Amazon Linux 2018.03 v3.3.9 running Tomcat 7 Java 7_             | 2018.03.0    | Java 1.7.0_261       | 3.1.0     | Tomcat 7.0.104     | Apache 2.4.43 (default), Apache 2.2.34, Nginx 1.16.1 |

### Node.js

| Platform Version and _Solution Stack Name_                                           | AMI          | Node.js versions (npm versions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Proxy Server                          | Git    | AWS X‑Ray |
| ------------------------------------------------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------ | --------- |
| **Node.js 12 AL2 version 5.2.0**<br>_64bit Amazon Linux 2 v5.2.0 running Node.js 12_ | 2.0.20200723 | 12.18.3 (6.14.6), 12.18.2 (6.14.5), 12.18.1 (6.14.5), 12.17.0 (6.14.4), 12.16.3 (6.14.4), 12.16.2 (6.14.4), 12.16.1 (6.13.4), 12.16.0 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 12.13.1 (6.12.1), 12.13.0 (6.12.0), 12.12.0 (6.11.3), 12.11.1 (6.11.3), 12.11.0 (6.11.3), 12.10.0 (6.10.3), 12.9.1 (6.10.2), 12.9.0 (6.10.2), 12.8.1 (6.10.2), 12.8.0 (6.10.2), 12.7.0 (6.10.0), 12.6.0 (6.9.0), 12.5.0 (6.9.0), 12.4.0 (6.9.0), 12.3.1 (6.9.0), 12.3.0 (6.9.0), 12.2.0 (6.9.0), 12.1.0 (6.9.0), 12.0.0 (6.9.0)<br>Default version: 12.18.3                                                                                                                                                                                                | nginx 1.18.0 (default), Apache 2.4.43 | 2.23.3 | 3.2.0     |
| **Node.js 10 AL2 version 5.2.0**<br>_64bit Amazon Linux 2 v5.2.0 running Node.js 10_ | 2.0.20200723 | 10.22.0 (6.14.6), 10.21.0 (6.14.4), 10.20.1 (6.14.4), 10.20.0 (6.14.4), 10.19.0 (6.13.4), 10.18.1 (6.13.4), 10.18.0 (6.13.4), 10.17.0 (6.11.3), 10.16.3 (6.13.4), 10.16.2 (6.9.0), 10.16.1 (6.9.0), 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.2 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.2 (6.4.1), 10.14.1 (6.4.1), 10.14.0 (6.4.1), 10.13.0 (6.4.1), 10.12.0 (6.4.1), 10.11.0 (6.4.1), 10.10.0 (6.4.1), 10.9.0 (6.2.0), 10.8.0 (6.2.0), 10.7.0 (6.1.0), 10.6.0 (6.1.0), 10.5.0 (6.1.0), 10.4.1 (6.1.0), 10.4.0 (6.1.0), 10.3.0 (6.1.0), 10.2.1 (5.6.0), 10.2.0 (5.6.0), 10.1.0 (5.6.0), 10.0.0 (5.6.0)<br>Default version: 10.22.0                                                                                                                       | nginx 1.18.0 (default), Apache 2.4.43 | 2.23.3 | 3.2.0     |
| **Node.js version 4.15.1**<br>_64bit Amazon Linux 2018.03 v4.15.1 running Node.js_   | 2018.03.0    | 12.18.3 (6.14.6), 12.18.2 (6.14.5), 12.18.1 (6.14.5), 12.18.0 (6.14.4), 12.16.3 (6.14.4), 12.16.2 (6.14.4), 12.16.1 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 10.22.0 (6.14.6), 10.21.0 (6.14.4), 10.20.1 (6.14.4), 10.20.0(6.14.4), 10.19.0 (6.13.4), 10.18.1 (6.13.4), 10.18.0 (6.13.4), 10.17.0 (6.11.3), 10.16.3 (6.9.0), 10.16.2 (6.9.0), 10.16.1 (6.9.0), 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.17.0 (6.13.4), 8.16.2 (6.4.1), 8.16.1 (6.4.1), 8.16.0 (6.4.1), 8.15.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.17.1 (3.10.10), 6.17.0 (3.10.10), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br>Default version: 12.18.3 | nginx 1.16.1, Apache 2.4.43           | 2.18.4 | 3.1.0     |

### PHP

| Platform Version and _Solution Stack Name_                                       | AMI          | Language   | Composer | Proxy Server                          |
| -------------------------------------------------------------------------------- | ------------ | ---------- | -------- | ------------------------------------- |
| **PHP 7.4 AL2 version 3.1.0**<br>_64bit Amazon Linux 2 v3.1.0 running PHP 7.4_   | 2.0.20200723 | PHP 7.4.7  | 1.9.3    | nginx 1.18.0 (default), Apache 2.4.43 |
| **PHP 7.3 AL2 version 3.1.0**<br>_64bit Amazon Linux 2 v3.1.0 running PHP 7.3_   | 2.0.20200723 | PHP 7.3.19 | 1.9.3    | nginx 1.18.0 (default), Apache 2.4.43 |
| **PHP 7.2 AL2 version 3.1.0**<br>_64bit Amazon Linux 2 v3.1.0 running PHP 7.2_   | 2.0.20200723 | PHP 7.2.31 | 1.9.3    | nginx 1.18.0 (default), Apache 2.4.43 |
| **PHP 7.3 version 2.9.9**<br>_64bit Amazon Linux 2018.03 v2.9.9 running PHP 7.3_ | 2018.03.0    | PHP 7.3.19 | 1.9.0    | Apache 2.4.43                         |
| **PHP 7.2 version 2.9.9**<br>_64bit Amazon Linux 2018.03 v2.9.9 running PHP 7.2_ | 2018.03.0    | PHP 7.2.31 | 1.9.0    | Apache 2.4.43                         |

### Python

| Platform Version and _Solution Stack Name_                                               | AMI          | Language      | Package Manager | Packager          | meld3       | AWS X‑Ray | Proxy Server                          |
| ---------------------------------------------------------------------------------------- | ------------ | ------------- | --------------- | ----------------- | ----------- | --------- | ------------------------------------- |
| **Python 3.7 AL2 version 3.1.0**<br>_64bit Amazon Linux 2 v3.1.0 running Python 3.7_     | 2.0.20200723 | Python 3.7.6  | pipenv 2020.6.2 |                   |             | 3.2.0     | nginx 1.18.0 (default), Apache 2.4.43 |
| **Python 3.6 version 2.9.13**<br>_64bit Amazon Linux 2018.03 v2.9.13 running Python 3.6_ | 2018.03.0    | Python 3.6.11 | pip 9.0.3       | setuptools 28.8.0 | meld3 1.0.2 | 3.1.0     | Apache 2.4.43 with mod_wsgi 3.5       |

### Ruby

| Platform Version and _Solution Stack Name_                                                                                 | AMI          | Language         | Package Manager | Application Server | AWS X‑Ray | Proxy Server |
| -------------------------------------------------------------------------------------------------------------------------- | ------------ | ---------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 2.7 AL2 version 3.1.0**<br>_64bit Amazon Linux 2 v3.1.0 running Ruby 2.7_                                           | 2.0.20200723 | Ruby 2.7.1-p83   | RubyGems 3.1.4  | Puma 4.3.5         | 3.2.0     | nginx 1.18.0 |
| **Ruby 2.6 AL2 version 3.1.0**<br>_64bit Amazon Linux 2 v3.1.0 running Ruby 2.6_                                           | 2.0.20200723 | Ruby 2.6.6-p146  | RubyGems 3.1.4  | Puma 4.3.5         | 3.2.0     | nginx 1.18.0 |
| **Ruby 2.5 AL2 version 3.1.0**<br>_64bit Amazon Linux 2 v3.1.0 running Ruby 2.5_                                           | 2.0.20200723 | Ruby 2.5.8-p224  | RubyGems 3.1.4  | Puma 4.3.5         | 3.2.0     | nginx 1.18.0 |
| **Ruby 2.6 with Puma version 2.11.9**<br>_64bit Amazon Linux 2018.03 v2.11.9 running Ruby 2.6 (Puma)_                      | 2018.03.0    | Ruby 2.6.6-p146  | RubyGems 3.1.2  | Puma 2.16.0        | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.6 with Passenger version 2.11.9**<br>_64bit Amazon Linux 2018.03 v2.11.9 running Ruby 2.6 (Passenger Standalone)_ | 2018.03.0    | Ruby 2.6.6-p146  | RubyGems 3.1.2  | Passenger 4.0.60   | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.5 with Puma version 2.11.9**<br>_64bit Amazon Linux 2018.03 v2.11.9 running Ruby 2.5 (Puma)_                      | 2018.03.0    | Ruby 2.5.8-p224  | RubyGems 3.1.2  | Puma 2.16.0        | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.5 with Passenger version 2.11.9**<br>_64bit Amazon Linux 2018.03 v2.11.9 running Ruby 2.5 (Passenger Standalone)_ | 2018.03.0    | Ruby 2.5.8-p224  | RubyGems 3.1.2  | Passenger 4.0.60   | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.4 with Puma version 2.11.9**<br>_64bit Amazon Linux 2018.03 v2.11.9 running Ruby 2.4 (Puma)_                      | 2018.03.0    | Ruby 2.4.10-p364 | RubyGems 3.1.2  | Puma 2.16.0        | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.4 with Passenger version 2.11.9**<br>_64bit Amazon Linux 2018.03 v2.11.9 running Ruby 2.4 (Passenger Standalone)_ | 2018.03.0    | Ruby 2.4.10-p364 | RubyGems 3.1.2  | Passenger 4.0.60   | 3.1.0     | nginx 1.16.1 |
