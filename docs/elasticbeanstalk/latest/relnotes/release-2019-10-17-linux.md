# Release: Elastic Beanstalk Linux-based platform updates on October 17, 2019

This release provides new Linux-based platform versions for AWS Elastic Beanstalk. The release includes security updates.
It also includes Multicontainer Docker, Go, Node.js, PHP, and Ruby updates and an nginx update.

**Release date:** October 17, 2019

## Changes

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | --------------- | ---- | ------- | ------- | ---- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/ "https://alas.aws.amazon.com/") on or before **October 9, 2019\*<br>• to all Linux-based platforms.<br>The **nginx*<br>• release includes security fixes. For more information, see \*\*Cross-platform<br>updates*<br>• in this table.<br>The **Ruby\*<br>• release includes security fixes. For more information, see **Platform-specific<br>updates\*<br>• in this table. |
| **Cross-platform updates**    | Made these cross-platform updates:<br>                                                                                                                                                                                                                                                                                                                                                                                                                                                | \*_Component_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_nginx_<br>•                 | Updated platforms supporting the nginx server to [version 1.16.1](https://nginx.org/en/CHANGES-1.16 "https://nginx.org/en/CHANGES-1.16").<br>This version includes security fixes. |      |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                                                                                                                                                                                             | \*_Platform_<br>•  | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Multicontainer Docker_<br>• | Updated the ECS agent to version 1.32.0.                                                                                                                                           | <br> | \*_Go_<br>• | Updated to Go release 1.13.1. For details, see [go1.13](https://golang.org/doc/devel/release.html#go1.13 "https://golang.org/doc/devel/release.html#go1.13") in<br>_The Go Programming Language Release History_. | <br> | \*_Node.js_<br>• | Updated the Node.js platform to add support for Node version<br>[8.16.2](https://nodejs.org/en/blog/release/v8.16.2/ "https://nodejs.org/en/blog/release/v8.16.2/"). | <br> | \*_PHP_<br>• | Added support for PHP 7.3. For migration information, see [Migrating<br>from PHP 7.2.x to PHP 7.3.x](https://www.php.net/manual/en/migration73.php "https://www.php.net/manual/en/migration73.php") in the _PHP Manual_. PHP 7.3 is released side-by-side with PHP 7.2, which is<br>still supported.<br>NoteSome PECL packages for PHP 7.3 aren't available in the Amazon Linux repository. Therefore, they aren't included in our platform. If your<br>application depends on them, you'll need to add commands to install them. | <br> | \*_Ruby_<br>• | Released new Ruby 2.6, 2.5, and 2.4 versions:<br>[2.6.5](https://www.ruby-lang.org/en/news/2019/10/01/ruby-2-6-5-released/ "https://www.ruby-lang.org/en/news/2019/10/01/ruby-2-6-5-released/"),<br>[2.5.7](https://www.ruby-lang.org/en/news/2019/10/01/ruby-2-5-7-released/ "https://www.ruby-lang.org/en/news/2019/10/01/ruby-2-5-7-released/"), and<br>[2.4.9](https://www.ruby-lang.org/en/news/2019/10/02/ruby-2-4-9-released/ "https://www.ruby-lang.org/en/news/2019/10/02/ruby-2-4-9-released/"), respectively.<br>These versions include security fixes. |     |

## New platform versions

###### These platforms are updated:

- [Packer Builder](#release-2019-10-17-linux.platforms.packer "#release-2019-10-17-linux.platforms.packer")
- [Single Container Docker](#release-2019-10-17-linux.platforms.docker "#release-2019-10-17-linux.platforms.docker")
- [Multicontainer Docker](#release-2019-10-17-linux.platforms.mcdocker "#release-2019-10-17-linux.platforms.mcdocker")
- [Preconfigured Docker](#release-2019-10-17-linux.platforms.dockerpreconfig "#release-2019-10-17-linux.platforms.dockerpreconfig")
- [Go](#release-2019-10-17-linux.platforms.go "#release-2019-10-17-linux.platforms.go")
- [Java SE](#release-2019-10-17-linux.platforms.javase "#release-2019-10-17-linux.platforms.javase")
- [Java with Tomcat](#release-2019-10-17-linux.platforms.java "#release-2019-10-17-linux.platforms.java")
- [Node.js](#release-2019-10-17-linux.platforms.nodejs "#release-2019-10-17-linux.platforms.nodejs")
- [PHP](#release-2019-10-17-linux.platforms.PHP "#release-2019-10-17-linux.platforms.PHP")
- [Python](#release-2019-10-17-linux.platforms.python "#release-2019-10-17-linux.platforms.python")
- [Ruby](#release-2019-10-17-linux.platforms.ruby "#release-2019-10-17-linux.platforms.ruby")

### Packer Builder

| Platform Version and _Solution Stack Name_                                                                       | AMI       | Packer Version |
| ---------------------------------------------------------------------------------------------------------------- | --------- | -------------- |
| **Elastic Beanstalk Packer Builder version 2.6.16**<br>_64bit Amazon Linux 2018.03 v2.6.16 running Packer 1.0.3_ | 2018.03.0 | 1.0.3          |

### Single Container Docker

| Platform Version and _Solution Stack Name_                                                                         | AMI       | Docker Version | Proxy Server |
| ------------------------------------------------------------------------------------------------------------------ | --------- | -------------- | ------------ |
| **Single Container Docker 18.06 version 2.13.0**<br>_64bit Amazon Linux 2018.03 v2.13.0 running Docker 18.06.1-ce_ | 2018.03.0 | 18.06.1-ce     | nginx 1.16.1 |

### Multicontainer Docker

| Platform Version and _Solution Stack Name_                                                                                                 | AMI       | Docker Version | ECS Agent |
| ------------------------------------------------------------------------------------------------------------------------------------------ | --------- | -------------- | --------- |
| **Multicontainer Docker 18.06 version 2.17.0**<br>_64bit Amazon Linux 2018.03 v2.17.0 running Multi-container Docker 18.06.1-ce (Generic)_ | 2018.03.0 | 18.06.1-ce     | 1.32.0    |

### Preconfigured Docker

| Platform Version and _Solution Stack Name_                                                                                         | AMI       | Platform          | Container OS         | Language | Proxy Server | Application Server | Docker Image                                  |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------- | -------------------- | -------- | ------------ | ------------------ | --------------------------------------------- |
| **Glassfish 5.0 (Docker) version 2.13.0**<br>_64bit Amazon Linux v2.13.0 running GlassFish 5.0 Java 8 (Preconfigured<br>• Docker)_ | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8   | nginx 1.16.1 | Glassfish 5.0      | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 |

### Go

| Platform Version and _Solution Stack Name_                                           | AMI       | Language  | AWS X‑Ray | Proxy Server |
| ------------------------------------------------------------------------------------ | --------- | --------- | --------- | ------------ |
| **Go 1.13 version 2.14.0**<br>_64bit Amazon Linux 2018.03 v2.14.0 running Go 1.13.1_ | 2018.03.0 | Go 1.13.1 | 3.1.0     | nginx 1.16.1 |

### Java SE

| Platform Version and _Solution Stack Name_                                       | AMI       | Language       | Tools                              | AWS X‑Ray | Proxy Server |
| -------------------------------------------------------------------------------- | --------- | -------------- | ---------------------------------- | --------- | ------------ |
| **Java 8 version 2.10.0**<br>_64bit Amazon Linux 2018.03 v2.10.0 running Java 8_ | 2018.03.0 | Java 1.8.0_222 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0     | nginx 1.16.1 |
| **Java 7 version 2.10.0**<br>_64bit Amazon Linux 2018.03 v2.10.0 running Java 7_ | 2018.03.0 | Java 1.7.0_231 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0     | nginx 1.16.1 |

### Java with Tomcat

| Platform Version and _Solution Stack Name_                                                                | AMI       | Language       | AWS X‑Ray | Application Server | Proxy Server                                         |
| --------------------------------------------------------------------------------------------------------- | --------- | -------------- | --------- | ------------------ | ---------------------------------------------------- |
| **Java 8 with Tomcat 8.5 version 3.3.0**<br>_64bit Amazon Linux 2018.03 v3.3.0 running Tomcat 8.5 Java 8_ | 2018.03.0 | Java 1.8.0_222 | 3.1.0     | Tomcat 8.5.42      | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.16.1 |
| **Java 7 with Tomcat 7 version 3.3.0**<br>_64bit Amazon Linux 2018.03 v3.3.0 running Tomcat 7 Java 7_     | 2018.03.0 | Java 1.7.0_231 | 3.1.0     | Tomcat 7.0.94      | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.16.1 |

### Node.js

| Platform Version and _Solution Stack Name_                                         | AMI       | Node.js versions (npm versions)                                                                                                                                                                                                                                                                                                                                                                              | Proxy Server                | Git    | AWS X‑Ray |
| ---------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | ------ | --------- |
| **Node.js version 4.11.0**<br>_64bit Amazon Linux 2018.03 v4.11.0 running Node.js_ | 2018.03.0 | 10.16.3 (6.9.0), 10.16.2 (6.9.0), 10.16.1 (6.9.0), 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.16.2 (6.4.1), 8.16.1 (6.4.1), 8.16.0 (6.4.1), 8.15.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.17.1 (3.10.10), 6.17.0 (3.10.10), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br>Default version: 10.16.3 | nginx 1.16.1, Apache 2.4.39 | 2.14.5 | 3.1.0     |

### PHP

| Platform Version and _Solution Stack Name_                                       | AMI       | Language   | Composer | Proxy Server  |
| -------------------------------------------------------------------------------- | --------- | ---------- | -------- | ------------- |
| **PHP 7.3 version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running PHP 7.3_ | 2018.03.0 | PHP 7.3.9  | 1.4.2    | Apache 2.4.39 |
| **PHP 7.2 version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running PHP 7.2_ | 2018.03.0 | PHP 7.2.22 | 1.4.2    | Apache 2.4.39 |

### Python

| Platform Version and _Solution Stack Name_                                             | AMI       | Language     | Package Manager | Packager          | meld3       | AWS X‑Ray | Proxy Server                    |
| -------------------------------------------------------------------------------------- | --------- | ------------ | --------------- | ----------------- | ----------- | --------- | ------------------------------- |
| **Python 3.6 version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Python 3.6_ | 2018.03.0 | Python 3.6.8 | pip 9.0.3       | setuptools 28.8.0 | meld3 1.0.2 | 3.1.0     | Apache 2.4.39 with mod_wsgi 3.5 |

### Ruby

| Platform Version and _Solution Stack Name_                                                                                 | AMI       | Language        | Package Manager | Application Server | AWS X‑Ray | Proxy Server |
| -------------------------------------------------------------------------------------------------------------------------- | --------- | --------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 2.6 with Puma version 2.11.0**<br>_64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.6 (Puma)_                      | 2018.03.0 | Ruby 2.6.5-p114 | RubyGems 3.0.3  | Puma 2.16.0        | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.6 with Passenger version 2.11.0**<br>_64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.6 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.6.5-p114 | RubyGems 3.0.3  | Passenger 4.0.60   | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.5 with Puma version 2.11.0**<br>_64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.5 (Puma)_                      | 2018.03.0 | Ruby 2.5.7-p206 | RubyGems 2.7.9  | Puma 2.16.0        | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.5 with Passenger version 2.11.0**<br>_64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.5 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.5.7-p206 | RubyGems 2.7.9  | Passenger 4.0.60   | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.4 with Puma version 2.11.0**<br>_64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.4 (Puma)_                      | 2018.03.0 | Ruby 2.4.9-p362 | RubyGems 2.7.9  | Puma 2.16.0        | 3.1.0     | nginx 1.16.1 |
| **Ruby 2.4 with Passenger version 2.11.0**<br>_64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.4 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.4.9-p362 | RubyGems 2.7.9  | Passenger 4.0.60   | 3.1.0     | nginx 1.16.1 |
