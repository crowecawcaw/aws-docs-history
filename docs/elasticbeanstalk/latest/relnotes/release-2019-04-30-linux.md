

# Release: Elastic Beanstalk Linux-based platform updates on April 30, 2019
<a name="release-2019-04-30-linux"></a>

This release provides new Linux-based platform versions for AWS Elastic Beanstalk. The release includes security updates. It also includes Multicontainer Docker, Go, Node.js, PHP, and Ruby updates, an Apache update, and support for additional Amazon EC2 instance types in certain AWS Regions.

**Release date:** April 30, 2019

## Changes
<a name="release-2019-04-30-linux.changes"></a>

**Notes**  
**2019-04-30** – At this time, the release doesn't include an update for the Node.js platform. We will update this platform soon and update the release notes.
**2019-05-03** – We released the Node.js platform update. This release is now complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/">Amazon Linux Security Center</a> on or before April 19, 2019 to all Linux-based platforms.<br />The Apache, PHP, and Ruby 2.4.6 releases include security updates.</td></tr>
  <tr><td><b>Cross-platform updates</b></td><td>Made these cross-platform updates:
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Apache</b></td><td>Updated platforms supporting the Apache HTTP Server 2.4 to version 2.4.39. For details, see <a href="https://downloads.apache.org/httpd/CHANGES_2.4">Changes with Apache 2.4.x</a> on the <i>Apache Software Foundation</i> website. The release includes seven security updates.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Multicontainer Docker</b></td><td>Updated the ECS agent to version 1.27.0.</td></tr>
  <tr><td><b>Go</b></td><td>Updated to minor revision 1.12.4. For details, see <a href="https://golang.org/doc/devel/release.html#go1.12">go1.12</a> in <i>The Go Programming Language Release History</i>.</td></tr>
  <tr><td><b>Node.js</b></td><td>Updated the Node.js platform to add support for Node versions <a href="https://nodejs.org/en/blog/release/v8.16.0/">8.16.0</a>, <a href="https://nodejs.org/en/blog/release/v6.17.1/">6.17.1</a>.</td></tr>
  <tr><td><b>PHP</b></td><td>Released new PHP 7.2, 7.1, and 5.6 versions: <a href="https://www.php.net/releases/7_2_17.php">7.2.17</a>, <a href="https://www.php.net/releases/7_1_28.php">7.1.28</a>, and <a href="https://www.php.net/releases/5_6_40.php">5.6.40</a>, respectively. These releases include security updates.</td></tr>
  <tr><td><b>Ruby</b></td><td>Released new Ruby 2.6 and 2.4 versions: <a href="https://www.ruby-lang.org/en/news/2019/04/17/ruby-2-6-3-released/">2.6.3</a> and <a href="https://www.ruby-lang.org/en/news/2019/04/01/ruby-2-4-6-released/">2.4.6</a>, respectively. The Ruby 2.4.6 release includes security updates.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Instance types</b></td><td>Added support for more Amazon EC2 instance types in some AWS Regions. In particular, we added support for the new M5ad and R5ad instances. They add high-speed, low latency local (physically connected) block storage to the existing M5a and R5a instances. For more information, see <a href="https://aws.amazon.com/blogs/aws/new-amd-epyc-powered-amazon-ec2-m5ad-and-r5ad-instances/">New AMD EPYC-Powered Amazon EC2 M5ad and R5ad Instances</a>.<br />The added instance types are listed in the following table.
<table>
<thead>
  <tr><th><b>Instance types</b></th><th><b>Regions</b></th></tr>
</thead>
<tbody>
  <tr><td><b>m5ad</b></td><td> <ul><li>US East (Ohio) – us-east-2</li><li>US West (Oregon) – us-west-2</li><li>Asia Pacific (Singapore) – ap-southeast-1</li></ul> </td></tr>
  <tr><td><b>r5ad</b></td><td> <ul><li>US East (Ohio) – us-east-2</li><li>US East (N. Virginia) – us-east-1</li><li>US West (Oregon) – us-west-2</li><li>Asia Pacific (Singapore) – ap-southeast-1</li></ul> </td></tr>
  <tr><td><b>z1d</b></td><td> <ul><li>Asia Pacific (Sydney) – ap-southeast-2</li><li>Europe (Frankfurt) – eu-central-1</li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2019-04-30-linux.platforms"></a>

**Topics**
+ [Packer Builder](#release-2019-04-30-linux.platforms.packer)
+ [Single Container Docker](#release-2019-04-30-linux.platforms.docker)
+ [Multicontainer Docker](#release-2019-04-30-linux.platforms.mcdocker)
+ [Preconfigured Docker](#release-2019-04-30-linux.platforms.dockerpreconfig)
+ [Go](#release-2019-04-30-linux.platforms.go)
+ [Java SE](#release-2019-04-30-linux.platforms.javase)
+ [Java with Tomcat](#release-2019-04-30-linux.platforms.java)
+ [Node.js](#release-2019-05-03-linux.platforms.nodejs)
+ [PHP](#release-2019-04-30-linux.platforms.PHP)
+ [Python](#release-2019-04-30-linux.platforms.python)
+ [Ruby](#release-2019-04-30-linux.platforms.ruby)

### Packer Builder
<a name="release-2019-04-30-linux.platforms.packer"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Packer Version  | 
| --- | --- | --- | 
|  **Elastic Beanstalk Packer Builder version 2.6.9** <br /> * 64bit Amazon Linux 2018.03 v2.6.9 running Packer 1.0.3 *  | 2018.03.0 | 1.0.3 | 

### Single Container Docker
<a name="release-2019-04-30-linux.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Single Container Docker 18.06 version 2.12.11** <br /> * 64bit Amazon Linux 2018.03 v2.12.11 running Docker 18.06.1-ce *  | 2018.03.0 | 18.06.1-ce | nginx 1.14.1 | 

### Multicontainer Docker
<a name="release-2019-04-30-linux.platforms.mcdocker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  ECS Agent  | 
| --- | --- | --- | --- | 
|  **Multicontainer Docker 18.06 version 2.13.0** <br /> * 64bit Amazon Linux 2018.03 v2.13.0 running Multi-container Docker 18.06.1-ce (Generic) *  | 2018.03.0 | 18.06.1-ce | 1.27.0 | 

### Preconfigured Docker
<a name="release-2019-04-30-linux.platforms.dockerpreconfig"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Platform  |  Container OS  |  Language  |  Proxy Server  |  Application Server  |  Docker Image  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  **Glassfish 5.0 (Docker) version 2.12.11** <br /> * 64bit Amazon Linux v2.12.11 running GlassFish 5.0 Java 8 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.14.1 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 | 
|  **Go 1.4 (Docker) version 2.12.11** <br /> * 64bit Debian jessie v2.12.11 running Go 1.4 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Go 1.4.2 | nginx 1.14.1 | none | golang:1.4.2-onbuild | 
|  **Go 1.3 (Docker) version 2.12.11** <br /> * 64bit Debian jessie v2.12.11 running Go 1.3 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Go 1.3.3 | nginx 1.14.1 | none | golang:1.3.3-onbuild | 
|  **Python 3.4 with uWSGI 2 (Docker) version 2.12.11** <br /> * 64bit Debian jessie v2.12.11 running Python 3.4 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Python 3.4 | nginx 1.14.1 | uWSGI 2.0.8 | amazon/aws-eb-python:3.4.2-onbuild-3.5.1 | 

### Go
<a name="release-2019-04-30-linux.platforms.go"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  **Go 1.12 version 2.11.1** <br /> * 64bit Amazon Linux 2018.03 v2.11.1 running Go 1.12.4 *  | 2018.03.0 | Go 1.12.4 | 3.0.0 | nginx 1.14.1 | 

### Java SE
<a name="release-2019-04-30-linux.platforms.javase"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  **Java 8 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running Java 8 *  | 2018.03.0 | Java 1.8.0\_201 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.0.0 | nginx 1.14.1 | 
|  **Java 7 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running Java 7 *  | 2018.03.0 | Java 1.7.0\_211 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.0.0 | nginx 1.14.1 | 

### Java with Tomcat
<a name="release-2019-04-30-linux.platforms.java"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  **Java 8 with Tomcat 8.5 version 3.1.3** <br /> * 64bit Amazon Linux 2018.03 v3.1.3 running Tomcat 8.5 Java 8 *  | 2018.03.0 | Java 1.8.0\_201 | 3.0.0 | Tomcat 8.5.32 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 | 
|  **Java 8 with Tomcat 8 version 3.1.3** <br /> * 64bit Amazon Linux 2018.03 v3.1.3 running Tomcat 8 Java 8 *  | 2018.03.0 | Java 1.8.0\_201 | 3.0.0 | Tomcat 8.0.53 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 | 
|  **Java 7 with Tomcat 7 version 3.1.3** <br /> * 64bit Amazon Linux 2018.03 v3.1.3 running Tomcat 7 Java 7 *  | 2018.03.0 | Java 1.7.0\_211 | 3.0.0 | Tomcat 7.0.91 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 | 
|  **Java 6 with Tomcat 7 version 3.1.3** <br /> * 64bit Amazon Linux 2018.03 v3.1.3 running Tomcat 7 Java 6 *  | 2018.03.0 | Java 1.6.0\_41 | 3.0.0 | Tomcat 7.0.91 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 | 

### Node.js
<a name="release-2019-05-03-linux.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  **Node.js version 4.8.3** <br /> * 64bit Amazon Linux 2018.03 v4.8.3 running Node.js *  | 2018.03.0 | 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.16.0 (6.4.1), 8.15.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.17.1 (3.10.10), 6.17.0 (3.10.10), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br /> Default platform: 10.15.3 | nginx 1.14.1, Apache 2.4.39 | 2.14.5 | 3.0.0 | 

### PHP
<a name="release-2019-04-30-linux.platforms.PHP"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  **PHP 7.2 version 2.8.9** <br /> * 64bit Amazon Linux 2018.03 v2.8.9 running PHP 7.2 *  | 2018.03.0 | PHP 7.2.17 | 1.4.2 | Apache 2.4.39 | 
|  **PHP 7.1 version 2.8.9** <br /> * 64bit Amazon Linux 2018.03 v2.8.9 running PHP 7.1 *  | 2018.03.0 | PHP 7.1.28 | 1.4.2 | Apache 2.4.39 | 
|  **PHP 7.0 version 2.8.9** <br /> * 64bit Amazon Linux 2018.03 v2.8.9 running PHP 7.0 *  | 2018.03.0 | PHP 7.0.33 | 1.4.2 | Apache 2.4.39 | 
|  **PHP 5.6 version 2.8.9** <br /> * 64bit Amazon Linux 2018.03 v2.8.9 running PHP 5.6 *  | 2018.03.0 | PHP 5.6.40 | 1.4.2 | Apache 2.4.39 | 
|  **PHP 5.5 version 2.8.9** <br /> * 64bit Amazon Linux 2018.03 v2.8.9 running PHP 5.5 *  | 2018.03.0 | PHP 5.5.38 | 1.4.2 | Apache 2.4.39 | 
|  **PHP 5.4 version 2.8.9** <br /> * 64bit Amazon Linux 2018.03 v2.8.9 running PHP 5.4 *  | 2018.03.0 | PHP 5.4.45 | 1.4.2 | Apache 2.4.39 | 

### Python
<a name="release-2019-04-30-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  **Python 3.6 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running Python 3.6 *  | 2018.03.0 | Python 3.6.8 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0 | Apache 2.4.39 with mod\_wsgi 3.5 | 
|  **Python 3.4 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running Python 3.4 *  | 2018.03.0 | Python 3.4.9 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0 | Apache 2.4.39 with mod\_wsgi 3.5 | 
|  **Python 2.7 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running Python 2.7 *  | 2018.03.0 | Python 2.7.16 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0 | Apache 2.4.39 with mod\_wsgi 3.5 | 
|  **Python 2.6 version 2.8.3** <br /> * 64bit Amazon Linux 2018.03 v2.8.3 running Python 2.6 *  | 2018.03.0 | Python 2.6.9 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0 | Apache 2.4.39 with mod\_wsgi 3.5 | 

### Ruby
<a name="release-2019-04-30-linux.platforms.ruby"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  **Ruby 2.6 with Puma version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.6 (Puma) *  | 2018.03.0 | Ruby 2.6.3-p62 | RubyGems 2.7.9 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.6 with Passenger version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.6 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.6.3-p62 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.5 with Puma version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.5 (Puma) *  | 2018.03.0 | Ruby 2.5.5-p157 | RubyGems 2.7.9 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.5 with Passenger version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.5 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.5.5-p157 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.4 with Puma version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.4 (Puma) *  | 2018.03.0 | Ruby 2.4.6-p354 | RubyGems 2.7.9 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.4 with Passenger version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.4 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.4.6-p354 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.3 with Puma version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.3 (Puma) *  | 2018.03.0 | Ruby 2.3.8-p459 | RubyGems 2.7.7 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.3 with Passenger version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.3 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.3.8-p459 | RubyGems 2.7.7 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.2 with Puma version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.2 (Puma) *  | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.2 with Passenger version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.2 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.2.10-p489 | RubyGems 2.7.6 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.1 with Puma version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.1 (Puma) *  | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.1 with Passenger version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.1 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.1.10-p492 | RubyGems 2.6.13 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.0 with Puma version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.0 (Puma) *  | 2018.03.0 | Ruby 2.0.0-p648 | RubyGems 2.6.13 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.0 with Passenger version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 2.0 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.0.0-p648 | RubyGems 2.6.13 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 1.9 with Passenger version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Ruby 1.9.3 *  | 2018.03.0 | Ruby 1.9.3-p551 | RubyGems 2.6.13 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 | 