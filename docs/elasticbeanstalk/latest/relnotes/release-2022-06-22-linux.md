

# Release: Elastic Beanstalk Amazon Linux platform updates on June 22, 2022
<a name="release-2022-06-22-linux"></a>

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux. The release includes security updates. It also includes AMI, ECS based Docker, Go, .NET Core, Node.js, and PHP updates. 

**Release date:** June 22, 2022

## Changes
<a name="release-2022-06-22-linux.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/alas2.html">Amazon Linux Security Center</a> on or before <b>June 16, 2022</b> to all released Amazon Linux 2 platforms.<br />The <b>Go</b> and <b>.NET Core</b> releases are security releases. For more information, see <b>Platform-specific updates</b> in this table.</td></tr>
  <tr><td><b>Cross-platform updates</b></td><td>Made these cross-platform updates:
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Base AMI</b></td><td>Updated the base AMI to version <b>2.0.20220606</b>.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Docker</b></td><td>Updated Amazon ECS to version <b>1.61.1</b> on the <i>ECS running on Amazon Linux 2</i> platform branch.</td></tr>
  <tr><td><b>Go</b></td><td>Updated Go to release <b>1.18.3</b>. For details, see <a href="https://golang.org/doc/devel/release.html#go1.18">go1.18</a> in <i>The Go Programming Language Release History</i>.<br />The Go 1.18.3 release is a security release.</td></tr>
  <tr><td><b>.NET Core</b></td><td>Updated .NET Core to releases <a href="https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.6/6.0.6.md">6.0.6</a> and and <a href="https://github.com/dotnet/core/blob/main/release-notes/3.1/3.1.26/3.1.26.md">3.1.26</a> <br />Both .NET Core updates are security releases.</td></tr>
  <tr><td><b>Node.js</b></td><td>Updated Node.js 16 to add support for Node version <a href="https://nodejs.org/en/blog/release/v16.15.1/">16.15.1</a>.<br /></td></tr>
  <tr><td><b>PHP</b></td><td>Updated PHP 8.0 and 7.4 to releases <a href="https://www.php.net/releases/8_0_18.php">8.0.18</a> and <a href="https://www.php.net/releases/7_4_29.php">7.4.29</a>, respectively.<br /></td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2022-06-22-linux.platforms"></a>

**Topics**
+ [Docker](#release-2022-06-22-linux.platforms.docker)
+ [Go](#release-2022-06-22-linux.platforms.go)
+ [Java SE](#release-2022-06-22-linux.platforms.javase)
+ [Tomcat](#release-2022-06-22-linux.platforms.java)
+ [.NET Core on Linux](#release-2022-06-22-linux.platforms.dotnetlinux)
+ [Node.js](#release-2022-06-22-linux.platforms.nodejs)
+ [PHP](#release-2022-06-22-linux.platforms.PHP)
+ [Python](#release-2022-06-22-linux.platforms.python)
+ [Ruby](#release-2022-06-22-linux.platforms.ruby)

### Docker
<a name="release-2022-06-22-linux.platforms.docker"></a>

**Note**  
 *ECS Amazon Linux 2 v3.1.3* is running ECS Agent 1.61.1. 



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker  |  Docker Compose  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Docker AL2 version 3.4.17** <br /> * 64bit Amazon Linux 2 v3.4.17 running Docker *  | 2.0.20220606 | 20.10.13-2 | 1.29.2 | nginx 1.20.0 | 
|  ** ECS AL2 version 3.1.3** <br /> * 64bit Amazon Linux 2 v3.1.3 running ECS *  | 2.0.20220606 |  |  |  | 

### Go
<a name="release-2022-06-22-linux.platforms.go"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Go 1 AL2 version 3.5.3** <br /> * 64bit Amazon Linux 2 v3.5.3 running Go 1 *  | 2.0.20220606 | Go 1.18.3 | 3.2.0 | nginx 1.20.0 | 

### Java SE
<a name="release-2022-06-22-linux.platforms.javase"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 11 version 3.2.16** <br /> * 64bit Amazon Linux 2 v3.2.16 running Corretto 11 *  | 2.0.20220606 | Corretto 11.0.15.9.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Corretto 8 version 3.2.16** <br /> * 64bit Amazon Linux 2 v3.2.16 running Corretto 8 *  | 2.0.20220606 | Corretto 8.332.08.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 

### Tomcat
<a name="release-2022-06-22-linux.platforms.java"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 11 with Tomcat 8.5 AL2 version 4.2.16** <br /> * 64bit Amazon Linux 2 v4.2.16 running Tomcat 8.5 Corretto 11 *  | 2.0.20220606 | Corretto 11.0.15.9.1 | 3.2.0 | Tomcat 8.5.75 | nginx 1.20.0 (default), Apache 2.4.53 | 
|  ** Corretto 8 with Tomcat 8.5 AL2 version 4.2.16** <br /> * 64bit Amazon Linux 2 v4.2.16 running Tomcat 8.5 Corretto 8 *  | 2.0.20220606 | Corretto 8.332.08.1 | 3.2.0 | Tomcat 8.5.75 | nginx 1.20.0 (default), Apache 2.4.53 | 

### .NET Core on Linux
<a name="release-2022-06-22-linux.platforms.dotnetlinux"></a>



|  Platform Version and *Solution Stack Name*   |  Framework  |  Proxy Server  |  AMI  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | 
|  ** .NET Core on AL2 version 2.3.3** <br /> * 64bit Amazon Linux 2 v2.3.3 running .NET Core *  | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26 | nginx 1.20.0 | 2.0.20220606 | 3.2.0 | 

### Node.js
<a name="release-2022-06-22-linux.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js 16 AL2 version 5.5.4** <br /> * 64bit Amazon Linux 2 v5.5.4 running Node.js 16 *  | 2.0.20220606 | 16.15.1 (8.11.0), 16.15.0 (8.5.5), 16.14.2 (8.5.0), 16.14.1 (8.5.0), 16.14.0 (8.3.1), 16.13.2 (8.1.2), 16.13.1 (8.1.2), 16.13.0 (8.1.0), 16.12.0 (8.1.0), 16.11.1 (8.0.0), 16.11.0 (8.0.0), 16.10.0 (7.24.0), 16.9.1 (7.21.1), 16.9.0 (7.21.1), 16.8.0 (7.21.0), 16.7.0 (7.20.3), 16.6.2 (7.20.3), 16.6.1 (7.20.3), 16.6.0 (7.19.1), 16.5.0 (7.19.1), 16.4.2 (7.18.1), 16.4.1 (7.18.1), 16.4.0 (7.18.1), 16.3.0 (7.15.1), 16.2.0 (7.13.0), 16.1.0 (7.11.2), 16.0.0 (7.10.0)<br /> Default version: 16.15.1 | nginx 1.20.0 (default), Apache 2.4.53 | 2.32.0 | 3.2.0 | 
|  ** Node.js 14 AL2 version 5.5.4** <br /> * 64bit Amazon Linux 2 v5.5.4 running Node.js 14 *  | 2.0.20220606 | 14.19.3 (6.14.17), 14.19.2 (6.14.17), 14.19.1 (6.14.16), 14.19.0 (6.14.16), 14.18.3 (6.14.15), 14.18.2 (6.14.15), 14.18.1 (6.14.15), 14.18.0 (6.14.15), 14.17.6 (6.14.15), 14.17.5 (6.14.14), 14.17.4 (6.14.14), 14.17.3 (6.14.13), 14.17.2 (6.14.13), 14.17.1 (6.14.13), 14.17.0 (6.14.13), 14.16.1 (6.14.12), 14.16.0 (6.14.11), 14.15.5 (6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8), 14.15.0 (6.14.8), 14.14.0 (6.14.8), 14.13.1 (6.14.8), 14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0 (6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7), 14.7.0 (6.14.7), 14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0 (6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br /> Default version: 14.19.3 | nginx 1.20.0 (default), Apache 2.4.53 | 2.32.0 | 3.2.0 | 

### PHP
<a name="release-2022-06-22-linux.platforms.PHP"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** PHP 8.0 AL2 version 3.3.15** <br /> * 64bit Amazon Linux 2 v3.3.15 running PHP 8.0 *  | 2.0.20220606 | PHP 8.0.18 | 2.0.13 | nginx 1.20.0 (default), Apache 2.4.53 | 

### Python
<a name="release-2022-06-22-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.8 AL2 version 3.3.15** <br /> * 64bit Amazon Linux 2 v3.3.15 running Python 3.8 *  | 2.0.20220606 | Python 3.8.5 | pipenv 2021.11.9 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.53 | 
|  ** Python 3.7 AL2 version 3.3.15** <br /> * 64bit Amazon Linux 2 v3.3.15 running Python 3.7 *  | 2.0.20220606 | Python 3.7.10 | pipenv 2021.11.9 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.53 | 

### Ruby
<a name="release-2022-06-22-linux.platforms.ruby"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 3.0 AL2 version 3.4.8** <br /> * 64bit Amazon Linux 2 v3.4.8 running Ruby 3.0 *  | 2.0.20220606 | Ruby 3.0.4-p208 | RubyGems 3.3.15 | Puma 5.6.4 | 3.2.0 | nginx 1.20.0 | 
|  ** Ruby 2.7 AL2 version 3.4.8** <br /> * 64bit Amazon Linux 2 v3.4.8 running Ruby 2.7 *  | 2.0.20220606 | Ruby 2.7.6-p219 | RubyGems 3.3.15 | Puma 5.6.4 | 3.2.0 | nginx 1.20.0 | 