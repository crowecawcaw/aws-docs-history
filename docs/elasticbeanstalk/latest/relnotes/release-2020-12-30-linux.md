

# Release: Elastic Beanstalk Amazon Linux AMI platform updates on December 30, 2020
<a name="release-2020-12-30-linux"></a>

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux AMI. The release includes security updates. It also includes Go and Node.js updates.

**Release date:** December 30, 2020

## Changes
<a name="release-2020-12-30-linux.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/">Amazon Linux Security Center</a> on or before <b>December 23, 2020</b> to all Amazon Linux AMI platforms.<br />The <b>Go</b> and <b>Node.js</b> releases include security fixes. For more information, see <b>Platform-specific updates</b> in this table.</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Go</b></td><td>Updated Go to release 1.15.6. For details, see <a href="https://golang.org/doc/devel/release.html#go1.15">go1.15</a> in <i>The Go Programming Language Release History</i>.<br />The <b>Go 1.15.5</b> release, which is part of the update, includes security fixes.</td></tr>
  <tr><td><b>Node.js</b></td><td>Updated the Node.js platform to add support for Node versions <a href="https://nodejs.org/en/blog/release/v12.20.0/">12.20.0</a> and <a href="https://nodejs.org/en/blog/release/v12.19.1/">12.19.1</a>.<br />The <b>Node.js 12.19.1</b> release includes security fixes.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2020-12-30-linux.platforms"></a>

**Note**  
The following tables list all supported platform branches for each platform. Only Amazon Linux AMI platform branches are updated.

**Topics**
+ [Docker](#release-2020-12-30-linux.platforms.docker)
+ [Multicontainer Docker](#release-2020-12-30-linux.platforms.mcdocker)
+ [Preconfigured Docker](#release-2020-12-30-linux.platforms.dockerpreconfig)
+ [Go](#release-2020-12-30-linux.platforms.go)
+ [Java SE](#release-2020-12-30-linux.platforms.javase)
+ [Tomcat](#release-2020-12-30-linux.platforms.java)
+ [Node.js](#release-2020-12-30-linux.platforms.nodejs)
+ [PHP](#release-2020-12-30-linux.platforms.PHP)
+ [Python](#release-2020-12-30-linux.platforms.python)
+ [Ruby](#release-2020-12-30-linux.platforms.ruby)

### Docker
<a name="release-2020-12-30-linux.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Docker AL2 version 3.2.3** <br /> * 64bit Amazon Linux 2 v3.2.3 running Docker *  | 2.0.20201218 | 19.03.13-ce | nginx 1.18.0 | 
|  ** Single Container Docker version 2.16.3** <br /> * 64bit Amazon Linux 2018.03 v2.16.3 running Docker 19.03.13-ce *  | 2018.03.0 | 19.03.13-ce | nginx 1.18.0 | 

### Multicontainer Docker
<a name="release-2020-12-30-linux.platforms.mcdocker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  ECS Agent  | 
| --- | --- | --- | --- | 
|  ** Multicontainer Docker version 2.24.1** <br /> * 64bit Amazon Linux 2018.03 v2.24.1 running Multi-container Docker 19.03.13-ce (Generic) *  | 2018.03.0 | 19.03.13-ce | 1.47.0 | 

### Preconfigured Docker
<a name="release-2020-12-30-linux.platforms.dockerpreconfig"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Platform  |  Container OS  |  Language  |  Proxy Server  |  Application Server  |  Docker Image  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Glassfish 5.0 (Docker) version 2.16.3** <br /> * 64bit Amazon Linux v2.16.3 running GlassFish 5.0 Java 8 (Preconfigured - Docker) *  | 2018.03.0 | Docker 19.03.13-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.18.0 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 | 

### Go
<a name="release-2020-12-30-linux.platforms.go"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Go 1 AL2 version 3.1.4** <br /> * 64bit Amazon Linux 2 v3.1.4 running Go 1 *  | 2.0.20201218 | Go 1.15.6 | 3.2.0 | nginx 1.18.0 | 
|  ** Go 1 version 2.17.2** <br /> * 64bit Amazon Linux 2018.03 v2.17.2 running Go 1.15.6 *  | 2018.03.0 | Go 1.15.6 | 3.1.0 | nginx 1.18.0 | 

### Java SE
<a name="release-2020-12-30-linux.platforms.javase"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 11 version 3.1.4** <br /> * 64bit Amazon Linux 2 v3.1.4 running Corretto 11 *  | 2.0.20201218 | Corretto 11.0.9.12.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.18.0 | 
|  ** Corretto 8 version 3.1.4** <br /> * 64bit Amazon Linux 2 v3.1.4 running Corretto 8 *  | 2.0.20201218 | Corretto 8.272.10.3 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.18.0 | 
|  ** Java 8 version 2.11.2** <br /> * 64bit Amazon Linux 2018.03 v2.11.2 running Java 8 *  | 2018.03.0 | Java 1.8.0\_265 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0 | nginx 1.18.0 | 
|  ** Java 7 version 2.11.2** <br /> * 64bit Amazon Linux 2018.03 v2.11.2 running Java 7 *  | 2018.03.0 | Java 1.7.0\_261 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0 | nginx 1.18.0 | 

### Tomcat
<a name="release-2020-12-30-linux.platforms.java"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 11 with Tomcat 8.5 AL2 version 4.1.4** <br /> * 64bit Amazon Linux 2 v4.1.4 running Tomcat 8.5 Corretto 11 *  | 2.0.20201218 | Corretto 11.0.9.12.1 | 3.2.0 | Tomcat 8.5.58 | nginx 1.18.0 (default), Apache 2.4.46 | 
|  ** Corretto 8 with Tomcat 8.5 AL2 version 4.1.4** <br /> * 64bit Amazon Linux 2 v4.1.4 running Tomcat 8.5 Corretto 8 *  | 2.0.20201218 | Corretto 8.272.10.3 | 3.2.0 | Tomcat 8.5.58 | nginx 1.18.0 (default), Apache 2.4.46 | 
|  ** Corretto 11 with Tomcat 7 AL2 version 4.1.4** <br /> * 64bit Amazon Linux 2 v4.1.4 running Tomcat 7 Corretto 11 *  | 2.0.20201218 | Corretto 11.0.9.12.1 | 3.2.0 | Tomcat 7.0.76 | nginx 1.18.0 (default), Apache 2.4.46 | 
|  ** Corretto 8 with Tomcat 7 AL2 version 4.1.4** <br /> * 64bit Amazon Linux 2 v4.1.4 running Tomcat 7 Corretto 8 *  | 2.0.20201218 | Corretto 8.272.10.3 | 3.2.0 | Tomcat 7.0.76 | nginx 1.18.0 (default), Apache 2.4.46 | 
|  ** Java 8 with Tomcat 8.5 version 3.4.2** <br /> * 64bit Amazon Linux 2018.03 v3.4.2 running Tomcat 8.5 Java 8 *  | 2018.03.0 | Java 1.8.0\_265 | 3.1.0 | Tomcat 8.5.57 | Apache 2.4.46 (default), Nginx 1.18.0 | 
|  ** Java 7 with Tomcat 7 version 3.4.2** <br /> * 64bit Amazon Linux 2018.03 v3.4.2 running Tomcat 7 Java 7 *  | 2018.03.0 | Java 1.7.0\_261 | 3.1.0 | Tomcat 7.0.104 | Apache 2.4.46 (default), Nginx 1.18.0 | 

### Node.js
<a name="release-2020-12-30-linux.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js 12 AL2 version 5.2.4** <br /> * 64bit Amazon Linux 2 v5.2.4 running Node.js 12 *  | 2.0.20201218 | 12.20.0 (6.14.8), 12.19.1 (6.14.8), 12.19.0 (6.14.8), 12.18.4 (6.14.6), 12.18.3 (6.14.6), 12.18.2 (6.14.5), 12.18.1 (6.14.5), 12.18.0 (6.14.4), 12.17.0 (6.14.4), 12.16.3 (6.14.4), 12.16.2 (6.14.4), 12.16.1 (6.13.4), 12.16.0 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 12.13.1 (6.12.1), 12.13.0 (6.12.0), 12.12.0 (6.11.3), 12.11.1 (6.11.3), 12.11.0 (6.11.3), 12.10.0 (6.10.3), 12.9.1 (6.10.2), 12.9.0 (6.10.2), 12.8.1 (6.10.2), 12.8.0 (6.10.2), 12.7.0 (6.10.0), 12.6.0 (6.9.0), 12.5.0 (6.9.0), 12.4.0 (6.9.0), 12.3.1 (6.9.0), 12.3.0 (6.9.0), 12.2.0 (6.9.0), 12.1.0 (6.9.0), 12.0.0 (6.9.0)<br /> Default version: 12.20.0 | nginx 1.18.0 (default), Apache 2.4.46 | 2.23.3 | 3.2.0 | 
|  ** Node.js 10 AL2 version 5.2.4** <br /> * 64bit Amazon Linux 2 v5.2.4 running Node.js 10 *  | 2.0.20201218 | 10.23.0 (6.14.8), 10.22.1 (6.14.6), 10.22.0 (6.14.6), 10.21.0 (6.14.4), 10.20.1 (6.14.4), 10.20.0 (6.14.4), 10.19.0 (6.13.4), 10.18.1 (6.13.4), 10.18.0 (6.13.4), 10.17.0 (6.11.3), 10.16.3 (6.9.0), 10.16.2 (6.9.0), 10.16.1 (6.9.0), 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.2 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.2 (6.4.1), 10.14.1 (6.4.1), 10.14.0 (6.4.1), 10.13.0 (6.4.1), 10.12.0 (6.4.1), 10.11.0 (6.4.1), 10.10.0 (6.4.1), 10.9.0 (6.2.0), 10.8.0 (6.2.0), 10.7.0 (6.1.0), 10.6.0 (6.1.0), 10.5.0 (6.1.0), 10.4.1 (6.1.0), 10.4.0 (6.1.0), 10.3.0 (6.1.0), 10.2.1 (5.6.0), 10.2.0 (5.6.0), 10.1.0 (5.6.0), 10.0.0 (5.6.0)<br /> Default version: 10.23.0 | nginx 1.18.0 (default), Apache 2.4.46 | 2.23.3 | 3.2.0 | 
|  ** Node.js version 4.17.1** <br /> * 64bit Amazon Linux 2018.03 v4.17.1 running Node.js *  | 2018.03.0 | 12.20.0 (6.14.8), 12.19.1 (6.14.8), 12.19.0 (6.14.8), 12.18.4 (6.14.6),12.18.3 (6.14.6), 12.18.2 (6.14.5), 12.18.1 (6.14.5), 12.18.0 (6.14.4), 12.16.3 (6.14.4), 12.16.2 (6.14.4), 12.16.1 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 10.23.0 (6.14.8), 10.22.1 (6.14.6), 10.22.0 (6.14.6), 10.21.0 (6.14.4), 10.20.1 (6.14.4), 10.20.0(6.14.4), 10.19.0 (6.13.4), 10.18.1 (6.13.4), 10.18.0 (6.13.4), 10.17.0 (6.11.3), 10.16.3 (6.9.0), 10.16.2 (6.9.0), 10.16.1 (6.9.0), 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1)<br /> Default version: 12.20.0 | nginx 1.18.0, Apache 2.4.43 | 2.18.4 | 3.1.0 | 

### PHP
<a name="release-2020-12-30-linux.platforms.PHP"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** PHP 7.4 AL2 version 3.1.4** <br /> * 64bit Amazon Linux 2 v3.1.4 running PHP 7.4 *  | 2.0.20201218 | PHP 7.4.11 | 1.9.3 | nginx 1.18.0 (default), Apache 2.4.46 | 
|  ** PHP 7.3 AL2 version 3.1.4** <br /> * 64bit Amazon Linux 2 v3.1.4 running PHP 7.3 *  | 2.0.20201218 | PHP 7.3.23 | 1.9.3 | nginx 1.18.0 (default), Apache 2.4.46 | 
|  ** PHP 7.2 AL2 version 3.1.4** <br /> * 64bit Amazon Linux 2 v3.1.4 running PHP 7.2 *  | 2.0.20201218 | PHP 7.2.34 | 1.9.3 | nginx 1.18.0 (default), Apache 2.4.46 | 
|  ** PHP 7.3 version 2.9.13** <br /> * 64bit Amazon Linux 2018.03 v2.9.13 running PHP 7.3 *  | 2018.03.0 | PHP 7.3.23 | 1.9.0 | Apache 2.4.46 | 
|  ** PHP 7.2 version 2.9.13** <br /> * 64bit Amazon Linux 2018.03 v2.9.13 running PHP 7.2 *  | 2018.03.0 | PHP 7.2.34 | 1.9.0 | Apache 2.4.46 | 

### Python
<a name="release-2020-12-30-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.7 AL2 version 3.1.4** <br /> * 64bit Amazon Linux 2 v3.1.4 running Python 3.7 *  | 2.0.20201218 | Python 3.7.9 | pipenv 2020.8.13 |  |  | 3.2.0 | nginx 1.18.0 (default), Apache 2.4.46 | 
|  ** Python 3.6 version 2.9.17** <br /> * 64bit Amazon Linux 2018.03 v2.9.17 running Python 3.6 *  | 2018.03.0 | Python 3.6.12 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.1.0 | Apache 2.4.46 with mod\_wsgi 3.5 | 

### Ruby
<a name="release-2020-12-30-linux.platforms.ruby"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 2.7 AL2 version 3.2.1** <br /> * 64bit Amazon Linux 2 v3.2.1 running Ruby 2.7 *  | 2.0.20201218 | Ruby 2.7.2-p137 | RubyGems 3.2.0 | Puma 5.1.1 | 3.2.0 | nginx 1.18.0 | 
|  ** Ruby 2.6 AL2 version 3.2.1** <br /> * 64bit Amazon Linux 2 v3.2.1 running Ruby 2.6 *  | 2.0.20201218 | Ruby 2.6.6-p146 | RubyGems 3.2.0 | Puma 5.1.1 | 3.2.0 | nginx 1.18.0 | 
|  ** Ruby 2.5 AL2 version 3.2.1** <br /> * 64bit Amazon Linux 2 v3.2.1 running Ruby 2.5 *  | 2.0.20201218 | Ruby 2.5.8-p224 | RubyGems 3.2.0 | Puma 5.1.1 | 3.2.0 | nginx 1.18.0 | 
|  ** Ruby 2.6 with Puma version 2.12.2** <br /> * 64bit Amazon Linux 2018.03 v2.12.2 running Ruby 2.6 (Puma) *  | 2018.03.0 | Ruby 2.6.6-p146 | RubyGems 3.1.2 | Puma 2.16.0 | 3.1.0 | nginx 1.18.0 | 
|  ** Ruby 2.6 with Passenger version 2.12.2** <br /> * 64bit Amazon Linux 2018.03 v2.12.2 running Ruby 2.6 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.6.6-p146 | RubyGems 3.1.2 | Passenger 4.0.60 | 3.1.0 | nginx 1.18.0 | 
|  ** Ruby 2.5 with Puma version 2.12.2** <br /> * 64bit Amazon Linux 2018.03 v2.12.2 running Ruby 2.5 (Puma) *  | 2018.03.0 | Ruby 2.5.8-p224 | RubyGems 3.1.2 | Puma 2.16.0 | 3.1.0 | nginx 1.18.0 | 
|  ** Ruby 2.5 with Passenger version 2.12.2** <br /> * 64bit Amazon Linux 2018.03 v2.12.2 running Ruby 2.5 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.5.8-p224 | RubyGems 3.1.2 | Passenger 4.0.60 | 3.1.0 | nginx 1.18.0 | 
|  ** Ruby 2.4 with Puma version 2.12.2** <br /> * 64bit Amazon Linux 2018.03 v2.12.2 running Ruby 2.4 (Puma) *  | 2018.03.0 | Ruby 2.4.10-p364 | RubyGems 3.1.2 | Puma 2.16.0 | 3.1.0 | nginx 1.18.0 | 
|  ** Ruby 2.4 with Passenger version 2.12.2** <br /> * 64bit Amazon Linux 2018.03 v2.12.2 running Ruby 2.4 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.4.10-p364 | RubyGems 3.1.2 | Passenger 4.0.60 | 3.1.0 | nginx 1.18.0 | 