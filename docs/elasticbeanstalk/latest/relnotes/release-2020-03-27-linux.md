# Release: Elastic Beanstalk Linux-based platform updates on March 27, 2020

This release provides new Linux-based platform versions for AWS Elastic Beanstalk. The release includes security updates.
It also includes Multicontainer Docker, Go, Java SE, Tomcat, PHP, and Python updates.

**Release date:** March 27, 2020

## Changes

The following table lists the changes included in this release.

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- | --------------- | ---- | ------- | ------- | ---- | ------------------------------ | ---------------------------------------- | ---- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/ "https://alas.aws.amazon.com/") on or before **March 18, 2020\*<br>• to all Linux-based platforms.<br>The **PHP*<br>• release includes security fixes. For more information, see \*\*Platform-specific<br>updates*<br>• in this table. |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                                                        | \*_Platform_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Multicontainer Docker_<br>• | Updated the ECS agent to version 1.37.0. | <br> | \*_Go_<br>• | Updated Go to release 1.14.1. For details, see [go1.14](https://golang.org/doc/devel/release.html#go1.14 "https://golang.org/doc/devel/release.html#go1.14") in<br>_The Go Programming Language Release History_. | <br> | **Java SE**, \*_Tomcat_<br>• | Updated Java 8 to OpenJDK Version 1.8.0.242.b08.<br>Updated Java 7 to OpenJDK Version 1.7.0.251.<br>Updated Tomcat 8.5 to [Tomcat<br>8.5.51](<https://tomcat.apache.org/tomcat-8.5-doc/changelog.html#Tomcat_8.5.51_(markt)> "https://tomcat.apache.org/tomcat-8.5-doc/changelog.html#Tomcat_8.5.51_(markt)").<br>Updated Tomcat 7 to [Tomcat<br>7.0.100](<https://tomcat.apache.org/tomcat-7.0-doc/changelog.html#Tomcat_7.0.100_(violetagg)> "https://tomcat.apache.org/tomcat-7.0-doc/changelog.html#Tomcat_7.0.100_(violetagg)"). | <br> | \*_PHP_<br>• | Updated PHP 7.3 and 7.2 to releases<br>[7.3.15](https://www.php.net/releases/7_3_15.php "https://www.php.net/releases/7_3_15.php") and<br>[7.2.28](https://www.php.net/releases/7_2_28.php "https://www.php.net/releases/7_2_28.php"), respectively.<br>These versions include security fixes. | <br> | \*_Python_<br>• | Updated Python 3.6 to [Python<br>3.6.10](https://docs.python.org/3.6/whatsnew/changelog.html#python-3-6-10-final "https://docs.python.org/3.6/whatsnew/changelog.html#python-3-6-10-final"). |     |

## New platform versions

###### These platforms are updated:

- [Single Container Docker](#release-2020-03-27-linux.platforms.docker "#release-2020-03-27-linux.platforms.docker")
- [Multicontainer Docker](#release-2020-03-27-linux.platforms.mcdocker "#release-2020-03-27-linux.platforms.mcdocker")
- [Preconfigured Docker](#release-2020-03-27-linux.platforms.dockerpreconfig "#release-2020-03-27-linux.platforms.dockerpreconfig")
- [Go](#release-2020-03-27-linux.platforms.go "#release-2020-03-27-linux.platforms.go")
- [Java SE](#release-2020-03-27-linux.platforms.javase "#release-2020-03-27-linux.platforms.javase")
- [Tomcat](#release-2020-03-27-linux.platforms.java "#release-2020-03-27-linux.platforms.java")
- [Node.js](#release-2020-03-27-linux.platforms.nodejs "#release-2020-03-27-linux.platforms.nodejs")
- [PHP](#release-2020-03-27-linux.platforms.PHP "#release-2020-03-27-linux.platforms.PHP")
- [Python](#release-2020-03-27-linux.platforms.python "#release-2020-03-27-linux.platforms.python")
- [Ruby](#release-2020-03-27-linux.platforms.ruby "#release-2020-03-27-linux.platforms.ruby")

### Single Container Docker

| Platform Version and _Solution Stack Name_                                                                         | AMI       | Docker Version | Proxy Server |
| ------------------------------------------------------------------------------------------------------------------ | --------- | -------------- | ------------ |
| **Single Container Docker 18.09 version 2.14.3**<br>_64bit Amazon Linux 2018.03 v2.14.3 running Docker 18.09.9-ce_ | 2018.03.0 | 18.09.9-ce     | nginx 1.16.1 |

### Multicontainer Docker

| Platform Version and _Solution Stack Name_                                                                                                 | AMI       | Docker Version | ECS Agent |
| ------------------------------------------------------------------------------------------------------------------------------------------ | --------- | -------------- | --------- |
| **Multicontainer Docker 18.09 version 2.20.0**<br>_64bit Amazon Linux 2018.03 v2.20.0 running Multi-container Docker 18.09.9-ce (Generic)_ | 2018.03.0 | 18.09.9-ce     | 1.37.0    |

### Preconfigured Docker

| Platform Version and _Solution Stack Name_                                                                                         | AMI       | Platform          | Container OS         | Language | Proxy Server | Application Server | Docker Image                                  |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------- | -------------------- | -------- | ------------ | ------------------ | --------------------------------------------- |
| **Glassfish 5.0 (Docker) version 2.14.3**<br>_64bit Amazon Linux v2.14.3 running GlassFish 5.0 Java 8 (Preconfigured<br>• Docker)_ | 2018.03.0 | Docker 18.09.9-ce | Amazon Linux 2018.03 | Java 8   | nginx 1.16.1 | Glassfish 5.0      | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 |

### Go

| Platform Version and _Solution Stack Name_                                           | AMI       | Language  | AWS X‑Ray | Proxy Server |
| ------------------------------------------------------------------------------------ | --------- | --------- | --------- | ------------ |
| **Go 1.14 version 2.15.1**<br>_64bit Amazon Linux 2018.03 v2.15.1 running Go 1.14.1_ | 2018.03.0 | Go 1.14.1 | 3.1.0     | nginx 1.16.1 |

### Java SE

| Platform Version and _Solution Stack Name_                                       | AMI       | Language       | Tools                              | AWS X‑Ray | Proxy Server |
| -------------------------------------------------------------------------------- | --------- | -------------- | ---------------------------------- | --------- | ------------ |
| **Java 8 version 2.10.4**<br>_64bit Amazon Linux 2018.03 v2.10.4 running Java 8_ | 2018.03.0 | Java 1.8.0_242 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0     | nginx 1.16.1 |
| **Java 7 version 2.10.4**<br>_64bit Amazon Linux 2018.03 v2.10.4 running Java 7_ | 2018.03.0 | Java 1.7.0_251 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0     | nginx 1.16.1 |

### Tomcat

| Platform Version and _Solution Stack Name_                                                                | AMI       | Language       | AWS X‑Ray | Application Server | Proxy Server                                         |
| --------------------------------------------------------------------------------------------------------- | --------- | -------------- | --------- | ------------------ | ---------------------------------------------------- |
| **Java 8 with Tomcat 8.5 version 3.3.4**<br>_64bit Amazon Linux 2018.03 v3.3.4 running Tomcat 8.5 Java 8_ | 2018.03.0 | Java 1.8.0_242 | 3.1.0     | Tomcat 8.5.51      | Apache 2.4.41 (default), Apache 2.2.34, Nginx 1.16.1 |
| **Java 7 with Tomcat 7 version 3.3.4**<br>_64bit Amazon Linux 2018.03 v3.3.4 running Tomcat 7 Java 7_     | 2018.03.0 | Java 1.7.0_251 | 3.1.0     | Tomcat 7.0.100     | Apache 2.4.41 (default), Apache 2.2.34, Nginx 1.16.1 |

### Node.js

| Platform Version and _Solution Stack Name_                                         | AMI       | Node.js versions (npm versions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Proxy Server                | Git    | AWS X‑Ray |
| ---------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------ | --------- |
| **Node.js version 4.14.1**<br>_64bit Amazon Linux 2018.03 v4.14.1 running Node.js_ | 2018.03.0 | 12.16.1 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 10.19.0 (6.13.4), 10.18.1 (6.13.4), 10.18.0 (6.13.4), 10.17.0 (6.11.3), 10.16.3 (6.9.0), 10.16.2 (6.9.0), 10.16.1 (6.9.0), 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.17.0 (6.13.4), 8.16.2 (6.4.1), 8.16.1 (6.4.1), 8.16.0 (6.4.1), 8.15.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.17.1 (3.10.10), 6.17.0 (3.10.10), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br>Default version: 12.16.1 | nginx 1.16.1, Apache 2.4.41 | 2.14.5 | 3.1.0     |

### PHP

| Platform Version and _Solution Stack Name_                                       | AMI       | Language   | Composer | Proxy Server  |
| -------------------------------------------------------------------------------- | --------- | ---------- | -------- | ------------- |
| **PHP 7.3 version 2.9.4**<br>_64bit Amazon Linux 2018.03 v2.9.4 running PHP 7.3_ | 2018.03.0 | PHP 7.3.15 | 1.9.0    | Apache 2.4.41 |
| **PHP 7.2 version 2.9.4**<br>_64bit Amazon Linux 2018.03 v2.9.4 running PHP 7.2_ | 2018.03.0 | PHP 7.2.28 | 1.9.0    | Apache 2.4.41 |

### Python

| Platform Version and _Solution Stack Name_                                             | AMI       | Language      | Package Manager | Packager          | meld3       | AWS X‑Ray | Proxy Server                    |
| -------------------------------------------------------------------------------------- | --------- | ------------- | --------------- | ----------------- | ----------- | --------- | ------------------------------- |
| **Python 3.6 version 2.9.7**<br>_64bit Amazon Linux 2018.03 v2.9.7 running Python 3.6_ | 2018.03.0 | Python 3.6.10 | pip 9.0.3       | setuptools 28.8.0 | meld3 1.0.2 | 3.1.0     | Apache 2.4.41 with mod_wsgi 3.5 |

### Ruby

| Platform Version and _Solution Stack Name_                                                                                 | AMI       | Language        | Package Manager | Application Server | AWS X‑Ray | Proxy Server |
| -------------------------------------------------------------------------------------------------------------------------- | --------- | --------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 2.6 with Puma version 2.11.4**<br>_64bit Amazon Linux 2018.03 v2.11.4 running Ruby 2.6 (Puma)_                      | 2018.03.0 | Ruby 2.6.5-p62  | RubyGems 2.7.9  | Puma 2.16.0        | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.6 with Passenger version 2.11.4**<br>_64bit Amazon Linux 2018.03 v2.11.4 running Ruby 2.6 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.6.5-p62  | RubyGems 2.7.9  | Passenger 4.0.60   | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.5 with Puma version 2.11.4**<br>_64bit Amazon Linux 2018.03 v2.11.4 running Ruby 2.5 (Puma)_                      | 2018.03.0 | Ruby 2.5.7-p157 | RubyGems 2.7.9  | Puma 2.16.0        | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.5 with Passenger version 2.11.4**<br>_64bit Amazon Linux 2018.03 v2.11.4 running Ruby 2.5 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.5.7-p157 | RubyGems 2.7.9  | Passenger 4.0.60   | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.4 with Puma version 2.11.4**<br>_64bit Amazon Linux 2018.03 v2.11.4 running Ruby 2.4 (Puma)_                      | 2018.03.0 | Ruby 2.4.9-p354 | RubyGems 2.7.9  | Puma 2.16.0        | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.4 with Passenger version 2.11.4**<br>_64bit Amazon Linux 2018.03 v2.11.4 running Ruby 2.4 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.4.9-p354 | RubyGems 2.7.9  | Passenger 4.0.60   | 3.1.0     | nginx 1.16.1 |
