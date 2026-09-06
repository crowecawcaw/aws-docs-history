

# Release: Elastic Beanstalk Linux-based platform updates on September 25, 2018
<a name="release-2018-09-25-linux"></a>

This release applies security updates to Linux-based platforms for AWS Elastic Beanstalk, and updates platform configurations. The release also includes Go and Node.js updates, a new worker environment tier version, and, for certain AWS Regions, support for additional Amazon EC2 instance types.

**Release date:** September 25, 2018

## Changes
<a name="release-2018-09-25-linux.changes"></a>


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/">Amazon Linux Security Center</a> on or before September 5, 2018 to all Linux-based platforms.</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platrform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Go</b></td><td>Updated the Go platform with the <a href="https://blog.golang.org/go1.11">Go 1.11 release</a>.</td></tr>
  <tr><td><b>Node.js</b></td><td>Updated the Node.js platform with <a href="https://nodejs.org/en/blog/vulnerability/august-2018-security-releases/">August 2018 Security Releases</a>. The Node.js Foundation applied these security updates to the new versions 6.14.4 and 8.11.4. We changed the default version for the platform to 6.14.4.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Worker environment tier</b></td><td>Added support for worker environment tier version 2.4. For details about worker environment tiers, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features-managing-env-tiers.html">AWS Elastic Beanstalk Worker Environments</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>.</td></tr>
  <tr><td><b>Instance types</b></td><td>Added support for more Amazon EC2 instance types in some AWS Regions, as follows:
<table>
<thead>
  <tr><th><b>Instance type</b></th><th><b>Regions</b></th></tr>
</thead>
<tbody>
  <tr><td><b>p3</b></td><td> <ul><li>Asia Pacific (Singapore)—ap-southeast-1</li><li>Asia Pacific (Sydney)—ap-southeast-2</li><li>Canada (Central)—ca-central-1</li><li>China (Ningxia)—cn-northwest-1</li><li>EU (Frankfurt)—eu-central-1</li><li>EU (London)—eu-west-2</li></ul> </td></tr>
  <tr><td><b>c5d</b></td><td> <ul><li>US West (N. California)—us-west-1</li><li>Asia Pacific (Seoul)—ap-northeast-2</li><li>Asia Pacific (Singapore)—ap-southeast-1</li><li>Asia Pacific (Sydney)—ap-southeast-2</li><li>Asia Pacific (Tokyo)—ap-northeast-1</li><li>EU (Frankfurt)—eu-central-1</li><li>EU (London)—eu-west-2</li></ul> </td></tr>
  <tr><td><b>m5d</b></td><td> <ul><li>US West (N. California)—us-west-1</li><li>Asia Pacific (Seoul)—ap-northeast-2</li><li>Asia Pacific (Singapore)—ap-southeast-1</li><li>Asia Pacific (Sydney)—ap-southeast-2</li><li>Asia Pacific (Tokyo)—ap-northeast-1</li><li>EU (Frankfurt)—eu-central-1</li><li>EU (London)—eu-west-2</li></ul> </td></tr>
  <tr><td><b>t3</b></td><td> <ul><li>US East (N. Virginia)—us-east-1</li><li>US East (Ohio)—us-east-2</li><li>US West (N. California)—us-west-1</li><li>US West (Oregon)—us-west-2</li><li>Asia Pacific (Singapore)—ap-southeast-1</li><li>Asia Pacific (Sydney)—ap-southeast-2</li><li>Asia Pacific (Tokyo)—ap-northeast-1</li><li>Canada (Central)—ca-central-1</li><li>EU (Frankfurt)—eu-central-1</li><li>EU (Ireland)—eu-west-1</li><li>EU (London)—eu-west-2</li><li>South America (São Paulo)—sa-east-1</li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## Updated platform configurations
<a name="release-2018-09-25-linux.platforms"></a>

**Topics**
+ [Packer Builder](#release-2018-09-25-linux.platforms.packer)
+ [Single Container Docker](#release-2018-09-25-linux.platforms.docker)
+ [Multicontainer Docker](#release-2018-09-25-linux.platforms.mcdocker)
+ [Preconfigured Docker](#release-2018-09-25-linux.platforms.dockerpreconfig)
+ [Go](#release-2018-09-25-linux.platforms.go)
+ [Java SE](#release-2018-09-25-linux.platforms.javase)
+ [Java with Tomcat](#release-2018-09-25-linux.platforms.java)
+ [Node.js](#release-2018-09-25-linux.platforms.nodejs)
+ [PHP](#release-2018-09-25-linux.platforms.PHP)
+ [Python](#release-2018-09-25-linux.platforms.python)
+ [Ruby](#release-2018-09-25-linux.platforms.ruby)

### Packer Builder
<a name="release-2018-09-25-linux.platforms.packer"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Packer Version  | 
| --- | --- | --- | 
|  **Elastic Beanstalk Packer Builder version 2.6.2** <br /> * 64bit Amazon Linux 2018.03 v2.6.2 running Packer 1.0.3 *  | 2018.03.0 | 1.0.3 | 

### Single Container Docker
<a name="release-2018-09-25-linux.platforms.docker"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Single Container Docker 18.03 version 2.12.3** <br /> * 64bit Amazon Linux 2018.03 v2.12.3 running Docker 18.06.1-ce *  | 2018.03.0 | 18.06.1-ce | nginx 1.12.1 | 

### Multicontainer Docker
<a name="release-2018-09-25-linux.platforms.mcdocker"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Docker Version  |  ECS Agent  | 
| --- | --- | --- | --- | 
|  **Multicontainer Docker 18.03 version 2.11.3** <br /> * 64bit Amazon Linux 2018.03 v2.11.3 running Multi-container Docker 18.06.1-ce (Generic) *  | 2018.03.0 | 18.06.1-ce | 1.20.2 | 

### Preconfigured Docker
<a name="release-2018-09-25-linux.platforms.dockerpreconfig"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Platform  |  Container OS  |  Language  |  Proxy Server  |  Application Server  |  Docker Image  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  **Glassfish 5.0 (Docker) version 2.12.3** <br /> * 64bit Amazon Linux v2.12.3 running GlassFish 5.0 Java 8 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.12.1 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 | 
|  **Go 1.4 (Docker) version 2.12.3** <br /> * 64bit Debian jessie v2.12.3 running Go 1.4 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Go 1.4.2 | nginx 1.12.1 | none | golang:1.4.2-onbuild | 
|  **Go 1.3 (Docker) version 2.12.3** <br /> * 64bit Debian jessie v2.12.3 running Go 1.3 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Go 1.3.3 | nginx 1.12.1 | none | golang:1.3.3-onbuild | 
|  **Python 3.4 with uWSGI 2 (Docker) version 2.12.3** <br /> * 64bit Debian jessie v2.12.3 running Python 3.4 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Python 3.4 | nginx 1.12.1 | uWSGI 2.0.8 | amazon/aws-eb-python:3.4.2-onbuild-3.5.1 | 

### Go
<a name="release-2018-09-25-linux.platforms.go"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Go 1.11 version 2.9.0** <br /> * 64bit Amazon Linux 2018.03 v2.9.0 running Go 1.11 *  | 2018.03.0 | Go 1.11 | nginx 1.12.1 | 

### Java SE
<a name="release-2018-09-25-linux.platforms.javase"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  **Java 8 version 2.7.5** <br /> * 64bit Amazon Linux 2018.03 v2.7.5 running Java 8 *  | 2018.03.0 | Java 1.8.0\_181 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 2.0.0 | nginx 1.12.1 | 
|  **Java 7 version 2.7.5** <br /> * 64bit Amazon Linux 2018.03 v2.7.5 running Java 7 *  | 2018.03.0 | Java 1.7.0.191 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 2.0.0 | nginx 1.12.1 | 

### Java with Tomcat
<a name="release-2018-09-25-linux.platforms.java"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  **Java 8 with Tomcat 8.5 version 3.0.4** <br /> * 64bit Amazon Linux 2018.03 v3.0.4 running Tomcat 8.5 Java 8 *  | 2018.03.0 | Java 1.8.0\_181 | 2.0.0 | Tomcat 8.5.32 | Apache 2.4.34 (default), Apache 2.2.34, Nginx 1.12.1 | 
|  **Java 8 with Tomcat 8 version 3.0.4** <br /> * 64bit Amazon Linux 2018.03 v3.0.4 running Tomcat 8 Java 8 *  | 2018.03.0 | Java 1.8.0\_181 | 2.0.0 | Tomcat 8.0.53 | Apache 2.4.34 (default), Apache 2.2.34, Nginx 1.12.1 | 
|  **Java 7 with Tomcat 7 version 3.0.4** <br /> * 64bit Amazon Linux 2018.03 v3.0.4 running Tomcat 7 Java 7 *  | 2018.03.0 | Java 1.7.0.191 | 2.0.0 | Tomcat 7.0.90 | Apache 2.4.34 (default), Apache 2.2.34, Nginx 1.12.1 | 
|  **Java 6 with Tomcat 7 version 3.0.4** <br /> * 64bit Amazon Linux 2018.03 v3.0.4 running Tomcat 7 Java 6 *  | 2018.03.0 | Java 1.6.0\_41 | 2.0.0 | Tomcat 7.0.90 | Apache 2.4.34 (default), Apache 2.2.34, Nginx 1.12.1 | 

### Node.js
<a name="release-2018-09-25-linux.platforms.nodejs"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Node.js version (npm version)  |  Proxy Server  |  Git  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  **Node.js version 4.5.4** <br /> * 64bit Amazon Linux 2018.03 v4.5.4 running Node.js *  | 2018.03.0 | 8.11.4 (5.6.0), 8.11.3(5.6.0), 7.10.1 (4.2.0), 6.14.4 (3.10.10), 6.14.3(3.10.10), 5.12.0 (3.8.6), 4.9.1(2.15.11), 4.8.7 (2.15.11)<br /> Default platform: 6.14.4 | nginx 1.12.1, Apache 2.4.34 | 2.14.4 | 2.0.0 | 

### PHP
<a name="release-2018-09-25-linux.platforms.PHP"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  **PHP 7.2 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running PHP 7.2 *  | 2018.03.0 | PHP 7.2.8 | 1.4.2 | Apache 2.4.34 | 
|  **PHP 7.1 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running PHP 7.1 *  | 2018.03.0 | PHP 7.1.20 | 1.4.2 | Apache 2.4.34 | 
|  **PHP 7.0 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running PHP 7.0 *  | 2018.03.0 | PHP 7.0.31 | 1.4.2 | Apache 2.4.34 | 
|  **PHP 5.6 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running PHP 5.6 *  | 2018.03.0 | PHP 5.6.37 | 1.4.2 | Apache 2.4.34 | 
|  **PHP 5.5 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running PHP 5.5 *  | 2018.03.0 | PHP 5.5.38 | 1.4.2 | Apache 2.4.34 | 
|  **PHP 5.4 version 2.8.2** <br /> * 64bit Amazon Linux 2018.03 v2.8.2 running PHP 5.4 *  | 2018.03.0 | PHP 5.4.45 | 1.4.2 | Apache 2.4.34 | 

### Python
<a name="release-2018-09-25-linux.platforms.python"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  **Python 3.6 version 2.7.4** <br /> * 64bit Amazon Linux 2018.03 v2.7.4 running Python 3.6 *  | 2018.03.0 | Python 3.6.5 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 2.0.0 | Apache 2.4.34 with mod\_wsgi 3.5 | 
|  **Python 3.4 version 2.7.4** <br /> * 64bit Amazon Linux 2018.03 v2.7.4 running Python 3.4 *  | 2018.03.0 | Python 3.4.8 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 2.0.0 | Apache 2.4.34 with mod\_wsgi 3.5 | 
|  **Python 2.7 version 2.7.4** <br /> * 64bit Amazon Linux 2018.03 v2.7.4 running Python 2.7 *  | 2018.03.0 | Python 2.7.14 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 2.0.0 | Apache 2.4.34 with mod\_wsgi 3.5 | 
|  **Python 2.6 version 2.7.4** <br /> * 64bit Amazon Linux 2018.03 v2.7.4 running Python 2.6 *  | 2018.03.0 | Python 2.6.9 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 2.0.0 | Apache 2.4.34 with mod\_wsgi 3.5 | 

### Ruby
<a name="release-2018-09-25-linux.platforms.ruby"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  **Ruby 2.5 with Puma version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.5 (Puma) *  | 2018.03.0 | Ruby 2.5.1-p57 | RubyGems 2.7.6 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.5 with Passenger version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.5 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.5.1-p57 | RubyGems 2.7.6 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 2.4 with Puma version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.4 (Puma) *  | 2018.03.0 | Ruby 2.4.4-p296 | RubyGems 2.7.6 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.4 with Passenger version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.4 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.4.4-p296 | RubyGems 2.7.6 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 2.3 with Puma version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.3 (Puma) *  | 2018.03.0 | Ruby 2.3.7-p456 | RubyGems 2.7.6 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.3 with Passenger version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.3 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.3.7-p456 | RubyGems 2.7.6 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 2.2 with Puma version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.2 (Puma) *  | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.2 with Passenger version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.2 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 2.1 with Puma version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.1 (Puma) *  | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.1 with Passenger version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.1 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 2.0 with Puma version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.0 (Puma) *  | 2018.03.0 | Ruby 2.0.0-p648 | RubyGems 2.6.13 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.0 with Passenger version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 2.0 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.0.0-p648 | RubyGems 2.6.13 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 1.9 with Passenger version 2.8.4** <br /> * 64bit Amazon Linux 2018.03 v2.8.4 running Ruby 1.9.3 *  | 2018.03.0 | Ruby 1.9.3-p551 | RubyGems 2.6.13 | Passenger 4.0.60 | nginx 1.12.1 | 