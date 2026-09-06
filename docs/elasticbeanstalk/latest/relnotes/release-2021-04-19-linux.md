

# Release: Elastic Beanstalk Amazon Linux AMI platform update for Python on April 19, 2021
<a name="release-2021-04-19-linux"></a>

This release provides a new version for the AWS Elastic Beanstalk Python platform based on Amazon Linux AMI. The release includes security updates. It also includes a component update on the Python platform.

**Release date:** April 19, 2021

## Changes
<a name="release-2021-04-19-linux.changes"></a>

Today we're releasing an update for the Python platform based on Amazon Linux AMI, to fix an emergent issue. We will follow with an update for the rest of the Amazon Linux AMI platforms at a later date.

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/">Amazon Linux Security Center</a> on or before <b>April 7, 2021</b> to the released platform.</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Python</b></td><td>Updated setuptools to <a href="https://pypi.org/project/setuptools/56.0.0/">setuptools 56.0.0</a>. The previous version included in the platform didn't support SNI, and this started to impact customers due to the <a href="https://github.com/pypa/pypi-support/issues/978">deprecation of non-SNI compatible clients</a>.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2021-04-19-linux.platforms"></a>

**Note**  
The following tables list all supported platform branches for each platform. Only Amazon Linux AMI platform branches are updated.

**Topics**
+ [Python](#release-2021-04-19-linux.platforms.python)

### Python
<a name="release-2021-04-19-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.8 AL2 version 3.2.1** <br /> * 64bit Amazon Linux 2 v3.2.1 running Python 3.8 *  | 2.0.20210326 | Python 3.8.5 | pipenv 2020.8.13 |  |  | 3.2.0 | nginx 1.18.0 (default), Apache 2.4.46 | 
|  ** Python 3.7 AL2 version 3.2.1** <br /> * 64bit Amazon Linux 2 v3.2.1 running Python 3.7 *  | 2.0.20210326 | Python 3.7.9 | pipenv 2020.8.13 |  |  | 3.2.0 | nginx 1.18.0 (default), Apache 2.4.46 | 
|  ** Python 3.6 version 2.10.0** <br /> * 64bit Amazon Linux 2018.03 v2.10.0 running Python 3.6 *  | 2018.03.0 | Python 3.6.12 | pip 9.0.3 | setuptools 56.0.0 | meld3 1.0.2 | 3.1.0 | Apache 2.4.46 with mod\_wsgi 3.5 | 