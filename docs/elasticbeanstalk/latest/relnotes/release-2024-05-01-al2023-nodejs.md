

# Release: Elastic Beanstalk Amazon Linux 2023 Node.js platform updates on May 01, 2024
<a name="release-2024-05-01-al2023-nodejs"></a>

This release is an emergent AWS Elastic Beanstalk Node.js platform update for Amazon Linux 2023. It addresses a security vulnerability and also updates Apache HTTP server on the Node.js AL2023 platforms.

**Release date:** May 01, 2024

## Changes
<a name="release-2024-05-01-al2023-nodejs.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/alas2023.html">Amazon Linux Security Center</a> on or before <b>April 25, 2024</b> to all AL2023 platforms.<br />Applied security updates that address <a href="https://explore.alas.aws.amazon.com/CVE-2024-27983.html">CVE-2024-27983</a> to the Node.js AL2023 platform branches.<br /> </td></tr>
  <tr><td><b>Cross-platform updates</b></td><td>Made these cross-platform updates:
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AMI</b></td><td>Updated the base AMI to version 2023.4.20240429.</td></tr>
</tbody>
</table>
</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Node.js</b></td><td><b>Language runtime updates</b><ul><li> Updated Node.js 20 to version <a href="https://nodejs.org/en/blog/release/v20.12.2">20.12.2</a>. </li><li> For Node.js 18, the security updates were backported to the existing <a href="https://nodejs.org/en/blog/release/v18.18.2">18.18.2</a> language release on the platform branch. </li></ul><br />This Node.js update is a security release.<br /><b>Apache HTTP Server</b><ul><li> Updated Apache HTTP Server 2.4 to version 2.4.59. For details, see <a href="https://downloads.apache.org/httpd/CHANGES_2.4.59">Changes with Apache 2.4.59</a> on the <i>Apache Software Foundation</i> website. </li></ul><br />This Apache update is security release.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2024-05-01-al2023-nodejs.platforms"></a>

**Topics**
+ [Node.js](#release-2024-05-01-nodejs-al2023.platforms.nodejs)

### Node.js
<a name="release-2024-05-01-nodejs-al2023.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js 20 AL2023 version 6.1.4** <br /> * 64bit Amazon Linux 2023 v6.1.4 running Node.js 20 *  | 2023.4.20240429 | 20.12.2 (10.5.0)<br /> Default version: 20.12.2 | nginx 1.24.0 (default), Apache 2.4.59 | 2.40.1 | 3.2.0 | 
|  ** Node.js 18 AL2023 version 6.1.4** <br /> * 64bit Amazon Linux 2023 v6.1.4 running Node.js 18 *  | 2023.4.20240429 | 18.18.2 (9.8.1)<br /> Default version: 18.18.2 | nginx 1.24.0 (default), Apache 2.4.59 | 2.40.1 | 3.2.0 | 