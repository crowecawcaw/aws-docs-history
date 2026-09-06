

# Release: Elastic Beanstalk Amazon Linux platform updates on February 3, 2022
<a name="release-2022-02-03-linux"></a>

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux. The release includes security updates, and it includes updates to AMI, Apache httpd, Docker, Go, Corretto, Node.js, PHP, and Ruby. It also introduces functionality to provide a consistent *webapp* userid and group id across platform updates.

**Release date:** February 3, 2022

## Changes
<a name="release-2022-02-03-linux.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/alas2.html">Amazon Linux Security Center</a> on or before <b>January 21, 2022</b> to all released Amazon Linux 2 platforms.<br />The <b>Apache httpd</b>, <b>Node.js</b>, and <b>PHP</b> releases are security releases. For more information, see <b>Cross-platform updates</b> and <b>Platform-specific updates</b> in this table.</td></tr>
  <tr><td><b>Cross-platform updates</b></td><td>Made these cross-platform updates:
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b><i>**New!**</i> Consistent <i>webapp</i> user for persistent storage permissions</b></td><td>Elastic Beanstalk assigns the <i>webapp</i> user a uid (user id) and gid (group id) value of 900 for new environments. It does the same for existing environments following a platform version update. This approach allows the <i>webapp</i> user to remain consistent across platform updates. Access permission for the <i>webapp</i> user to permanent file system storage also remains consistent as a result. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.concepts.design.html#concepts.concepts.design.storage">Persistent storage</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>. Customers with existing Amazon EFS file systems that rely on a specific <i>webapp</i> user uid or gid other than 900 should be aware that the uid and gid value will change to 900 with this platform update. Please refer to this <a href="https://github.com/aws/elastic-beanstalk-roadmap/issues/137">GitHub issue</a> for more information regarding this platform update.  </td></tr>
  <tr><td><b>Base AMI</b></td><td>Updated the base AMI to version <b>2.0.20220121</b>.</td></tr>
  <tr><td><b>Apache httpd</b></td><td>Updated platforms supporting the Apache HTTP Server 2.4 to version <b>2.4.52</b>. For details, see <a href="https://downloads.apache.org/httpd/CHANGES_2.4">Changes with Apache 2.4.x</a> on the <i>Apache Software Foundation</i> website.<br />The Apache 2.4.52 release is a security release.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Docker</b></td><td>Updated Docker to version <b>20.10.7-5</b>.<br />Fixed support for Docker <a href="https://docs.docker.com/develop/develop-images/multistage-build/">multi-stage builds</a> in Amazon Linux 2 platform branches. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker.html#docker-platform-single">The Docker platform</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>.</td></tr>
  <tr><td><b>Go</b></td><td>Updated Go to release <b>1.17.6</b>. For details, see <a href="https://golang.org/doc/devel/release.html#go1.17">go1.17</a> in <i>The Go Programming Language Release History</i>.</td></tr>
  <tr><td><b>Corretto</b></td><td>Updated Corretto 8 to version <b>8.322.06.3</b>. For more information, see <a href="https://github.com/corretto/corretto-8/blob/develop/CHANGELOG.md">Change Log for Amazon Corretto 8</a> in the Corretto 8 repository on GitHub.</td></tr>
  <tr><td><b>Node.js</b></td><td>Updated Node.js 14 to add support for Node version <a href="https://nodejs.org/en/blog/release/v14.18.3/">14.18.3</a>.<br />Updated Node.js 12 to add support for Node version <a href="https://nodejs.org/en/blog/release/v12.22.9/">12.22.9</a>.<br />The new Node.js versions are security releases.</td></tr>
  <tr><td><b>PHP</b></td><td>Updated PHP 8.0 and 7.4 to releases <a href="https://www.php.net/releases/8_0_13.php">8.0.13</a> and <a href="https://www.php.net/releases/7_4_26.php">7.4.26</a>, respectively.<br />These updates are security releases.</td></tr>
  <tr><td><b>Ruby</b></td><td>Updated RubyGems to release <a href="https://blog.rubygems.org/2022/01/26/3.3.6-released.html">3.3.6</a>.<br />Updated Puma to version <a href="https://github.com/puma/puma/releases/tag/v5.6.1">5.6.1</a>.Notes: <ul><li> If you use the bootsnap gem, we recommend you update to <a href="https://rubygems.org/gems/bootsnap/versions/1.9.3">bootsnap 1.9.3</a> or later. Older versions of bootsnap may encounter an issue with Ruby 3.0.3. For more information, see <a href="https://github.com/Shopify/bootsnap/issues/378">Shopify bootsnap issue 378</a> on the GitHub website. </li><li> This version of Ruby enforces the version locking feature, described in <a href="https://github.com/rubygems/rubygems/pull/4076">Rubygems Pull Request 4076</a> on the GitHub website. This feature may cause some issues with applications running on this platform version. To prevent these issues we're including a workaround that will continue to use the bundler version already installed on the instance, instead of enforcing the bundler update feature. No action is required on your part.  </li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2022-02-03-linux.platforms"></a>

**Topics**
+ [Docker](#release-2022-02-03-linux.platforms.docker)
+ [Go](#release-2022-02-03-linux.platforms.go)
+ [Java SE](#release-2022-02-03-linux.platforms.javase)
+ [Tomcat](#release-2022-02-03-linux.platforms.java)
+ [.NET Core on Linux](#release-2022-02-03-linux.platforms.dotnetlinux)
+ [Node.js](#release-2022-02-03-linux.platforms.nodejs)
+ [PHP](#release-2022-02-03-linux.platforms.PHP)
+ [Python](#release-2022-02-03-linux.platforms.python)
+ [Ruby](#release-2022-02-03-linux.platforms.ruby)

### Docker
<a name="release-2022-02-03-linux.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker  |  Docker Compose  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Docker AL2 version 3.4.11** <br /> * 64bit Amazon Linux 2 v3.4.11 running Docker *  | 2.0.20220121 | 20.10.7-5 | 1.29.2 | nginx 1.20.0 | 

### Go
<a name="release-2022-02-03-linux.platforms.go"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Go 1 AL2 version 3.4.5** <br /> * 64bit Amazon Linux 2 v3.4.5 running Go 1 *  | 2.0.20220121 | Go 1.17.6 | 3.2.0 | nginx 1.20.0 | 

### Java SE
<a name="release-2022-02-03-linux.platforms.javase"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 11 version 3.2.11** <br /> * 64bit Amazon Linux 2 v3.2.11 running Corretto 11 *  | 2.0.20220121 | Corretto 11.0.13.8.2 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Corretto 8 version 3.2.11** <br /> * 64bit Amazon Linux 2 v3.2.11 running Corretto 8 *  | 2.0.20220121 | Corretto 8.322.06.3 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 

### Tomcat
<a name="release-2022-02-03-linux.platforms.java"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 11 with Tomcat 8.5 AL2 version 4.2.11** <br /> * 64bit Amazon Linux 2 v4.2.11 running Tomcat 8.5 Corretto 11 *  | 2.0.20220121 | Corretto 11.0.13.8.2 | 3.2.0 | Tomcat 8.5.72 | nginx 1.20.0 (default), Apache 2.4.52 | 
|  ** Corretto 8 with Tomcat 8.5 AL2 version 4.2.11** <br /> * 64bit Amazon Linux 2 v4.2.11 running Tomcat 8.5 Corretto 8 *  | 2.0.20220121 | Corretto 8.322.06.3 | 3.2.0 | Tomcat 8.5.72 | nginx 1.20.0 (default), Apache 2.4.52 | 

### .NET Core on Linux
<a name="release-2022-02-03-linux.platforms.dotnetlinux"></a>



|  Platform Version and *Solution Stack Name*   |  Framework  |  Proxy Server  |  AMI  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | 
|  ** .NET Core on AL2 version 2.2.10** <br /> * 64bit Amazon Linux 2 v2.2.10 running .NET Core *  | .NET 5.0.13, supports 5.0.13, 3.1.22, 2.1.30 | nginx 1.20.0 | 2.0.20220121 | 3.2.0 | 

### Node.js
<a name="release-2022-02-03-linux.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js 14 AL2 version 5.4.10** <br /> * 64bit Amazon Linux 2 v5.4.10 running Node.js 14 *  | 2.0.20220121 | 14.18.3 (6.14.15), 14.18.2 (6.14.15), 14.18.1 (6.14.15), 14.18.0 (6.14.15), 14.17.6 (6.14.15), 14.17.5 (6.14.14), 14.17.4 (6.14.14), 14.17.3 (6.14.13), 14.17.2 (6.14.13), 14.17.1 (6.14.13), 14.17.0 (6.14.13), 14.16.1 (6.14.12), 14.16.0 (6.14.11), 14.15.5 (6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8), 14.15.0 (6.14.8), 14.14.0 (6.14.8), 14.13.1 (6.14.8), 14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0 (6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7), 14.7.0 (6.14.7), 14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0 (6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br /> Default version: 14.18.3 | nginx 1.20.0 (default), Apache 2.4.52 | 2.32.0 | 3.2.0 | 
|  ** Node.js 12 AL2 version 5.4.10** <br /> * 64bit Amazon Linux 2 v5.4.10 running Node.js 12 *  | 2.0.20220121 | 12.22.9 (6.14.15), 12.22.8 (6.14.15), 12.22.7 (6.14.15), 12.22.6 (6.14.15), 12.22.5 (6.14.14), 12.22.4 (6.14.14), 12.22.3 (6.14.13), 12.22.2 (6.14.13), 12.22.1 (6.14.12), 12.22.0 (6.14.11), 12.21.0 (6.14.11), 12.20.2 (6.14.11), 12.20.1 (6.14.10), 12.20.0 (6.14.8), 12.19.1 (6.14.8), 12.19.0 (6.14.8), 12.18.4 (6.14.6), 12.18.3 (6.14.6), 12.18.2 (6.14.5), 12.18.1 (6.14.5), 12.18.0 (6.14.4), 12.17.0 (6.14.4), 12.16.3 (6.14.4), 12.16.2 (6.14.4), 12.16.1 (6.13.4), 12.16.0 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 12.13.1 (6.12.1), 12.13.0 (6.12.0), 12.12.0 (6.11.3), 12.11.1 (6.11.3), 12.11.0 (6.11.3), 12.10.0 (6.10.3), 12.9.1 (6.10.2), 12.9.0 (6.10.2), 12.8.1 (6.10.2), 12.8.0 (6.10.2), 12.7.0 (6.10.0), 12.6.0 (6.9.0), 12.5.0 (6.9.0), 12.4.0 (6.9.0), 12.3.1 (6.9.0), 12.3.0 (6.9.0), 12.2.0 (6.9.0), 12.1.0 (6.9.0), 12.0.0 (6.9.0)<br /> Default version: 12.22.9 | nginx 1.20.0 (default), Apache 2.4.52 | 2.32.0 | 3.2.0 | 

### PHP
<a name="release-2022-02-03-linux.platforms.PHP"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** PHP 8.0 AL2 version 3.3.10** <br /> * 64bit Amazon Linux 2 v3.3.10 running PHP 8.0 *  | 2.0.20220121 | PHP 8.0.13 | 2.0.13 | nginx 1.20.0 (default), Apache 2.4.52 | 
|  ** PHP 7.4 AL2 version 3.3.10** <br /> * 64bit Amazon Linux 2 v3.3.10 running PHP 7.4 *  | 2.0.20220121 | PHP 7.4.26 | 1.10.22 | nginx 1.20.0 (default), Apache 2.4.52 | 

### Python
<a name="release-2022-02-03-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.8 AL2 version 3.3.10** <br /> * 64bit Amazon Linux 2 v3.3.10 running Python 3.8 *  | 2.0.20220121 | Python 3.8.5 | pipenv 2021.11.9 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.52 | 
|  ** Python 3.7 AL2 version 3.3.10** <br /> * 64bit Amazon Linux 2 v3.3.10 running Python 3.7 *  | 2.0.20220121 | Python 3.7.10 | pipenv 2021.11.9 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.52 | 

### Ruby
<a name="release-2022-02-03-linux.platforms.ruby"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 3.0 AL2 version 3.4.2** <br /> * 64bit Amazon Linux 2 v3.4.2 running Ruby 3.0 *  | 2.0.20220121 | Ruby 3.0.3-p157 | RubyGems 3.3.6 | Puma 5.6.1 | 3.2.0 | nginx 1.20.0 | 
|  ** Ruby 2.7 AL2 version 3.4.2** <br /> * 64bit Amazon Linux 2 v3.4.2 running Ruby 2.7 *  | 2.0.20220121 | Ruby 2.7.5-p203 | RubyGems 3.3.6 | Puma 5.6.1 | 3.2.0 | nginx 1.20.0 | 
|  ** Ruby 2.6 AL2 version 3.4.2** <br /> * 64bit Amazon Linux 2 v3.4.2 running Ruby 2.6 *  | 2.0.20220121 | Ruby 2.6.9-p207 | RubyGems 3.3.6 | Puma 5.6.1 | 3.2.0 | nginx 1.20.0 | 