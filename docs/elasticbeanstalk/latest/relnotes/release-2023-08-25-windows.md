

# Release: Elastic Beanstalk Windows Server platform update on August 25, 2023
<a name="release-2023-08-25-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components and includes a platform deprecation announcement.

**Release date:** August 25, 2023

## Changes
<a name="release-2023-08-25-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Windows security updates</b></td><td>Applied August 2023 security updates for Windows.<br />See the Microsoft <a href="https://portal.msrc.microsoft.com/en-us/security-guidance">Security Update Guide</a>.</td></tr>
  <tr><td><b>Platform deprecation</b></td><td>Today we're announcing the future retirement for the following platform branches. <ul><li> Windows Server 2012 R2 running IIS 8.5 </li><li> Windows Server Core 2012 R2 running IIS 8.5 </li></ul><br />These platform branches are now <i>deprecated</i>.<br />If you currently use these retiring platform branches, we strongly recommend that you start planning your migration to one of the <i>Windows Server version 2</i> platforms, which are current and fully supported:<ul><li> Windows Server 2019 with IIS 10.0 version 2.x </li><li> Windows Server 2016 with IIS 10.0 version 2.x </li></ul><br />For full migration considerations, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-v2migration.html">Major Version Migration</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>. <br />Deprecated platform branches aren't listed on the <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html">Supported platforms</a> page of the <i>AWS Elastic Beanstalk Platforms</i> guide. They are listed on a separate page, <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html">Retiring platform versions</a>.<br />For more information about platform deprecation, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html">Elastic Beanstalk platform support policy</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>.Addendum These release notes previously shared our plans to retire these platform branches on June 30, 2024. In accordance with our platform support policies, we are unable to provide End of Life software to our customers. <b><i>Windows Server 2012 R2</i> and <i>Windows Server 2012 R2 Core</i> platform branches will now retire on December 4, 2023.</b> On December 4, these platform branches will be removed from Elastic Beanstalk console. Customers can continue to operate existing environments on these platform branches until March 4, 2024, which is 90 days after the December 4 retirement date. <br />Elastic Beanstalk will make Beanstalk Windows 2012 AMIs private after March 4, 2024. This will prevent customers from being able to launch instances in their Beanstalk environments if they are using the default Beanstalk AMI. In order to retain access to the AMIs, customers may copy the AMIs into their accounts to be used in their Beanstalk environments. For detailed instructions, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.customenv-env-copy.html">Preserving access to an AMI for a retired platform</a> in the <i>AWS Elastic Beanstalk Developer Guide</i> </td></tr>
  <tr><td><b>Framework updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Framework</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b></td><td>Updated .NET 6 to version 6.0.21 on Windows Server 2019 and 2016 platform versions.</td></tr>
</tbody>
</table>
 </td></tr>
  <tr><td><b>AWS component updates</b></td><td> 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Details</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2023.08.10.</td></tr>
  <tr><td><b>CloudWatch Agent</b></td><td>Updated the CloudWatch Agent to version 1.300026.1b168.</td></tr>
  <tr><td><b>EC2Launch</b></td><td>Updated EC2Launch V2 to version 2.0.1521.0.</td></tr>
  <tr><td><b>SSM Agent</b></td><td>Updated the SSM Agent to version 3.1.2282.0.</td></tr>
</tbody>
</table>
 </td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2023-08-25-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2023-08-25-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>



|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.11.7**  |  * 64bit Windows Server 2019 v2.11.7 running IIS 10.0 *  | .NET 6.0.21, supports 6.0.21, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.11.7**  |  * 64bit Windows Server Core 2019 v2.11.7 running IIS 10.0 *  | .NET 6.0.21, supports 6.0.21, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.11.7**  |  * 64bit Windows Server 2016 v2.11.7 running IIS 10.0 *  | .NET 6.0.21, supports 6.0.21, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.11.7**  |  * 64bit Windows Server Core 2016 v2.11.7 running IIS 10.0 *  | .NET 6.0.21, supports 6.0.21, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 | 

#### More details
<a name="platforms-supported.net.details"></a>



|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  ** Windows Server 2019 with IIS 10.0 version 2.11.7**  | 2023.08.10 | 3.7.617.0 |  | 3.1.2282.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2019 with IIS 10.0 version 2.11.7**  | 2023.08.10 | 3.7.617.0 |  | 3.1.2282.0 | 3.6 | 3.2.0 | 
|  ** Windows Server 2016 with IIS 10.0 version 2.11.7**  | 2023.08.10 | 3.7.617.0 |  | 3.1.2282.0 | 3.6 | 3.2.0 | 
|  ** Windows Server Core 2016 with IIS 10.0 version 2.11.7**  | 2023.08.10 | 3.7.617.0 |  | 3.1.2282.0 | 3.6 | 3.2.0 | 