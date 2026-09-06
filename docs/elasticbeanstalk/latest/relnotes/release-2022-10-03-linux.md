

# Release: Elastic Beanstalk Amazon Linux 2 platform updates on October 3, 2022
<a name="release-2022-10-03-linux"></a>

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux 2. The release includes security updates. It also includes AMI, ECS based Docker, Go, .NET Core, Node.js, PHP, and Ruby updates. 

**Release date:** October 3, 2022

## Changes
<a name="release-2022-10-03-linux.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/alas2.html">Amazon Linux Security Center</a> on or before <b>September 14, 2022</b> to all Amazon Linux 2 platforms.<br />Some of the platform updates are security releases. For more information, see <b>Platform-specific updates</b> in this table.</td></tr>
  <tr><td><b>Cross-platform updates</b></td><td>Made these cross-platform updates:
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2.0.20220912.</td></tr>
</tbody>
</table>
<br /><a href="#release-2022-10-03-linux.platforms">All platforms in this release</a> were updated to a new minor version because the version of Go used to compile the platform engine was updated to a new major release.</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Docker</b></td><td>Updated Amazon ECS to version <b>1.62.2</b> on the <i>ECS Amazon Linux 2</i> platform branch.</td></tr>
  <tr><td><b>Go</b></td><td>Updated Go to release 1.19.1. For details, see <a href="https://go.dev/doc/devel/release#go1.19.1">go1.19.1</a> in <i>The Go Programming Language Release History</i>.<br />This is a security release.</td></tr>
  <tr><td><b>.NET Core</b></td><td>Updated .NET Core to releases <a href="https://github.com//dotnet/core/blob/main/release-notes/6.0/6.0.9/6.0.9.md#notable-changes">6.0.9</a> and <a href="https://github.com/dotnet/core/blob/master/release-notes/3.1/3.1.29/3.1.29.md#notable-changes">3.1.29</a>.<br />Both the .NET Core 6.0 and .NET Core 3.1 updates are security releases.</td></tr>
  <tr><td><b>Node.js</b></td><td>Updated Node.js 16 to add support for Node version <a href="https://nodejs.org/en/blog/release/v16.17.1/">16.17.1</a>.<br />Updated Node.js 14 to add support for Node versions <a href="https://nodejs.org/en/blog/release/v14.20.1/">14.20.1</a>.<br />The new Node.js versions are security releases. Node.js 12 is a retiring (deprecated) platform branch. For full version information of Elastic Beanstalk retiring platform branches, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html">Elastic Beanstalk platform versions scheduled for retirement</a> in the <i>AWS Elastic Beanstalk Platforms</i> guide. </td></tr>
  <tr><td><b>PHP</b></td><td>Updated PHP 8.1 release to <a href="https://www.php.net/releases/8_1_11.php">8.1.11</a>.<br />This is a security release.<br /><b>**New!**</b>— Starting with this release, Elastic Beanstalk now stores the PHP 8.1 related RPM packages on the EC2 instances in the local directory <code>/opt/elasticbeanstalk/RPMS</code>. You can use <code>rpm -i</code> to install needed packages. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_PHP.container.html#php-8-1-considerations">PHP 8.1 considerations</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>. PHP 7.4 is a retiring (deprecated) platform branch. For full version information of Elastic Beanstalk retiring platform branches, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html">Elastic Beanstalk platform versions scheduled for retirement</a> in the <i>AWS Elastic Beanstalk Platforms</i> guide. </td></tr>
  <tr><td><b>Ruby</b></td><td>Updated RubyGems to release 3.3.22. For details, see <a href="https://blog.rubygems.org/2022/09/07/3.3.22-released.html">3.3.22 Released</a> on the <i>RubyGems blog</i>. Ruby 2.6 is a retiring (deprecated) platform branch. For full version information of Elastic Beanstalk retiring platform branches, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html">Elastic Beanstalk platform versions scheduled for retirement</a> in the <i>AWS Elastic Beanstalk Platforms</i> guide. </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2022-10-03-linux.platforms"></a>

**Note**  
The following tables list all supported platform branches for each platform. Only Amazon Linux 2 platform branches are updated.

**Topics**
+ [Docker](#release-2022-10-03-linux.platforms.docker)
+ [Go](#release-2022-10-03-linux.platforms.go)
+ [Java SE](#release-2022-10-03-linux.platforms.javase)
+ [Tomcat](#release-2022-10-03-linux.platforms.java)
+ [.NET Core on Linux](#release-2022-10-03-linux.platforms.dotnetlinux)
+ [Node.js](#release-2022-10-03-linux.platforms.nodejs)
+ [PHP](#release-2022-10-03-linux.platforms.PHP)
+ [Python](#release-2022-10-03-linux.platforms.python)
+ [Ruby](#release-2022-10-03-linux.platforms.ruby)

All platforms in this release were updated to a new minor version because the version of Go used to compile the platform engine was updated to a new major release.

### Docker
<a name="release-2022-10-03-linux.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  ECS Agent  |  Docker  |  Docker Compose  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Docker AL2 version 3.5.0** <br /> * 64bit Amazon Linux 2 v3.5.0 running Docker *  | 2.0.20220912 |  | 20.10.17-1 | 1.29.2 | nginx 1.20.0 | 
|  ** ECS AL2 version 3.2.0** <br /> * 64bit Amazon Linux 2 v3.2.0 running ECS *  | 2.0.20220912 | 1.62.2 |  |  |  | 

### Go
<a name="release-2022-10-03-linux.platforms.go"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Go 1 AL2 version 3.6.0** <br /> * 64bit Amazon Linux 2 v3.6.0 running Go 1 *  | 2.0.20220912 | Go 1.19.1 | 3.2.0 | nginx 1.20.0 | 

### Java SE
<a name="release-2022-10-03-linux.platforms.javase"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 17 version 3.4.0** <br /> * 64bit Amazon Linux 2 v3.4.0 running Corretto 17 *  | 2.0.20220912 | Corretto 17.0.4.9.1 | Ant 1.10.7, Gradle 7.4.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Corretto 11 version 3.4.0** <br /> * 64bit Amazon Linux 2 v3.4.0 running Corretto 11 *  | 2.0.20220912 | Corretto 11.0.16.9.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Corretto 8 version 3.4.0** <br /> * 64bit Amazon Linux 2 v3.4.0 running Corretto 8 *  | 2.0.20220912 | Corretto 8.342.07.4 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 

### Tomcat
<a name="release-2022-10-03-linux.platforms.java"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 11 with Tomcat 8.5 AL2 version 4.3.0** <br /> * 64bit Amazon Linux 2 v4.3.0 running Tomcat 8.5 Corretto 11 *  | 2.0.20220912 | Corretto 11.0.16.9.1 | 3.2.0 | Tomcat 8.5.79 | nginx 1.20.0 (default), Apache 2.4.54 | 
|  ** Corretto 8 with Tomcat 8.5 AL2 version 4.3.0** <br /> * 64bit Amazon Linux 2 v4.3.0 running Tomcat 8.5 Corretto 8 *  | 2.0.20220912 | Corretto 8.342.07.4 | 3.2.0 | Tomcat 8.5.79 | nginx 1.20.0 (default), Apache 2.4.54 | 

### .NET Core on Linux
<a name="release-2022-10-03-linux.platforms.dotnetlinux"></a>



|  Platform Version and *Solution Stack Name*   |  Framework  |  Proxy Server  |  AMI  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | 
|  ** .NET Core on AL2 version 2.4.0** <br /> * 64bit Amazon Linux 2 v2.4.0 running .NET Core *  | .NET 6.0.9, supports 6.0.9, 5.0.17, 3.1.29 | nginx 1.20.0 | 2.0.20220912 | 3.2.0 | 

### Node.js
<a name="release-2022-10-03-linux.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js 16 AL2 version 5.6.0** <br /> * 64bit Amazon Linux 2 v5.6.0 running Node.js 16 *  | 2.0.20220912 | 16.17.1 (8.15.0), 16.17.0 (8.15.0), 16.16.0 (8.11.0), 16.15.1 (8.11.0), 16.15.0 (8.5.5), 16.14.2 (8.5.0), 16.14.1 (8.5.0), 16.14.0 (8.3.1), 16.13.2 (8.1.2), 16.13.1 (8.1.2), 16.13.0 (8.1.0), 16.12.0 (8.1.0), 16.11.1 (8.0.0), 16.11.0 (8.0.0), 16.10.0 (7.24.0), 16.9.1 (7.21.1), 16.9.0 (7.21.1), 16.8.0 (7.21.0), 16.7.0 (7.20.3), 16.6.2 (7.20.3), 16.6.1 (7.20.3), 16.6.0 (7.19.1), 16.5.0 (7.19.1), 16.4.2 (7.18.1), 16.4.1 (7.18.1), 16.4.0 (7.18.1), 16.3.0 (7.15.1), 16.2.0 (7.13.0), 16.1.0 (7.11.2), 16.0.0 (7.10.0)<br /> Default version: 16.17.1 | nginx 1.20.0 (default), Apache 2.4.54 | 2.37.1 | 3.2.0 | 
|  ** Node.js 14 AL2 version 5.6.0** <br /> * 64bit Amazon Linux 2 v5.6.0 running Node.js 14 *  | 2.0.20220912 | 14.20.1 (6.14.17), 14.20.0 (6.14.17), 14.19.3 (6.14.17), 14.19.2 (6.14.17), 14.19.1 (6.14.16), 14.19.0 (6.14.16), 14.18.3 (6.14.15), 14.18.2 (6.14.15), 14.18.1 (6.14.15), 14.18.0 (6.14.15), 14.17.6 (6.14.15), 14.17.5 (6.14.14), 14.17.4 (6.14.14), 14.17.3 (6.14.13), 14.17.2 (6.14.13), 14.17.1 (6.14.13), 14.17.0 (6.14.13), 14.16.1 (6.14.12), 14.16.0 (6.14.11), 14.15.5 (6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8), 14.15.0 (6.14.8), 14.14.0 (6.14.8), 14.13.1 (6.14.8), 14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0 (6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7), 14.7.0 (6.14.7), 14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0 (6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br /> Default version: 14.20.1 | nginx 1.20.0 (default), Apache 2.4.54 | 2.37.1 | 3.2.0 | 

### PHP
<a name="release-2022-10-03-linux.platforms.PHP"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** PHP 8.1 AL2 version 3.5.0** <br /> * 64bit Amazon Linux 2 v3.5.0 running PHP 8.1 *  | 2.0.20220912 | PHP 8.1.11 | 2.3.5 | nginx 1.20.0 (default), Apache 2.4.54 | 
|  ** PHP 8.0 AL2 version 3.5.0** <br /> * 64bit Amazon Linux 2 v3.5.0 running PHP 8.0 *  | 2.0.20220912 | PHP 8.0.20 | 2.0.13 | nginx 1.20.0 (default), Apache 2.4.54 | 

### Python
<a name="release-2022-10-03-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.8 AL2 version 3.4.0** <br /> * 64bit Amazon Linux 2 v3.4.0 running Python 3.8 *  | 2.0.20220912 | Python 3.8.5 | pipenv 2021.11.9 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.54 | 
|  ** Python 3.7 AL2 version 3.4.0** <br /> * 64bit Amazon Linux 2 v3.4.0 running Python 3.7 *  | 2.0.20220912 | Python 3.7.10 | pipenv 2021.11.9 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.54 | 

### Ruby
<a name="release-2022-10-03-linux.platforms.ruby"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 3.0 AL2 version 3.5.0** <br /> * 64bit Amazon Linux 2 v3.5.0 running Ruby 3.0 *  | 2.0.20220912 | Ruby 3.0.4-p208 | RubyGems 3.3.22 | Puma 5.6.5 | 3.2.0 | nginx 1.20.0 | 
|  ** Ruby 2.7 AL2 version 3.5.0** <br /> * 64bit Amazon Linux 2 v3.5.0 running Ruby 2.7 *  | 2.0.20220912 | Ruby 2.7.6-p219 | RubyGems 3.3.22 | Puma 5.6.5 | 3.2.0 | nginx 1.20.0 | 