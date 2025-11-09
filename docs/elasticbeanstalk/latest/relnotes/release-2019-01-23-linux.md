# Release: Elastic Beanstalk Linux-based platform updates on January 23, 2019

This release applies security updates to Linux-based platforms for AWS Elastic Beanstalk, and updates platform configurations.
The release includes Node.js, PHP, Python, and Ruby updates, some cross-platform updates, and, for certain AWS Regions, support for additional Amazon EC2 instance types.

**Release date:** January 23, 2019

## Changes

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ---------------- | ---- | ------- | ------- | ---- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/ "https://alas.aws.amazon.com/") on or before January 12,<br>2019 to all Linux-based platforms.<br>See also the **nginx\*<br>• entry in **Cross-platform updates\*<br>• for nginx security<br>updates. |
| **Cross-platform updates**    | Made these cross-platform updates:<br>                                                                                                                                                                                                                                                                          | \*_Component_<br>•     | \*_Update_<br>•  | <br> | --<br>• | --<br>• | <br> | \*_Apache_<br>•                | Updated platforms supporting the Apache HTTP Server 2.4 to version 2.4.37. For details, see [Changes with Apache 2.4.x](https://downloads.apache.org/httpd/CHANGES_2.4 "https://downloads.apache.org/httpd/CHANGES_2.4") on the \*Apache Software<br>Foundation<br>• website. | <br> | \*_nginx_<br>•        | Updated platforms supporting the nginx server to [version 1.14.1](https://nginx.org/en/CHANGES-1.14 "https://nginx.org/en/CHANGES-1.14").<br>This version includes these security updates:<br>• [CVE-2018-16843](https://nvd.nist.gov/vuln/detail/CVE-2018-16843 "https://nvd.nist.gov/vuln/detail/CVE-2018-16843")<br>• [CVE-2018-16844](https://nvd.nist.gov/vuln/detail/CVE-2018-16844 "https://nvd.nist.gov/vuln/detail/CVE-2018-16844")<br>• [CVE-2018-16845](https://nvd.nist.gov/vuln/detail/CVE-2018-16845 "https://nvd.nist.gov/vuln/detail/CVE-2018-16845") | <br> | \*_AWS X-Ray_<br>• | Updated platforms that support X-Ray to [X-Ray daemon v3.0.0](https://aws.amazon.com/releasenotes/2018-08-28-aws-x-ray-supports-sampling-rules/?tag=releasenotes%23keywords%23aws-x-ray "https://aws.amazon.com/releasenotes/2018-08-28-aws-x-ray-supports-sampling-rules/?tag=releasenotes%23keywords%23aws-x-ray").                                                                                                                                                                                                                           |      |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                       | \*_Platform_<br>•      | \*_Update_<br>•  | <br> | --<br>• | --<br>• | <br> | \*_Multicontainer Docker_<br>• | Updated the ECS agent to version 1.24.0.                                                                                                                                                                                                                                      | <br> | \*_Node.js_<br>•      | Updated the Node.js platform to add support for Node versions<br>[10.15.0](https://nodejs.org/en/blog/release/v10.15.0/ "https://nodejs.org/en/blog/release/v10.15.0/"),<br>[8.15.0](https://nodejs.org/en/blog/release/v8.15.0/ "https://nodejs.org/en/blog/release/v8.15.0/"), and<br>[6.16.0](https://nodejs.org/en/blog/release/v6.16.0/ "https://nodejs.org/en/blog/release/v6.16.0/").                                                                                                                                                                          | <br> | \*_PHP_<br>•       | Updated the PHP 7.2, 7.1, 7.0, and 5.6 configurations to PHP versions<br>[7.2.13](http://php.net/archive/2018.php#id2018-12-06-3 "http://php.net/archive/2018.php#id2018-12-06-3"),<br>[7.1.25](http://php.net/archive/2018.php#id2018-12-06-4 "http://php.net/archive/2018.php#id2018-12-06-4"),<br>[7.0.33](http://php.net/archive/2018.php#id2018-12-06-5 "http://php.net/archive/2018.php#id2018-12-06-5"), and<br>[5.6.39](http://php.net/archive/2018.php#id2018-12-06-2 "http://php.net/archive/2018.php#id2018-12-06-2"), respectively. | <br> | \*_Python_<br>• | Updated the Python 3.6 configuration to [Python<br>3.6.7](https://docs.python.org/3.6/whatsnew/changelog.html#python-3-6-7-final "https://docs.python.org/3.6/whatsnew/changelog.html#python-3-6-7-final"). | <br> | \*_Ruby_<br>• | • Updated the Ruby platform to add support for [Ruby 2.6.0](https://www.ruby-lang.org/en/news/2018/12/25/ruby-2-6-0-released/ "https://www.ruby-lang.org/en/news/2018/12/25/ruby-2-6-0-released/").<br>• Added support for AWS X-Ray. For details about X-Ray, see the [AWS X-Ray Developer Guide](../../../xray/latest/devguide.md "../../../xray/latest/devguide.md"). |     |
| **Instance types**            | Added support for more Amazon EC2 instance types in some AWS Regions, as follows:<br>                                                                                                                                                                                                                           | \*_Instance type_<br>• | \*_Regions_<br>• | <br> | --<br>• | --<br>• | <br> | \*_r5d_<br>•                   | • Europe (Paris) – eu-west-3<br>• AWS GovCloud (US-West) – us-gov-west-1                                                                                                                                                                                                      | <br> | \*_r5, c5d, m5d_<br>• | • Europe (Paris) – eu-west-3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | <br> | \*_x1e_<br>•       | • Asia Pacific (Seoul) – ap-northeast-2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |      |

## Updated platform configurations

###### These platforms are updated:

- [Packer Builder](#release-2019-01-22-linux.platforms.packer "#release-2019-01-22-linux.platforms.packer")
- [Single Container Docker](#release-2019-01-22-linux.platforms.docker "#release-2019-01-22-linux.platforms.docker")
- [Multicontainer Docker](#release-2019-01-22-linux.platforms.mcdocker "#release-2019-01-22-linux.platforms.mcdocker")
- [Preconfigured Docker](#release-2019-01-22-linux.platforms.dockerpreconfig "#release-2019-01-22-linux.platforms.dockerpreconfig")
- [Go](#release-2019-01-22-linux.platforms.go "#release-2019-01-22-linux.platforms.go")
- [Java SE](#release-2019-01-22-linux.platforms.javase "#release-2019-01-22-linux.platforms.javase")
- [Java with Tomcat](#release-2019-01-22-linux.platforms.java "#release-2019-01-22-linux.platforms.java")
- [Node.js](#release-2019-01-22-linux.platforms.nodejs "#release-2019-01-22-linux.platforms.nodejs")
- [PHP](#release-2019-01-22-linux.platforms.PHP "#release-2019-01-22-linux.platforms.PHP")
- [Python](#release-2019-01-22-linux.platforms.python "#release-2019-01-22-linux.platforms.python")
- [Ruby](#release-2019-01-22-linux.platforms.ruby "#release-2019-01-22-linux.platforms.ruby")

### Packer Builder

| Configuration and _Solution Stack Name_                                                                        | AMI       | Packer Version |
| -------------------------------------------------------------------------------------------------------------- | --------- | -------------- |
| **Elastic Beanstalk Packer Builder version 2.6.6**<br>_64bit Amazon Linux 2018.03 v2.6.6 running Packer 1.0.3_ | 2018.03.0 | 1.0.3          |

### Single Container Docker

| Configuration and _Solution Stack Name_                                                                            | AMI       | Docker Version | Proxy Server |
| ------------------------------------------------------------------------------------------------------------------ | --------- | -------------- | ------------ |
| **Single Container Docker 18.03 version 2.12.7**<br>_64bit Amazon Linux 2018.03 v2.12.7 running Docker 18.06.1-ce_ | 2018.03.0 | 18.06.1-ce     | nginx 1.14.1 |

### Multicontainer Docker

| Configuration and _Solution Stack Name_                                                                                                    | AMI       | Docker Version | ECS Agent |
| ------------------------------------------------------------------------------------------------------------------------------------------ | --------- | -------------- | --------- |
| **Multicontainer Docker 18.03 version 2.11.7**<br>_64bit Amazon Linux 2018.03 v2.11.7 running Multi-container Docker 18.06.1-ce (Generic)_ | 2018.03.0 | 18.06.1-ce     | 1.24.0    |

### Preconfigured Docker

| Configuration and _Solution Stack Name_                                                                                             | AMI       | Platform          | Container OS         | Language   | Proxy Server | Application Server | Docker Image                                  |
| ----------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------- | -------------------- | ---------- | ------------ | ------------------ | --------------------------------------------- |
| **Glassfish 5.0 (Docker) version 2.12.7**<br>_64bit Amazon Linux v2.12.7 running GlassFish 5.0 Java 8 (Preconfigured<br>• Docker)_  | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8     | nginx 1.14.1 | Glassfish 5.0      | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 |
| **Go 1.4 (Docker) version 2.12.7**<br>_64bit Debian jessie v2.12.7 running Go 1.4 (Preconfigured<br>• Docker)_                      | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie        | Go 1.4.2   | nginx 1.14.1 | none               | golang:1.4.2-onbuild                          |
| **Go 1.3 (Docker) version 2.12.7**<br>_64bit Debian jessie v2.12.7 running Go 1.3 (Preconfigured<br>• Docker)_                      | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie        | Go 1.3.3   | nginx 1.14.1 | none               | golang:1.3.3-onbuild                          |
| **Python 3.4 with uWSGI 2 (Docker) version 2.12.7**<br>_64bit Debian jessie v2.12.7 running Python 3.4 (Preconfigured<br>• Docker)_ | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie        | Python 3.4 | nginx 1.14.1 | uWSGI 2.0.8        | amazon/aws-eb-python:3.4.2-onbuild-3.5.1      |

### Go

| Configuration and _Solution Stack Name_                                              | AMI       | Language  | AWS X‑Ray | Proxy Server |
| ------------------------------------------------------------------------------------ | --------- | --------- | --------- | ------------ |
| **Go 1.11 version 2.10.0**<br>_64bit Amazon Linux 2018.03 v2.10.0 running Go 1.11.4_ | 2018.03.0 | Go 1.11.4 | 3.0.0     | nginx 1.14.1 |

### Java SE

| Configuration and _Solution Stack Name_                                        | AMI       | Language       | Tools                              | AWS X‑Ray | Proxy Server |
| ------------------------------------------------------------------------------ | --------- | -------------- | ---------------------------------- | --------- | ------------ |
| **Java 8 version 2.8.0**<br>_64bit Amazon Linux 2018.03 v2.8.0 running Java 8_ | 2018.03.0 | Java 1.8.0_191 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.0.0     | nginx 1.14.1 |
| **Java 7 version 2.8.0**<br>_64bit Amazon Linux 2018.03 v2.8.0 running Java 7_ | 2018.03.0 | Java 1.7.0.201 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.0.0     | nginx 1.14.1 |

### Java with Tomcat

| Configuration and _Solution Stack Name_                                                                   | AMI       | Language       | AWS X‑Ray | Application Server | Proxy Server                                         |
| --------------------------------------------------------------------------------------------------------- | --------- | -------------- | --------- | ------------------ | ---------------------------------------------------- |
| **Java 8 with Tomcat 8.5 version 3.1.0**<br>_64bit Amazon Linux 2018.03 v3.1.0 running Tomcat 8.5 Java 8_ | 2018.03.0 | Java 1.8.0_191 | 3.0.0     | Tomcat 8.5.32      | Apache 2.4.37 (default), Apache 2.2.34, Nginx 1.14.1 |
| **Java 8 with Tomcat 8 version 3.1.0**<br>_64bit Amazon Linux 2018.03 v3.1.0 running Tomcat 8 Java 8_     | 2018.03.0 | Java 1.8.0_191 | 3.0.0     | Tomcat 8.0.53      | Apache 2.4.37 (default), Apache 2.2.34, Nginx 1.14.1 |
| **Java 7 with Tomcat 7 version 3.1.0**<br>_64bit Amazon Linux 2018.03 v3.1.0 running Tomcat 7 Java 7_     | 2018.03.0 | Java 1.7.0.201 | 3.0.0     | Tomcat 7.0.91      | Apache 2.4.37 (default), Apache 2.2.34, Nginx 1.14.1 |
| **Java 6 with Tomcat 7 version 3.1.0**<br>_64bit Amazon Linux 2018.03 v3.1.0 running Tomcat 7 Java 6_     | 2018.03.0 | Java 1.6.0_41  | 3.0.0     | Tomcat 7.0.91      | Apache 2.4.37 (default), Apache 2.2.34, Nginx 1.14.1 |

### Node.js

| Configuration and _Solution Stack Name_                                          | AMI       | Node.js version (npm version)                                                                                                                                                                       | Proxy Server                | Git    | AWS X‑Ray |
| -------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------ | --------- |
| **Node.js version 4.8.0**<br>_64bit Amazon Linux 2018.03 v4.8.0 running Node.js_ | 2018.03.0 | 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br>Default platform: 10.15.0 | nginx 1.14.1, Apache 2.4.37 | 2.14.5 | 3.0.0     |

### PHP

| Configuration and _Solution Stack Name_                                          | AMI       | Language   | Composer | Proxy Server  |
| -------------------------------------------------------------------------------- | --------- | ---------- | -------- | ------------- |
| **PHP 7.2 version 2.8.6**<br>_64bit Amazon Linux 2018.03 v2.8.6 running PHP 7.2_ | 2018.03.0 | PHP 7.2.13 | 1.4.2    | Apache 2.4.37 |
| **PHP 7.1 version 2.8.6**<br>_64bit Amazon Linux 2018.03 v2.8.6 running PHP 7.1_ | 2018.03.0 | PHP 7.1.25 | 1.4.2    | Apache 2.4.37 |
| **PHP 7.0 version 2.8.6**<br>_64bit Amazon Linux 2018.03 v2.8.6 running PHP 7.0_ | 2018.03.0 | PHP 7.0.33 | 1.4.2    | Apache 2.4.37 |
| **PHP 5.6 version 2.8.6**<br>_64bit Amazon Linux 2018.03 v2.8.6 running PHP 5.6_ | 2018.03.0 | PHP 5.6.39 | 1.4.2    | Apache 2.4.37 |
| **PHP 5.5 version 2.8.6**<br>_64bit Amazon Linux 2018.03 v2.8.6 running PHP 5.5_ | 2018.03.0 | PHP 5.5.38 | 1.4.2    | Apache 2.4.37 |
| **PHP 5.4 version 2.8.6**<br>_64bit Amazon Linux 2018.03 v2.8.6 running PHP 5.4_ | 2018.03.0 | PHP 5.4.45 | 1.4.2    | Apache 2.4.37 |

### Python

| Configuration and _Solution Stack Name_                                                | AMI       | Language      | Package Manager | Packager          | meld3       | AWS X‑Ray | Proxy Server                    |
| -------------------------------------------------------------------------------------- | --------- | ------------- | --------------- | ----------------- | ----------- | --------- | ------------------------------- |
| **Python 3.6 version 2.8.0**<br>_64bit Amazon Linux 2018.03 v2.8.0 running Python 3.6_ | 2018.03.0 | Python 3.6.7  | pip 9.0.3       | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0     | Apache 2.4.37 with mod_wsgi 3.5 |
| **Python 3.4 version 2.8.0**<br>_64bit Amazon Linux 2018.03 v2.8.0 running Python 3.4_ | 2018.03.0 | Python 3.4.9  | pip 9.0.3       | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0     | Apache 2.4.37 with mod_wsgi 3.5 |
| **Python 2.7 version 2.8.0**<br>_64bit Amazon Linux 2018.03 v2.8.0 running Python 2.7_ | 2018.03.0 | Python 2.7.15 | pip 9.0.3       | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0     | Apache 2.4.37 with mod_wsgi 3.5 |
| **Python 2.6 version 2.8.0**<br>_64bit Amazon Linux 2018.03 v2.8.0 running Python 2.6_ | 2018.03.0 | Python 2.6.9  | pip 9.0.3       | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0     | Apache 2.4.37 with mod_wsgi 3.5 |

### Ruby

| Configuration and _Solution Stack Name_                                                                                  | AMI       | Language         | Package Manager | Application Server | AWS X‑Ray | Proxy Server |
| ------------------------------------------------------------------------------------------------------------------------ | --------- | ---------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 2.6 with Puma version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.6 (Puma)_                      | 2018.03.0 | Ruby 2.6.0-p0    | RubyGems 3.0.2  | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.6 with Passenger version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.6 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.6.0-p0    | RubyGems 3.0.2  | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.5 with Puma version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.5 (Puma)_                      | 2018.03.0 | Ruby 2.5.3-p105  | RubyGems 2.7.7  | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.5 with Passenger version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.5 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.5.3-p105  | RubyGems 2.7.7  | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.4 with Puma version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.4 (Puma)_                      | 2018.03.0 | Ruby 2.4.5-p335  | RubyGems 2.7.7  | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.4 with Passenger version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.4 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.4.5-p335  | RubyGems 2.7.7  | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.3 with Puma version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.3 (Puma)_                      | 2018.03.0 | Ruby 2.3.8-p459  | RubyGems 2.7.7  | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.3 with Passenger version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.3 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.3.8-p459  | RubyGems 2.7.7  | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.2 with Puma version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.2 (Puma)_                      | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6  | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.2 with Passenger version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.2 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6  | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.1 with Puma version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.1 (Puma)_                      | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.1 with Passenger version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.1 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.0 with Puma version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.0 (Puma)_                      | 2018.03.0 | Ruby 2.0.0-p648  | RubyGems 2.6.13 | Puma 2.16.0        | 3.0.0     | nginx 1.14.1 |
| **Ruby 2.0 with Passenger version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 2.0 (Passenger Standalone)_ | 2018.03.0 | Ruby 2.0.0-p648  | RubyGems 2.6.13 | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
| **Ruby 1.9 with Passenger version 2.9.0**<br>_64bit Amazon Linux 2018.03 v2.9.0 running Ruby 1.9.3_                      | 2018.03.0 | Ruby 1.9.3-p551  | RubyGems 2.6.13 | Passenger 4.0.60   | 3.0.0     | nginx 1.14.1 |
