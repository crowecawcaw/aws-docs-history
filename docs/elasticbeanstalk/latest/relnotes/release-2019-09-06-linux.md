

# Release: Elastic Beanstalk Linux-based platform updates on September 6, 2019
<a name="release-2019-09-06-linux"></a>

This release provides new Linux-based platform versions for AWS Elastic Beanstalk. The release includes security updates. It also includes Multicontainer Docker, Go, Java, Node.js, and Ruby updates.

**Release date:** September 6, 2019

## Changes
<a name="release-2019-09-06-linux.changes"></a>


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/">Amazon Linux Security Center</a> on or before <b>August 26, 2019</b> to all Linux-based platforms.<br />The <b>Node.js</b> and <b>Ruby</b> releases include security updates. For more information, see <b>Platform-specific updates</b> in this table.</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Multicontainer Docker</b></td><td>Updated the ECS agent to version 1.30.0.</td></tr>
  <tr><td><b>Go</b></td><td>Updated to Go release 1.13. For details, see <a href="https://golang.org/doc/devel/release.html#go1.13">go1.13</a> in <i>The Go Programming Language Release History</i>.</td></tr>
  <tr><td><b>Java SE</b>, <b>Java with Tomcat</b></td><td>Updated the Java 8 platform versions to OpenJDK Version 1.8.0.222.b10.<br />Updated the Java 7 platform versions to OpenJDK Version 1.7.0.231.</td></tr>
  <tr><td><b>Node.js</b></td><td>Updated the Node.js platform to add support for Node versions <a href="https://nodejs.org/en/blog/release/v10.16.3/">10.16.3</a>, <a href="https://nodejs.org/en/blog/release/v10.16.2/">10.16.2</a>, <a href="https://nodejs.org/en/blog/release/v10.16.1/">10.16.1</a>, and <a href="https://nodejs.org/en/blog/release/v8.16.1/">8.16.1</a>.<br />The latest Node.js 10 and Node.js 8 versions are security releases and include fixes for vulnerabilities.</td></tr>
  <tr><td><b>Ruby</b></td><td>Released new Ruby 2.6, 2.5, and 2.4 versions: <a href="https://www.ruby-lang.org/en/news/2019/08/28/ruby-2-6-4-released/">2.6.4</a>, <a href="https://www.ruby-lang.org/en/news/2019/08/28/ruby-2-5-6-released/">2.5.6</a>, and <a href="https://www.ruby-lang.org/en/news/2019/08/28/ruby-2-4-7-released/">2.4.7</a>, respectively.<br />For security vulnerabilities fixed in the latest versions, see <a href="https://www.ruby-lang.org/en/news/2019/08/28/multiple-jquery-vulnerabilities-in-rdoc/">Multiple jQuery vulnerabilities in RDoc</a>. Update – September 18, 2019: Due to a <a href="https://bugs.ruby-lang.org/issues/16136">bug</a> in the Ruby 2.6.4 runtime, we had to roll back two platform versions: <b>Ruby 2.6 with Puma</b> and <b>Ruby 2.6 with Passenger</b>. Both are back to version 2.10.1 with Ruby 2.6.3. <br />If you're already using version 2.10.2 of one of the Ruby 2.6 platforms, you still have access to this latest version. All other customers now see version 2.10.1 as the latest Ruby 2.6 version. </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2019-09-06-linux.platforms"></a>

**Topics**
+ [Packer Builder](#release-2019-09-06-linux.platforms.packer)
+ [Single Container Docker](#release-2019-09-06-linux.platforms.docker)
+ [Multicontainer Docker](#release-2019-09-06-linux.platforms.mcdocker)
+ [Preconfigured Docker](#release-2019-09-06-linux.platforms.dockerpreconfig)
+ [Go](#release-2019-09-06-linux.platforms.go)
+ [Java SE](#release-2019-09-06-linux.platforms.javase)
+ [Java with Tomcat](#release-2019-09-06-linux.platforms.java)
+ [Node.js](#release-2019-09-06-linux.platforms.nodejs)
+ [PHP](#release-2019-09-06-linux.platforms.PHP)
+ [Python](#release-2019-09-06-linux.platforms.python)
+ [Ruby](#release-2019-09-06-linux.platforms.ruby)

### Packer Builder
<a name="release-2019-09-06-linux.platforms.packer"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Packer Version  | 
| --- | --- | --- | 
|  ** Elastic Beanstalk Packer Builder version 2.6.15** <br /> * 64bit Amazon Linux 2018.03 v2.6.15 running Packer 1.0.3 *  | 2018.03.0 | 1.0.3 | 

### Single Container Docker
<a name="release-2019-09-06-linux.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Single Container Docker 18.06 version 2.12.17** <br /> * 64bit Amazon Linux 2018.03 v2.12.17 running Docker 18.06.1-ce *  | 2018.03.0 | 18.06.1-ce | nginx 1.14.1 | 

### Multicontainer Docker
<a name="release-2019-09-06-linux.platforms.mcdocker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  ECS Agent  | 
| --- | --- | --- | --- | 
|  ** Multicontainer Docker 18.06 version 2.16.0** <br /> * 64bit Amazon Linux 2018.03 v2.16.0 running Multi-container Docker 18.06.1-ce (Generic) *  | 2018.03.0 | 18.06.1-ce | 1.30.0 | 

### Preconfigured Docker
<a name="release-2019-09-06-linux.platforms.dockerpreconfig"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Platform  |  Container OS  |  Language  |  Proxy Server  |  Application Server  |  Docker Image  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Glassfish 5.0 (Docker) version 2.12.17** <br /> * 64bit Amazon Linux v2.12.17 running GlassFish 5.0 Java 8 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.14.1 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 | 

### Go
<a name="release-2019-09-06-linux.platforms.go"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Go 1.13 version 2.13.0** <br /> * 64bit Amazon Linux 2018.03 v2.13.0 running Go 1.13 *  | 2018.03.0 | Go 1.13 | 3.1.0 | nginx 1.14.1 | 

### Java SE
<a name="release-2019-09-06-linux.platforms.javase"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Java 8 version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Java 8 *  | 2018.03.0 | Java 1.8.0\_222 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0 | nginx 1.14.1 | 
|  ** Java 7 version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Java 7 *  | 2018.03.0 | Java 1.7.0\_231 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0 | nginx 1.14.1 | 

### Java with Tomcat
<a name="release-2019-09-06-linux.platforms.java"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Java 8 with Tomcat 8.5 version 3.2.2** <br /> * 64bit Amazon Linux 2018.03 v3.2.2 running Tomcat 8.5 Java 8 *  | 2018.03.0 | Java 1.8.0\_222 | 3.1.0 | Tomcat 8.5.42 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 | 
|  ** Java 7 with Tomcat 7 version 3.2.2** <br /> * 64bit Amazon Linux 2018.03 v3.2.2 running Tomcat 7 Java 7 *  | 2018.03.0 | Java 1.7.0\_231 | 3.1.0 | Tomcat 7.0.94 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.14.1 | 

### Node.js
<a name="release-2019-09-06-linux.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js version 4.10.2** <br /> * 64bit Amazon Linux 2018.03 v4.10.2 running Node.js *  | 2018.03.0 | 10.16.3 (6.9.0), 10.16.2 (6.9.0), 10.16.1 (6.9.0), 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.16.1 (6.4.1), 8.16.0 (6.4.1), 8.15.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.17.1 (3.10.10), 6.17.0 (3.10.10), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br /> Default version: 10.16.3 | nginx 1.14.1, Apache 2.4.39 | 2.14.5 | 3.1.0 | 

### PHP
<a name="release-2019-09-06-linux.platforms.PHP"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** PHP 7.2 version 2.8.15** <br /> * 64bit Amazon Linux 2018.03 v2.8.15 running PHP 7.2 *  | 2018.03.0 | PHP 7.2.19 | 1.4.2 | Apache 2.4.39 | 

### Python
<a name="release-2019-09-06-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.6 version 2.9.2** <br /> * 64bit Amazon Linux 2018.03 v2.9.2 running Python 3.6 *  | 2018.03.0 | Python 3.6.8 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.1.0 | Apache 2.4.39 with mod\_wsgi 3.5 | 

### Ruby
<a name="release-2019-09-06-linux.platforms.ruby"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 2.6 with Puma version 2.10.1** <br /> * 64bit Amazon Linux 2018.03 v2.10.1 running Ruby 2.6 (Puma) *  | 2018.03.0 | Ruby 2.6.3-p62 | RubyGems 2.7.9 | Puma 2.16.0 | 3.1.0 | nginx 1.14.1 | 
|  ** Ruby 2.6 with Passenger version 2.10.1** <br /> * 64bit Amazon Linux 2018.03 v2.10.1 running Ruby 2.6 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.6.3-p62 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.1.0 | nginx 1.14.1 | 
|  ** Ruby 2.5 with Puma version 2.10.2** <br /> * 64bit Amazon Linux 2018.03 v2.10.2 running Ruby 2.5 (Puma) *  | 2018.03.0 | Ruby 2.5.6-p201 | RubyGems 2.7.9 | Puma 2.16.0 | 3.1.0 | nginx 1.14.1 | 
|  ** Ruby 2.5 with Passenger version 2.10.2** <br /> * 64bit Amazon Linux 2018.03 v2.10.2 running Ruby 2.5 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.5.6-p201 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.1.0 | nginx 1.14.1 | 
|  ** Ruby 2.4 with Puma version 2.10.2** <br /> * 64bit Amazon Linux 2018.03 v2.10.2 running Ruby 2.4 (Puma) *  | 2018.03.0 | Ruby 2.4.7-p357 | RubyGems 2.7.9 | Puma 2.16.0 | 3.1.0 | nginx 1.14.1 | 
|  ** Ruby 2.4 with Passenger version 2.10.2** <br /> * 64bit Amazon Linux 2018.03 v2.10.2 running Ruby 2.4 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.4.7-p357 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.1.0 | nginx 1.14.1 | 