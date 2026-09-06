

# Release: Elastic Beanstalk Amazon Linux 2023 platform updates on July 05, 2023
<a name="release-2023-07-05-al2023-python"></a>

This release provides new versions for AWS Elastic Beanstalk platforms based on Amazon Linux 2023. The release includes security updates. It also includes AMI, nginx, and Python updates.

**Release date:** July 05, 2023

## Changes
<a name="release-2023-07-05-al2023-python.changes"></a>

At this time Elastic Beanstalk only supports the Python platform on Amazon Linux 2023. We're working on releasing support for AL2023 to more platforms.

For more information, see [Elastic Beanstalk Linux platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux.html) in the *AWS Elastic Beanstalk Developer Guide*.

For more information about Amazon Linux 2023, see [Comparing Amazon Linux 2 and Amazon Linux 2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html) in the *Amazon Linux 2023 User Guide*. 

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/alas2023.html">Amazon Linux Security Center</a> on or before <b>June 27, 2023</b> to all AL2023 platforms.<br /> </td></tr>
  <tr><td><b>Cross-platform updates</b></td><td>Made these cross-platform updates:
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2023.1.20230629.</td></tr>
  <tr><td><b>nginx</b></td><td>Updated AL2023 platforms supporting the nginx server to <a href="https://https://nginx.org/en/CHANGES-1.24">version 1.24.0</a> from version 1.22.1<br />The updates in this release include security fixes.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Python</b></td><td>Updated Pipenv to release 2023.6.26 for both the Python 3.9 and Python 3.11 platform branches. For details, see the Pipenv <a href="https://pipenv.pypa.io/en/latest/changelog/">Release and Version History</a>.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2023-07-05-al2023-python.platforms"></a>

**Note**  
The following tables list all supported platform branches for each platform. Only Amazon Linux 2023 platform branches are updated.

**Topics**
+ [Python](#release-2023-07-05-al2023-python.platforms.python)

### Python
<a name="release-2023-07-05-al2023-python.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.11 AL2023 version 4.0.2** <br /> * 64bit Amazon Linux 2023 v4.0.2 running Python 3.11 *  | 2023.1.20230629 | Python 3.11.2 | pipenv 2023.6.26 |  |  | 3.2.0 | nginx 1.24.0 (default), Apache 2.4.56 | 
|  ** Python 3.9 AL2023 version 4.0.2** <br /> * 64bit Amazon Linux 2023 v4.0.2 running Python 3.9 *  | 2023.1.20230629 | Python 3.9.16 | pipenv 2023.6.26 |  |  | 3.2.0 | nginx 1.24.0 (default), Apache 2.4.56 | 