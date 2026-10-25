

# Release: Elastic Beanstalk Amazon Linux 2023 platform updates for Node.js 24 and Node.js 22 on October 22, 2026
<a name="release-2026-10-22-al2023-nodejs"></a>

This release provides new versions for AWS Elastic Beanstalk Node.js 24 and Node.js 22 platforms based on Amazon Linux 2023. The release includes security updates. It also includes AMI and Node.js updates.

**Release date:** October 22, 2026

To update your environments to the new platform versions, see [Updating your Elastic Beanstalk environment's platform version](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.platform.upgrade.html) in the *AWS Elastic Beanstalk Developer Guide*. If you've turned on [managed platform updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-platform-update-managed.html), Elastic Beanstalk applies the new platform versions to your environments during their weekly maintenance window.

## Changes
<a name="release-2026-10-22-al2023-nodejs.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/alas2023.html">Amazon Linux Security Center</a> on or before <b>October 21, 2026</b> to the Node.js 24 and Node.js 22 AL2023 platforms.</td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Node.js</b></td><td> <ul><li> Updated Node.js 24 to version <a href="https://nodejs.org/en/blog/release/v24.22.1">24.22.1</a> (npm 11.19.1). </li><li> Updated Node.js 22 to version <a href="https://nodejs.org/en/blog/release/v22.23.4">22.23.4</a> (npm 10.9.9). </li><li> Node.js 24.22.1 and Node.js 22.23.4 are security releases. For details, see the <a href="https://nodejs.org/en/blog/vulnerability/october-2026-security-releases">Node.js October 2026 security releases</a>. </li><li> Updated the base AMI to version 2023.12.20261021. </li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2026-10-22-al2023-nodejs.platforms"></a>

**Topics**
+ [Node.js](#release-2026-10-22-al2023-nodejs.platforms.nodejs)

### Node.js
<a name="release-2026-10-22-al2023-nodejs.platforms.nodejs"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Node.js versions (npm versions)  |  Proxy Server  |  Git  |  AWS X-Ray  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Node.js 24 AL2023 version 6.11.12** <br /> * 64bit Amazon Linux 2023 v6.11.12 running Node.js 24 *  | 2023.12.20261021 | 24.22.1 (11.19.1)<br /> Default version: v24.22.1 | nginx 1.30.5 (default), Apache 2.4.69 | 2.50.1 | 3.7.0 | 
|  ** Node.js 22 AL2023 version 6.11.12** <br /> * 64bit Amazon Linux 2023 v6.11.12 running Node.js 22 *  | 2023.12.20261021 | 22.23.4 (10.9.9)<br /> Default version: v22.23.4 | nginx 1.30.5 (default), Apache 2.4.69 | 2.50.1 | 3.7.0 | 