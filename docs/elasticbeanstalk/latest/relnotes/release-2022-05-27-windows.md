

# Release: Elastic Beanstalk Windows Server platform update on May 27, 2022
<a name="release-2022-05-27-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. It also introduces support for .NET 6 on the Windows Server platforms. The release applies Windows security updates and also updates framework and AWS components.

**Release date:** May 27, 2022

## Changes
<a name="release-2022-05-27-windows.changes"></a>

In this latest release, we're adding AWS Elastic Beanstalk support for .NET 6 on the Windows Server platforms.

With this release, you can use Elastic Beanstalk to deploy your .NET 6 applications to your AWS Windows environments. .NET 6 is supported on Windows Server 2016 and later. Also, .NET 6 has improved performance for ARM64. For more information about how AWS can help you leverage .NET 6, see [.NET 6 on AWS](https://aws.amazon.com/blogs/developer/net-6-on-aws/) on the AWS Developer Blog.

For more information about .NET 6 features, see the Microsoft website [What's new in .NET 6](https://docs.microsoft.com/en-us/dotnet/core/whats-new/dotnet-6).

In addition to introducing .NET 6 on the Windows Server platforms, some additional changes are included for the Windows platform in this release. They are listed in the following table.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied May 2022 security updates for Windows.<br />See the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Introduced .NET 6.0.5 on Windows Server 2019 and 2016 platform versions.<br />Updated .NET Core 3 to version 3.1.25 on Windows Server 2019 and 2016 platform versions.<br />Updated .NET 5 to version 5.0.17 on Windows Server 2019 and 2016 platform versions.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2022.05.11</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.247350.0b251814</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2022-05-27-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2022-05-27-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.10.0**  |  * 64bit Windows Server 2019 v2.10.0 running IIS 10.0 *  | .NET 6.0.5, supports 6.0.5, 5.0.17, 3.1.25<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.10.0**  |  * 64bit Windows Server Core 2019 v2.10.0 running IIS 10.0 *  | .NET 6.0.5, supports 6.0.5, 5.0.17, 3.1.25<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.10.0**  |  * 64bit Windows Server 2016 v2.10.0 running IIS 10.0 *  | .NET 6.0.5, supports 6.0.5, 5.0.17, 3.1.25<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.10.0**  |  * 64bit Windows Server Core 2016 v2.10.0 running IIS 10.0 *  | .NET 6.0.5, supports 6.0.5, 5.0.17, 3.1.25<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.10.0**  |  * 64bit Windows Server 2012 R2 v2.10.0 running IIS 8.5 *  | .NET Core 2.1.30, supports 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.0**  |  * 64bit Windows Server Core 2012 R2 v2.10.0 running IIS 8.5 *  | .NET Core 2.1.30, supports 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.10.0**  | 2022.05.11 | 3.15.1620 |  | 3.1.1045.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.10.0**  | 2022.05.11 | 3.15.1620 |  | 3.1.1045.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.10.0**  | 2022.05.11 | 3.15.1620 |  | 3.1.1045.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.10.0**  | 2022.05.11 | 3.15.1620 |  | 3.1.1045.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.10.0**  | 2022.05.11 | 3.15.1620 |  | 3.1.1045.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.0**  | 2022.05.11 | 3.15.1620 | 4.9.4556 | 3.1.1045.0 | 3.6 | 3.2.0 | 