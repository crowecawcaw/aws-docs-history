

# Release: Elastic Beanstalk Linux-based platform updates on October 31, 2018
<a name="release-2018-10-31-linux"></a>

This release applies security updates to Linux-based platforms for AWS Elastic Beanstalk, and updates platform configurations. The release also includes Go, Node.js, PHP, and Ruby updates, and, for certain AWS Regions, support for additional Amazon EC2 instance types.

**Release date:** October 31, 2018

## Changes
<a name="release-2018-10-31-linux.changes"></a>


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/">Amazon Linux Security Center</a> on or before October 18, 2018 to all Linux-based platforms.</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Go</b></td><td>Updated the Go platform to version 1.11.1.</td></tr>
  <tr><td><b>Node.js</b></td><td>Updated the Node.js platform to support <a href="https://nodejs.org/en/blog/release/v8.12.0/">Node v8.12.0</a>.</td></tr>
  <tr><td><b>PHP</b></td><td>Updated the PHP 7.2, 7.1, 7.0, and 5.6 configurations to PHP releases <a href="http://php.net/archive/2018.php#id2018-10-11-2">7.2.11</a>, <a href="http://php.net/archive/2018.php#id2018-10-11-3">7.1.23</a>, <a href="http://php.net/archive/2018.php#id2018-09-13-3">7.0.32</a>, and <a href="http://php.net/archive/2018.php#id2018-09-13-5">5.6.38</a>, respectively.</td></tr>
  <tr><td><b>Ruby</b></td><td>Updated the Ruby 2.5, 2.4, and 2.3 configurations to Ruby releases <a href="https://www.ruby-lang.org/en/news/2018/10/18/ruby-2-5-3-released/">2.5.3</a>, <a href="https://www.ruby-lang.org/en/news/2018/10/17/ruby-2-4-5-released/">2.4.5</a>, and <a href="https://www.ruby-lang.org/en/news/2018/10/17/ruby-2-3-8-released/">2.3.8</a>, respectively.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Instance types</b></td><td>Added support for more Amazon EC2 instance types in some AWS Regions, as follows:
<table>
<thead>
  <tr><th><b>Instance type</b></th><th><b>Regions</b></th></tr>
</thead>
<tbody>
  <tr><td><b>c5d</b></td><td> <ul><li>AWS GovCloud (US-West) – us-gov-west-1</li></ul> </td></tr>
  <tr><td><b>f1.4xlarge</b></td><td> <ul><li>US East (N. Virginia) – us-east-1</li><li>US West (Oregon) – us-west-2</li><li>Europe (Ireland) – eu-west-1</li><li>AWS GovCloud (US-West) – us-gov-west-1</li></ul> </td></tr>
  <tr><td><b>g3</b></td><td> <ul><li>Canada (Central) – ca-central-1</li></ul> </td></tr>
  <tr><td><b>g3s</b></td><td> <ul><li>US East (Ohio) – us-east-2</li><li>US East (N. Virginia) – us-east-1</li><li>US West (Oregon) – us-west-2</li><li>Asia Pacific (Sydney) – ap-southeast-2</li><li>Asia Pacific (Tokyo) – ap-northeast-1</li><li>Europe (Frankfurt) – eu-central-1</li><li>Europe (Ireland) – eu-west-1</li></ul> </td></tr>
  <tr><td><b>m5d</b></td><td> <ul><li>AWS GovCloud (US-West) – us-gov-west-1</li></ul> </td></tr>
  <tr><td><b>r5</b></td><td> <ul><li>US West (N. California) – us-west-1</li><li>Asia Pacific (Seoul) – ap-northeast-2</li><li>Asia Pacific (Singapore) – ap-southeast-1</li><li>Asia Pacific (Sydney) – ap-southeast-2</li><li>Asia Pacific (Tokyo) – ap-northeast-1</li><li>Canada (Central) – ca-central-1</li><li>Europe (Frankfurt) – eu-central-1</li><li>Europe (Ireland) – eu-west-1</li><li>Europe (London) – eu-west-2</li><li>Europe (Paris) – eu-west-3</li><li>AWS GovCloud (US-West) – us-gov-west-1</li></ul> </td></tr>
  <tr><td><b>r5d</b></td><td> <ul><li>US West (N. California) – us-west-1</li><li>Asia Pacific (Seoul) – ap-northeast-2</li><li>Asia Pacific (Singapore) – ap-southeast-1</li><li>Asia Pacific (Sydney) – ap-southeast-2</li><li>Asia Pacific (Tokyo) – ap-northeast-1</li><li>Canada (Central) – ca-central-1</li><li>Europe (Frankfurt) – eu-central-1</li><li>Europe (Ireland) – eu-west-1</li><li>Europe (London) – eu-west-2</li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## Updated platform configurations
<a name="release-2018-10-31-linux.platforms"></a>

**Topics**
+ [Packer Builder](#release-2018-10-29-linux.platforms.packer)
+ [Single Container Docker](#release-2018-10-29-linux.platforms.docker)
+ [Multicontainer Docker](#release-2018-10-29-linux.platforms.mcdocker)
+ [Preconfigured Docker](#release-2018-10-29-linux.platforms.dockerpreconfig)
+ [Go](#release-2018-10-29-linux.platforms.go)
+ [Java SE](#release-2018-10-29-linux.platforms.javase)
+ [Java with Tomcat](#release-2018-10-29-linux.platforms.java)
+ [Node.js](#release-2018-10-29-linux.platforms.nodejs)
+ [PHP](#release-2018-10-29-linux.platforms.PHP)
+ [Python](#release-2018-10-29-linux.platforms.python)
+ [Ruby](#release-2018-10-29-linux.platforms.ruby)

### Packer Builder
<a name="release-2018-10-29-linux.platforms.packer"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Packer Version  | 
| --- | --- | --- | 
|  **Elastic Beanstalk Packer Builder version 2.6.3** <br /> * 64bit Amazon Linux 2018.03 v2.6.3 running Packer 1.0.3 *  | 2018.03.0 | 1.0.3 | 

### Single Container Docker
<a name="release-2018-10-29-linux.platforms.docker"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Single Container Docker 18.03 version 2.12.4** <br /> * 64bit Amazon Linux 2018.03 v2.12.4 running Docker 18.06.1-ce *  | 2018.03.0 | 18.06.1-ce | nginx 1.12.1 | 

### Multicontainer Docker
<a name="release-2018-10-29-linux.platforms.mcdocker"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Docker Version  |  ECS Agent  | 
| --- | --- | --- | --- | 
|  **Multicontainer Docker 18.03 version 2.11.4** <br /> * 64bit Amazon Linux 2018.03 v2.11.4 running Multi-container Docker 18.06.1-ce (Generic) *  | 2018.03.0 | 18.06.1-ce | 1.21.0 | 

### Preconfigured Docker
<a name="release-2018-10-29-linux.platforms.dockerpreconfig"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Platform  |  Container OS  |  Language  |  Proxy Server  |  Application Server  |  Docker Image  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  **Glassfish 5.0 (Docker) version 2.12.4** <br /> * 64bit Amazon Linux v2.12.4 running GlassFish 5.0 Java 8 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.12.1 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 | 
|  **Go 1.4 (Docker) version 2.12.4** <br /> * 64bit Debian jessie v2.12.4 running Go 1.4 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Go 1.4.2 | nginx 1.12.1 | none | golang:1.4.2-onbuild | 
|  **Go 1.3 (Docker) version 2.12.4** <br /> * 64bit Debian jessie v2.12.4 running Go 1.3 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Go 1.3.3 | nginx 1.12.1 | none | golang:1.3.3-onbuild | 
|  **Python 3.4 with uWSGI 2 (Docker) version 2.12.4** <br /> * 64bit Debian jessie v2.12.4 running Python 3.4 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Python 3.4 | nginx 1.12.1 | uWSGI 2.0.8 | amazon/aws-eb-python:3.4.2-onbuild-3.5.1 | 

### Go
<a name="release-2018-10-29-linux.platforms.go"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Go 1.11 version 2.9.1** <br /> * 64bit Amazon Linux 2018.03 v2.9.1 running Go 1.11 *  | 2018.03.0 | Go 1.11.1 | nginx 1.12.1 | 

### Java SE
<a name="release-2018-10-29-linux.platforms.javase"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  **Java 8 version 2.7.6** <br /> * 64bit Amazon Linux 2018.03 v2.7.6 running Java 8 *  | 2018.03.0 | Java 1.8.0\_181 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 2.0.0 | nginx 1.12.1 | 
|  **Java 7 version 2.7.6** <br /> * 64bit Amazon Linux 2018.03 v2.7.6 running Java 7 *  | 2018.03.0 | Java 1.7.0.191 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 2.0.0 | nginx 1.12.1 | 

### Java with Tomcat
<a name="release-2018-10-29-linux.platforms.java"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  **Java 8 with Tomcat 8.5 version 3.0.5** <br /> * 64bit Amazon Linux 2018.03 v3.0.5 running Tomcat 8.5 Java 8 *  | 2018.03.0 | Java 1.8.0\_181 | 2.0.0 | Tomcat 8.5.32 | Apache 2.4.34 (default), Apache 2.2.34, Nginx 1.12.1 | 
|  **Java 8 with Tomcat 8 version 3.0.5** <br /> * 64bit Amazon Linux 2018.03 v3.0.5 running Tomcat 8 Java 8 *  | 2018.03.0 | Java 1.8.0\_181 | 2.0.0 | Tomcat 8.0.53 | Apache 2.4.34 (default), Apache 2.2.34, Nginx 1.12.1 | 
|  **Java 7 with Tomcat 7 version 3.0.5** <br /> * 64bit Amazon Linux 2018.03 v3.0.5 running Tomcat 7 Java 7 *  | 2018.03.0 | Java 1.7.0.191 | 2.0.0 | Tomcat 7.0.90 | Apache 2.4.34 (default), Apache 2.2.34, Nginx 1.12.1 | 
|  **Java 6 with Tomcat 7 version 3.0.5** <br /> * 64bit Amazon Linux 2018.03 v3.0.5 running Tomcat 7 Java 6 *  | 2018.03.0 | Java 1.6.0\_41 | 2.0.0 | Tomcat 7.0.90 | Apache 2.4.34 (default), Apache 2.2.34, Nginx 1.12.1 | 

### Node.js
<a name="release-2018-10-29-linux.platforms.nodejs"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Node.js version (npm version)  |  Proxy Server  |  Git  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  **Node.js version 4.6.0** <br /> * 64bit Amazon Linux 2018.03 v4.6.0 running Node.js *  | 2018.03.0 | 8.12.0 (6.4.1), 8.11.4 (5.6.0), 7.10.1 (4.2.0), 6.14.4 (3.10.10), 6.14.3(3.10.10), 5.12.0 (3.8.6), 4.9.1(2.15.11), 4.8.7 (2.15.11)<br /> Default platform: 6.14.4 | nginx 1.12.1, Apache 2.4.34 | 2.14.5 | 2.0.0 | 

### PHP
<a name="release-2018-10-29-linux.platforms.PHP"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  **PHP 7.2 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running PHP 7.2 *  | 2018.03.0 | PHP 7.2.11 | 1.4.2 | Apache 2.4.34 | 
|  **PHP 7.1 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running PHP 7.1 *  | 2018.03.0 | PHP 7.1.23 | 1.4.2 | Apache 2.4.34 | 
|  **PHP 7.0 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running PHP 7.0 *  | 2018.03.0 | PHP 7.0.32 | 1.4.2 | Apache 2.4.34 | 
|  **PHP 5.6 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running PHP 5.6 *  | 2018.03.0 | PHP 5.6.38 | 1.4.2 | Apache 2.4.34 | 
|  **PHP 5.5 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running PHP 5.5 *  | 2018.03.0 | PHP 5.5.38 | 1.4.2 | Apache 2.4.34 | 
|  **PHP 5.4 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running PHP 5.4 *  | 2018.03.0 | PHP 5.4.45 | 1.4.2 | Apache 2.4.34 | 

### Python
<a name="release-2018-10-29-linux.platforms.python"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  **Python 3.6 version 2.7.5** <br /> * 64bit Amazon Linux 2018.03 v2.7.5 running Python 3.6 *  | 2018.03.0 | Python 3.6.5 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 2.0.0 | Apache 2.4.34 with mod\_wsgi 3.5 | 
|  **Python 3.4 version 2.7.5** <br /> * 64bit Amazon Linux 2018.03 v2.7.5 running Python 3.4 *  | 2018.03.0 | Python 3.4.8 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 2.0.0 | Apache 2.4.34 with mod\_wsgi 3.5 | 
|  **Python 2.7 version 2.7.5** <br /> * 64bit Amazon Linux 2018.03 v2.7.5 running Python 2.7 *  | 2018.03.0 | Python 2.7.14 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 2.0.0 | Apache 2.4.34 with mod\_wsgi 3.5 | 
|  **Python 2.6 version 2.7.5** <br /> * 64bit Amazon Linux 2018.03 v2.7.5 running Python 2.6 *  | 2018.03.0 | Python 2.6.9 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 2.0.0 | Apache 2.4.34 with mod\_wsgi 3.5 | 

### Ruby
<a name="release-2018-10-29-linux.platforms.ruby"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  **Ruby 2.5 with Puma version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.5 (Puma) *  | 2018.03.0 | Ruby 2.5.3-p105 | RubyGems 2.7.7 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.5 with Passenger version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.5 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.5.3-p105 | RubyGems 2.7.7 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 2.4 with Puma version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.4 (Puma) *  | 2018.03.0 | Ruby 2.4.5-p335 | RubyGems 2.7.7 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.4 with Passenger version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.4 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.4.5-p335 | RubyGems 2.7.7 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 2.3 with Puma version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.3 (Puma) *  | 2018.03.0 | Ruby 2.3.8-p459 | RubyGems 2.7.7 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.3 with Passenger version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.3 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.3.8-p459 | RubyGems 2.7.7 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 2.2 with Puma version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.2 (Puma) *  | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.2 with Passenger version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.2 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 2.1 with Puma version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.1 (Puma) *  | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.1 with Passenger version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.1 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 2.0 with Puma version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.0 (Puma) *  | 2018.03.0 | Ruby 2.0.0-p648 | RubyGems 2.6.13 | Puma 2.16.0 | nginx 1.12.1 | 
|  **Ruby 2.0 with Passenger version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 2.0 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.0.0-p648 | RubyGems 2.6.13 | Passenger 4.0.60 | nginx 1.12.1 | 
|  **Ruby 1.9 with Passenger version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Ruby 1.9.3 *  | 2018.03.0 | Ruby 1.9.3-p551 | RubyGems 2.6.13 | Passenger 4.0.60 | nginx 1.12.1 | 