

# Release: Elastic Beanstalk Amazon Linux 2 Corretto platform updates on July 28, 2022
<a name="release-2022-07-28-linux-corretto-17"></a>

This release provides new versions for the AWS Elastic Beanstalk Corretto platforms based on Amazon Linux 2. It includes Amazon Linux 2 security updates. This release also introduces a new platform branch, **Corretto 17**, based on Amazon Linux 2.

**Release date:** July 28, 2022

## Changes
<a name="release-2022-07-28-linux-corretto-17.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/alas2.html">Amazon Linux Security Center</a> on or before <b>July 14, 2022</b> to all released Amazon Linux 2 Corretto platforms.</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Corretto</b></td><td><b>**New!**</b> — Introduced new <b>Corretto 17</b> platform branch, running Corretto version <b>17.0.3.6.1</b>.<br />For more information, see <a href="https://github.com/corretto/corretto-17/blob/develop/CHANGELOG.md#corretto-version-170361">Change Log for Amazon Corretto 17</a> in the Corretto 17 repository on GitHub. Also, see the <a href="https://aws.amazon.com/corretto">Amazon Corretto</a> website. Refer to the following <b>Note</b> in the next section if you use the AWS CLI or EB CLI to create environments based on the <b>Corretto 11</b> or <b>Corretto 8</b> platform versions in this release. </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2022-07-28-linux-corretto-17.platforms"></a>

**Topics**
+ [Java SE](#release-2022-07-28-linux-corretto-17.platforms.javase)

### Java SE
<a name="release-2022-07-28-linux-corretto-17.platforms.javase"></a>

**Note - Customers that use the AWS CLI or EB CLI to create environments should be aware of the following:**  
In this release, for Corretto 8 and Corretto 11, there is a mismatch between the platform version of the branch and the version listed in the *Solution Stack Name*.  
Corretto 8 **v3.2.17** has Solution Stack Name *64bit Amazon Linux 2 **v3.3.0** running Corretto 8*.
Corretto 11 **v3.2.17** has Solution Stack Name *64bit Amazon Linux 2 **v3.3.0** running Corretto 11*. 
If you use the AWS CLI or EB CLI to create environments for these two platform branches in this release, be sure to use these solution stack names in parameters that require them.  
This mismatch occurs in *this release only*. The platform releases that follow will have the standard matching version names in their corresponding Solution Stack Name. The Elastic Beanstalk console does not display the Solution Stack Name, and is therefore not affected.



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Tools  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Corretto 17 version 3.3.0** <br /> * 64bit Amazon Linux 2 v3.3.0 running Corretto 17 *  | 2.0.20220606 | Corretto 17.0.3.6.1 | Ant 1.10.7, Gradle 7.4.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Corretto 11 version 3.2.17** <br /> * 64bit Amazon Linux 2 v3.3.0 running Corretto 11 *  | 2.0.20220606 | Corretto 11.0.15.9.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 
|  ** Corretto 8 version 3.2.17** <br /> * 64bit Amazon Linux 2 v3.3.0 running Corretto 8 *  | 2.0.20220606 | Corretto 8.332.08.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | 