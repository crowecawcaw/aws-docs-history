

# Release: Elastic Beanstalk Linux-based platform updates on October 17, 2019
<a name="release-2019-10-17-linux"></a>

This release provides new Linux-based platform versions for AWS Elastic Beanstalk. The release includes security updates. It also includes Multicontainer Docker, Go, Node.js, PHP, and Ruby updates and an nginx update.

**Release date:** October 17, 2019

## Changes
<a name="release-2019-10-17-linux.changes"></a>


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/">Amazon Linux Security Center</a> on or before <b>October 9, 2019</b> to all Linux-based platforms.<br />The <b>nginx</b> release includes security fixes. For more information, see <b>Cross-platform updates</b> in this table.<br />The <b>Ruby</b> release includes security fixes. For more information, see <b>Platform-specific updates</b> in this table.</td></tr>
  <tr><td><b>Cross-platform updates</b></td><td>Made these cross-platform updates:
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>nginx</b></td><td>Updated platforms supporting the nginx server to <a href="https://nginx.org/en/CHANGES-1.16">version 1.16.1</a>.<br />This version includes security fixes.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Multicontainer Docker</b></td><td>Updated the ECS agent to version 1.32.0.</td></tr>
  <tr><td><b>Go</b></td><td>Updated to Go release 1.13.1. For details, see <a href="https://golang.org/doc/devel/release.html#go1.13">go1.13</a> in <i>The Go Programming Language Release History</i>.</td></tr>
  <tr><td><b>Node.js</b></td><td>Updated the Node.js platform to add support for Node version <a href="https://nodejs.org/en/blog/release/v8.16.2/">8.16.2</a>.</td></tr>
  <tr><td><b>PHP</b></td><td>Added support for PHP 7.3. For migration information, see <a href="https://www.php.net/manual/en/migration73.php">Migrating from PHP 7.2.x to PHP 7.3.x</a> in the <i>PHP Manual</i>. PHP 7.3 is released side-by-side with PHP 7.2, which is still supported. Some PECL packages for PHP 7.3 aren't available in the Amazon Linux repository. Therefore, they aren't included in our platform. If your application depends on them, you'll need to add commands to install them. </td></tr>
  <tr><td><b>Ruby</b></td><td>Released new Ruby 2.6, 2.5, and 2.4 versions: <a href="https://www.ruby-lang.org/en/news/2019/10/01/ruby-2-6-5-released/">2.6.5</a>, <a href="https://www.ruby-lang.org/en/news/2019/10/01/ruby-2-5-7-released/">2.5.7</a>, and <a href="https://www.ruby-lang.org/en/news/2019/10/02/ruby-2-4-9-released/">2.4.9</a>, respectively.<br />These versions include security fixes.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2019-10-17-linux.platforms"></a>

**Topics**
+ [Packer Builder](#release-2019-10-17-linux.platforms.packer)
+ [Single Container Docker](#release-2019-10-17-linux.platforms.docker)
+ [Multicontainer Docker](#release-2019-10-17-linux.platforms.mcdocker)
+ [Preconfigured Docker](#release-2019-10-17-linux.platforms.dockerpreconfig)
+ [Go](#release-2019-10-17-linux.platforms.go)
+ [Java SE](#release-2019-10-17-linux.platforms.javase)
+ [Java with Tomcat](#release-2019-10-17-linux.platforms.java)
+ [Node.js](#release-2019-10-17-linux.platforms.nodejs)
+ [PHP](#release-2019-10-17-linux.platforms.PHP)
+ [Python](#release-2019-10-17-linux.platforms.python)
+ [Ruby](#release-2019-10-17-linux.platforms.ruby)

### Packer Builder
<a name="release-2019-10-17-linux.platforms.packer"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Packer Version  | 
| --- | --- | --- | 
|  ** Elastic Beanstalk Packer Builder version 2.6.16** <br /> * 64bit Amazon Linux 2018.03 v2.6.16 running Packer 1.0.3 *  | 2018.03.0 | 1.0.3 | 

### Single Container Docker
<a name="release-2019-10-17-linux.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Single Container Docker 18.06 version 2.13.0** <br /> * 64bit Amazon Linux 2018.03 v2.13.0 running Docker 18.06.1-ce *  | 2018.03.0 | 18.06.1-ce | nginx 1.16.1 | 

### Multicontainer Docker
<a name="release-2019-10-17-linux.platforms.mcdocker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  ECS Agent  | 
| --- | --- | --- | --- | 
|  ** Multicontainer Docker 18.06 version 2.17.0** <br /> * 64bit Amazon Linux 2018.03 v2.17.0 running Multi-container Docker 18.06.1-ce (Generic) *  | 2018.03.0 | 18.06.1-ce | 1.32.0 | 

### Preconfigured Docker
<a name="release-2019-10-17-linux.platforms.dockerpreconfig"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Platform  |  Container OS  |  Language  |  Proxy Server  |  Application Server  |  Docker Image  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Glassfish 5.0 (Docker) version 2.13.0** <br /> * 64bit Amazon Linux v2.13.0 running GlassFish 5.0 Java 8 (Preconfigured - Docker) *  | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.16.1 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 | 

### Go
<a name="release-2019-10-17-linux.platforms.go"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Go 1.13 version 2.14.0** <br /> * 64bit Amazon Linux 2018.03 v2.14.0 running Go 1.13.1 *  | 2018.03.0 | Go 1.13.1 | 3.1.0 | nginx 1.16.1 | 

### Java SE
<a name="release-2019-10-17-linux.platforms.javase"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Java 8 version 2.10.0** <br /> * 64bit Amazon Linux 2018.03 v2.10.0 running Java 8 *  | 2018.03.0 | Java 1.8.0\_222 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0 | nginx 1.16.1 | 
|  ** Java 7 version 2.10.0** <br /> * 64bit Amazon Linux 2018.03 v2.10.0 running Java 7 *  | 2018.03.0 | Java 1.7.0\_231 | Ant 1.9.6, Gradle 2.7, Maven 3.3.3 | 3.1.0 | nginx 1.16.1 | 

### Java with Tomcat
<a name="release-2019-10-17-linux.platforms.java"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Java 8 with Tomcat 8.5 version 3.3.0** <br /> * 64bit Amazon Linux 2018.03 v3.3.0 running Tomcat 8.5 Java 8 *  | 2018.03.0 | Java 1.8.0\_222 | 3.1.0 | Tomcat 8.5.42 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.16.1 | 
|  ** Java 7 with Tomcat 7 version 3.3.0** <br /> * 64bit Amazon Linux 2018.03 v3.3.0 running Tomcat 7 Java 7 *  | 2018.03.0 | Java 1.7.0\_231 | 3.1.0 | Tomcat 7.0.94 | Apache 2.4.39 (default), Apache 2.2.34, Nginx 1.16.1 | 

### Node.js
<a name="release-2019-10-17-linux.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js version 4.11.0** <br /> * 64bit Amazon Linux 2018.03 v4.11.0 running Node.js *  | 2018.03.0 | 10.16.3 (6.9.0), 10.16.2 (6.9.0), 10.16.1 (6.9.0), 10.16.0 (6.9.0), 10.15.3 (6.4.1), 10.15.1 (6.4.1), 10.15.0 (6.4.1), 10.14.1 (6.4.1), 8.16.2 (6.4.1), 8.16.1 (6.4.1), 8.16.0 (6.4.1), 8.15.1 (6.4.1), 8.15.0 (6.4.1), 8.14.0 (6.4.1), 7.10.1 (4.2.0), 6.17.1 (3.10.10), 6.17.0 (3.10.10), 6.16.0 (3.10.10), 6.15.1 (3.10.10), 5.12.0 (3.8.6), 4.9.1 (2.15.11), 4.8.7 (2.15.11)<br /> Default version: 10.16.3 | nginx 1.16.1, Apache 2.4.39 | 2.14.5 | 3.1.0 | 

### PHP
<a name="release-2019-10-17-linux.platforms.PHP"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** PHP 7.3 version 2.9.0** <br /> * 64bit Amazon Linux 2018.03 v2.9.0 running PHP 7.3 *  | 2018.03.0 | PHP 7.3.9 | 1.4.2 | Apache 2.4.39 | 
|  ** PHP 7.2 version 2.9.0** <br /> * 64bit Amazon Linux 2018.03 v2.9.0 running PHP 7.2 *  | 2018.03.0 | PHP 7.2.22 | 1.4.2 | Apache 2.4.39 | 

### Python
<a name="release-2019-10-17-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.6 version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Python 3.6 *  | 2018.03.0 | Python 3.6.8 | pip 9.0.3 | setuptools 28.8.0 | meld3 1.0.2 | 3.1.0 | Apache 2.4.39 with mod\_wsgi 3.5 | 

### Ruby
<a name="release-2019-10-17-linux.platforms.ruby"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 2.6 with Puma version 2.11.0** <br /> * 64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.6 (Puma) *  | 2018.03.0 | Ruby 2.6.5-p114 | RubyGems 3.0.3 | Puma 2.16.0 | 3.1.0 | nginx 1.16.1 | 
|  ** Ruby 2.6 with Passenger version 2.11.0** <br /> * 64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.6 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.6.5-p114 | RubyGems 3.0.3 | Passenger 4.0.60 | 3.1.0 | nginx 1.16.1 | 
|  ** Ruby 2.5 with Puma version 2.11.0** <br /> * 64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.5 (Puma) *  | 2018.03.0 | Ruby 2.5.7-p206 | RubyGems 2.7.9 | Puma 2.16.0 | 3.1.0 | nginx 1.16.1 | 
|  ** Ruby 2.5 with Passenger version 2.11.0** <br /> * 64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.5 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.5.7-p206 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.1.0 | nginx 1.16.1 | 
|  ** Ruby 2.4 with Puma version 2.11.0** <br /> * 64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.4 (Puma) *  | 2018.03.0 | Ruby 2.4.9-p362 | RubyGems 2.7.9 | Puma 2.16.0 | 3.1.0 | nginx 1.16.1 | 
|  ** Ruby 2.4 with Passenger version 2.11.0** <br /> * 64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.4 (Passenger Standalone) *  | 2018.03.0 | Ruby 2.4.9-p362 | RubyGems 2.7.9 | Passenger 4.0.60 | 3.1.0 | nginx 1.16.1 | 