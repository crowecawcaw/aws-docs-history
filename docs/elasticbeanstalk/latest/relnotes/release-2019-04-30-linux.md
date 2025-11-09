# Release: Elastic Beanstalk Linux-based platform updates on April 30, 2019

This release provides new Linux-based platform versions for AWS Elastic Beanstalk. The release includes security updates.
It also includes Multicontainer Docker, Go, Node.js, PHP, and Ruby updates, an Apache update, and support for additional Amazon EC2 instance types in certain AWS Regions.

**Release date:** April 30, 2019

## Changes

###### Notes

- 2019-04-30 – At this time, the release doesn't include an update for the Node.js platform. We will update
  this platform soon and update the release notes.
- 2019-05-03 – We released the Node.js platform update. This release is now complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- | ---------------- | ---- | ------- | ------- | ---- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/ "https://alas.aws.amazon.com/") on or before April 19,<br>2019 to all Linux-based platforms.<br>The Apache, PHP, and Ruby 2.4.6 releases include security updates.                                                                                                                                                                                                                                                                                                                                       |
| **Cross-platform updates**    | Made these cross-platform updates:<br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | \*_Component_<br>•      | \*_Update_<br>•  | <br> | --<br>• | --<br>• | <br> | \*_Apache_<br>•                | Updated platforms supporting the Apache HTTP Server 2.4 to version 2.4.39. For details, see [Changes with Apache 2.4.x](https://downloads.apache.org/httpd/CHANGES_2.4 "https://downloads.apache.org/httpd/CHANGES_2.4") on the \*Apache Software<br>Foundation<br>• website. The release includes seven security updates. |      |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | \*_Platform_<br>•       | \*_Update_<br>•  | <br> | --<br>• | --<br>• | <br> | \*_Multicontainer Docker_<br>• | Updated the ECS agent to version 1.27.0.                                                                                                                                                                                                                                                                                   | <br> | \*_Go_<br>•   | Updated to minor revision 1.12.4. For details, see [go1.12](https://golang.org/doc/devel/release.html#go1.12 "https://golang.org/doc/devel/release.html#go1.12") in<br>_The Go Programming Language Release History_. | <br> | \*_Node.js_<br>• | Updated the Node.js platform to add support for Node versions [8.16.0](https://nodejs.org/en/blog/release/v8.16.0/ "https://nodejs.org/en/blog/release/v8.16.0/"), [6.17.1](https://nodejs.org/en/blog/release/v6.17.1/ "https://nodejs.org/en/blog/release/v6.17.1/"). | <br> | \*_PHP_<br>• | Released new PHP 7.2, 7.1, and 5.6 versions:<br>[7.2.17](https://www.php.net/releases/7_2_17.php "https://www.php.net/releases/7_2_17.php"),<br>[7.1.28](https://www.php.net/releases/7_1_28.php "https://www.php.net/releases/7_1_28.php"), and<br>[5.6.40](https://www.php.net/releases/5_6_40.php "https://www.php.net/releases/5_6_40.php"), respectively.<br>These releases include security updates. | <br> | \*_Ruby_<br>• | Released new Ruby 2.6 and 2.4 versions:<br>[2.6.3](https://www.ruby-lang.org/en/news/2019/04/17/ruby-2-6-3-released/ "https://www.ruby-lang.org/en/news/2019/04/17/ruby-2-6-3-released/") and<br>[2.4.6](https://www.ruby-lang.org/en/news/2019/04/01/ruby-2-4-6-released/ "https://www.ruby-lang.org/en/news/2019/04/01/ruby-2-4-6-released/"), respectively.<br>The Ruby 2.4.6 release includes security updates. |     |
| **Instance types**            | Added support for more Amazon EC2 instance types in some AWS Regions. In particular, we added support for the new M5ad and R5ad instances. They<br>add high-speed, low latency local (physically connected) block storage to the existing M5a and R5a instances. For more information, see [New AMD EPYC-Powered Amazon EC2 M5ad and R5ad<br>Instances](https://aws.amazon.com/blogs/aws/new-amd-epyc-powered-amazon-ec2-m5ad-and-r5ad-instances/ "https://aws.amazon.com/blogs/aws/new-amd-epyc-powered-amazon-ec2-m5ad-and-r5ad-instances/").<br>The added instance types are listed in the following table.<br> | \*_Instance types_<br>• | \*_Regions_<br>• | <br> | --<br>• | --<br>• | <br> | \*_m5ad_<br>•                  | • US East (Ohio) – us-east-2<br>• US West (Oregon) – us-west-2<br>• Asia Pacific (Singapore) – ap-southeast-1                                                                                                                                                                                                              | <br> | \*_r5ad_<br>• | • US East (Ohio) – us-east-2<br>• US East (N. Virginia) – us-east-1<br>• US West (Oregon) – us-west-2<br>• Asia Pacific (Singapore) – ap-southeast-1                                                                  | <br> | \*_z1d_<br>•     | • Asia Pacific (Sydney) – ap-southeast-2<br>• Europe (Frankfurt) – eu-central-1                                                                                                                                                                                         |      |

## New platform versions

###### These platforms are updated:

- [Packer Builder](#release-2019-04-30-linux.platforms.packer "#release-2019-04-30-linux.platforms.packer")
- [Single Container Docker](#release-2019-04-30-linux.platforms.docker "#release-2019-04-30-linux.platforms.docker")
- [Multicontainer Docker](#release-2019-04-30-linux.platforms.mcdocker "#release-2019-04-30-linux.platforms.mcdocker")
- [Preconfigured Docker](#release-2019-04-30-linux.platforms.dockerpreconfig "#release-2019-04-30-linux.platforms.dockerpreconfig")
- [Go](#release-2019-04-30-linux.platforms.go "#release-2019-04-30-linux.platforms.go")
- [Java SE](#release-2019-04-30-linux.platforms.javase "#release-2019-04-30-linux.platforms.javase")
- [Java with Tomcat](#release-2019-04-30-linux.platforms.java "#release-2019-04-30-linux.platforms.java")
- [Node.js](#release-2019-05-03-linux.platforms.nodejs "#release-2019-05-03-linux.platforms.nodejs")
- [PHP](#release-2019-04-30-linux.platforms.PHP "#release-2019-04-30-linux.platforms.PHP")
- [Python](#release-2019-04-30-linux.platforms.python "#release-2019-04-30-linux.platforms.python")
- [Ruby](#release-2019-04-30-linux.platforms.ruby "#release-2019-04-30-linux.platforms.ruby")

### Packer Builder

| Platform Version and _Solution Stack Name_                                                                     | AMI       | Packer Version |
| -------------------------------------------------------------------------------------------------------------- | --------- | -------------- |
| **Elastic Beanstalk Packer Builder version 2.6.9**<br>_64bit Amazon Linux 2018.03 v2.6.9 running Packer 1.0.3_ | 2018.03.0 | 1.0.3          |

### Single Container Docker

| Platform Version and _Solution Stack Name_                                                                           | AMI       | Docker Version | Proxy Server |
| -------------------------------------------------------------------------------------------------------------------- | --------- | -------------- | ------------ |
| **Single Container Docker 18.06 version 2.12.11**<br>_64bit Amazon Linux 2018.03 v2.12.11 running Docker 18.06.1-ce_ | 2018.03.0 | 18.06.1-ce     | nginx 1.14.1 |

### Multicontainer Docker

| Platform Version and _Solution Stack Name_                                                                                                 | AMI       | Docker Version | ECS Agent |
| ------------------------------------------------------------------------------------------------------------------------------------------ | --------- | -------------- | --------- |
| **Multicontainer Docker 18.06 version 2.13.0**<br>_64bit Amazon Linux 2018.03 v2.13.0 running Multi-container Docker 18.06.1-ce (Generic)_ | 2018.03.0 | 18.06.1-ce     | 1.27.0    |

### Preconfigured Docker

| Platform Version and _Solution Stack Name_                                                                                            | AMI       | Platform          | Container OS         | Language   | Proxy Server | Application Server | Docker Image                                  |
| ------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------- | -------------------- | ---------- | ------------ | ------------------ | --------------------------------------------- |
| **Glassfish 5.0 (Docker) version 2.12.11**<br>_64bit Amazon Linux v2.12.11 running GlassFish 5.0 Java 8 (Preconfigured<br>• Docker)_  | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8     | nginx 1.14.1 | Glassfish 5.0      | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 |
| **Go 1.4 (Docker) version 2.12.11**<br>_64bit Debian jessie v2.12.11 running Go 1.4 (Preconfigured<br>• Docker)_                      | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie        | Go 1.4.2   | nginx 1.14.1 | none               | golang:1.4.2-onbuild                          |
| **Go 1.3 (Docker) version 2.12.11**<br>_64bit Debian jessie v2.12.11 running Go 1.3 (Preconfigured<br>• Docker)_                      | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie        | Go 1.3.3   | nginx 1.14.1 | none               | golang:1.3.3-onbuild                          |
| **Python 3.4 with uWSGI 2 (Docker) version 2.12.11**<br>_64bit Debian jessie v2.12.11 running Python 3.4 (Preconfigured<br>• Docker)_ | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie        | Python 3.4 | nginx 1.14.1 | uWSGI 2.0.8        | amazon/aws-eb-python:3.4.2-onbuild-3.5.1      |

### Go

| Platform Version and _Solution Stack Name_                                           | AMI       | Language  | AWS X‑Ray | Proxy Server |
| ------------------------------------------------------------------------------------ | --------- | --------- | --------- | ------------ |
| **Go 1.12 version 2.11.1**<br>_64bit Amazon Linux 2018.03 v2.11.1 running Go 1.12.4_ | 2018.03.0 | Go 1.12.4 | 3.0.0     | nginx 1.14.1 |

### Java SE

| Platform Version and _Solution Stack Name_                                     | AMI       | Language       | Tools                              | AWS X‑Ray | Proxy Server |
| ------------------------------------------------------------------------------ | --------- | -------------- | ---------------------------------- | --------- | ------------ |
| **Java 8 version 2.8.3**<br>_64bit Amazon Linux 2018.03 v2.8.3 running Java 8_ | 2018.03.0 | Java 1.8.0_201 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.0.0     | nginx 1.14.1 |
| **Java 7 version 2.8.3**<br>_64bit Amazon Linux 2018.03 v2.8.3 running Java 7_ | 2018.03.0 | Java 1.7.0_211 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.0.0     | nginx 1.14.1 |

### Java with Tomcat

| Platform Version and _Solution Stack Name_                                                                | AMI       | Language       | AWS X‑Ray | Application Server | Proxy Server                                         |
| --------------------------------------------------------------------------------------------------------- | --------- | -------------- | --------- | ------------------ | ---------------------------------------------------- |
| **Java 8 with Tomcat 8.5 version 3.1.3**<br>_64bit Amazon Linux 2018.03 v3.1.3 running Tomcat 8.5 Java 8_ | 2018.03.0 | Java 1.8.0_201 | 3.0.0     | Tomcat 8.5.32      | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 |
| **Java 8 with Tomcat 8 version 3.1.3**<br>_64bit Amazon Linux 2018.03 v3.1.3 running Tomcat 8 Java 8_     | 2018.03.0 | Java 1.8.0_201 | 3.0.0     | Tomcat 8.0.53      | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 |
| **Java 7 with Tomcat 7 version 3.1.3**<br>_64bit Amazon Linux 2018.03 v3.1.3 running Tomcat 7 Java 7_     | 2018.03.0 | Java 1.7.0_211 | 3.0.0     | Tomcat 7.0.91      | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 |
| **Java 6 with Tomcat 7 version 3.1.3**<br>_64bit Amazon Linux 2018.03 v3.1.3 running Tomcat 7 Java 6_     | 2018.03.0 | Java 1.6.0_41  | 3.0.0     | Tomcat 7.0.91      | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 |

### Node.js

| Platform Version and _Solution Stack Name_                                       | AMI       | Node.js versions (npm versions)                                                                                                                                                                                                                                                                           | Proxy Server                | Git    | AWS X‑Ray |
| -------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------ | --------- |
| **Node.js version 4.8.3**<br>_64bit Amazon Linux 2018.03 v4.8.3 running Node.js_ | 2018.03.0 | 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.16.0 (6.4.1), 8.15.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.17.1 (3.10.10), 6.17.0 (3.10.10), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br>Default platform: 10.15.3 | nginx 1.14.1, Apache 2.4.39 | 2.14.5 | 3.0.0     |

### PHP

| Platform Version and _Solution Stack Name_                                       | AMI       | Language   | Composer | Proxy Server  |
| -------------------------------------------------------------------------------- | --------- | ---------- | -------- | ------------- |
| **PHP 7.2 version 2.8.9**<br>_64bit Amazon Linux 2018.03 v2.8.9 running PHP 7.2_ | 2018.03.0 | PHP 7.2.17 | 1.4.2    | Apache 2.4.39 |
| **PHP 7.1 version 2.8.9**<br>_64bit Amazon Linux 2018.03 v2.8.9 running PHP 7.1_ | 2018.03.0 | PHP 7.1.28 | 1.4.2    | Apache 2.4.39 |
| **PHP 7.0 version 2.8.9**<br>_64bit Amazon Linux 2018.03 v2.8.9 running PHP 7.0_ | 2018.03.0 | PHP 7.0.33 | 1.4.2    | Apache 2.4.39 |
| **PHP 5.6 version 2.8.9**<br>_64bit Amazon Linux 2018.03 v2.8.9 running PHP 5.6_ | 2018.03.0 | PHP 5.6.40 | 1.4.2    | Apache 2.4.39 |
| **PHP 5.5 version 2.8.9**<br>_64bit Amazon Linux 2018.03 v2.8.9 running PHP 5.5_ | 2018.03.0 | PHP 5.5.38 | 1.4.2    | Apache 2.4.39 |
| **PHP 5.4 version 2.8.9**<br>_64bit Amazon Linux 2018.03 v2.8.9 running PHP 5.4_ | 2018.03.0 | PHP 5.4.45 | 1.4.2    | Apache 2.4.39 |

### Python

| Platform Version and _Solution Stack Name_                                             | AMI       | Language      | Package Manager | Packager          | meld3       | AWS X‑Ray | Proxy Server                    |
| -------------------------------------------------------------------------------------- | --------- | ------------- | --------------- | ----------------- | ----------- | --------- | ------------------------------- |
| **Python 3.6 version 2.8.3**<br>_64bit Amazon Linux 2018.03 v2.8.3 running Python 3.6_ | 2018.03.0 | Python 3.6.8  | pip 9.0.3       | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0     | Apache 2.4.39 with mod_wsgi 3.5 |
| **Python 3.4 version 2.8.3**<br>_64bit Amazon Linux 2018.03 v2.8.3 running Python 3.4_ | 2018.03.0 | Python 3.4.9  | pip 9.0.3       | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0     | Apache 2.4.39 with mod_wsgi 3.5 |
| **Python 2.7 version 2.8.3**<br>_64bit Amazon Linux 2018.03 v2.8.3 running Python 2.7_ | 2018.03.0 | Python 2.7.16 | pip 9.0.3       | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0     | Apache 2.4.39 with mod_wsgi 3.5 |
| **Python 2.6 version 2.8.3**<br>_64bit Amazon Linux 2018.03 v2.8.3 running Python 2.6_ | 2018.03.0 | Python 2.6.9  | pip 9.0.3       | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0     | Apache 2.4.39 with mod_wsgi 3.5 |

### Ruby

| Platform Version and _Solution Stack Name_                                                                               | AMI       | Language         | Package Manager | Application Server | AWS X‑Ray | Proxy Server |
| ------------------------------------------------------------------------------------------------------------------------ | --------- | ---------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 2.6 with Puma version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.6 (Puma)_                      | 2018.03.0 | Ruby 2.6.3-p62   | RubyGems 2.7.9  | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.6 with Passenger version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.6 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.6.3-p62   | RubyGems 2.7.9  | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.5 with Puma version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.5 (Puma)_                      | 2018.03.0 | Ruby 2.5.5-p157  | RubyGems 2.7.9  | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.5 with Passenger version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.5 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.5.5-p157  | RubyGems 2.7.9  | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.4 with Puma version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.4 (Puma)_                      | 2018.03.0 | Ruby 2.4.6-p354  | RubyGems 2.7.9  | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.4 with Passenger version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.4 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.4.6-p354  | RubyGems 2.7.9  | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.3 with Puma version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.3 (Puma)_                      | 2018.03.0 | Ruby 2.3.8-p459  | RubyGems 2.7.7  | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.3 with Passenger version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.3 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.3.8-p459  | RubyGems 2.7.7  | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.2 with Puma version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.2 (Puma)_                      | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6  | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.2 with Passenger version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.2 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6  | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.1 with Puma version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.1 (Puma)_                      | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.1 with Passenger version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.1 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.0 with Puma version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.0 (Puma)_                      | 2018.03.0 | Ruby 2.0.0-p648  | RubyGems 2.6.13 | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.0 with Passenger version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.0 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.0.0-p648  | RubyGems 2.6.13 | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 1.9 with Passenger version 2.9.3**<br>_64bit Amazon Linux 2018.03 v2.9.3 running Ruby 1.9.3_                      | 2018.03.0 | Ruby 1.9.3-p551  | RubyGems 2.6.13 | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
