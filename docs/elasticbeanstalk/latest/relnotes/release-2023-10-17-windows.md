

# Release: Elastic Beanstalk Windows Server platform update on October 17, 2023
<a name="release-2023-10-17-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** October 17, 2023

## Changes
<a name="release-2023-10-17-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied October 2023 security updates for Windows.<br />See the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>End of updates for retiring platform branches Windows Server 2012 R2/R2 Core</b></td><td>On October 10, 2023 the operating systems <i>Windows Server 2012 R2</i> and <i>Windows Server 2012 R2 Core</i> reached <i>end of support</i> by Microsoft. After this date, Microsoft no longer provides security updates, non-security updates, bug fixes, or technical support for these products. For more information see the Microsoft website <a href="https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2012-r2">Windows Server 2012 R2 – Microsoft Lifecycle.</a><br />Due to the Microsoft <i>end of support</i> status, there will not be any changes to release for these platform branches going forward.<ul><li> Windows Server 2012 R2 running IIS 8.5 </li><li> Windows Server Core 2012 R2 running IIS 8.5 </li></ul><br />We strongly recommend that you start planning your migration to one of the Elastic Beanstalk Windows Server version 2 platforms, which are current and fully supported. For a list of these platforms see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html">Supported platforms</a> in AWS Elastic Beanstalk Platforms. For full migration considerations see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-v2migration.html">Major Version Migration </a> in the <i>AWS Elastic Beanstalk Developer Guide</i>.Addendum These release notes previously shared our plans to retire these platform branches on June 30, 2024. In accordance with our platform support policies, we are unable to provide End of Life software to our customers. <b><i>Windows Server 2012 R2</i> and <i>Windows Server 2012 R2 Core</i> platform branches will now retire on December 4, 2023.</b> On December 4, these platform branches will be removed from Elastic Beanstalk console. Customers can continue to operate existing environments on these platform branches until March 4, 2024, which is 90 days after the December 4 retirement date. <br />Elastic Beanstalk will make Beanstalk Windows 2012 AMIs private after March 4, 2024. This will prevent customers from being able to launch instances in their Beanstalk environments if they are using the default Beanstalk AMI. In order to retain access to the AMIs, customers may copy the AMIs into their accounts to be used in their Beanstalk environments. For detailed instructions, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.customenv-env-copy.html">Preserving access to an AMI for a retired platform</a> in the <i>AWS Elastic Beanstalk Developer Guide</i> </td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 6 to version 6.0.23 on Windows Server 2019 and 2016 platform versions.<br />Windows .NET Core 3.1 is being removed from the listed platform versions, because it's past Microsoft’s end of support dates. For more information, see <a href="https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core">.NET and .NET Core Support Policy</a> on the Microsoft website.<ul><li> Windows Server 2016 and 2019 platforms — .NET Core 3.1 removed </li></ul></td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2023.10.11.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.300028.4b233.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version 3.2.1630.0.</td></tr>
  <tr><td><b>AWSPoswershell</b></td><td>Updated AWSPoswershell to version 4.1.426.</td></tr>
  <tr><td><b>cfn-init</b></td><td>Updated cfn-init to version 2.0.28.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2023-10-17-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2023-10-17-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.12.0**  |  * 64bit Windows Server 2019 v2.12.0 running IIS 10.0 *  | .NET 6.0.23, supports 6.0.23<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.12.0**  |  * 64bit Windows Server Core 2019 v2.12.0 running IIS 10.0 *  | .NET 6.0.23, supports 6.0.23<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.12.0**  |  * 64bit Windows Server 2016 v2.12.0 running IIS 10.0 *  | .NET 6.0.23, supports 6.0.23<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.12.0**  |  * 64bit Windows Server Core 2016 v2.12.0 running IIS 10.0 *  | .NET 6.0.23, supports 6.0.23<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.12.0**  | 2023.10.11 | 3.7.661.0 |  | 3.2.1630.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.12.0**  | 2023.10.11 | 3.7.661.0 |  | 3.2.1630.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.12.0**  | 2023.10.11 | 3.7.661.0 |  | 3.2.1630.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.12.0**  | 2023.10.11 | 3.7.661.0 |  | 3.2.1630.0 | 3.6 | 3.2.0 | 