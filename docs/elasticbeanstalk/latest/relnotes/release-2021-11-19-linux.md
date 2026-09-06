

# Release: Elastic Beanstalk Amazon Linux platform updates on November 19, 2021
<a name="release-2021-11-19-linux"></a>

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux. The release includes security updates. It updates AMI, Go, Corretto, Tomcat, .NET Core, Node.js, Ruby, and updates Graviton image IDs. It also introduces an on-instance tool called *pkg-repo* to unlock yum package repositories.

**Release date:** November 19, 2021

## Changes
<a name="release-2021-11-19-linux.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/alas2.html">Amazon Linux Security Center</a> on or before <b>November 12, 2021</b> to all released Amazon Linux 2 platforms.<br />The <b>Go</b>, <b>Corretto</b>, and <b>Node.js</b> releases are security releases. For more information, see <b>Platform-specific updates</b> in this table.</td></tr>
  <tr><td><b>Cross-platform updates</b></td><td>Made these cross-platform updates:
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b><i>**New!**</i> <code>pkg-repo</code> on-instance CLI</b></td><td>This tool provides the capability to unlock and lock yum package repositories on EC2 instances running Amazon Linux 2. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms-scripts.html#custom-platforms-scripts.pkg-repo">pkg-repo</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>.</td></tr>
  <tr><td><b>Base AMI</b></td><td>Updated the base AMI to version <b>2.0.20211103</b>.</td></tr>
  <tr><td><b>Graviton AMIs</b></td><td>Added Graviton instance support to the Corretto and .NET Core platforms.<br />Updated Graviton images for platforms that support Graviton instances.<br />For a list of Graviton image IDs for each supported platform branch and region, see <a href="#release-2021-11-19-linux.graviton">Graviton image IDs for supporting platforms</a> on this page.<br />For more information about how to create and configure environments using Graviton instances, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.html#using-features.managing.ec2.instance-types">Amazon EC2 instance types</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Go</b></td><td>Updated Go to release <b>1.17.3</b>. For details, see <a href="https://golang.org/doc/devel/release.html#go1.17">go1.17</a> in <i>The Go Programming Language Release History</i>.<br />The Go 1.17.3 release is a security release.</td></tr>
  <tr><td><b>Corretto</b>, <b>Tomcat</b></td><td>Updated Corretto 11 to version <b>11.0.13.8.1</b>. For more information, see <a href="https://github.com/corretto/corretto-11/blob/develop/CHANGELOG.md">Change Log for Amazon Corretto 11</a> in the Corretto 11 repository on GitHub.<br />Updated Corretto 8 to version <b>8.312.07.1</b>. For more information, see <a href="https://github.com/corretto/corretto-8/blob/develop/CHANGELOG.md">Change Log for Amazon Corretto 8</a> in the Corretto 8 repository on GitHub.<br />Updated Tomcat 8.5 to <a href="https://tomcat.apache.org/tomcat-8.5-doc/changelog.html#Tomcat_8.5.72_(schultz)">Tomcat 8.5.69</a>.<br />Both Corretto updates are security releases.</td></tr>
  <tr><td><b>.NET Core</b></td><td>Updated .NET Core to releases <a href="https://github.com/dotnet/core/blob/master/release-notes/5.0/5.0.12/5.0.12.md">5.0.12</a> and <a href="https://github.com/dotnet/core/blob/master/release-notes/3.1/3.1.21/3.1.21.md">3.1.21</a>. </td></tr>
  <tr><td><b>Node.js</b></td><td>Updated Node.js 14 to add support for Node version <a href="https://nodejs.org/en/blog/release/v14.17.6/">14.17.6</a>.<br />Updated Node.js 12 to add support for Node version <a href="https://nodejs.org/en/blog/release/v12.22.7/">12.22.7</a>.<br />The Node.js 14 update is a security release.</td></tr>
  <tr><td><b>Ruby</b></td><td>Added a new platform branch, <b>Ruby 3.0</b>. For more information, see <a href="https://www.ruby-lang.org/en/news/2020/12/25/ruby-3-0-0-released/">Ruby 3.0.0 Released</a>.<br />Updated RubyGems to release <a href="https://blog.rubygems.org/2021/10/26/3.2.30-released.html">3.2.30</a>.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2021-11-19-linux.platforms"></a>

**Topics**
+ [Docker](#release-2021-11-19-linux.platforms.docker)
+ [Go](#release-2021-11-19-linux.platforms.go)
+ [Java SE](#release-2021-11-19-linux.platforms.javase)
+ [Tomcat](#release-2021-11-19-linux.platforms.java)
+ [.NET Core on Linux](#release-2021-11-19-linux.platforms.dotnetlinux)
+ [Node.js](#release-2021-11-19-linux.platforms.nodejs)
+ [PHP](#release-2021-11-19-linux.platforms.PHP)
+ [Python](#release-2021-11-19-linux.platforms.python)
+ [Ruby](#release-2021-11-19-linux.platforms.ruby)

### Docker
<a name="release-2021-11-19-linux.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker  |  Docker Compose  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Docker AL2 version 3.4.9** <br /> * 64bit Amazon Linux 2 v3.4.9 running Docker *  | 2.0.20211103 | 20.10.7-3 | 1.29.2 | nginx 1.20.0 | 

### Go
<a name="release-2021-11-19-linux.platforms.go"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** Go 1 AL2 version 3.4.3** <br /> * 64bit Amazon Linux 2 v3.4.3 running Go 1 *  | 2.0.20211103 | Go 1.17.3 | 3.2.0 | nginx 1.20.0 | 

### Java SE
<a name="release-2021-11-19-linux.platforms.javase"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 11 version 3.2.8** <br /> * 64bit Amazon Linux 2 v3.2.8 running Corretto 11 *  | 2.0.20211103 | Corretto 11.0.13.8.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Corretto 8 version 3.2.8** <br /> * 64bit Amazon Linux 2 v3.2.8 running Corretto 8 *  | 2.0.20211103 | Corretto 8.312.07.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 

### Tomcat
<a name="release-2021-11-19-linux.platforms.java"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  AWS X-Ray  |  Application Server  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 11 with Tomcat 8.5 AL2 version 4.2.8** <br /> * 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 11 *  | 2.0.20211103 | Corretto 11.0.13.8.1 | 3.2.0 | Tomcat 8.5.72 | nginx 1.20.0 (default), Apache 2.4.51 | 
|  ** Corretto 8 with Tomcat 8.5 AL2 version 4.2.8** <br /> * 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 8 *  | 2.0.20211103 | Corretto 8.312.07.1 | 3.2.0 | Tomcat 8.5.72 | nginx 1.20.0 (default), Apache 2.4.51 | 

### .NET Core on Linux
<a name="release-2021-11-19-linux.platforms.dotnetlinux"></a>



|  Platform Version and *Solution Stack Name*   |  Framework  |  Proxy Server  |  AMI  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | 
|  ** .NET Core on AL2 version 2.2.8** <br /> * 64bit Amazon Linux 2 v2.2.8 running .NET Core *  | .NET 5.0.12, supports 5.0.12, 3.1.21, 2.1.30 | nginx 1.20.0 | 2.0.20211103 | 3.2.0 | 

### Node.js
<a name="release-2021-11-19-linux.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js 14 AL2 version 5.4.8** <br /> * 64bit Amazon Linux 2 v5.4.8 running Node.js 14 *  | 2.0.20211103 | 14.18.1 (6.14.15), 14.18.0 (6.14.15), 14.17.6 (6.14.15), 14.17.5 (6.14.14), 14.17.4 (6.14.14), 14.17.3 (6.14.13), 14.17.2 (6.14.13), 14.17.1 (6.14.13), 14.17.0 (6.14.13), 14.16.1 (6.14.12), 14.16.0 (6.14.11), 14.15.5 (6.14.11), 14.15.4 (6.14.10), 14.15.3 (6.14.9), 14.15.2 (6.14.9), 14.15.1 (6.14.8), 14.15.0 (6.14.8), 14.14.0 (6.14.8), 14.13.1 (6.14.8), 14.13.0 (6.14.8), 14.12.0 (6.14.8), 14.11.0 (6.14.8), 14.10.1 (6.14.8), 14.10.0 (6.14.8), 14.9.0 (6.14.8), 14.8.0 (6.14.7), 14.7.0 (6.14.7), 14.6.0 (6.14.6), 14.5.0 (6.14.5), 14.4.0 (6.14.5), 14.3.0 (6.14.5), 14.2.0 (6.14.4), 14.1.0 (6.14.4), 14.0.0 (6.14.4)<br /> Default version: 14.18.1 | nginx 1.20.0 (default), Apache 2.4.51 | 2.32.0 | 3.2.0 | 
|  ** Node.js 12 AL2 version 5.4.8** <br /> * 64bit Amazon Linux 2 v5.4.8 running Node.js 12 *  | 2.0.20211103 | 12.22.7 (6.14.15), 12.22.6 (6.14.15), 12.22.5 (6.14.14), 12.22.4 (6.14.14), 12.22.3 (6.14.13), 12.22.2 (6.14.13), 12.22.1 (6.14.12), 12.22.0 (6.14.11), 12.21.0 (6.14.11), 12.20.2 (6.14.11), 12.20.1 (6.14.10), 12.20.0 (6.14.8), 12.19.1 (6.14.8), 12.19.0 (6.14.8), 12.18.4 (6.14.6), 12.18.3 (6.14.6), 12.18.2 (6.14.5), 12.18.1 (6.14.5), 12.18.0 (6.14.4), 12.17.0 (6.14.4), 12.16.3 (6.14.4), 12.16.2 (6.14.4), 12.16.1 (6.13.4), 12.16.0 (6.13.4), 12.15.0 (6.13.4), 12.14.1 (6.13.4), 12.14.0 (6.13.4), 12.13.1 (6.12.1), 12.13.0 (6.12.0), 12.12.0 (6.11.3), 12.11.1 (6.11.3), 12.11.0 (6.11.3), 12.10.0 (6.10.3), 12.9.1 (6.10.2), 12.9.0 (6.10.2), 12.8.1 (6.10.2), 12.8.0 (6.10.2), 12.7.0 (6.10.0), 12.6.0 (6.9.0), 12.5.0 (6.9.0), 12.4.0 (6.9.0), 12.3.1 (6.9.0), 12.3.0 (6.9.0), 12.2.0 (6.9.0), 12.1.0 (6.9.0), 12.0.0 (6.9.0)<br /> Default version: 12.22.7 | nginx 1.20.0 (default), Apache 2.4.51 | 2.32.0 | 3.2.0 | 

### PHP
<a name="release-2021-11-19-linux.platforms.PHP"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Composer  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  ** PHP 8.0 AL2 version 3.3.8** <br /> * 64bit Amazon Linux 2 v3.3.8 running PHP 8.0 *  | 2.0.20211103 | PHP 8.0.8 | 2.0.13 | nginx 1.20.0 (default), Apache 2.4.51 | 
|  ** PHP 7.4 AL2 version 3.3.8** <br /> * 64bit Amazon Linux 2 v3.3.8 running PHP 7.4 *  | 2.0.20211103 | PHP 7.4.21 | 1.10.22 | nginx 1.20.0 (default), Apache 2.4.51 | 

### Python
<a name="release-2021-11-19-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.8 AL2 version 3.3.8** <br /> * 64bit Amazon Linux 2 v3.3.8 running Python 3.8 *  | 2.0.20211103 | Python 3.8.5 | pipenv 2020.8.13 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.51 | 
|  ** Python 3.7 AL2 version 3.3.8** <br /> * 64bit Amazon Linux 2 v3.3.8 running Python 3.7 *  | 2.0.20211103 | Python 3.7.10 | pipenv 2020.8.13 |  |  | 3.2.0 | nginx 1.20.0 (default), Apache 2.4.51 | 

### Ruby
<a name="release-2021-11-19-linux.platforms.ruby"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Application Server  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Ruby 3.0 AL2 version 3.4.0** <br /> * 64bit Amazon Linux 2 v3.4.0 running Ruby 3.0 *  | 2.0.20211103 | Ruby 3.0.2-p107 | RubyGems 3.2.30 | Puma 5.5.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Ruby 2.7 AL2 version 3.4.0** <br /> * 64bit Amazon Linux 2 v3.4.0 running Ruby 2.7 *  | 2.0.20211103 | Ruby 2.7.4-p191 | RubyGems 3.2.30 | Puma 5.5.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Ruby 2.6 AL2 version 3.4.0** <br /> * 64bit Amazon Linux 2 v3.4.0 running Ruby 2.6 *  | 2.0.20211103 | Ruby 2.6.8-p205 | RubyGems 3.2.30 | Puma 5.5.2 | 3.2.0 | nginx 1.20.0 | 

## Graviton image IDs for supporting platforms
<a name="release-2021-11-19-linux.graviton"></a>

**Elastic Beanstalk provides enhanced console support for Graviton as of November 24, 2021**  
Customers are no longer required to manually enter the listed custom AMIs to create a new Elastic Beanstalk environment with arm64 processor architecture.  
If you created environments with the custom AMIs provided in the first wave release, we recommend that you remove the custom AMIs and upgrade to the latest platform version. For specific instructions, see [Recommendations for Graviton arm64 first wave environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.html#using-features.managing.ec2.graviton-wave-1) in the *AWS Elastic Beanstalk Developer Guide*.

The following sections list the Graviton image IDs for each platform branch that supports Graviton instance types. The images are specific to each supporting AWS Region. For more information about Graviton instances, see [Amazon EC2 instance types](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.html#using-features.managing.ec2.instance-types) in the *AWS Elastic Beanstalk Developer Guide*.

### US East (Ohio) – us-east-2
<a name="release-2021-11-19-linux.graviton-CMH"></a>



|  Platform version  |  Graviton image ID  |  x86 image ID  | 
| --- | --- | --- | 
| 64bit Amazon Linux 2 v3.4.9 running Docker | ami-0441e8ce73df09a41 | ami-075b47874be930f25 | 
| 64bit Amazon Linux 2 v3.4.3 running Go 1 | ami-0c927e122bfeb846b | ami-02940a953f290f6e7 | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 11 | ami-0dfcb2794a2e57653 | ami-02f63cc19478b7a3f | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 8 | ami-0db86d0ea18af1303 | ami-0202b9614a19a1fec | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 11 | ami-0995f5d405a5078e9 | ami-027b50191944765d6 | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 8 | ami-02f7ee83ff873a8c4 | ami-09629aecb6b47c334 | 
| 64bit Amazon Linux 2 v2.2.8 running .NET Core | ami-097df5d4310310bec | ami-0365a58a29bf22001 | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 14 |  ami-06400ed43c645c34f | ami-04aa1daf519b5cd45 | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 12 | ami-090baf298cc814ca9 | ami-01a2a29f949cdaf72 | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 8.0 | ami-00cf32aa5968ac2fd | ami-02e0ca27ec850e02f | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 7.4 | ami-0b752a53bcc84ccde | ami-0e86f0bb24bcb1a8f | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.8 | ami-011e9784068cd6bd1 | ami-055982caf649e8b45 | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.7 | ami-02f644cbb7ce055c9 | ami-03dc2a7eaa4d60375 | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 3.0 | ami-07d6f7cb58498cf35 | ami-0d544f38a010032fc | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 2.7 | ami-021dbbba99c9abb3a | ami-0a73484227b76b5e4 | 

### US East (N. Virginia) – us-east-1
<a name="release-2021-11-19-linux.graviton-IAD"></a>



|  Platform version  |  Graviton image ID  |  x86 image ID  | 
| --- | --- | --- | 
| 64bit Amazon Linux 2 v3.4.9 running Docker | ami-0f01cafded2c0b853 |  ami-015baecf2e21c75c0 | 
| 64bit Amazon Linux 2 v3.4.3 running Go 1 | ami-00fbb5b18f69c62a5 | ami-03c336d85392cd61b | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 11 | ami-0104e52b36106e5fd | ami-04116eb6f40396f6a | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 8 | ami-0d50f7f310f21b103 | ami-09bd420f2ee8e3dde | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 11 | ami-099e73de8c620b269 | ami-0dd8003d03ad12103 | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 8 | ami-07496b2445e51c867 | ami-097a177d91fa8eaa8 | 
| 64bit Amazon Linux 2 v2.2.8 running .NET Core | ami-03e802e46e1175c05 | ami-0b91f9cb2b2283657 | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 12 | ami-05e45257c449568ab | ami-066968fa7496e7be0 | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 14 | ami-0b9cbe454c6b13d9e | ami-016b7e315722f3a1c | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.7 | ami-0f87e56baf2566f2f | ami-0339707bccb34bac7 | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.8 | ami-0e0a22f5bf3c10bc2 | ami-0e1edcfd7be020fc7 | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 8.0 | ami-042c6aca1d2045eb6 | ami-0d9954c8ba42a30ef | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 7.4 | ami-0f9203b5249754444 | ami-02a46289b82b8aca2 | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 3.0 | ami-06e22dd5599cd8ffc | ami-042d4310d92154e82 | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 2.7 | ami-0b5783de2e7233b30 | ami-075faf3a24979654b | 

### US West (Oregon) – us-west-2
<a name="release-2021-11-19-linux.graviton-PDX"></a>



|  Platform version  |  Graviton image ID  |  x86 image ID  | 
| --- | --- | --- | 
| 64bit Amazon Linux 2 v3.4.9 running Docker | ami-0e66bce56aeae6763 | ami-023d642dc37e347b4 | 
| 64bit Amazon Linux 2 v3.4.3 running Go 1 | ami-0225d371be5051096 | ami-080b3ea7e462f7806 | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 11 | ami-0037ef3fc3bbe5eb4 | ami-0cd6b23319ad159be | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 8 | ami-03c1429b874a48300 | ami-03fd672bfb672b061 | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 11 | ami-0520ed73cbe072b69 | ami-069d178e894e64a91 | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 8 | ami-047e1202e78abe2c0 | ami-0793f1ea75ac920b1 | 
| 64bit Amazon Linux 2 v2.2.8 running .NET Core | ami-0b165ee3b84bbd0da | ami-00e818485cfc7c8a2 | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 14 | ami-08ef086cb7558d193 | ami-0a88881007784330f | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 12 | ami-010cc0781fbf6cce0 | ami-0af5432b642787153 | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 8.0 | ami-0c998a81bb7419ffe | ami-0494b4c9e9c9e919b | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 7.4 | ami-0d52b22e32d766a8f | ami-04319ba70a257149a | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.8 | ami-02bcf41fecdb6a55e | ami-0fe8cfe9a1f5d32ae | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.7 | ami-034fbd670766367cf | ami-023ebe82b137da832 | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 3.0 | ami-0dd77d44be7693374 | ami-0b3d59b4153276b98 | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 2.7 | ami-0089d1773b90cb777 | ami-0786dedccb30400bd | 

### Europe (Ireland) – eu-west-1
<a name="release-2021-11-19-linux.graviton-DUB"></a>



|  Platform version  |  Graviton image ID  |  x86 image ID  | 
| --- | --- | --- | 
| 64bit Amazon Linux 2 v3.4.9 running Docker | ami-088610b6efb279441 | ami-012191135c13ce958 | 
| 64bit Amazon Linux 2 v3.4.3 running Go 1 | ami-0a5617eefa6a74133 | ami-0af426d1233cb20e7 | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 11 | ami-0844bf59d8617dc3f | ami-02edfb4b280fab7ac | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 8 | ami-0abfd770beaa1f554 | ami-070d1e02477bb0dfc | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 11 | ami-0729d7f3ddf1ef5a6 | ami-0af33e05c29c5ac02 | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 8 | ami-0c68cace423c474d6 | ami-079edbe9c4942b952 | 
| 64bit Amazon Linux 2 v2.2.8 running .NET Core | ami-00f2c7dd3bf54b6b5 | ami-0cb9a803c5778f4da | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 14 | ami-04ff37c08f3f3a570 | ami-097d868b8d54109ce | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 12 | ami-045d81829c6f2ba95 | ami-0a268446bafac0aeb | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 8.0 | ami-07757af693b44026d | ami-06594a7d8d8d31fe2 | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 7.4 | ami-05f4f641f3151fde1 | ami-0820ac51bd6a52358 | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.8 | ami-0ce77ac57445317a4 | ami-060329240a6a9862b | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.7 | ami-0f7443ebec63dc5c2 | ami-02a5ee9da975b582f | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 3.0 | ami-0dc924de9fcb28b52 | ami-0d3c2a66834833f3d | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 2.7 | ami-0a6cc43cd3b39aba7 | ami-071f87be132533b8a | 

### Europe (Frankfurt) – eu-central-1
<a name="release-2021-11-19-linux.graviton-FRA"></a>



|  Platform version  |  Graviton image ID  |  x86 image ID  | 
| --- | --- | --- | 
| 64bit Amazon Linux 2 v3.4.9 running Docker | ami-0b7b2641b2a71b2f8 | ami-00360b1288f309a4d | 
| 64bit Amazon Linux 2 v3.4.3 running Go 1 | ami-029bda5fae7720e2d | ami-03ffb01c765d2436b | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 11 | ami-00343d91b55f5e070 | ami-0d5452c027605eded | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 8 | ami-0a3f7e7f3ca620c24 | ami-00004eddce87cd093 | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 11 | ami-0282eabcd9f90481f | ami-0ac7755983eb8a01c | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 8 | ami-0b3942ddc11bd610d | ami-07065aad8e3d8a512 | 
| 64bit Amazon Linux 2 v2.2.8 running .NET Core | ami-035948e9a27f5920c | ami-02a9fb0eafacd2a08 | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 14 | ami-048302fb03e745f52 | ami-0e92cafb69968e863 | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 12 | ami-0aaf86f7b68a2edca | ami-064b7f35e3915684e | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 8.0 | ami-0051db71488b0ec91 | ami-0bd38497f5f34173b | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 7.4 | ami-0728beaccef36ea32 | ami-038a300b2cfb0d5a1 | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.8 | ami-094b6bccbe5680e95 | ami-017d3a75426c575c9 | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.7 | ami-0bb907b45c583f04f | ami-0298b03e603f63d09 | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 3.0 | ami-0e1c40e826ba73e0c | ami-098de7c80d55b0f45 | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 2.7 | ami-063ab945bc90bbdc4 | ami-0b69084c8e45390a5 | 

### South America (São Paulo) – sa-east-1
<a name="release-2021-11-19-linux.graviton-GRU"></a>



|  Platform version  |  Graviton image ID  |  x86 image ID  | 
| --- | --- | --- | 
| 64bit Amazon Linux 2 v3.4.9 running Docker | ami-0821698f1a7194c47 | ami-02b46e1073dfa2b90 | 
| 64bit Amazon Linux 2 v3.4.3 running Go 1 | ami-03966d055dffb613e | ami-0b5a9a6e7b5980c9b | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 11 | ami-0ed77c0832c19d72d | ami-0097d7808c976326f | 
| 64bit Amazon Linux 2 v3.2.8 running Corretto 8 | ami-00ed07f8fbb4d83f2 | ami-01991af1dc8972812 | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 11 | ami-07b32ce45701ce14a | ami-03f2c99dd0139becd | 
| 64bit Amazon Linux 2 v4.2.8 running Tomcat 8.5 Corretto 8 | ami-0647b5368b2ee4649 | ami-0bd3b69839de7a068 | 
| 64bit Amazon Linux 2 v2.2.8 running .NET Core | ami-09e0f494b31c53191 | ami-07eb29c9c617fda61 | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 14 | ami-049b1f83225330905 | ami-01e673efffa5eac2c | 
| 64bit Amazon Linux 2 v5.4.8 running Node.js 12 | ami-0b906a156cac2dcab | ami-0df6eb3f035925367 | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 8.0 | ami-05cf011539988c46e | ami-0a160423b11873be8 | 
| 64bit Amazon Linux 2 v3.3.8 running PHP 7.4 | ami-0a94676ff8c458770 | ami-0196b5eef914b6c69 | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.8 | ami-09330456584469924 | ami-06d49fcff919c1c65 | 
| 64bit Amazon Linux 2 v3.3.8 running Python 3.7 | ami-06e0953a29e1bbbb9 | ami-0a7b77eaef16adc4b | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 3.0 | ami-0456af2f62e5aa685 | ami-0bea9b9d4ae0560d9 | 
| 64bit Amazon Linux 2 v3.4.0 running Ruby 2.7 | ami-06b4eb87313c5a30e | ami-0630c0a0cafcd6707 | 