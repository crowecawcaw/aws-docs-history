

# Release: Elastic Beanstalk Linux-based platform updates on June 14, 2019
<a name="release-2019-06-14-linux"></a>

This release provides new Linux-based platform versions for AWS Elastic Beanstalk. The release includes security updates. It also includes a Go update and support for an additional Amazon EC2 instance type in certain AWS Regions.

**Release date:** June 14, 2019

## Changes
<a name="release-2019-06-14-linux.changes"></a>


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/">Amazon Linux Security Center</a> on or before <b>June 5, 2019</b> to all Linux-based platforms.</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Go</b></td><td>Updated to minor revision 1.12.6. For details, see <a href="https://golang.org/doc/devel/release.html#go1.12">go1.12</a> in <i>The Go Programming Language Release History</i>.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Instance types</b></td><td>Added support for an additional Amazon EC2 instance type in some AWS Regions, as listed in the following table.
<table>
<thead>
  <tr><th><b>Instance type</b></th><th><b>Regions</b></th></tr>
</thead>
<tbody>
  <tr><td><b>T3a</b></td><td> <ul><li>US East (Ohio) – us-east-2</li><li>US East (N. Virginia) – us-east-1</li><li>US West (Oregon) – us-west-2</li><li>Asia Pacific (Singapore) – ap-southeast-1</li><li>Europe (Ireland) – eu-west-1</li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2019-06-14-linux.platforms"></a>

**Topics**
+ [Packer Builder](#release-2019-06-14-linux.platforms.packer)
+ [Single Container Docker](#release-2019-06-14-linux.platforms.docker)
+ [Multicontainer Docker](#release-2019-06-14-linux.platforms.mcdocker)
+ [Preconfigured Docker](#release-2019-06-14-linux.platforms.dockerpreconfig)
+ [Go](#release-2019-06-14-linux.platforms.go)
+ [Java SE](#release-2019-06-14-linux.platforms.javase)
+ [Java with Tomcat](#release-2019-06-14-linux.platforms.java)
+ [Node.js](#release-2019-06-14-linux.platforms.nodejs)
+ [PHP](#release-2019-06-14-linux.platforms.PHP)
+ [Python](#release-2019-06-14-linux.platforms.python)
+ [Ruby](#release-2019-06-14-linux.platforms.ruby)

### Packer Builder
<a name="release-2019-06-14-linux.platforms.packer"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Packer Version  | 
| --- | --- | --- | 
|  **Elastic Beanstalk Packer Builder version 2.6.11** <br /> * 64bit Amazon Linux 2018.03 v2.6.11 running Packer 1.0.3 *  | 2018.03.0 | 1.0.3 | 

### Single Container Docker
<a name="release-2019-06-14-linux.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  **Single Container Docker 18.06 version 2.12.13** <br /> * 64bit Amazon Linux 2018.03 v2.12.13 running Docker 18.06.1-ce *  | 2018.03.0 | 18.06.1-ce | nginx 1.14.1 | 

### Multicontainer Docker
<a name="release-2019-06-14-linux.platforms.mcdocker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  ECS Agent  | 
| --- | --- | --- | --- | 
|  **Multicontainer Docker 18.06 version 2.14.1** <br /> * 64bit Amazon Linux 2018.03 v2.14.1 running Multi-container Docker 18.06.1-ce (Generic) *  | 2018.03.0 | 18.06.1-ce | 1.28.0 | 

### Preconfigured Docker
<a name="release-2019-06-14-linux.platforms.dockerpreconfig"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Platform  |  Container OS  |  Language  |  Proxy Server  |  Application Server  |  Docker Image  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  **Glassfish 5.0 (Docker) version 2.12.13** <br /> * 64bit Amazon Linux v2.12.13 running GlassFish 5.0 Java 8 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.14.1 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 | 

### Go
<a name="release-2019-06-14-linux.platforms.go"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  **Go 1.12 version 2.11.3** <br /> * 64bit Amazon Linux 2018.03 v2.11.3 running Go 1.12.6 *  | 2018.03.0 | Go 1.12.6 | 3.0.0 | nginx 1.14.1 | 

### Java SE
<a name="release-2019-06-14-linux.platforms.javase"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  **Java 8 version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Java 8 *  | 2018.03.0 | Java 1.8.0\_201 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.0.0 | nginx 1.14.1 | 
|  **Java 7 version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Java 7 *  | 2018.03.0 | Java 1.7.0\_211 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.0.0 | nginx 1.14.1 | 

### Java with Tomcat
<a name="release-2019-06-14-linux.platforms.java"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  **Java 8 with Tomcat 8.5 version 3.1.5** <br /> * 64bit Amazon Linux 2018.03 v3.1.5 running Tomcat 8.5 Java 8 *  | 2018.03.0 | Java 1.8.0\_201 | 3.0.0 | Tomcat 8.5.40 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 | 
|  **Java 7 with Tomcat 7 version 3.1.5** <br /> * 64bit Amazon Linux 2018.03 v3.1.5 running Tomcat 7 Java 7 *  | 2018.03.0 | Java 1.7.0\_211 | 3.0.0 | Tomcat 7.0.91 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 | 

### Node.js
<a name="release-2019-06-14-linux.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  **Node.js version 4.9.1** <br /> * 64bit Amazon Linux 2018.03 v4.9.1 running Node.js *  | 2018.03.0 | 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.16.0 (6.4.1), 8.15.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.17.1 (3.10.10), 6.17.0 (3.10.10), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br /> Default version: 10.16.0 | nginx 1.14.1, Apache 2.4.39 | 2.14.5 | 3.0.0 | 

### PHP
<a name="release-2019-06-14-linux.platforms.PHP"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  **PHP 7.2 version 2.8.11** <br /> * 64bit Amazon Linux 2018.03 v2.8.11 running PHP 7.2 *  | 2018.03.0 | PHP 7.2.17 | 1.4.2 | Apache 2.4.39 | 

### Python
<a name="release-2019-06-14-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  **Python 3.6 version 2.8.5** <br /> * 64bit Amazon Linux 2018.03 v2.8.5 running Python 3.6 *  | 2018.03.0 | Python 3.6.8 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.0.0 | Apache 2.4.39 with mod\_wsgi 3.5 | 

### Ruby
<a name="release-2019-06-14-linux.platforms.ruby"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  **Ruby 2.6 with Puma version 2.9.5** <br /> * 64bit Amazon Linux 2018.03 v2.9.5 running Ruby 2.6 (Puma) *  | 2018.03.0 | Ruby 2.6.3-p62 | RubyGems 2.7.9 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.6 with Passenger version 2.9.5** <br /> * 64bit Amazon Linux 2018.03 v2.9.5 running Ruby 2.6 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.6.3-p62 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.5 with Puma version 2.9.5** <br /> * 64bit Amazon Linux 2018.03 v2.9.5 running Ruby 2.5 (Puma) *  | 2018.03.0 | Ruby 2.5.5-p157 | RubyGems 2.7.9 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.5 with Passenger version 2.9.5** <br /> * 64bit Amazon Linux 2018.03 v2.9.5 running Ruby 2.5 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.5.5-p157 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.4 with Puma version 2.9.5** <br /> * 64bit Amazon Linux 2018.03 v2.9.5 running Ruby 2.4 (Puma) *  | 2018.03.0 | Ruby 2.4.6-p354 | RubyGems 2.7.9 | Puma 2.16.0 | 3.0.0 | nginx 1.14.1 | 
|  **Ruby 2.4 with Passenger version 2.9.5** <br /> * 64bit Amazon Linux 2018.03 v2.9.5 running Ruby 2.4 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.4.6-p354 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.0.0 | nginx 1.14.1 | 