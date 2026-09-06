

# Release: Elastic Beanstalk Amazon Linux AMI platform updates on May 4, 2020
<a name="release-2020-05-04-linux"></a>

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux AMI. The release includes third party security updates. It also includes Docker, Go, Node.js, and Ruby updates.

**Release date:** May 4, 2020

## Changes
<a name="release-2020-05-04-linux.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/">Amazon Linux Security Center</a> on or before <b>April 23, 2020</b> to all Amazon Linux AMI platforms.<br />The <b>Ruby</b> release includes security fixes. For more information, see <b>Platform-specific updates</b> in this table.</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Docker</b></td><td>Updated Docker to version 19.03.6-ce.<br />(Multicontainer Docker) Updated the ECS agent to version 1.39.0.</td></tr>
  <tr><td><b>Go</b></td><td>Updated Go to release 1.14.2. For details, see <a href="https://golang.org/doc/devel/release.html#go1.14">go1.14</a> in <i>The Go Programming Language Release History</i>.</td></tr>
  <tr><td><b>Node.js</b></td><td>Updated the Node.js platform to add support for Node versions <a href="https://nodejs.org/en/blog/release/v12.16.2/">12.16.2</a> and <a href="https://nodejs.org/en/blog/release/v10.20.0/">10.20.0</a>.</td></tr>
  <tr><td><b>Ruby</b></td><td>Released new Ruby 2.6, 2.5, and 2.4 versions: <a href="https://www.ruby-lang.org/en/news/2020/03/31/ruby-2-6-6-released/">2.6.6</a>, <a href="https://www.ruby-lang.org/en/news/2020/03/31/ruby-2-5-8-released/">2.5.8</a>, and <a href="https://www.ruby-lang.org/en/news/2020/03/31/ruby-2-4-10-released/">2.4.10</a>, respectively.<br />For security vulnerabilities fixed in the latest versions, see their respective Ruby release notes.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2020-05-04-linux.platforms"></a>

**Topics**
+ [Single Container Docker](#release-2020-05-04-linux.platforms.docker)
+ [Multicontainer Docker](#release-2020-05-04-linux.platforms.mcdocker)
+ [Preconfigured Docker](#release-2020-05-04-linux.platforms.dockerpreconfig)
+ [Go](#release-2020-05-04-linux.platforms.go)
+ [Java SE](#release-2020-05-04-linux.platforms.javase)
+ [Tomcat](#release-2020-05-04-linux.platforms.java)
+ [Node.js](#release-2020-05-04-linux.platforms.nodejs)
+ [PHP](#release-2020-05-04-linux.platforms.PHP)
+ [Python](#release-2020-05-04-linux.platforms.python)
+ [Ruby](#release-2020-05-04-linux.platforms.ruby)

### Single Container Docker
<a name="release-2020-05-04-linux.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Single Container Docker version 2.15.0** <br /> * 64bit Amazon Linux 2018.03 v2.15.0 running Docker 19.03.6-ce *  | 2018.03.0 | 19.03.6-ce | nginx 1.16.1 | 

### Multicontainer Docker
<a name="release-2020-05-04-linux.platforms.mcdocker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  ECS Agent  | 
| --- | --- | --- | --- | 
|  ** Multicontainer Docker version 2.20.2** <br /> * 64bit Amazon Linux 2018.03 v2.20.2 running Multi-container Docker 19.03.6-ce (Generic) *  | 2018.03.0 | 19.03.6-ce | 1.39.0 | 

### Preconfigured Docker
<a name="release-2020-05-04-linux.platforms.dockerpreconfig"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Platform  |  Container OS  |  Language  |  Proxy Server  |  Application Server  |  Docker Image  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Glassfish 5.0 (Docker) version 2.15.0** <br /> * 64bit Amazon Linux v2.15.0 running GlassFish 5.0 Java 8 (Preconfigured - Docker) *  | 2018.03.0 | Docker 19.03.6-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.16.1 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 | 

### Go
<a name="release-2020-05-04-linux.platforms.go"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Go 1.14 version 2.15.3** <br /> * 64bit Amazon Linux 2018.03 v2.15.3 running Go 1.14.2 *  | 2018.03.0 | Go 1.14.2 | 3.1.0 | nginx 1.16.1 | 

### Java SE
<a name="release-2020-05-04-linux.platforms.javase"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Java 8 version 2.10.7** <br /> * 64bit Amazon Linux 2018.03 v2.10.7 running Java 8 *  | 2018.03.0 | Java 1.8.0\_242 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0 | nginx 1.16.1 | 
|  ** Java 7 version 2.10.7** <br /> * 64bit Amazon Linux 2018.03 v2.10.7 running Java 7 *  | 2018.03.0 | Java 1.7.0\_251 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0 | nginx 1.16.1 | 

### Tomcat
<a name="release-2020-05-04-linux.platforms.java"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Java 8 with Tomcat 8.5 version 3.3.6** <br /> * 64bit Amazon Linux 2018.03 v3.3.6 running Tomcat 8.5 Java 8 *  | 2018.03.0 | Java 1.8.0\_242 | 3.1.0 | Tomcat 8.5.51 | Apache 2.4.41 (default), Apache 2.2.34, Nginx 1.16.1 | 
|  ** Java 7 with Tomcat 7 version 3.3.6** <br /> * 64bit Amazon Linux 2018.03 v3.3.6 running Tomcat 7 Java 7 *  | 2018.03.0 | Java 1.7.0\_251 | 3.1.0 | Tomcat 7.0.100 | Apache 2.4.41 (default), Apache 2.2.34, Nginx 1.16.1 | 

### Node.js
<a name="release-2020-05-04-linux.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js version 4.14.3** <br /> * 64bit Amazon Linux 2018.03 v4.14.3 running Node.js *  | 2018.03.0 | 12.16.2(6.14.4), 12.16.1 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 10.20.0(6.14.4), 10.19.0 (6.13.4), 10.18.1 (6.13.4), 10.18.0 (6.13.4), 10.17.0 (6.11.3), 10.16.3 (6.9.0), 10.16.2 (6.9.0), 10.16.1 (6.9.0), 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.17.0 (6.13.4), 8.16.2 (6.4.1), 8.16.1 (6.4.1), 8.16.0 (6.4.1), 8.15.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.17.1 (3.10.10), 6.17.0 (3.10.10), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br /> Default version: 12.16.2 | nginx 1.16.1, Apache 2.4.41 | 2.14.6 | 3.1.0 | 

### PHP
<a name="release-2020-05-04-linux.platforms.PHP"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** PHP 7.3 version 2.9.6** <br /> * 64bit Amazon Linux 2018.03 v2.9.6 running PHP 7.3 *  | 2018.03.0 | PHP 7.3.15 | 1.9.0 | Apache 2.4.41 | 
|  ** PHP 7.2 version 2.9.6** <br /> * 64bit Amazon Linux 2018.03 v2.9.6 running PHP 7.2 *  | 2018.03.0 | PHP 7.2.28 | 1.9.0 | Apache 2.4.41 | 

### Python
<a name="release-2020-05-04-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.6 version 2.9.10** <br /> * 64bit Amazon Linux 2018.03 v2.9.10 running Python 3.6 *  | 2018.03.0 | Python 3.6.10 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.1.0 | Apache 2.4.41 with mod\_wsgi 3.5 | 

### Ruby
<a name="release-2020-05-04-linux.platforms.ruby"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 2.6 with Puma version 2.11.6** <br /> * 64bit Amazon Linux 2018.03 v2.11.6 running Ruby 2.6 (Puma) *  | 2018.03.0 | Ruby 2.6.6-p146 | RubyGems 3.1.2 | Puma 2.16.0 | 3.1.0 | nginx 1.16.1 | 
|  ** Ruby 2.6 with Passenger version 2.11.6** <br /> * 64bit Amazon Linux 2018.03 v2.11.6 running Ruby 2.6 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.6.6-p146 | RubyGems 3.1.2 | Passenger 4.0.60 | 3.1.0 | nginx 1.16.1 | 
|  ** Ruby 2.5 with Puma version 2.11.6** <br /> * 64bit Amazon Linux 2018.03 v2.11.6 running Ruby 2.5 (Puma) *  | 2018.03.0 | Ruby 2.5.8-p224 | RubyGems 3.1.2 | Puma 2.16.0 | 3.1.0 | nginx 1.16.1 | 
|  ** Ruby 2.5 with Passenger version 2.11.6** <br /> * 64bit Amazon Linux 2018.03 v2.11.6 running Ruby 2.5 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.5.8-p224 | RubyGems 3.1.2 | Passenger 4.0.60 | 3.1.0 | nginx 1.16.1 | 
|  ** Ruby 2.4 with Puma version 2.11.6** <br /> * 64bit Amazon Linux 2018.03 v2.11.6 running Ruby 2.4 (Puma) *  | 2018.03.0 | Ruby 2.4.10-p364 | RubyGems 3.1.2 | Puma 2.16.0 | 3.1.0 | nginx 1.16.1 | 
|  ** Ruby 2.4 with Passenger version 2.11.6** <br /> * 64bit Amazon Linux 2018.03 v2.11.6 running Ruby 2.4 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.4.10-p364 | RubyGems 3.1.2 | Passenger 4.0.60 | 3.1.0 | nginx 1.16.1 | 