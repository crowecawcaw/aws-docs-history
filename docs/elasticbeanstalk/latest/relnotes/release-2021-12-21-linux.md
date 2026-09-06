

# Release: Elastic Beanstalk Amazon Linux platform updates on December 21, 2021
<a name="release-2021-12-21-linux"></a>

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux. The release contains security updates, including the hotpatch for Apache Log4j. It also includes AMI, Go, Corretto, Tomcat, .NET Core, Node.js, Python, and Ruby updates.

**Release date:** December 21, 2021

## Changes
<a name="release-2021-12-21-linux.changes"></a>

The following table lists the changes included in this release.

**Important**  
Elastic Beanstalk installs Log4j from the Amazon Linux default package repositories in its Tomcat platforms for Amazon Linux 1 and Amazon Linux 2. The versions of Log4j available in the Amazon Linux 1 and Amazon Linux 2 repositories are not affected by [CVE-2021-44228](https://www.cve.org/CVERecord?id=CVE-2021-44228) or [CVE-2021-45046](https://www.cve.org/CVERecord?id=CVE-2021-45046) in their default configuration.  
*If you've made configuration changes to your application’s use of log4j, or installed newer versions of log4j, then we recommend that you take action to update your application’s code to mitigate this issue.*  
Out of caution, Elastic Beanstalk is releasing new platform versions that use the latest Amazon Linux default package repositories, which include the [Log4j hotpatched JDK](https://aws.amazon.com/blogs/opensource/hotpatch-for-apache-log4j/), in today's release. If you've customized log4j installation as your application dependency, we recommend that you upgrade to the latest Elastic Beanstalk platform version to mitigate CVE-2021-44228 or CVE-2021-45046. You can also enable automated managed updates as part of normal update practices.  
For more information about security-related software updates for Amazon Linux, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/).

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/alas2.html">Amazon Linux Security Center</a> on or before <b>December 17, 2021</b> to all released Amazon Linux 2 platforms.<br />In particular, the release includes the <a href="https://alas.aws.amazon.com/announcements/2021-001.html">Amazon Linux hotpatch tool for Apache Log4j</a>. This tool can help mitigate recently discovered Log4j vulnerabilities. See the <b>Important</b> message at the top of this release note page.<br />The <b>Go</b>, <b>Corretto</b>, <b>.NET Core</b>, and <b>Ruby</b> releases are security releases. For more information, see <b>Platform-specific updates</b> in this table.</td></tr>
  <tr><td><b>Cross-platform updates</b></td><td>Made these cross-platform updates:
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Base AMI</b></td><td>Updated the base AMI to version <b>2.0.20211201</b>.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Go</b></td><td>Updated Go to release <b>1.17.5</b>. For details, see <a href="https://golang.org/doc/devel/release.html#go1.17">go1.17</a> in <i>The Go Programming Language Release History</i>.<br />The Go 1.17.5 release is a security release.</td></tr>
  <tr><td><b>Corretto</b>, <b>Tomcat</b></td><td>Updated Corretto 11 to version <b>11.0.13.8.2</b>. For more information, see <a href="https://github.com/corretto/corretto-11/blob/develop/CHANGELOG.md">Change Log for Amazon Corretto 11</a> in the Corretto 11 repository on GitHub.<br />Updated Corretto 8 to version <b>8.312.07.2</b>. For more information, see <a href="https://github.com/corretto/corretto-8/blob/develop/CHANGELOG.md">Change Log for Amazon Corretto 8</a> in the Corretto 8 repository on GitHub.<br />Both Corretto updates are security releases.</td></tr>
  <tr><td><b>.NET Core</b></td><td>Updated .NET Core to releases <a href="https://github.com/dotnet/core/blob/master/release-notes/5.0/5.0.13/5.0.13.md">5.0.13</a> and <a href="https://github.com/dotnet/core/blob/master/release-notes/3.1/3.1.22/3.1.22.md">3.1.22</a>. <br />Both .NET Core updates are security releases.</td></tr>
  <tr><td><b>Node.js</b></td><td>Updated Node.js 14 to add support for Node version <a href="https://nodejs.org/en/blog/release/v14.18.2/">14.18.2</a>.<br />Updated Node.js 12 to add support for Node version <a href="https://nodejs.org/en/blog/release/v12.22.8/">12.22.8</a>.</td></tr>
  <tr><td><b>Python</b></td><td>Updated Pipenv to release <b>2021.11.9</b>. For details, see the Pipenv <a href="https://pipenv.pypa.io/en/latest/changelog/">Release and Version History</a>.</td></tr>
  <tr><td><b>Ruby</b></td><td>Updated Ruby 3.0, 2.7, and 2.6 to releases <a href="https://www.ruby-lang.org/en/news/2021/11/24/ruby-3-0-3-released/">3.0.3</a>, <a href="https://www.ruby-lang.org/en/news/2021/11/24/ruby-2-7-5-released/">2.7.5</a>, and <a href="https://www.ruby-lang.org/en/news/2021/11/24/ruby-2-6-9-released/">2.6.9</a>, respectively.<br />Updated RubyGems to release <a href="https://blog.rubygems.org/2021/11/23/3.2.32-released.html">3.2.32</a>.<br />The three Ruby updates are security releases.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2021-12-21-linux.platforms"></a>

**Topics**
+ [Docker](#release-2021-12-21-linux.platforms.docker)
+ [Go](#release-2021-12-21-linux.platforms.go)
+ [Java SE](#release-2021-12-21-linux.platforms.javase)
+ [Tomcat](#release-2021-12-21-linux.platforms.java)
+ [.NET Core on Linux](#release-2021-12-21-linux.platforms.dotnetlinux)
+ [Node.js](#release-2021-12-21-linux.platforms.nodejs)
+ [PHP](#release-2021-12-21-linux.platforms.PHP)
+ [Python](#release-2021-12-21-linux.platforms.python)
+ [Ruby](#release-2021-12-21-linux.platforms.ruby)

### Docker
<a name="release-2021-12-21-linux.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker  |  Docker Compose  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Docker AL2 version 3.4.10** <br /> * 64bit Amazon Linux 2 v3.4.10 running Docker *  | 2.0.20211201 | 20.10.7-3 | 1.29.2 | nginx 1.20.0 | 

### Go
<a name="release-2021-12-21-linux.platforms.go"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Go 1 AL2 version 3.4.4** <br /> * 64bit Amazon Linux 2 v3.4.4 running Go 1 *  | 2.0.20211201 | Go 1.17.5 | 3.2.0 | nginx 1.20.0 | 

### Java SE
<a name="release-2021-12-21-linux.platforms.javase"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 11 version 3.2.9** <br /> * 64bit Amazon Linux 2 v3.2.9 running Corretto 11 *  | 2.0.20211201 | Corretto 11.0.13.8.2 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Corretto 8 version 3.2.9** <br /> * 64bit Amazon Linux 2 v3.2.9 running Corretto 8 *  | 2.0.20211201 | Corretto 8.312.07.2 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 

### Tomcat
<a name="release-2021-12-21-linux.platforms.java"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 11 with Tomcat 8.5 AL2 version 4.2.9** <br /> * 64bit Amazon Linux 2 v4.2.9 running Tomcat 8.5 Corretto 11 *  | 2.0.20211201 | Corretto 11.0.13.8.2 | 3.2.0 | Tomcat 8.5.72 | nginx 1.20.0 (default), Apache 2.4.51 | 
|  ** Corretto 8 with Tomcat 8.5 AL2 version 4.2.9** <br /> * 64bit Amazon Linux 2 v4.2.9 running Tomcat 8.5 Corretto 8 *  | 2.0.20211201 | Corretto 8.312.07.2 | 3.2.0 | Tomcat 8.5.72 | nginx 1.20.0 (default), Apache 2.4.51 | 

### .NET Core on Linux
<a name="release-2021-12-21-linux.platforms.dotnetlinux"></a>



|  Platform Version and *Solution Stack Name*   |  Framework  |  Proxy Server  |  AMI  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | 
|  ** .NET Core on AL2 version 2.2.9** <br /> * 64bit Amazon Linux 2 v2.2.9 running .NET Core *  | .NET 5.0.13, supports 5.0.13, 3.1.22, 2.1.30 | nginx 1.20.0 | 2.0.20211201 | 3.2.0 | 

### Node.js
<a name="release-2021-12-21-linux.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js 14 AL2 version 5.4.9** <br /> * 64bit Amazon Linux 2 v5.4.9 running Node.js 14 *  | 2.0.20211201 | 14.18.2 (6.14.15), 14.18.1 (6.14.15), 14.18.0 (6.14.15), 14.17.6 (6.14.15), 14.17.5 (6.14.14), 14.17.4 (6.14.14), 14.17.3 (6.14.13), 14.17.2 (6.14.13), 14.17.1 (6.14.13), 14.17.0 (6.14.13), 14.16.1 (6.14.12), 14.16.0 (6.14.11), 14.15.5 (6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8), 14.15.0 (6.14.8), 14.14.0 (6.14.8), 14.13.1 (6.14.8), 14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0 (6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7), 14.7.0 (6.14.7), 14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0 (6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br /> Default version: 14.18.2 | nginx 1.20.0 (default), Apache 2.4.51 | 2.32.0 | 3.2.0 | 
|  ** Node.js 12 AL2 version 5.4.9** <br /> * 64bit Amazon Linux 2 v5.4.9 running Node.js 12 *  | 2.0.20211201 | 12.22.8 (6.14.15), 12.22.7 (6.14.15), 12.22.6 (6.14.15), 12.22.5 (6.14.14), 12.22.4 (6.14.14), 12.22.3 (6.14.13), 12.22.2 (6.14.13), 12.22.1 (6.14.12), 12.22.0 (6.14.11), 12.21.0 (6.14.11), 12.20.2 (6.14.11), 12.20.1 (6.14.10), 12.20.0 (6.14.8), 12.19.1 (6.14.8), 12.19.0 (6.14.8), 12.18.4 (6.14.6), 12.18.3 (6.14.6), 12.18.2 (6.14.5), 12.18.1 (6.14.5), 12.18.0 (6.14.4), 12.17.0 (6.14.4), 12.16.3 (6.14.4), 12.16.2 (6.14.4), 12.16.1 (6.13.4), 12.16.0 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 12.13.1 (6.12.1), 12.13.0 (6.12.0), 12.12.0 (6.11.3), 12.11.1 (6.11.3), 12.11.0 (6.11.3), 12.10.0 (6.10.3), 12.9.1 (6.10.2), 12.9.0 (6.10.2), 12.8.1 (6.10.2), 12.8.0 (6.10.2), 12.7.0 (6.10.0), 12.6.0 (6.9.0), 12.5.0 (6.9.0), 12.4.0 (6.9.0), 12.3.1 (6.9.0), 12.3.0 (6.9.0), 12.2.0 (6.9.0), 12.1.0 (6.9.0), 12.0.0 (6.9.0)<br /> Default version: 12.22.8 | nginx 1.20.0 (default), Apache 2.4.51 | 2.32.0 | 3.2.0 | 

### PHP
<a name="release-2021-12-21-linux.platforms.PHP"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** PHP 8.0 AL2 version 3.3.9** <br /> * 64bit Amazon Linux 2 v3.3.9 running PHP 8.0 *  | 2.0.20211201 | PHP 8.0.8 | 2.0.13 | nginx 1.20.0 (default), Apache 2.4.51 | 
|  ** PHP 7.4 AL2 version 3.3.9** <br /> * 64bit Amazon Linux 2 v3.3.9 running PHP 7.4 *  | 2.0.20211201 | PHP 7.4.21 | 1.10.22 | nginx 1.20.0 (default), Apache 2.4.51 | 

### Python
<a name="release-2021-12-21-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.8 AL2 version 3.3.9** <br /> * 64bit Amazon Linux 2 v3.3.9 running Python 3.8 *  | 2.0.20211201 | Python 3.8.5 | pipenv 2021.11.9 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.51 | 
|  ** Python 3.7 AL2 version 3.3.9** <br /> * 64bit Amazon Linux 2 v3.3.9 running Python 3.7 *  | 2.0.20211201 | Python 3.7.10 | pipenv 2021.11.9 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.51 | 

### Ruby
<a name="release-2021-12-21-linux.platforms.ruby"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 3.0 AL2 version 3.4.1** <br /> * 64bit Amazon Linux 2 v3.4.1 running Ruby 3.0 *  | 2.0.20211201 | Ruby 3.0.3-p157 | RubyGems 3.2.32 | Puma 5.5.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Ruby 2.7 AL2 version 3.4.1** <br /> * 64bit Amazon Linux 2 v3.4.1 running Ruby 2.7 *  | 2.0.20211201 | Ruby 2.7.5-p203 | RubyGems 3.2.32 | Puma 5.5.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Ruby 2.6 AL2 version 3.4.1** <br /> * 64bit Amazon Linux 2 v3.4.1 running Ruby 2.6 *  | 2.0.20211201 | Ruby 2.6.9-p207 | RubyGems 3.2.32 | Puma 5.5.2 | 3.2.0 | nginx 1.20.0 | 